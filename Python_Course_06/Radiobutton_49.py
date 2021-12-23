from tkinter import *

team = ['Real Madrid', 'Barcelona', 'Chelsea']
count_rm = count_fcb = count_chls = 0

def my_team():
    if (x.get() == 0):
        print('I\'m fan of Real Madrid!')
    elif (x.get() == 1):
        print('I\'m fan of FC Barcelona!')
    elif (x.get() == 2):
        print('I\'m fan of Chelsea!')
    else:
        print('What?')
print('Number of fans:')

def count():
    global count_rm, count_fcb, count_chls

    if (x.get() == 0):
        count_rm += 1
    elif (x.get() == 1):
        count_fcb += 1
    elif (x.get() == 2):
        count_chls += 1
    print(f'Real Madrid: {count_rm} Barcelona: {count_fcb} Chelsea:{count_chls}')
    if count_rm + count_fcb + count_chls == 20:
        exit()

window = Tk()
x = IntVar()
RM_image = PhotoImage(file = 'img_5.png')
Barca_image = PhotoImage(file = 'img_6.png')
Chelsea_image = PhotoImage(file = 'img_11.png')
images = [RM_image, Barca_image, Chelsea_image]

for index in range(len(team)):
    radio_b = Radiobutton(window,
                          text = team[index],
                          font = ('Arial', 50),
                          variable = x,
                          value = index,
                          fg = '#0c0c0d',
                          bg = '#37d5ed',
                          activeforeground = '#0c0c0d',
                          activebackground = '#37d5ed',
                          padx = 25,
                          indicatoron = 0,
                          width = 1000,
                          command = count,
                          image = images[index],
                          compound = 'left',
                          # height = 200
                          )
    radio_b.pack(anchor = W)
window.config(background = '#37d5ed')
window.mainloop()
