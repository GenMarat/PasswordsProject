import  sqlite3

db = sqlite3.connect('ArtGallery.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Pictures(
PieceID integer PRIMARY KEY,
ArtistID integer NOT NULL,
Title text NOT NULL,
Medium text NOT NULL,
Price integer NOT NULL);""")
for i in range(1):
    id_piece = int(input('Enter the ID piece: '))
    id_artist = int(input('Enter the ID artist: '))
    title = input('Enter the title picture: ')
    medium = input('Enter the medium: ')
    price = input('Enter the price: ')

    cursor.execute("""INSERT INTO Pictures(PieceID, ArtistID, Title, Medium, Price)
    VALUES(?, ?, ?, ?, ?)""", (id_piece, id_artist, title, medium, price))
    db.commit()
db.close()