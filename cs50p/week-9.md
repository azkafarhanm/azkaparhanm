# CS50P Week 9: Et Cetera

## Hari 1 – 21 November 2026

Mulai Lecture 9, sampai sekitar **menit 16** (selesai `set` dan `global`, sebelum konstanta). Pagi: Kuis Harian #22 dan pemanasan murojaah soal Shirtificate. Ngoding 1 jam, bahasa Inggris 10 menit.

Lecture terakhir CS50P. Isinya kumpulan hal kecil yang tidak masuk tema minggu mana pun, makanya judulnya Et Cetera. Tidak ada problem setnya, jadi saya dan Claude sepakat: nonton 10-15 menit, lalu langsung soal kecil yang menuntut menebak hasil dulu sebelum dijalankan.

### Kuis Harian #22

15 soal, giliran Hari ke-2: Week 1 dan Week 5. Hasilnya **12/15**.

Yang salah:

| No | Materi | Koreksinya |
|---|---|---|
| 9 | if terpisah vs elif | Angka 20 dengan dua if terpisah menghasilkan dua baris, **tanpa error**. Saya kira ada error. Justru itu bahayanya |
| 10 | match vs if | Yang tidak bisa dilakukan match itu perbandingan `>` dan `<`. `case > 0` itu SyntaxError, bahkan sebelum program jalan |
| 12 | diam artinya lulus | `if square(2) != 4: print(...)` tidak mencetak apa-apa kalau square benar |

Nomor 12 tambahan dari Claude yang baru saya sadari: `return n + n` tetap lolos untuk angka 2, karena 2+2 juga 4. Yang membongkarnya angka 3, karena 3+3 = 6 sedangkan seharusnya 9. Itu sebabnya tes di lecture isinya lima assert, bukan satu. **Satu angka bisa kebetulan benar.**

Soal nomor 6 kuis kemarin (`align` tertukar dengan `set_y`) diulang dalam bentuk kebalikan, dan kali ini benar.

### Pemanasan murojaah

Lima pertanyaan soal Shirtificate, dijawab dari ingatan tanpa buka catatan. Empat benar. Yang keliru satu:

Saya bilang `help` itu "untuk tahu gunanya apa". **Salah.** `help` itu untuk melihat **parameternya**. Pembagiannya:

```
dir(objek)    ->  NAMANYA        (set_y, set_font, cell, ...)
help(nama)    ->  PARAMETERNYA   (set_y(y) butuh angka apa)
dokumentasi   ->  CELAH & JEBAKANNYA
```

Koreksi kecil lain: tinggi cell pertama saya itu **210 mm**, tepat setinggi halaman A4. Bukan "200 lebih kira-kira", memang pas sepanjang halaman, makanya pena jatuh ke dasar.

---

## set

Wadah yang **tidak mau isi kembar**. Tipe data bawaan Python, sejajar dengan yang lain, cuma belum pernah saya pakai sampai sekarang.

| Wadah | Kurung | Urut? | Boleh kembar? |
|---|---|---|---|
| list | siku | ya | ya |
| tuple | biasa | ya | ya |
| dict | kurawal | - | kuncinya tidak |
| set | kurawal | **tidak** | **tidak** |

Percobaan saya:

```python
print(set([1, 2, 2, 3, 3, 3]))   # {1, 2, 3}
print(set("banana"))             # 3 huruf: b, a, n
```

Dari enam huruf banana jadi tiga. Yang kembar hilang **sendiri**, tanpa disuruh.

### Kurung kurawal dipakai berdua

Ini yang saya tanyakan: bukannya `{ }` itu punya dictionary? Ternyata dipakai berdua, dan Python menentukannya dari **isinya**:

```
ada tanda :  di dalam   ->  dict
tidak ada            ->  set
```

Jebakannya di yang kosong:

```python
print(type({}))        # dict, bukan set
print(type(set()))     # set
```

Kurawal kosong sudah diklaim duluan oleh dict. Jadi set kosong harus ditulis `set()`.

### Tidak bisa ditunjuk, tapi bisa dilewati

```python
s = {"ali", "umar", "budi"}
print(s[0])    # TypeError: 'set' object is not subscriptable
```

**subscript** itu istilah untuk `[0]`, penunjuk posisi. Set tidak punya posisi sama sekali, jadi tidak ada yang bisa ditunjuk.

Tapi for loop tetap jalan:

```python
for nama in s:
    print(nama)
```

Ini dua kemampuan berbeda yang saya kira satu:

| Istilah | Artinya | Set |
|---|---|---|
| iterable | bisa dilewati satu per satu pakai for | BISA |
| subscriptable | bisa ditunjuk posisinya pakai `[0]` | TIDAK |

Beda dengan error yang saya kenal di Jar, `'int' object is not callable`. Yang itu urusan kurung biasa, yang ini urusan kurung siku.

### Urutannya tidak dijamin

Karena tidak urut, hasil for loop bisa berbeda tiap kali dijalankan. Kalau butuh urut pakai `sorted`, tapi hasilnya **bukan set lagi**, melainkan list baru:

```python
s = {"umar", "ali", "budi"}
hasil = sorted(s)
print(type(hasil))   # list
print(s)             # set aslinya tidak berubah
```

Ini kebalikan dari jebakan shuffle di Making Faces:

```
sorted(s)            menyerahkan hasil baru   ->  harus DIPAKAI
s.sort()             mengubah di tempat       ->  mengembalikan None
random.shuffle(x)    mengubah di tempat       ->  mengembalikan None
```

Catatan dari Claude yang menajamkan: hasil `sorted` tidak harus masuk variabel, yang penting **dipakai**. Boleh langsung `print(sorted(s))` atau `for nama in sorted(s)`. Yang salah itu kalau hasilnya dibuang: `sorted(s)` sendirian jalan, tidak error, tapi tidak terjadi apa-apa. Salah tanpa error lagi.

Dan `.sort()` itu milik list saja. Set tidak punya, karena tidak ada urutan untuk diurutkan.

### Identik itu sama persis, bukan mirip

Ini yang paling bikin saya berputar. Saya terus bilang "mirip", padahal **di Python tidak ada mirip, cuma sama atau beda.** Patokannya hasil `==`.

```python
print(set(["Ali", "ali", "ALI"]))   # tiga-tiganya bertahan
print(set([1, 1.0, True]))          # jadi satu
```

Yang kedua mengagetkan. Sebabnya:

```python
print(1 == 1.0)     # True
print(1 == True)    # True
print("Ali" == "ali")  # False
```

`True` itu sebenarnya angka 1 di balik layar (`int(True)` = 1, `True + True` = 2). Jadi `1`, `1.0`, dan `True` dianggap satu barang yang sama.

Yang bertahan adalah **yang masuk duluan**:

```python
print(set([1, 1.0, True]))   # {1}
print(set([True, 1.0, 1]))   # {True}
```

Koreksi penting dari Claude: yang kembar **tidak pernah masuk** ke dalam set sejak awal, bukan "tercetak lalu disembunyikan". Saya kira hilangnya waktu di-print. Buktinya tanpa print sama sekali:

```python
s = set()
s.add(1)      # len 1
s.add(1.0)    # len 1
s.add(True)   # len 1
```

Ditambah tiga kali, isinya tetap satu. Dan `.add` tidak error, cuma diabaikan diam-diam.

### Method set

```
list   .append(x)      menambah di ujung, urutannya penting
set    .add(x)         menambah, tidak ada ujung
dict   d[kunci] = x    tidak pakai method
```

Namanya beda bukan asal beda. `append` artinya melampirkan di belakang, dan itu cuma masuk akal kalau ada belakangnya. Set tidak punya belakang, jadi namanya cuma `add`.

### Pertanyaan mahasiswa: kalau nama asramanya salah ketik?

Mahasiswa bertanya: kalau `Slytherin` jadi `Slytheron`, huruf I jadi O, apakah set menganggapnya sama? Dan apakah Python memeriksa huruf per huruf?

Jawab David: `It would compare the strings` — yang dibandingkan **seluruh string sekaligus**. Beda satu huruf saja, itu dua string berbeda, dan set menyimpan dua-duanya.

```python
print(set(["Slytherin", "Slytheron", "slytherin"]))   # tiga-tiganya
print("Slytherin" == "Slytheron")          # False
print("Slytherin"[0] == "Slytheron"[0])    # True, dua-duanya S
```

Tebakan saya salah di baris kedua, saya kira True.

Pelajarannya: **set tidak membersihkan data kotor.** Dia cuma membuang yang identik. Kalau datanya ada salah ketik, hasilnya tetap kelihatan rapi dan tidak error, tapi salah. Tema salah tanpa error lagi.

Manfaat praktisnya, membuang data kembar jadi satu baris:

```python
nama = ["ali", "umar", "ali", "budi", "umar"]
print(len(nama))        # 5
print(len(set(nama)))   # 3
```

Tanpa loop, tanpa if.

---

## global

Lokal dan global itu soal **di mana variabelnya dibuat**:

```
lokal    dibuat DI DALAM function   ->  hidup selama function jalan, lalu hilang
global   dibuat DI LUAR function    ->  hidup selama program jalan
```

Yang mengejutkan: variabel global **tidak segampang itu diubah dari dalam function.**

### Percobaan 1 dan 2

```python
saldo = 100

def lihat():
    print(saldo)     # jalan, keluar 100
```

```python
saldo = 100

def tambah():
    saldo = saldo + 50    # UnboundLocalError
```

Saya menebak percobaan kedua error, dan itu benar. Tapi **letak errornya saya tebak salah.** Saya kira errornya di `print(saldo)` yang di luar. Ternyata errornya **di dalam function**, di baris `saldo = saldo + 50` itu sendiri.

Sebabnya: Python melihat ada `saldo = ...` di dalam function, lalu memutuskan **"berarti saldo ini lokal"**, dan keputusan itu berlaku untuk seluruh isi function termasuk baris yang sama. Jadi yang dibaca di sebelah kanan `=` itu saldo lokal yang **belum ada isinya**.

Jadi yang bikin error bukan "mengakses variabel luar", tapi **tanda `=` itu sendiri**:

```
ada  =  di function   ->  seluruh nama itu jadi lokal, yang luar tertutup
tidak ada  =          ->  Python mencari ke luar, dapat yang global
```

Koreksi penting: Python **tidak melokalkan variabel global**. Yang global tetap utuh. Yang terjadi, dibuat variabel **baru yang terpisah** yang kebetulan namanya sama. Dua kotak berbeda dengan nama sama:

```python
saldo = 100

def tambah():
    saldo = 50
    print(saldo)   # 50, kotak di dalam

tambah()
print(saldo)       # 100, kotak di luar, tidak tersentuh
```

### main bukan function istimewa

Di `bank.py` David, `balance = 0` ada di dalam `main`. Jadi `balance` itu bukan global sama sekali, dia lokal milik `main`, dan `deposit` tidak bisa melihatnya.

```
main      punya kotaknya sendiri
deposit   punya kotaknya sendiri
withdraw  punya kotaknya sendiri
```

Tidak ada yang bisa mengintip kotak tetangganya. Yang bisa dilihat semua function cuma yang ada **di luar semua function**, di tingkat file.

Percobaan saya:

```python
def main():
    x = 5
    lihat()

def lihat():
    print(x)       # NameError

main()
```

### Dua error yang beda, dan cara membedakannya

| Error | Artinya | Pemicunya |
|---|---|---|
| NameError | namanya tidak ada sama sekali di mana pun | `print(x)`, tidak ada `=`, dicari ke luar tidak ketemu |
| UnboundLocalError | namanya ADA sebagai lokal, tapi belum diisi | `x = x + 1`, ada `=`, dipastikan lokal, masih kosong |

Jadi dari pesan errornya saja sudah bisa ketahuan mana yang salah. Pembedanya tetap tanda `=`.

### Keyword global

```python
def deposit(n):
    global balance     # baris sendiri, bukan ditempel
    balance += n
```

`global balance` itu **bukan assignment**, tidak ada `=` dan tidak ada nilai yang diberikan. Dia cuma pengumuman di awal function: nama ini maksudnya yang di luar, jangan bikin kotak baru.

```
tanpa global   ->  boleh baca, TIDAK boleh ubah
pakai global   ->  boleh baca DAN boleh ubah
```

Dua syarat harus terpenuhi bersamaan: variabelnya ada di tingkat file, dan `global` ditulis di function yang mau mengubahnya. Kalau variabelnya masih di dalam `main`, `global` pun tidak menolong.

Bukti satu baris bedanya:

```python
balance = 0
def deposit(n):
    balance = n
deposit(100)
print(balance)     # 0, tidak berubah, TIDAK ERROR
```

```python
balance = 0
def deposit(n):
    global balance
    balance = n
deposit(100)
print(balance)     # 100
```

Yang pertama itu jebakan paling halus: tidak error sama sekali, cuma diam-diam tidak terjadi apa-apa.

### Kejanggalan yang saya rasakan sendiri

Waktu melihat `bank.py` yang sudah jalan, saya merasa ada yang aneh: **tidak ada `return` sama sekali**, tapi `main` tetap melihat saldonya berubah.

Ternyata memang begitu. `main` bukan menerima apa-apa dari `deposit`. `main` membaca **kotak yang sama** yang barusan diubah `deposit`. Tidak ada yang dioper.

```
lewat return      deposit menyerahkan hasil   ->  main menampungnya
lewat global      deposit mengubah diam-diam  ->  main tidak tahu apa-apa
```

Dan kata Claude, kejanggalan yang saya rasakan itu **persis alasan global dihindari**. Lihat baris pemanggilnya:

```python
deposit(100)                        # tidak ada tanda saldo berubah
balance = deposit(balance, 100)     # tandanya ada di baris itu juga
```

Baris pertama tidak memberi tahu apa pun. Siapa pun yang membaca `main` harus membuka `deposit` dulu untuk tahu bahwa saldonya diubah. Kalau ada 20 function yang boleh menyentuh `balance`, begitu saldonya salah, harus diperiksa dua puluh-duanya untuk tahu siapa pelakunya.

Versi tanpa global, hasilnya sama persis (0 lalu 50), yang beda cuma **apakah perubahannya kelihatan dari luar**:

```python
def main():
    balance = 0
    balance = deposit(balance, 100)
    balance = withdraw(balance, 50)
    print("Balance:", balance)

def deposit(balance, n):
    return balance + n

def withdraw(balance, n):
    return balance - n
```

Ini tema semantics lagi, sama seperti `jar.capacity` lawan `jar._capacity`: kode yang jalan itu gampang, kode yang jujur mengatakan apa yang dia lakukan itu yang susah.

### Alasan kedua: susah dites

Ini yang paling kena buat saya, karena sudah dua kali kejeduk.

```python
balance = 0

def deposit(n):
    global balance
    balance += n

def test_satu():
    deposit(100)
    assert balance == 100

def test_dua():
    deposit(50)
    assert balance == 50     # GAGAL
```

Awalnya saya tidak paham contoh ini sama sekali. Baru masuk setelah dijalankan polos tanpa pytest dan tanpa assert, cuma print:

```
awal        : 0
setelah 100 : 100
setelah 50  : 150
```

Setoran kedua **tidak mulai dari 0**. Dia mulai dari 100, sisa setoran pertama. Itu maksudnya "meninggalkan balance di angka 100".

Lalu dibungkus jadi function, angkanya sama saja:

```
di test_satu, balance = 100
di test_dua , balance = 150
```

Padahal di `test_dua` saya baru menyetor 50, jadi yang saya harapkan 50. Dan kalau `test_satu()` dihapus, `test_dua` tiba-tiba benar: `balance = 50`. **Function yang sama, angka yang beda, cuma karena ada tetangganya yang jalan duluan.**

Di situlah letak tidak deterministiknya: hasil tes bergantung pada tes mana yang jalan duluan.

Yang penting dicatat: "menyesuaikan harapan jadi 150" itu **bukan obatnya, itu jebakannya**. Tesnya hijau hari ini, tapi begitu `test_satu` dihapus atau urutannya berubah, merah lagi padahal kodenya tidak disentuh. Itu persis catatan Week 6 saya: tes yang lolos hari ini tapi gagal besok.

Versi parameter tidak bisa kena ini, karena tiap tes membawa angkanya sendiri:

```python
def deposit(balance, n):
    return balance + n

def test_satu():
    assert deposit(0, 100) == 100

def test_dua():
    assert deposit(0, 50) == 50
```

Sekarang penyakit yang sama sudah ketemu tiga kali:

| Kasus | Bergantung pada apa |
|---|---|
| Seasons | tanggal hari ini |
| Cookie Jar | tes sebelahnya |
| global | sisa function sebelumnya |

Tiga wujud, satu obat: **kirim lewat parameter, jangan mengandalkan apa pun di luar.**

Kesimpulannya: `global` itu bisa, tapi hampir selalu ada cara yang lebih baik, dan caranya sudah saya kuasai sejak Week 2.

---

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| tidbits | potongan kecil yang menarik, serpihan informasi |
| touch on | menyinggung sedikit, menyebut sambil lalu |
| overarching | yang memayungi semuanya, tema besar |
| whet your appetite | membangkitkan selera, bikin penasaran ingin lebih. whet = mengasah, beda dengan wet (basah) |
| glean | memungut sedikit demi sedikit, menyimpulkan dari petunjuk yang berserakan |
| albeit | meskipun, walaupun. Dibaca ol-BI-it |
| exhaustive | lengkap sampai tuntas, tidak ada yang terlewat |
| whip up | bikin cepat-cepat, dadakan |
| leverage | memanfaatkan yang sudah ada untuk hasil lebih besar. Arti asli: daya ungkit |
| dig into | mendalami, membongkar sampai ke dalamnya |
| per the documentation | menurut dokumentasinya. per = menurut, bukan per hitungan |
| subscript | penunjuk posisi, tanda `[0]` |
| iterable | bisa dilewati satu per satu pakai for |
| notasi | cara menuliskannya, tandanya. Misalnya `:` dan `->` pada type hints |

Satu jebakan kata: David bilang "a set of students", padahal di kodenya `students` itu **list**. Di situ "set" dipakai dalam arti Inggris biasa, sekumpulan, bukan tipe data Python. Kalau bingung, lihat kodenya, bukan ucapannya.

---

## Yang mau dicoba

- Lanjut Lecture 9 dari menit 16, materi berikutnya konstanta.
- Jalankan ulang percobaan `set` dan `global` besok pagi dari ingatan, tanpa membuka catatan ini.

---

## Hari 2 – 22 November 2026

Hari Minggu dan banyak kerjaan, jadi **lecture tidak dilanjut sama sekali**. Masih berhenti di menit 16. Yang jalan hari ini: Murojaah 10 (dicatat terpisah di `murojaah.md`), pemanasan, dan Kuis Harian #23.

### Pemanasan murojaah: set dan global

Lima pertanyaan dari materi kemarin, dijawab dari ingatan tanpa buka catatan. **Dua benar, tiga meleset.**

| No | Yang ditanya | Hasil |
|---|---|---|
| 1 | Kenapa `s[0]` error tapi `for` jalan | Salah. Saya malah menjawab soal nomor 2, bicara soal membandingkan |
| 2 | Kenapa `{1, 1.0, True}` jadi satu | Benar, patokannya hasil `==` |
| 3 | Sebab `UnboundLocalError` dan letaknya | Lupa total |
| 4 | Beda `NameError` dan `UnboundLocalError` | Separuh. NameError benar, yang satunya belum kena intinya |
| 5 | Dua alasan `global` dihindari | Satu dari dua. Yang susah dilacak benar, yang susah dites lupa |

Koreksi nomor 1: set **tidak menyimpan urutan**, jadi tidak ada "yang ke-0" untuk ditunjuk. Tapi untuk melewati semuanya satu per satu tidak perlu tahu siapa duluan, makanya `for` tetap jalan. Dua kemampuan yang berbeda:

```
iterable        bisa dilewati satu per satu pakai for    set: BISA
subscriptable   bisa ditunjuk posisinya pakai [0]        set: TIDAK
```

Koreksi nomor 3 dan 4, dan ini yang paling perlu diulang: yang bikin error itu **tanda sama dengannya sendiri**, bukan "mengakses variabel luar". Begitu ada `=`, Python memutuskan nama itu lokal untuk seluruh isi function, jadi yang dibaca di sebelah kanan itu kotak lokal yang masih kosong. Patokan menebak errornya:

```
ada  =  di function    ->  UnboundLocalError (namanya ADA sebagai lokal, belum diisi)
tidak ada  =           ->  NameError (namanya tidak ada di mana pun)
```

Koreksi nomor 5: alasan kedua **susah dites**, dan itu percobaan yang kemarin saya jalankan sampai tiga tahap. `test_dua` keluar 150 padahal menyetor 50, lalu tiba-tiba benar begitu `test_satu` dihapus.

Dua kata saya yang diperbaiki:

- "per huruf dibandingkan" — bukan. Python membandingkan string **utuh**, hasilnya satu True atau False. Ini jawaban David ke mahasiswa kemarin, *it would compare the strings*. Kalau saya yang memaksa per huruf hasilnya bisa menyesatkan: `"Slytherin" == "Slytheron"` False, tapi `"Slytherin"[0] == "Slytheron"[0]` True.
- "membandingkan variabel saldo" di nomor 3 — bukan membandingkan tapi **membaca**. Tidak ada perbandingan di `saldo + 50`, yang gagal itu pengambilan nilainya.

### Kuis Harian #23

17 soal, lebih banyak dari biasa karena antrean ulangannya menumpuk: tiga dari kuis #22, tiga dari pemanasan tadi, dan dua dari murojaah pagi. Giliran Hari ke-3: Week 2 dan Week 6.

Hasilnya **15/17**, dan yang salah dua-duanya kosakata — **konsepnya bersih semua**, termasuk enam soal ulangan yang kemarin lepas.

| No | Kata | Koreksinya |
|---|---|---|
| 2 | whet your appetite | Soal kebalikan. whet = mengasah (selera), whip up = mengocok, bikin cepat-cepat. Sama-sama diawali wh dan sama-sama dari dapur, makanya tertukar |
| 4 | exhaustive | Lengkap sampai tuntas, bukan melelahkan. Akarnya memang sama dengan exhausted (exhaust = menguras habis), tapi arahnya beda: exhausted itu ORANGNYA yang terkuras, exhaustive itu BAHASANNYA yang dikuras habis |

Yang nempel setelah diulang: `if` terpisah lawan `elif`, `match` yang tidak bisa `>` dan `<`, "diam artinya lulus" termasuk jebakan `n + n` yang lolos di angka 2, iterable lawan subscriptable, sebab `UnboundLocalError`, `isupper()` lawan `upper()`, dan koma yang membuat tuple.

### Yang mau dicoba

- Lanjut Lecture 9 dari **menit 16**, materi berikutnya konstanta.

---

## Hari 3 – 23 November 2026

Lanjut Lecture 9 dari menit 16 sampai sekitar **menit 26**. Selesai bagian `global` dan masuk **konstanta**. Pagi: Kuis Harian #24 dan pemanasan dari Murojaah 10.

### Kuis Harian #24

17 soal, giliran Hari ke-4: Week 3 dan Week 0, plus ulangan dari #22, #23, dan pemanasan kemarin. Hasilnya **15/17**.

Yang salah **dua-duanya ulangan dari kemarin**, jadi salah dua kali berturut-turut: `whet your appetite` dan `exhaustive`. Semua soal konsep benar, termasuk enam soal ulangan.

Karena penjelasan arti saja jelas tidak cukup, patokannya diganti jadi yang mekanis:

```
exhausted    akhiran -ed   kena pada ORANGNYA   -> saya kelelahan
exhaustive   akhiran -ive  sifat BENDANYA       -> daftarnya lengkap
```

Pola yang sama dengan `bored` (saya bosan) lawan `boring` (filmnya membosankan). Pertanyaan pengujinya: **siapa yang terkuras?**

```
whet   ada h    mengasah   (whetstone = batu asah)
wet    tanpa h  basah
```

Jadi yang dibayangkan **pisau diasah**, bukan air.

### Pemanasan murojaah: File Extensions

Lima pertanyaan dari Murojaah 10, dijawab dari ingatan. **Lima-limanya benar**, termasuk nomor 5 yang paling panjang (perbandingan versi lama dan versi murojaah, lengkap sampai dua hal yang bisa diambil dari versi baru).

Dua tambahan kecil:

- `os.path.splitext("test.txt.pdf")` menghasilkan `('test.txt', '.pdf')` — ekstensinya **sudah termasuk titiknya**, beda dengan `split(".")[-1]` yang menghasilkan `pdf` tanpa titik.
- Untuk nomor 3, kalimat penguncinya: `file` tetap **string**, dan list hasil `split` langsung hilang karena tidak ada yang memegangnya. Sebabnya string itu immutable, jadi `split` tidak punya cara mengubahnya di tempat.

---

## Shadowing

Pertanyaan mahasiswa: kalau ada variabel global, lalu di dalam function ada variabel **bernama sama**, apa yang terjadi?

Jawab David: `the latter will shadow the former` — yang belakangan (di dalam function) **menutupi** yang duluan (yang global).

```
shadow        menutupi sampai yang di bawahnya tidak terlihat
the former    yang disebut duluan    -> global
the latter    yang disebut belakang  -> yang di dalam function
```

Ini persis percobaan yang saya jalankan sendiri kemarin:

```python
saldo = 100

def tambah():
    saldo = 50
    print(saldo)   # 50

tambah()
print(saldo)       # 100
```

Jadi istilah resmi dari yang kemarin saya sebut "kotak baru terpisah" itu **shadowing**, dan istilah ini dipakai di banyak bahasa lain juga. Yang global **tertutupi, bukan terhapus dan bukan berubah** — begitu keluar dari function, bayangannya hilang.

Yang perlu diwaspadai: shadowing **tidak error dan tidak ada peringatan**. Kalau saya sebenarnya bermaksud mengubah yang global tapi lupa menulis `global`, programnya jalan mulus dan diam-diam tidak terjadi apa-apa. Daftar "salah tanpa error" lagi.

Patokan David: `the rule of thumb is, just don't do that` — jangan memberi nama yang sama. Bukan karena salah, tapi karena nanti saya sendiri yang bingung membaca kode saya.

## global sebenarnya lokal terhadap FILE

Ini yang paling membuka hari ini. David bilang variabel global di Python itu `technically local` juga — lokal terhadap **filenya** (module), bukan terhadap seluruh program.

Percobaan dua file:

```python
# bank.py
balance = 100
```

```python
# utama.py
import bank
print(balance)      # NameError: name 'balance' is not defined
print(bank.balance) # 100, ini yang benar
```

Ini **aturan absen** yang saya rumuskan sendiri di Week 4: nama yang tepat sesudah `import` itulah satu-satunya yang masuk ke absen file saya. `import bank` cuma mendaftarkan nama `bank`, tidak membawa isinya.

Tingkatannya:

```
lokal terhadap function    hilang begitu function selesai
"global" (file/module)     terlihat semua function DI FILE ITU
benar-benar global         TIDAK ADA di Python
```

Jadi kata `global` itu agak menipu namanya. Yang lebih tepat: **module-level variable**.

### Titik bukan cuma untuk class

Pertanyaan saya: `bank.balance` itu kan bentuk pemanggilan class, kenapa variabel biasa juga begitu?

Ternyata titik artinya cuma satu: **ambil yang ada di dalamnya**. Yang di sebelah kiri bisa apa saja. Dan saya sudah memakainya untuk variabel sejak Week 4 tanpa sadar — `sys.argv` itu variabel (list), bukan method, makanya tanpa kurung.

| Bentuk | Isinya | Kurung |
|---|---|---|
| `random.choice()` | method milik module | pakai |
| `sys.argv` | variabel milik module | tanpa |
| `math.pi` | konstanta milik module | tanpa |
| `jar.deposit()` | method milik objek | pakai |
| `jar.size` | property milik objek | tanpa |

Aturan lama tetap berlaku: **kurung berarti dipanggil, tanpa kurung berarti diambil isinya.**

Yang baru saya tahu: yang di-import itu bukan cuma function. Satu file bisa berisi variabel, function, dan class sekaligus, dan ketiganya bisa diambil dari luar. `from datetime import date` itu contohnya — `date` itu **class**, makanya `date(1998)` bentuknya sama dengan `Student("Harry")`.

Koreksi kecil: "langsung dieksekusi" itu kurang tepat. Yang dieksekusi itu **filenya**, dan cuma **sekali**, saat `import` dijalankan. Setelah itu `bank.balance` cuma membaca. Ini yang saya buktikan 17 November waktu `python utama.py` mencetak dua baris.

## Kenapa global dihindari, versi David

Alasannya sama persis dengan yang saya simpulkan sendiri kemarin **sebelum menontonnya**:

- `things can get messy quickly` — cepat berantakan.
- `less obvious quickly exactly where your information is stored` — jadi tidak jelas lagi di mana datanya sebenarnya disimpan, sebagian di atas file, sebagian di dalam function.
- Patokannya: `use global variables sparingly`, pakai seperlunya saja.

Dan jalan keluar yang dia tunjukkan ternyata **class** — `self._balance` menggantikan variabel global. Bagian ini bukan materi baru buat saya, isinya persis Cookie Jar:

```python
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n
```

Yang baru cuma **konteksnya**: class dipakai untuk menggantikan global.

Alasan `_balance` juga diulang David dengan kalimat yang pas: `to indicate that it's private, even though that's not enforced by Python`, dan `just a visual clue to myself`. Itu yang saya catat 13 November dengan kalimat saya sendiri — **`_house` itu rambu, bukan gembok**.

Sempat ada momen menebak: di transkrip menit 19.43 tertulis `self.balance minus equals n` tanpa garis bawah. Tebakan saya kalau benar begitu errornya `AttributeError: property 'balance' has no setter`, karena penulisan ke nama property selalu lewat setter — persis yang saya tabrak di `__init__` Cookie Jar. Ternyata di kodenya tetap `self._balance`, jadi transkrip YouTube-nya yang salah dengar.

```
self._balance -= n    langsung ke gudang, AMAN
self.balance  -= n    lewat property, butuh setter, MELEDAK kalau tidak ada
```

## Konstanta

Konstanta = variabel yang **nilainya tidak dimaksudkan untuk diubah**.

```
variabel     isinya berubah-ubah selama program jalan
konstanta    ditetapkan sekali, tidak diubah
```

Di Python ditulis **HURUF BESAR SEMUA**, tapi Python **tidak memaksakannya**:

```python
JUZ = 30
JUZ = 31
print(JUZ)   # 31, tanpa peringatan apa pun
```

Jadi huruf besar itu rambu, bukan gembok — pola yang sama dengan `_balance`:

```
_balance    garis bawah  ->  "jangan disentuh dari luar"
JUZ         huruf besar  ->  "jangan diubah"
_           garis bawah  ->  "isinya tidak saya pakai"
```

Ketiganya `you're on the honor system`.

### Bandingkan dengan const di JavaScript

Saya pernah belajar JavaScript dan di sana `const` benar-benar tidak bisa diubah. Jadi bedanya:

```
JavaScript   const JUZ = 30; lalu JUZ = 31;   ->  TypeError, DITOLAK
Python       JUZ = 30        lalu JUZ = 31;   ->  jalan, tanpa peringatan
```

Tapi ada jebakan di `const` JavaScript yang bentuknya **persis temuan tuple saya 6 November**:

```javascript
const daftar = [1, 2, 3];
daftar = [4, 5, 6];      // DITOLAK
daftar.push(4);          // BOLEH
```

Yang dikunci itu **slot namanya**, bukan isi barangnya. Sama dengan list di dalam tuple yang tetap bisa diubah. Satu pola, dua bahasa.

### Kenapa konstanta dianggap bagus

`it allows you to program defensively` — menulis kode dengan berjaga-jaga, mengantisipasi kecerobohan sejak awal. Supaya kalau suatu saat saya atau orang lain tidak sengaja mengubah nilainya, ketahuan.

Dan praktiknya: angka yang dipakai di tengah kode dinaikkan ke atas file.

```python
MEOWS = 3

for _ in range(MEOWS):
    print("meow")
```

Istilahnya `bubble up` dan `surface it` — naik seperti gelembung, dimunculkan ke permukaan. Gambaran yang sama dengan **propagate** waktu error merambat naik mencari `except`.

Alasan David yang paling jujur: `clearer to colleagues, and frankly, me tomorrow after I've forgotten what I did today`. Alasan yang sama dengan kenapa catatan ini saya tulis.

Dan `_` pada `for _ in range(3)` itu nama variabel biasa, tapi kesepakatannya berarti "isinya tidak saya pakai". Rambu lagi.

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| shadow | menutupi sampai yang di bawahnya tidak terlihat |
| the former / the latter | yang disebut duluan / yang disebut belakangan |
| rule of thumb | patokan praktis dari pengalaman, bukan aturan baku |
| frowned upon | tidak disukai, dipandang kurang pantas (frown = mengerutkan dahi) |
| messy | berantakan, semrawut |
| sparingly | secukupnya saja, sehemat mungkin |
| enforced | dipaksakan, ditegakkan |
| clue | petunjuk |
| confines | batas, lingkup (`in the confines of this class`) |
| manipulate | mengotak-atik, mengubah nilainya. Bukan menipu |
| encapsulate | membungkus jadi satu kemasan sekaligus menyembunyikan isinya (dari capsule) |
| fine-grained | butirannya halus, kendali sampai ke detail kecil (grain = butir) |
| coarse-grained | butirannya kasar, kendali garis besar saja |
| tend to | cenderung |
| program defensively | menulis kode dengan berjaga-jaga |
| bubble up / surface it | naikkan ke atas, munculkan ke permukaan |

Catatan: `abstraction` dan `encapsulation` bedanya tipis dan sering dipakai bergantian. Patokan saya: **abstraction** fokus ke yang tidak perlu dilihat, **encapsulation** fokus ke yang dijadikan satu paket.

Dan satu keluarga kata pelunak yang dipakai David terus: `tend to`, `generally speaking`, `rule of thumb`, `to some extent`. Semuanya cara bilang "biasanya begini, tapi ada pengecualian". Berguna untuk komentar kode bahasa Inggris — jangan menulis lebih mutlak daripada yang diyakini.

## Yang mau dicoba

- Lanjut Lecture 9 dari **menit 26**. Materi berikutnya kemungkinan type hints dan docstring.

---

## Hari 4 – 24 November 2026

Lanjut Lecture 9 dari menit 26 sampai sekitar **menit 37**. Selesai konstanta, masuk **class variable**, lalu **type hints** dan **mypy**. Pagi: Kuis Harian #25 dan pemanasan.

### Kuis Harian #25

16 soal, giliran Hari ke-5: Week 4 dan Week 1. Hasilnya **14/16**.

Kabar bagusnya: `whet your appetite` dan `exhaustive` yang dua kali berturut-turut salah **akhirnya nempel**. Patokan mekanis yang dipakai:

```
-ed   kena pada ORANGNYA      exhausted  -> saya kelelahan
-ive  sifat BENDANYA          exhaustive -> daftarnya lengkap
whet  ada h, dari whetstone (batu asah)  -> mengasah
wet   tanpa h                            -> basah
```

Yang salah dua, dan dua-duanya konsep:

| No | Materi | Koreksinya |
|---|---|---|
| 9 | randint inclusive | Saya SUDAH tahu ujung belakangnya ikut, yang saya kira tidak ikut malah ujung DEPANnya |
| 12 | Pythonic is_even | Yang benar `return n % 2 == 0` saja |

Untuk nomor 9 koreksinya jadi lebih tajam dari yang saya kira:

```
randint(1, 5)   DUA ujungnya ikut: 1 sampai 5
range(1, 5)     awalnya ikut, akhirnya TIDAK: 1, 2, 3, 4
```

Jadi yang pernah dibuang itu **selalu yang belakang**, tidak pernah yang depan. Tidak ada bentuk yang membuang angka depan.

Untuk nomor 12, kuncinya satu pertanyaan: `n % 2 == 0` itu sudah menghasilkan apa? Dibuktikan:

```python
print(n % 2 == 0)         # True
print(type(n % 2 == 0))   # <class 'bool'>
```

Hasilnya **sudah** boolean. Menulis `if ...: return True else: return False` sama dengan bertanya "kalau True, kembalikan True". Ini pola yang sudah saya pakai sendiri waktu merapikan NUMB3RS jadi `return bool(...)`.

### Pemanasan murojaah

Lima pertanyaan dari materi kemarin (shadowing, global module-level, titik, konstanta, dua alasan global dihindari). **Lima-limanya benar.**

---

## Class variable

`MEOWS = 3` ditulis di dalam class, di luar method. Saya sempat menyebutnya "global variable di dalam class" — **salah istilah**, ini **class variable**, dan nama itu sudah saya pelajari 15 November di `hat.py`.

```python
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
```

Tiga tingkat yang sekarang lengkap:

| Ditulis di mana | Namanya | Dipanggil |
|---|---|---|
| Di dalam function | variabel lokal | langsung |
| Di dalam class, di luar `__init__` | class variable | `Cat.MEOWS` |
| Di dalam `__init__` pakai `self.` | instance variable | `cat.nama` |
| Di luar semua, tingkat file | "global" (module-level) | `bank.balance` |

### self.MEOWS juga jalan, tapi David memilih Cat.MEOWS

Percobaan saya, mengganti `Cat.MEOWS` jadi `self.MEOWS`:

```python
def meow(self):
    for _ in range(self.MEOWS):
        print("meow")
```

**Jalan.** Kalau Python tidak menemukan nama itu di objeknya, dia naik mencari ke classnya.

Saya langsung menghubungkannya dengan error yang merambat naik mencari `except`, dan itu memang pola yang sama — "cari ke atas sampai ketemu". Bedanya apa yang dicari:

```
error     mencari PENANGKAP (except), lewat rantai pemanggilan
atribut   mencari NAMA, dari objek naik ke class
super()   mencari kode INDUK, naik satu tingkat
```

Lalu kenapa David tetap menulis yang lebih panjang? Ada dua alasan.

**1. Kejelasan.** `Cat.MEOWS` mengatakan "ini milik class, sama untuk semua kucing". `self.MEOWS` kelihatan seperti milik kucing ini saja, padahal bukan. Tema semantics lagi, sama dengan `student["name"]` menang dari `student[0]`.

**2. Kepastian.** Percobaan yang membuktikannya:

```python
a = Cat()
b = Cat()
b.MEOWS = 10

print(a.MEOWS)      # 3   <- naik ke class, karena a tidak punya sendiri
print(b.MEOWS)      # 10  <- punya sendiri
print(Cat.MEOWS)    # 3   <- yang asli, TIDAK berubah
```

`b.MEOWS = 10` itu **membuat atribut baru di objek b**, bukan mengubah yang di class. Jadi `a` tidak tersentuh sama sekali — ini persis temuan saya 6 November bahwa atribut menempel ke OBJEK bukan ke class, waktu itu dibuktikan dengan `a.cat` yang tidak menyentuh `b`.

Dan kata yang tepat bukan "menimpa" tapi **menutupi** — shadowing lagi, cuma arahnya objek menutupi class, bukan function menutupi file.

Dengan `Cat.MEOWS`, pencarian itu **dilewati**: langsung ke class, tidak peduli objeknya punya nama yang sama atau tidak.

### del

Keyword baru yang saya temui waktu percobaan, bukan dari lecture. `del` singkatan dari delete, gunanya menghapus **nama**:

```
del x             hapus variabel
del b.MEOWS       hapus atribut milik objek
del daftar[0]     hapus item di posisi
del kamus["a"]    hapus satu pasangan di dict
```

Buktinya bahwa yang di class tidak pernah tersentuh:

```python
del b.MEOWS
print(b.MEOWS)      # 3, bayangannya hilang jadi naik ke class lagi

del Cat.MEOWS
print(a.MEOWS)      # AttributeError, pencariannya mentok
```

---

## Type hints

Notasinya dua, dan saya sudah melihatnya duluan tanggal 21 di `help(pdf.set_y)` tanpa tahu namanya:

```python
def tambah(n: int) -> int:
    return n + n
```

```
n: int      parameter n maunya diisi integer
-> int      FUNCTION ini menyerahkan integer
```

Yang perlu diperjelas: `-> int` itu milik **functionnya**, bukan milik `n`. Letaknya juga menegaskan — ditulis sesudah kurung tutup, di luar wilayah parameter. Yang di dalam kurung tentang masukan, yang sesudah kurung tentang keluaran.

```python
def sapa(nama: str) -> None:
    print(f"halo, {nama}")
```

`-> None` karena isinya cuma print, tidak ada return. Jadi sekarang saya bisa membaca `set_y(y: float) -> None` tanpa menebak-nebak.

### Python TIDAK memeriksanya

Ini yang saya kira cuma keyword biasa, ternyata ada pembagian:

```
MENULIS type hints    tidak butuh tool apa-apa, cuma notasi : dan ->
MEMERIKSA type hints  butuh tool luar, yaitu mypy
```

Buktinya:

```python
def tambah(n: int) -> int:
    return n + n

print(tambah("halo"))   # jalan mulus, keluar halohalo
```

Type hintnya bilang `int`, isinya string, Python diam saja. Ini pola lama yang bertambah satu:

```
nilai default   bukan pengumuman tipe
type hint       bukan pemeriksaan
```

### mypy

Program terpisah yang membaca kode lalu mengadukan ketidakcocokan. Dia **tidak menjalankan** programnya, cuma membacanya.

```
python file.py    menjalankan
mypy file.py      memeriksa, tanpa menjalankan
```

Bukan bawaan Python, harus `pip install mypy` dulu — sama seperti cowsay, fpdf2, dan tabulate.

Contoh David yang paling mengena:

```python
number: int = input("Number: ")
```

mypy menemukannya di **baris 6**, padahal `meow(number)` baru dipanggil di baris 7. Pesannya: `Incompatible types in assignment (expression has type "str", variable has type "int")`.

Kalau dijalankan Python biasa, baris itu **tidak error sama sekali** — `number` berisi string, dan baru meledak nanti di `range(n)`. Jadi gunanya type hints bukan mencegah, tapi **memajukan waktu ketahuannya**.

Dan yang diperiksa mypy itu `your own type hints` — aturan yang **saya** tulis sendiri. Kalau saya tidak menulis type hints sama sekali, mypy tidak punya apa-apa untuk diperiksa.

Jadi daftar rambu-bukan-gembok sekarang bertambah satu, dan yang terakhir ini punya penjaganya:

```
_balance    garis bawah   jangan disentuh dari luar      tidak ada penjaganya
JUZ         huruf besar   jangan diubah                  tidak ada penjaganya
n: int      type hint     maunya diisi integer           PENJAGANYA mypy
```

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| accidentally | TIDAK sengaja (lawan dari on purpose). Saya sempat mengira artinya sengaja |
| readily | dengan mudah, tanpa susah payah |
| adhere to | mematuhi, menaati, berpegang pada. Arti harfiahnya melekat, seakar dengan adhesive (lem) |
| frankly | terus terang, sejujurnya |
| a little more quickly | sedikit lebih cepat. `a little` itu pelunak, seperti tend to |
| dynamically | Python menentukan tipenya sendiri saat program jalan, tidak perlu diberi tahu |

Catatan: `frankly` sudah pernah masuk catatan 15 November, jadi ini ulangan. Keluarga katanya `to be fair` dan `honestly` — semuanya menandai bahwa yang disebut sesudahnya itu pengakuan, bukan klaim.

## Yang mau dicoba

- Lanjut Lecture 9 dari **menit 37**.
- Coba `pip install mypy` lalu jalankan pada salah satu file lama saya, lihat apa yang diadukan.

---

## Hari 5 – 25 November 2026

Lanjut Lecture 9 dari menit 37 sampai sekitar **menit 52**. Selesai type hints dan mypy, masuk **docstring**. Pagi: Kuis Harian #26 dan pemanasan.

### Kuis Harian #26

16 soal, giliran Hari ke-6: Week 5 dan Week 2. Hasilnya **14/16**, dan yang salah dua-duanya **Week 2** — materi yang paling lama tidak saya sentuh.

| No | Materi | Koreksinya |
|---|---|---|
| 10 | `range(1, 10, 2)` | Angka ketiga itu LANGKAH, bukan batas |
| 11 | `.get(item, 0)` | Angka 0 itu nilai CADANGAN kalau kuncinya belum ada |

Percobaan nomor 10:

```python
print(list(range(1, 10)))       # [1..9]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
```

Bacanya `range(mulai, batas, langkah)`. Mulai ikut, batas TIDAK ikut, langkah bawaannya 1. Angka 9 masih ikut karena di bawah 10; berikutnya 11, sudah lewat, berhenti.

Percobaan nomor 11:

```python
d = {"apel": 2}
print(d.get("apel", 0))    # 2
print(d.get("jeruk", 0))   # 0, walaupun jeruk tidak ada
print(d["jeruk"])          # KeyError
```

Jadi `d[x] = d.get(x, 0) + 1` artinya: ambil hitungan lama, kalau belum pernah ada anggap 0, lalu tambah 1. Ini pola Grocery List saya 7 Oktober.

### Pemanasan murojaah

Lima pertanyaan dari materi kemarin. Empat benar, termasuk nomor 2 yang paling panjang (kenapa `self.MEOWS` jalan tapi David tetap memilih `Cat.MEOWS`).

Nomor 5 belum kena intinya. Saya bilang "yang satu program kita, yang satu tools" — benar tapi belum menjawab bedanya. Yang penting: **mypy tidak menjalankan apa pun.**

```
python file.py    MENJALANKAN     input muncul, print keluar
mypy file.py      MEMBACA saja    tidak ada yang dijalankan
```

Dari situ keunggulannya: mypy bisa menemukan masalah di baris 6 padahal baris 7 belum pernah dieksekusi. Kalau dia harus menjalankan dulu, dia tidak akan lebih cepat dari Python. Buktinya, `mypy` pada file yang ada `input()`-nya **tidak bertanya apa-apa** — langsung keluar laporannya.

---

## Kenapa Python longgar soal tipe

David menjelaskan alasannya, dan ini pertukaran yang menarik. Python sengaja dirancang `versatile` dan `flexible`, supaya `doesn't have to bother checking these kinds of details`.

```
longgar   cepat ditulis, cepat jalan, tapi salah tipe lolos diam-diam
ketat     lebih repot, tapi kesalahannya ketahuan lebih awal
```

Tapi dia jujur mengakui sisi lainnya: `strong type checks do tend to be a good thing for the correctness of your code`. Itu sebabnya mypy ada — menambahkan ketatnya **tanpa** memaksakannya ke seluruh bahasa. Saya yang memilih.

Dan `but to date, Python itself does not enforce these conventions` — kata `to date` menyisakan kemungkinan suatu saat berubah. Dia tidak bilang tidak akan pernah.

Istilah resmi untuk apa yang selama ini saya sebut rambu ternyata **convention**: huruf besar untuk konstanta, garis bawah untuk privat, `self` untuk parameter pertama. Semuanya convention, bukan aturan bahasa.

Alasan tim profesional tetap memakai type hints, kata David, cukup satu kalimat: `if it just decreases the probability of bugs`.

## mypy menangkap function yang tidak mengembalikan apa-apa

Contoh berikutnya yang paling mengena buat saya:

```python
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

meows: str = meow(number)
```

Pesan mypy: `"meow" does not return a value`.

**Ini persis masalah hello.py di Week 5 saya**, dan juga shuffle yang tiga kali saya tabrak:

```
function yang cuma print   ->  mengembalikan None
ditampung ke variabel      ->  variabelnya berisi None
```

Bedanya: dulu saya baru tahu setelah tesnya merah. Sekarang mypy mengadukannya **sebelum dijalankan**.

Pertanyaan saya: kalau `meow` benar-benar mengembalikan sesuatu tapi tipenya beda dengan kotaknya, apakah mypy juga mengadu? **Iya.** Dibuktikan:

```python
def meow(n: int) -> int:
    return n * 2

meows: str = meow(3)
```

```
python   jalan mulus, keluar 6
mypy     error: Incompatible types in assignment
         (expression has type "int", variable has type "str")
```

Python-nya tetap diam. Yang mengadu cuma mypy.

Koreksi untuk saya: di kasus aslinya isi `meow(number)` itu bukan integer tapi **None**. `number` memang integer, tapi itu yang MASUK; yang KELUAR tidak ada.

```
number        int      yang masuk
meow(...)     None     yang keluar
meows: str             kotak yang menunggu str
```

Dan solusi David: `let's practice what we preached in our focus on unit tests, having a function like meow not have side effects like printing itself, but let's have it return the actual string`. Obatnya sama dengan catatan saya 18 Oktober — **function yang mudah dites adalah function yang me-return hasilnya**, urusan print diserahkan ke main.

Bentuk akhirnya:

```python
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
```

`end=""` dipakai karena `\n`-nya sudah ada di dalam string, kalau tidak barisnya dobel di akhir. Pola yang sama dengan `readlines` di Week 6.

### Pertanyaan mahasiswa: kenapa \n tidak dianggap tulisan biasa?

Padahal ada di dalam tanda kutip. Jawabannya: `\` di dalam string itu **tanda khusus**, dia dan huruf sesudahnya dibaca berpasangan.

```
\n    baris baru
\t    tab
\\    satu backslash sungguhan
\"    tanda kutip yang tidak menutup string
```

Percobaan:

```python
print("meow\n" * 3)      # tiga baris
print(r"meow\n" * 3)     # satu baris, tulisannya meow\n tiga kali
print(len("\n"))         # 1
```

Yang ketiga keluar `1` — `\n` itu **satu karakter**, bukan dua, walaupun diketik dengan dua tombol.

Jadi tanda kutip menentukan "ini teks", tapi tidak membuat isinya mentah. Yang membuat mentah itu huruf `r` di depannya — **raw string** dari Week 7.

### typecasting lawan converting

David mengoreksi istilahnya sendiri:

```
C / C++    typecasting   menafsir ulang data yang SAMA sebagai tipe lain
Python     converting    MEMBUAT nilai baru dari yang lama
```

`int("50")` tidak menyulap string itu jadi angka. Dia menghasilkan angka BARU, dan stringnya tetap utuh — persis pelajaran lama saya bahwa `int(x)` tidak mengubah `x`.

Dan satu hal yang sering bikin bingung, kata `int` dipakai di dua tempat berbeda:

```python
number: int = int(input("Number: "))
#       ^^^       ^^^
#    type hint   dipanggil, menghasilkan nilai baru
```

Yang pertama cuma catatan, yang kedua benar-benar bekerja. **Type hint tidak menggantikan konversi** — `number: int` tidak membuat Python mengubah stringnya, `int(...)` tetap wajib ditulis.

Catatan: David menyebut `int itself is still a function`, padahal `int` itu **class** — saya buktikan sendiri 13 November lewat dokumentasi resmi yang menulis `class int(x, base=10)`.

---

## Docstring

String yang ditaruh di **baris pertama di dalam** function, pakai tanda kutip tiga.

```python
def meow(n: int) -> str:
    """Return a string of n meows, one per line."""
    return "meow\n" * n
```

Dan ini yang paling membuka: **docstring itulah yang selama ini saya baca lewat `help()`**. Waktu saya menjalankan `help(pdf.set_y)` tanggal 21, yang muncul itu docstring yang ditulis pembuat fpdf.

Jadi urutan lama saya sekarang lebih masuk akal:

```
dir(objek)    namanya
help(nama)    docstringnya  <- DITULIS MANUSIA, bukan dihasilkan Python
dokumentasi   celah dan jebakannya
```

### Letaknya menentukan, bukan selera

```python
# penjelasan di sini          <- cuma komentar, TIDAK masuk __doc__
def meow(n):
    """penjelasan di sini"""  <- INI yang jadi docstring
    return n
```

Yang di atas dibuang Python begitu selesai dibaca. Yang di dalam disimpan. Salah tempat berarti `help()` kosong.

### function ternyata punya atribut

Ini yang paling mengagetkan hari ini. Saya kira atribut cuma ada pada objek yang dibuat dari class.

```python
print(meow.__name__)   # meow
print(meow.__doc__)    # isi docstringnya
```

Koreksinya: **tidak ada function tanpa class.** `meow` itu sudah objek, dan classnya bernama `function`. Python membuatnya begitu baris `def` dibaca.

```python
print(type(meow))      # <class 'function'>
```

Jadi aturan lama tetap berlaku, objek memang lahir dari class. Yang baru: class `function` itu bawaan Python, bukan yang saya tulis. Ini kelanjutan temuan 13 November bahwa `int` dan `str` pun class.

```
"azka"    objek dari class str
[1, 2]    objek dari class list
meow      objek dari class function
```

Koreksi istilah kedua, dan ini persis koreksi yang saya dapat 20 November soal `.size`:

```
special method    dunder yang DIPANGGIL, pakai kurung    __init__()  __add__()
atribut dunder    dunder yang berisi DATA, tanpa kurung  __doc__  __name__
```

`meow.__doc__` tanpa kurung, jadi atribut. Dugaan saya bahwa dunder cuma ada di class memang wajar karena semua dunder yang saya temui selama ini ditulis di dalam class, tapi aturan sebenarnya lebih sederhana: **dunder itu nama yang sudah dipesan Python**, di mana pun letaknya.

### Beda __name__ dan __doc__

```python
def diam(n):
    return n

print(diam.__name__)   # diam
print(diam.__doc__)    # None
```

```
__name__   PYTHON yang isi    selalu ada
__doc__    SAYA yang isi      None kalau tidak ditulis
```

Itu sebabnya `help()` pada function orang lain kadang cuma menampilkan tanda tangannya saja — pembuatnya tidak menulis docstring.

Dan `__name__` yang sama isinya menyesuaikan tempatnya:

```
__name__ pada file       __main__ atau nama modulnya
__name__ pada function   nama functionnya
__name__ pada class      nama classnya
```

### Beda help() dan __doc__

```
meow.__doc__    mengambil ISI mentahnya
help(meow)      membacakannya RAPI, plus tanda tangan dan tipenya
```

Terbukti di terminal saya: `help` menampilkan `meow(n: int) -> str` beserta docstringnya, sedangkan `__doc__` cuma barisnya saja.

### Berapa banyak dunder bawaan Python

Tidak ada angka pasti yang perlu dihafal, puluhan dan bertambah tiap versi. Cara melihatnya pakai alat yang sudah saya punya:

```python
print([x for x in dir(list) if x.startswith("__")])
```

Yang sudah saya pakai sejauh ini: `__init__`, `__str__`, `__add__`, `__sub__`, `__name__`, `__doc__`, `__dict__`, `__main__`. Itu sudah cukup. Yang perlu nempel cuma polanya: `__...__` berarti nama yang sudah dipesan, jangan bikin sendiri dengan bentuk itu.

### Bentuk baku PEP 257

```
:param n:         penjelasan parameter n, kalimat manusia
:type n: int      jenis isi parameter n
:raise TypeError: error apa yang bisa dilempar, dan kapan
:return:          apa yang diserahkan, kalimat manusia
:rtype: str       jenis yang diserahkan
```

`rtype` = **return type**. Jadi berpasangan: `:return:` menjelaskan APA isinya, `:rtype:` menyebut JENISnya. Sama polanya dengan `:param` dan `:type`.

Soal titik dua di depan dan belakang: itu bukan aturan Python dan bukan aturan VS Code. Namanya **reStructuredText**, bahasa penanda mirip Markdown untuk dokumentasi. Buat Python semuanya cuma teks biasa; yang membacanya alat pembuat dokumentasi, yang mengubahnya jadi halaman web rapi.

PEP sendiri = **Python Enhancement Proposal**, dokumen usulan resmi. PEP 257 mengatur docstring, PEP 8 mengatur gaya penulisan kode.

Dan PEP itu kesepakatan, bukan paksaan. Docstring boleh ditulis asal-asalan:

```python
def meow(n):
    """asdfgh"""
    return n
```

Jalan mulus, tapi `help(meow)` menampilkan `asdfgh` dan pembacanya tidak dapat apa-apa.

Jadi daftar rambu-bukan-gembok sekarang empat:

```
_balance      garis bawah
JUZ           huruf besar
n: int        type hint        (punya penjaga: mypy)
"""..."""     docstring PEP 257
```

### Tumpang tindih docstring dan type hints

```python
def meow(n: int) -> str:     <- type hint, dibaca MYPY
    """
    :type n: int             <- teks, dibaca MANUSIA dan alat dokumentasi
    :rtype: str
    """
```

Tipenya ditulis dua kali untuk pembaca yang berbeda. Makanya David bilang `this does not have anything to do fundamentally with type hints`.

Pertanyaan saya: kalau dua-duanya bertentangan, apakah bertabrakan saat mypy dijalankan? **Tidak**, dan justru itu masalahnya. Dibuktikan dengan menulis docstring yang sengaja kebalikan dari type hintnya — mypy tetap **hijau**, karena buat dia docstring cuma string biasa.

```
type hint     diperiksa mypy      ketahuan kalau salah
docstring     tidak diperiksa     bisa bohong selamanya
```

Jadi bahayanya bukan tabrakan, tapi **tidak ada yang menabrak**. Kalau parameternya suatu saat diubah tapi docstringnya lupa diperbarui, pembacanya tersesat tanpa satu pun error. Daftar "salah tanpa error" lagi, bentuk baru: bukan programnya yang salah, tapi **keterangannya**.

Itu alasan praktis kenapa sekarang banyak yang membuang `:type:` dan `:rtype:` dan mengandalkan type hints saja — satu sumber kebenaran lebih aman daripada dua yang bisa menyimpang. Tapi bentuk lengkapnya masih sering ketemu `in the wild`, terutama di kode lama.

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| versatile | serbaguna, bisa dipakai macam-macam keperluan |
| flexible | luwes, tidak kaku |
| writeability | kemudahan menulisnya |
| bother | repot-repot (`doesn't have to bother checking`) |
| a matter of opinion | soal selera, bukan benar-salah |
| to date | sampai saat ini, hingga sekarang. Sinonim so far |
| convention | kesepakatan, kebiasaan yang disepakati bersama |
| code base | seluruh kumpulan kode satu project |
| in the wild | di dunia nyata, di kode orang lain yang beredar |
| foolish | bodoh, konyol (dari fool) |
| practice what we preached | jalankan sendiri apa yang kita khotbahkan |
| side effects | efek samping, kerja sampingan di luar menyerahkan hasil |
| typecasting | menafsir ulang tipe (istilah C/C++), BUKAN yang terjadi di Python |
| converting | mengubah dengan membuat nilai baru — ini yang dilakukan Python |
| doc string | string penjelas di dalam function |
| PEP | Python Enhancement Proposal, dokumen usulan resmi |
| reStructuredText | bahasa penanda mirip Markdown untuk dokumentasi |
| rtype | return type, jenis nilai kembalian |
| proactively annotated | ditandai duluan sebelum diminta |

## Yang mau dicoba

- Lanjut Lecture 9 dari **menit 52**.
- Pasang `pip install mypy` lalu jalankan pada salah satu file lama, lihat apa yang diadukan.
- Tambahkan docstring ke satu function lama saya, lalu cek dengan `help()`.
