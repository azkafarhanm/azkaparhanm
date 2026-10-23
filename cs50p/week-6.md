# CS50P Week 6: File I/O

## Hari 1 – 21 Oktober 2026

Mulai Lecture 6, sampai sekitar **menit 31** (bagian CSV). Ngoding 2 jam, bahasa Inggris 35 menit.

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

### Yang mau dicoba
- Kerjakan Kuis Kosakata #1 besok pagi.
- Di terminal Python: `file = open("coba.txt", "w")`, lalu `print(file)`, `file.close()`. Lihat `coba.txt` muncul di daftar file.
- Coba `"Ron\n".rstrip()`, `"  Ron  \n".strip()`, dan `len("Ron\n")`.
- Catat ide fitur jurnal olahraga.
- Lanjut lecture dari menit 31 (CSV).

---

## Hari 2 – 22 Oktober 2026

### Kuis Kosakata #1
- Pagi ini mengerjakan kuis kosakata pertama dari Claude (10 soal, kata-kata dari lecture). Hasilnya **100%**. Kuis berikutnya akan dibuat lebih susah: ada soal kebalikan (arti Indonesia → frasa Inggris) dan kata lama dicampur.

### Pemanasan
- Saya sempat salah: mengira mode `"w"` yang dijalankan tiga kali akan menyimpan tiga nama. Ternyata `"w"` **menimpa**, jadi yang tersisa cuma nama terakhir. Kalau mau menambah, pakai `"a"`.
- `with` menutup file **otomatis** setelah blok selesai, jadi tidak perlu `file.close()`.

### Roadmap versi 2
- Saya bertanya soal Fase 0 di roadmap. Ternyata bagian keamanan TahfidzFlow (backup/restore Neon, log Vercel, rollback Vercel) **belum sama sekali** saya pelajari.
- Keputusan: target waktu **tidak diubah**, supaya saya bisa membandingkan rencana dengan kenyataan. Ditambah kolom **realisasi**.
- Keamanan TahfidzFlow dikerjakan bareng Claude di sesi akhir pekan, tidak mendesak.
- Bahasa Inggris: dikerjakan sebelum lecture, plus **shadowing** satu kalimat David 2–3 menit.

### Lecture: membaca CSV (lanjut dari menit 31)
- Awalnya David memakai `row[0]` dan `row[1]` hasil `split`. Lalu diganti supaya lebih jelas, langsung dibongkar:

```python
name, house = line.rstrip().split(",")
```

- Awalnya David menyimpan kalimat jadi (`f"{name} is in {house}"`) ke list lalu di-sort. Ini disebut **hackish**: jalan, tapi akal-akalan. Yang di-sort itu kalimat, bukan data.
- Lebih baik simpan **datanya**: satu santri = satu **dictionary**, lalu semua dikumpulkan di list. Jadi **list of dicts**.

```python
student = {"name": name, "house": house}
students.append(student)
```

- `sorted(students)` langsung **error (TypeError)**, karena Python tidak tahu dictionary mau diurutkan berdasarkan apa. Perlu diberi `key`.

### `key=` dan bagaimana `sorted` memanggilnya
- David membuat function kecil:

```python
def get_name(student):
    return student["name"]
```

- Lalu `sorted(students, key=get_name)`. **Tanpa tanda kurung**, karena kita tidak memanggil `get_name`, kita **menyerahkannya** ke `sorted`.
- Yang paling lama saya pahami: **siapa yang memanggil `get_name`?** Jawabannya `sorted` sendiri. `sorted` mengambil satu per satu dictionary dari `students`, memanggil `get_name(dict itu)`, dapat **patokan** (namanya), memasangkan patokan dengan dictionary aslinya, mengurutkan berdasarkan patokan, lalu yang dikembalikan tetap **dictionary utuh**.
- Bisa juga `get_house` kalau mau diurutkan berdasarkan asrama.
- Saya juga bertanya: apakah kita harus bisa membuat semua ini **from scratch**? Kesimpulannya: yang penting memahami konstruksi berpikirnya. Library yang sudah ada dipakai saja.
- Saya bertanya kenapa tidak dictionary di dalam dictionary. Bisa, tapi list of dicts lebih cocok di sini karena tiap santri punya bentuk data yang sama dan kita ingin mengurutkannya.

### lambda
- Function `get_name` cuma dipakai sekali. Jadi David menggantinya dengan **lambda**: function **tanpa nama** (*anonymous function*), ditulis langsung di tempat. `return`-nya tidak ditulis, otomatis.

```python
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```

### Masalah koma di dalam data
- David mengganti asrama (*house*) dengan rumah (*home*). Alamat Harry: `Number Four, Privet Drive` (Privet Drive = nama jalan di cerita Harry Potter).
- Barisnya jadi `Harry,Number Four, Privet Drive`. `split(",")` menghasilkan **tiga** potongan, padahal yang menampung cuma dua (`name, home`). Hasilnya:

```
ValueError: too many values to unpack (expected 2)
```

- Ibaratnya membagi tiga kitab ke dua santri. Sama dengan Refueling kalau user mengetik `1/2/3`.
- Masalahnya: koma dipakai untuk **dua tugas**, sebagai pemisah dan sebagai isi data.

### Library `csv`
- David tidak mau **reinvent the wheel** (membuat ulang sesuatu yang sudah ada), jadi pakai library `csv`.
- Di file CSV, isi yang mengandung koma diberi **tanda kutip**: `Harry,"Number Four, Privet Drive"`.
- `csv.reader(file)` itu juga **objek**, bukan isi file. Ibaratnya **qari** yang paham aturan: tahu koma mana yang pemisah dan mana yang isi. Isi file baru dibaca saat `for` berjalan.
- Setiap putaran, `reader` memberikan satu baris dalam bentuk **list** yang sudah dipotong dengan benar: `["Harry", "Number Four, Privet Drive"]`. `rstrip()` juga tidak perlu lagi.
- Bisa diambil pakai indeks `row[0]`, `row[1]`. Indeks itu **nomor posisi** di list, bukan `row`-nya.
- Saya menebak bisa dibongkar seperti dulu (`name, home = row`). Ternyata benar, dan David malah langsung membongkarnya di dalam `for`:

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
```

- Hasilnya terurut, dan alamat Harry tampil utuh dengan komanya.

### Kosakata
| Kata | Arti |
|---|---|
| jagged | bergerigi, tidak rata |
| conversely | sebaliknya |
| instinctively / intuitively | secara naluri / secara intuitif |
| no longer | tidak lagi |
| hackish | akal-akalan, jalan tapi tidak rapi |
| verbose | bertele-tele, terlalu panjang |
| improve upon | memperbaiki, menyempurnakan |
| upon | di atas, saat |
| from scratch | dari nol |
| arguably | bisa dibilang |
| in one breath | dalam satu tarikan napas, sekaligus |
| if you will | kalau boleh dibilang begitu |
| take certain liberties | mengambil kebebasan tertentu, sedikit menyederhanakan |
| standardize on | sepakat memakai sebagai standar |
| in order to | untuk, supaya |
| delineate | menandai batas, memisahkan |
| reinvent the wheel | membuat ulang sesuatu yang sudah ada (buang waktu) |
| so to speak | istilahnya |
| dealing with | mengurus, menangani |
| albeit | meskipun (formal) |
| instead of | bukan, sebagai ganti |
| figure out | mencari tahu, memecahkan |
| no less | bahkan, pula (penekanan) |
| get out of the business of | terbebas dari urusan |

### Yang mau dicoba
- Kuis Kosakata #2 besok (lebih susah).
- Buat `students.csv` sendiri dengan satu alamat berkoma, coba versi `split(",")` sampai error, lalu versi `csv.reader`.
- Coba `sorted(..., key=lambda ...)` untuk mengurutkan berdasarkan `home`, juga dengan `reverse=True`.
- Lanjut lecture dari menit 1:05 (pertanyaan mahasiswa soal csv reader, lalu menulis CSV).

---

## Hari 3 – 23 Oktober 2026

Lanjut Lecture 6 dari menit 1:05 sampai **selesai** (1:32). Ngoding 2 jam, bahasa Inggris 10 menit. Lecture 6 tamat. 🎉

### Kuis Kosakata #2
- Lebih susah dari kemarin (ada soal kebalikan Indonesia → Inggris, kata lama dicampur). Hasilnya **100%** lagi.

### Pemanasan
1. `sorted(students)` dengan list of dicts → **TypeError**, karena Python tidak tahu dict mau dibandingkan berdasarkan apa.
2. `key=get_name` tanpa kurung, karena yang memanggil `get_name` adalah `sorted` sendiri.
3. `Harry,"Number Four, Privet Drive"`: pakai `split(",")` jadi 3 potongan, pakai `csv.reader` jadi 2. Koreksi: komanya **2**, bukan 3. Dua kali potong menghasilkan tiga potongan. Dan `csv` itu **module**, `csv.reader` itu **function**-nya.
4. Baris CSV dengan 3 kolom dibongkar ke `name, home` → `ValueError: too many values to unpack`. `csv.reader` tidak menyelamatkan dari error ini, karena masalahnya jumlah kolom, bukan koma.

### Apa itu objek?
- Di Python **hampir semua hal adalah objek**: `5`, `"Harry"`, list, dict, file, function, bahkan module.
- Jadi pertanyaan yang berguna bukan "ini objek atau bukan?", tapi **"objek jenis apa, dan bisa apa?"**
- Objek = barang yang punya **data** + **kemampuan (method)**. Jenisnya (*type*) menentukan dia bisa apa. Cek pakai `type()`.
- Pola titik: `sesuatu.kemampuan()` → `sesuatu` objeknya, `kemampuan` method-nya. Contoh `file.write()`, `students.append()`.
- Koreksi dari Claude: bedanya `file` dan isi file bukan "objek vs bukan objek". `file` itu **file object**, isi yang dibaca (`line`) itu **str object**. Jenisnya saja yang beda.
- Jenis objek **tidak terbatas**: ada bawaan Python (`str`, `int`, `list`, `dict`, file object...), dari library (reader object, response object dari `requests`), dan buatan sendiri (Week 8).

### Variabel vs objek
- **Objek** = orangnya. **Variabel** = nama panggilan yang ditempelkan ke orang itu. Seperti santri bernama Ahmad yang dipanggil "Mad".
- `writer = csv.writer(file)` → `writer` itu **variabel** yang menunjuk ke **writer object**. Namanya boleh diganti (`juru_tulis`), objeknya tetap sama.

### Analogi kantor TU: module, function, objek, method
| Di pesantren | Di Python | Contoh |
|---|---|---|
| Kantor TU | module / library | `csv` |
| Loket-loket | function | `reader`, `writer`, `DictReader`, `DictWriter` |
| Petugas yang diberikan loket | objek | writer object |
| Keahlian petugas | method | `writerow`, `writerows` |

- Library menyediakan loket dan "SOP" petugas (namanya **class**, Week 8). **Petugasnya baru dibuat** saat kode `csv.writer(file)` dijalankan.
- `csv.writerow(...)` langsung → **error**, karena keahlian itu milik petugas, bukan kantornya.
- Tidak semua function menyerahkan petugas. `print`, `len`, `random.randint` langsung bekerja. Yang menyerahkan objek biasanya untuk pekerjaan berkelanjutan: `open`, `csv.reader`, `csv.writer`, `Image.open`.
- Polanya: **panggil function → dapat objek → pakai method-nya.**

### Membaca dan menulis file sekaligus?
- Mahasiswa bertanya: bisakah file dibaca dan diubah sekaligus? Jawab David: **bisa**, tapi file dibayangkan seperti **kaset**: berurutan (*sequential*), harus diputar (*unwind*) ke posisi tertentu. Tidak ada *random access*.
- Lebih ribet (*more involved*), tapi bisa (*doable*). Sarannya: **baca dulu semua, ubah di program, lalu tulis ulang**. Kecuali filenya sangat besar (*massive*).
- Contoh mengganti "Ron" jadi "Ronald": baca dengan `readlines()`, lalu buka dengan `"w"` dan tulis ulang sambil `name = name.replace("Ron", "Ronald")`.
- Penting: `replace` **tidak mengubah** string aslinya, dia mengembalikan string baru. Jadi harus ditangkap: `name = ...`. Tanpa `if` juga tidak apa-apa.
- Jebakan `replace`: dia mencocokkan **huruf**, bukan kata. Saya sempat salah tebak:
  - Dijalankan dua kali: `Ron` → `Ronald` → `Ronaldald`.
  - `Veronica` aman, tapi **karena huruf besar-kecil** (`ron` ≠ `Ron`), bukan karena Python paham nama. `Ronny` jadi `Ronaldny`.
- Urutan penting: baca dulu sampai file tertutup, **baru** buka dengan `"w"`. Hati-hati, `"w"` langsung mengosongkan file.
- Baru kenal **list comprehension** `[... for name in names]`: cara singkat membuat list. Pakai `for` biasa juga boleh.

### `csv.DictReader` dan header
- `for name, home in reader:` hanya benar kalau urutan kolomnya pasti. Kalau kolom ditukar, salah tanpa error.
- **DictReader**: setiap `row` jadi **dictionary**, ambil pakai `row["name"]`, `row["home"]`.
- Dari mana key-nya? Dari **baris pertama file** (header). Saya sempat mengira dari huruf kolom Excel (A, B, C). Ternyata yang dimaksud judul kolom seperti di rekap nilai tahfidz: Nama Santri | Kelas | Juz | Nilai.

```
name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```

- Kode jadi lebih **robust** (tahan banting), seperti hafalan yang mutqin: tetap benar walaupun urutan kolomnya diacak.
- Pertanyaan mahasiswa: kenapa membuat dict baru `{"name": row["name"], ...}`, padahal `row` sudah dict? Bisa langsung `students.append(row)`. David: *"Oh, very clever."*
- Baris kosong di antara data: `split` sendiri → `not enough values to unpack`. `csv.reader` juga error. **DictReader melewati baris kosong** otomatis.
- Pemisah tidak harus koma: bisa tab (TSV) atau `;` dengan `delimiter=`.

### Menulis CSV: `csv.writer` dan `csv.DictWriter`
- Pakai mode `"a"` supaya header tidak terhapus.
- `csv.writer(file)` → writer object → `writer.writerow([name, home])`. Harus **list**, karena list punya urutan. Koma, tanda kutip, dan pindah baris diurus otomatis (alamat Harry otomatis diberi kutip).
- `csv.writer` **tidak tahu ada header**. Kalau saya menulis `[home, name]`, tetap ditulis dan datanya tertukar tanpa error. *"The onus is on us"*: tanggung jawab urutan ada di kita.
- `csv.DictWriter(file, fieldnames=["name", "home"])` → `writer.writerow({"name": name, "home": home})`. **`fieldnames`** = contekan urutan kolom. Urutan di dict boleh sembarang.
- DictWriter juga tidak membaca header dari file. Dia tahu urutan dari `fieldnames` yang saya tulis.

| | Tahu urutan kolom dari mana? |
|---|---|
| `csv.writer` | urutan list (tanggung jawab saya) |
| `csv.DictWriter` | `fieldnames` |
| `csv.DictReader` | baris pertama file (header) |

- Method lain: `writerows` (banyak baris sekaligus), dan khusus DictWriter `writeheader` (menulis header).

### Praktik di VS Code (Windows)
- Saya coba versi A (`csv.writer`) dan B (`csv.DictWriter`) sendiri. Dua masalah yang ketemu:
  1. **Data menempel di baris header** → di file tidak ada Enter setelah `name,home`. Mode `"a"` menulis tepat di ujung file. Solusi: tekan Enter setelah header, simpan.
  2. **Ada baris kosong di antara data** → masalah khas Windows, pindah barisnya dobel. Solusi: `open("students.csv", "a", newline="")`. David tidak mengalaminya karena codespace CS50 pakai Linux.
- Jangan biarkan file CSV terbuka dan belum tersimpan di tab saat program menulis ke file itu.
- Extension **Continue** mengambil alih `Ctrl+L`. Shortcut yang perlu diingat:

| Shortcut | Fungsi |
|---|---|
| `Ctrl+Shift+E` | munculkan daftar file |
| `Ctrl+P` | buka file dengan mengetik namanya |
| `` Ctrl+` `` | buka/tutup terminal |
| `Ctrl+K` lalu `Ctrl+S` | pengaturan keyboard shortcut |

### Gambar dengan PIL
- Binary file = isinya 0 dan 1 untuk gambar, suara, video. Kalau dibuka di VS Code, isinya simbol aneh.
- **Animated GIF** = beberapa gambar diam yang ditampilkan bergantian, seperti **flipbook**.
- Kucing oranye itu maskot **Scratch**, bahasa pemrograman dari MIT yang pakai balok-balok.
- `Image.open(arg)` beda dengan `open` biasa: milik PIL, untuk gambar, hasilnya image object.
- Saya menebak sendiri sebelum David: `sys.argv` berisi 3 item (nama program + 2 file), jadi harus pakai slice **`sys.argv[1:]`**. Kalau tidak, `Image.open("costumes.py")` error.

```python
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
```

- `save_all=True` = simpan semua frame, bukan satu gambar. `append_images` = gambar yang ditempel setelah yang pertama. `duration=200` = 0,2 detik per frame. `loop=0` = berulang selamanya (angka lain = terbatas).
- `[images[1]]` dua kurung siku: dalam = **indeks** (ambil kucing2), luar = **membungkus jadi list**. Saya sempat mengira `images[9]` berarti "sampai gambar ke-10". Salah, indeks itu **satu posisi**. Untuk banyak gambar pakai **`images[1:]`** (sudah list, tidak perlu dibungkus lagi).
- Isi di dalam `save(...)` itu **argument**: `"costumes.gif"` positional, `save_all=True` dan lainnya keyword argument. Ditulis 3 baris karena terlalu panjang, boleh selama masih di dalam kurung.
- Library-nya bernama **Pillow** (`pip install pillow`), tapi import-nya `from PIL import Image`.
- Penutup David: dengan **primitives** (alat dasar) membaca dan menulis file, kita bisa mengolah teks, CSV, sampai gambar. Seperti 28 huruf hijaiyah yang menyusun seluruh mushaf.

### Kosakata
| Kata | Arti |
|---|---|
| to hand | sudah tersedia |
| readable / writable | bisa dibaca / bisa ditulis |
| as you go along | sambil jalan |
| the short answer is | jawaban singkatnya |
| mental model | cara membayangkan sesuatu di kepala |
| sequential | berurutan |
| whereby | yang dengannya (formal) |
| unwind | mengurai gulungan (juga: bersantai) |
| scrubber | penggeser posisi video |
| random access | akses acak, bisa langsung loncat |
| keep track of | terus mencatat/mengikuti |
| involved (kata sifat) | rumit, ribet |
| doable | bisa dikerjakan |
| piecemeal | sedikit-sedikit |
| massive | sangat besar |
| expensive (time-wise) | berat (dari segi waktu) |
| seek | memindahkan posisi baca file |
| segue | peralihan ke topik berikutnya (dibaca *SEG-wei*) |
| accordingly | sesuai dengan itu |
| rely on | bergantung pada |
| robust | kokoh, tahan banting |
| hints / as to | petunjuk / tentang |
| behave | berperilaku, berjalan |
| take a peek | mengintip, melihat sekilas |
| so as to / anticipate | supaya / bersiap untuk |
| break down | gagal, tidak berlaku lagi |
| sole argument | satu-satunya argumen |
| fieldnames | nama-nama kolom |
| subsequently | setelah itu |
| onus | tanggung jawab, beban |
| whereas | sedangkan |
| so long as | asalkan |
| in so far as | sejauh, karena |
| best practices | cara terbaik yang disepakati |
| double check | memeriksa ulang |
| tend to | cenderung |
| resort to | terpaksa memakai |
| otherwise known as | yang juga dikenal sebagai |
| binary | biner, hanya 0 dan 1 |
| it turns out | ternyata |
| and the like | dan sejenisnya |
| illusion / fill in the gaps | ilusi / mengisi celah |
| frame | satu gambar dalam animasi |
| static | diam |
| to someone's point | seperti kata seseorang |
| cross my fingers | semoga berhasil 🤞 |
| scratched the surface | baru belajar sedikit |
| primitives | alat-alat dasar |
| be it ... or ... | baik ... maupun ... |
| dive in deeper | mempelajari lebih jauh |

### Yang mau dicoba
- Kuis Kosakata #3 besok.
- Coba `type(open("coba.txt", "w"))` dan `type(print)`.
- Coba di terminal: `"Ronald".replace("Ron", "Ronald")`, `"Ronny".replace(...)`, `"Veronica".replace(...)`.
- Buat CSV dengan satu baris kosong, bandingkan `csv.reader` dan `csv.DictReader`.
- Coba `writeheader()` di DictWriter untuk file yang masih kosong.
- (Opsional) Hapus shortcut `Ctrl+L` milik Continue.
- Mulai **Problem Set 6**.
