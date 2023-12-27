import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "uty"
)

def create(db):
    cursor = db.cursor()
    lagi = "y"

    while lagi =="y":
        npmBaru = input("Tambahkan NPM : ")
        namaBaru = input("Tambahkan nama Mahasiwa : ")
        prodiBaru = input("Tambahkan Prodi Mahasiswa : ")

        cursor.execute(""" INSERT INTO mahasiswa1(npm, nama, prodi) VALUES(%s, %s, %s)""", (npmBaru, namaBaru, prodiBaru))
        db.commit()
        lagi = input("Tambah data lagi (y/t) : ")

def read(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mahasiswa1")
    
    for x in cursor.fetchall():
        print(x)

create(db)
read(db)        