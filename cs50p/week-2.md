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

## Hari 2 – 26 September 2026
Coding: 60 menit | Inggris: 35 menit

### Meow tanpa loop
- Bisa juga print meow tiga kali tanpa loop: `print("meow\n" * 3, end="")`.
- `\n` artinya ganti baris. String dikali angka artinya diulang, sama seperti `"3" * 2` jadi `"33"`.
- Pakai `end=""` karena tulisannya sudah diakhiri `\n`, sedangkan print bawaannya menambah ganti baris lagi. Tanpa end, ada baris kosong berlebih.
- Cara ini ringkas tapi kurang bagus dibaca, jadi loop lebih disukai.

### while True dan break
- while True itu syaratnya selalu benar, jadi harus ada break supaya bisa berhenti.
- Kalau mau bertanya berulang kali ke user sampai jawabannya benar, pakai while True lalu break di dalam if.

### Posisi break (indentasi)
- Setiap titik dua `:` membuka satu tingkat baru. Isinya menjorok satu tingkat lebih dalam.
- Patokannya dari if, bukan dari while. break diletakkan satu tingkat di bawah baris bertitik dua yang jadi syaratnya.
- Jangan dihafal "selalu dua kali", karena kalau if-nya bertumpuk bisa jadi tiga tingkat dari while.
- Seberapa dalam pun, break tetap keluar dari loop-nya (while), karena if bukan loop.
- Cara memposisikan: tanyakan "baris ini dijalankan dalam kondisi apa?"

### Tiga keadaan break
- Tanpa break sama sekali: bertanya terus, benar atau salah, tidak pernah berhenti. Itu infinite loop.
- break di dalam if: kalau salah (negatif) tanya lagi, tanya lagi. Kalau sudah benar (positif), break, tidak usah tanya lagi.
- break sejajar dengan if: cuma satu putaran, benar atau salah, karena break selalu dibaca lalu dijalankan. Jadi while-nya tidak berguna.
- Kalau if dibiarkan kosong tanpa isi, error, seperti def kosong.

### continue
- continue BUKAN penghenti loop. Hanya break yang menghentikan loop.
- continue artinya lewati sisa putaran ini, lalu lanjut ke putaran berikutnya.
- Contoh: kalau angka 3 di-continue, output-nya jadi 1 2 4, karena angka 3 di-skip.
- Di contoh David `if n < 0: continue` lalu `else: break`, continue-nya tidak terlalu dibutuhkan. Cukup `if n > 0: break`.

### return di dalam loop
- return itu menyelesaikan seluruh function dan menyerahkan nilainya. Karena while ada di dalam function, loop-nya ikut berhenti.
- break hanya keluar dari loop, function masih lanjut. return keluar dari seluruh function.
- Seperti break itu keluar dari ruang kelas tapi masih di sekolah, return itu pulang sekaligus membawa kertas hasilnya.
- Di get_number, `return n` di dalam if langsung melakukan dua pekerjaan: menghentikan loop dan menyerahkan nilai.

### meow(number)
- `number = get_number()` sudah menampung angka dari user.
- Tapi kalau di baris berikutnya ditulis `meow(3)`, angka dari user tidak pernah dipakai. User ketik 5, meow tetap 3 kali.
- Seharusnya `meow(number)`, supaya isi kotak number dikirim sebagai argument.
- Polanya sama seperti Making Faces: hasil function ditangkap ke variabel, lalu variabel itu dikirim ke function berikutnya.

### Yang masih bingung
-

## Hari 3 – 27 September 2026
Coding: 90 menit | Inggris: 35 menit

### Kosakata
- "cyclically" artinya secara berulang atau berputar, dari kata cycle (siklus). Maksud David: menulis kode yang berulang pakai loop, dan mendapatkan jawaban kembali pakai return.
- "off by one" artinya meleset satu angka.
- "shall we say" artinya katakanlah, bisa dibilang.
- "get used to it" artinya terbiasa.
- "initialize" artinya memberi nilai awal pada variabel sebelum dipakai.

### List dan index
- Angka di dalam square bracket namanya index, yaitu nomor urut posisi.
- Index dihitung dari 0. `students[0]` itu anggota pertama, `students[2]` itu anggota ketiga.
- Karena manusia menghitung dari 1, di kepala kita selalu meleset satu. Itulah "off by one mentally". Lama-lama terbiasa.
- `students` artinya seluruh list sekaligus. `students[i]` artinya satu anggota di posisi i.
- `len(students)` memberikan jumlah anggota list.

### Tanya jawab: initialize variabel di for
- Mahasiswa bertanya: apakah variabel student perlu disiapkan dulu sebelum for?
- Jawaban David: tidak perlu. Python otomatis mengisi student dengan Hermione dulu, lalu Harry, lalu Ron.
- Beda dengan while, di situ kita harus menulis `i = 0` sendiri sebelum loop.
- Kebiasaan penamaan: list pakai jamak (students), variabel loop pakai tunggal (student). Supaya mudah dibaca: untuk setiap student di dalam students.

### Hash table
- Hash table itu tempat menyimpan data berpasangan: label dan isinya. Di Python namanya dict.
- List diakses pakai nomor urut, dict diakses pakai label.
- Seperti lemari loker santri berlabel nama: langsung menuju loker "Azka", tidak menghitung dari loker pertama.

### Dua jenis for loop
- Kalau cuma butuh isinya, pakai `for student in students`. Ini lebih simpel.
- Kalau butuh isi dan nomor urutnya, pakai `for i in range(len(students))`, lalu isinya diambil dengan `students[i]`.
- Di versi range, i bukan berisi nama, tapi nomor: 0, 1, 2. Seperti nomor kursi. Untuk tahu siapa yang duduk di kursi itu, harus lihat daftarnya dengan `students[i]`.
- `print(i + 1, students[i])` hasilnya daftar bernomor mulai dari 1. Pakai `i + 1` karena index mulai dari 0.
- Urutan tampilnya tetap sesuai urutan di list.

### Kesalahan yang saya pikirkan
- Tidak bisa mencampur dua jenis loop. `for student in students` tidak punya i, jadi `print(i + 1, student)` error NameError. `for i in range(...)` tidak punya student, jadi `print(i + 1, student)` juga NameError.
- `print(i + 1, students)` tidak error, tapi yang tercetak seluruh list di setiap putaran, bukan satu nama. Karena loop tidak mengubah students, yang berubah hanya i.

### range dan print
- range hanya menerima bilangan bulat (int). Kalau diberi desimal, TypeError.
- print bisa menerima argument sebanyak apa pun. Di dokumentasi tertulis `print(*objects, sep=' ', end='\n')`. Tanda bintang artinya boleh berapa pun jumlahnya.

### Yang masih ingin dicoba
- Menampilkan isi list tanpa kurung siku, jadi seperti "Hermione, Harry, Ron". Caranya pakai method `join`, kebalikan dari split. Belum dibahas di lecture.
- Belum mencoba `print(students[3])`, penasaran error apa yang muncul.
