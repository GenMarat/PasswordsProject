from tkinter import *

window = Tk()
window.title('Times Table')
window.geometry('400x300')

number_user = Label(text='Enter a number:')
number_user.place(x=20, y=20, width=100, height=25)




if __name__ == '__main__':
    window.mainloop()