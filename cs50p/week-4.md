# CS50P Week 4: Libraries

## Hari 1 – 9 Oktober 2026

Menonton lecture sekitar 10 menit awal (bagian random: choice dan randint). Lebih banyak waktu dipakai untuk bertanya sampai benar-benar paham.

### Library itu apa?
- Awalnya saya bingung, library kan artinya perpustakaan. Ternyata memang mirip: library itu kumpulan kode yang sudah ditulis orang lain, tinggal kita pakai, tidak perlu menulis dari nol.
- Ibaratnya perpustakaan berisi kitab-kitab. Kita tidak perlu mengarang kitab sendiri, cukup ambil kitab yang dibutuhkan.

### Module
- Module itu satu file `.py` yang isinya kumpulan function.
- Contohnya `random`, asalnya dari file `random.py`. Di dalamnya ada function seperti `choice` dan `randint`.
- File ini sudah ikut terpasang bersama Python, jadi tinggal di-`import`. Waktu import cukup tulis namanya, tanpa `.py`.
- Analogi saya: module = kitab, function di dalamnya = bab.
- Ternyata file yang saya buat sendiri seperti `plates.py` atau `fuel.py` juga termasuk module, karena sama-sama file `.py`. Ini nanti dibahas David di akhir lecture, termasuk hubungannya dengan `__name__`.

### `import random` vs `from random import choice`
```python
import random
random.choice(["heads", "tails"])
```
```python
from random import choice
choice(["heads", "tails"])
```
- `import random` itu cuma mengambil satu kitab, ditaruh di meja. Function-nya tetap ada di dalam kitab. Jadi kalau mau pakai bab choice, kitabnya harus dibuka dulu: `random.choice`.
- Urutannya: nama module dulu, titik, baru nama function. Kitab, titik, bab. Bukan `choice.random`.
- Titik di tengah artinya "milik" atau "di dalam", sama seperti `c.lower()`.
- `from random import choice` itu nama `choice` ditempel langsung di daftar nama filemu. Jadi bisa langsung panggil `choice` tanpa menyebut kitabnya.
- Kalau cuma `import random`, lalu saya panggil `choice(...)` saja, hasilnya NameError, karena filemu belum kenal nama `choice`.

| Ditulis | Yang dikenal filemu | Cara panggil |
|---|---|---|
| `import random` | `random` saja | `random.choice(...)` |
| `from random import choice` | `choice` saja | `choice(...)` |
| `from random import choice, randint` | `choice` dan `randint` | `choice(...)`, `randint(...)` |

- Intinya, kata yang tepat sesudah `import`, itulah nama yang dikenal filemu.

### Trade-off dua cara import
- Cara kedua lebih ringkas, tapi rawan tabrakan nama. Kalau saya juga punya variabel bernama `choice`, function-nya tertimpa:
```python
from random import choice
choice = "apel"
choice(["heads", "tails"])   # TypeError: 'str' object is not callable
```
- Ini sama persis dengan percobaan `print = 5` saya waktu Pset 3. Setelah ditimpa, `print("halo")` jadi error not callable.
- Cara pertama lebih panjang, tapi jelas asal function-nya dari mana, dan aman kalau saya punya variabel bernama `choice`, karena function-nya tetap utuh di `random.choice`.

### Namespace dan scope
- Namespace itu daftar nama yang dikenal di filemu. Ibaratnya lembar absen halaqah: yang namanya ada di absen bisa langsung dipanggil, yang tidak ada ya tidak bisa.
- Yang masuk absen: variabel yang saya buat (`x = 5`), function yang saya buat dengan `def` (misalnya `main`), built-in milik Python (`print`, `input`), dan nama yang di-import.
- Saya sempat mengira `choice` itu namespace. Ternyata bukan. Namespace itu lembar absennya, sedangkan `choice` cuma salah satu nama santri yang tercatat di absen itu.
- Scope untuk sekarang anggap mirip. Bedanya, scope lebih menekankan di wilayah mana sebuah nama dikenal. Contohnya variabel di dalam `main()` tidak dikenal di function lain, seperti absen kelas 7 yang hanya berlaku di kelas 7.

### Kalau tidak tahu isi module-nya?
- Pertanyaan saya: kalau awam sama sekali, tahu nama module-nya `random` tapi tidak tahu isi function-nya apa saja, bagaimana mau praktek?
- Jawabannya: baca dokumentasinya. Dokumentasi resmi module random ada di docs.python.org, di situ ada semua function, gunanya, dan contohnya.
- Bisa juga lewat interactive mode: `import random`, lalu `help(random.choice)`. Tekan `q` untuk keluar.
- Programmer tidak menghafal isi semua module. Cukup tahu module-nya ada, lalu buka dokumentasi saat butuh. Sama seperti tidak harus hafal isi semua kitab, cukup tahu kitab mana yang harus dibuka.

### Sequence
- Sequence itu kumpulan yang isinya berurutan, contohnya list `["heads", "tails"]` atau string `"abc"`.

### `random.choice`
- Tugasnya cuma satu: mengambil SATU isi secara acak dari sequence yang diberikan.
- Analogi: kocokan undian. Nama ditulis di kertas, digulung, dimasukkan ke toples. Toplesnya = sequence, `choice` = tangan yang mengambil satu gulungan tanpa melihat, hasilnya = satu nama yang terambil.
- Gulungannya dikembalikan lagi ke toples, jadi isi list tidak berkurang dan hasil yang sama bisa keluar lagi.
- `choice` tidak hanya untuk list. String juga bisa: `random.choice("abc")` hasilnya "a", "b", atau "c".
- Aturannya: beri `choice` satu toples. Kalau ditulis `random.choice("heads", "tails")` tanpa kurung siku, error, karena itu dua barang terpisah. Bukan karena "tidak pakai list".

### Peluang 50:50
- Awalnya saya kira 50:50 artinya hasilnya harus seimbang, misalnya heads 3 kali lalu tails 3 kali.
- Ternyata bukan. 50:50 artinya di setiap satu pengambilan, peluangnya sama, 1 dari 2.
- Toplesnya tidak punya ingatan. Setelah heads keluar 3 kali, pengambilan ke-4 tetap 50:50, bukan "giliran" tails.
- Kalau diambil sedikit, hasilnya bisa berat sebelah. Kalau diambil banyak sekali (1000 kali), biasanya mendekati 500 dan 500, tapi jarang pas persis.
- Peluang tiap isi = 100% dibagi jumlah isi toples. 2 isi = 50%, 3 isi = sekitar 33,3%, 4 isi = 25%.
- Yang dihitung jumlah gulungan, bukan jumlah nama yang berbeda. `["heads", "heads", "tails"]` berarti heads 2 dari 3 (sekitar 66,7%), tails 1 dari 3.

### `random.randint`
- `random.randint(1, 10)` mengambil satu bilangan bulat acak dari 1 sampai 10. Setiap dipanggil diundi ulang, jadi angka yang sama bisa keluar berkali-kali.
- Kedua ujungnya ikut (inclusive). Angka 1 dan 10 sama-sama bisa keluar, jadi ada 10 kemungkinan, masing-masing 10%.
- Hati-hati beda dengan range:

| Ditulis | Angka 10 ikut? |
|---|---|
| `random.randint(1, 10)` | ikut (1 sampai 10) |
| `range(1, 10)` | tidak ikut (1 sampai 9) |

- Bedanya dengan `choice`: `choice` diberi satu toples (sequence), `randint` diberi dua angka (awal dan akhir).

### Kosakata
| Kata | Arti |
|---|---|
| library | kumpulan kode siap pakai yang ditulis orang lain |
| module | satu file `.py` berisi kumpulan function |
| randomness | keacakan |
| marginally | sedikit, tipis |
| sequence | kumpulan yang isinya berurutan (list, string) |
| namespace | daftar nama yang dikenal di filemu |
| inclusive | ujungnya ikut dihitung |

### Yang mau dicoba
- Di interactive mode: `import random`, lalu ketik `choice(["a", "b"])` (harusnya NameError), lalu `random.choice(["a", "b"])` (jalan).
- Jalankan `random.choice(["heads", "tails"])` beberapa kali, lihat hasilnya berubah-ubah.
- Buat file kecil dengan for loop 10 kali yang mencetak `random.choice(["heads", "tails"])`, jalankan beberapa kali, cek apakah selalu 5 dan 5.
- Lanjut lecture dari sekitar menit 10.

---

## Hari 2 – 10 Oktober 2026

Belajar sekitar satu jam, tapi video yang tertonton cuma sekitar 5 menit (sampai bagian shuffle). Soalnya saya banyak pause dan banyak bertanya, terutama tentang bagaimana sistemnya bekerja.

### Pemanasan: murojaah materi kemarin
1. `import random` lalu `choice(["heads", "tails"])`, mana yang error?
   - Jawaban saya: yang error baris `choice(...)`, karena filemu cuma kenal nama `random`, belum kenal `choice`.
   - Yang saya lupa sebut: nama error-nya **NameError**. Perbaikannya ada dua: tulis `random.choice(...)`, atau ganti import-nya jadi `from random import choice`.
2. Kenapa `random.choice("heads", "tails")` error, tapi `random.choice("abc")` jalan, padahal dua-duanya tanpa kurung siku?
   - Jawaban saya: `"heads", "tails"` itu dianggap dua barang, bukan satu. `"abc"` itu masih satu barang (satu string) yang isinya a, b, c.
   - Tambahan: `"abc"` bisa diundi karena string itu sendiri sudah sequence. Kotaknya sudah ada, jadi tidak perlu kurung siku lagi.
3. `random.randint(1, 6)` dan hasilnya 6, 6, 6. Apakah peluang 6 di panggilan ke-4 jadi lebih kecil?
   - Jawaban saya: tidak, peluangnya masih tetap ada. Angka yang mungkin keluar 1 sampai 6, inklusif angka 6 juga.
   - Lebih tepatnya: peluangnya bukan cuma masih ada, tapi tetap sama persis, 1 dari 6. Toples tidak punya ingatan.

### Kode di layar: generate.py
```python
import random

number = random.randint(1, 10)
print(number)
```
- Dijalankan beberapa kali, hasilnya beda-beda: 10, 2, 5.

### Kosakata: deferring
- DeepL menerjemahkan "menunda", tapi itu bukan arti yang dipakai di sini.
- "defer sesuatu" = menunda (*defer the meeting* = menunda rapat).
- "defer **to** seseorang" = menyerahkan atau mempercayakan kepada (*defer to the ustadz* = menyerahkan keputusan ke ustadz).
- David bilang *"you're deferring to Python to actually do..."*. Artinya urusan mengacak angka diserahkan ke Python. Saya tidak menulis cara mengacaknya, cukup panggil `random.randint(1, 10)`, caranya urusan Python.
- Mirip kalau ada santri bertanya hukum tajwid yang rumit, lalu saya bilang "tanya ke ustadz senior saja". Itu bukan menunda, tapi menyerahkan ke yang lebih ahli.

### random.shuffle
```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
```
- shuffle mengacak urutan isi list. Hasilnya misalnya queen, jack, king.

### Kosakata: permutations
- Permutation = susunan urutan yang mungkin dari sekumpulan barang. Barangnya sama, yang beda hanya urutannya.
- Kartu 3 buah (jack, queen, king) cuma bisa disusun dengan 6 cara.
- Waktu dijelaskan pakai "cabang pohon", saya tidak tergambar. Yang membuat saya paham adalah cara mengelompokkan. Contohnya 3 santri mau setoran (Ali, Umar, Zaid):
  - Kalau Ali maju pertama, sisanya Umar dan Zaid, cuma bisa 2 urutan: Ali, Umar, Zaid atau Ali, Zaid, Umar.
  - Kalau Umar maju pertama, juga 2 urutan.
  - Kalau Zaid maju pertama, juga 2 urutan.
  - Jadi ada 3 kelompok × 2 urutan = 6 urutan.
- Makanya David bilang *"there's not that many permutations we might see"*. Karena cuma 6 kemungkinan, kalau programnya dijalankan berkali-kali, urutan yang sama cepat muncul lagi. Itu bukan berarti shuffle-nya rusak.
- Kalau santrinya 10 orang, cara menyusunnya langsung melonjak jadi 3.628.800 kali kemungkinan muncul nya 
- Untuk koding, yang penting cukup paham bahwa jumlah susunannya terbatas. Cara menghitungnya cuma bonus.

### Bedanya shuffle dengan function yang lain
- Kata David, shuffle ini agak beda dari function pada umumnya. Ternyata bedanya bukan soal apa yang dikerjakan, tapi soal bagaimana hasilnya diberikan.
- Function yang selama ini saya pakai, hasilnya dikembalikan (return), lalu ditampung pakai `=`:
```python
number = random.randint(1, 10)
coin = random.choice(["heads", "tails"])
```
- shuffle tidak mengembalikan apa-apa. Dia langsung mengacak list aslinya. Makanya `random.shuffle(cards)` ditulis sendirian, tanpa `=`.
- Analogi:
  - choice = minta ustadz memilihkan satu nama dari toples, lalu ustadz menyerahkan kertas nama itu ke tangan saya.
  - shuffle = saya serahkan papan absen ke ustadz, lalu ustadz mengacak urutan nama di papan itu langsung. Tidak ada papan baru, papan yang lama yang berubah.
- Kebalikan dari `c.lower()`. Dulu saya belajar `c.lower()` tidak mengubah `c`, hasilnya harus ditampung (`c = c.lower()`). shuffle justru langsung mengubah list-nya.

### Jebakan shuffle
```python
cards = random.shuffle(cards)   # salah
print(cards)                    # None
```
- Karena shuffle tidak mengembalikan apa-apa, yang masuk ke `cards` adalah `None`, dan list kartunya malah hilang.
- Ini salah satu cara munculnya `None` seperti di error `NoneType` waktu Week 3.

### Kosakata
| Kata | Arti |
|---|---|
| defer to | menyerahkan atau mempercayakan kepada |
| permutation | susunan urutan yang mungkin |
| shuffle | mengocok, mengacak urutan |

### Yang mau dicoba
- Di interactive mode: buat list `cards`, jalankan `random.shuffle(cards)`, lalu `print(cards)`. Ulangi beberapa kali.
- Buktikan jebakannya: `x = random.shuffle(cards)`, lalu `print(x)`. Harusnya `None`.
- Lanjut lecture dari bagian sesudah shuffle.

---

## Hari 3 – 11 Oktober 2026

Pagi murojaah dulu (catatannya nanti di murojaah.md). Siangnya lanjut lecture sampai bagian `sys.exit`, sekitar menit 40 dari total 1 jam 17 menit. Banyak istilah Inggris yang saya tanyakan.

### Pemanasan: murojaah shuffle
1. Kenapa `random.shuffle(cards)` ditulis tanpa `=`?
   - Jawaban saya: shuffle punya aturan beda dari function biasa. Tanpa `=` sudah bisa mengubah value-nya, sedangkan function lain harus disimpan dulu di variabel.
   - Yang diluruskan: shuffle tidak **menampilkan** apa-apa, dia cuma **mengubah urutan** list aslinya. Yang menampilkan tetap `print`.
2. Output dari `cards = random.shuffle(cards)` lalu `print(cards)`?
   - Jawaban saya: NameError, karena shuffle tidak bisa disimpan ke variabel. **Salah.**
   - Yang benar: tidak ada error, outputnya `None`. Python boleh-boleh saja menyimpan hasil shuffle ke variabel, cuma hasilnya `None`, jadi list kartunya tertimpa.
   - Kenapa bukan NameError: NameError muncul kalau Python tidak kenal namanya. Di sini nama `cards` dikenal (ada di absen sejak baris pertama), isinya saja yang berubah jadi `None`.
   - Padahal jebakan ini sudah ada di catatan Hari 2. Berarti baca catatan belum tentu nempel, harus diuji.
3. 2 santri (Ali dan Umar) bisa disusun berapa cara?
   - Saya kira pertanyaannya pakai kode, jadi saya jawab pakai choice, shuffle, dan "range". Ternyata maksudnya hitung manual: 2 cara (Ali, Umar dan Umar, Ali).
   - Yang saya sebut "range" itu maksudnya `randint`. randint dan choice tidak menyusun urutan, cuma shuffle yang menyusun urutan.

### Permutation 10 santri: kenapa melonjak?
- Caranya sama seperti 3 santri: 10 × 9 × 8 × ... × 1 = 3.628.800.
- Setiap tambah satu orang, jumlah sebelumnya **dikalikan**, bukan ditambah. Makanya naiknya tajam.
- 2 → 2, 3 → 6, 4 → 24, 5 → 120, ... 10 → 3.628.800.
- 3 kartu cuma 6 kemungkinan, jadi urutan yang sama cepat terulang. 10 kartu ada 3,6 juta kemungkinan, jadi jarang terulang.

### Bisakah peluang kartu diatur?
- Ada mahasiswa yang bertanya: bisa tidak king dibuat lebih sering keluar daripada jack dan queen?
- Jawaban David: dengan choice, randint, dan shuffle tidak bisa, karena function itu sengaja dibuat sederhana dan semua isinya peluangnya sama. Tapi bisa kalau buat function sendiri, atau pakai function yang lebih canggih di library.
- Sebenarnya saya sudah ketemu satu akal-akalan: `random.choice(["heads", "heads", "tails"])`. Function-nya tetap choice, tapi isi toplesnya diatur, jadi peluang heads 2 dari 3.

### Module statistics dan mean
```python
import statistics

print(statistics.mean([100, 90]))
```
- Hasilnya 95.
- Nama function-nya `mean`, bukan "main". (Di catatan kecil saya sempat kebalik.)
- Mean artinya **rata-rata**: semua angka dijumlahkan, lalu dibagi banyaknya angka. (100 + 90) ÷ 2 = 95.
- Awalnya saya kira mean itu "angka tengah", atau "nilai awal tambah nilai akhir dibagi dua". Ternyata bukan. Di contoh ini memang kebetulan pas, karena angkanya cuma dua. Kalau angkanya `[100, 90, 80]`, yang dijumlahkan semuanya lalu dibagi 3. "Angka tengah" itu istilah lain, namanya median.
- Saya juga sempat mengira mean harus ada dua argumen. Ternyata mean cuma mau **satu** argumen, yaitu satu toples (list) yang isinya boleh berapa angka saja. Mirip choice: `statistics.mean(100, 90)` tanpa kurung siku akan error, karena itu dua barang.
- Yang menarik: di kode ini tidak ada variabel sama sekali. List langsung masuk ke mean, hasil mean langsung masuk ke print. Bacanya dari dalam ke luar, sama seperti `int(input(...))`.
- Kalau pakai variabel juga boleh (`scores = [100, 90]`, `average = statistics.mean(scores)`, `print(average)`). Dua-duanya benar, trade-off antara ringkas dan mudah dibaca.

### Module sys dan sys.argv
- `sys` itu module, sama seperti random dan statistics. `sys.argv` dibaca: dari kitab sys, ambil argv.
- argv = **arg**ument **v**ector. Vector di sini anggap saja list. Kata David itu cuma "fancy way", istilah keren untuk sesuatu yang sederhana.
- Isinya: daftar kata yang diketik user di terminal, sekalian waktu menjalankan program. Jadi tidak perlu prompt input.
```
$ python name.py David
```
```python
sys.argv  →  ["name.py", "David"]
#              indeks 0    indeks 1
```
- Indeks 0 selalu nama file-nya sendiri. Kata dari user baru mulai indeks 1. Makanya kodenya pakai `sys.argv[1]`.
- Bedanya dengan input():
  - `input()` = santri dipanggil maju dulu, baru ditanya "mau setoran surat apa?"
  - `sys.argv` = "Ali, maju, setoran Al-Mulk." Datanya disebut sekalian waktu dipanggil.

### Kalau nama lengkap (ada spasi)
- `python name.py David Malan` → sys.argv jadi `["name.py", "David", "Malan"]`. Spasi memisahkan kata, jadi David dan Malan dianggap dua argumen.
- Supaya nama lengkap dianggap satu argumen, pakai tanda kutip: `python name.py "David Malan"` → `["name.py", "David Malan"]`.

### IndexError
- Kalau dijalankan tanpa nama (`python name.py`), sys.argv cuma `["name.py"]`. Lalu `sys.argv[1]` minta barang kedua yang tidak ada.
- Hasilnya: `IndexError: list index out of range`. Error baru: nomor urut yang diminta di luar jangkauan list.
- Ibarat absen cuma berisi 1 nama, lalu saya panggil santri nomor 2. Orangnya tidak ada.
- Kalau diganti `[0]`, memang tidak error, tapi hasilnya `hello, my name is name.py`. Program jalan, tapi salah. Sama seperti catatan saya di Pset 1: program yang jalan belum tentu benar.

### Cara memperbaikinya: beberapa metode
1. Pakai `try` dan `except IndexError` → print "Too few arguments". Mirip Week 3, tapi error yang ditangkap IndexError, bukan ValueError.
2. Pakai `len(sys.argv)` untuk menghitung ada berapa kata:
   - `< 2` → terlalu sedikit (too few)
   - `> 2` → terlalu banyak (too many)
   - `else` → pas 2, aman pakai `sys.argv[1]`
   - Masalahnya: print utama (tugas inti program) jadi terselip di `else`, paling bawah. David bilang tugas utamanya "relegated" ke else clause.
3. Pakai `sys.exit(...)` di dalam if dan elif.

### sys.exit
```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```
- `sys.exit` = langsung keluar dari program saat itu juga, sambil menampilkan pesannya.
- Jadi kalau argumennya salah, program berhenti, dan print di bawah (di luar if, bukan di luar loop) tidak pernah dijalankan.
- Karena itu `else` tidak dibutuhkan lagi, dan print utamanya tidak terselip di dalam else.
- Mirip catatan Vanity Plates: kalau if diakhiri return, else-nya bisa dibuang. Bedanya, di sini yang menghentikan adalah sys.exit, dan yang dihentikan seluruh program, bukan cuma function.

### SyntaxError lagi: mea culpa
- David sempat kena `SyntaxError: unterminated string literal` karena lupa tanda kutip penutup di `"Too few arguments`.
- Kata David: SyntaxError itu "mea culpa", salah programmer sendiri, bukan salah user.

### Kosakata
| Kata | Arti |
|---|---|
| skew | membuat condong, berat sebelah |
| mean | rata-rata |
| leverage | memanfaatkan |
| argument vector (argv) | daftar kata yang diketik di terminal |
| infer | menyimpulkan dari petunjuk |
| at first glance | sekilas |
| rather + sifat | cukup, agak (*rather complicated* = cukup rumit) |
| rather than | daripada |
| and yet | namun, tetapi |
| as though | seolah-olah |
| indeed | memang, betul |
| frankly | jujur saja, terus terang |
| isn't all that + sifat | tidak terlalu |
| amount (kata benda) | jumlah |
| amount to | sama dengan, berarti |
| from the get-go | sejak awal (get-go di sini kata benda, bukan dua kata kerja) |
| too few / too many | terlalu sedikit / terlalu banyak |
| quite | cukup; not quite = belum sepenuhnya |
| quiet / quit | hening / berhenti, keluar (beda dengan quite) |
| mea culpa | salahku (bahasa Latin) |
| messed up | mengacaukan, berbuat salah |
| red herring | pengalih perhatian |
| relegated | tersingkir ke posisi kurang penting |
| name tag | label nama |
| clause | bagian, klausa |
| absolutely | benar-benar, tentu saja |
| ultimately | pada akhirnya, intinya |
| incarnation | versi, bentuk |
| prematurely | sebelum waktunya, lebih awal |

### Yang mau dicoba
- Buat `name.py` sendiri, coba tiga cara: `python name.py`, `python name.py David`, `python name.py David Malan`, dan `python name.py "David Malan"`. Bandingkan hasilnya.
- Coba `statistics.mean` dengan list berisi 3 angka atau lebih, hitung manual dulu, lalu cocokkan.
- Lanjut lecture dari bagian sesudah sys.exit (sekitar menit 40).
