import sqlite3
from tkinter import *

def last_id(base_name: str, sql_request: str):
    db = sqlite3.connect(base_name)
    cursor = db.cursor()
    cursor.execute(sql_request)
    list_id = []
    for i in cursor.fetchall():
        list_id.append(i[0])
    cursor.close()
    db.close()
    return max(list_id)

def get_data_base(base_name: str, sql_request: str) -> list:
    db = sqlite3.connect(base_name)
    cursor = db.cursor()
    cursor.execute(sql_request)
    list_artist = []
    for i in cursor.fetchall():
        list_artist.append(i[0])
    cursor.close()
    db.close()
    return list_artist

def add_artist(base_data: str):
    db = sqlite3.connect(base_data)
    cursor = db.cursor()
    id_set = last_id(base_data, ARTIST_ID) + 1
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

ARTIST_ID = "SELECT ArtistsID FROM Artists"
PIECE_ID = "SELECT PieceID FROM Pictures"
ARTIST = "SELECT Name FROM Artists"

window = Tk()
window.title('Art gallery base')
window.geometry('720x600')

#Add Artist Group
frame_artist = LabelFrame(text='Add artist')
frame_artist.place(x=10, y=10, height=110, width=700)

name_lable = Label(text='Name')
name_lable.place(x=20, y=30)

address_lable = Label(text='Address')
address_lable.place(x=160, y=30)

town_lable = Label(text='Town')
town_lable.place(x=300, y=30)

country_lable = Label(text='Country')
country_lable.place(x=440, y=30)

postcode_lable = Label(text='Postcode')
postcode_lable.place(x=580, y=30)

name_artist = Entry(text='')
name_artist.place(x=20, y=50, width=120)

address_artist = Entry(text='')
address_artist.place(x=160, y=50, width=120)

town_artist = Entry(text='')
town_artist.place(x=300, y=50, width=120)

country_artist = Entry(text='')
country_artist.place(x=440, y=50, width=120)

postcode_artist = Entry(text='')
postcode_artist.place(x=580, y=50, width=120)

button_add_artist = Button(text='Add artist', command=lambda: add_artist('ArtGallery.db'))
button_add_artist.place(x=580, y=80, width=120)

#Add Picture Group
frame_picture = LabelFrame(text='Add picture')
frame_picture.place(x=10, y=130, height=110, width=700)

artist_lable = Label(text='Artist')
artist_lable.place(x=20, y=150)

artists_list = get_data_base('ArtGallery.db', ARTIST)
artists = StringVar()
artists.set('')
artist_listbox = OptionMenu(window, artists, *artists_list)
artist_listbox.place(x=20, y=168, height=25, width=120)

title_lable = Label(text='Title')
title_lable.place(x=160, y=150)

title = Entry(text='')
title.place(x=160, y=170, width=260)

medium_lable = Label(text='Medium')
medium_lable.place(x=440, y=150)

medium_list = ['Acrylic', 'Ink', 'Oil', 'Watercolour']
medium = StringVar()
medium.set('')
medium_listbox = OptionMenu(window, artists, *medium_list)
medium_listbox.place(x=440, y=168, height=25, width=120)

price_lable = Label(text='Price')
price_lable.place(x=580, y=150)

price = Entry(text='')
price.place(x=580, y=170, width=120)

button_add_picture = Button(text='Add picture')
button_add_picture.place(x=580, y=200, width=120)

if __name__ == '__main__':
    window.mainloop()