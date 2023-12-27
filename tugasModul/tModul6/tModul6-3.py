banyak_ganjil = 0
banyak_genap = 0

rangkaian_bilangan = ("1 2 3 4 5 6 7 8 9")
bilangan_list = rangkaian_bilangan.split()

for bilangan in bilangan_list:
    bilangan = int(bilangan) 
    
    if bilangan % 2 == 0:
        banyak_genap += 1
    else:
        banyak_ganjil += 1

print("Banyaknya bilangan ganjil:", banyak_ganjil)
print("Banyaknya bilangan genap:", banyak_genap)