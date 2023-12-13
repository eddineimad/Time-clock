from tkinter import *
import random

secret = random.randint(1, 100)

def check_guess():
    guess = int(number.get())
    if guess == secret :
        result_label.config(text="mebreak !!")
    elif guess < secret :
       result_label.config(text="zid chewya !")
    else:
       result_label.config(text="n9as chewya!")
window = Tk()
window.title("guess the number !")

Label (window, text="guess a number between 1 and 100")
number = Entry(window)
number.pack()

Button(window, text="check !", command=check_guess).pack()

result_label = Label(window, text="")
result_label.pack()
window.mainloop()
