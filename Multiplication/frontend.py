from tkinter import *

window = Tk()
window.title('Times Table')
window.geometry('400x235')

lable_text = Label(text='Enter a number:')
lable_text.place(x=20, y=20, width=100, height=25)

number_user = Entry(text='')
number_user.place(x=125, y=20, width=120, height=25)

multi_list = Listbox()
multi_list.place(x=125, y=60, width=120, height=150)

button_table = Button(text='View Times Table')
button_table.place(x=260, y=20, width=120, height=25)

button_clear = Button(text='Clear')
button_clear.place(x=260, y=60, width=120, height=25)

if __name__ == '__main__':
    window.mainloop()