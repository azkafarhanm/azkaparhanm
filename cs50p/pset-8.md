# CS50P Problem Set 8: Object-Oriented Programming

## 1. Seasons of Love — selesai, check50 hijau 7/7 (17 November 2026)

Soalnya: meminta tanggal lahir dengan format `YYYY-MM-DD`, lalu mencetak sudah berapa menit kita hidup, dalam kata-kata bahasa Inggris, tanpa kata `and`. Ditambah `test_seasons.py` untuk menguji sendiri function selain `main`.

### Yang paling lama menyangkut: urutan kerjanya kebalik

Yang bikin saya berputar paling lama bukan rumusnya, bukan `timedelta`, bukan `replace`. Tapi satu pertanyaan: **`convert` itu sebenarnya menerima apa?**

Sebabnya saya menulis `seasons.py` dulu sampai jalan, baru menulis tesnya belakangan. Begitu tesnya ditulis, ternyata tesnya memanggil `convert` dengan string tanggal, padahal `convert` di kode saya menerima jumlah hari. Jadi strukturnya harus dibongkar ulang. Saya sampai memindahkan `try/except` ke dalam `convert`, lalu memindahkannya kembali ke `main`.

Soalnya sendiri bilang **either before or after**. Hari ini saya membuktikan sendiri kenapa "before" lebih hemat: tes itu memaksa saya memutuskan **apa yang masuk dan apa yang keluar** dari sebuah function, sebelum isinya ditulis.

Ini pelajaran yang sama dengan Week 5 tanggal 19 Oktober: tes harus mengikuti **spesifikasi**, bukan mengikuti kode saya sendiri. Hari ini kejadiannya malah terbalik.

### Pembagian tugas yang akhirnya benar

```
main     meminta input dari user
         menangkap error dengan try/except
         keluar dengan sys.exit kalau formatnya salah
         mencetak hasil

convert  membedah string jadi tanggal
         menghitung selisih
         mengubah angka jadi kata
         TIDAK menangkap errornya sendiri
```

Kenapa `convert` tidak boleh menangkap errornya sendiri: kalau dia menangkap lalu memanggil `sys.exit`, maka yang sampai ke pytest itu `SystemExit`, bukan `ValueError`. Tesnya jadi gagal padahal inputnya memang sengaja dibuat salah.

Dan saya tidak perlu menulis `raise ValueError` manual sama sekali. `split`, `int`, dan `date` **sudah otomatis** melemparkannya sendiri kalau inputnya buruk. Error itu lalu merambat naik dari `convert` ke tempat dia dipanggil, yaitu blok `try` di `main`.

Ini sambungan dari Pset 5 tanggal 20 Oktober: error naik lewat rantai pemanggilan sampai ketemu `except`.

### Tes saya ternyata bom waktu

Ini temuan terbesar hari ini, dan check50 **tidak menangkapnya**.

Versi pertama tes saya memeriksa tanggal lahir satu tahun lalu, dan `convert` memanggil `date.today()` sendiri di dalamnya. Hitungannya:

```
2025-11-17 sampai 2026-11-17  =  365 hari  ->  525.600 menit   (hijau hari ini)
2025-11-17 sampai 2026-11-18  =  366 hari  ->  527.040 menit   (gagal BESOK)
```

Tesnya akan gagal besok. Bukan karena kodenya rusak, tapi karena pembandingnya ikut berubah tiap hari.

check50 lolos karena dia dijalankan hari ini. Jenis masalah yang sama dengan daftar lama saya: **jalan hari ini, salah besok, tanpa satu pun error.**

Padahal CS50 Duck sudah menyinggungnya di awal: *fungsi yang mudah dites itu yang deterministik, beri input tertentu maka hasilnya selalu sama*. Saya waktu itu menjawab `date.today()` sebaiknya di `main` — dan jawaban saya **benar**. Tapi hilang waktu strukturnya dibongkar-pasang.

### Memisahkan tiga tugas di dalam convert

Waktu mau memperbaiki, saya hampir memindahkan satu gerombolan sekaligus lagi. Yang menyelamatkan itu memisahkan tugasnya satu per satu:

```
1. Membedah string jadi tanggal   -> ini yang BISA melempar ValueError
2. Mengambil tanggal hari ini     -> ini yang bikin hasilnya BERUBAH tiap hari
3. Mengurangi lalu mengubah kata  -> ini butuh hasil nomor 1 dan 2
```

Yang bikin tes gagal besok itu nomor 2. Yang menghidupkan tes ValueError itu nomor 1. Beda nomor, jadi **cukup nomor 2 yang dikeluarkan**.

Kalau nomor 1 ikut dikeluarkan, tes `pytest.raises(ValueError)` saya langsung mati, karena `convert` tidak lagi menyentuh `split`, `int`, atau `date`.

Lalu dari mana `convert` dapat tanggal hari ini kalau tidak boleh mengambil sendiri? Lewat **parameter**. Jadi parameternya jadi dua.

### Istilah barunya: dipaku (hardcoded)

```
pembanding pakai date.today()      -> berubah tiap hari, angka harapan jadi basi
pembanding dipaku sendiri          -> dua tanggal mati, selisih mati, hasil TETAP
```

Istilah ini sudah ada di catatan saya sejak Week 5 tanggal 16 Oktober, namanya *baked in* atau *hardcoded*, waktu angka 2 dan 3 ditulis langsung di tes kalkulator. Baru hari ini saya pakai sendiri dengan sadar.

### Error yang saya tabrak hari ini

```
TypeError: int() argument must be a string ... not 'list'
  -> int(input(...).split("-")), urutannya kebalik.
     int() tidak bisa mengubah satu list sekaligus.

ValueError: invalid literal for int() with base 10: '2000-05-21'
  -> int(input(...)).split("-"), kebalik lagi tapi sebaliknya.
     int() tidak bisa menelan "2000-05-21" utuh.

AttributeError: 'datetime.date' object has no attribute 'split'
  -> date.today().split("-"), split itu milik str, bukan milik date.

ValueError: not enough values to unpack (expected 3, got 1)
  -> input "20202" tanpa tanda hubung, split cuma menghasilkan satu bagian.

IndentationError: expected an indented block after 'try'
  -> blok try dibuka tapi isinya belum dimasukkan ke dalam.

SystemExit: Invalid date (di pytest)
  -> try/except masih di dalam convert, ValueErrornya keburu
     diubah jadi SystemExit sebelum sampai ke pytest.
```

### Jebakan replace yang makan waktu

Hasil `inflect` untuk 9009 itu `nine thousand and nine`. Saya mau buang kata `and`-nya.

```
replace("and", "")        -> "nine thous,  nine"   RUSAK
                             karena "and" di dalam "thousand" ikut kena

replace(" and", "")       -> benar
                             spasi di depan bikin yang menempel di kata lain aman
```

Dan ada argumen ketiga di `replace` yang membatasi **berapa kali** penggantian dilakukan, hitungannya seperti manusia (1 berarti sekali), bukan indeks, dan selalu mulai dari kiri.

Ini sambungan dari Pset 6: jebakan `replace` memang sudah pernah saya catat waktu Week 6.

### Kesalahan menulis yang berulang

Waktu memperbaiki tes, saya menulis:

```
convert("2026-11-17", "2026, 11, 17")
```

Itu **string**, bukan objek `date`. Saya pikir saya menyelesaikan masalah, padahal saya cuma menghindarinya — dan menukar satu error dengan error lain.

Lalu di percobaan berikutnya:

```
date(2026, 11, 17)     pakai koma  -> tiga angka, benar
date(2026-11-17)       pakai minus -> SATU hitungan pengurangan
                                      2026 - 11 - 17 = 1998
                                      jadi date(1998), penumpangnya kurang dua
```

Python tidak protes soal sintaksnya, karena `2026-11-17` itu pengurangan yang sah. Yang protes itu `date`, karena kursinya tiga tapi penumpangnya satu.

### Dunder sub

Saya pikir `__sub__` belum pernah dipelajari. Ternyata dia saudaranya `__add__` yang baru saya pelajari kemarin:

```
tanda +   ->  __add__
tanda -   ->  __sub__
```

Aturannya sama persis: Python lihat tipe di **sebelah kiri** tandanya, lalu cari method itu di class tersebut.

Dan hint di soal Seasons sendiri menyebutnya: class `date` **implements `__sub__`**, sehingga mengurangi dua objek `date` menghasilkan objek `timedelta`. Jadi `today - birthday` bisa jalan bukan karena tanggal itu angka, tapi karena penulis Python sudah menuliskan `__sub__` di dalam class `date`. Dan `.days` yang saya pakai itu atribut milik `timedelta`, benda yang dilahirkan oleh `__sub__` itu.

Percobaan saya sendiri di `train.py`:

```python
print("halo" + "dunia")        # halodunia
print("halo" - "dunia")        # TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("__sub__" in dir(str))   # False
print("__sub__" in dir(date))  # True
```

Jadi tanda `-` itu bukan hak semua benda. Dia cuma jalan di class yang penulisnya memang menuliskan `__sub__`.

Waktu menjalankan percobaan itu saya kena `NameError: name 'date' is not defined`, persis masalah yang sedang saya perbaiki di file tes, cuma pindah file. Aturan absen lagi: nama yang tepat sesudah `import` itulah satu-satunya yang masuk ke absen file itu, dan absen `seasons.py` bukan absen `test_seasons.py`.

### Kasus pinggiran

Tes saya cuma punya satu contoh normal, jadi saya coba kasus paling ujung: orang yang lahir hari ini juga, selisihnya nol hari.

```
convert tanggal hari ini lawan tanggal hari ini  ->  Zero minutes
```

Hasilnya benar, tidak ada yang rusak. Jadi yang bertambah itu **tesnya**, bukan kodenya. Gunanya: kalau suatu hari isi `convert` diubah, tes itu yang menjerit kalau kasus nol ikut rusak. Tes yang cuma punya satu contoh tidak bisa menjerit.

Ini *covering your bases* dari Week 5 tanggal 17 Oktober: positif, negatif, nol.

Lalu saya coba tanggal lahir di masa depan:

```
convert("2030-01-01", tanggal hari ini)
  ->  'Minus one million, six hundred forty-three thousand forty minutes'
```

Minus. Programnya tidak error sama sekali, cuma jawabannya tidak masuk akal buat manusia. Tapi spesifikasi tidak memintanya, dan check50 tidak mengetesnya, jadi dibiarkan. Kalau dipaksa ditolak, saya malah menambah aturan yang tidak diminta — kebalikan dari pelajaran Pset 7: baca spesifikasi untuk tahu **batas** tugas.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| REPL | Read Eval Print Loop, nama resmi mode interaktif Python yang `>>>` itu |
| hardcoded / baked in | dipaku langsung di kode, tidak dihitung atau diambil dari luar |
| deterministic | hasilnya selalu sama untuk input yang sama |
| propagate | merambat naik, error yang tidak ditangkap naik ke pemanggilnya |
| chaining | merantai beberapa method dalam satu baris |
| edge case | kasus pinggiran, kasus paling ujung yang biasanya terlupakan |
| overloading | memberi arti baru pada tanda operator lewat dunder method |


---

## 2. Cookie Jar — selesai, check50 hijau 12/12 (18 November 2026)

Soalnya: membuat class `Jar` dengan `__init__`, `__str__`, `deposit`, `withdraw`, dan dua property `capacity` dan `size`. Ditambah `test_jar.py` berisi **empat atau lebih** function tes.

Ini soal pertama yang memakai semua yang saya pelajari di Lecture 8 sekaligus.

### Atribut tidak bisa disimpan ke nama property

Percobaan pertama saya menulis `self.capacity = capacity` di dalam `__init__`, dan langsung meledak:

```
AttributeError: property 'capacity' of 'Jar' object has no setter
```

Jadi gudangnya harus bernama lain, `self._capacity`. Alasannya: `@property` **tanpa** `@capacity.setter` itu read-only, dan read-only menolak **semua** penulisan, termasuk penulisan oleh `__init__` sendiri.

Ini persis yang saya temukan tanggal 11 November waktu `house`, dan persis mekanisme `shirt.size` di Pset 6 yang dulu bikin bingung kenapa tidak bisa ditimpa.

Yang saya tanyakan: kalau ada setter, apakah `self.capacity = capacity` jadi boleh? Jawabannya **boleh**. Tapi itu memunculkan aturan kedua yang dulu saya campur jadi satu:

```
Aturan 1  ada setter atau tidak  ->  menentukan BOLEH menulis atau tidak
Aturan 2  nama gudang harus beda ->  menentukan RECURSION atau tidak
```

Di soal ini setter tidak dibutuhkan sama sekali, karena spesifikasinya cuma minta `capacity` bisa **dibaca**.

### isinstance

Istilah baru buat saya, dipakai untuk memeriksa apakah capacity itu benar-benar `int`.

```python
isinstance(8, int)     # True
isinstance(8, list)    # False
isinstance(8)          # TypeError: isinstance expected 2 arguments, got 1
```

Butuh **dua** argumen, bendanya dan classnya. Logis, karena pertanyaannya memang "benda ini jenisnya itu bukan" — dua hal.

Jebakan yang perlu diingat walaupun tidak diuji di soal ini:

```python
isinstance(True, int)    # True
```

Karena `bool` itu **anak** dari `int`. Inheritance lagi, persis pohon keluarga exception yang saya pelajari tanggal 16 November. `isinstance` menerima anaknya juga, bukan cuma yang persis.

### Validasi deposit: yang dibandingkan isi SETELAH ditambah

Versi pertama saya menulis `if n > self._capacity`. Kelihatannya benar, tapi salah.

```
kapasitas 12, isi 10, lalu deposit 5
  n > capacity     ->  5 > 12  ->  False  ->  LOLOS, isinya jadi 15
  n + size > cap   ->  15 > 12 ->  True   ->  ValueError, benar
```

Yang dibandingkan itu **isi sesudah ditambah**, bukan jumlah yang ditambahkan. Ini satu-satunya baris di `jar.py` yang pantas diberi komentar alasan, karena kodenya sendiri tidak menjelaskan kenapa ada `+ self._size` di situ.

### Menghitung bukan menyimpan

Saya sempat menulis penjumlahannya tanpa tanda sama dengan. Hasilnya dihitung lalu dibuang.

Pelajaran lama tanggal 6 Oktober: `int(x)` tidak mengubah `x`. Beda dengan `cards.sort()` yang memang mengubah di tempat; penjumlahan tidak.

### Property dipanggil tanpa kurung

Di tes pertama saya menulis `jar.capacity(12)`, hasilnya:

```
TypeError: 'int' object is not callable
```

Bacanya: `jar.capacity` **sudah selesai** dan menghasilkan `12`. Lalu `(12)` di belakangnya mencoba memanggil angka 12 seperti function. Angka tidak bisa dipanggil.

Jadi yang meledak bukan propertynya, tapi kurung yang menempel sesudahnya. Kembaran dari `print = 5` lalu `print("halo")` yang errornya sama persis.

Dan saya sempat menulis `Jar.capacity` dengan J besar. Itu bertanya ke **class**, bukan ke objek — aturan kiri titik yang saya pelajari tanggal 12 November.

### Import class berarti mengimpor cetakannya, bukan hasil cetakannya

```
from jar import Jar     ->  yang masuk ke absen cuma NAMA CLASSNYA
jar = Jar()             ->  objeknya saya bikin sendiri di file tes
```

Sama persis dengan `import random` yang cuma mendaftarkan nama `random`, bukan isinya. Cetakan tidak berguna sampai dipakai mencetak.

### Kode di dasar file ikut jalan saat file dipinjam

Waktu masih ada baris percobaan di dasar `jar.py`, tesnya belum sempat jalan sama sekali:

```
ERROR collecting test_jar.py
test_jar.py:1: from jar import Jar
jar.py:43:     jar.deposit(1)
ValueError: exceed capacity
```

Yang meledak bukan tesnya, tapi baris percobaan di dasar `jar.py` yang ikut dijalankan oleh `import`.

Lalu saya perhatikan sesuatu: kalau yang ditinggal cuma `jar = Jar()` saja, `pytest` **tidak error**. Jadi aturannya perlu saya tulis lebih tepat:

```
Yang TERJADI  : SEMUA baris di dasar file ikut jalan saat dipinjam. Tanpa kecuali.
Yang TERLIHAT : cuma yang bikin keributan.
                raise -> error, print -> nyetak, input -> pytest menggantung
```

`jar = Jar()` tetap dijalankan, cuma dia diam. Masuk daftar lama saya: **jalan tanpa error, tapi tetap salah tempat.** Patokan yang lebih aman daripada "errornya muncul atau tidak": file yang dibuat untuk dipinjam tidak menaruh apa-apa di dasarnya, kecuali yang dibungkus penjaga `if __name__ == "__main__":`.

### Tes yang saling bergantung

Versi pertama `test_jar.py` saya membuat toplesnya **sekali di atas**, lalu semua tes memakai toples yang sama. Akibatnya tiap tes bergantung pada baris di atasnya dan pada urutan tes.

Buktinya saya kena sendiri:

```
FAILED test_jar.py::test_invalid - Failed: DID NOT RAISE ValueError
```

Hitungannya begini:

```
kapasitas 12, isi 2 (karena ada deposit di atas)
  deposit(12)  ->  2 + 12 = 14  ->  lebih dari 12  ->  ValueError  ->  tes lolos

kalau deposit di atas dihapus, isi 0
  deposit(12)  ->  0 + 12 = 12  ->  TIDAK lebih dari 12  ->  tidak ada ValueError
               ->  DID NOT RAISE
```

Waktu itu saya memperbaikinya dengan menyesuaikan angkanya. Jalan, tapi itu menambal gejalanya.

Perbaikan yang benar: tiap tes membuat toplesnya **sendiri di dalam functionnya**, jadi toplesnya jadi **local variable** yang lahir dan mati di dalam tes itu. Setelah dirapikan, `test_invalid` tidak perlu hitung-hitungan lagi — toplesnya kosong, jadi `deposit(13)` jelas lewat kapasitas dan `withdraw(13)` jelas lebih banyak dari nol.

Dan pengulangan `jar = Jar()` di lima tempat itu **bukan** pengulangan yang perlu dibuang. Di kode biasa pengulangan itu masalah; di tes justru kemandirian.

Pelajarannya sama dengan Seasons kemarin: tes yang baik tidak bergantung pada apa pun di luar dirinya. Kemarin yang di luar dirinya itu tanggal hari ini, hari ini yang di luar dirinya itu tes sebelahnya.

### Soal komentar

Komentar di `jar.py` saya isi dengan salinan spesifikasi soal, supaya tidak bolak-balik ganti tab waktu ngoding. Itu sah selama mengerjakan. Tapi dua catatan untuk nanti:

```
Komentar di ujung kanan baris  ->  barisnya jadi sangat panjang
                                   lebih enak ditaruh di ATAS methodnya

Komentar salinan soal          ->  menjawab "apa yang diminta"
Komentar yang paling berguna   ->  menjawab "KENAPA kodenya begini"
                                   yaitu hal yang tidak terbaca dari kodenya
```

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| non-negative | tidak negatif, jadi nol ikut termasuk |
| exceed | melebihi, melampaui |
| collectively | secara bersama-sama, kalau digabung |
| thoroughly | sampai tuntas, menyeluruh |
| state | keadaan yang tersimpan di dalam objek |
| mock | mensimulasikan, memalsukan keadaan untuk keperluan tes |
| underlying | yang ada di bawahnya, yang mendasari |
| rubberducking | menjelaskan masalah ke benda mati sampai salahnya kelihatan sendiri |

---

## 3. CS50 Shirtificate — selesai, check50 hijau, sudah submit (19 November 2026)

Soalnya: meminta nama, lalu menghasilkan **PDF** berisi gambar kaos CS50 dengan tulisan "nama took CS50" di dadanya. Pakai library `fpdf2`.

**Dengan selesainya soal ini, SEMUA problem set CS50P tuntas.** Pset 0 sampai 8, sembilan problem set. Sisanya tinggal Week 9 (Et Cetera, tidak ada psetnya) dan final project.

### Error pertama: font harus dipasang sebelum menulis

```
fpdf.errors.FPDFException: No font set, you need to call set_font() beforehand
```

Jelas sekali pesannya, dan ini mengajarkan satu hal soal urutan: `pdf.cell(...)` itu **menggambar**, dan menggambar butuh tahu fontnya apa. Jadi `set_font` harus dipanggil lebih dulu.

Pola yang sama berlaku untuk `set_text_color`: pengaturannya berlaku untuk **semua yang digambar sesudahnya**, sampai diubah lagi. Jadi kalau judul hitam dan nama putih, `set_text_color` harus dipanggil **dua kali**, masing-masing sebelum cellnya.

### Pena yang tak terlihat

Ini yang paling lama bikin saya berputar. Teks keduanya tidak muncul, padahal kodenya ada.

Sebabnya: `fpdf` punya semacam **pena** yang posisinya berpindah sendiri setiap kali satu cell selesai digambar. Jadi cell kedua tidak mulai dari atas halaman, tapi dari tempat pena berhenti.

```
cell pertama h=210  ->  pena turun sejauh 210 mm
cell kedua          ->  mulai dari situ, sudah hampir di dasar halaman
                        teksnya ada, tapi di luar area yang terlihat
```

Pengaturnya `new_y`, nilainya `"TOP"`, `"LAST"`, atau `"NEXT"`.

Tapi yang akhirnya menyelesaikan masalah saya bukan itu, melainkan **mengambil alih kendalinya**:

```python
pdf.set_y(y=30)
pdf.cell(...)      # cell ini pasti mulai di 30 mm dari atas
```

Dengan `set_y`, tiap teks punya posisi yang pasti dan tidak saling memengaruhi. Tidak perlu lagi menghitung "kalau yang di atas tingginya sekian, yang ini jatuhnya di mana".

### Satuannya milimeter, bukan piksel

```
Halaman A4 = 210 mm lebar, 297 mm tinggi
Angka Y besar  ->  lebih ke BAWAH
Angka Y kecil  ->  lebih ke ATAS
```

Saya sempat mengira ini "rumus matematika" yang rumit. Ternyata cuma dua angka itu, sisanya coba-amati-sesuaikan.

### Menengahkan itu ada rumusnya, bukan tebak-tebakan

Waktu mengecilkan gambar kaos, saya menulis `x=15, w=180` dan kebetulan pas di tengah. Ternyata itu memang hitungan yang benar:

```
x = (lebar halaman − lebar gambar) ÷ 2
x = (210 − 180) ÷ 2 = 15
```

Untuk arah tegak rumusnya sama, tinggal ganti angka halamannya:

```
y = (297 − tinggi gambar) ÷ 2
```

Tapi di kasus saya ada ganjalan: saya cuma menulis `w=180`, tingginya tidak saya sebut. Jadi tinggi gambar di kertas belum saya ketahui.

### Tinggi gambar dihitung dari perbandingan aslinya

Percobaan yang saya jalankan:

```
python -c "from PIL import Image; print(Image.open('shirtificate.png').size)"
(593, 592)
```

Hampir persegi, bedanya satu piksel. Lalu hitungannya:

```
perbandingan  = tinggi_px ÷ lebar_px = 592 ÷ 593 = 0,9983
tinggi gambar = 180 × 0,9983 = 179,70 mm

y tengah = (297 − 179,70) ÷ 2 = 58,65 mm
```

Punya saya `y=70`, jadi bajunya memang sedikit di bawah titik tengah — dan itu benar, karena di atasnya ada judul yang butuh ruang.

Itu sebabnya `pdf.image` cukup diberi `w` saja: dia menghitung barisnya sendiri di balik layar supaya gambarnya tidak gepeng.

### Kenapa bajunya mepet waktu `w` belum ditulis

Di awal saya menulis `pdf.image("shirtificate.png", x=1, y=45)` tanpa `w`, dan bajunya mepet ke garis kiri kanan. Ternyata ada sebabnya:

```
fpdf menganggap 72 piksel = 1 inci = 25,4 mm
jadi 1 piksel = 25,4 ÷ 72 = 0,353 mm

593 piksel × 0,353 = 209 mm
```

**209 dari 210 mm.** Hampir selebar kertasnya. Jadi tanpa `w`, fpdf memakai lebar aslinya, dan lebar aslinya memang hampir selebar A4.

Dan yang harus saya ingat: kalau `w=593` ditulis, itu jadi 593 **milimeter**, hampir tiga kali lebar kertas. Angka di `w` itu milimeter, bukan piksel.

### size itu atribut, isinya milik objeknya

Saya sempat mengira `.size` itu angka tetap bawaan librarynya. Bukan. Yang tetap itu **bentuknya** — selalu tuple berisi dua angka. Isinya dibaca dari file gambarnya masing-masing.

```
jar.size      ->  jumlah cookie di toples ITU
gambar.size   ->  ukuran gambar ITU
```

Dua-duanya bernama `size`, dua-duanya atribut, dan dua-duanya bergantung pada objek yang ditanya. Pelajaran 6 November: atribut menempel ke objek, bukan ke class.

Dan `.size` **tidak mengukur** saat dipanggil. Ukurannya sudah dibaca waktu `Image.open(...)` dijalankan lalu disimpan di dalam objeknya. Itu sebabnya dia tanpa kurung.

```
tanpa kurung  (atribut)  ->  mengambil data yang SUDAH ada
pakai kurung  (method)   ->  menyuruh mengerjakan sesuatu SEKARANG
```

### Pelajaran terbesar hari ini: cara mencari di dokumentasi

Yang bikin saya lama bukan matematikanya, tapi **cara mencari**. Saya tahu mau "mengatur posisi vertikal", tapi yang saya buka malah `set_char_spacing` dan `set_stretching`. Lalu saya menyerah karena daftarnya terlalu panjang. Baru setelah disuruh `Ctrl+F` dengan huruf sumbu vertikal, `set_y` ketemu dalam hitungan detik.

Patokannya satu kalimat: **cari berdasarkan apa yang mau dilakukan, bukan dengan membaca daftarnya dari atas.**

Dan ada cara yang lebih cepat lagi daripada membuka situsnya, pakai alat yang sudah saya kenal sejak Figlet tanggal 13 Oktober:

```python
from fpdf import FPDF
pdf = FPDF()

for nama in dir(pdf):
    if nama.startswith("set_"):
        print(nama)
```

Keluar semua yang diawali `set_`, dan `set_y` menonjol sendiri. Kalau yang diingat cuma potongan katanya, saring dengan `in`:

```python
for nama in dir(pdf):
    if "font" in nama:
        print(nama)
```

Lalu setelah namanya ketemu, `help(pdf.set_y)` untuk melihat parameternya.

```
dir   ->  APA SAJA yang ada         (untuk MENCARI)
help  ->  cara pakai yang satu itu  (untuk SESUDAH ketemu)
dok.  ->  KENAPA dipakai, contoh, jebakannya
```

Urutan yang paling hemat: `dir` dulu untuk dapat namanya, `help` untuk parameternya, baru dokumentasi kalau masih ada yang janggal. Karena mencari `set_y` di dokumentasi itu satu kali lompat, sementara mencari "cara mengatur posisi vertikal" itu menyapu puluhan hasil.

`dir` sendiri artinya **directory** dalam arti daftar isi — seperti papan direktori di lobi gedung, bukan folder.

### Core fonts

Font bawaan `fpdf` yang bisa langsung dipakai tanpa menambah file:

```
helvetica
times
courier
symbol
zapfdingbats
```

Di luar itu harus ditambahkan sendiri dengan `add_font()` beserta file fontnya. Saya pakai `courier` untuk judul dan `helvetica` untuk nama.

### Import nganggur, kelima kalinya

```python
from PIL import Image, ImageOps
```

Tidak dipakai satu pun di versi akhir. Ini kali kelima pola yang sama: `import sys` nganggur tiga kali di Pset 7, `...` menggantung di Seasons, `jar = Jar()` di dasar `jar.py`, sekarang ini. Selalu sisa percobaan awal yang tidak ikut dibersihkan waktu arah kodenya berubah.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| explicit | disebutkan terang-terangan, tidak dibiarkan ditebak |
| orientation | arah kertas, portrait (tegak) atau landscape (mendatar) |
| portrait | kertas tegak, lebih tinggi daripada lebar |
| align | perataan teks secara mendatar di dalam cell |
| core fonts | font bawaan yang sudah tersedia tanpa perlu ditambahkan |
| aspect ratio | perbandingan lebar dan tinggi gambar |
| DPI | dots per inch, berapa piksel dianggap satu inci |
| directory | daftar isi (arti `dir`), bukan folder |
