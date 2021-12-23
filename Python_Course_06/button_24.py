from tkinter import *

i = 11
def click():
    global i
    i -=1
    if i == 0:
        print('Work is Done!')
        exit()
    print(i)

mirror = Tk()
b_img = PhotoImage(file = 'img_1.png')

button = Button(mirror,
                text = 'Click it!',
                command = click,
                font = ('Comic Sans', 30),
                fg = '#244ee3',
                bg = '#f5f12c',
                image = b_img,
                compound = 'top',
                activeforeground = '#244ee3',
                activebackground = '#f5f12c',
                state = ACTIVE          #DISABLED -> Will not work
                )

button.pack()
mirror.mainloop()
