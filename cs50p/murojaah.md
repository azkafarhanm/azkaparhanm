# Murojaah CS50P

Catatan menulis ulang soal lama dari layar kosong.
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Boleh buka dokumentasi.
Jadwal: setiap Minggu jam 05.20.

| No | Soal | Tanggal | Waktu | Hasil |
|---|---|---|---|---|
| 1 | Math Interpreter (Pset 1) | 4 Okt | 60 menit | check50 6/6 |
| 2 | Vanity Plates (Pset 2) | 5 Okt | 60 menit | check50 10/10 |
| 3 | Making Faces (Pset 0) | 11 Okt | 60 menit | check50 4/4 |
| 4 | Meal Time (Pset 1) | 17 Okt | 90 menit | check50 7/7 |
| 5 | Tip Calculator (Pset 0) | 25 Okt | 60 menit | check50 3/3 |
| 6 | Indoor Voice (Pset 0) | 1 Nov | 10 menit | check50 4/4 |
| 7 | CS50 P-Shirt (Pset 6) | 4 Nov | 90 menit | check50 13/13 |

---

## Murojaah 1: Math Interpreter, ditulis ulang dari layar kosong (4 Oktober 2026)

Waktu mengerjakan: 60 menit
Hasil: check50 hijau semua (6/6)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Boleh buka dokumentasi.

Yang saya cari di dokumentasi:
- Cara menampilkan satu angka di belakang koma. Nama resminya di dokumentasi Python adalah "format specification mini-language", bagian precision.

Error yang saya temui:
- `SyntaxError: invalid syntax` karena saya menulis tiga variabel berjajar tanpa operator. Python tidak tahu maksudnya apa.
- `TypeError: unsupported format string passed to tuple.__format__` karena di dalam curly braces saya menulis beberapa nilai dipisah koma. Koma itu membuat Python mengikatnya jadi satu paket namanya tuple. Aturan desimal tidak bisa dipakai untuk satu paket berisi beberapa angka.
- Saya juga sempat pakai `d`. Ternyata `d` itu untuk bilangan bulat (int), sedangkan untuk float pakai `f`.
- `TypeError: unsupported operand type(s) for +: 'float' and 'str'` karena saya menjumlahkan angka dengan y, padahal y isinya operator (tulisan), bukan angka kedua. Harusnya angka pertama dengan angka ketiga.
- Aturan desimal sempat saya tulis di luar curly braces lagi, jadi ikut tercetak sebagai tulisan. Ini kesalahan yang sama seperti waktu pertama mengerjakan.
- check50 sempat merah di "2 - 3" dengan actual kosong. Kalau tidak ada case yang cocok, match diam saja, tidak error dan tidak mencetak apa-apa.

Yang saya pelajari:
- Yang membuat tuple itu komanya, bukan kurungnya. `print(x, y, z)` tidak error, karena komanya memisahkan argument untuk print.
- Di dalam curly braces f-string, Python hanya mau satu nilai. Aturan setelah titik dua berlaku untuk seluruh isi curly braces, bukan cuma ke nilai yang paling dekat.
- Bedanya dengan not: not justru menempel ke syarat yang paling dekat, kecuali diberi kurung.
- Perhitungan boleh langsung ditulis di dalam curly braces f-string. Waktu pertama mengerjakan, saya membuat variabel result. Kemungkinan dulu saya kena error yang sama (salah variabel), lalu mengira format string-nya yang tidak bisa.
- Kode lama dan kode baru beda bentuk tapi logikanya sama. Yang baru lebih ringkas karena split langsung ditempel ke hasil input.

Perbandingan dengan pertama kali:
- Pertama kali (24 September) masih dibantu arahan. Sekarang dari layar kosong, error saya baca dan perbaiki sendiri.
- Murojaah berikutnya: sekitar awal November. Bandingkan waktunya.

---

## Murojaah 2: Vanity Plates, ditulis ulang dari layar kosong (5 Oktober 2026)

Waktu mengerjakan: 60 menit
Hasil: check50 hijau semua (10/10)
Yang saya buka: catatan GitHub saya sendiri (pset-2.md, tidak berisi kode jawaban) dan dokumentasi Python. Kode lama tidak dibuka, tidak bertanya ke AI.

Yang membuat saya tersendat:
- Aturan "angka pertama tidak boleh 0". Saya perlu memikirkan ulang cara pakai variabel penanda: cek 0 hanya selama penanda masih False, sesudah ketemu angka pertama penanda jadi True.
- Pengecekan isalnum. Saya sempat menulis `c.isalnum()` di bawah loop, padahal seharusnya `s.isalnum()`.

Kenapa `c.isalnum()` membuat PI3.14 lolos (Valid):
- Variabel loop c tetap ada setelah loop selesai, dan isinya huruf terakhir, yaitu "4".
- Jadi `c.isalnum()` di bawah loop cuma mengecek "4", bukan seluruh plat.
- Titik di PI3.14 juga lolos di dalam loop, karena titik bukan angka dan bukan huruf, jadi tidak ada if yang menanganinya. if yang False hanya melewati isinya, tidak membuat pengecekan gagal.
- Python tetap membaca semua baris dulu sampai selesai. Yang benar: `s.isalnum()`, cek seluruh plat.

Setelah lulus, bahas versi yang lebih ringkas:
- `plate == False` bisa ditulis `not plate`.
- `int(c) == 0` bisa ditulis `c == "0"`. c itu teks, jadi bandingkan dengan nol yang pakai tanda kutip.
- `else` sesudah `return False` tidak perlu. Kalau return jalan, function berhenti. Kalau Python masih sampai ke baris berikutnya, artinya return tidak jalan. Jadi `plate = True` cukup ditulis sejajar dengan if.
- Pola yang saya catat: kalau if diakhiri return, biasanya else-nya bisa dibuang dan isinya diturunkan sejajar dengan if.
- Kalau `plate = True` ditaruh di dalam if tepat di bawah `return False`, baris itu tidak akan pernah jalan. Namanya dead code.
- Ringkas itu bagus, tapi mudah dibaca lebih penting.

Yang masih mau dicoba:
- Tulis versi ringkasnya di file `plates2.py`, telusuri CS50 dan CS05 dengan tangan, lalu jalankan check50 lagi.

---

## Murojaah 3: Making Faces, ditulis ulang dari layar kosong (11 Oktober 2026)

Waktu mengerjakan: 60 menit
Hasil: check50 hijau semua (4/4)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Kali ini saya juga tidak membuka dokumentasi dan catatan GitHub. Murni dari ingatan.

Error dan kendala yang saya temui:
- check50 sempat merah 2 dari 4. Programnya jalan tanpa error, tapi emoji cemberut yang saya pakai salah wajah. Ketahuannya dengan membandingkan expected dan actual karakter demi karakter.
- `\n` di ujung actual itu normal, cuma tanda baris baru dari print. Bukan itu penyebab merahnya.
- check50 berkali-kali "Could not connect to GitHub". Ternyata bukan internet saya: `curl -I https://github.com` hasilnya HTTP/2 200. Gangguannya di jalur check50, dan setelah dicoba ulang akhirnya tersambung.
- `git` di folder CS50 memang sengaja dimatikan, jadi "Git is disabled" itu bukan error.

Perbandingan dengan kode lama:
- Kode baru saya pakai if sebelum replace, jadi barisnya lebih banyak. Kode lama langsung return hasil replace yang disambung dua kali, tanpa if.
- Ternyata if itu tidak perlu. Kalau tidak ada yang diganti, replace mengembalikan tulisan apa adanya.

Jebakan yang saya temukan setelah check50 hijau:
- Syarat saya: `":)" or ":(" in emoji`. Kelihatannya benar, tapi salah.
- `in` hanya menempel ke yang paling dekat, yaitu `":("`. Di kiri or tinggal `":)"` sendirian, tanpa pertanyaan.
- String yang ada isinya selalu dianggap True. Saya buktikan dengan `bool(":)")` hasilnya True. Jadi syarat itu SELALU benar, apa pun inputnya. Pengecekan senyum tidak pernah benar-benar terjadi.
- Yang benar: dua pertanyaan lengkap di kiri dan kanan or, yaitu `":)" in emoji or ":(" in emoji`. Tidak perlu tanda kurung.
- Setelah syaratnya saya betulkan, input `hello` malah mencetak `None`. Karena syaratnya False, isi if dilewati, function selesai tanpa return, lalu diam-diam mengembalikan None.
- Padahal soal minta `hello` dikembalikan apa adanya. Jadi versi yang "dibetulkan" itu salah, padahal check50 hijau. check50 tidak menguji input tanpa emotikon.
- Kesimpulan: versi lama tanpa if justru yang paling benar dan paling sederhana.

Murojaah konsep (dijawab dari ingatan):
1. Aturan desimal di f-string: lancar. Aturannya harus di dalam curly braces. Kalau di luar, tidak error tapi ikut tercetak sebagai tulisan. Yang membuat tuple itu komanya, bukan kurungnya.
2. Function tanpa return: awalnya saya kira "tidak ada apa-apa". Ternyata mengembalikan None, dan None itu tetap sebuah nilai (seperti amplop kosong yang tetap sampai). if menganggap None sebagai False, begitu juga 0 dan "" (string kosong).
3. Fuel Gauge: lancar setelah diingatkan konteks soalnya. Pengecekan yang menentukan reprompt harus di dalam loop sebelum break. Kalau di luar loop, program sudah tidak bisa bertanya lagi. Yang ditolak: angka negatif dan X > Y. X > Y sama dengan lebih dari 100%, misalnya 3/2 = 150%, tangki tidak mungkin lebih dari penuh.

Yang saya pelajari:
- Kode yang lulus check50 belum tentu bebas jebakan. Uji sendiri juga input yang tidak diuji check50.
- `in`, seperti `not`, menempel ke yang paling dekat.
- Kalau gagal tersambung, cek dulu masalahnya di mana (internet atau alatnya) sebelum panik.

Perbandingan dengan pertama kali:
- Pertama kali (19 September) saya kena TypeError dan NameError karena hasil convert tidak ditangkap. Sekarang bagian itu langsung benar dari ingatan.
- Murojaah berikutnya untuk soal ini: sekitar pertengahan November.

---

## Murojaah 4: Meal Time, ditulis ulang dari layar kosong (17 Oktober 2026)

Waktu mengerjakan: 90 menit
Hasil: check50 hijau semua (7/7)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Boleh buka dokumentasi.
Yang saya buka: setelah buntu lebih dari 30 menit, saya buka catatan GitHub saya sendiri (pset-1.md, tidak berisi kode jawaban). Yang saya lupa: cara mengubah 7:30 jadi 7.5. Ternyata menit dibagi 60 (satu jam = 60 menit), lalu ditambah jamnya.

Yang membuat saya tersendat:
- Lagi-lagi saya terlalu fokus di function convert. if elif untuk jam makan saya taruh di dalam convert, padahal convert tugasnya cuma mengubah waktu jadi angka. Yang memutuskan jam makan itu tugas main.
- Akibatnya, kalau jamnya di luar rentang makan (14:00, 21:00), convert selesai tanpa return, hasilnya None, dan None itu ikut ter-print. Saya lama bingung "kok None", malah sibuk mencari cara menghilangkan None-nya, sampai mencoba trik `else: pass`.
- split sempat saya taruh di main. Lalu convert tidak bisa memakai hours dan minutes, karena variabel di main tidak kelihatan dari dalam convert: `NameError: name 'hours' is not defined`.
- Saya sempat bingung convert harus menerima dua bahan (jam dan menit) padahal parameternya satu. Akhirnya ketemu: split dipindah ke dalam convert. convert menerima satu tulisan utuh seperti "7:30", lalu dipecah di dalamnya.
- check50 merah "convert successfully returns decimal hours", expected 7.5, actual Error. Ternyata check50 memanggil convert langsung dengan satu tulisan seperti "7:30". Jadi bentuk convert ditentukan oleh soal, bukan pilihan saya. Secara Python, function boleh saja punya dua parameter, tapi soal ini mau satu.

Error yang saya temui:
- `SyntaxError: invalid syntax` karena menulis `return pass`. pass bukan nilai, jadi tidak bisa di-return.
- `ValueError: not enough values to unpack (expected 2, got 1)` waktu saya ketik `21` tanpa titik dua. split cuma menghasilkan satu potongan, padahal di kiri ada dua variabel. (Soal bilang boleh assume input selalu benar bentuknya, jadi ini cuma percobaan.)
- `NameError: name 'time' is not defined` karena memakai variabel yang sudah saya ganti namanya.
- `SyntaxError: '(' was never closed` karena tanda kutip penutup saya taruh di luar kurung: `print("dinner time)"`.

Murojaah konsep (dijawab dari ingatan):
1. check50 hijau belum tentu bebas celah, karena check50 cuma menguji kasus yang dipilih pembuat soal. Mengecek semua kemungkinan itu mustahil, yang realistis uji per jenis: input normal, input di batas, input salah/aneh. Analogi saya: penguji tahfidz cuma menyimak beberapa ayat yang dia pilih. Santri lancar di ayat itu, belum tentu benar di seluruh surat. Di tes ala Week 5, "diam artinya lulus": penguji pegang mushaf, kalau bacaannya benar dia diam, baru menegur kalau salah.
2. `kartu = random.shuffle(kartu)`: shuffle mengacak list-nya langsung, lalu mengembalikan None. Kalau ditampung, list yang sudah teracak malah tertimpa None. Jadi tidak perlu ditampung ke variabel.
3. try/except: kalau try berhasil, except dilewati dan else dijalankan. Kalau try gagal, except yang jalan. except cuma menjaga baris di dalam try, jadi error di else tidak ditangkap, program crash. Di while True, setelah except jalan, program balik ke awal loop. Yang menghentikan loop cuma break.

Yang saya pelajari:
- Setiap function punya tugasnya sendiri. convert = mengubah, main = memutuskan dan mencetak.
- Variabel di satu function tidak bisa dilihat function lain. Bahan dari luar masuk lewat parameter.
- None sudah muncul tiga kali (Making Faces, shuffle, Meal Time). Polanya sama: function selesai tanpa return, lalu hasilnya dipakai. Kalau melihat None di layar, pertanyaan pertama: function mana yang selesai tanpa return?
- Setelah hijau, rapikan: blok `"""else: pass"""` di bawah return itu dead code (tidak akan pernah jalan), dan komentar #hours #minutes yang sudah tidak dipakai, dihapus.

Perbandingan dengan pertama kali:
- Pertama kali (24 September) saya masih dibantu arahan soal letak split dan `__name__`. Sekarang `if __name__ == "__main__":` langsung saya tulis dari ingatan, dan letak split saya temukan sendiri lewat error.
- Rumus menit dibagi 60 masih lupa, harus buka catatan. Ini yang perlu diulang.

---

## Murojaah 5: Tip Calculator, ditulis ulang dari layar kosong (25 Oktober 2026)

Waktu mengerjakan: 60 menit
Hasil: check50 hijau semua (3/3)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Saya cuma membuka dokumentasi Python (string methods). Catatan GitHub tidak dibuka.

Yang saya temukan sendiri di dokumentasi:
- `removeprefix` untuk membuang `$` di awal dan `removesuffix` untuk membuang `%` di akhir. Waktu pertama mengerjakan saya pakai replace.
- Bedanya: removeprefix/removesuffix hanya membuang di awal/akhir, replace membuang di mana saja. Untuk soal ini removeprefix lebih tepat maksudnya.

Error yang saya temui:
- `TypeError: can't multiply sequence by non-int of type 'float'`. Sequence di sini artinya string. dollars masih berupa tulisan, belum jadi angka. Nyambung dengan catatan Einstein: `"3" * 2` jadi `"33"` (string dikali int = diulang), tapi string dikali float tidak bisa.
- `SyntaxError: invalid decimal literal` dua kali, karena saya menulis `:.1f` di luar f-string (di return dan di dalam float). Aturan desimal hanya hidup di dalam curly braces f-string. Ini kesalahan berulang sejak Math Interpreter.
- Saya juga sempat ingin membulatkan desimal di dalam function, padahal tidak perlu. Ini salah tebak yang sama seperti waktu pertama mengerjakan (20 September).

Murojaah konsep (dijawab dari ingatan):
1. Function yang cuma print tanpa return: tes assert menerima None, jadi gagal. Tulisan print memang muncul di layar, tapi tes tidak melihat layar, cuma menerima yang di-return. Seperti santri yang membaca di kamar sendiri tapi tidak menyetor ke penguji. (None keempat kalinya.)
2. `assert value("hey")` tanpa `==`: saya sempat tertukar, mengira yang dicek "hey". Ternyata yang dicek HASILNYA (100 atau 20). Angka selain 0 dianggap True, jadi dua-duanya lolos. Tesnya cuma memastikan "bukan kosong", tidak menyimak berapa angkanya. Seperti ustadz yang cuma bertanya "santri ini membaca sesuatu atau tidak?" tanpa menyimak bacaannya.
3. KeyError: kuncinya tidak ada di dictionary. ValueError: jenisnya benar tapi isinya tidak cocok, misalnya `int("abc")`, atau split menghasilkan 3 potongan padahal variabelnya 2 (too many values to unpack). ValueError tidak selalu dari user, data dari file atau API juga bisa.

Yang saya pelajari:
- Kalau tidak tahu method-nya, cari di dokumentasi string methods. Ternyata saya bisa menemukannya sendiri.
- Kali ini saya lebih banyak mengulik dulu. Awalnya saya kira desimal harus diatur di dalam function supaya angkanya rapi. Setelah membaca dokumentasi, baru sadar ternyata bisa langsung saja: function cukup mengembalikan angkanya, pengaturan desimal urusan f-string di print. Banyak hal terbuka lewat dokumentasi, termasuk waktu mencari-cari prefix dan suffix.
- Kode yang ditulis langkah demi langkah tidak apa-apa. Mudah dibaca lebih penting daripada ringkas.
- Rapikan: indentasi harus konsisten 4 spasi (dollars_to_float sempat 5 spasi), dan biasakan pakai `if __name__ == "__main__":` seperti di Week 5.

Perbandingan dengan pertama kali:
- Pertama kali (20 September) saya kena TypeError karena pembagian 100 ada di dalam kurung float. Sekarang urutannya langsung benar: jadikan float dulu, baru dibagi 100.
- Pertama kali pakai satu baris padat `float(d.replace("$", ""))`. Sekarang langkah demi langkah: buang prefix, jadikan float, return.
- Yang masih berulang: aturan desimal di luar f-string. Ini yang perlu diulang.

  ---

## Murojaah 6: Indoor Voice, ditulis ulang dari layar kosong (1 November 2026)

Waktu mengerjakan: 10 menit
Hasil: check50 hijau semua (4/4)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan.

Error yang saya temui: tidak ada. Langsung hijau sekali jalan.

Perbandingan dengan pertama kali (19 September):
- Dulu saya kena NameError karena mengira lower bisa berdiri sendiri, lalu
  AttributeError karena lower saya tempelkan ke function input, bukan ke
  string hasilnya. Sekarang langsung benar dari ingatan.
- Dulu lower sempat ditulis tanpa parentheses, jadi methodnya cuma disebut
  dan belum dijalankan. Sekarang tidak terulang.
- Dulu check50 saya jalankan tanpa slug sehingga error. Sekarang langsung
  lengkap dengan alamat soalnya.

Catatan: soal ini terasa ringan. Yang dulu susah di sini adalah errornya,
bukan logikanya. Murojaah berikutnya ambil yang lebih berat.
Saya tidak menulis rencana sebagai komentar #. Untuk soal sependek ini
tidak terasa perlu, tapi tetap harus dibiasakan untuk soal yang panjang.


---

## Murojaah 7: CS50 P-Shirt, ditulis ulang dari layar kosong (4 November 2026)

Waktu mengerjakan: tidak dicatat  
Hasil: check50 hijau semua (13/13)  
Aturan: kode lama tidak dibuka, tidak bertanya ke AI, Copilot dimatikan. Saya mengerjakan tanpa CS50 Duck. Yang saya gunakan hanya spesifikasi soal, petunjuk/dokumentasi yang dirujuk soal, catatan Week 6 saya sendiri, dan dokumentasi Python/Pillow.

### Yang saya ingat dan susun sendiri

Program menerima nama file foto input dan file output lewat command-line argument. Saya melakukan pemeriksaan jumlah argumen, ekstensi kedua file, dan apakah ekstensi input sama dengan ekstensi output. Setelah itu foto dibuka, ukuran gambar kaus dibaca, foto di-fit ke ukuran kaus, kaus ditempel sebagai overlay, lalu hasilnya disimpan ke nama file output.

Kali ini saya masih ingat alur utama P-Shirt dari awal sampai akhir. Terminal tidak mencetak pesan saat berhasil karena program menyimpan gambar ke file. Saya bisa membuka hasilnya, seperti `after1.jpg`, `after2.jpg`, dan `after3.jpg`, untuk melihat gambar jadi.

### Yang sempat tersendat

- **Nama library Pillow dan nama import-nya berbeda.** Saya sempat mengira harus menulis `import Pillow`. Dokumentasi dan percobaan mengingatkan bahwa nama paket instalasinya Pillow, tetapi namespace yang dipakai di kode adalah `PIL`: `from PIL import Image, ImageOps`.
- **Salah tanda saat memberi argumen bernama.** Saya menulis `image: photo` pada pemanggilan `ImageOps.fit`, lalu mendapat `SyntaxError: invalid syntax`. Untuk memberi nilai pada keyword argument, sintaksnya memakai tanda sama dengan: `image=photo`. Titik dua dipakai untuk hal lain, misalnya anotasi tipe atau awal blok, bukan untuk mengisi argumen fungsi.
- Saya bolak-balik antara catatan Week 6, dokumentasi Python, dan spesifikasi soal beserta hints. Membaca ulang urutan kerja dan fungsi yang disebut soal membantu saya mengingat hubungan antara foto, ukuran shirt, hasil fit, paste, dan save.

### Perbandingan kode lama dan kode murojaah

Sekarang saya sudah memberikan tangkapan layar kode lama, jadi bagian ini membandingkan dua kode yang benar-benar terlihat. Kode lama sudah menangani ekstensi yang diizinkan, kapitalisasi, jumlah argumen, dan kecocokan ekstensi input/output. Jadi pemeriksaan tersebut bukan hal baru di kode murojaah; cara menuliskannya yang berubah.

| Bagian | Kode lama | Kode murojaah |
|---|---|---|
| Import path | `import os`, lalu `os.path.splitext(...)` | `from os import path`, lalu `path.splitext(...)` |
| Ekstensi yang diizinkan | Memakai `endswith((".jpg", ".png", ".jpeg"))` setelah `.lower()` | Menyimpan `.jpg`, `.jpeg`, `.png` dalam list `ekstensi`, lalu membandingkan hasil `path.splitext(...)[1]` yang sudah di-`.lower()` |
| Samakan ekstensi input/output | Membandingkan hasil `os.path.splitext(...)[1]` dari kedua nama setelah `.lower()` | Logika sama, memakai `path.splitext(...)[1]` |
| Nama gambar | `before` untuk foto input dan `after` untuk hasil fit | `photo` untuk foto input dan `picture_fit` untuk hasil fit |
| Penjelasan di kode | Ada komentar untuk pemeriksaan argumen, ekstensi, proses gambar, dan error file | Versi baru lebih sedikit komentar; nama variabelnya lebih menjelaskan objek yang dipegang |
| Pesan file hilang | `Input file or shirt.png does not exist` | `File does not exist` |

#### Apa yang berubah dan apa artinya

- **Import `os.path` disingkat.** Keduanya benar. Kode lama memanggil `os.path.splitext`; kode baru mengimpor bagian `path` saja, jadi pemanggilannya menjadi `path.splitext`. Hasil dan tugasnya sama.
- **Pengecekan ekstensi ditulis dengan cara berbeda.** Kode lama bertanya, “Apakah nama ini berakhir dengan salah satu akhiran yang diizinkan?” lewat `endswith`. Kode baru mengambil bagian ekstensi setelah titik lewat `splitext`, lalu bertanya apakah ekstensi itu ada di list. Keduanya mengubah nama menjadi huruf kecil dulu, jadi `.JPG` dan `.jpg` sama-sama diterima. Kode baru membuat daftar ekstensi terlihat sebagai data tersendiri; kode lama menuliskan pilihan langsung di dalam `endswith`.
- **Pemeriksaan jumlah argumen pada dasarnya tetap sama.** Keduanya menolak jumlah yang terlalu sedikit dengan `len(sys.argv) <= 2` dan terlalu banyak dengan `len(sys.argv) >= 4` atau bentuk setara `> 3`. Ingat bahwa `sys.argv[0]` adalah nama program; dua nama file berarti panjang daftar tepat 3.
- **Nama variabel gambar berubah.** `before` dan `after` di kode lama sudah menggambarkan urutan sebelum/sesudah, sedangkan `photo` dan `picture_fit` di kode baru lebih langsung menjelaskan bahwa objek pertama adalah foto dan objek kedua adalah foto hasil penyesuaian. Ini membuat argumen untuk `ImageOps.fit`, `paste`, dan `save` lebih mudah ditelusuri.
- **Pesan error file hilang menjadi lebih umum.** Pesan lama menyebut dua kemungkinan file yang tidak ditemukan: foto input atau `shirt.png`. Pesan baru lebih singkat, tetapi tidak memberi petunjuk file mana yang perlu diperiksa.
- **Ada komentar yang lebih lengkap pada kode lama.** Komentar seperti “Use lower() only for checking, keep the original name” mengingatkan kenapa nama asli tidak diubah. Kode murojaah lebih ringkas; jika nanti dibaca ulang, komentar pendek tentang alasan itu bisa membantu.
- **Bagian overlay intinya sama.** Kedua versi mengambil ukuran dari `shirt.size`, mengubah foto dengan `ImageOps.fit`, memakai `shirt` sebagai gambar tempelan sekaligus mask di `paste`, lalu menyimpan hasil ke nama output. Nama variabel hasilnya saja yang berbeda.
- **Kedua versi membungkus pembukaan foto dengan `with`, tetapi membuka `shirt.png` tanpa `with`.** Ini sama-sama berhasil di soal. Catatan lama sudah menandai bahwa menutup kedua file secara eksplisit akan lebih rapi sebagai kebiasaan.

Perbaikan ekstensi `.jpeg`, huruf besar-kecil, jumlah argumen, dan kecocokan ekstensi sudah ada di kode lama setelah revisi 29 Oktober. Pada murojaah kali ini saya berhasil menulis ulang pengecekan itu dari awal, bukan baru menambahkannya. Error `image: photo` adalah kesalahan ketik sementara saat menyusun kode murojaah; bentuk yang benar adalah `image=photo`, seperti pada kode lama yang terlihat di gambar.

Perbandingan ini sekarang mengacu pada kedua tangkapan layar kode, bukan hanya ringkasan lama di `pset-6.md`.
### Error dan pemeriksaan terminal

- Error sintaks `image: photo` hilang setelah saya mengganti titik dua dengan `=`.
- Saya menjalankan program untuk tiga foto yang tersedia, `before1.jpg`, `before2.jpg`, dan `before3.jpg`; hasilnya tersimpan tanpa perlu mencetak apa pun.
- Saya juga mencoba `python shirt.py before.jpg after.jpg`. Program menjawab `File does not exist` karena file bernama `before.jpg` memang tidak ada; file yang tersedia bernama `before1.jpg`, `before2.jpg`, dan `before3.jpg`. Ini bukan kerusakan proses overlay, tetapi percobaan yang memastikan pengecekan file hilang bekerja.
- Check50 terakhir lulus semua 13/13, termasuk validasi argumen/ekstensi serta hasil overlay pada enam gambar uji.

### Yang saya pelajari

- Nama paket untuk `pip install` tidak harus sama dengan nama yang dipakai untuk `import`.
- Keyword argument memakai bentuk `nama=nilai`; kesalahan satu tanda baca bisa membuat program gagal dibaca Python.
- `ImageOps.fit` membuat hasil gambar baru; simpan hasilnya sebelum memanggil `paste` atau `save`.
- Saat perintah berhasil menyimpan file, terminal bisa tetap diam. Periksa file output untuk melihat hasilnya.
- Pengerjaan ulang terasa jauh lebih ringan daripada saat pertama kali. Saya bisa merakit program tanpa bantuan Duck dengan mengandalkan spesifikasi, dokumentasi, dan catatan belajar sendiri.
