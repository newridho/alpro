import datetime

def tampilMenu(menu):
    print("Daftar Menu:")
    for i, (nama_menu, harga) in enumerate(menu.items(), 1):
        print(f"{i}. {nama_menu} - Rp.{harga}")

def pesanan(menu):
    makananDipilih = []
    totalHarga = 0

    while True:
        try:
            choice = int(input("\nPilih nomor menu yang ingin dipesan (0 untuk selesai): "))
            if choice == 0:
                break
            elif choice < 0 or choice > len(menu):
                print("Pilihan tidak valid. Silakan pilih nomor menu yang benar.")
            else:
                selected_item = list(menu.keys())[choice - 1]
                qty = int(input(f"Masukkan jumlah {selected_item} yang ingin dipesan: "))
                if qty < 0:
                    print("Jumlah tidak boleh negatif.")
                else:
                    subtotal = menu[selected_item] * qty
                    makananDipilih.append((selected_item, qty, subtotal))
                    totalHarga += subtotal

                    print(f"{selected_item} sebanyak {qty} buah ditambahkan ke dalam pesanan.")
        except ValueError:
            print("Masukkan nomor menu yang valid.")

    return makananDipilih, totalHarga

def pesanMinum(mMinuman):
    minumanDipilih = []
    totalHargaMinuman = 0

    while True:
        try:
            choice = int(input("\nPilih nomor minuman yang ingin dipesan (0 untuk selesai): "))
            if choice == 0:
                break
            elif choice < 0 or choice > len(mMinuman):
                print("Pilihan tidak valid. Silakan pilih nomor minuman yang benar.")
            else:
                selected_drink = list(mMinuman.keys())[choice - 1]
                qty = int(input(f"Masukkan jumlah {selected_drink} yang ingin dipesan: "))
                if qty < 0:
                    print("Jumlah tidak boleh negatif.")
                else:
                    subtotal = mMinuman[selected_drink] * qty
                    minumanDipilih.append((selected_drink, qty, subtotal))
                    totalHargaMinuman += subtotal

                    print(f"{selected_drink} sebanyak {qty} buah ditambahkan ke dalam pesanan.")
        except ValueError:
            print("Masukkan nomor minuman yang valid.")

    return minumanDipilih, totalHargaMinuman

def generate_receipt(namaPelanggan, makananDipilih, totalHarga, minumanDipilih, totalHargaMinuman, uang_bayar):
    totalBayar = totalHarga + totalHargaMinuman
    kembalian = uang_bayar - totalBayar

    print("==================================================")
    print("================ S T R U K =======================")
    print("==================================================")
    print(f"=== Nama: {namaPelanggan}")
    print(f"=== Makanan:")
    for item, qty, subtotal in makananDipilih:
        print(f"===           {item} - {qty} buah")

    print(f"=== Minuman:")
    for drink, qty, subtotal in minumanDipilih:
        print(f"===           {drink} - {qty} buah")

    print(f"=== Total harga (Makanan): Rp.{totalHarga:,.2f}")
    print(f"=== Total harga (Minuman): Rp.{totalHargaMinuman:,.2f}")
    print(f"=== Total harga pesanan: Rp.{totalBayar:,.2f}")
    print(f"=== Uang bayar: Rp.{uang_bayar:,.2f}")
    print(f"=== Kembalian: Rp.{kembalian:,.2f}")
    print(f"=== Waktu pemesanan: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("==================================================")
    print("==================================================")

if __name__ == "__main__":
    menu = {
        "Mi goreng": 10000,
        "Martabak": 45000,
        "Nasi padang": 10000,
        "Ayam geprek": 15000,
        "Sushi": 60000,
    }

    mMinuman = {
        "Air mineral": 5000,
        "Es teh": 7000,
        "Es jeruk": 8000,
        "Jus alpukat": 12000,
        "Kopi": 10000,
    }

    namaPelanggan = input("Nama pelanggan: ")

    tampilMenu(menu)
    makananDipilih, totalHarga = pesanan(menu)

    tampilMenu(mMinuman)
    minumanDipilih, totalHargaMinuman = pesanMinum(mMinuman)

    uang_bayar = int(input("\nMasukkan uang yang dibayarkan: "))

    generate_receipt(namaPelanggan, makananDipilih, totalHarga, minumanDipilih, totalHargaMinuman, uang_bayar)
