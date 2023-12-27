def password():
    user = input("User-nya =")
    passw = input("Password-nya =")
    usernameDb = "root"
    passwordDb = "root"
    if user == usernameDb :
        if passw == passwordDb :
            print("Username dan Password cocok")
        else :
            print("Password salah")
    else :
        print("Username tidak terdaftar") 

password()