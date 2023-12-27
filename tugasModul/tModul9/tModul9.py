import random

minNum = 1
maxNum = 10
maxKesempatan = 3

for kesempatan in range(1, maxKesempatan + 1):
    aku = int(input("Masukkan angka tebakan anda = "))
    x = random.randint(minNum, maxNum)

    if aku == x:
        print("Anda Menang")
        break
    else:
        if kesempatan < maxKesempatan:
            print(f"Coba lagi coyy, kesempatan {maxKesempatan - kesempatan} lagi.")
        else:
            print("Angka sebenarnya adalah", x)
            print("Kesempatan habis, Anda kalah.")
