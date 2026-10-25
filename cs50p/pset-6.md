# Problem Set 6

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

Sama seperti sebelumnya: petunjuk saat mengerjakan soal saya minta ke CS50 Duck. Claude saya pakai untuk murojaah lecture sebelum mulai, dan untuk membahas setelah submit.

## Pemanasan sebelum mulai (24 Oktober 2026 pagi)

Kuis Kosakata #3 (kata dari akhir Lecture 6 dicampur kata lama): **100%**, tiga kali berturut-turut.

Empat pertanyaan coding, sengaja dipilih yang berguna untuk Pset 6:

1. **`python lines.py hello.py` → `len(sys.argv)` berapa?** 2. Benar. Tapi saya sempat mengira program otomatis tahu kalau user lupa mengetik nama file. Ternyata tidak: kalau langsung memakai `sys.argv[1]`, program crash dengan `IndexError`. Jadi harus dicek dulu pakai `len(sys.argv)`, lalu keluar dengan `sys.exit("pesan")`.
2. **Cek nama file berakhiran `.py`.** Pakai `endswith`. Ejaannya pakai **s**: *ends with*.
3. **`open` file yang tidak ada.** Errornya `FileNotFoundError`, ditangkap dengan `try` / `except`. Saya sempat menjawab pakai mode `"w"`. Itu **berbahaya**: `"w"` memang tidak error karena membuat file baru, tapi kalau filenya sudah ada, isinya langsung dikosongkan. Program yang membaca tidak boleh pakai `"w"`.
4. **Baris `"    # komentar"` diawali `#`?** `startswith("#")` saja hasilnya `False`, karena karakter pertamanya spasi. Harus dibuang dulu pakai `lstrip()` (kiri) atau `strip()` (kiri dan kanan).

## 1. Lines of Code — selesai, check50 hijau semua 9/9 (24 Oktober 2026)

Yang diminta soal: program yang menerima **tepat satu** command-line argument (nama file Python), lalu mencetak jumlah baris kode di file itu, **tidak termasuk komentar dan baris kosong**. Keluar dengan `sys.exit` kalau argumennya kurang/lebih, bukan file `.py`, atau filenya tidak ada.

Lumayan menantang. Saya mulai sekitar jam 4.30 pagi, selesai jam 7.

### Kebingungan 1: command-line argument itu isi file?
- Saya kira dengan `python lines.py ascii.py`, program langsung "tahu" isi `ascii.py`, lalu bisa di-loop `for i in ascii.py`.
- Ternyata command-line argument **cuma nama file**, berupa string `"ascii.py"`. Program belum tahu apa-apa soal isinya.
- Ada dua langkah terpisah: **ambil nama file** dari `sys.argv[1]`, lalu **buka file itu dengan `open`** supaya bisa dibaca baris per baris.

### Kebingungan 2: `open` hanya untuk `.txt` dan `.csv`?
- Ternyata file `.py` juga **file teks biasa**, isinya baris-baris kode sebagai teks. Jadi bisa dibuka dengan `open` dan di-loop `for line in file`.

### Kebingungan 3: harus membuat dua file?
- Saya bingung, yang di-`open` itu file saya sendiri (`lines.py`) atau file lain?
- `lines.py` adalah **program saya**. File yang dihitung **diberikan user** lewat command-line argument, jadi di kode saya tidak menulis nama file tertentu.
- `sys.argv[0]` = `"lines.py"` (program saya), `sys.argv[1]` = file yang mau dicek. Dengan begitu program bisa dipakai untuk file apa saja.
- Waktu check50 berjalan, dia memakai file-file uji miliknya sendiri. Program saya cukup memproses apa pun yang diberikan.

### Kebingungan 4: `sys.argv[1]` di dalam `open` pakai tanda kutip?
- Tidak. `"sys.argv[1]"` dengan kutip itu teks harfiah, jadi Python malah mencari file yang namanya `sys.argv[1]`. Tanpa kutip, yang dipakai adalah **nilainya** (nama file dari user).

### Kebingungan 5: urutan pengecekan
- Cek argumen (jumlah dan `.py`) **dulu**, sebelum `open`. Kalau user tidak memberi nama file lalu langsung dibuka, program sudah error sebelum sempat mengecek.
- Untuk `.py`: pakai `endswith`, tapi kondisinya harus dibalik pakai `not`, karena yang mau dilakukan adalah **keluar kalau tidak** berakhiran `.py`.

### Kebingungan 6: file tidak ada tidak bisa dibandingkan seperti string
- Jumlah argumen dan `.py` bisa dicek dengan membandingkan. Tapi file ada atau tidak baru ketahuan **saat `open` dijalankan**.
- Jadi pakai `try` / `except FileNotFoundError`. Yang dibungkus `try` adalah bagian yang bisa gagal, yaitu saat membuka file.

### Kebingungan 7: komentar dan baris kosong
- `startswith` huruf kecil semua, tanpa underscore.
- **`strip()` dulu, baru dicek.** Kalau tidak, komentar yang diawali spasi tidak terdeteksi.
- Baris kosong atau yang cuma berisi spasi, setelah di-`strip()`, jadi string kosong `""`. Bisa dibandingkan dengan `""`, atau ingat bahwa string kosong itu *falsy*.

### Kebingungan 8: cara menghitung baris
- Pakai penampung angka yang mulai dari 0, lalu bertambah setiap kali ketemu baris kode di dalam loop.

### Eksperimen di terminal
- Awalnya saya coba-coba: `input` nama lalu mencetak isi `lines.py` sendiri baris per baris, untuk melihat isi `line` setiap putaran.
- Sebelum check50, saya uji sendiri semua kasus: tanpa argumen, dua argumen, file `.txt`, nama yang bukan `.py`, file yang tidak ada, dan menghitung `lines.py` sendiri. Semua pesan error muncul sesuai harapan.

### Refleksi: cepat bertanya ke Duck
- Saya tidak ngoding 30 menit dulu baru bertanya. Saya merasa kalau tidak langsung bertanya, saya akan stuck lama, cuma bengong di depan layar. Memahami soal dan mereka-reka rencana programnya saja sudah makan waktu.
- Bertanya ke Duck tetap melatih logika saya: Duck tidak memberi jawaban, cuma pertanyaan pancingan, dan akhirnya saya yang menyusun kodenya. Kadang saya bertanya hanya untuk **verifikasi** ("benar kan pakai ini?") karena masih kurang percaya dengan ide sendiri.
- Saran dari Claude:
  - Untuk pertanyaan "benar kan pakai ini?", **coba jalankan dulu di terminal**. Terminal adalah pemeriksa yang paling jujur: kalau salah, langsung error.
  - **Tulis tebakan dulu** di komentar kode sebelum bertanya. Hari ini hampir semua tebakan saya benar (strip dulu, `endswith`, `try` di sekitar `open`). Itu bukti ide saya bisa dipercaya.
  - Simpan pertanyaan ke Duck untuk saat benar-benar tidak tahu harus mulai dari mana.

## Pemanasan sebelum soal 2 (25 Oktober 2026)

Pagi ini murojaah mingguan dulu (Tip Calculator, lihat `murojaah.md`), lalu lanjut soal.

Kuis Kosakata #4: **60%** (6 benar, 4 salah). Memang lebih susah. Yang salah, akan diulang di kuis berikutnya:

| Frasa | Arti | Kunci mengingat |
|---|---|---|
| take a **peek** | melihat sekilas | *peek* (dua e) = mengintip, *peak* = puncak |
| **resort to** | terpaksa memakai (pilihan terakhir) | bukan *re-sort* (mengurutkan ulang) |
| **break down** (asumsi) | tidak berlaku lagi, gagal | asumsi yang runtuh |
| **to recap** | untuk merangkum | *recap* = rangkum, *recall* = mengingat |

Pertanyaan coding, semua benar:
1. `csv.reader` → setiap baris berupa **list berisi string**. `csv.DictReader` → **dictionary**.
2. Memasang library luar: `pip install nama_library`, diketik di **terminal**, bukan di kode.
3. Dokumentasi library baru: biasanya di halaman library itu di **pypi.org**.

## 2. Pizza Py — selesai, check50 hijau semua 7/7 (25 Oktober 2026)

Yang diminta soal: program yang menerima **tepat satu** command-line argument (file CSV berisi menu pizza), lalu menampilkannya sebagai tabel ASCII art memakai library **tabulate** dengan format **grid**. Keluar dengan `sys.exit` kalau argumennya kurang/lebih, bukan `.csv`, atau filenya tidak ada.

Seperti biasa, saya mulai dari memikirkan kerangkanya dulu: bagaimana `open`-nya, lalu bangun kerangka di sekitarnya. Soal ini mirip Lines of Code (cek argumen, cek akhiran file, file tidak ada), jadi saya melihat kode Lines saya sendiri untuk pola cek argumennya. Tidak terlalu sulit.

Persiapan di terminal: `wget` untuk mengunduh `sicilian.csv` dan `regular.csv`, lalu `pip install tabulate`.

### Kebingungan 1: perlu writer dan mode `"a"`?
- Saya kira harus pakai `csv.writer` atau `DictWriter`, karena isi CSV harus "diubah" jadi tabel.
- Ternyata soal cuma minta **menampilkan** tabel ke layar ("outputs"), bukan menulis ke file. Jadi cukup **membaca**. Mana yang untuk membaca: `reader`. Mana yang untuk menulis: `writer`.

### Kebingungan 2: membuka dua file sekaligus?
- Satu `open` hanya membuka **satu** file. Kalau butuh dua file, pakai dua `open`. (Di soal ini ternyata tidak perlu.)

### Kebingungan 3: list atau dictionary?
- Dari dokumentasi tabulate, dia bisa menerima dua-duanya: list of lists, atau iterable of dictionaries.
- Saya pilih `csv.reader` (list). Baris pertama CSV adalah header (`Sicilian Pizza,Small,Large`), jadi di tabulate saya pakai pengaturan **`headers="firstrow"`**. Format tabelnya pakai **`tablefmt="grid"`**. Dua-duanya saya temukan di dokumentasi, dengan petunjuk dari Duck.
- `tabulate` bisa langsung menerima `reader`, karena reader bisa di-loop baris per baris.

### Error yang saya temui
- `csv.reader()` tanpa isi → `TypeError: expected at least 1 argument, got 0`. Juru tulis pembaca harus diberi file yang mau dibaca.
- `endswith(.csv)` tanpa tanda kutip → `SyntaxError`. Di sini kutip **wajib**, karena `.csv` itu teks.
- `open("sys.argv[1]")` **pakai** tanda kutip → semua file dianggap tidak ada, bahkan `regular.csv` yang jelas ada. Python malah mencari file yang namanya `sys.argv[1]`.
  - Ini **kesalahan berulang**. Kemarin di Lines saya sudah menanyakannya ke Duck (Kebingungan 4), tapi hari ini tetap tertulis pakai kutip.
  - Kunci membedakan: `".csv"` itu **teks** → pakai kutip. `sys.argv[1]` itu **variabel** → tanpa kutip.
  - Tips Duck: kalau program mencari file yang salah, `print` dulu nama filenya sebelum `open`, di dalam programnya.
- Di terminal Python (`>>>`), `print(sys.argv[1])` → `NameError`, karena `sys` belum di-import. Lagi pula terminal `>>>` tidak menerima command-line argument, jadi cara mengecek yang benar adalah `print` sementara di dalam `pizza.py`.

### Eksperimen di terminal
- Awalnya saya mencoba tabulate langsung dengan nama file tertentu, jadi tabel tetap muncul walaupun argumennya `ff.py` atau `sala.csv`. Setelah cek argumen dan `sys.argv[1]` dipasang dengan benar, pesan errornya muncul sesuai harapan.
- Sebelum check50, saya uji: tanpa argumen, dua argumen, file bukan `.csv`, file yang tidak ada, dan dua file pizza.

### Yang saya pelajari
- Baca soal dengan teliti: "outputs" artinya tampil di layar. Tidak semua soal file perlu menulis.
- Membaca dokumentasi library baru (tabulate) itu bisa. Contoh di dokumentasi langsung menunjukkan cara memakai `headers` dan `tablefmt`.
- Memakai ulang pola dari kode sendiri itu sah, asal paham kenapa polanya begitu.

## Yang ingin dicoba
- Coba `style50 lines.py` untuk melihat saran kerapian kode.
- Soal berikutnya: Scourgify.
- Ulangi beda tanda kutip: teks pakai kutip, variabel tanpa kutip.
