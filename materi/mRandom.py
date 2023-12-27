import random
import os
os.system('cls')

print("Bilangan desimal acak dari 0 sampai 1 : ", random.random())

print("Bilangan desimal acak dari 5 sampai 10 : ", random.uniform(5,10))

print("Bilangan bulat acak dari 5 sampai 10 : ", random.randint(5,10))

print("Bilangan bulat genap acak dari 5 sampai 10 : ", random.randrange(2,10,2))

huruf = ['A', 'B', 'C', 'D']
random.shuffle(huruf)

print("Urutan acak huruf adalah", huruf)

print("Bilangan acak dari 0 sampai 100 :", random.choice(range(0,100)))

random.seed(1)
print("Bilangan desimal acak setelah seed 1 :", random.random())
random.seed(2)
print("Bilangan desimal acak setelah seed 2 :", random.random())