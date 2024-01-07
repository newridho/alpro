def tambahBarang(listBarang, qty, hargaSatuan):
    barangBaru = input("Masukkan Nama Barang: ")
    listBarang.append(barangBaru)
    qtyBaru = int(input("Masukkan Jumlah Barang: "))
    qty.append(qtyBaru)
    hargaSatuanbaru = float(input("Masukkan Harga Satuan: "))
    hargaSatuan.append(hargaSatuanbaru)

def totalBayar(qty, hargaSatuan):
    total = [a * b for a, b in zip(qty, hargaSatuan)]
    totalBelanja = sum(total)
    print(f"Total Belanja Anda: {totalBelanja}")

    return total

def main():
    listBarang = []
    qty = []
    hargaSatuan = []

    tambahBarang(listBarang, qty, hargaSatuan)
    totalBayar(qty, hargaSatuan)

    # print("===INDOAPRIL-MART===")

if __name__ == "__main__":
    main()
