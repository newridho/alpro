# Modul 
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')         

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')    


mulai = 10
selesai = 1
stop = -1

for i in range(mulai, selesai, stop):
    print(i)


mulai = 10
selesai = 1
stop = -1

for i in range(mulai, selesai, stop):
    print(i)

angka = 1

while angka < 10:
    print(angka)
    angka*=1.5

for baris in range (2):
    for kolom in range (3):
        print('*', end='')
    print('')    

for x in 'UTY-MAHALL':
    if x == '-':
        print('Selesai')
        continue
    print(x)    