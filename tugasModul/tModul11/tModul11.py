import math

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

def akar(x):
    return math.sqrt(x)

def pangkat(x, y):
    return x ** y

def kalkulator():
    while True:
        print("Pilih Operasi")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Akar")
        print("6. Pangkat")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan operasi (1/2/3/4/5/6/7): ")

        if pilihan == '1':
            bilangan1 = round(float(input("Masukkan bilangan pertama: ")))
            bilangan2 = round(float(input("Masukkan bilangan kedua: ")))
            print(bilangan1, "+", bilangan2, "=", tambah(bilangan1, bilangan2))
        elif pilihan == '2':
            bilangan1 = round(float(input("Masukkan bilangan pertama: ")))
            bilangan2 = round(float(input("Masukkan bilangan kedua: ")))
            print(bilangan1, "-", bilangan2, "=", kurang(bilangan1, bilangan2))
        elif pilihan == '3':
            bilangan1 = round(float(input("Masukkan bilangan pertama: ")))
            bilangan2 = round(float(input("Masukkan bilangan kedua: ")))
            print(bilangan1, "*", bilangan2, "=", kali(bilangan1, bilangan2))
        elif pilihan == '4':
            bilangan1 = round(float(input("Masukkan bilangan pertama: ")))
            bilangan2 = round(float(input("Masukkan bilangan kedua: ")))
            print(bilangan1, "/", bilangan2, "=", bagi(bilangan1, bilangan2))
        elif pilihan == '5':
            bilangan = round(float(input("Masukkan bilangan: ")))
            print("Akar dari", bilangan, "adalah", akar(bilangan))
        elif pilihan == '6':
            bilangan1 = round(float(input("Masukkan bilangan: ")))
            bilangan2 = round(float(input("Masukkan pangkat: ")))
            print(bilangan1, "pangkat", bilangan2, "adalah", pangkat(bilangan1, bilangan2))
        elif pilihan == '7':
            print("Program selesai. Terima Kasih.")
            break
        else:
            print("Input salah. Silakan masukkan pilihan yang valid.")

kalkulator()
