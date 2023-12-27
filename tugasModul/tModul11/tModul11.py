#fungsi penjumiahan
def Tambah(x, y):
    return x + y

#fungsi pengurangan 
def Kurang(x, y):
    return x-y

#fungsi perkalian
def Kali(x, y):
    return x*y

#fungsi pembagian
def Bagi(x, y):
    return x/y

def kalkulator():

    #Menu
    print ("Pilih Operasi")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")
    print("5.Keluar")
    #Meminta input dari pengguna
    pilihan = input("Masukkan pilihan operasi (1/2/3/4/5): ")

    if pilihan == '1': 
        bilanganl = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        print (bilanganl,"+", bilangan2, "=", Tambah (bilanganl, bilangan2))
    elif pilihan == '2':
        bilanganl = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int (input("Masukkan bilangan kedua: "))
        print(bilanganl,"-", bilangan2, "=", bilangan2)
        Kurang(bilanganl,bilangan2)
    elif pilihan == '3':
        bilanganl = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int (input("Masukkan bilangan kedua: "))
        print(bilanganl,"*", bilangan2, "=", bilangan2)
        Kali(bilanganl,bilangan2)
    elif pilihan == '4':
        bilanganl = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int (input("Masukkan bilangan kedua: "))
        print(bilanganl,"/", bilangan2, "=", bilangan2)
        Bagi(bilanganl,bilangan2)
    elif pilihan == '5':
        print("program selesai. Terima Kasih")
        exit

    else: print("Input salah")

kalkulator()