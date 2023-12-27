jumlah_sks = 0
total_nilai = 0

jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

for i in range(jumlah_mata_kuliah):
    sks = int(input(f"Masukkan jumlah SKS mata kuliah ke-{i + 1}: "))
    nilai = float(input(f"Masukkan nilai mata kuliah ke-{i + 1}: "))
    
    kredit = sks * nilai
    
    total_nilai += kredit
    
    jumlah_sks += sks

ipk = total_nilai / jumlah_sks

print(f"Jumlah SKS yang diambil: {jumlah_sks}")
print(f"IPK mahasiswa: {ipk}")