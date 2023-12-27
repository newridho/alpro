# OPERATOR ARITMATIKA

# Tambah
nilaiPertama = input("Masukkan Nilai Pertama = ")
nilaiKedua = input("Masukkan Nilai Kedua = ")

pertambahan = int(nilaiPertama) + int(nilaiKedua)
pengurangan = int(nilaiPertama) - int(nilaiKedua)
perkalian = int(nilaiPertama) * int(nilaiKedua)
pembagian = int(nilaiPertama) // int(nilaiKedua)

print("pertambahan = ", pertambahan)
print("pengurangan = ", pengurangan)
print("perkalian = ", perkalian)
print("pembagian = ", pembagian)


# Operator Log
x = True
y = False

hasil = not(x and (not y)) and ((not x) or y)

print(hasil)

nilaiDicari = 12
kumpulanNilai = [5, 6, 1, 3, 2, 7, 8, 9]

hasil = nilaiDicari in kumpulanNilai
print(hasil)


# ------------------------Pertemuan 4--------------------------------------
def printHalo():
    print('Ohayou')

printHalo()

def penjumlahanDua():
    no1 = int(input('Bilangan 1: '))
    no2 = int(input('Bilangan 2: '))

    hasil = no1 + no2

    print(hasil)

penjumlahanDua()    

def luasPersegi():
    sisi = int(input('Masukkan sisi = '))
    hasil = sisi * sisi

    return hasil

print(luasPersegi())   

def lPP():
    P = int(input('Masukkan Panjang = '))
    L = int(input('Masukkan Lebar = '))
    hasil = P * L

    return hasil

print(lPP())   

def duaBil(nilai1, nilai2):

    # Proses
    hasil = nilai1 * nilai2
    # Output
    print(hasil)

nilai1 = int(input('Masukkan Nilai 1 = '))   
nilai2 = int(input('Masukkan Nilai 2 = '))   
duaBil(nilai1, nilai2)






