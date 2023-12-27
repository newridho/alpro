daftarData = []

def tampilkanMenu():
    print("Pilih Menu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    return pilihan

def tambahData():
    data = {}
    data['nim'] = input("Masukkan nim : ")
    data['nama'] = input("Masukkan nama : ")
    data['asal'] = input("Masukkan asal : ")
    daftarData.append(data)
    print(f"'{data['nama']}' telah ditambahkan ke daftar.")

def tampilkanDaftar():
    if len(daftarData) == 0:
        print("Daftar kosong.")
    else:
        print("Daftar data:")
        for i, data in enumerate(daftarData, 1):
            print(f"data {i}:")
            print(f"Nim: {data['nim']}, Nama: {data['nama']}, Asal: {data['asal']}")
            print("--------------")

def hapus_data():
    tampilkanDaftar()
    if len(daftarData) == 0:
        return

    try:
        indeks = int(input("Masukkan nomor data yang ingin dihapus: "))
        if 1 <= indeks <= len(daftarData):
            dataTerhapus = daftarData.pop(indeks - 1)
            print(f"'{dataTerhapus['nama']}' telah dihapus dari daftar.")
        else:
            print("Nomor data tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor data.")

while True:
    pilihan = tampilkanMenu()
    if pilihan == '1':
        tambahData()
    elif pilihan == '2':
        tampilkanDaftar()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
