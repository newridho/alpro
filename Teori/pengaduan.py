def ajukan_pengaduan(pengaduan_list):
    pengaduan_baru = input("Masukkan pengaduan: ")
    pengaduan_list.append(pengaduan_baru)
    print("Pengaduan berhasil diajukan.")

def tampilkan_pengaduan(pengaduan_list, index=0):
    if index == len(pengaduan_list):
        print("\nSemua pengaduan:")
        for i, pengaduan in enumerate(pengaduan_list, start=1):
            print(f"{i}. {pengaduan}")
        return
    else:
        print(f"{index + 1}. {pengaduan_list[index]}")
        tampilkan_pengaduan(pengaduan_list, index + 1)

def main():
    pengaduan_list = [
        [1, "Jalan Rusak Parah"],
        [2, "Pohon Tumbang"],
        [3, "Macet Parah"]
    ]
    
    while True:
        print("\nMenu:")
        print("1. Ajukan Pengaduan")
        print("2. Tampilkan Pengaduan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            ajukan_pengaduan(pengaduan_list)
        elif pilihan == "2":
            tampilkan_pengaduan(pengaduan_list)
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
