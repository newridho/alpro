import random

circle = ["Anto", "Budi", "Citra", "Devii"]
hari = ["Minggu ke-1", "Minggu ke-2", "Minggu ke-3", "Minggu ke-4"]

print("==== JADWAL MENJAGA CUPANG ====")

for i in range(4):
    yangJaga = random.choice(circle)
    circle.remove(yangJaga)

    sisa = ', '.join(circle) if i < 3 else "Habis"
    print(f"{hari[i]}: {yangJaga}     |      Sisa [{sisa}]")

    if i < 3:
        print()

print("==== SEMANGAT MENJAGA CUPANG! ====")
