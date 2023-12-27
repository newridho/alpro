# Latihan 1
bil = float(input("Masukkan bilangan : "))
hasil = bil % 2

# print(hasil)
if hasil == 0:
    print("Hasil Genap")
else:    
    print("Hasil Ganjil")

print("---------------------------")

# Latihan 2
skor = float(input("Masukkan nilai 0-10: "))
result = skor * 10

if result > 80:
    print("A")
elif result > 60:
    print("B")
elif result > 40:    
    print("C")
elif result > 20:    
    print("D")
else:    
    print("E")

# Latihan 3
bil = float(input("Masukkan Bilangan: "))
hasil = bil % 3

if hasil == 1:
    nilai = float(input("Masukkan Nilai: "))
    r = hasil + nilai
    if r > 50:
        print(r)
    else:
        print('Y')    
else:
    print("X")