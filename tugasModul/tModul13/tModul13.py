def tambahBarang(listBarang, qty, hargaSatuan):
    while True:        
        barangBaru = input("Masukkan Nama Barang (q untuk keluar): ")
        if barangBaru.lower() == "q":
            break
        qtyBaru = int(input("Masukkan Jumlah Barang : "))
        hargaSatuanBaru = float(input("Masukkan Harga Satuan : "))
        listBarang.append(barangBaru)
        qty.append(qtyBaru)
        hargaSatuan.append(hargaSatuanBaru)

def totalBayar(qty, hargaSatuan):
    totalPerProduk = [a * b for a, b in zip(qty, hargaSatuan)] 
    totalBelanja = sum(totalPerProduk)

    diskon, potongan, totalDiskon = cekDiskon(totalBelanja)

    bayar = round(totalBelanja - totalDiskon)
    uang = round(int(input("Masukkan uang konsumen: ")))
    kembalian = round(uang - bayar)

    print(f"Total Belanja Anda: {totalBelanja}")
    
    return totalBelanja, totalPerProduk, bayar, uang, kembalian, totalDiskon

def cekDiskon(totalBelanja):
    diskon = 0.1 if totalBelanja > 150000 else 0
    potongan = totalBelanja * diskon

    return diskon, potongan, potongan

def tampilStrukBelanja(listBarang, qty, hargaSatuan, totalPerProduk, bayar, uang, kembalian, totalDiskon):
    tampilStruk = input("Tampilkan Struk (y/t) : ")
    if tampilStruk.lower() == "y":
        print("======INDOAPRIL-MART========")
        print("============================")
        print(f"Nama Barang \t Jumlah \t Harga Satuan \t Total")
        for i in range(len(listBarang)):
            print(f"{listBarang[i]}\t\t{qty[i]}\t\t{hargaSatuan[i]}\t\t{totalPerProduk[i]}")
    
    print("============================")    
    print(f"Total Bayar : \t\t\t {round(bayar)}")    
    print(f"Bayar       : \t\t\t\t {round(uang)}")    
    print(f"Kembalian   : \t\t\t {round(kembalian)}")
    print(f"Diskon      : \t\t\t {round(totalDiskon)}")
    print("============================")    

def main():
    listBarang = []
    qty = []
    hargaSatuan = []

    tambahBarang(listBarang, qty, hargaSatuan)
    totalBelanja, totalPerProduk, bayar, uang, kembalian, totalDiskon = totalBayar(qty, hargaSatuan)
    tampilStrukBelanja(listBarang, qty, hargaSatuan, totalPerProduk, bayar, uang, kembalian, totalDiskon)

if __name__ == "__main__":
    main()
