for x in range(1, 101):
    if x % 2 == 0:
        print(x, "adalah bilangan genap")
    else:  
        print(x, "adalah bilangan ganjil")  

# task 1
jumlahGanjil = 0
for x in range (1, 100):
    if x % 2 == 1:
        jumlahGanjil+=1
        
print("Jumlah bilangan ganjil dari 1 - 100 ada", jumlahGanjil)   

#task 2
jumlahHuruf = 0
kalimat = input("Masukkan kalimat = ")
for y in kalimat:
    if y == " ":
        continue
    jumlahHuruf+=1
    
print( "Jumlah Huruf dalam kalimat",kalimat,"adalah",jumlahHuruf,"huruf")      