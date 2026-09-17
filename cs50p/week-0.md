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

### Yang masih bingung
- Pada `input("masukkan nama anda: ")`, mana yang side effect dan mana yang return value?

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
