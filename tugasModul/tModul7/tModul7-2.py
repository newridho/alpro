dataTeman = []

def tambahData(nomor):
    teman = input(f"Masukkan teman ke-{nomor}: ")
    dataTeman.append({"Teman": teman})
    print("Data telah ditambahkan.")

def tampilkanData():
    if not dataTeman:
        print("Data kosong.")
    else:
        print(f"Kamu Memiliki {len(dataTeman)} teman.")
        for i, item in enumerate(dataTeman, 1):
            print(f"{i}. teman: {item['Teman']}")

nomor = 1
while True:
    tambahData(nomor)
    
    lagi = input("Tambahkan data lagi? (y/n): ").lower()
    if lagi != "y":
        print("===============")
        tampilkanData()
        break
    nomor += 1