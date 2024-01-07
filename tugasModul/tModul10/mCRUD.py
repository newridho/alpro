import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_ridhoo"
)

daftarData = []

def tampilkanMenu():
    print("Pilih Menu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Edit data")
    print("4. Hapus data")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    return pilihan

def insert_data(db):
    cursor = db.cursor()
    npmKamu = input("Masukan NPM kamuu : ")
    namaKamu = input("Masukan Namamu : ")
    prodiKamu = input("Masukan prodimu : ")
    nilaiKamu = input("Masukan Nilai : ")

    sql = "INSERT INTO mahasiswa1 (npm,nama,prodi,nilai) VALUES (%s,%s,%s,%s)"
    val = npmKamu, namaKamu, prodiKamu, nilaiKamu
    cursor.execute(sql,val)
    db.commit()
    
    print("{} data berhasil ditambah".format(cursor.rowcount))

def search_by_npm(db):
    cursor = db.cursor()
    npm_cari = input("Masukkan NPM yang ingin dicari: ")
    
    sql = "SELECT * FROM mahasiswa1 WHERE npm = %s"
    val = (npm_cari,)
    
    cursor.execute(sql, val)
    fetch = cursor.fetchall()

    if not fetch:
        print("Data tidak ditemukan.")
    else:
        for x in fetch:
            print(">>> DATA MAHASISWA <<<")
            print("======================")
            print("NIM                  : ", x[0])
            print("Nama Mahasiswa       : ", x[1])
            print("Program Studi        : ", x[2])
            print("Nilai                : ", x[3])    

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswa1"
    
    cursor.execute(sql)
    fetch = cursor.fetchall()

    for x in fetch:
        print(">>> DATA MAHASISWA <<<")
        print("======================")
        print("NIM                  : ", x[0])
        print("Nama Mahasiswa       : ", x[1])
        print("Program Studi        : ", x[2])
        print("Nilai                : ", x[3])
        # print(x)


def editData(db):
    cursor = db.cursor()
    npmLama = input("Masukkan NPM data yang ingin diubah :")

    npmBaru = input("Masukkan NPM baru : ")
    namaBaru = input("Masukkan Nama baru : ")
    prodiBaru = input("Masukkan Prodi baru : ")
    nilaiBaru = input("Masukkan Nilai baru : ")

    sql = "UPDATE mahasiswa1 SET npm=%s, nama=%s, prodi=%s, nilai=%s WHERE npm=%s"
    val = npmBaru, namaBaru, prodiBaru, nilaiBaru, npmLama
    cursor.execute(sql,val)
    db.commit()

    print("{} data berhasil diubah".format(cursor.rowcount))

def deleteData(db):
    cursor = db.cursor()

    show_data(db)
    nim_dicari = input("Masukkan nim : ")
    sql = "DELETE FROM mahasiswa1 WHERE npm=%s"
    val = (nim_dicari,)
    cursor.execute(sql,val)
    db.commit()

    print ("{} data berhasil dihapus", format(cursor.rowcount))
    print("Data berhasil dihapus")
    

while True:
    pilihan = tampilkanMenu()
    if pilihan == '1':
        insert_data(db)
    elif pilihan == '2':
        search_by_npm(db)
    elif pilihan == '3':
        editData(db)
    elif pilihan == '4':
        deleteData(db)
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")


# deleteData(db)
# editData(db)
# insert_data(db)
# show_data(db)