# CS50P Week 6: File I/O

## Hari 1 – 21 Oktober 2026

Mulai Lecture 6, sampai sekitar **menit 31** (bagian CSV). Ngoding 2 jam, bahasa Inggris 35 menit.

### Diskusi sebelum mulai: sudah 5 week, lalu ke mana?
- Tidak terasa sudah 5 week. Tinggal Week 6, 7, 8, 9, lalu final project.
- CS50P baru **fase 1 dari 4** di roadmap saya: (1) fondasi berpikir lewat CS50P, (2) bahasa project saya (JavaScript, TypeScript, web, SQL, Git), (3) AI engineering, (4) siap kerja. Ternyata saya malah lebih cepat dari jadwal: Week 3–5 dijadwalkan selesai di bulan kedua.
- Apakah materi sejauh ini sudah cukup untuk project sendiri? Untuk program kecil di terminal, sudah. Bahkan dekat dengan pekerjaan AI engineer:
  - Bitcoin (requests + JSON) = cara yang sama dengan memanggil model AI lewat API.
  - Exceptions = menangani API yang gagal.
  - Function yang return = "tools" yang bisa dipanggil model AI.
  - Unit test = mirip **evaluasi** jawaban AI.
- Yang belum: menyimpan data (Week 6, mulai hari ini), mengorganisasi kode besar (Week 8, OOP), tampilan web dan database (fase 2).
- **Ide final project saya: jurnal olahraga di terminal**, karena saya sering ke gym dan ingin konsisten. Cocok dengan File I/O (menyimpan catatan latihan) dan unit test (misalnya menghitung streak). Ide fitur dicatat dulu, rancangannya setelah Week 6.
- Python bukan cuma untuk backend dan database. Program CLI, otomatisasi, analisis data, dan AI juga wilayah Python.

**Soal fase 2 (JavaScript dan TypeScript):** saya khawatir rasanya seperti belajar bahasa baru lagi. Ternyata **bahasa kedua jauh lebih mudah**, karena yang paling sulit itu cara berpikirnya, dan itu sudah dibangun di CS50P.

| Konsep | Python | JavaScript |
|---|---|---|
| Kondisi | `if` / `elif` / `else` | `if` / `else if` / `else` |
| Function | `def`, `return` | `function`, `return` |
| Error | `try` / `except`, `raise` | `try` / `catch`, `throw` |
| Pinjam kode | `import` | `import` |
| Tes | pytest, `assert` | Jest/Vitest, `expect` |

- Ibarat santri yang sudah paham nahwu dan sharaf lalu membaca kitab bidang lain: kaidahnya sudah ada, tinggal mengenal istilah baru.
- TypeScript = JavaScript ditambah keterangan jenis data. Di Week 9 CS50P ada **type hints** yang idenya mirip.
- Tidak harus menguasai seluruh materi JavaScript. Tujuan fase 2: bisa membaca dan memeriksa kode project saya sendiri (menelusuri alur TahfidzFlow dari halaman sampai database).

### Pemanasan (murojaah)
1. **raise di `convert`, tidak ada try/except di `main`.** Error naik terus sampai ujung. Kalau benar-benar tidak ada except, program crash. Benar.
2. **`convert("3/0")` vs `convert(3/0)`.** Saya sempat mencampur dua kasus:

| Ditulis | Yang terjadi |
|---|---|
| `convert("3/0")` | String masuk ke convert, ZeroDivisionError muncul **di dalam** convert |
| `convert(3/0)` | Python menghitung 3/0 **duluan**, error meledak di baris tes, convert **tidak pernah dipanggil** |
| `convert(2/4)` | 0.5 masuk ke convert, error `'float' object has no attribute 'split'` |

3. **Kenapa Y = 0 harus terpisah.** Semua syarat dalam satu if berujung ke satu else, jadi hanya satu jenis error yang bisa keluar. Benar.
4. **Setelah `.json()` bentuknya apa, dan salah nama kunci jadi error apa?** Dictionary, benar. Tapi saya ragu antara ValueError dan KeyError. Yang benar **KeyError**. Ini koreksi yang sama dengan murojaah 17 Oktober.
   - KeyError = kunci yang diminta tidak ada di dictionary. "Key" = kunci dictionary, bukan API key.
   - Kalau API key salah, dictionary-nya **tetap ada**, tapi isinya pesan penolakan, misalnya `{"error": "Invalid API key"}`. Waktu kode meminta `["data"]`, kunci itu tidak ada, jadi KeyError.
   - Analogi: minta daftar harga ke loket, tapi karena kartu anggota salah, yang diberikan surat penolakan. Suratnya ada, tapi kolom "harga" tidak ada di dalamnya.

### Kenapa butuh file?
- Selama ini data disimpan di **variabel**, dan **downside**-nya: isi variabel **hilang** begitu program selesai.
- Kalau disimpan di **file**, datanya tetap ada walaupun program sudah ditutup. Untuk jurnal olahraga saya, ini yang membuat catatan kemarin masih bisa dibaca hari ini.
- Contoh awal David: tiga nama ditampung di list, lalu diurutkan dengan **`sorted(names)`**, yang menghasilkan list baru yang sudah urut abjad. List aslinya tidak berubah.
- `for _ in range(3):` → `_` dipakai sebagai nama variabel loop kalau isinya tidak dipakai. Kebiasaan programmer, bukan aturan.

### Function `open`
```python
file = open("names.txt", "w")
```
- `open` punya dua argumen:
  1. **Nama file**: `"names.txt"`.
  2. **Mode**: satu huruf yang menjelaskan mau diapakan file itu.

| Mode | Singkatan | Artinya |
|---|---|---|
| `"r"` | read | Membaca. Ini **default**, boleh tidak ditulis |
| `"w"` | write | Menulis. **Isi lama dikosongkan dulu** (menimpa) |
| `"a"` | append | Menambahkan di bagian akhir, isi lama tetap |

- Kalau `names.txt` belum ada, `"w"` (dan `"a"`) membuatnya.
- **Ekstensi `.txt`** = text, isinya teks biasa. Ini **convention** (kebiasaan yang disepakati), bukan aturan. Python tidak peduli ekstensinya. Gunanya seperti label di map rapor: orang dan aplikasi lain langsung tahu isinya.
- Mode `"r"` itu **implicit** (tersirat, default). Polanya sama dengan `hello(to="world")` dan `print(..., end="\n")`.

### Variabel `file` itu isinya apa?
Ini bagian yang paling lama saya pahami.
- `file` **bukan** nama spesial, itu variabel biasa. Yang spesial isinya: **objek file** yang di-return oleh `open`.
- Variabel `file` **tidak menyimpan isi** file. Isinya **keterangan** tentang file yang sedang dibuka: nama, mode, encoding, posisi menulis, dan apakah masih terbuka. Keterangan-keterangan itu tidak saling berhubungan, cuma daftar keterangan tentang satu file.
- "Terhubung" maksudnya: variabel `file` di **kode saya** menyambungkan program ke file sungguhan (misalnya `catat.txt`) di **komputer saya**.
- Bisa dilihat langsung dengan `print(file)`, hasilnya kira-kira `<_io.TextIOWrapper name='names.txt' mode='w' encoding='UTF-8'>`.
- Analogi **remote TV**: TV = file sungguhan di komputer, remote = variabel `file`. Remote bukan TV, tidak menyimpan acara, tapi lewat remote kita bisa menyuruh TV.
- Analogi **kartu peminjaman perpustakaan**: kartunya bukan buku, tapi mencatat buku mana, untuk apa, sampai halaman berapa.
- Setelah baris `open(...)`, file baru dibuat dan dibuka, isinya masih kosong. Seperti mengambil buku tulis kosong dan membukanya.

### Method milik objek file
- `file.write(...)` = menulis ke file. `file.close()` = menutup file.
- `write`, `read`, `close` itu **method milik objek file**, bukan milik function `open`. Makanya ditulis `file.write`, bukan `open.write`. Ibaratnya pabrik (`open`) membuat remote (objek file), dan tombol-tombolnya ada di remote.
- Setiap jenis objek punya method-nya sendiri:

| Objek | Dibuat oleh | Method |
|---|---|---|
| String | diketik atau `input()` | `.lower()`, `.split()`, `.startswith()` |
| Response | `requests.get(...)` | `.json()` |
| Figlet | `Figlet()` | `.renderText()`, `.setFont()` |
| File | `open(...)` | `.write()`, `.read()`, `.close()` |

- Integer juga objek, tapi method-nya jarang dipakai. Untuk angka kita lebih sering pakai operator. Di Python hampir semuanya objek. Membuat objek sendiri nanti di Week 8.
- Waktu menulis nama ke file, setiap nama diberi `\n` supaya pindah baris.

### Mode `"w"` menimpa
- David menjalankan program beberapa kali (Hermione, Harry, Ron), tapi isi `names.txt` **cuma "Ron"**. Mode `"w"` mengosongkan isi lama setiap kali dibuka.
- Vishal (mahasiswa) mengusulkan supaya setiap nama ditambahkan, jadi pakai mode **`"a"`**.
- David menghapus file dengan `rm names.txt` di terminal. Saya kira kalau mau ganti mode harus dihapus dulu. Ternyata **tidak**. Mode itu bukan sifat yang menempel di file, mode hanya berlaku saat file dibuka. David menghapus cuma supaya demonya mulai dari bersih.
- Dua macam "menghapus":

| | Yang terjadi | Filenya |
|---|---|---|
| `rm names.txt` di terminal | File dibuang seluruhnya | Hilang (tidak masuk Recycle Bin!) |
| `open("names.txt", "w")` | Isinya dikosongkan, lalu ditulis ulang | Tetap ada |

- Ibarat buku tulis yang sama: bisa dibuka untuk dihapus lalu ditulis ulang, atau untuk menambah di halaman terakhir. Tergantung niat saat membukanya.

### Keyword `with`
```python
with open("names.txt", "r") as file:
    lines = file.readlines()
```
- `with` = "selama di dalam blok ini". Dengan `with`, file **otomatis dibuka dan ditutup**. Tidak perlu ingat menulis `file.close()`.
- `as` juga keyword, artinya **"sebagai"**: memberi nama pada objek yang dihasilkan `open`.
- Sama dengan cara lama `file = open(...)` lalu `file.close()`, tapi lebih aman.
- Polanya sama dengan `with pytest.raises(...)` di Week 5.

### Membaca file: `readlines()` dan `\n`
- `file.readlines()` = method yang membaca semua baris dan me-return **list**, satu baris satu string.
- Tebakan saya benar: `\n` **ikut terbawa**, jadi hasilnya `["Hermione\n", "Harry\n", "Ron\n"]`.
- Tebakan saya yang salah: saya kira list-nya jadi vertikal. Ternyata `\n` hanya satu karakter di ujung setiap string. Kalau list di-print utuh, tetap satu baris dan `\n` terlihat sebagai tulisan.
- Waktu di-loop dan setiap baris di-print, muncul **baris kosong ganda**. Ini **symptom** (gejala). Penyebabnya dua pindah baris: satu dari `\n` di string, satu dari `print`.
- Dua cara memperbaikinya:
  1. `print(..., end="")`. Bawaan `end` itu `"\n"`, **bukan kosong**. Jadi menulis `end="\n"` tidak mengubah apa-apa. Supaya print tidak pindah baris, isinya harus kosong `""`. Ini hanya menghilangkan pindah baris milik print, `\n` di string tetap bekerja.
  2. **`line.rstrip()`**, yang dipakai David. Membuang whitespace di **kanan** (r = right).
- Saya kira `strip` cuma membuang spasi. Ternyata yang dibuang semua **whitespace**: spasi, `\n`, dan tab. `\n` itu **satu karakter** (`len("Ron\n")` = 4) dan termasuk whitespace. `strip` hanya membuang di pinggir, bukan di tengah.

### Lebih ringkas: loop langsung ke file dan `sorted`
Catatan di buku saya: "ternyata bisa dibuat lebih simple".
- Objek file bisa **langsung di-loop**, tidak perlu `readlines()` dulu:

```python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

- `sorted` juga bisa dipakai **langsung ke file**, tanpa list `names` dan tanpa loop tambahan:

```python
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
```

### `sorted`: `reverse` dan `key`
- Ada mahasiswa yang bertanya apakah bisa diurutkan **descending** (Z ke A). Bisa: `sorted(names, reverse=True)`. Bawaannya `reverse=False`.
  - ascending = naik (A→Z, 1→9), descending = turun (Z→A, 9→1).
- **`key`** menjawab "diurutkan **berdasarkan apa**?". Bawaannya `None`, artinya berdasarkan nilainya langsung. `key` diberi sebuah **function**, lalu `sorted` membandingkan hasil function itu.
  - Contoh: `sorted(names, key=len)` mengurutkan dari nama terpendek.
  - Ditulis `key=len` **tanpa kurung**. Kita menyerahkan function-nya, `sorted` yang memanggil.
  - Analogi: santri bisa dibariskan berdasarkan nama, tinggi badan, atau jumlah juz hafalan. Santrinya sama, patokannya beda.

### Kenapa Python tidak membuang `\n` otomatis?
- Ada mahasiswa bertanya: `\n` selalu kita buang setelah dibaca, bukankah ini desain yang jelek? Kenapa tidak di-strip otomatis?
- Saya sempat bingung, karena `\n` kan dibutuhkan. Ternyata ada **dua saat** berbeda:
  1. **Di file**: `\n` dibutuhkan sebagai pemisah antar nama. Tanpa itu jadi `HermioneHarryRon`.
  2. **Setelah dibaca ke program**: setiap nama sudah jadi item terpisah di list, jadi `\n` tidak berguna lagi.
- Mahasiswa itu bilang `\n` tidak berguna **setelah dibaca**. Jawab David: Python membaca **as is** (apa adanya), karena **kadang kita masih butuh** `\n`, misalnya menyalin isi file ke file lain persis sama. Programmer yang memutuskan.
- Prinsipnya: lebih baik diberi data utuh lalu kita buang sendiri, daripada dibuang diam-diam padahal kita butuh. Yang sudah dibuang tidak bisa diminta kembali.
- Analogi:

| Analogi | Di Python |
|---|---|
| Rak berisi kitab | File `names.txt` |
| Sekat antar kitab | `\n` |
| Petugas yang mengambilkan kitab | `readlines()` / `for line in file` |
| Melepas sekat sendiri | `rstrip()` |

  Kalau petugas membuang sekatnya diam-diam, lalu suatu saat kita ingin menata ulang kitab ke rak lain persis seperti aslinya, tidak bisa lagi.

### CSV
- David menambah asrama: isi `names.txt` jadi bergantian, baris nama lalu baris asrama. David khawatir **"mixing apples and oranges"**: mencampur dua jenis data. Membingungkan dan **ambiguous**. Kalau satu baris terlewat, semua pasangan di bawahnya bergeser.
- Solusinya **convention** yang dipakai banyak programmer: **CSV** (*comma-separated values*). Satu baris = satu santri lengkap, dipisah koma:

```
Hermione,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

- Waktu dibaca, setiap baris bisa di-`split(",")`, sama seperti `"3/4".split("/")` di Refueling.
- CSV bisa dibuka dan diekspor dari Excel, Apple Numbers, dan Google Spreadsheets. Cocok untuk jurnal olahraga saya nanti, misalnya `tanggal,jenis latihan,durasi`.

### Kosakata
| Kata | Arti |
|---|---|
| downside | kelemahan, sisi buruk (lawannya upside) |
| a downside of which is | yang kelemahannya adalah |
| eventually | pada akhirnya, suatu saat nanti. **Bukan** "mungkin" |
| on the other hand | di sisi lain |
| if I were to | seandainya saya |
| not quite | belum sepenuhnya |
| alphabetical order | urutan abjad |
| as opposed to | alih-alih, bukannya (ejaannya pakai -d dan "to") |
| go about (doing) | menempuh cara untuk |
| whose | yang ...-nya (kepemilikan). Beda dengan who's = who is |
| purpose in life | tujuan hidup (gaya bercanda David) |
| usage | cara pemakaian |
| relatively | relatif, cukup |
| straightforward | sederhana, lugas |
| its / it's | its = miliknya, it's = it is |
| conventional / convention | sesuai kebiasaan umum / kebiasaan yang disepakati |
| overwriting | menimpa |
| implicit / explicit | tersirat / ditulis jelas |
| quote/unquote | cara lisan menyebut tanda kutip |
| symptom | gejala (yang terlihat dari bug) |
| ascending / descending | urutan naik / turun |
| germ (of an idea) | kuman; benih, bibit ide |
| thus far | sejauh ini (sama dengan so far) |
| as is | apa adanya |
| worry | khawatir |
| apples and oranges | dua hal yang jenisnya berbeda |
| ambiguous | ambigu, bisa ditafsirkan lebih dari satu cara |

### Bahasa Inggris saya keteteran
- Jujur, saya lebih banyak coding. Bahasa Inggris cuma istiqomah di Duocards dan freeCodeCamp (satu task sehari). Ngobrol dengan AI 10 menit hampir tidak pernah. Kadang jam 9 malam sudah mau istirahat, bahasa Inggris belum.
- Duocards saya sudah bercampur dengan kosakata umum, jadi kosakata coding tenggelam.
- Keputusan: **setiap hari Claude memberi 10 kuis kosakata** khusus dari lecture CS50P (bisa mode flashcard juga), di awal sesi bersama pemanasan coding. Kata lama diulang, yang salah lebih sering muncul.
- Saran lain dari Claude:
  - Kerjakan bahasa Inggris **duluan**, sebelum membuka lecture.
  - Satu segmen pendek per hari, tonton dulu tanpa pause dan tanpa DeepL, tebak intinya, baru diputar ulang.
  - Speaking diganti **shadowing satu kalimat David** per hari, 2–3 menit.
  - Jurnal mencatat menit bahasa Inggris yang **sebenarnya**.

### Yang mau dicoba
- Kerjakan Kuis Kosakata #1 besok pagi.
- Di terminal Python: `file = open("coba.txt", "w")`, lalu `print(file)`, `file.close()`. Lihat `coba.txt` muncul di daftar file.
- Coba `"Ron\n".rstrip()`, `"  Ron  \n".strip()`, dan `len("Ron\n")`.
- Catat ide fitur jurnal olahraga.
- Lanjut lecture dari menit 31 (CSV).
