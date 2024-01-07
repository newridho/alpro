l_nama_barang = []
l_qty = []
l_harga_satuan = []

kasir = "Seseorang"
alamat = "SEVENELEVEN Jombor" 

while True:
    nama_barang = input("Nama Barang (q untuk selesai): ")
    if nama_barang == "q":
        break
    qty = int(input('Qty Barang: '))
    harga_satuan =  int(input("Masukan Harga Satuan: "))
    l_nama_barang.append(nama_barang)
    l_qty.append(qty)
    l_harga_satuan.append(harga_satuan)
    
total_per_produk = [a*b for a,b in zip(l_qty, l_harga_satuan)]
total_belanja = sum(total_per_produk)
diskon = 0.1 if total_belanja > 150000 else 0
potongan = total_belanja * diskon
bayar = total_belanja - potongan 
uang = int(input('Masukan Uang Konsumen: '))
kembalian = uang - bayar

tampilStruk = input("Tampilkan Struk (y/t) : ")
if tampilStruk == "y":
    print("=====SEVENELEVEN=====")
    print("Nama Kasir : ", kasir)
    print(alamat)
    print("==============================")
    print("Nama Barang  Jumlah  Harga Satuan")
    for i in range(len(l_nama_barang)):
        print(f"{l_nama_barang[i]}\t\t{l_qty[i]}\t\t{l_harga_satuan[i]}\t{total_per_produk[i]}")

    print(f"Total Bayar: \t\t\t\t {bayar}")    
    print(f"Bayar: \t\t\t\t {uang}")    
    print(f"Kembalian: \t\t\t\t {kembalian}")    
    # print(l_nama_barang, l_qty, l_harga_satuan)

    print("==============================")


print(f"Kembalian : Rp {kembalian:.2f}")