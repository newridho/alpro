#task1
# Buatlah program ramalan jodoh kamu dengan output :
# =================================================
import random
# import string

nama = input("masukkan nama : ")
ttl  = input("masukkan tgl lahir : ")
zodiak = ['Virgo', 'Gemini', 'Libra']

print("===== RAMALAN JODOHKU =====")
print("Nama                  : ",nama)
print("Tanggal lahir         : ",ttl)
print("Inisial Jodoh         : ",random.choice(nama))
print("Lahir di tanggal      : ",random.randint(1,31)) 
print("Zodiaknya             : ",random.choice(zodiak)) 

#task 2
# Suatu tim futsal ingin membuat kaos tim. Jamal Kebingungan dan ingin mencari nomor punggung acak berupa angka ganjil dari 1-100. Buatkan program untuk dia menemukan nomor punggung dengan output :
# Nomor punggung keberuntunganmu adalah 1(nomor acak)

print("Nomor punggung keberuntunganmu adalah ", random.randrange(1,100,2))

#task 3
#Anto, Budi, Citra, Devi, Edgar, Faza, Gilang adalah suatu circle yang suka membaca buku. Kemarin mereka membeli buku "Laut Bercerita" dan ingin membacanya secara bergantian sehari sekali dalam satu minggu. Mereka sepakat membuat jadwal membaca dengan mengacak nama di dalam circle dan tidak boleh ada yang membaca dua kali dalam satu minggu. Buatlah program untuk membuat jadwal giliran membaca buku tsb dengan output :

circle = ["Anto", "Budi", "Citra", "Devi", "Edgar", "Faza", "Gilang"]
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
random.shuffle(circle)

for i in range (0,7):
    print(f"Hari {hari[i]}: {circle[i]}")