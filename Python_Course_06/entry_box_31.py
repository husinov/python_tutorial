from tkinter import *

def submit():
    username = entry.get()
    print('Hi ' + username + '. Welcome to our Project...')
    entry.config(state = DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()

window.geometry('500x500')
window.title('Nuriddin')

entry = Entry(window,
              font = ('Arial', 20),
              fg = '#44eb60',
              bg = 'black',
              # show = '*',
              # bd = 25
              )
entry.pack(side = 'left')

submit_b = Button(window,
                  text = 'submit',
                  command = submit
                  )
submit_b.pack(side = 'right')

delete_b = Button(window,
                  text = 'delete',
                  command = delete
                  )
delete_b.pack(side = 'right')

backspace.b = Button(window,
                     text = 'backspace',
                     command = backspace
                     )
backspace.b.pack(side = 'right')

window.mainloop()
