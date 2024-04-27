from tkinter import *


def miles_to_kms():
    miles = float(input_box.get())
    km = round(miles * 1.609)
    kms_answer_label.config(text=f"{km}")


window = Tk()
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

input_box = Entry(width=7,)
input_box.grid(column=1, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kms_answer_label = Label(text="0")
kms_answer_label.grid(column=1, row=1)

kms_label = Label(text="Km")
kms_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_kms)
calculate.grid(column=1, row=2)


window.mainloop()
