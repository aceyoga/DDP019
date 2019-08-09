# Template soal nomor 2.
import os

daftar_menu = []
review = ["Eneg","Biasa","Enak"]
kas = 1000000000
jalan = True
input_file = open(input("Masukkan nama file(Usahakan program ini dan file txtnya dalam satu folder): "),"r")
rtxt = input_file.readlines()
for i in range(len(rtxt)):
   split1 = rtxt[i].split("\n")
   split1.pop(-1)
   split2 = split1[0].split(",")
   submenu = [i+1]
   submenu.extend(split2)
   daftar_menu.append(submenu)

while jalan:
   list_pesanan = []
   # Sebelum meminta input pesanan, kasirnya tanyain dulu mau nginput pesanan atau ngga, kalo ngga berarti programnya diakhiri.
   while True:
      opsi = input("Anda mau membayar atau keluar?(bayar/exit): ")
      if opsi == "exit":
         exit()
      elif opsi == "bayar":
         break
      else:
         print("Input anda salah, coba lagi!")
   # Spesifikasi 2
   # Program akan meminta input makanan/minuman yang dipesan. Sebelum meminta input, program menampilkan daftar menunya dulu.
   for consumables in daftar_menu:
      print(str(consumables[0])+".","Nama:",consumables[1],", Harga:",consumables[2])
   # Input pesanan disini. Ingat bahwa konsumen bisa memesan lebih dari 1 makanan/minuman. Hint: while True bisa disetop
   while True:
      input_pesanan = input("Masukkan pesanan anda: ")
      if input_pesanan == "exit":
         break
      else:
         list_pesanan.append(input_pesanan)
   harga_pesanan = 0
   for pesanan in list_pesanan:
      for menunya in daftar_menu:
         if pesanan == menunya[1]:
            harga_pesanan += int(menunya[2])
            break
         else:
            continue
   # Setelah meminta input, program mencetak total harga pesanan, lalu meminta input uang pembayaran oleh pelanggan.
   print(list_pesanan)
   print("Harga pesanan anda adalah {} rupiah.".format(harga_pesanan))
   # Hint: Spesifikasi 4 ini memiliki kondisional tergantung bintang yang ingin kalian dapatkan.
   # Hint 2: Uang yang masuk itu dimasukin kedalam kas dulu, dan kembalian ambilnya dari kas juga :D
   # Ini solusi bintang 7.
   ngitung = True
   while True:
      uang_bayar = int(input("Masukkan uang yang dibayarkan pemesan: "))
      if uang_bayar > harga_pesanan:      
         print("Uang yang dibayarkan berlebih.")
         kas += uang_bayar
         # Setelah ngeluarin kembalian, program minta review disini.
         print("Ada 3 macam review, yaitu: ")
         for i in range(3):
            print(str(i+1)+".",review[-i-1])
         print("Silakan pilih review untuk makanan anda.")
         while True:
            input_review = input("Masukkan review anda untuk pesanan kami!(eneg, biasa, enak): ")
            if input_review == "eneg" or input_review == "biasa" or input_review == "enak":
               for pesanan in list_pesanan:
                  for menunya in daftar_menu:
                     if pesanan == menunya[1]:
                        menunya[3] = input_review
                        break
                     else:
                        continue
               break      
            else:
               print("Masukkan review yang benar!")
         print("Terimakasih sudah makan direstoran kami! Ini kembaliannya: {}".format(uang_bayar-harga_pesanan))
         kas -= (uang_bayar-harga_pesanan)
         break
         # Setelah ngasih review, uang kembalian(jika ada) dikembalikan disini, dan program memprint terimakasih sesuai contoh di soal.
      elif uang_bayar == harga_pesanan: 
         print("Uang yang dibayarkan pas.")
         kas += uang_bayar
         # Setelah ngeluarin kembalian, program minta review disini.
         print("Ada 3 macam review, yaitu: ")
         for i in range(3):
            print(str(i+1)+".",review[-i-1])
         print("Silakan pilih review untuk makanan anda.")
         while True:
            input_review = int(input("Masukkan review anda untuk pesanan kami!(1(Eneg), 2(Biasa), 3(Enak)): "))
            if input_review == 1 or input_review == 2 or input_review == 3:
               for pesanan in list_pesanan:
                  for menunya in daftar_menu:
                     if pesanan == menunya[1]:
                        menunya[3] = review[input_review]
                        break
                     else:
                        continue
               break
            else:
               print("Masukkan kode review yang benar!")
         print("Terimakasih sudah makan direstoran kami!")
         break
      else:
         print("Uang yang dibayarkan kurang! Silakan masukkan lagi sehingga uangnya pas atau lebih!")
         continue
os.system('cls') # Terminal akan dibersihkan dengan ini. Untuk mac OS, cls ganti clear. 
# Kalo pake IDLE, ini sama import os apus aja.
