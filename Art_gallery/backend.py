import sqlite3
from tkinter import *

def last_id():
    db = sqlite3.connect('ArtGallery.db')
    cursor = db.cursor()
    cursor.execute("SELECT ArtistsID FROM Artists")
    list_id = []
    for i in cursor.fetchall():
        list_id.append(i[0])
    cursor.close()
    db.close()
    return max(list_id)

def add_artist():
    db = sqlite3.connect('ArtGallery.db')
    cursor = db.cursor()
    id_set = last_id() + 1
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

'''db = sqlite3.connect('ArtGallery.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
ArtistsID integer PRIMARY KEY,
Name text NOT NULL,
Address text NOT NULL,
Town text,
Country text NOT NULL,
Postcode text NOT NULL);""")
for i in range(1):
    id_set = int(input('Enter the ID: '))
    name_set = input('Enter the full name: ')
    address_set = input('Enter the address: ')
    town_set = input('Enter the town: ')
    country_set = input('Enter the country: ')
    postcode_set = input('Enter the postcode: ')
    cursor.execute("""INSERT INTO Artists(ArtistsID, Name, Address, Town, Country, Postcode)
    VALUES(?, ?, ?, ?, ?, ?)""", (id_set, name_set, address_set, town_set, country_set, postcode_set))
    db.commit()
db.close()'''

window = Tk()
window.title('Art gallery base')
window.geometry('720x600')

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

button_add_artist = Button(text='Add artist', command=add_artist)
button_add_artist.place(x=580, y=70, width=120)

if __name__ == '__main__':
    window.mainloop()