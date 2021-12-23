from tkinter import *

def submit():
    print('The temperature is ' + str(scale.get()) + ' degrees C')

window = Tk()

window.title('Temperature')

hot_T = PhotoImage(file = 'img_2.png')
hot_label = Label(window, image = hot_T)
hot_label.pack()

scale = Scale(window,
              from_ = 70,
              to = -30,
              length = 400,
              font = ('Consolas', 15),
              fg = '#0af5a6',
              bg = '#2637f0',
              tickinterval = 10,
              troughcolor = '#00FF00',
              # showvalue = 0,
              )
button = Button(window,
                text = 'submit',
                command = submit)
button.pack(side = 'bottom')

scale.set(0)
scale.pack()

cold_T = PhotoImage(file = 'img_3.png')
cold_label = Label(window, image = cold_T)
cold_label.pack()

window.mainloop()
