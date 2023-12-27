def hitungHurufAngka():
    s = input("Input a string = ")
    a=h=0
    for c in s:
        if c.isdigit():
            a=a+1
        elif c.isalpha():
            h=h+1
        else:
            pass
    print("Huruf = ", h)
    print("Angka = ", a)

def utama():
    print("Program Hitung Angka dan Huruf")
    hitungHurufAngka()
    print("done")    

utama()