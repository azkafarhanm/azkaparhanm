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

Saya mulai sekitar jam 4.30 pagi, selesai jam 7.

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

### Tips belajar dari Claude
- Untuk pertanyaan "benar kan pakai ini?", **coba jalankan dulu di terminal**. Terminal adalah pemeriksa yang paling jujur: kalau salah, langsung error.
- **Tulis tebakan dulu** di komentar kode sebelum bertanya ke Duck. Di soal ini hampir semua tebakan saya benar (strip dulu, `endswith`, `try` di sekitar `open`).
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

## Pemanasan sebelum soal 3 (26 Oktober 2026)

Kuis Kosakata #5: **90%**, naik dari 60%. Empat frasa yang kemarin salah (*peek*, *resort to*, *break down*, *recap*) sekarang benar semua. Yang salah cuma **segue**, dibaca *SEG-wei* (mirip kendaraan Segway).

Pertanyaan coding:
1. **`"Potter, Harry"` dipecah tanpa spasi.** `split(",")` lalu `strip()` setiap bagian. Benar. Hasil `split(",")` itu `["Potter", " Harry"]`, ada spasi di depan `" Harry"`. Cara lain: `split(", ")` dengan koma + spasi sebagai pemisah.
2. **Membuat file baru lalu menulis.** Mode `"w"`. Benar.
3. **Method DictWriter untuk menulis header.** Saya jawab `fieldnames`, belum tepat. `fieldnames` cuma **memberi tahu** nama dan urutan kolom (contekan), belum menulis apa-apa ke file. Yang menulis baris header adalah **`writeheader()`**.
4. **Dua `open` dalam satu program** (satu baca, satu tulis). Bisa. Susunannya bisa berurutan atau bersarang.

## 3. Scourgify — selesai, check50 hijau semua 8/8 (26 Oktober 2026)

Yang diminta soal: program yang menerima **dua** command-line argument:
- file CSV lama untuk dibaca (`before.csv`), kolomnya `name` dan `house`, dengan nama berbentuk `"Potter, Harry"` (nama belakang dulu, koma, nama depan);
- file CSV baru untuk ditulis (`after.csv`), kolomnya `first`, `last`, `house`.

Setiap nama dipecah jadi nama depan dan nama belakang. Kalau argumennya tidak tepat dua, atau file pertama tidak bisa dibaca, keluar dengan `sys.exit`.

### Kebingungan 1: cara menyusun ulang datanya
- Awalnya saya bingung mencerna soal: file lama dibaca dulu sampai selesai, baru ditulis? Lalu bagian memisahkan nama itu di mana?
- Saya sempat mengira semua dictionary dari DictReader harus dikumpulkan dulu ke sebuah list.
- Ternyata **dua-duanya bisa**: kumpulkan ke list dulu, atau langsung proses dan tulis **baris per baris** di dalam loop. Saat loop membaca satu baris, informasinya sudah cukup untuk langsung ditulis.

### Kebingungan 2: `for name, house in reader` dengan DictReader
- Saya menulis `for name, house in reader`, seperti di lecture dengan `csv.reader` (list).
- Tapi DictReader memberi **satu dictionary utuh** setiap putaran, jadi tidak dibongkar ke dua variabel. Yang benar: `for row in reader`, lalu ambil isinya dengan key: `row["name"]`, `row["house"]`.

### Kebingungan 3: apakah baris header ikut masuk loop?
- Saya khawatir baris pertama (`name,house`) ikut dianggap data dan ikut diproses.
- Ternyata **DictReader memakai baris pertama sebagai key**, jadi tidak ikut masuk loop sebagai data.

### Kebingungan 4: membuka file output di dalam loop
- Saya sempat menaruh `with open` untuk file output **di dalam** loop.
- Akibatnya: kalau ada 3 baris data, file output dibuka 3 kali, dan `writeheader()` ikut berulang terus.
- Yang benar: buka file output **sebelum** loop, panggil `writeheader()` **sekali**, lalu `writerow()` **di dalam** loop untuk setiap baris.

### Kebingungan 5: bagaimana menyambungkan reader dan writer?
- Pertanyaan utama saya: hasil reader itu bagaimana "diserahkan" ke writer? Seperti `input` yang hasilnya disimpan di variabel lalu dipakai lagi.
- Saya kira kolom-kolom di `fieldnames` otomatis sudah terisi nilai dari reader. Ternyata **tidak otomatis**.
- **Jembatannya** adalah dictionary yang saya buat sendiri: key-nya nama kolom (`"first"`, `"last"`, `"house"`, pakai tanda kutip karena teks), value-nya variabel hasil split (tanpa kutip, tanpa f-string). Dictionary itu yang dikirim ke `writer.writerow(...)`.
- Yang menulis adalah **writer**, jadi `writerow` dipanggil di sisi file output, bukan reader.

### Kebingungan 6: urutan last dan first
- Nama di file lama ditulis **nama belakang dulu**. Jadi hasil split masuknya ke `last` dulu, baru `first`. Saya sempat menulis terbalik (`first, last = ...`).
- Saya memakai `split(", ")` (koma + spasi) supaya spasinya ikut hilang.

### Kebingungan 7: hanya satu baris yang tertulis
- Setelah program jalan, `cat after.csv` cuma berisi header dan **satu** orang: `Blaise,Zabini,Slytherin`, yaitu orang terakhir di file.
- Penyebabnya: loop ada di blok `with` reader, sedangkan `writerow` ada di blok `with` writer yang **terpisah**, di luar loop. Saat loop selesai, variabel `first`, `last`, `house` hanya menyimpan isi putaran **terakhir**, lalu itulah yang ditulis sekali.
- Masalahnya: kalau `writerow` dimasukkan ke loop reader, writer belum terbuka. Kalau sebaliknya, reader sudah tertutup (blok `with` menutup file begitu blok selesai).
- Solusinya: **kedua file dibuka bersamaan** sebelum loop. Bisa dalam satu `with` yang dipisah koma, atau `with` bertumpuk (yang kedua di dalam yang pertama). Dua-duanya sah.
- Nama `as` untuk kedua file **harus berbeda**. Kalau dua-duanya `as file`, nama kedua menimpa yang pertama.

### Error yang saya temui
- `csv.DictReader()` dan `csv.DictWriter()` tanpa isi: DictReader butuh file, DictWriter butuh file **dan** `fieldnames`.
- Indentasi `try` dan `except` sempat salah: isi `try` harus menjorok ke dalam, dan `except` harus sejajar dengan `try`.
- Kolom `row["home"]`, padahal di file lama nama kolomnya `house`. Nama key harus **persis sama** dengan header file.
- **"Could not read before.csv", padahal filenya ada.** Penyebabnya file **output** (`after.csv`) dibuka tanpa mode, jadi default-nya `"r"` (baca). File yang belum ada tidak bisa dibaca → `FileNotFoundError`. Perbaikannya: file output dibuka dengan mode **`"w"`**.
  - Pelajaran dari Duck: pesan error saya selalu menyebut `sys.argv[1]`, padahal yang bermasalah file kedua. Pesan error yang tidak sesuai penyebabnya bikin bingung saat debugging.
- `sys.exit("Could not read", sys.argv[1])` → `TypeError: exit expected at most 1 argument, got 2`. `sys.exit` hanya menerima **satu** pesan. Gabungkan dulu jadi satu string (pakai `+` atau f-string).
- Pesan sempat tertulis `Could not readbefore.csv` karena lupa spasi setelah "read".

### Yang saya pelajari
- `cat namafile` di terminal untuk melihat isi file hasil tulisan program.
- Blok `with` menutup file begitu blok selesai. Kalau butuh dua file terbuka sekaligus, bukanya bersamaan.
- Reader dan writer tidak tersambung otomatis. Saya yang menyambungkan lewat dictionary di `writerow`.
- `fieldnames` = contekan urutan kolom, `writeheader()` = menuliskan contekan itu sebagai baris pertama, `writerow()` = menulis satu baris data.

## 4. CS50 P-Shirt — selesai, check50 hijau semua 13/13 (26 Oktober 2026)

Dikerjakan malam harinya, setelah Scourgify. Soal baru, dan banyak dibantu petunjuk Duck.

Yang diminta soal: program yang menerima **dua** command-line argument, yaitu foto input dan nama file output. Program menempelkan (**overlay**) `shirt.png` yang background-nya transparan ke atas foto, setelah fotonya di-**resize dan di-crop** supaya ukurannya sama dengan shirt, lalu hasilnya disimpan sebagai output. Keluar dengan `sys.exit` kalau argumennya tidak tepat dua, ekstensinya bukan `.jpg`/`.jpeg`/`.png`, ekstensi input dan output berbeda, atau file input tidak ada.

### Memahami soal dulu
- **overlay** = menumpuk/menempelkan di atas. Jadi kaos ditempel di atas foto orang, bukan sebaliknya.
- Kenapa `shirt.png` berformat PNG? Karena PNG bisa punya bagian **transparan**. Ibarat plastik mika bergambar kaos yang ditaruh di atas foto: bagian bergambar menutupi foto, bagian bening membiarkan foto (kepala, latar) tetap terlihat.
- Alat yang disebut soal, berurutan: `Image.open` → `ImageOps.fit` → `Image.paste` → `Image.save`.

### Validasi argument
- `endswith` bisa menerima **beberapa akhiran sekaligus**, tapi harus dikemas sebagai **tuple**. Saya sempat menulis `endswith(".jpg", ".png")` dengan dua argumen terpisah, hasilnya `TypeError: slice indices must be integers`. Yang benar pakai kurung tambahan: `endswith((".jpg", ".png"))`, karena argumen keduanya sebenarnya adalah posisi awal potongan, bukan akhiran kedua.
- Untuk membandingkan apakah **ekstensi input sama dengan output**, `endswith` kurang cocok. Duck mengarahkan saya ke **`os.path.splitext`**:
  - `os.path.splitext("aku.py")` hasilnya **tuple** `('aku', '.py')`.
  - Saya sempat memanggil `splitext('aku.py')` langsung dan kena `NameError`. Lalu sudah `import os` pun tetap NameError, karena function itu ada di dalam `os.path`, jadi harus ditulis lengkap: `os.path.splitext(...)`.
  - Mengambil isi tuple pakai **indeks**, sama seperti list. Indeks 0 = nama file, indeks 1 = ekstensi. Saya belum pernah diajarkan ini di lecture, jadi ini pelajaran baru.
  - Bisa langsung `os.path.splitext(...)[1]` tanpa variabel perantara.

### Kebingungan: file mana yang saya buka dan isi?
- Saya bingung, apakah foto input itu "sudah terisi" atau saya yang mengisinya.
- Jawabannya ada di soal: **input = file yang user sediakan** (saya buka dan baca), **output = file baru hasil olahan saya** (saya simpan). `shirt.png` adalah file ketiga yang disediakan CS50, dan namanya ditulis langsung di kode karena selalu sama.
- Jadi ada tiga sumber gambar, dan `Image.open` dipanggil dua kali: untuk input dan untuk shirt.

### Kebingungan: ukuran resize-nya dari mana?
- Saya kira ukurannya bebas saya tentukan. Ternyata tidak: ukurannya **diambil dari shirt**, lewat `size = shirt.size` (hasilnya tuple lebar dan tinggi).
- Tujuannya supaya foto dan shirt **sama persis ukurannya**, baru bisa ditempel dengan pas.
- `ImageOps.fit` **me-return gambar baru**, jadi hasilnya harus ditangkap ke variabel. Saya sempat memanggilnya tanpa menyimpan hasilnya, jadi hasilnya hilang.
- Nilai di `image=im` ditulis **tanpa tanda kutip**, karena `im` itu variabel berisi objek gambar, bukan teks.

### Kebingungan terbesar: siapa yang ditempel ke siapa
- Pola dari soal: `photo.paste(shirt, shirt)`.
  - Yang **di depan titik** adalah gambar **dasar/background**.
  - Argumen pertama = gambar yang ditempel.
  - Argumen kedua = **mask**.
- Saya beberapa kali tertukar, sempat menulis shirt sebagai background dan foto sebagai tempelan. Duck memancing dengan pertanyaan: masuk akal tidak kalau foto orang ditempel di atas kaos? Dari situ baru nyambung: **yang jadi background adalah foto yang sudah di-fit**, dan shirt yang ditempel di atasnya.
- **Mask** itu semacam cetakan yang menentukan bagian mana yang ikut tertempel dan bagian mana yang dibiarkan tembus. Karena `shirt.png` punya area transparan, shirt dipakai **dua kali** (sebagai gambar dan sebagai mask) supaya bagian transparannya tetap transparan, tidak menutupi foto dengan kotak.
- `save` juga dipanggil dari objek background yang sama, dan nama file output diisi dari `sys.argv[2]`. Saya sempat menulis `image.save(image)`, padahal save butuh **nama file**, bukan objek gambar.

### Error yang saya temui
- `shirt.png` ukurannya **0 byte** sehingga muncul `PIL.UnidentifiedImageError: cannot identify image file`. Penyebabnya: saya sempat membuat file kosong dengan `code shirt.png`, lalu `wget` menyimpan file yang asli dengan nama `shirt.png.1` karena namanya sudah terpakai.
  - Cara mengeceknya: **`ls -l`** untuk melihat ukuran file. 0 byte hampir selalu berarti file kosong atau gagal diunduh.
  - Solusinya: hapus yang kosong, lalu ganti nama `shirt.png.1` jadi `shirt.png`.
- `NameError: name 'PIL' is not defined` saat memanggil `PIL.ImageOps.fit(...)`. Pola `from PIL import Image` membuat **`Image`** tersedia, tapi bukan `PIL` itu sendiri.
- `NameError: name 'Image' is not defined` setelah saya mengutak-atik baris import.
- "file does not exist" saat menjalankan `python shirt.py before1.png after.png`, padahal file muppet semuanya `.jpg`. Ternyata itu **pertanda bagus**: program saya memang benar menolak file yang tidak ada.
- Sebelum file muppet diunduh, folder cuma berisi `shirt.png` dan `shirt.py`. Cara mengeceknya: **`ls`**.

### Persiapan di terminal
- `wget <url>` untuk mengunduh `shirt.png` dan `muppets.zip`, lalu `unzip muppets.zip` untuk mengeluarkan `before1.jpg`, `before2.jpg`, `before3.jpg`.
- `pip install Pillow` (ternyata di codespace sudah terpasang).
- Saya sempat salah ketik `pytohn`, hasilnya `command not found`.

### Yang masih perlu diperbaiki (check50 hijau, tapi belum sesuai soal) → sudah diperbaiki 29 Oktober, lihat di bawah
Ini **kesalahan berulang yang keempat kalinya**: check50 hijau belum tentu semua aturan soal terpenuhi.

1. **`.jpeg` belum ditangani.** Soal menyebut tiga ekstensi: `.jpg`, `.jpeg`, dan `.png`. Tuple di `endswith` saya baru berisi dua.
2. **Belum case-insensitive.** Soal bilang pengecekan ekstensi harus mengabaikan huruf besar-kecil, jadi `FOTO.JPG` seharusnya diterima. Sekarang ditolak. Perlu disamakan dulu huruf besar-kecilnya sebelum dicek.
3. **Satu argumen bikin crash.** Saya mengecek `== 1` dan `>= 4`, jadi kasus **dua** isi `sys.argv` (satu file saja) lolos, lalu program crash `IndexError` saat mengambil `sys.argv[2]`. Ini persis masalah yang sudah saya perbaiki di Scourgify dengan `<= 2`, tapi lupa diterapkan di sini.
4. **Pesan error "Invalid output" kurang jelas**, padahal yang dicek input dan output sekaligus.

### Masukan desain dari Duck
- Validasi input dan output sebaiknya **simetris**: dua-duanya dicek dengan aturan yang sama.
- Pertimbangkan membungkus logika ke dalam `main()` dan function pembantu, supaya lebih rapi dan mudah dites.
- Nama variabel `im`, `image`, `resize` kurang menjelaskan perannya. Nama yang menyebut **foto** dan **shirt** lebih mudah dibaca, apalagi karena di sini ada beberapa gambar sekaligus.
- `shirt.png` dibuka tanpa `with`, jadi tidak dijamin tertutup rapi seperti input.
- Import sebaiknya konsisten: cukup `from PIL import Image, ImageOps`, lalu panggil `ImageOps.fit(...)` tanpa awalan `PIL.`.

### Yang saya pelajari
- `ls -l` untuk mengecek ukuran file, dan `wget` serta `unzip` untuk menyiapkan bahan soal.
- Tuple diakses dengan indeks seperti list.
- Pola `from X import Y` hanya menyediakan `Y`, bukan `X`.
- Untuk `paste`, yang di depan titik adalah **background**.

### Perbaikan 29 Oktober 2026

Empat hal yang belum sesuai soal sudah saya perbaiki. **Tidak saya submit ulang**, karena nilainya sudah 13/13. Perbaikan ini untuk pemahaman saya sendiri.

#### Hasil uji
| Perintah | Pesan yang keluar |
|---|---|
| `python shirt.py` | `Too few command-line arguments` |
| `python shirt.py foto.jpg` | `Too few command-line arguments` (dulu crash `IndexError`) |
| `python shirt.py a.jpg b.jpg c.jpg` | `Too many command-line arguments` |
| `python shirt.py catatan.txt out.txt` | `Invalid format` |
| `python shirt.py foto.jpg out.png` | `Input and output have different extensions` |
| `python shirt.py FOTO.JPG OUT.JPG` | berhasil (dulu ditolak) |
| `python shirt.py foto.jpeg out.jpeg` | lolos pengecekan format (dulu ditolak) |

`style50` bilang: *"Looks good, but consider adding more comments!"*

#### Penamaan itu penting
- Nama variabel lama (`im`, `image`, `resize`) saya ganti jadi `before`, `after`, dan `shirt`, supaya terlihat perannya masing-masing.
- Di soal ini ada beberapa gambar sekaligus. Nama yang tidak jelas gampang bikin salah paham, misalnya tertukar mana background dan mana tempelan, seperti yang sempat terjadi waktu mengerjakan.
- Ibarat di halaqah: lebih jelas memanggil "penyetor" dan "penyimak" daripada "santri 1" dan "santri 2".

#### Atribut vs metode
| | Atribut | Metode |
|---|---|---|
| Artinya | keterangan yang sudah menempel di objek | pekerjaan yang dijalankan objek |
| Ditulis | tanpa kurung | pakai kurung |
| Contoh di soal ini | `shirt.size` | `after.paste(...)`, `after.save(...)` |
| Contoh Week 6 | `file.name` | `file.write(...)` |

Patokannya: atribut itu **keterangan**, metode itu **perbuatan**.

#### `lower()` cuma singgahan
- `.lower()` menghasilkan string **baru**. `sys.argv[1]` aslinya tidak berubah, kecuali hasilnya disimpan ke variabel.
- Di soal ini justru itu yang dibutuhkan: `.lower()` dipakai sebentar untuk mengecek ekstensi, sedangkan nama asli (misalnya `FOTO.JPG`) tetap utuh untuk dibuka dengan `Image.open`.
- Kalau nama aslinya ikut diubah jadi `foto.jpg`, pengecekannya lolos tapi filenya tidak ketemu, karena **Linux itu case-sensitive**: `FOTO.JPG` dan `foto.jpg` dianggap dua file berbeda. Codespace CS50 memakai Linux. Windows sebaliknya, menganggap keduanya file yang sama.
- Saya sempat menyebutnya "case insensitive". Yang benar case-**sensitive**, artinya **membedakan** huruf besar-kecil.
- Ibarat menyalin nama santri ke kertas buram untuk dicocokkan dengan absen. Nama di rapor aslinya tidak ikut diubah.

#### Satu `except` memayungi semua baris
- Percobaan: `shirt.png` saya sembunyikan dengan `mv shirt.png shirt-simpan.png`, lalu menjalankan `python shirt.py before1.jpg after.jpg`. Hasilnya `File does not exist`, padahal `before1.jpg` ada. Yang hilang `shirt.png`. Setelah itu dikembalikan dengan `mv shirt-simpan.png shirt.png`.
- Sebabnya: `try` itu **satu payung besar**. `except FileNotFoundError` tidak peduli baris mana yang gagal, selama jenis errornya sama.
- Ini **bukan pelanggaran soal**, check50 tetap hijau. Cuma pesannya menyalahkan file yang salah, dan itu menyesatkan saat mencari masalah.
- Usul saya pesan "Invalid format", tapi kurang cocok: pesan itu sudah dipakai untuk ekstensi yang salah, jadi user akan mengecek ekstensinya padahal sudah benar. Pesannya harus tetap tentang file yang tidak ditemukan, tapi menyebut dua kemungkinannya, misalnya `Input file or shirt.png does not exist`.
- `shirt.png` juga dibuka tanpa `with`. Di program pendek ini tidak apa-apa, karena Python menutupnya sendiri saat program selesai. Ini soal kebiasaan untuk program yang lebih besar.

#### Komentar dalam bahasa Inggris
- Komentar itu bekal **murojaah**: saat menulis ulang dari layar kosong, saya tidak perlu membaca ulang soal untuk ingat kenapa sebuah baris ada. Juga untuk developer lain kalau nanti bekerja sama.
- Tulis **kenapa**, bukan **apa**.
- Tidak perlu kalimat lengkap. Cukup bentuk perintah pendek, diawali kata kerja, jadi tidak pusing soal tenses:

| Pola | Contoh |
|---|---|
| Check ... | `# Check that the user gave exactly two files` |
| Make sure ... | `# Make sure both files have the same extension` |
| Allow only ... | `# Allow only .jpg, .jpeg, and .png files` |
| Use ... only for ... | `# Use lower() only for checking, keep the original name` |
| Open ... and ... | `# Open the photo and resize it to fit the shirt` |

- Cara melatihnya: pikirkan dulu dalam bahasa Indonesia, cari kata kerjanya, lalu sambung dengan nama variabel yang sudah ada di kode.
- Koreksi komentar pertama saya:

| Yang saya tulis | Masalah | Lebih baik |
|---|---|---|
| Komentar yang sama ditulis dua kali, di atas cek "terlalu sedikit" dan "terlalu banyak" | Dobel | Cukup satu komentar di atas dua `if` itu |
| `# Make sure both files have the same extension` di atas cek format | **Salah tempat**: baris di bawahnya mengecek format yang diizinkan, bukan ekstensi yang sama | `# Allow only .jpg, .jpeg, and .png files` |
| `# file input and output must be same` | Urutan kata ala bahasa Indonesia ("file input"), dan tidak jelas apanya yang sama | `# Input and output files must have the same extension` |

- Pelajaran terpenting: **komentar harus cocok dengan baris di bawahnya.** Komentar yang salah tempat lebih membingungkan daripada tidak ada komentar.

## Penutup Problem Set 6 — selesai semua (26 Oktober 2026)

| Soal | check50 |
|---|---|
| Lines of Code | 9/9 |
| Pizza Py | 7/7 |
| Scourgify | 8/8 |
| CS50 P-Shirt | 13/13 |

### Pelajaran umum
- Semua soal Pset 6 polanya sama di awal: **cek command-line argument dulu, baru buka file.**
- `sys.argv[1]` ditulis **tanpa** tanda kutip (variabel), `".csv"` dan `".jpg"` **pakai** kutip (teks).
- Library baru (tabulate, Pillow) bisa dipelajari sendiri dari dokumentasinya. Bagian **Hints** di soal selalu menunjuk ke halaman dokumentasi yang tepat.
- Banyak function me-**return** objek baru, jadi hasilnya harus ditangkap ke variabel: `ImageOps.fit`, `replace`, `strip`.
- **check50 hijau belum tentu semua aturan soal terpenuhi.** Terjadi lagi di P-Shirt (`.jpeg`, case-insensitive, satu argumen). Program yang crash juga dianggap "exits", jadi check50 tetap hijau.

## Yang ingin dicoba
- Coba `style50 lines.py` untuk melihat saran kerapian kode.
- ~~Coba jalankan `python scourgify.py before.csv` (hanya satu argumen)~~ → sudah, hasilnya IndexError. Sudah diperbaiki jadi `<= 2` dan submit ulang.
- ~~Perbaiki shirt.py: tambah `.jpeg`, buat case-insensitive, perbaiki cek jumlah argumen, perjelas pesan error.~~ → sudah, 29 Oktober (tidak submit ulang).
- Buktikan Linux case-sensitive: di folder `shirt`, jalankan `ls HASIL.JPG` lalu `ls hasil.jpg`. Bandingkan hasilnya.
- Rapikan tiga komentar di `shirt.py` sesuai koreksi di atas.
- Ganti pesan `File does not exist` jadi pesan yang menyebut dua file.
- Lanjut **Week 7: Regular Expressions**.
- Ulangi beda tanda kutip: teks pakai kutip, variabel tanpa kutip.
