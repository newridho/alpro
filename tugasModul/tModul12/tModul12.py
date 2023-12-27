# import random

uh1 = int(input("Masukkan Nilai Ulangan harian 1 : ")) 
uh2 = int(input("Masukkan Nilai Ulangan harian 2 : ")) 
# for x in range
rataUH = (uh1 + uh2) / 2
print("Rata-Rata nilai Ulangan Harian : ", rataUH)

uts = int(input("Masukkan Nilai Ulangan Tengah Semester : ")) 
uas = int(input("Masukkan Nilai Ulangan Akhir Semester : ")) 

totalNilai = (rataUH*30/100)+(uts*30/100)+(uas*40/100)

if totalNilai >= 0 and totalNilai < 20:
    ketNilai = "E"
elif totalNilai >= 20 and totalNilai < 40:
    ketNilai = "D"
elif totalNilai >= 40 and totalNilai < 60:
    ketNilai = "C"
elif totalNilai >= 60 and totalNilai < 80:
    ketNilai = "B"
elif totalNilai >= 80 and totalNilai < 100:
    ketNilai = "A"
    
print("---------Nilai Ke 1--------------------")
print("Nilai Harian : ", uh1)
print("---------Nilai Ke 2--------------------")
print("Nilai Harian : ", uh2)
print("Nilai Ujian Tengah Semester : ", uts)
print("Nilai Ujian Akhir Semester : ", uas)
print("---------Total Nilai--------------------")
print("Total Nilai yang didapat : ", totalNilai)
print("Total Nilai Dalam Huruf : ", ketNilai)