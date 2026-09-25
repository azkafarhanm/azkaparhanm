# CS50P Week 2: Loops

## Hari 1 – 25 September 2026
Coding: 90 menit | Inggris: 35 menit

### while
- while dipakai dengan variabel penghitung yang ditambah setiap putaran, sampai syaratnya salah lalu berhenti.
- Kalau lupa menambah penghitungnya, jadinya infinite loop. Hentikan dengan Ctrl + C.
- Bahasa lain punya `++` dan `--`, Python tidak punya.
- Python pakai `i += 1`, artinya sama dengan `i = i + 1`. Itu convention, cara singkat.

### Tanya jawab menit 13:53
- Mahasiswa bertanya: bisakah for loop diberi nilai i di awal, berjalan sesuai syarat, lalu i ditambah sambil jalan, semuanya dalam satu baris seperti di bahasa C atau Java?
- Jawaban David: tidak bisa persis seperti itu. Tapi Python punya jenis for loop sendiri.

### for
- for tidak memeriksa syarat true atau false seperti while.
- for menyusuri daftar list, mengambil setiap anggota satu per satu, sampai anggotanya habis.
- Seperti absen santri dari daftar: panggil nama pertama, kedua, ketiga, berhenti saat daftarnya habis.
- Jumlah putaran = jumlah anggota daftar. Isinya angka atau tulisan tidak berpengaruh.
- Percobaan: `for i in ["azka", "farhan", "ahmad"]` mencetak meow 3 kali karena isian list-nya ada 3.
- Kalau yang di-print `i`, hasilnya azka, farhan, ahmad. Di setiap putaran, i berisi satu anggota.
- Di while kita sendiri yang menyiapkan hitungan, memeriksa syarat, dan menambah hitungan. Di for, Python yang mengurus, jadi aman dari infinite loop.

### range
- range itu function bawaan Python untuk menghasilkan deretan angka berurutan.
- Mulai dari 0, dan berhenti sebelum angka yang ditulis. `range(3)` isinya 0, 1, 2, tidak memuat 3.
- Makanya `for _ in range(3)` berputar tepat 3 kali.
- range bisa diberi argument opsional: `range(berhenti)`, `range(mulai, berhenti)`, `range(mulai, berhenti, langkah)`.
- Percobaan:
  - `list(range(5))` → `[0, 1, 2, 3, 4]`
  - `list(range(1, 4))` → `[1, 2, 3]`
  - `list(range(0, 10, 2))` → `[0, 2, 4, 6, 8]`

### Pythonic: underscore
- Di `for i in range(3): print("meow")`, variabel i tidak pernah dipakai.
- Python wajib punya variabel untuk menghitung putaran, tapi kalau kita tidak peduli nilainya, namai `_`.
- Tidak mengubah hasil program, cuma tanda untuk diri sendiri nanti atau rekan kerja bahwa variabel itu sengaja tidak dipakai.
- Mirip dengan `case _` di match: sama-sama artinya "tidak peduli isinya".

### for dengan split
- split menghasilkan list, jadi bisa langsung disusuri dengan for.
- `for kata in "saya belajar python".split(): print(kata)` hasilnya 3 baris: saya, belajar, python.
- Karena print bawaannya ditutup ganti baris. Kalau pakai `end=" "`, ketiganya muncul dalam satu baris.

### Yang masih bingung
-
