#Cara Lain

nilaiHarian2 = float(input("Masukkan Nilai Harian pertama : "))
nilaiHarian2 = float(input("Masukkan Nilai Harian Kedua : "))
nilaiUTS = float(input("Masukan Nilai UTS : "))
nilaiUAS = float(input("Masukkan Nilai UAS : "))

#Proses
rata_rataNilaiHarian= nilaiHarian2+nilaiHarian2
hasilRataRata = rata_rataNilaiHarian/2
#persenan
akhir = 0.3*hasilRataRata
akhirUTS = 0.3*nilaiUTS
akhirUAS = 0.4*nilaiUAS
nilai_hasil = akhir+akhirUTS+akhirUAS

#NIlai Huruf

#Output


print("==== Nilai ke 1 ====")
print("Nilai Harian 1 :", nilaiHarian2)
print("==== Nilai Harian 2====")
print("Nilai Harian 2 : ", nilaiHarian2)
print("Nilai UTS : ",nilaiUTS)
print("Nilai UAS : ",nilaiUAS)
print("Rata rata nilai harian : ",hasilRataRata)
print("Rata rata nilai UTS : ",nilaiUTS)
print("Rata rata nilai UAS : ",nilaiUAS)
print("==== nilai Akhir ====")
print("Total Nilai yang didapat :",nilai_hasil)

if nilai_hasil >= 80:
    print("Total Nilai dalam huruf : A")
elif nilai_hasil >= 60:
    print("Total Nilai dalam huruf : B")
elif nilai_hasil >= 40:
    print("Total Nilai dalam huruf : C")
elif nilai_hasil >= 20:
    print("Total Nilai dalam huruf : D")
elif nilai_hasil >= 0:
    print("Total Nilai dalam huruf : E")