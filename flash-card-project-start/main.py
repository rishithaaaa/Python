from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
count = -1
try:
    data = pd.read_csv("data/spanish_words.csv")
except FileNotFoundError as e:
    print(e)
else:
    data = pd.DataFrame.to_dict(data, orient="records")

def display_score():
    right_button.destroy()
    wrong_button.destroy()
    canvas.itemconfig(card_title,text="Score:", font=("Ariel", 30, "italic"), fill="black")
    canvas.itemconfig(card_word, text=f"{count}/10", font=("Ariel", 40, "bold"))

def increment_score():
    global count
    count += 1

def decrement_score():
    global count
    count -= 1

def display_white_card():
    global current_card, flip_timer, count
    if count == 5:
        display_score()
    increment_score()
    window.after_cancel(flip_timer)
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")
    current_card = random.choice(data)
    canvas.itemconfig(card, image=card_white)
    canvas.itemconfig(card_title, text="Spanish", font=("Ariel", 30, "italic"), fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['Spanish']}", font=("Ariel", 40, "bold"), fill="black")
    flip_timer = window.after(3000, func=flip_the_card)


def flip_the_card():
    right_button.config(state="normal")
    wrong_button.config(state="normal")
    canvas.itemconfig(card, image=card_green)
    canvas.itemconfig(card_title, text="English", font=("Ariel", 30, "italic"), fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_the_card)

card_white = PhotoImage(file="images/card_front.png")
card_green = PhotoImage(file="images/card_back.png")

my_image = PhotoImage(file="images/card_front.png")

canvas = Canvas(window, bd=0, highlightthickness=0, width=800, height=526, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card = canvas.create_image(400, 263, image=my_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=lambda: [display_white_card(), increment_score()])
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=lambda: [display_white_card()])
right_button.grid(column=1, row=1)
#
# start_img = PhotoImage(file="images/start.jpeg")
# start_button = Button(image=start_img, command=display_white_card())
# sta
# start_button.place(x=400, y=550)

window.mainloop()


# disable buttons
# ticks ones