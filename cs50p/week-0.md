# CS50P Week 0: Functions, Variables

## Hari 1 – 16 September 2026
Coding: 40 menit | Inggris: 30 menit

### Function dan argument
- Function harus ada parentheses.
- Di dalamnya ada quote dan unquote, yang dinamakan string.
- Argument itu isi yang ada di dalam parentheses.
- Belajar documentation dan parameter seperti `sep` dan `end`.

### Side effect
- Side effect ini menarik sekali.
- Side effect itu sesuatu yang terjadi dari function.

### Koma dan plus operator
- Pakai koma otomatis menambah spasi sendiri.
- Kalau pakai plus operator, di argument pertama sebelum unquote harus ada spasi supaya hasilnya rapi.

### Variabel
- Variabel itu menyimpan nilai dari input user.
- Variabel itu menyimpan nilai, bukan hanya dari input tapi dari berbagai tipe data.
- Kalau variabel diisi dua kali (`nama = "azka"` lalu `nama = "parhan"`), yang muncul adalah isi value yang terbaru, yaitu parhan.

### Istilah lain
- Bugs itu istilah untuk kesalahan yang kita buat dalam membuat kode.


## Hari 2 – 17 September 2026
Coding: 100 menit | Inggris: 35 menit

### sep dan end
- sep (separator) dan end gunanya untuk mengganti default di Python.
- Default sep: di antara argument yang dipisah koma otomatis ada spasi.
- Kalau ditambah sep, misalnya `sep="-"`, default spasinya hilang diganti strip. Contoh: `print("halo,", nama, sep="-")` hasilnya `halo,-parhan`.
- Default end: seperti enter setelah selesai mengetik, jadi pindah ke baris baru.
- Kalau `end=""` (kosong), enter-nya hilang. Contoh: `print("halo", end="")` lalu `print("azka")` hasilnya `haloazka` merapat di satu line.

### f-string
- Di print ada huruf f sebelum tanda kutip.
- Kalau mau menunjukkan isi value dari variable, tulis nama variable-nya di dalam bracket `{}`.
- Contoh: `print(f"halo, {nama}")` hasilnya `halo, parhan`.

### Method
- `print` itu function.
- `nama.strip()` itu method.
- `nama` itu variable, `strip` itu function, jadi method itu function yang nempel ke variable, dengan titik di tengah.
- Function bisa digabung dengan function lagi, terutama di input.

### strip, split, capitalize, title
- `strip` menghapus white space yang di kiri dan di kanan.
- `split` memisahkan. Waktu dicek di VS Code, hasilnya jadi list.
- `capitalize` membuat huruf pertama di awal jadi kapital. Contoh: `azka farhan` jadi `Azka farhan`.
- `title` membuat huruf pertama setiap kata jadi kapital. Contoh: `azka farhan` jadi `Azka Farhan`.
- Banyak function lain di library Python, ada link-nya di video. Belum aku lihat.

### Lainnya
- Modulo itu sisa dari pembagian. Contoh: `3 % 2` hasilnya `1`.
- Interactive mode itu seperti interpreter Python, tektokan back and forth. Kita kasih perintah, langsung dijawab. Contoh: ketik `1 + 2`, langsung keluar `3`.

### Yang masih bingung
- List belum paham, nanti dibahas di Week 2.

## Hari 3 – 18 September 2026
Coding: 120 menit | Inggris: 35 menit
Lecture Week 0 selesai ditonton.

### def dan pemanggilan function
- Function ada pemanggilannya. Dipanggil tanpa def di depannya, dan ditulis di luar function, tidak mengikuti aturan indented.
- Kalau tidak ada pemanggilan, resepnya tidak jalan. Waktu `hello()` dihapus, tulisan hello tidak muncul.
- Ternyata kita bisa buat resep sendiri. Tinggal panggil function itu, nanti jadi apa yang sudah terbentuk dalam resep.
- Function bawaan di dokumentasi Python itu memang sudah dibuat resepnya dari sananya.
- `main()` ditaruh di paling bawah. Kalau `hello(name)` ada di dalam resep main dan main belum dipanggil, tidak ada yang jalan.
- `square` error `NameError: name 'square' is not defined` karena resepnya belum dibuat. Kalau mau panggil function, harus di-define dulu.

### Parameter dan argument
- Parameter itu kotak kosong waktu mendefine function. Contoh: `def hello(to):`, `to` itu parameter.
- Argument itu isian saat pemanggilan function. Contoh: `hello("azka")`.
- Isiannya diberikan dari luar waktu dipanggil, bukan diisi di dalam resep.
- Satu pemanggilan jalan satu kali. Kalau mau dua sapaan, panggil dua kali.
- Default value seperti `to="world"` dipakai kalau pemanggilannya kosong. Kalau ada argument, isi argument yang dipakai.

### Scope
- Scope itu wilayah. Variabel yang dibuat di dalam satu resep tidak dikenal oleh resep lain.
- Arah masuk: parameter dan argument. Arah keluar: return.
- `NameError: name 'name' is not defined` muncul kalau `hello` memakai `name` yang lahir di dalam `main`.
- `TypeError: hello() takes 0 positional arguments but 1 was given` muncul kalau argument dikirim tapi resepnya belum punya kotak kosong.
- Bedanya: NameError muncul waktu isi resep dibaca, TypeError muncul lebih awal waktu pemanggilan.

### return
- print itu showing, return itu giving.
- Resep tanpa return tidak menyerahkan apa-apa, jadi variabelnya berisi `None`.
- `number = square(5)` dengan resep yang isinya print: angka 25 tetap muncul di layar, tapi `print(number)` keluar `None`.
- `number * 2` error karena None tidak bisa dikalikan.
- Kalau resepnya print saja, `print("x squared is", square(x))` tidak error, tapi hasilnya `x squared is None`. Program jalan tapi hasilnya salah.
- Pada `nama = input("masukkan nama anda: ")`: yang muncul di screen itu side effect, dan yang disimpan ke variabel nama itu return value.

### Materi lain hari ini
- Square bracket di dokumentasi Python artinya optional, tambahan.
- `round` membulatkan ke integer terdekat. Contoh: 4.6 jadi 5. Bisa juga dibatasi jumlah desimalnya.
- Float bisa menampung input integer.
- Pemisah ribuan pakai f-string, di dalam curly brace pakai colon lalu koma, hasilnya seperti 1,000.

### Yang masih bingung
- Membaca traceback (jejak error) belum paham, mau dibahas lagi.
