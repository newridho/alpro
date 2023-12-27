print("~Tugas 1")
print("Memilah bilangan terbesar")

bilA = int(input("Masukkan bilangan A = "))
bilB = int(input("Masukkan bilangan B = "))
bilC = int(input("Masukkan bilangan C = "))
if bilA > bilB:
    print(bilA)
elif bilB > bilC:
    print(bilB)
else :
    print(bilC)

print("~Tugas 2")

def coba(Angka1, Angka2):
    nilai = Angka1+Angka2
    if nilai >= 80:
        print("Nilainya A")
    elif nilai >= 70:
        print("Nilainya B")
    elif nilai >= 60:
        print("Nilainya C")
    elif nilai >= 50:
        print("Nilainya D")
    else :
        print("Nilainya E")
    
    return Angka1 , Angka2

Angka1 = int(input("Masukkan Angka Pertama = "))
Angka2 = int(input("Masukkan Angka Kedua = "))

print(coba(Angka1, Angka2))