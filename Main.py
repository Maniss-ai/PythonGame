from tkinter import *
import tkinter.font as tkFont
import pyttsx3 as py


top = Tk()
top.title("Memory Puzzle Game")
top.geometry("450x300")
top.config(background = "gray")

def fun():
    print(var.get())

var = IntVar()
top.geometry("400x400")

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
# the label for user_name
# py.speak("Please, Enter you username  ")
user_name = Label(top, text="Username", ).place(x=40, y=60)
# the label for user_password

# py.speak("Please, Enter your Age   ")
Age = Label(top, text="Age").place(x=40, y=100)

user_name_input_area = Entry(top, width=30).place(x=110, y=60)
Age_entry_area = Entry(top, width=30).place(x=110, y=100)

# py.speak("Please, click on the radio button as per your gender   ")
Radiobutton(top, text = "Male", value = 1, variable = var, width = 7).place(x=153, y=140)
Radiobutton(top, text = "Female", value = 2, variable = var, width = 8).place(x=149, y=170)
# Button(top, text = "Check", command = fun, bitmap = "info").place(x=140, y=240)

# py.speak("Please on submit button if you want to start this interesting game")
submit_button = Button(top, text="Submit", height = 3, width = 15, command = top.destroy).place(x=135, y=210)

top.mainloop()
import app
app.main()
