# Template soal nomor 2.
import os

daftar_menu = []
review = ["Eneg","Biasa","Enak"]
kas = 1000000000
input_file = open(input("Masukkan nama file(Usahakan program ini dan file txtnya dalam satu folder): "),"r")
rtxt = input_file.readlines()
for i in range(len(rtxt)):
   split1 = rtxt[i].split("\n")
   split1.pop(-1)
   split2 = split1[0].split(",")
   submenu = [i+1]
   submenu.extend(split2)
   daftar_menu.append(submenu)
while True:
   list_pesanan = []
   # Sebelum meminta input pesanan, kasirnya tanyain dulu mau nginput pesanan atau ngga, kalo ngga berarti programnya diakhiri.
   opsi = input("Anda mau membayar atau keluar?(bayar/exit): ")
   if opsi == "exit":
      break
   # Spesifikasi 2
   # Program akan meminta input makanan/minuman yang dipesan. Sebelum meminta input, program menampilkan daftar menunya dulu.
   for consumables in daftar_menu:
      print(consumables[0],". Nama:",consumables[1],", Harga:",consumables[2])
   # Input pesanan disini. Ingat bahwa konsumen bisa memesan lebih dari 1 makanan/minuman. Hint: while True bisa disetop
   while True:
      input_pesanan = input("Masukkan pesanan anda: ")
      list_pesanan.append(input_pesanan)
   
   # Setelah meminta input, program mencetak total harga pesanan, lalu meminta input uang pembayaran oleh pelanggan.
   # Hint: Spesifikasi 4 ini memiliki kondisional tergantung bintang yang ingin kalian dapatkan.
   # Hint 2: Uang yang masuk itu dimasukin kedalam kas dulu, dan kembalian ambilnya dari kas juga :D
   
   # Setelah ngeluarin kembalian, program minta review disini.
   # Hint: Reviewnya tinggal ganti dengan pilihan review dari konsumen.
   print("Ada 3 macam review, yaitu: ")
   for i in range(3):
      print(i+1,review[-i-1])
   print("Silakan pilih review untuk makanan anda.")
   
   # Setelah ngasih review, uang kembalian(jika ada) dikembalikan disini, dan program memprint terimakasih sesuai contoh di soal.
   os.system('cls') # Terminal akan dibersihkan dengan ini. Untuk mac OS, cls ganti clear.