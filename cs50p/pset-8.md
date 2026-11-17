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

### Yang mau dicoba

- Lanjut ke soal berikutnya di Problem Set 8.
