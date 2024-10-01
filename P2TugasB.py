password_benar = "12345"

for attempt in range(3): 
    password = input("Masukkan password: ")
    
    if password == password_benar:
        print("Selamat datang bos!")
        break
    else:
        print("Password salah, coba lagi!")

else:
    print("Terima kasih sudah menggunakan aplikasi kami.")


    