import sqlite3
from tkinter import *

def last_id(base_data: str):
    db = sqlite3.connect(base_data)
    cursor = db.cursor()
    cursor.execute("SELECT ArtistsID FROM Artists")
    list_id = []
    for i in cursor.fetchall():
        list_id.append(i[0])
    cursor.close()
    db.close()
    return max(list_id)

def add_artist(base_data: str):
    db = sqlite3.connect(base_data)
    cursor = db.cursor()
    id_set = last_id(base_data) + 1
    name_set = name_artist.get()
    address_set = address_artist.get()
    town_set = town_artist.get()
    country_set = country_artist.get()
    postcode_set = postcode_artist.get()
    cursor.execute("""INSERT INTO Artists(ArtistsID, Name, Address, Town, Country, Postcode)
        VALUES(?, ?, ?, ?, ?, ?)""", (id_set, name_set, address_set, town_set, country_set, postcode_set))
    name_artist.delete(0, END)
    address_artist.delete(0, END)
    town_artist.delete(0, END)
    country_artist.delete(0, END)
    postcode_artist.delete(0, END)
    db.commit()
    db.close()

window = Tk()
window.title('Art gallery base')
window.geometry('720x600')

name_lable = Label(text='Name')
name_lable.place(x=20, y=20)

address_lable = Label(text='Address')
address_lable.place(x=160, y=20)

town_lable = Label(text='Town')
town_lable.place(x=300, y=20)

country_lable = Label(text='Country')
country_lable.place(x=440, y=20)

postcode_lable = Label(text='Postcode')
postcode_lable.place(x=580, y=20)

name_artist = Entry(text='')
name_artist.place(x=20, y=40, width=120)

address_artist = Entry(text='')
address_artist.place(x=160, y=40, width=120)

town_artist = Entry(text='')
town_artist.place(x=300, y=40, width=120)

country_artist = Entry(text='')
country_artist.place(x=440, y=40, width=120)

postcode_artist = Entry(text='')
postcode_artist.place(x=580, y=40, width=120)

button_add_artist = Button(text='Add artist', command=lambda: add_artist('ArtGallery.db'))
button_add_artist.place(x=580, y=70, width=120)

if __name__ == '__main__':
    window.mainloop()