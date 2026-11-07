# CS50P Week 8: Object-Oriented Programming

## Hari 1 – 6 November 2026

Mulai Lecture 8, sampai sekitar **menit 31** (bagian atribut, sebelum `__init__`). Pagi: Kuis Harian #10 dan pemanasan murojaah, lalu membahas kode Pset 7 soal 4 dan 5. Ngoding 2 jam, bahasa Inggris 10 menit.

### Kuis Harian #10

18 soal, giliran Hari ke-4: Week 3 dan Week 0, plus lima soal kemarin yang diulang dengan bentuk berbeda. Hasilnya **12/18**.

Yang salah:

| No | Materi | Koreksinya |
|---|---|---|
| 2 | break vs continue | Yang menghasilkan 1, 2 itu **break**. Saya jawab continue, padahal kemarin sudah benar bahwa continue menghasilkan 1, 2, 4 |
| 3 | dua jenis for loop | `for student in students` tidak punya `i`, jadi NameError. Kebalikan dari soal kemarin |
| 11 | kosakata | rub someone the wrong way = bikin tidak nyaman, ada yang mengganjal |
| 16 | print vs return | Function yang isinya cuma print menampilkan 25 di layar, tapi variabel penampungnya berisi **None** |
| 17 | TypeError vs NameError | `hello("azka")` pada function tanpa parameter itu **TypeError**, muncul saat pemanggilan. NameError muncul lebih belakangan, waktu isi resep dibaca |
| 18 | sep | `sep` **mengganti** spasi bawaan, bukan menambah. Jadi hasilnya `halo,-parhan` |

Soal 2 dan 3 itu ulangan yang **salah lagi**. Tapi setelah dicoba sendiri di terminal, ternyata bukan karena tidak paham, melainkan **kurang teliti membaca soal**. Obatnya beda: bukan belajar ulang, tapi baca pelan-pelan dulu sebelum memilih. Ini sejenis dengan check50 hijau yang tetap meleset dari syarat soal.

### Pemanasan murojaah

Tiga pertanyaan tentang prinsip merapikan kode regex kemarin, semuanya benar dari ingatan tanpa membuka catatan: dua tugas kurung, kenapa menangkap teks tetap itu berputar-putar, dan kenapa urutan alternatif pendek-dulu tetap bukan kebiasaan baik.

---

## Lecture 8: dari procedural sampai class

David membangun satu program kecil secara bertahap, dan setiap tahap memunculkan masalah yang mendorong tahap berikutnya. Urutannya:

```
1. tiga baris polos (procedural)
2. dipecah jadi get_name dan get_house
3. digabung jadi get_student     → muncul masalah: return cuma bisa satu nilai
4. dibungkus tuple               → muncul masalah: student[0] tidak terbaca maksudnya
5. diganti dictionary            → lebih terbaca, tapi masih bukan "tipe santri"
6. class                         → bikin tipe data sendiri
```

Kalimat kuncinya: menulis function itu *"not necessarily because it solves the problem more correctly"*. Kode tiga barisnya sudah benar apa adanya. Yang berubah cuma **bisa dikembangkan atau tidak**. Ini argumen yang sama persis dengan waktu saya merapikan `numb3rs.py` kemarin.

### Tuple

- `return name, house` itu sebenarnya **white lie**. Python tetap mengembalikan **satu** nilai, cuma dibungkus jadi tuple.
- Yang membuat tuple itu **komanya**, bukan tanda kurungnya. Dibuktikan dengan `x = "Harry", "Gryffindor"` lalu `type(x)`.
- Bedanya dengan list **bukan** soal banyak atau sedikit isinya, tapi **bisa diubah atau tidak**:

```
list   → mutable, isinya boleh diubah belakangan
tuple  → immutable, isinya tidak boleh diubah
```

- Percobaan saya:

```python
daftar = ["Harry", "Gryffindor"]
daftar[0] = "Ron"          # boleh

pasangan = ("Harry", "Gryffindor")
pasangan[0] = "Ron"        # TypeError: 'tuple' object does not support item assignment
```

- Kata David, pesan error itu **arcanely expressed**, bahasanya tidak ramah. Terjemahan gampangnya: "assignment itu menyalin dari kanan ke kiri", dan tuple tidak mengizinkan itu.
- Penting: tidak bisa diubah itu **feature**, bukan bug. Memang sengaja dirancang begitu.

### Kenapa dikunci justru jadi kelebihan

Tebakan saya: "untuk menjaga". Ternyata benar, dan alasannya dua:

1. **Aman dari perubahan tak sengaja.** Kalau ada kode lain yang keliru menimpa isinya, Python langsung menolak. Pakai list, perubahannya terjadi diam-diam tanpa protes — jenis bug yang paling susah ketahuan, sama seperti `csv.writer` yang menukar kolom.
2. **Menyatakan niat.** Orang yang membaca langsung tahu data ini memang tidak dimaksudkan berubah.

Ibarat data setoran yang sudah ditandatangani: itu arsip, bukan buku coretan. Dikunci justru supaya bisa dipercaya.

### Jebakan: list di dalam tuple

Saya bertanya sendiri, apa bisa mengubah list yang ada di dalam tuple. Ternyata **bisa**, dan ini mengejutkan:

```python
t = ("Harry", ["Gryffindor", "Seeker"])

t[0] = "Ron"             # TypeError
t[1].append("Captain")   # BOLEH
t[1][0] = "Ravenclaw"    # BOLEH
```

Saya sempat menyimpulkan "bisa ditambah tapi tidak bisa diganti". Itu **salah**, karena `t[1][0] = ...` itu mengganti dan tetap berhasil.

Yang benar, pembedanya **siapa yang diubah**:

```
t[0] = ...        → mengubah tuple-nya sendiri    → DITOLAK
t[1][0] = ...     → mengubah list di dalam slot   → BOLEH
t[1].append(...)  → mengubah list di dalam slot   → BOLEH
```

Dua yang boleh itu tidak menyentuh tuple sama sekali. Slot nomor 1 tetap menunjuk ke list yang sama dari awal sampai akhir.

Analogi loker: tuple itu rak yang lokernya dilas, isinya tidak bisa ditukar dengan benda lain. Tapi kalau di dalam loker ada tas, tasnya tetap boleh dibuka, ditambah, bahkan ditukar bajunya. Yang tuple larang cuma **menukar isi lokernya**.

### Kenapa dictionary lebih baik daripada tuple di sini

Masalahnya ada di baris seperti ini:

```python
print(f"{student[0]} from {student[1]}")
```

Saya sempat mengira `student[0]` sudah memberi tahu bahwa itu nama. Ternyata **tidak**. Yang tahu itu saya, karena saya ingat urutannya dari baris `return`. Kodenya sendiri tidak menyebut "nama" di mana pun. Kalau file ini saya buka tiga bulan lagi dan cuma melihat baris itu, saya harus gulir ke bawah dulu untuk tahu mana nama dan mana asrama.

Dan kalau urutannya tertukar, programnya **tidak error**. Dia tetap jalan dan mencetak `Gryffindor from Harry`. Salahnya baru ketahuan kalau ada manusia yang membaca hasilnya. Tema berulang lagi: **salah tanpa error itu lebih berbahaya daripada error**.

Dictionary menyelesaikan ini karena punya **better semantics**:

```
syntax     → BENTUK penulisannya, sah menurut aturan bahasa
semantics  → MAKNANYA, apa yang sebenarnya dimaksud
```

`student[0]` itu syntactically valid tapi semantiknya kosong. `student["name"]` maknanya ikut menempel di kodenya. Bedanya seperti tulisan Arab yang khat-nya benar tapi salah harakat: bentuknya sah, maknanya meleset.

Alasan praktis dari David: kalau nilainya ada tiga, empat, atau lebih, cepat atau lambat saya atau rekan kerja akan lupa urutannya lalu menulis kode yang bug.

Catatan penulisan: kutip ganda di dalam f-string yang juga pakai kutip ganda bikin Python bingung. Harus beda jenis, `f"{student['name']}"`. Ini sudah ada di catatan Week 6 saya, sekarang baru jelas alasannya.

### Kenapa akhirnya butuh class

Argumen David, tiga langkah:

1. **Pengandaian**: seandainya pembuat Python langsung menyediakan tipe data `student`, kita tidak perlu ribut memilih tuple, list, atau dictionary.
2. **Kenapa mustahil**: itu **slippery slope**, lereng licin, sekali dimulai tidak ada habisnya. Kalau ada `student`, kenapa tidak `teacher`, `book`, `santri`, `setoran`? Pembuat bahasa tidak mungkin menebak semua jenis data yang dibutuhkan semua programmer di dunia.
3. **Solusinya**: mereka memberi **alat serbaguna** — list, dict, tuple — dan satu alat serbaguna lagi, yaitu **class**.

Jadi Python tidak memberi saya tipe `Santri` jadi, tapi memberi saya **alat untuk membuat tipe `Santri` sendiri**.

Catatan: `class` di Python bukan kelas sekolah. Kata David itu **coincidentally** terdengar nyambung karena contohnya `Student` dan santri memang ikut kelas, tapi tidak ada hubungannya. Sama seperti `print_column` di Week 2 yang bukan `print` bawaan Python.

### Objek, akhirnya terbuka

Ini bagian yang paling kebuka hari ini, karena sebelumnya saya masih remang-remang.

Pemahaman saya yang lama: objek itu "korban" yang ditempeli function, misalnya di `name.lower()`, objeknya adalah `name`.

Ternyata **salah**. Yang jadi objek bukan `name`. `name` itu cuma nama panggilan. Objeknya adalah **tulisannya sendiri**. Buktinya, tanpa variabel sama sekali tetap jalan:

```python
"azka".lower()
"azka farhan".split()
(5).bit_length()
```

Jadi yang saya tulis sendiri di Week 6 itu benar: **objek = orangnya, variabel = nama panggilan yang ditempelkan ke orang itu.**

Lalu `type()` membuka hal berikutnya:

```
type("azka")                  → <class 'str'>
type(5)                       → <class 'int'>
type([1, 2, 3])               → <class 'list'>
type(open("coba.txt", "w"))   → <class '_io.TextIOWrapper'>
type(print)                   → <class 'builtin_function_or_method'>
```

Kata yang muncul di semua hasil itu: **class**. Jadi `str` itu class, dan `"azka"` itu satu objek yang dibuat dari class itu. Class-nya yang menentukan objek itu bisa apa — makanya `lower` ada di `str` tapi tidak ada di `int`.

Ini juga yang saya tulis sendiri di Week 6 tanpa sadar: *"Library menyediakan SOP petugas (namanya class, Week 8). Petugasnya baru dibuat saat kode dijalankan."*

```
class    → SOP / cetakan (mold)
objek    → petugasnya, hasil cetakannya
atribut  → DATA yang dimilikinya
method   → KEMAMPUAN yang dimilikinya
```

Arahnya: **objek dibuat dari class**, bukan class ditempelkan ke objek. Satu cetakan bisa menghasilkan banyak benda, dan masing-masing berdiri sendiri.

### Membaca kode class baris per baris

Bagian ini yang paling lama saya pahami. Tiga baris, tiga peristiwa berbeda:

```python
student = Student()         # satu objek baru lahir dari cetakan Student
student.name = input(...)   # membuat atribut name pada objek itu
return student              # menyerahkan satu benda utuh
```

```
Student     → cetakannya (class), huruf besar
Student()   → memakai cetakan itu untuk membuat SATU benda baru
student     → nama panggilan untuk benda yang baru lahir
student.name → atribut milik benda itu
```

Huruf besar-kecilnya cuma **convention**, bukan aturan Python.

`Student()` memang **terlihat persis seperti memanggil function**, lengkap dengan kurung. Itu bukan kebetulan; nanti kurungnya juga bisa diisi argument. Polanya sama dengan yang sudah saya pakai sejak Week 4:

```
Figlet()         → objek Figlet
Image.open(...)  → objek Image
csv.writer(f)    → objek writer
Student()        → objek Student
```

Semuanya: **panggil sesuatu, dapat objek, pakai atribut dan method-nya.**

### Atribut vs method

```
atribut  → data,       tanpa kurung   → student.name, shirt.size
method   → kemampuan,  pakai kurung   → file.write(), shirt.resize()
```

Saya sadar `shirt.size` di Pset 6 ternyata atribut, dan isinya **tuple** berisi lebar dan tinggi. Jadi tuple sudah saya pakai sejak Pset 6 tanpa sadar — persis yang David maksud dengan *"we've actually dabbled"*.

Dan masuk akal kenapa ukuran gambar disimpan sebagai tuple: itu data yang tidak seharusnya diubah sembarangan. Di PIL, `size` memang dibuat read-only; cara mengubah ukuran lewat method `resize()`, yang menghasilkan gambar **baru**, bukan mengubah aslinya. Pola yang sama dengan `lower()`.

Kesalahan saya di sini: mengira atribut berarti tidak bisa diubah. **Salah.** Atribut biasa bisa diubah. Yang tidak bisa diubah itu tuple-nya, dan `shirt.size` kebetulan saja berisi tuple. Dua pertanyaan yang harus dipisah:

```
Atribut?       → soal CARA mengambilnya (pakai titik)
Bisa diubah?   → soal JENIS benda yang disimpan di dalamnya
```

### Atribut menempel ke objek, bukan ke class

Percobaan yang membuktikannya:

```python
class Rumah:
    ...

a = Rumah()
b = Rumah()
a.cat = "biru"
print(a.cat)    # biru
print(b.cat)    # AttributeError: 'Rumah' object has no attribute 'cat'
```

Padahal `b` dibuat dari cetakan yang sama. Artinya mengisi `a.cat` tidak menyentuh class maupun `b` sama sekali. Tiap objek punya catatannya sendiri.

Analogi blangko setoran:

```
class Rumah      → blangko kosong yang saya rancang
Rumah()          → fotokopi satu lembar blangko baru
a.cat = "biru"   → mengisi kolom di lembar itu saja
```

Blangko aslinya tetap kosong, dan lembar milik orang lain juga tetap kosong.

Atribut itu seperti **bahan atau ciri** dari bendanya: `rumah.cat`, `rumah.lampu`, `student.name`.

### Yang masih menggantung

Sampai di sini, atribut masih diisi **dari luar** class, satu per satu. Itu rapuh: programmer bisa lupa mengisi salah satunya, atau salah ketik `student.nmae` dan Python diam saja. Objeknya tetap lahir tapi cacat, dan error-nya baru muncul jauh belakangan.

Juga terlihat ada ketimpangan:

```
atribut  → sejauh ini dibuat dari LUAR class
method   → selalu ditulis di DALAM class
```

`__init__` nanti memindahkan pengisian atribut ke dalam class, jadi satu paket dengan kelahiran objeknya.

### Kosakata

| Kata | Arti |
|---|---|
| dabble | menyentuh sedikit-sedikit, mencoba tanpa mendalami |
| invariably | selalu, tanpa kecuali |
| encounter | menemui, menjumpai (ketemu dengan sendirinya) |
| gradually | sedikit demi sedikit, bertahap (sinonim incrementally) |
| stumble upon | tersandung, menemukan tanpa sengaja |
| trimming | memangkas, merapikan pinggirannya (seperti `.strip()`) |
| spit back out | memuntahkan kembali, menampilkan ulang mentah-mentah |
| necessary / unnecessary | perlu / tidak perlu (awalan un- artinya tidak) |
| not necessarily | belum tentu, bukan serta-merta karena |
| lay the foundation | meletakkan fondasi (lampau: laid) |
| building blocks | balok-balok susun, bahan untuk dibangun ke atas |
| paint oneself into a corner | menjebak diri sendiri, terpojok oleh ulah sendiri |
| white lie | bohong putih; di sini: penyederhanaan yang tidak sepenuhnya akurat |
| coincidence / coincidentally | kebetulan / secara kebetulan |
| arcane / arcanely expressed | sulit dipahami / diungkapkan dengan bahasa yang tidak ramah |
| semantics | makna (lawan pasangannya: syntax, bentuk penulisan) |
| garbled | kacau, tidak jelas (suara atau teks yang rusak) |
| at hand | yang sedang dihadapi sekarang |
| to hand | sudah tersedia, siap dipakai (beda dengan at hand) |
| consolidate | menggabungkan jadi satu, memadatkan |
| mold | cetakan |
| slippery slope | lereng licin, sekali dimulai tidak ada habisnya |
| custom | buatan sendiri, bukan bawaan |
| apt | pas, tepat (nama yang apt = nama yang pas) |
| mutable / immutable | bisa diubah / tidak bisa diubah |

Kata lama yang muncul lagi dan tetap bikin blank: **arcane** (Week 4 dan 5), **as is** dan **quote/unquote** (Week 6), **mouthful** (Week 3). Catatan saja ternyata tidak cukup, perlu diulang lewat kuis.

Pasangan yang gampang tertukar dan perlu dikuiskan berpasangan: `at hand` vs `to hand`, `necessary` vs `unnecessary`, `syntax` vs `semantics`, `lay` vs `lie`.

### Yang mau dicoba

- Jalankan `a = Rumah()` dan `b = Rumah()` sendiri, isi atribut yang beda, lalu cek `a is b`.
- Coba `shirt.size` di Pset 6 lalu `type()`-kan hasilnya, buktikan itu tuple.
- Coba `t = ("Harry", ["Gryffindor"])` lalu `t[1][0] = "Ravenclaw"` sekali lagi dari layar kosong.
- Lanjut lecture dari menit 31, bagian `__init__`. Berhenti dan tanya waktu sampai di **`self`**.

---

## Hari 2 – 7 November 2026

Hari pendek. Kuis Harian #11 dan pemanasan murojaah saja, lecture belum dilanjut. Ngoding 30 menit, bahasa Inggris 10 menit.

### Kuis Harian #11

19 soal, giliran Hari ke-5: Week 4 dan Week 1, plus enam soal kemarin yang diulang dengan bentuk berbeda. Hasilnya **14/19**.

Enam soal ulangan kemarin **benar semua** kali ini, termasuk nomor 2 dan 3 yang dua hari berturut-turut salah. Berarti dugaan kemarin tepat: masalahnya ketelitian membaca, bukan pemahaman.

Yang salah hari ini:

| No | Materi | Koreksinya |
|---|---|---|
| 10 | white lie | Penyederhanaan yang tidak sepenuhnya akurat, bukan kebohongan untuk menipu |
| 13 | consolidate | Menggabungkan jadi satu, memadatkan. Lawannya **decompose** dari Week 2 |
| 14 | import | `import random` lalu `choice(...)` itu **NameError**. Jawaban saya sudah benar isinya, cuma nama error-nya belum saya sebut |
| 15 | shuffle | `cards = random.shuffle(cards)` hasilnya **None**, bukan NameError |
| 17 | if terpisah | Dua `if` yang tumpang tindih mencetak **dua baris**, tidak error |

### shuffle dan None: salah untuk ketiga kalinya

Ini sudah tiga kali meleset: catatan Week 4 Hari 2, murojaah 11 Oktober, dan sekarang kuis #11. Jadi perlu dicatat lebih tegas.

Percobaan yang saya jalankan sendiri:

```python
import random
cards = ["jack", "queen", "king"]
cards = random.shuffle(cards)
print(cards)
```

Hasilnya **`None`**, dan **tidak ada error sama sekali**.

Dua hal yang selalu saya campur:

| Yang saya kira | Yang benar |
|---|---|
| NameError, karena shuffle tidak boleh disimpan ke variabel | Boleh saja disimpan, tidak ada aturan yang melarang. Nama `cards` juga dikenal sejak baris kedua |
| Isinya None karena shuffle tidak butuh variabel | Isinya None karena **shuffle tidak punya return** |

Alasannya bukan soal boleh atau tidak boleh, tapi soal **apa yang diserahkan**. Dan ini ternyata bukan materi baru — persis sama dengan soal nomor 16 di kuis kemarin:

```
def square(x): print(x * x)     → number = square(5)        → number berisi None
random.shuffle(cards)           → cards = random.shuffle(…) → cards berisi None
```

Dua-duanya function yang **mengerjakan sesuatu** tanpa **menyerahkan** apa pun. `square` menampilkan ke layar, `shuffle` mengubah list aslinya di tempat. Hasil kerjanya nyata, tapi tangannya kosong waktu pulang.

Rumus yang saya tulis di Week 0 perlu ditambah satu:

```
print    → showing, menampilkan ke layar
return   → giving, menyerahkan nilai
shuffle  → doing, mengubah di tempat
```

Yang ketiga ini juga tidak memberi apa-apa, jadi hasilnya None kalau dipaksa disimpan.

Catatan kecil: saya juga sempat lupa shuffle itu apa, dan mengira ada hubungannya dengan angka 6. Angka 6 itu dari **permutation** (3 kartu punya 6 kemungkinan urutan), beda hal. shuffle = mengacak urutan list.

### Tema yang muncul lagi: salah tanpa error

Soal nomor 17 menambah satu contoh lagi ke daftar yang sudah panjang minggu ini:

```
dua if yang tumpang tindih   → mencetak dua baris, tidak error
csv.writer urutan tertukar   → data tertukar, tidak error
student[0] urutan tertukar   → nama dan asrama tertukar, tidak error
[1-9]|1[0-2] dengan search   → jam 12 terbaca 1, tidak error
cards = random.shuffle(...)  → list hilang jadi None, tidak error
```

Semuanya program yang tetap jalan mulus padahal hasilnya salah. Jenis bug yang paling susah ketahuan, dan cuma bisa ditangkap kalau hasilnya benar-benar diperiksa.

### Pemanasan murojaah

Empat pertanyaan tentang materi OOP kemarin, dijawab dari ingatan tanpa membuka catatan. Nomor 2, 3, dan 4 benar:

- Atribut tanpa kurung, method pakai kurung. Itu patokan tercepat.
- Di tuple, slotnya tidak bisa ditukar tapi isi list yang ada di dalam slot tetap bebas diubah.
- `student["name"]` lebih baik daripada `student[0]` karena semantiknya lebih kuat: tidak perlu mengingat urutan, tidak perlu menggulir ke bawah, dan tidak rawan tertukar.

Nomor 1 (class vs objek) ingatannya kabur dan saya mencampur dua analogi sekaligus. Koreksinya: pilih satu dan konsisten.

```
class = denah rumah   →  objek = rumah yang dibangun dari denah itu
class = SOP petugas   →  objek = petugasnya
```

Yang penting arahnya: **objek dibuat dari class**. Satu denah bisa jadi banyak rumah, dan tiap rumah punya cat dan lampunya sendiri.

### Yang mau dicoba

- Lanjut lecture dari menit 31, bagian `__init__`. Berhenti dan tanya waktu sampai di **`self`**.
- Ulangi percobaan shuffle dari layar kosong besok, jangan baca catatan ini dulu.
