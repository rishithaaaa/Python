from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    import random
    import array
    MAX_LEN = 12

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)


    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

        # print out password
    password_entry.delete(0, END)
    set_pass(password)

def set_pass(pas):
    password_entry.insert(0, pas)

def find_password():
    website_value = website_entry.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError or KeyError:
        messagebox.showinfo(message="No data is found to search")
    else:
        if website_value in data:
            email = data[website_value]['email']
            loaded_pass = data[website_value]["password"]
            messagebox.showinfo(title="Credentials!", message=f"Email: {email}\nPassword: {loaded_pass}")
        else:
            messagebox.showwarning(title="No data found", message="No data exists for the website you mentioned")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global data
    website_input = website_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()

    new_data = {
        website_input: {
            "email": username_input,
            "password": password_input
        }
    }
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please make sure to fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered:\n\nEmail/Username: {username_input}\nPassword: {password_input}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# window.minsize(240, 240)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=31)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=2, row=1)


username = Label(text="Email/Username:")
username.grid(column=0, row=3, pady=10)

username_entry = Entry(width=50)
username_entry.grid(column=1, row=3, columnspan=2)
username_entry.insert(0, "demo@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=4)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=4, pady=5, columnspan=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=4)

add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, row=5, columnspan=3)
window.mainloop()