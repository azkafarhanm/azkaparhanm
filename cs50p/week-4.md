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
- Kalau santrinya 10 orang, cara menyusunnya langsung melonjak jadi 3.628.800.
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
