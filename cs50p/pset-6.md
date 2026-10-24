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

## Yang ingin dicoba
- Coba `style50 lines.py` untuk melihat saran kerapian kode.
- Soal berikutnya: Pizza Py.
