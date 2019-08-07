# Template soal nomor 1.
from string import ascii_letters, digits
from random import choice, randint
list_password = []
characters = ascii_letters + digits
jalan = True
# Input mau bikin brp password
while jalan:
    passnum = input("Mau bikin brp password?(satu/banyak/exit): ")
    if passnum == "satu":
        while True:
            panjang_pass = input("Passwordnya mau sepanjang apa?(Min=4,Max=20): ")
            if panjang_pass.lower() == "default":
                panjang_pass = 10
                break
            elif panjang_pass.lower() != "default":
                if int(panjang_pass) < 4 or int(panjang_pass) > 20:
                    print("Password tidak sesuai ketentuan, coba lagi!")
                elif panjang_pass.isdigit():    
                    break
                else:
                    print("Password tidak sesuai ketentuan, coba lagi!")
        password =  "".join(choice(characters) for x in range(int(panjang_pass)))
        print(password)
        while True:
            opsi = input("Mau bikin pass lagi?(ketik 'lagi' kalo mau, 'exit' buat keluar): ")
            if opsi.lower() == "lagi":
                break          
            elif opsi.lower() == "exit":
                jalan = False
                break
            else:
                print("input tidak sesuai ketentuan, coba lagi!")
    elif passnum == "banyak":
        while True:
            input_jumlah_pass = int(input("Passwordnya mau sebanyak apa?(Minimal 2): "))
            if input_jumlah_pass < 2:
                print("Password yang diminta kurang dari 2, coba lagi!")
            else:
                break
        while True:
            panjang_minimal = input("Passwordnya minimal sepanjang apa?(Min=4,Max=20): ")
            panjang_maksimal = input("Passwordnya maksimal sepanjang apa?(Min=4,Max=20): ")
            if panjang_minimal.lower() == "default" and panjang_maksimal.lower() == "default":
                panjang_pass = range(8,12)
                break
            else:
                panjang_pass = range(int(panjang_minimal),int(panjang_maksimal))
                break
        while True:
            opsi = input("Passwordnya mau disimpen didalem file atau diprint?(save/print): ")
            if opsi.lower() == "save":
                txt = open("passlist.txt","w")
                for i in range(input_jumlah_pass):
                    password =  "".join(choice(characters) for x in panjang_pass)
                    txt.write(password + "\n")
                print("Password telah dibuat dan disimpan!")
                break
            elif opsi.lower() == "print":
                for i in range(input_jumlah_pass):
                    password =  "".join(choice(characters) for x in panjang_pass)
                    print(password)
                print("Password telah dicetak kelayar!")
                break
            else:
                print("Masukkan perintah dengan benar!")
        while True:
            opsi = input("Mau bikin pass lagi?(ketik 'lagi' kalo mau, 'exit' buat keluar): ")
            if opsi.lower() == "lagi":
                break          
            elif opsi.lower() == "exit":
                jalan = False
                break
            else:
                print("input tidak sesuai ketentuan, coba lagi!")
# Input panjang passwordnya berapa
# Input mau disave kedalam file atau ditampilin langsung ke terminal
# Syntax buat yang save kedalam file: filenya = file(input("Masukkan nama"))