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
    nim = input("Masukan NPM kamuu : ")
    nama = input("Masukan Nama kamuu : ")
    prodi = input("Masukan prodi kamuu : ")
    matkul = input("Masukan Mata Kuliah kamuu : ")
    nilaiUH1 = int(input("Masukkan Nilai Ulangan harian 1 : ")) 
    nilaiUH2 = int(input("Masukkan Nilai Ulangan harian 2 : ")) 
    nilaiUTS = int(input("Masukkan Nilai Ulangan Tengah Semester : ")) 
    nilaiUAS = int(input("Masukkan Nilai Ulangan Akhir Semester : ")) 

    jmlUH = nilaiUH1 +nilaiUH2
    rataUH = jmlUH / 2
    print("Rata-Rata nilai Ulangan Harian : ", rataUH)

    akhirUH = 0.3*rataUH
    akhirUTS = 0.3*nilaiUTS
    akhirUAS = 0.4*nilaiUAS
    totalNilai = round(akhirUH+akhirUTS+akhirUAS)

    if totalNilai >= 0 and totalNilai < 20:
        nilaiHuruf = "E"
    elif totalNilai >= 20 and totalNilai < 40:
        nilaiHuruf = "D"
    elif totalNilai >= 40 and totalNilai < 60:
        nilaiHuruf = "C"
    elif totalNilai >= 60 and totalNilai < 80:
        nilaiHuruf = "B"
    elif totalNilai >= 80 and totalNilai < 100:
        nilaiHuruf = "A"

    sql = "INSERT INTO mahasiswa2 (nim_mhs,nama_mhs,prodi_mhs,mk_mhs,nilai_uh1,nilai_uh2,nilai_uts,nilai_uas,total_nilai,nilai_huruf) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = nim, nama, prodi, matkul, nilaiUH1, nilaiUH2, nilaiUTS, nilaiUAS, totalNilai, nilaiHuruf
    cursor.execute(sql,val)
    db.commit()
    
    print("{} data berhasil ditambahkan coyy".format(cursor.rowcount))

#menampilkan data sesuai nim
def search_by_nim(db):
    cursor = db.cursor()
    nimCari = input("Masukkan NPM yang ingin dicari: ")
    
    sql = "SELECT * FROM mahasiswa2 WHERE nim_mhs = %s"
    val = (nimCari)
    
    cursor.execute(sql, (val,))
    fetch = cursor.fetchall()

    if not fetch:
        print("Data tidak ditemukan.")
    else:
        for data in fetch:
            print(">>> DATA MAHASISWA <<<")
            print("======================")
            print("NIM                              : ", data[0])
            print("Nama Mahasiswa                   : ", data[1])
            print("Program Studi                    : ", data[2])
            print("Mata Kuliah                      : ", data[3])
            print("Nilai Ulangan Harian 1           : ", data[4])    
            print("Nilai Ulangan Harian 2           : ", data[5])    
            print("Nilai Ulangan Tengah Semester    : ", data[6])    
            print("Nilai Ulangan Akhir Semester     : ", data[7])    
            print("Total Nilai                      : ", data[8])    
            print("Keterangan Nilai                 : ", data[9])    

#menampilkan data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswa2"
    cursor.execute(sql)
    fetch = cursor.fetchall()

    for data in fetch:
        print(">>> DATA MAHASISWA <<<")
        print("======================")
        print("NIM                              : ", data[0])
        print("Nama Mahasiswa                   : ", data[1])
        print("Program Studi                    : ", data[2])
        print("Mata Kuliah                      : ", data[3])
        print("Nilai Ulangan Harian 1           : ", data[4])    
        print("Nilai Ulangan Harian 2           : ", data[5])    
        print("Nilai Ulangan Tengah Semester    : ", data[6])    
        print("Nilai Ulangan Akhir Semester     : ", data[7])    
        print("Total Nilai                      : ", data[8])    
        print("Keterangan Nilai                 : ", data[9])


def editData(db):
    cursor = db.cursor()
    nimLama = input("Masukkan data NIM yang ingin diubah :")
    
    nimBaru = input("Masukan NPM kamuu : ")
    namaBaru = input("Masukan Nama kamuu : ")
    prodiBaru = input("Masukan prodi kamuu : ")
    matkulBaru = input("Masukan Mata Kuliah kamuu : ")
    nilaiUH1Baru = int(input("Masukkan Nilai Ulangan harian 1 : ")) 
    nilaiUH2Baru = int(input("Masukkan Nilai Ulangan harian 2 : ")) 
    nilaiUTSBaru = int(input("Masukkan Nilai Ulangan Tengah Semester : ")) 
    nilaiUASBaru = int(input("Masukkan Nilai Ulangan Akhir Semester : ")) 

    
    jmlUH = nilaiUH1Baru + nilaiUH2Baru
    rataUH = jmlUH / 2

    akhirUH = 0.3*rataUH
    akhirUTS = 0.3*nilaiUTSBaru
    akhirUAS = 0.4*nilaiUASBaru
    totalNilaiBaru = round(akhirUH+akhirUTS+akhirUAS)

    if totalNilaiBaru >= 0 and totalNilaiBaru < 20:
        nilaiHurufBaru = "E"
    elif totalNilaiBaru >= 20 and totalNilaiBaru < 40:
        nilaiHurufBaru = "D"
    elif totalNilaiBaru >= 40 and totalNilaiBaru < 60:
        nilaiHurufBaru = "C"
    elif totalNilaiBaru >= 60 and totalNilaiBaru < 80:
        nilaiHurufBaru = "B"
    elif totalNilaiBaru >= 80 and totalNilaiBaru < 100:
        nilaiHurufBaru = "A"

    sql = "UPDATE mahasiswa2 SET nim_mhs=%s, nama_mhs=%s, prodi_mhs=%s, mk_mhs=%s, nilai_uh1=%s, nilai_uh2=%s, nilai_uts=%s, nilai_uas=%s, total_nilai=%s, nilai_huruf=%s WHERE nim_mhs=%s"
    val = nimBaru,namaBaru,prodiBaru,matkulBaru,nilaiUH1Baru,nilaiUH2Baru,nilaiUTSBaru,nilaiUASBaru,totalNilaiBaru,nilaiHurufBaru, nimLama
    cursor.execute(sql,val)
    db.commit()

    print("{} data berhasil diubah".format(cursor.rowcount))

def deleteData(db):
    cursor = db.cursor()

    show_data(db)
    nim_dicari = input("Masukkan nim : ")
    sql = "DELETE FROM mahasiswa2 WHERE nim_mhs=%s"
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
        search_by_nim(db)
    elif pilihan == '3':
        editData(db)
    elif pilihan == '4':
        deleteData(db)
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")