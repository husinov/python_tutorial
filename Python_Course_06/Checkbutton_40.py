from tkinter import *

def check_it():
    if (x.get() == 1):
        print('You are agree')
    else:
        print('You are disagree')

window = Tk()
x = IntVar()

img = PhotoImage(file = 'img_4.png')
window.geometry('375x211')
check = Checkbutton(window,
                    text = 'Are you agree?',
                    font = ('Arial', 30),
                    variable = x,
                    command = check_it,
                    onvalue = 1,
                    offvalue = 0,
                    fg = '#00FF00',
                    bg = 'black',
                    activeforeground = '#00FF00',
                    activebackground = 'black',
                    image = img,
                    compound = 'center',
                    # state = ACTIVE
                    )

check.pack()

window.mainloop()
