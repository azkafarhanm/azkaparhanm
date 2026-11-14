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

---

## Hari 3 – 8 November 2026

Lanjut Lecture 8 dari menit 31, sampai bagian `__init__` dan `self`. Paginya Kuis Harian #12, pemanasan, dan Murojaah 8 (catatannya di `murojaah.md`). Ngoding 2 jam, bahasa Inggris 10 menit.

### Kuis Harian #12

18 soal, giliran Hari ke-6: Week 5 dan Week 2. Hasilnya **13/18**. Enam soal ulangan benar semua lagi.

Yang salah:

| No | Materi | Koreksinya |
|---|---|---|
| 7 | dabble | Menyentuh sedikit-sedikit, memakai tanpa mendalami |
| 9 | trimming | Memangkas pinggirannya, seperti `.strip()`. Satu keluarga dengan *trailing* |
| 10 | mold | Cetakan, bukan hasil cetakannya |
| 16 | for di dict | Yang keluar **key**-nya, bukan isinya. Untuk isinya: `santri[x]` |
| 18 | abstraksi | Memberi nama pada sekumpulan langkah, pemakainya cukup tahu APA bukan BAGAIMANA |

Pola yang saya sadari: ketiga kosakata yang salah (7, 9, 10) adalah kata yang **dijelaskan ke saya di tengah menonton**, bukan yang saya baca dari catatan. Kata yang masuk sambil nonton ternyata paling cepat menguap.

### Instance, instantiation, instance variable

Tiga istilah yang bentuknya mirip dan sempat saya campur. Peta yang benar:

```python
student = Student()        # baris INI instantiation
student.name = "Harry"
```

```
Student           → class (blueprint / cetakan)
Student()         → instantiation, proses pembuatannya
objek / instance  → benda yang lahir dari baris itu
student           → variabel, nama panggilan untuk benda itu
.name .house      → atribut, juga disebut instance variable
```

Kesalahan saya:

| Yang saya kira | Yang benar |
|---|---|
| Variabel itu namanya instance | Variabel cuma nama panggilan. Instance itu bendanya |
| Hasil cetakan dari class itu atributnya | Yang keluar dari cetakan itu **seluruh bendanya**. Atribut adalah bagian dari benda itu |
| Instantiation itu baris pengisian atribut | Instantiation itu baris `Student()`. Baris atribut cuma **mengisi** benda yang sudah lahir |

Bukti bahwa variabel bukan instance:

```python
a = Student()
b = a
```

Ada **satu** instance tapi **dua** nama panggilan. Kalau variabel sama dengan instance, harusnya ada dua.

Saya sempat menyimpulkan "objek itu yang dibuat pertama kali, variabel sesudahnya bukan objek". Itu juga salah, karena bukan soal urutan. Patokannya **benda vs nama**: `a` itu variabel pertama, tapi tetap cuma nama. Cara mengenali di kode: lihat sisi **kanan** tanda sama dengan — `Student()` di kanan itu yang melahirkan bendanya.

Istilah lain yang muncul di menit yang sama: **incarnation** (perwujudan, sudah ada di catatan Week 4), dan **boil down to** (intinya adalah, dari catatan Week 3).

Catatan ejaan: istilahnya **instance**, bukan "instansi". Kalau salah tulis, pencarian di dokumentasi jadi meleset.

### Objek lahir dalam keadaan kosong

Ini yang paling lama mengganjal. Kalau class-nya masih `...` alias kosong, apa yang lahir dari `Student()`?

Jawabannya: **benda kosong**. Objek tetap ada walaupun belum punya isi.

```python
class Student:
    ...

a = Student()
print(a)         # <__main__.Student object at 0x0000020458AD86E0>
print(type(a))   # <class '__main__.Student'>
```

Bendanya sudah ada, punya jenis, bahkan punya alamat di memori — padahal belum ada satu atribut pun.

Analogi blangko (formulir kosong yang sudah ada kolomnya, seperti kertas rekap nilai tahfidz):

```
class Student   → rancangan kolomnya
Student()       → fotokopi SATU lembar baru
a.name = ...    → menulis di kolom lembar itu saja
```

Lembar fotokopinya sudah ada wujudnya begitu keluar dari mesin, walaupun semua kolom masih kosong. Keberadaannya tidak bergantung pada terisi atau tidak.

### Atribut yang ada vs yang tidak pernah dibuat

Saya sempat mengira atribut "tidak keluar kalau tidak dipanggil". Perlu dipisah dua keadaan:

| Keadaan | Hasilnya |
|---|---|
| Atribut sudah dibuat, cuma tidak di-print | ADA, tersimpan di objeknya, tinggal diambil kapan saja |
| Atribut tidak pernah dibuat | TIDAK ADA sama sekali, AttributeError |

`print` itu kegiatan **melihat**, bukan yang membuat atributnya ada. Yang membuatnya ada adalah baris `a.cat = "biru"`. Seperti lampu yang sudah terpasang di rumah: tetap ada walaupun sedang tidak dilihat.

Catatan istilah: atribut **diakses**, method **dipanggil**. Kata "memanggil" (*call*) biasanya khusus untuk yang bertanda kurung.

### `__init__`

Yang otomatis dijalankan saat objek lahir. Tidak pernah saya panggil sendiri — begitu `Student(...)` dijalankan, Python langsung menjalankannya.

Namanya dunder, satu keluarga dengan `__name__` dan `__init__.py`. Init = *initialize*, menyiapkan.

Gunanya: memindahkan pengisian atribut dari luar ke **dalam** class, jadi satu paket dengan kelahiran objeknya.

### `self`: dibuktikan, bukan dihafal

Percobaan yang membuka semuanya:

```python
class Student:
    def __init__(self, name, house):
        print("di dalam init:", self)
        self.name = name
        self.house = house


a = Student("Harry", "Gryffindor")
print("di luar      :", a)
```

Hasilnya:

```
di dalam init: <__main__.Student object at 0x0000020458AD86E0>
di luar      : <__main__.Student object at 0x0000020458AD86E0>
```

Alamatnya **sama persis**. Jadi `self` dan `a` itu benda yang sama. `self` = objek yang sedang lahir itu sendiri.

Urutan kejadiannya:

```
1. Student("Harry", "Gryffindor") dipanggil
2. Python membuat objek kosong
3. Python memanggil __init__, objek kosong tadi dimasukkan
   otomatis ke parameter pertama → self
4. "Harry" → name, "Gryffindor" → house
5. self.name = name → mengisi kolom di objek itu
6. Objek yang sudah terisi diserahkan ke a
```

Makanya jumlahnya kelihatan tidak cocok:

```
Student("Harry", "Gryffindor")     → saya kirim 2
def __init__(self, name, house)    → Python tambahkan 1 di depan, jadi 3
```

### `self` bukan keyword

Saya buktikan dengan mengganti semua `self` jadi `aku`. Jalan normal. Dan waktu saya baru mengganti sebagian, muncul:

```
NameError: name 'self' is not defined
```

Persis seperti salah ketik nama variabel biasa. Kalau `self` itu keyword, error-nya pasti lain.

Tapi tetap ditulis `self`, tiga alasannya:

1. Semua dokumentasi Python memakainya.
2. Kode dibaca orang lain, termasuk saya sendiri nanti.
3. Linter dan VS Code memberi peringatan kalau parameter pertama bukan `self`.

Sama seperti huruf besar pada nama class: bukan aturan Python, tapi kesepakatan yang dipatuhi semua orang.

### `self.name = name`: dua `name` yang berbeda

Kata David: *"we are adding the variable to object, aka instance variable to object."* (**aka** = *also known as*, disebut juga.)

```
name        → parameter, variabel biasa, mati begitu __init__ selesai
self.name   → atribut, ditanam di dalam objek, ikut umur objeknya
```

Baris itu **menyalin** isi parameter ke dalam objeknya. Kalau tidak ditulis, `name` tetap diterima tapi hilang begitu `__init__` selesai.

Namanya boleh beda:

```python
def __init__(self, nama_dari_luar, house):
    self.name = nama_dari_luar
```

Yang di kiri titik menentukan nama atributnya, yang di kanan cuma sumber isinya. Programmer biasanya menyamakan supaya mudah dibaca.

Kesadaran baru: **atribut itu memang variabel**, cuma tempat tinggalnya di dalam objek. Jadi satu benda, tiga nama: atribut = instance variable = variabel yang ditanam di objek.

### Di dalam class vs di luar class

Polanya sama, yang berbeda cuma nama pegangannya:

```python
# DI DALAM class — pegangannya bernama self
class Student:
    def __init__(self, name, house):
        self.name = name

# DI LUAR class — pegangannya variabel saya sendiri
student = Student("Harry", "Gryffindor")
student.name = "Ron"
```

Dua-duanya berbentuk `<pegangan>.name`. Di dalam class saya **belum tahu** objeknya nanti disimpan ke variabel bernama apa, makanya Python menyediakan nama sementara yang selalu sama: `self`.

Kalau di luar class saya menulis `self.name` → NameError, karena di luar sana tidak ada yang bernama `self`.

### Tanpa `__init__` bisa tidak?

Bisa. Versi dua hari lalu jalan tanpa `__init__`. Yang berubah bukan bisa atau tidaknya, tapi **jaminannya**.

Tapi ada satu yang tidak bisa:

```python
class Student:
    ...

a = Student("Harry", "Gryffindor")
```

```
TypeError: Student() takes no arguments
```

Jadi aturannya:

```
Tanpa __init__   →  Student()                      kurungnya harus kosong
Dengan __init__  →  Student("Harry", "Gryffindor") argumen masuk lewat kurung
```

`__init__` itu yang **membuka pintu** supaya kurung di `Student(...)` bisa diisi.

Perbandingan dari sisi apa yang bisa salah:

| Tanpa `__init__` | Dengan `__init__` |
|---|---|
| Objek lahir kosong, diisi dari luar | Objek tidak bisa lahir tanpa name dan house |
| Bisa lupa mengisi salah satu | Kurang argument langsung TypeError |
| Salah ketik `student.nmae` diterima tanpa protes | Semua objek dijamin punya bentuk yang sama |
| Kesalahan ketahuan jauh belakangan | Ketahuan di detik objeknya dibuat |

Pola yang sudah berkali-kali muncul minggu ini: **lebih baik meledak sejak awal daripada diam-diam salah**.

### Kenapa `print(a)` keluar tulisan aneh

```
<__main__.Student object at 0x0000015036...>
```

Bacanya: objek jenis `Student`, dari file utama, tersimpan di alamat memori itu. Python mencetak itu karena **dia tidak tahu saya ingin objek ini ditampilkan seperti apa**.

`print("Harry")` jelas mau menampilkan apa. Tapi objek Student punya dua atribut — mau ditampilkan nama saja? dua-duanya? format apa? Python tidak bisa menebak.

Yang menyelesaikan ini namanya `__str__`, dunder berikutnya di lecture.

### `__new__` membuat, `__init__` mengisi

Tadi saya sempat mengira Python menyimpan `__new__` di objek saat objek dibuat. Lebih tepatnya, Python **memanggil** proses pembuatan itu di balik layar. Saat saya menulis `Student("Harry", "Gryffindor")`, urutannya secara sederhana:

```text
Student(...) → __new__ membuat instance kosong
             → __init__ mengisi instance itu dengan name dan house
             → hasilnya diikat ke variabel student
```

`__new__` biasanya diwarisi dari `object`, jadi saya tidak perlu menulis atau memanggilnya sendiri. Saya cukup menulis `__init__` untuk mengatur nilai awal objek. Di pelajaran pemula, `__init__` sering disebut constructor, tetapi secara teknis tugas membuat instance ada pada `__new__`; `__init__` menginisialisasinya.

### Banyak siswa: satu objek per siswa, kumpulkan dalam list

Kalau ada banyak siswa, saya tidak membuat `self.name1`, `self.name2`, dan seterusnya. Satu objek `Student` mewakili **satu siswa**, dengan satu `name` dan satu `house`. Buat banyak objek, lalu simpan objek-objek itu di dalam list:

```python
students = [
    Student("Harry", "Gryffindor"),
    Student("Hermione", "Gryffindor"),
    Student("Draco", "Slytherin"),
]

for student in students:
    print(f"{student.name} dari {student.house}")
```

List bisa menyimpan berbagai nilai, termasuk objek. `students[0]` mengambil objek pertama; lalu `.name` atau `.house` mengambil atribut dari objek itu. Kalau satu orang punya nama depan dan nama belakang, saya bisa membuat atribut `first_name` dan `last_name`. Bentuk data mengikuti hal yang sedang saya wakili: satu siswa per objek, banyak siswa dalam list.

### Kosakata

| Kata | Arti |
|---|---|
| instance | objeknya sendiri, wujud nyata dari sebuah class |
| instantiation | proses membuat objek dari class |
| instance variable | istilah lebih teknis untuk atribut |
| blueprint | denah, rancangan bangunan |
| aka (also known as) | atau disebut juga |
| lay / set the stage | menyiapkan landasan, membuka jalan |
| reckless | ceroboh, gegabah tanpa memikirkan risiko |
| the best of both worlds | dapat kelebihan dua-duanya |

Kata yang terulang dan tetap blank: **laid** (sudah ditanya 6 November sebagai *lay the foundation*).

Pasangan yang gampang tertukar: `reckless` (ceroboh), `careless` (kurang teliti), `regardless` (tanpa peduli).

### Yang mau dicoba

- Ulangi percobaan alamat `self` dan `a` dari layar kosong besok, tanpa membuka catatan ini.
- Buat dua objek dari class yang sama, isi atribut yang berbeda, lalu cek `a is b`.
- Lanjut lecture dari bagian `__str__`.


---

## Hari 4 – 9 November 2026

Lanjut Lecture 8 sekitar menit 48:40, membahas class dan object di memori, perbandingan class dengan dictionary, lalu validasi dan encapsulation. Ngoding 30 menit, bahasa Inggris 10 menit.

### Class dan object di memori

Pertanyaan siswa: bagaimana class dan object direpresentasikan di memori?

Penjelasan David: class adalah kode yang mendefinisikan cetakan atau template. Saat kita membuat object, object itu memakai ruang memori berupa sejumlah byte. Python yang mengatur letaknya di RAM; sebagai programmer, saya tidak perlu menentukan alamatnya sendiri.

Gambaran sederhananya:

```
class Student       → aturan/cetakan untuk membuat siswa
Student(...)        → Python membuat satu object di memori
student             → nama variabel yang merujuk ke object itu
```

Catatan: David menyebut class sebagai kode untuk memudahkan gambaran. Saat program berjalan, Python juga merepresentasikan class itu sendiri sebagai object. Hal penting untuk saya sekarang: Python mengurus detail memori, jadi saya bisa fokus memakai class dan object.

### Dictionary bisa, lalu kenapa pakai class?

Pertanyaan siswa: kalau data siswa bisa disimpan di dictionary, apa gunanya class?

Untuk data sederhana, keduanya memang bisa dipakai:

```python
student = {"name": "Harry", "house": "Gryffindor"}
print(student["name"])
```

```python
student = Student("Harry", "Gryffindor")
print(student.name)
```

Dictionary cukup untuk menyimpan data sederhana. Class memberi tempat untuk mengumpulkan data dan perilaku yang berkaitan, menjaga bentuk object tetap konsisten, dan menaruh aturan validasi bersama tipe data yang sedang diperiksa. Saat program makin besar, susunan ini lebih mudah dipahami dan dikembangkan.

### Encapsulation: kode yang berkaitan dikumpulkan

Pemahaman saya: dalam OOP, kode yang berhubungan dengan suatu benda dikumpulkan di class benda itu. Untuk `Student`, contohnya atribut `name` dan `house`, serta aturan yang menentukan apakah nama dan house valid.

David menyebut validasi di function terpisah seperti `get_student()` sebagai lebih *decoupled* dari `Student`—artinya, aturan validasi terpisah dari class siswa. Kalau aturan itu berada di class, class bisa menjaga agar object `Student` dibuat dengan data yang sesuai. Mengumpulkan hal yang berkaitan ini disebut *encapsulate* dalam konteks pembahasan video.

Fungsi yang bertanya langsung ke pengguna masih bisa terpisah; yang penting, aturan tentang data siswa diletakkan dekat dengan class yang mewakili siswa.

### `if not name` dan `.strip()`

Kalau pengguna menekan Enter tanpa mengetik apa pun, `input()` menghasilkan string kosong `""`. String kosong dianggap *false* di Python, jadi ini sudah cukup untuk menangkap input kosong:

```python
if not name:
    raise ValueError("Nama tidak boleh kosong")
```

Tapi string berisi spasi saja, seperti `"   "`, tidak kosong dan dianggap *true*. `.strip()` menghapus spasi di awal dan akhir **dari hasilnya**, sehingga `"   ".strip()` menjadi `""`. Maka `if not name.strip()` juga menangkap input yang cuma berisi spasi.

```python
if not name.strip():
    raise ValueError("Nama tidak boleh kosong")
```

Kalau nama yang disimpan juga ingin dibersihkan, hasil `.strip()` perlu diberikan kembali ke `name`:

```python
name = name.strip()
if not name:
    raise ValueError("Nama tidak boleh kosong")

self.name = name
```

`.strip()` tidak mengubah string asli dengan sendirinya. Tanpa menyimpan hasilnya kembali, spasi pada nilai `name` tetap ada.

### Kosakata

| Kata | Arti |
|---|---|
| decoupled | terpisah, tidak terikat erat |
| encapsulate | mengumpulkan atau membungkus hal-hal yang berkaitan di dalam satu class |
| validation | pemeriksaan apakah data memenuhi aturan |
| allocate memory | menyediakan/mengalokasikan ruang di memori |

### Yang mau dicoba

- Lanjut Lecture 8 dari sekitar menit 53:04.
- Coba bedakan input kosong `""`, input spasi `"   "`, dan input nama dengan spasi pinggir `" Harry "` menggunakan `if not name` dan `name.strip()`.


---

## Hari 5 – 10 November 2026

Pemanasan sebelum lanjut Lecture 8: kuis pilihan ganda OOP **9/10**. Yang perlu diluruskan: `Student` adalah class; `student` adalah nama variabel yang merujuk ke object. Lanjut menonton sampai sekitar **1:15**. Ngoding 2 jam, bahasa Inggris 10 menit.

### Alur class, object, dan `__init__`

Hari ini saya merapikan lagi urutan saat program berjalan:

```
1. Python membaca definisi class dan function.
   Definisi disiapkan; isi function belum dijalankan.
2. main() memanggil get_student().
3. get_student() menerima input, lalu memanggil Student(name, house, patronus).
4. Python menyediakan object, lalu menjalankan __init__ dengan object itu sebagai self.
5. __init__ memeriksa nilai. Kalau valid, self.name, self.house,
   dan self.patronus diisi.
6. Object kembali dari get_student() dan disimpan dalam variabel student di main().
```

`student` adalah variabel biasa yang merujuk ke object; ia bukan instance variable. Instance variable-nya adalah atribut seperti `self.name` dan `self.house`.

Parameter tidak otomatis ditempelkan ke object. Baris seperti `self.name = name` yang menyimpan nilai parameter sebagai atribut. Kalau validasi di `__init__` menjalankan `raise ValueError(...)`, proses berhenti sebelum atribut diisi dan pemanggilan `Student(...)` menghasilkan error.

`return None` dari `__init__` tidak membatalkan object yang dibuat dan tidak menjadikan variabel `student` bernilai `None`. Jika `__init__` berhenti lebih awal, atribut yang belum sempat dibuat memang tidak ada; mengaksesnya akan menghasilkan `AttributeError`.

### Membuat exception sendiri

Kalau ingin jenis error khusus, definisikan class yang mewarisi `Exception`:

```python
class EricError(Exception):
    pass
```

`Exception` di dalam kurung adalah **class induk**, bukan argumen biasa. Hubungan inheritance itu membuat `EricError` menjadi jenis exception yang bisa di-`raise` dan ditangkap dengan `except EricError`.

```python
raise EricError("Missing name")
```

Di sini tanda kurung setelah `EricError` membuat object error dan memberikan pesan kepadanya. Kalau class itu belum didefinisikan, Python tidak mengenali namanya. Untuk error umum, exception bawaan seperti `ValueError` biasanya sudah cukup.

### Object dicetak sebagai teks: `__str__` dan `__repr__`

Kalau menulis `print(student)` sebelum membuat aturan tampilannya, Python memberikan representasi bawaan, misalnya:

```
<__main__.Student object at 0x...>
```

Itu bukan berarti object kosong. Object-nya bisa punya atribut; tampilan bawaan hanya menunjukkan class dan penanda lokasi object di memori, bukan isi atributnya.

`__str__(self)` menentukan teks yang lebih ramah untuk pengguna ketika `print(student)` atau `str(student)` dipakai. Python otomatis memberikan object yang sedang dicetak ke parameter `self`. Dari situ method bisa mengambil atributnya:

```python
def __str__(self):
    return f"{self.name} from {self.house}"
```

`__repr__` biasanya ditujukan untuk programmer dan dapat memberi representasi yang lebih teknis. Keduanya adalah method khusus; kita bisa menentukan tampilannya di class.

### Method buatan sendiri: Patronus dan `charm()`

Setelah nama dan house, class `Student` bisa menyimpan atribut tambahan seperti `patronus`. David lalu menambahkan method `charm()` untuk menggambarkan aksi siswa saat memakai mantra.

```python
print(student.charm())
```

Saat `student.charm()` dipanggil, Python otomatis memberikan object `student` sebagai `self`. Method itu bisa membaca `self.patronus` dan memilih hasil yang cocok. Jika patronus tidak dikenal, kode dapat menyediakan hasil cadangan lewat `case _`.

Gagasan yang saya tangkap: class tidak hanya menyimpan data; class juga bisa mengumpulkan perilaku yang sesuai dengan data itu. `name`, `house`, dan `patronus` adalah data; `charm()` adalah perilaku siswa.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| enlightening | memberi wawasan atau membuat lebih paham |
| there lies the real power | di situlah letak kekuatan sebenarnya |
| conjure | memunculkan atau menghadirkan, terutama dengan sihir |
| charm | mantra/sihir tertentu; di kode David dijadikan nama method |
| tease apart | mengurai bagian-bagian agar lebih mudah dipahami |
| egotistical | terlalu mengagumi diri sendiri; dipakai bercanda saat membahas nama error sendiri |

### Yang mau dicoba

- Buat class kecil dengan `__str__`, lalu bandingkan hasil `print(object)` dan `repr(object)`.
- Definisikan exception sendiri dan coba tangkap dengan `try`/`except`.
- Lanjutkan Lecture 8 dari sekitar menit **1:15** dan lihat bagaimana method `charm()` memakai atribut Patronus.

## Hari 6 – 11 November 2026

Hari ini tidak ada kuis, langsung pemanasan lalu lanjut Lecture 8. Bagian pertama catatan ini (method `charm()`) saya susun sendiri sebelum diskusi, bagian setelahnya hasil diskusi panjang soal `@property`.

### Pemanasan: tiga koreksi istilah

Pemanasan hari ini diambil dari catatan GitHub hari Senin dan Selasa.

| Yang saya jawab | Yang benar |
|---|---|
| "Variabelnya namanya instance" | Instance itu **objeknya**, bukan variabelnya. Variabel cuma pegangan ke objek itu. |
| "Initiation" | **Instantiation** — proses membuat objek dari class. Ini kesalahan kedua kali, harus diulang terus. |
| "`__init__` yang membuat dan mencetak objek" | Python yang **membuat** objek kosong, `__init__` cuma **mengisinya**. Mencetak itu urusan `__str__`. |

Perumpamaannya seperti santri baru: panitia yang mendaftarkan dan menyediakan kamarnya (Python membuat objek), `__init__` itu acara pengisian biodata — nama, kelas, kamar. Dua pekerjaan berbeda.

### Percobaan: kalau `raise` terjadi di dalam `__init__`

Saya kira kalau `raise` jalan di `__init__`, programnya tetap lanjut dan atributnya jadi `None`. Ternyata salah. Saya coba sendiri:

```python
class Student:
    def __init__(self, name):
        raise ValueError("stop")
        self.name = name

a = Student("Harry")
print(a)
```

Hasilnya `ValueError` lalu program berhenti total. `print(a)` tidak pernah jalan.

Pelajarannya: `raise` itu **menghentikan**, bukan melewati. Dan karena `self.name = name` ada di bawah `raise`, baris itu tidak pernah dieksekusi — jadi atributnya bukan `None`, tapi **tidak pernah ada sama sekali**. Kalau dipaksa diakses hasilnya `AttributeError`, bukan `None`.

Ini bedanya:

```
None            = kotaknya ada, isinya kosong
AttributeError  = kotaknya memang tidak pernah dibuat
```

Dan variabel `a` sendiri tidak pernah terisi, karena `Student("Harry")` tidak pernah selesai mengembalikan objeknya.

### Method dan `charm()` pada class Student

Method adalah function yang didefinisikan di dalam class. Jadi `charm()` menjadi method milik class `Student`.

Method instance biasanya menerima parameter pertama bernama `self`. Python mengisi `self` secara otomatis dengan objek yang sedang memanggil method itu. Dengan `self`, method bisa membaca atribut milik objek tersebut, seperti `self.patronus`.

```python
class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "?"
```

`self.patronus` berisi atribut patronus milik objek. `match` memeriksa nilainya, lalu `return` memberikan hasil yang sesuai. `case _` menjadi pilihan umum kalau nilainya tidak cocok dengan pilihan lain.

Urutan jalannya kalau dipanggil `print(student.charm())`:

1. `Student(...)` membuat objek dan menjalankan `__init__`.
2. Nilai `"Stag"` disimpan sebagai `student.patronus`.
3. `student.charm()` memanggil method `charm()` untuk objek `student`.
4. Python otomatis mengirim objek `student` sebagai `self`.
5. Method membaca `self.patronus`, mencocokkannya di `match`, lalu mengembalikan emoji.
6. `print()` menampilkan hasil yang dikembalikan.

Jadi `charm()` **tidak berjalan otomatis** hanya karena objek dibuat. Method itu berjalan saat dipanggil. Hasilnya bergantung pada nilai atribut yang tersimpan di objek tersebut.

Kesimpulan bagian ini: class mengumpulkan data dan perilaku yang berkaitan. `name`, `house`, `patronus` adalah datanya; `charm()` adalah perilakunya. `self` adalah cara method merujuk pada objek yang sedang dipakai.

### `@property` dan `@house.setter` — bagian paling berat hari ini

Bagian ini paling lama saya pahami. Awalnya saya dijelaskan pakai perumpamaan pintu depan dan pintu belakang, tapi saya malah tambah rancu. Akhirnya metafora itu dibuang, diganti percobaan langsung pakai penanda `print`.

```python
class Student:
    def __init__(self, house):
        self.house = house

    @property
    def house(self):
        print(">> BACA jalan")
        return self._house

    @house.setter
    def house(self, value):
        print(">> TULIS jalan")
        if value not in ["Gryffindor", "Slytherin"]:
            raise ValueError("House tidak sah")
        self._house = value

s = Student("Gryffindor")
print(s.house)
s.house = "Privet Drive"
```

Outputnya:

```
>> TULIS jalan
>> BACA jalan
Gryffindor
>> TULIS jalan
ValueError: House tidak sah
```

Dari output itu baru kelihatan aturannya, dan ternyata cuma satu hal: **ada tanda sama dengan atau tidak.**

| Yang ditulis | Ada `=`? | Yang jalan |
|---|---|---|
| `s.house` | tidak | `@property` (pembaca) |
| `s.house = "..."` | ya | `@house.setter` (penulis) |
| `self.house = house` di `__init__` | ya | `@house.setter` juga |

Baris ketiga itu yang penting. `self.house = house` di dalam `__init__` sengaja lewat setter, supaya validasinya **juga berlaku saat objek baru lahir**, bukan cuma saat diubah belakangan. Itu sebabnya penanda `>> TULIS jalan` muncul duluan sebelum apa-apa.

Buktinya atribut yang benar-benar tersimpan bukan `house`:

```python
print(s.__dict__)
# {'_house': 'Gryffindor'}
```

### Dua percobaan yang saya jalankan sendiri

**Percobaan 1 — dekoratornya saja yang dihapus, functionnya tetap ada.**

Saya hapus baris `@house.setter`, tapi `def house(self, value)` dibiarkan. Hasilnya:

```
Gryffindor
```

Tidak ada penanda sama sekali. Dua-duanya mati. Sebabnya Python membaca dari atas ke bawah, jadi `def house` yang kedua **menimpa** property yang pertama, persis seperti `x = 5` lalu `x = 10`. Yang tersisa cuma function biasa yang tidak pernah dipanggil siapa pun.

Dan `print(s.__dict__)` berubah jadi `{'house': 'Gryffindor'}` — bukan `_house` lagi, karena penyimpanannya kembali jadi atribut biasa. Validasinya mati total tanpa satu pun error muncul.

Ini masuk daftar **"salah tanpa error"** yang sudah panjang di catatan saya.

**Percobaan 2 — setternya dihapus seluruhnya.**

```
File "latihan.py", line 43, in <module>
    s = Student("Gryffindor")
File "latihan.py", line 33, in __init__
    self.house = house
AttributeError: property 'house' of 'Student' object has no setter
```

Meledak di baris 33, di dalam `__init__`, sebelum sampai ke baris paling bawah.

Perbandingan dua percobaan ini bagus sekali:

| Percobaan | Hasil |
|---|---|
| Dekorator saja yang dihapus | Salah tanpa error, validasi mati diam-diam |
| Setter dihapus total | Meledak lebih awal di `__init__` |

Yang kedua justru lebih baik, karena kesalahannya ketahuan.

Pelajaran dari percobaan kedua: **read-only artinya semua penulisan ditolak, termasuk penulisan oleh `__init__` sendiri.** Python tidak peduli penulisan itu datang dari luar atau dari dalam class. Kalau memang mau read-only, `__init__` harus menyimpan langsung ke gudangnya:

```python
def __init__(self, house):
    self._house = house      # langsung, tidak lewat pintu
```

Dan ternyata ini persis mekanisme `shirt.size` di Pset 6 yang dulu bikin saya bingung kenapa tidak bisa ditimpa.

### Kenapa gudangnya harus bernama lain

Ini pertanyaan terakhir saya hari ini: kenapa tiba-tiba muncul `_house`?

Jawabannya dua lapis:

| | Aturan atau bukan |
|---|---|
| Pakai underscore `_house` | **Kesepakatan** antar programmer, bukan aturan Python. Boleh dinamai `gudang`, `rumahnya`, apa saja. |
| Nama gudang beda dari nama property | **Aturan keras.** Kalau sama, `RecursionError`. |

Yang bekerja itu **bedanya**, bukan underscore-nya.

Saya sudah pernah kena `RecursionError`-nya sendiri waktu menulis `return self.house` di dalam getter — berhenti di ulangan ke-1016 dengan pesan `maximum recursion depth exceeded`.

Alurnya kalau namanya sama:

```
s.house = "Gryffindor"  -> ada "=" -> ada setter untuk "house"? ADA  -> setter jalan
   self.house = value   -> ada "=" -> ada setter untuk "house"? ADA  -> setter jalan
      self.house = value -> ada "=" -> ada setter? ADA -> setter jalan
         ... sampai Python menyerah
```

Tidak ada yang pernah sampai ke penyimpanan. Pintu terus menunjuk ke pintu itu sendiri.

Begitu namanya dibedakan:

```
self._house = value  -> Python tanya: ada setter untuk "_house"? TIDAK ADA
                     -> ya sudah, simpan sebagai atribut biasa. Rantai berhenti.
```

Getternya pola yang sama, cuma pemicunya beda — tanpa `=`, yang ditanyakan "ada property bernama ini?".

Satu kalimat yang mau saya ingat:

> Nama gudang harus beda dari nama property, supaya saat Python bertanya "ada property atau setter untuk nama ini?", jawabannya **tidak ada** — dan rantainya berhenti di situ.

Soal underscore sendiri, itu kode isyarat sesama programmer: "ini barang dalam, jangan disentuh dari luar." Python tidak melarang `s._house = "Privet Drive"` dari luar — tembus, validasi terlewat. Tapi underscore itu seperti tulisan "KHUSUS PENGURUS" di pintu gudang pesantren: tidak dikunci, tapi yang paham tidak akan masuk.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| adversarially | dengan niat menyerang atau mencari celah; dipakai saat membahas orang yang sengaja mengakali validasi |
| circumvent | mengakali, memutar lewat jalan lain supaya tidak kena aturan |
| in place | di tempatnya, sudah terpasang dan berlaku |
| term of art | istilah khusus di suatu bidang yang artinya beda dari arti sehari-hari |
| into the weeds | masuk terlalu dalam ke detail kecil |

### Yang mau dicoba

- Ganti semua `_house` jadi `gudang` di getter dan setter, lalu jalankan — harusnya tetap normal.
- Ubah `__init__` jadi `self._house = house` dengan setter sudah dihapus, lalu tebak baris mana yang meledak saat `s.house = "Privet Drive"`.
- Lanjutkan Lecture 8 dari bagian setelah `@property`.

## Hari 7 – 12 November 2026

### Kuis Harian #13 (15 soal, Week 6 + Week 3) — 13/15

Yang salah nomor 8 dan 13.

**Nomor 8, `in place`.** Ini materi `shuffle`/`None` yang keempat kalinya meleset, jadi dikunci pakai percobaan dengan function baru:

```python
cards = ["A", "B", "C"]
hasil = cards.sort()
print(cards)
print(hasil)
```

Tebakan saya: `cards` jadi `None`. Ternyata **tertukar**. Yang benar:

```
['A', 'B', 'C']     <- cards, listnya terurut di tempat
None                <- hasil, karena sort() tidak menyerahkan apa-apa
```

Dua hal berbeda terjadi di satu baris `hasil = cards.sort()`:

```
cards.sort()   -> mengerjakan: list aslinya diurutkan   <- BERHASIL
hasil = ...    -> menampung: tidak ada yang diserahkan  <- dapat None
```

Pekerjaannya tetap jalan. Yang kosong itu tangkapannya.

Dan saya sempat bilang lagi "tidak memerlukan variabel" — itu bentuk lama yang sudah dikoreksi 7 November. Menyimpan ke variabel **boleh**, tidak ada yang melarang; isinya saja yang `None`. Beda dengan "tidak boleh disimpan".

**Nomor 13, `csv.reader` vs `csv.DictReader`.**

```
csv.reader      -> kasih LIST  -> row[0], row[1]
csv.DictReader  -> kasih DICT  -> row["name"], row["house"]
```

DictReader memakai baris header sebagai nama kunci. Bedanya bukan soal ukuran file, dua-duanya dibaca baris per baris lewat `for`. Dan `row[0]` tertukar dengan `row[1]` **tidak error sama sekali**, cuma hasilnya salah — alasan yang sama kenapa dictionary menang dari tuple di Week 8.

### Pemanasan: lima soal, lima benar

Semua benar, satu kurang lengkap. Di soal "apa yang dijalankan `self.house = house` di dalam `__init__`", mekanismenya sudah benar (Python bertanya dulu ada setter atau tidak), tapi saya belum menyebut **kenapa itu penting**: karena lewat setter, validasinya berlaku sejak objek lahir.

```python
s = Student("Privet Drive")    # langsung ValueError, objeknya tidak pernah jadi
```

Satu kalimat: **objek tidak bisa lahir cacat.** Itu seluruh gunanya `@property`.

Koreksi istilah lagi: instantiation itu **barisnya** (`Student("Harry")`), bukan nama classnya.

### Percobaan besar: apa yang ditulis `__init__` menentukan segalanya

Saya otak-atik nama atribut di dalam `__init__` dan hasilnya membingungkan sampai ketahuan sebabnya. Empat percobaan:

```
init menulis     getter membaca    hasil
---------------------------------------------------------------
self.house       self._house       JALAN. Setter dipanggil, dia yang bikin _house
self._house      self._house       JALAN, tapi setter DILEWATI saat lahir
self.gedung      self._gedung      ERROR
self._gedung     self._gedung      JALAN, tapi setter DILEWATI saat lahir
```

Awalnya saya kira baris kedua "masih jalan jadi sama saja". Ternyata tidak. Bukti ada di penandanya:

```
self._house di init:        self.house di init:
>> BACA jalan               >> SET jalan      <- ini yang hilang
Gryffindor                  >> BACA jalan
>> SET jalan                Gryffindor
                            >> SET jalan
```

`>> SET jalan` yang pertama **tidak muncul**. Jadi "masih jalan" itu betul, tapi setternya tidak dipanggil saat lahir. Validasinya dilewati, cuma kebetulan tidak meledak.

Akar kebingungan saya: menggabungkan **dua aturan yang terpisah**. Ternyata ada dua, dan keduanya tidak berhubungan:

```
Aturan 1 - kapan setter dipanggil?
   Python cuma lihat: nama sesudah self. itu nama property atau bukan.
   self.house  -> "house" nama property     -> setter dipanggil
   self._house -> "_house" bukan property   -> simpan langsung
   self.gedung -> "gedung" bukan property   -> simpan langsung

Aturan 2 - nama gudang harus beda dari nama property.
   Tujuannya cuma satu: mencegah recursion. Tidak ada hubungannya dengan __init__.
```

Jadi `_house` dan `house` itu **dua nama yang sama sekali berbeda** bagi Python, sama asingnya seperti `gedung`. Tidak ada istilah "mirip" atau "sinkron" di sini.

Kenapa baris ketiga error? Pesannya jelas:

```
AttributeError: 'Student' object has no attribute '_gedung'. Did you mean: 'gedung'?
```

`self.gedung = house` menyimpan atribut bernama `gedung`. Getternya mencari `_gedung`. Beda satu underscore, barangnya memang tidak ada. Python bahkan sudah menebakkan.

Jadi `__init__` punya dua pilihan dan harus dipilih dengan sadar:

```
self.house  = house    -> lewat pintu, validasi berlaku sejak lahir   <- yang benar
self._house = house    -> masuk gudang langsung, validasi dilewati
```

### Kecacatan memang lolos kalau lewat gudang

Pertanyaan saya: kalau `__init__` langsung ke gudang, apakah kecacatannya lolos? Dicoba:

```python
def __init__(self, house):
    self._house = house        # langsung ke gudang

s = Student("Privet Drive")
print(s.house)
```

Tidak meledak. `Privet Drive` jelas tidak sah menurut setternya, tapi objeknya tetap lahir membawa nilai itu.

Lalu saya tambahkan `s.house = "Privet Drive"` dan sempat salah lapor bahwa tidak error — ternyata saya kurang teliti, baris yang saya ubah bukan yang saya kira. Setelah dicek ulang:

```
s.house  = "Privet Drive"   -> "house" nama property   -> setter jalan -> ValueError
s._house = "Privet Drive"   -> "_house" bukan property -> langsung timpa gudang, lolos
```

Dan `s._house` itu persis kosakata **circumvent** dari kuis tadi pagi: mengakali lewat jalan samping. Python tidak mengunci `_house`, jadi siapa pun yang tahu nama gudangnya bisa menembus validasi. Underscore itu tanda "jangan disentuh", bukan gembok.

```
melindungi dari kecerobohan  -> ya
melindungi dari niat jahat   -> tidak
```

### Decorator itu apa

Decorator adalah **baris `@...` yang ditempel di atas sebuah function, dan mengubah perilaku function itu tanpa menyentuh isinya**.

```python
def house(self):            # function biasa
    return self._house
# dipanggil: s.house()      <- pakai kurung

@property                   # ditempeli decorator
def house(self):
    return self._house
# dipanggil: s.house        <- tanpa kurung, jalan sendiri saat dibaca
```

Isi functionnya sama persis. Yang berubah cuma cara Python memperlakukannya. Seperti stempel di berkas setoran: isi berkasnya tidak diubah satu huruf pun, tapi begitu distempel "SUDAH DISAHKAN", cara orang memperlakukannya berubah.

Dan tanda `@` di sini tidak ada hubungannya dengan `@` di email atau di regex.

### Yang sebenarnya dilakukan `@property`

Dua baris ini:

```python
@property
def house(self):
    return self._house
```

sebenarnya cara singkat dari:

```python
def house(self):
    return self._house

house = property(house)      # house sekarang jadi OBJEK property
```

Jadi `@property` **membuat sebuah benda** bernama `house`. Baru setelah itu `@house.setter` bisa menempel padanya, karena `.setter` itu method milik benda tersebut — sama seperti `"azka".lower()`, harus ada bendanya dulu baru methodnya bisa dipakai.

Saya coba hapus function di bawah `@property`, lalu langsung `@house.setter`:

```
NameError: name 'house' is not defined
```

Benar, karena tanpa functionnya, baris `house = property(house)` tidak pernah terjadi, jadi tidak ada benda bernama `house` untuk ditempeli.

Urutannya mengikat:

```
1. def house + @property   -> objek property lahir
2. @house.setter           -> baru bisa menempel padanya
```

Ini juga menjawab pertanyaan mahasiswa di lecture: kenapa perlu getter kalau sudah ada setter? Karena setter cuma hidup saat **menulis**. Waktu `print(student)` membaca `{self.house}`, itu membaca — getter yang dipanggil. Tanpa getter, tidak ada yang bisa mengambil nilai dari `_house`, dan dari luar orang cuma tahu nama `house`.

### `property` itu class, bukan function

David bilang *"Property is a function in Python"*, tapi sebenarnya `property` itu **class**. Cara pakainya mirip function karena ada kurungnya, tapi `Student("Harry")` juga ada kurungnya dan itu instantiation, bukan pemanggilan function.

```python
print(type(Student.house))
# <class 'property'>
```

Polanya sama dengan yang sudah saya kenal sejak 6 November:

```
str      class  ->  "azka"   objek  ->  .lower()  method
property class  ->  house    objek  ->  .setter   method
```

### `Student.house` vs `s.house` — siapa yang bertanya

Ini bagian yang paling lama saya cerna hari ini. Percobaannya:

```python
print(Student.house)
s = Student("Gryffindor")
print(s.house)
```

```
<property object at 0x000001D6825B6390>
>> BACA jalan
Gryffindor
```

`>> BACA jalan` muncul **sekali saja**. Jadi `print(Student.house)` tidak menjalankan getter sama sekali.

Kuncinya: **getter butuh `self`.** `self` itu objeknya. Tidak ada objek berarti tidak ada `self`, jadi getternya tidak mungkin dijalankan — mau membaca `_house` milik siapa?

```
Student.house   -> yang bertanya CLASS. Tidak ada objek, tidak ada self.
                   Python cuma menyerahkan benda property-nya. Tidak ada yang jalan.

s.house         -> yang bertanya OBJEK s. self = s.
                   Mesinnya dijalankan, keluar isi s._house.
```

Yang bertanya selalu **di sebelah kiri titik**:

```
s.house
│ └─ nama lacinya
└─── objeknya
```

Dua kesalahan saya waktu merangkum, dicatat supaya tidak terulang:

```
salah: "objeknya itu house"          benar: objeknya itu s, house cuma nama laci
salah: "house milik property"        benar: lacinya milik class Student, ISINYA benda property
salah: "Student.house hasil cetakan property"   benar: Student.house ADALAH benda property itu
```

Dan kata "masuk ke" yang saya pakai juga keliru — Python tidak masuk ke mana-mana. Benda property itu sudah dibuat sejak `class Student:` dibaca, sebelum ada satu pun siswa. `Student.house` cuma menyerahkan isi lacinya.

Satu kalimat untuk diingat: **bertanya ke class = diberi mesinnya, bertanya ke objek = mesinnya dijalankan.**

### Bug yang saya temukan duluan sebelum David

Di menit 1:27 David menulis `self.house = house` di dalam setter, lalu bilang *"they're going to collide"*. Saya sempat salah tangkap, saya kira yang bertabrakan itu `name` lawan `house`. Ternyata bukan: yang bertabrakan **`house` lawan `house`** — nama function (property) dan nama tempat penyimpanan.

Solusinya di menit 1:28:06, persis yang sudah saya tabrak sendiri kemarin:

> use an almost identical name, with a little indicator

"Almost identical name with a little indicator" itu `_house`. Jadi `RecursionError` ulangan ke-1016 yang saya kena kemarin, hari ini baru dijelaskan David.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| fancy / fancier | mewah, lebih canggih dari yang biasa; property disebut "a fancier attribute" |
| graduate from X | naik tingkat dari X, bukan sekadar "lulus" |
| at your disposal | tersedia siap pakai di tanganmu (idiom; `disposal` sendirian artinya pembuangan) |
| maliciously | dengan niat jahat |
| collide | bertabrakan, dua hal berebut tempat yang sama |
| at will | sesuka hati, kapan pun mau |
| adversarially | (ulangan) dengan niat mencari celah — benar di kuis pagi, lupa lagi sore harinya |

### Yang mau dicoba

- Jadikan pemanasan besok: `Student.house` vs `s.house`, kenapa getter tidak jalan lewat class, apa yang dibuat `@property`, dan kenapa `property` itu class bukan function.
- Lanjutkan Lecture 8 dari menit 1:31.

## Hari 8 – 13 November 2026

### Kuis Harian #14 (15 soal, Week 0 + Week 4) — 14/15

Semua kosakata benar, termasuk `in place` dan `adversarially` yang kemarin lepas. Yang salah cuma nomor 10, dan itu kedua kalinya (pernah salah di kuis #11).

Soalnya: file diawali `import random`, lalu di bawahnya ditulis `angka = choice([1, 2, 3])`.

Patokan yang harus saya kunci: **nama yang tepat sesudah `import` itulah satu-satunya yang masuk ke absen filemu.**

```
import random              -> absenmu berisi: random
from random import choice  -> absenmu berisi: choice
```

Jadi `import random` tidak membawa serta isinya ke absen. `choice` tetap ada di dalam `random.py`, cuma namanya tidak terdaftar di file saya, makanya harus lewat pemiliknya: `random.choice(...)`.

Seperti daftar absen kelas: yang didaftarkan nama "Kelompok A", bukan nama tiap santri di dalamnya. Mau memanggil satu santri, sebut dulu kelompoknya.

### Pemanasan: dua dari lima masih kosong

Nomor 1 dan 2 inti jawabannya benar. Tapi di nomor 2 saya menambahkan penjelasan soal `__init__` yang sebenarnya tidak nyambung — alasan getter tidak jalan lewat class itu cuma satu: tidak ada objek, maka tidak ada `self`.

Nomor 3 belum ketemu. Jawabannya satu baris:

```python
house = property(house)
```

Nomor 4 terlewat. Jawabannya `NameError: name 'house' is not defined`.

Nomor 5 jawabannya benar (`property` itu class), tapi buktinya saya karang sendiri — bilang "karena punya method". Bukti yang benar itu yang saya jalankan kemarin: `print(type(Student.house))` keluar `<class 'property'>`.

Untuk nomor 3 dibuktikan dengan menulis ulang tanpa satu pun tanda `@`:

```python
class Student:
    def __init__(self, house):
        self._house = house

    def house(self):
        print(">> BACA jalan")
        return self._house

    house = property(house)
```

Tebakan saya jalan, dan memang jalan. `>> BACA jalan` tetap muncul. Jadi `@property` benar-benar cuma cara menulis yang lebih singkat — tidak ada sihir di tanda `@`-nya.

### Lecture 8 dari menit 1:31

**Lubang di `__init__` yang saya temukan duluan.** David menulis `self._house = house` di `__init__` lalu berkata sendiri: *"there's no error checking in init whatsoever."* Itu persis kesimpulan yang saya tulis kemarin — validasinya dilewati, objek bisa lahir cacat.

**Jalan tembus `_house`.** Lalu David menulis `student._house = "Number Four, Privet Drive"` dan berkata *"we slip through"*. Juga persis yang saya buktikan kemarin. Alasannya:

```
Python tidak punya private yang sungguhan.
Di bahasa lain seperti Java, private itu dikunci compiler.
Di Python: you're on the honor system.
```

`_house` itu rambu, bukan gembok. Sama seperti tulisan "KHUSUS PENGURUS" di pintu gudang pesantren — tidak dikunci, tapi yang paham tidak masuk.

### Semua tipe data ternyata class

Bagian ini yang paling membuka hari ini. Dokumentasi resmi Python menulis:

```
class int(x, base=10)
class str(object='')
list.append(x)
```

Kata pertamanya **`class`**, bukan `function`. Jadi `int("50")` itu instantiation, bentuknya sama persis dengan `Student("Harry")`.

Artinya sejak Week 0, setiap kali saya menulis `int(input(...))`, saya sudah membuat objek dari sebuah class. Sudah berminggu-minggu memakai OOP tanpa tahu namanya.

Dan ada bentuk singkat yang selama ini saya kira "bukan apa-apa":

```
nama = []     sama dengan    nama = list()
teks = ""     sama dengan    teks = str()
d    = {}     sama dengan    d    = dict()
angka = 0     sama dengan    angka = int()
```

Yang kanan itu instantiation yang terang-terangan. Yang kiri cuma jalan pintas karena terlalu sering dipakai.

Pemetaannya satu lawan satu dengan class buatan sendiri:

```
                  class buatan Python        class buatan saya
cetakan           dict                       Student
instantiation     dict() atau {}             Student("Harry")
objek             {"a": 1}                   s
method            .keys()  .get()            .charm()
self              dictnya sendiri            s
```

Satu-satunya yang beda: siapa yang menulis classnya.

**Method milik satu class tidak bisa dipakai class lain.** `append` punya `list`, `lower` punya `str`. Dan isi sebuah class bukan rahasia — bisa dibuka pakai `dir(str)` dan `help(str.strip)`, alat yang sudah saya pakai waktu mengerjakan Figlet tanggal 13 Oktober.

**`self` berlaku untuk semua, bukan cuma class buatan sendiri.** Waktu menulis `nama.append("Ron")`, Python mengirim `nama` sebagai `self` dan `"Ron"` sebagai `x`. Aturannya satu: **apa pun yang ada di sebelah kiri titik, itulah yang dikirim sebagai `self`.** Jadi setiap `.method()` yang pernah saya tulis sejak Week 0 — `.strip()`, `.split()`, `.append()`, `.lower()` — semuanya mengirim objeknya sebagai `self` di balik layar.

### `base` — ditandai, bukan materi inti

Saya sempat mengira `base=10` itu "angka 1 sampai 10". Ternyata `base` itu basis bilangan: sistem hitung apa yang dipakai teksnya.

```python
print(int("1010"))          # 1010
print(int("1010", base=2))  # 10
print(int("ff", base=16))   # 255
```

Teksnya sama, yang berubah cara membacanya. Hitungannya belum saya pahami betul, dan setelah dibahas disepakati ini **bukan materi CS50P** — tidak ada satu pun problem set yang memakainya. Dijadwalkan jadi sesi tersendiri nanti, karena biner dan heksadesimal memang akan ketemu lagi di warna `#FF0000`, satuan byte, dan UTF-8.

### Class method — baru mulai, belum paham betul

Selama ini semua yang saya pakai itu **instance method**: butuh objek, parameter pertamanya `self`.

```
instance method  ->  butuh OBJEK, ada self
class method     ->  tidak butuh objek, cukup classnya
```

Patokannya satu pertanyaan: **apakah jawabannya berubah tergantung objek yang mana?**

```
berubah tiap objek   ->  instance method
sama untuk semua     ->  class method
```

`charm()` berubah — Harry patronusnya rusa, Ron anjing. Tapi "house apa saja yang ada" jawabannya sama untuk semua siswa.

Percobaan yang saya jalankan:

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def charm(self):
        return f"{self.name} dari {self.house}"

    def daftar_house():
        return ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


s = Student("Harry", "Gryffindor")

print(s.charm())                  # baris A
print(Student.daftar_house())     # baris B
print(s.daftar_house())           # baris C
```

Hasilnya:

```
Harry dari Gryffindor
['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
TypeError: Student.daftar_house() takes 0 positional arguments but 1 was given
```

Angka di pesan errornya yang menjelaskan semuanya:

```
0 = tempat yang disediakan daftar_house()
1 = yang dikirim Python, yaitu s
```

Python tetap mengirim objeknya walaupun tidak ada tempat untuk menerimanya. Koreksi untuk saya: masalahnya **bukan** objeknya kosong — `s` isinya lengkap. Masalahnya tidak ada kursi untuk menampungnya.

Saya sempat bertanya apakah bisa ditaruh di luar class saja. Jawabannya **bisa**, jalan tanpa masalah. Jadi class tidak wajib secara teknis. Alasan menaruhnya di dalam class itu **kerapian**:

```
daftar_house()           <- milik siapa? harus dibaca isinya dulu
Student.daftar_house()   <- jelas, ini urusan Student
```

Ini alasan yang sama dengan `student[0]` lawan `student["name"]` tanggal 6 November: dua-duanya jalan, yang satu memberi tahu maksudnya. Istilahnya semantics.

Kegunaan class method yang paling sering: **membuat objeknya sendiri**. Function yang bertanya nama ke pengguna lalu menghasilkan Student baru itu dipanggil sebelum ada siswa sama sekali, jadi tidak mungkin jadi instance method.

Bagian ini berhenti di sini dan saya minta diulang besok, karena sudah mulai lemas dan belum paham betul.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| burst someone's bubble | merusak ilusi orang, menyampaikan kenyataan yang mengecewakan |
| slip through | lolos, menyelinap lewat celah |
| under the hood | di balik kap mesin, bagian dalam yang tidak terlihat |
| honor system | sistem kejujuran, tidak ada pengawas |
| visibility | siapa yang boleh melihat atau mengakses |
| private / public / protected | tingkatan akses: tertutup, terbuka, setengah |
| signify | menandakan, memberi isyarat |
| dig into | menggali, menelusuri sampai dalam (lawan dari dabble) |
| expressiveness | daya ungkap, seberapa luas gagasan bisa dinyatakan |
| sensible | masuk akal, bijak — BUKAN sensitif, ini jebakan |
| incarnation | wujud nyata, penjelmaan |
| a.k.a. | also known as, alias |
| baked into | sudah tertanam menyatu dari sananya (ketemu lagi, pertama 16 Oktober) |
| convention | kesepakatan bersama, bukan aturan paksa (ketemu lagi, pertama 21 Oktober) |
| from the get-go | sejak awal mula (ketemu lagi, pertama 11 Oktober) |

### Yang mau dicoba

- Jadikan pemanasan besok: class method lawan instance method, kenapa `s.daftar_house()` meledak, dan apa guna `@classmethod`.
- Ulang juga: `house = property(house)` dan bukti `type(Student.house)`.
- Lanjutkan Lecture 8 dari menit 1:48, bagian `@classmethod`.

## Hari 9 – 14 November 2026

### Kuis Harian #15 (15 soal, Week 1 + Week 5) — 15/15

Sempurna, pertama kalinya sejak kuis #8 tanggal 31 Oktober. Semua kosakata kemarin benar, termasuk `sensible` yang jebakannya mirip `sensitive`.

Dan `import random` akhirnya nempel di percobaan ketiga. Bentuk soalnya dibalik: dari hasil yang diinginkan ke cara menulisnya.

```
mau menulis choice([1,2,3]) telanjang  ->  from random import choice
mau menulis random.choice([1,2,3])     ->  import random
```

Patokannya tetap: nama yang tepat sesudah `import` itulah yang masuk ke absen filemu.

### Pemanasan: class method, dengan tes yang bisa dicek

Kemarin saya minta materi ini diulang karena belum paham betul. Kali ini dipakai tes mekanis, bukan dikira-kira:

> Buka functionnya. Ada kata `self` di dalamnya atau tidak?

```
self dipakai di dalamnya      ->  instance method (butuh objek)
self tidak muncul sekali pun  ->  class method    (tidak butuh objek)
```

Alasannya: isi `self` itu objeknya. Kalau function butuh `self`, berarti dia butuh tahu "siswa yang mana", karena jawabannya diambil dari data siswa itu. `charm()` membaca `self.patronus` — patronus milik siapa? Harus ada siswanya dulu. `daftar_house()` tidak membaca apa pun dari siswa, jawabannya sama untuk semua.

Cara saya sendiri merumuskannya, dan ini yang paling nempel buat saya:

```
butuh "ini milik siapa?"     ->  instance method
tidak ada "milik siapa"-nya  ->  class method
```

Patronus, rumah, nama — menempel pada seseorang. Jadwal setoran, daftar house, jumlah asrama — tidak menempel pada siapa pun.

Analogi pesantren: "siapa namamu?" harus ditanyakan ke satu santri, jawabannya beda-beda. "Jam berapa setoran mulai?" ditanyakan ke pesantrennya, siapa pun yang ditanya jawabannya sama. Pertanyaan kedua kalau dipaksa ke satu santri bukannya salah, cuma **aneh** — seolah jadwal setoran itu milik pribadi dia. Itu yang David sebut *not sensible*.

### Latihan class method

Tiga soal, dua benar penuh dan satu benar tempatnya.

**Soal 1 — menandai jenis method.** Benar semua: `__init__`, `deposit`, `__str__` instance method; `kapasitas_maksimal` class method.

**Soal 2 — menebak di mana meledak.** Benar tempatnya (baris `print(jar.kapasitas_maksimal())`) dan benar sebabnya: tidak ada penampung. Pesan errornya:

```
TypeError: Jar.kapasitas_maksimal() takes 0 positional arguments but 1 was given
```

Satu kalimat saya perlu dirapikan. Saya sempat bilang *"objek jar menyimpan sebuah argumen yang akan dikirim ke objek"* — itu tidak nyambung. Yang dikirim bukan ISI `jar`, tapi **`jar` itu sendiri**. Aturannya tetap: apa pun di sebelah kiri titik, itulah yang dikirim sebagai parameter pertama.

**Soal 3 — melengkapi class method.** Benar dua-duanya: `@classmethod` dan `cls`.

Lalu saya bertanya apakah `cls` boleh tidak ditulis. **Tidak boleh.** Begitu ada `@classmethod`, Python SELALU mengirim classnya sebagai parameter pertama, jadi tempatnya wajib ada. Kalau dikosongkan, errornya sama persis dengan soal 2.

```
tempat parameter pertama  ->  WAJIB ada
namanya cls               ->  kesepakatan, boleh diganti
```

Persis seperti `self` yang saya buktikan tanggal 8 November waktu menggantinya jadi `aku`.

### `cls` dan `self` — bedanya apa

```
self  ->  isinya OBJEKNYA   ->  dipakai instance method
cls   ->  isinya CLASSNYA   ->  dipakai class method
```

Jadi di dalam class method, menulis `cls(12)` itu sama saja dengan menulis `Jar(12)`.

Kenapa pakai `cls` kalau dua-duanya jalan? Keuntungannya baru terasa kalau ada class lain yang mewarisi, dan itu materi yang belum dibahas — namanya **inheritance**. Ditandai untuk nanti.

### Kegunaan class method yang paling sering: pabrik objek

Ini bagian yang kemarin saya minta dijelaskan ulang dengan kode lengkap.

Masalahnya: function `get_student()` tugasnya MEMBUAT seorang Student baru. Kalau dipaksa jadi instance method, jadinya konyol:

```python
s = Student("Harry", "Gryffindor")   # bikin siswa dulu...
student = s.get_student()            # ...supaya bisa bikin siswa?
```

Telur dan ayam. Untuk memanggil instance method butuh objek, padahal objek itulah yang sedang mau dibuat.

Makanya harus bisa dipanggil tanpa objek sama sekali:

```python
student = Student.get()
```

Analogi pesantrennya: mendaftarkan santri baru itu lapor ke **kantor pendaftaran**, bukan minta tolong ke santri lain yang sudah masuk duluan. Dan kalau belum ada satu santri pun, pendaftaran tetap harus bisa jalan.

Dua versi lengkap yang saya jalankan, hasilnya identik:

```python
# VERSI A - function menggantung di luar class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} dari {self.house}"


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


def main():
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()
```

```python
# VERSI B - dipindah ke dalam class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} dari {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
```

Kenapa versi B lebih baik padahal hasilnya sama? Satu alasan saja: **kejelasan.**

```
get_student()    <- milik siapa? harus dibaca isinya dulu
Student.get()    <- jelas sejak dibaca, ini pabriknya Student
```

Alasan yang sama dengan `student[0]` lawan `student["name"]` tanggal 6 November: dua-duanya jalan, yang satu memberi tahu maksudnya. Istilahnya semantics.

### Lecture 8 dari menit 1:48 — Sorting Hat

**Analogi rumah.** David bilang instance itu *a very specific incarnation* dari classnya, lalu memakai analogi kompleks perumahan: semua rumah dari denah yang sama, tapi tiap rumah agak beda karena catnya beda.

```
denah yang sama     ->  class Student
rumah yang berdiri  ->  objek s, objek b
catnya beda         ->  nilai atributnya beda
```

**Contoh baru: Sorting Hat.** Di cerita Harry Potter ada topi runcing yang dipakaikan ke murid baru, lalu topi itu menyebutkan murid tersebut masuk asrama mana.

Kodenya nanti dipakai begini:

```python
Hat.sort("Harry")      # keluar: Harry is in Gryffindor
```

Sebelah kiri titiknya **`Hat`**, classnya, bukan objek. Dan itu pas untuk class method karena di seluruh Hogwarts topinya **cuma ada satu** — tidak masuk akal membuat banyak objek topi lalu bertanya "topi yang mana?". Padanan pesantrennya: panitia penempatan kamar itu satu, bukan tiap santri punya panitia sendiri.

**Jebakan kata `sort`.** Saya kira ini function bawaan Python. Ternyata bukan — itu nama karangan David, sama seperti `charm()`. Yang bikin bingung, kata `sort` dalam bahasa Inggris punya dua arti:

```
sort = mengurutkan            ->  ini yang dipakai cards.sort()
sort = memilah, menggolongkan ->  ini yang dipakai Sorting Hat
```

Dua hari lalu saya menjalankan `cards.sort()` yang mengurutkan A, B, C — itu arti pertama, dan memang method bawaan milik class `list`. Yang di `hat.py` ini arti kedua: memilah murid ke golongannya. Padanannya di pesantren: **penjurusan** atau pembagian halaqah.

**Dichotomy.** David menunjukkan selisih antara cara menulis dan cara memanggil:

```
def sort(self, name):     <- waktu dibuat: DUA parameter
hat.sort("Harry")         <- waktu dipanggil: SATU argumen
```

Rumusnya:

```
jumlah parameter saat didefinisikan = jumlah argumen yang diketik + 1
```

`+1` itu `self`, selalu dikirim otomatis dan selalu di urutan pertama. Dan ini sudah saya lihat sebelumnya: `nama.append("Ron")` satu argumen diketik, padahal di dalam class `list` parameternya dua. Soal nomor 2 di latihan tadi pagi juga persis ini.

### Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| incarnation | wujud nyata, penjelmaan dari sesuatu yang abstrak |
| thereof | dari hal tersebut |
| paint and such | cat dan sebagainya |
| pointy | runcing |
| sorting hat | topi penyortir yang membagi murid ke asrama |
| so to speak | begitulah istilahnya, boleh dibilang begitu |
| unfamiliar | belum kenal, belum akrab |
| dichotomy | pembagian dua, dua sisi yang berbeda dan berpasangan |
| encapsulate | membungkus, menyembunyikan di dalam |
| tuck away | menyelipkan ke dalam supaya tidak berserakan |
| requisite | yang diperlukan, yang disyaratkan |

### Yang mau dicoba

- Jadikan pemanasan besok: `cls` lawan `self`, kenapa tempat parameter pertama wajib ada, dan kenapa pabrik objek harus class method.
- Simpan pertanyaan kenapa `cls(12)` lebih baik dari `Jar(12)` sampai bagian inheritance.
- Lanjutkan Lecture 8 dari menit 1:52.
