from tkinter import *

contain = Tk()
contain.title('Nuriddin')
contain.geometry('500x500')

image = PhotoImage(file = 'img.png')
cool = Label(contain,
             text = 'This is Tiger',
             font = ('TimesNewRoman', 20, 'italic'),
             fg = '#f51137',
             bg = '#6ff27d',
             image = image,
             compound = 'center'
             )

cool.place(x=50,y=50)

contain.mainloop()
