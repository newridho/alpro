# # Harga per Jam
harga = 5000
bilik1= 4
bilik2 = 4
bilik3 = 4
hargaBilik1 = int(harga) * int(bilik1)
hargaBilik2 = int(harga) * int(bilik1)
hargaBilik3 = int(harga) * int(bilik1)
uangSiti = (bilik1 + bilik2 + bilik3) * 5000
print('TotalBilik 1 = ', hargaBilik1) 
print('TotalBilik 2 = ', hargaBilik2) 
print('TotalBilik 3 = ', hargaBilik3)
print('uangSiti = ', uangSiti) 

# Inisialisasi list untuk menyimpan data
data = []

# Fungsi untuk menambahkan data ke dalam list
def tambah_data(nomor):
    teman = input(f"Masukkan teman ke-{nomor}: ")
    data.append({"Teman": teman})
    print("Data telah ditambahkan.")

# Fungsi untuk menampilkan data
def tampilkan_data():
    if not data:
        print("Data kosong.")
    else:
        print(f"Kamu Memiliki {len(data)} teman.")
        for i, item in enumerate(data, 1):
            print(f"{i}. teman: {item['Teman']}")

# Program utama
nomor = 1
while True:
    tambah_data(nomor)
    
    lagi = input("Tambahkan data lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        print("===============")
        tampilkan_data()
        break
    nomor += 1