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

def get_data_base(base_name: str, sql_request: str) -> list: #Возврат списка по sql запросу всех значений столбца BD.
    db = sqlite3.connect(base_name)
    cursor = db.cursor()
    cursor.execute(sql_request)
    list_artist = []
    for i in cursor.fetchall():
        list_artist.append(i[0])
    cursor.close()
    db.close()
    return list_artist

def get_artist_id(base_data: str, name: str):
    db = sqlite3.connect(base_data)
    cursor = db.cursor()
    cursor.execute("SELECT ArtistsID FROM Artists WHERE Name=?", [name])
    for i in cursor.fetchall():
        id = int(i[0])
    cursor.close()
    db.close()
    return id

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

def add_picture(base_data: str):
    db = sqlite3.connect(base_data)
    cursor = db.cursor()

    piece_id_get = last_id(base_data, PIECE_ID) + 1
    artist_name_get = str(artists.get())
    artist_id_get = get_artist_id(base_data, artist_name_get)
    title_get = str(title.get())
    medium_get = str(medium.get())
    price_get = int(price.get())

    cursor.execute("""INSERT INTO Pictures(PieceID, ArtistID, Title, Medium, Price)
        VALUES(?, ?, ?, ?, ?)""", (piece_id_get, artist_id_get, title_get, medium_get, price_get))

    title.delete(0, END)
    price.delete(0, END)
    artists.set('')
    medium.set('')
    db.commit()
    cursor.close()
    db.close()

def search_pic_add_listbox(base_name: str): # Запрос по имени, технике исполнения и стоимости. Список выводится в listbox
    db = sqlite3.connect(base_name)
    cursor = db.cursor()
    artists_search = artists.get()
    medium_search = medium.get()
    price_search = price.get()
    list_pictures = []
    if len(artists_search) != 0:
        cursor.execute("""SELECT Pictures.Title FROM Pictures, Artists
WHERE Artists.ArtistsID = Pictures.ArtistID AND Artists.Name=?""", [artists_search])
        for i in cursor.fetchall():
            list_pictures.append(i[0])
    elif len(medium_search) != 0:
        cursor.execute("SELECT Pictures.Title FROM Pictures WHERE Pictures.Medium=?", [medium_search])
        for i in cursor.fetchall():
            list_pictures.append(i[0])
    elif len(price_search) != 0:
        cursor.execute("SELECT Pictures.Title FROM Pictures WHERE Pictures.Price=?", [price_search])
        for i in cursor.fetchall():
            list_pictures.append(i[0])
    search_listbox.delete(0, END)
    price.delete(0, END)
    artists.set('')
    medium.set('')
    cursor.close()
    db.close()
    for i in list_pictures:
        search_listbox.insert(END, i)

def delete_picture(base_name: str):
    file_del = open('ListDelete.txt', 'a')
    db = sqlite3.connect(base_name)
    cursor = db.cursor()
    pic_del = search_listbox.curselection()
    pic_del = search_listbox.get(pic_del)
    list_del = []
    cursor.execute("""SELECT ArtistID, Medium, Price FROM Pictures WHERE Title=?""", [pic_del])
    for i in cursor.fetchall():
        idart_medium_price = i
    idart = str(idart_medium_price[0])
    cursor.execute("""SELECT Artists.Name FROM Pictures, Artists
WHERE Artists.ArtistsID = Pictures.ArtistID AND Artists.ArtistsID=?""", [idart])
    for x in cursor.fetchall():
        name_art = str(x[0])
    write_arсhive = name_art + ',' + pic_del + ',' + str(idart_medium_price[1]) + ',' + str(idart_medium_price[2])
    file_del.write(write_arсhive + '\n')
    cursor.execute("DELETE FROM Pictures WHERE Title=?", [pic_del])
    sel_del = search_listbox.curselection()
    search_listbox.delete(sel_del)
    db.commit()
    cursor.close()
    db.close()

def clear_listbox():
    search_listbox.delete(0, END)

ARTIST_ID = "SELECT ArtistsID FROM Artists"
PIECE_ID = "SELECT PieceID FROM Pictures"
ARTIST = "SELECT Name FROM Artists"

window = Tk()
window.title('Art gallery base')
window.geometry('720x600')

#Add Artist Group--------------------------------------------

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

#Add Picture Group---------------------------------------------------------

frame_picture = LabelFrame(text='Add or search picture')
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
medium_listbox = OptionMenu(window, medium, *medium_list)
medium_listbox.place(x=440, y=168, height=25, width=120)

price_lable = Label(text='Price')
price_lable.place(x=580, y=150)

price = Entry(text='')
price.place(x=580, y=170, width=120)

button_add_picture = Button(text='Add picture', command=lambda: add_picture('ArtGallery.db'))
button_add_picture.place(x=580, y=200, width=120)

#Search Group---------------------------------------------------------

button_search = Button(text='Search', command=lambda: search_pic_add_listbox('ArtGallery.db'))
button_search.place(x=440, y=200, width=120)

frame_picture = LabelFrame(text='Delete')
frame_picture.place(x=10, y=250, height=195, width=700)

search_listbox = Listbox()
search_listbox.place(x=20, y=275, height=150, width=410)

#Delete Picture Group---------------------------------------------------------

button_cleare = Button(text='Clear', command=clear_listbox)
button_cleare.place(x=440, y=275, width=120)

button_delete = Button(text='Delete', command=lambda: delete_picture('ArtGallery.db'))
button_delete.place(x=580, y=275, width=120)

if __name__ == '__main__':
    window.mainloop()