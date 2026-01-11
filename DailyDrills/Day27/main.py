from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

def clicked():
    my_label["text"] = entry.get()

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.grid(row=0,column=0)

button = Button(text="ClickMe", command=clicked)
button.grid(row=1,column=1)

button = Button(text="ClickMe", command=clicked)
button.grid(row=2,column=0)

# Entry
entry = Entry(width=10)
entry.grid(row=3,column=4)




window.mainloop()