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
