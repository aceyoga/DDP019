# Week 3.5 Challenge!
By: Yoga Mahendra

## Selesaikan kedua permasalahan dibawah ini dengan melengkapi template program yang telah disediakan di folder Enjoy the show!

### 1. Password Generator
#### Cerita:
Seorang maba fasilkom ingin iseng mencoba membuat program yang bisa membuatkannya sebuah password, lalu dia ingin bisa memilih untuk menampilkannya langsung di Terminal, atau menyimpannya kedalam sebuah file dengan format(.txt). Dengan catatan, passwordnya *minimal* 4 digit dan *maksimum* 20 digit. Default satu password: 10 digit, default banyak password: 8-12 digit.

Program ini juga bisa membuat satu passwordnya atau lebih(programnya bikin berapa password dan panjangnya berapa itu tergantung si penggunanya).

Dan setelah program selesai membuat password, dia ingin bisa melakukannya lagi(Programnya ngga langsung ke exit gitu loh). Untuk mempermudah kodingannya, *Terminal* tidak perlu dibersihkan.

#### Bintang 4 kalo 100% sesuai permintaan soal, bintang 2 kalo cuma bikin satu password dan dikeluarin di terminal.

### 2. Seni Akuntansi Offline
#### Cerita:

Seorang kasir part-time suatu restoran terkenal di jepang kebetulan merupakan sarjana Manajemen. Dia merasa bosan karena setiap hari dia harus melakukan hal yang sama, yaitu mengecek biaya yang harus dibayar oleh konsumen, menerima pembayaran, lalu menghitungnya dan memasukkannya kedalam rak uang dibawah mesin kasirnya.

Karena itu, dia meminta bantuan kalian untuk membuatkannya sebuah program yang bisa mempermudah pekerjaannya sebagai kasir. Spesifikasi program yang dimintanya adalah sebagai berikut:
1. Program ini meminta daftar menu, lalu memasukannya ke sistem.
2. Program ini akan meminta input menu apa saja yang dipesan oleh konsumen, lalu mengecek dan memberitahu harga total yang harus dibayar konsumen di terminal.
3. Uang yang dibayar oleh konsumen, akan masuk secara otomatis kedalam rak uang dibawah mesin kasirnya. Uang yang masuk akan disortir ke slotnya masing-masing.
4. Jika konsumen tidak memberikan uang yang cukup, program akan mengeluarkan tulisan "Uang tidak cukup! Anda harus membayar dengan uang yang cukup atau lebih!" lalu meminta uangnya lagi. Jika konsumen memberikan uang pas, maka program akan mengeluarkan tulisan "Uang yang dibayarkan pas, terimakasih sudah makan direstoran kami!" tanpa memberitahu jumlah uang kembaliannya(Duitnya pas kok wkwk). Jika konsumen memberikan uang lebih, maka program akan mengeluarkan  tulisan "Uang yang dibayarkan berlebih, dan ini kembaliannya: " lalu mengeluarkan total uang yang dikembalikan, dan mengeluarkan tulisan "Terimakasih sudah makan direstoran kami!". Tentu saja, uang yang dibayarkan akan masuk dulu kedalam rak uang, kemudian baru mengambil uang kembaliannya.
5. Program juga akan meminta review dari pemesan, lalu program akan menyimpan review pesanannya di sistem.

#### Bintang 7 kalo 100% sesuai permintaan soal; bintang 6 kalo spesifikasi 4 diasumsikan uang pembayaran pas sama kurang; bintang 5 kalo spesifikasi 4 diasumsikan uang pembayaran selalu pas, bintang 4 kalo spesifikasi 4 diasumsikan uang selalu pas dan spesifikasi 5 ga dibikin.

## Untuk kedua soal, kk sudah menyiapkan file simulator yang akan mengecek apakah program kalian berhasil dijalankan sesuai permintaan atau tidak.
### Untuk soal nomor 1, diasumsikan input minta bikin satu password bakal cuma minta satu input angka, dan input minta bikin banyak password akan meminta panjang minimal dan maksimal dari password itu dalam 2 input berbeda. Soal ini sendiri memiliki 2 solusi yang cukup berbeda, jadi gpp kalo ngga terlalu mirip dengan kunci jawaban yang akan dirilis minggu depan.
### Untuk soal nomor 2, diasumsikan file menu udah tersedia, tinggal lengkapin spesifikasi 1 aja. Untuk input di spesifikasi 2, konsumen bisa memasukkan nama makanan/minuman/consumables yang dipesannya, atau nomor indeks makanan tersebut di menu(Nanti tiap mau bayar, daftar menunya diprint sesuai format yang ada di lampiran). Spesifikasi 5 itu reviewnya untuk semua yang dipesan oleh si konsumen, jadi kalo konsumen mesan nasi goreng sama es teh hangat dan reviewnya enak, maka nasi goreng sama es teh hangat akan dapat review enak. Reviewnya sendiri ada 3, yaitu: Eneg(Eneg = ga enak :v),Biasa, Enak. Konsumen tinggal masukin angka 1, 2, 3 untuk masing-masing review. Review makanan akan ditampilkan di menu ya :D

#### Note: Aslinya soal no.2 ini tingkat kesulitannya adalah bintang 10, atau setara dengan soal lab DDP1. Waktu pengerjaan soal bintang 10 adalah *Satu jam 20 menit*, tapi terkadang soalnya lebih sulit dan mengakibatkan waktu pengerjaan bertambah, dari 15 menit sampai dengan 2 jam(Pernah ada yang sampe 23.55 wkwkwk). Karena ini DDP0, maka semua soal yang kami, para tutor berikan, sudah dinerf parah dan didesain agar mudah dipahami dan dikerjakan peserta. Performa kalian dalam mengerjakan soal bisa(dan akan) dijadikan acuan dalam belajar mandiri untuk sesi mentoring privat selanjutnya. Kalo soalnya terlalu sulit, kami minta maaf yak :D (Ingat bahwa soal lab DDP1 tidak mengenal ampun, malah kalo telat ngumpul bakal ada pengurangan nilai, bahkan nilai lab itu dibuat 0.)
