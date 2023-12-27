def perkalian(number1, number2):
    # mengkalikan 2 angka
    hasil = number1 * number2
    
    if (hasil % 2 == 0) :
        print(hasil, 'adalah Bilangan Genap')
    else :
        print(hasil, 'adalah Bilangan Ganjil')    
    
    return hasil 