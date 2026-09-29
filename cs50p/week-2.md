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

## Hari 4 – 28 September 2026
Coding: 90 menit | Inggris: 35 menit
Video belum selesai, berhenti di bagian dictionaries.

### IndexError
- `print(students[3])` dengan list tiga nama hasilnya `IndexError: list index out of range`.
- Index-nya hanya 0, 1, 2. Index 3 tidak ada, jadi di luar jangkauan.
- Patokan: index terakhir selalu jumlah anggota dikurangi satu.

### Salah terminal
- Saya sempat mengetik kode Python langsung di PowerShell, jadinya error aneh seperti cmdlet dan ParserError.
- Tandanya: `PS D:\...>` itu PowerShell. Kalau sedang di Python, awal barisnya `>>>`.
- Kode Python harus ditulis di file lalu `python latihan.py`, atau ketik `python` dulu untuk interactive mode.

### Pembuktian students, students[i], student
- `for i in range(len(students)): print(i + 1, students[i])` → satu nama per baris. students[i] mengambil satu anggota.
- `print(i + 1, students)` → seluruh list di setiap baris. students itu seluruh daftar, loop tidak mengubahnya.
- `print(i + 1, student)` → NameError, karena di loop versi range tidak ada variabel student. Python bahkan menawarkan "Did you mean: 'students'?".

### Kenapa butuh dict
- Kalau data satu orang dipisah di beberapa list (students, houses, patronus), yang menghubungkannya cuma posisi index.
- "Honor system" artinya sistem atas dasar kepercayaan. Tidak ada yang menjamin list-list itu tetap berpasangan, cuma ketelitian programmer.
- Bisa berantakan: lupa menambah di salah satu list jadi IndexError, atau urutannya bergeser jadi pasangannya tertukar tanpa error sama sekali.
- Seperti mencatat nama santri, kelas, dan nomor wali di tiga buku terpisah.

### dict
- dict ditulis dengan kurung kurawal `{}`, isinya pasangan label dan isi, dipisah titik dua.
- "Run out of keys" artinya kehabisan tombol keyboard. Satu simbol dipakai untuk beberapa arti. `{}` di f-string artinya tempat menyisipkan nilai, di luar tulisan artinya membuat dict.
- Sama seperti `*` dan `+` yang artinya berbeda untuk angka dan string. Lihat simbolnya ada di mana, baru tentukan artinya.

### for di dict
- Kalau iterate over dictionary pakai for, yang diambil key-nya saja (labelnya), bukan isinya.
- "Could have gone both ways" maksudnya pembuat Python bisa saja memilih for memberikan isinya, tapi mereka memilih key.
- `students[student]` artinya buka loker yang labelnya sesuai isi student.
- for tidak membuat label. Labelnya sudah ada sejak dict ditulis. for cuma berjalan membaca label satu per satu.
- Di setiap putaran, variabel loop memegang satu key saja, bukan semua key sekaligus.
- Kalau sudah tahu labelnya, tidak perlu for. Langsung `santri["Ahmad"]`.
- Mau buka satu loker → langsung pakai label. Mau buka semua loker → pakai for.

### KeyError
- `print(santri["Budi"])` dengan label yang tidak ada hasilnya `KeyError: 'Budi'`.
- List, nomor urut tidak ada → IndexError. Dict, label tidak ada → KeyError.
- Keduanya sama-sama mencari loker yang tidak ada, bedanya cara menunjuk lokernya.

### List berisi dict
- David menyusun students jadi list, dan setiap anggotanya dict berisi name, house, patronus. Jadi setiap santri punya satu kartu.
- "That's my prerogative as a programmer" artinya itu hak saya sebagai programmer untuk memutuskan. Bentuk data itu pilihan desain, bukan aturan Python.
- Draco diberi `"patronus": None`, artinya sengaja menyatakan tidak ada nilai.
- Untuk mengambil asrama Hermione: `students[0]["house"]`. Ambil kartunya dulu dengan nomor, lalu buka kartunya dengan label.
- Kurung siku kedua langsung menempel, tanpa titik. Titik hanya untuk method.
- Polanya mirip `input().strip().lower()`: yang kedua bekerja pada hasil yang pertama.

### Kosakata
- patronus: istilah cerita Harry Potter, bukan istilah pemrograman.
- conjure up: memunculkan dengan sihir.
- prerogative: hak atau wewenang untuk memutuskan sendiri.

### Jenis error yang sudah saya kenal
- NameError, TypeError, ValueError, IndexError, KeyError.

### Yang masih ingin dicoba
- `students[3]["patronus"]` dengan data David, hasilnya apa?
- Lanjutkan video Week 2 dari bagian dictionaries.

## Hari 5 – 29 September 2026
Coding: 90 menit | Inggris: 30 menit
Lecture Week 2 selesai ditonton.

### None bukan KeyError
- `students[3]["patronus"]` hasilnya None, bukan error.
- `santri["Budi"]` KeyError karena labelnya tidak ada.
- `students[3]["patronus"]` None karena labelnya ada, isinya sengaja dibuat tidak ada.
- Loker yang kosong berbeda dengan loker yang tidak pernah dibuat.

### Menulis dari atas ke bawah
- David menulis `print_column(3)` di main dulu, padahal function-nya belum dibuat. Tulis dulu apa yang mau dilakukan, baru bagaimana caranya di bawah.
- Tidak error karena def main hanya dibaca, belum dijalankan. Selama print_column sudah ditulis sebelum `main()` dipanggil di akhir, aman.
- "forethought" artinya memikirkan sebelumnya. "as good a name as any" artinya nama ini pantas saja dipakai.

### Nama function dengan underscore
- `print_column` bukan print yang ditempeli sesuatu. Itu satu nama baru buatan David.
- Nama di Python tidak boleh ada spasi, jadi kata-katanya disambung garis bawah. Namanya snake_case.
- Sudah sering saya pakai: get_number, is_even, dollars_to_float, meal_time.
- Namanya diawali print karena tugas function itu memang mencetak.

### Abstraksi
- Abstraksi artinya memberi nama pada sekumpulan langkah, jadi pemakainya cukup tahu apa yang dilakukan, tanpa perlu tahu bagaimana caranya.
- print_column bisa diisi `print("#\n" * height, end="")` atau `for _ in range(height): print("#")`. Isinya beda, tapi main tidak berubah dan hasilnya sama.
- "underlying implementation" artinya cara kerja di baliknya, isi resepnya.
- Seperti menyuruh ketua kamar "siapkan halaqah", tidak perlu tahu caranya.
- print, input, len juga abstraksi. Saya pakai tanpa tahu isi resepnya.

### Kenapa David mengulang materi lama
- Di bagian Mario, David menggabungkan semua yang sudah dipelajari: def, parameter, for, range, _, print, end, string dikali angka.
- Tujuannya melatih cara berpikir: melihat gambar batu bata di game, lalu menerjemahkannya jadi kode.
- Ini juga murojaah yang sengaja dibangun di kurikulum.

### Nested loops
- "keep nesting inside of each other" artinya terus bersarang, satu di dalam yang lain.
- Mau membuat kotak batu bata seperti di Mario, row-nya 3 dan column-nya juga 3.
- Loop luar menjalankan setiap baris. Di setiap putaran, dia menjalankan loop dalam.
- Loop dalam menjalankan setiap batu bata dalam satu baris, isinya juga 3, jadi print "#" tiga kali.
- `end=""` gunanya mencegah baris baru. Karena setiap print bawaannya membuat baris baru, maka dibuat end kosong supaya batu batanya merapat menyamping: ###.
- Setelah loop dalam selesai, baru `print()` yang sendirian itu dijalankan. Gunanya menutup baris dan memindahkan kursor ke bawah.
- print() itu sejajar dengan `for j`, jadi dijalankan setiap kali satu baris selesai.
- Kalau print() dihapus, semua batu bata bertumpuk jadi satu baris: sembilan # merapat.
- Seperti absen santri per kamar: loop luar pindah kamar, loop dalam memanggil santri satu per satu di kamar itu.

### Kode bisa diringkas
- "tighten up this code" artinya merapikan dan meringkas kode.
- `print("#" * size)` bisa menggantikan loop dalam. String dikali angka mengulang # menyamping, dan print bawaannya sudah ganti baris, jadi print() kosong tidak perlu lagi. Cukup satu loop.
- Bisa juga dipecah jadi tiga function: main, print_square, print_row. Setiap function mengurus satu tugas kecil.
- "decompose" artinya memecah masalah besar jadi bagian kecil.
- "wrap your mind around" artinya memahami sesuatu yang agak rumit.
- Versi ringkas bisa karena semua batu batanya sama. Kalau isinya berbeda-beda, nested loop tetap dibutuhkan.

### Yang masih bingung
-
