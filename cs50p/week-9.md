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

---

## Hari 6 – 26 November 2026

Lanjut Lecture 9 dari menit 52 sampai sekitar **menit 55**. Selesai docstring, lewat doctest, lalu masuk **argparse**. Sebagian besar waktu habis di argparse, karena saya minta praktek jadi usernya dulu supaya paham.

### Kuis Harian #27

Giliran Hari ke-7. Yang salah cuma **nomor 14**, soal `__name__` dan `__doc__`. Dua-duanya dunder, tapi isinya beda urusan:

```
__name__    nama modulnya        "__main__" kalau dijalankan langsung
__doc__     isi docstringnya     None kalau tidak ada docstring
```

Nomor ini masuk daftar ulangan untuk kuis besok.

### Pemanasan murojaah

Pertanyaan soal letak docstring. Jawaban saya: kalau stringnya ditaruh **di atas** function, Python cuma menganggapnya komentar biasa, bukan docstring. Supaya terbaca jadi `__doc__`, dia harus **di dalam** function, tepat di baris pertama.

```python
# penjelasan di sini        <- komentar, TIDAK masuk __doc__

def meow(n):
    """penjelasan di sini"""   <- docstring, masuk __doc__
```

---

## Docstring yang dipanen jadi dokumentasi

Ini yang awalnya bikin saya bingung. Saya kira maksudnya docstring saya **berubah** jadi PDF. Bukan.

Yang terjadi: ada alat yang **membaca** semua docstring di kode saya, lalu menyusunnya jadi dokumen — bisa halaman web, bisa PDF. Docstringnya tetap di tempatnya, cuma disalin keluar.

Jadi alurnya satu arah:

```
docstring di kode  ->  dipanen alat  ->  halaman web / PDF
```

Dan ini bukan hal asing. Yang selama ini saya baca di docs.python.org itu sumbernya sama dengan yang keluar kalau saya ketik `help()` di terminal. Satu tulisan, dua pintu keluar.

Inilah alasan kenapa PEP 257 bikin aturan bentuk penulisan docstring. Kalau bentuknya seragam, alat pemanennya tahu mana judul mana keterangan. Kalau tiap orang menulis sesuka hati, hasil panennya berantakan.

## doctest

Di docstring juga boleh ditulis **contoh pemakaian** lengkap dengan hasilnya, pakai tanda `>>>` seperti di terminal. Gunanya dobel: manusia yang membaca langsung lihat contohnya, dan ada alat yang bisa **menjalankan** contoh itu lalu mengecek hasilnya cocok atau tidak.

Jadi contoh di dokumentasi tidak cuma pajangan, dia bisa ikut diuji.

---

## argparse

Kata `parse` artinya **membedah dan memahami**. `argparse` berarti alat yang membedah argumen dari terminal.

Selama ini di Figlet saya mengurus sendiri: hitung `len(sys.argv)`, periksa `sys.argv[1]`, lalu `sys.exit("Invalid usage")` kalau tidak cocok. Itu yang dimaksud "diurus sendiri". Dengan argparse, pekerjaan itu diambil alih.

Kode latihan saya:

```python
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
```

Dua baris yang sering saya tertukar:

```
baris 1   argparse.ArgumentParser(...)   instantiation, bikin objeknya
baris 2   parser.add_argument(...)       pemanggilan method pada objek yang sudah jadi
```

Percobaan print penanda, untuk melihat isi tiap tahap:

```
1. parser itu: ArgumentParser(prog='train.py', description='Meow like a cat', ...)
2. sudah didaftarkan
3. args itu: Namespace(n=1)
4. args.n itu: 1 <class 'int'>
```

Yang penting dari sini: angka 1 di `Namespace(n=1)` itu muncul **padahal saya tidak mengetik apa-apa**. Dia datang dari `default=1`.

## Praktek jadi user

Saya jalankan satu per satu, menebak dulu tiap kali.

```
python train.py           meow  (sekali, dari default)
python train.py -n 3      meow meow meow
python train.py --help    keluar daftar options
```

Hasil `--help`:

```
usage: train.py [-h] [-n N]

Meow like a cat

options:
  -h, --help  show this help message and exit
  -n N        number of times to meow
```

Baris `-n N` itu bacanya: labelnya `-n`, lalu isinya menyusul. Huruf `N` besar cuma tempat kosong yang mewakili angka.

Yang berubah antara perintah pertama dan kedua **cuma satu angka**, yaitu isi `args.n`. Kodenya tidak saya sentuh sama sekali. `for _ in range(args.n)` tetap baris yang sama.

Dan yang saya ketik di terminal itu sebenarnya **teks**, bukan angka. Yang mengubahnya jadi angka beneran adalah `type=int`.

## Strip dihilangkan: positional

Saya tanya, boleh tidak stripnya dihapus jadi `"n"` saja, biar lebih jelas namanya. Ternyata boleh — tapi yang berubah bukan namanya, melainkan **aturan mainnya**.

```python
parser.add_argument("n", default=1, help="number of times to meow", type=int)
```

Empat percobaan, dan tiga di antaranya terbalik dari kemarin:

```
python train.py        error: the following arguments are required: n
python train.py -n 3   error: unrecognized arguments: -n
python train.py n 3    error: argument n: invalid int value: 'n'
python train.py 3      meow meow meow
```

Perintah ketiga itu saya jalankan iseng, dan justru itu yang paling membuka. Saya mengetik huruf `n` dengan harapan dikenali sebagai **nama**. Tapi argparse tidak melihat nama — dia melihat huruf `n` sebagai **isi**, lalu mencoba `int("n")` dan gagal.

Pelajarannya:

```
positional   namanya cuma hidup di dalam kode (args.n), user tidak pernah mengetiknya
flag         namanya diketik user di terminal (-n 3)
```

Saya sebenarnya sudah lama memakai positional tanpa sadar: `python train.py` itu sendiri. Saya tidak pernah mengetik `python --file train.py`.

Satu lagi yang halus. Error kedua bunyinya `unrecognized arguments: -n`, **bukan** `required: n`. Artinya angka 3-nya sebenarnya **diterima** dan sudah mengisi n. Yang bikin gagal cuma `-n`, yang tidak punya tempat lagi. Jadi dua error itu beda sebab: yang satu kosong, yang satu kelebihan.

Dan `default=1` jadi mubazir di versi positional. Masuk akal kalau dipikir: kalau sesuatu sudah **wajib**, buat apa punya cadangan. Cadangan cuma berguna untuk yang boleh kosong.

## Label versus urutan

Ini inti segmennya. Penampungnya **sama** di dua versi, yaitu `args.n`. Buktinya baris terakhir tidak pernah saya ubah: `for _ in range(args.n)`. Yang saya ketik di terminal itu bukan penampungnya, tapi **alamatnya**.

Ada dua cara argparse tahu angka itu untuk siapa:

```
-n 3    dikenali lewat LABEL,  "ini untuk n"
3       dikenali lewat URUTAN, "yang pertama itu n"
```

Yang dimaksud urutan itu urutan kata yang diketik di terminal, dihitung dari kiri:

```
python   train.py   3   5
                    ^   ^
                 kata1  kata2 (setelah nama file)
```

Ini sama persis dengan `sys.argv[1]` dan `sys.argv[2]` yang saya pakai waktu bikin Figlet. Angka di dalam kurung siku itu memang urutan. Bedanya sekarang argparse yang menghitung, bukan saya.

Kenapa label harus diketik kalau pakai flag? Karena flag **boleh dilewat**. Begitu sesuatu boleh dilewat, menghitung urutan jadi mustahil. Kalau ada dua flag `-n` dan `-v` lalu user mengetik `python train.py 3`, tidak ada yang bisa menjawab angka itu untuk siapa.

Sebaliknya positional **tidak boleh dilewat**, dan justru karena itu urutannya bisa diandalkan.

Untuk flag, yang berlaku bukan urutan tapi **menempel**:

```
python train.py -v 5 -n 3
                      ^^ ^
                      3 milik n karena menempel di belakang -n
```

Angka 3 di situ ada di posisi keempat, bukan pertama, tapi tetap masuk ke n.

Kesimpulan yang saya susun sendiri, dan ternyata pas:

```
flag        mirip dictionary   {"n": 3}   dikenali lewat key
positional  mirip list         [3, 5]     dikenali lewat urutan
```

`Namespace(n=1)` yang muncul di layar itu memang betul-betul disimpan sebagai pasangan nama dan nilai, bukan deretan.

Dan ini menyambung ke yang sudah lama saya pegang:

```
student[0]        list, bergantung urutan
student["name"]   dictionary, bergantung nama
```

Sama persis. Cuma kali ini pelakunya si user di terminal, bukan saya di dalam kode. Makanya positional punya bahaya lama itu lagi: kalau dua positional tertukar urutannya, programnya tetap jalan tanpa error, cuma isinya salah. **Salah tanpa error** lagi.

Tentang tulisan di `add_argument`, tugasnya bisa satu atau dua tergantung ada strip atau tidak:

```
"-n"   label yang diketik user  +  nama penampung (args.n)
"n"    nama penampung saja (args.n)
```

Waktu pakai strip, argparse membuang stripnya lalu sisanya dipakai jadi nama penampung. Itu sebabnya saya menulis `args.n`, bukan `args.-n`.

Catatan supaya tidak salah hafal: tugas utama strip itu "dikenali lewat label". Boleh-kosongnya itu akibat bawaan, bukan definisinya. Di luar lecture ada flag yang justru diwajibkan — bentuknya tetap `-n` tapi tidak boleh dilewat.

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| parse | membedah lalu memahami. Asal kata argparse |
| blinking | berkedip |
| positional | berdasarkan posisi, urutan ke berapa |
| optional | boleh diisi boleh tidak |
| flag | bendera, argumen berlabel seperti `-n` |
| unrecognized | tidak dikenali |
| required | diwajibkan |
| harvest | memanen, mengambil hasil untuk dipakai di tempat lain |

## Yang mau dicoba

- **PR dari tadi malam**: kembalikan ke `"-n"`, lalu jalankan `python train.py 3`. Tebak dulu ditolak atau tidak.
- Hapus `type=int`, lalu jalankan `python train.py -n 3`. Lihat `range` meledak di mana.
- Hapus `default=1`, lalu jalankan `python train.py` tanpa `-n`. Isi `args.n` jadi apa kalau cadangannya tidak ada.
- Daftarkan dua argumen sekaligus, lalu bandingkan: versi flag `-n 3 -v 5` dibolak-balik tetap sama, versi positional `3 5` dibalik jadi `5 3` tetap jalan tapi isinya tertukar.
- Bandingkan `help(str.strip)` di terminal dengan halaman `str.strip` di docs.python.org, buktikan sumbernya sama.
- Lanjut Lecture 9 dari **menit 55**.
- Pasang `pip install mypy` lalu jalankan pada salah satu file lama, lihat apa yang diadukan.
- Tambahkan docstring ke satu function lama saya, lalu cek dengan `help()`.

---

## Hari 7 – 27 November 2026

Lanjut Lecture 9 dari menit 55 sampai sekitar **menit 1:05**. Tapi sebagian besar waktu habis membongkar `Namespace` sampai tuntas, karena di situ saya paling banyak salah paham.

### Kuis Harian #28

Giliran Hari ke-1 (Week 0 dan Week 4). **Bersih semua**, dan tiga soal ulangan (`range` dengan langkah, `.get` dengan cadangan, `__name__` lawan `__doc__`) nempel semuanya.

Satu nomor saya tandai sebagai **soal yang cacat, bukan jawaban yang salah**: nomor 12 punya dua pilihan yang bedanya cuma spasi di ujung (`"  Azka Parhan  "` lawan `"Azka Parhan"`), dan tampilan kuis memakan spasi di ujung sehingga dua pilihan itu terlihat identik. Aturannya sekarang: kalau spasi jadi pembeda, tanda kutipnya harus ditulis kelihatan.

### Pemanasan murojaah

Lima soal: nomor 1 dan 5 benar, nomor 3 separuh, nomor 2 dan 4 belum kena.

Nomor 2 saya menjelaskan **akibatnya** (positional wajib diisi, default jadi mubazir), padahal yang ditanya **kenapa labelnya wajib diketik**. Jawabannya: karena flag boleh dilewat, dan begitu boleh dilewat, menghitung urutan jadi mustahil.

Nomor 3 saya jawab bagian keduanya saja (`int("n")` gagal), yang pertama terlewat: huruf `n` dianggap isi karena **nama positional tidak pernah diketik user**.

Nomor 4 saya malah masuk ke pembahasan atribut lawan special method, padahal jawabannya sederhana — yang keluar dari `help()` itu **tulisan manusia**, docstring yang diketik pembuat library.

Nomor 5 benar, satu koreksi letak: pada sebuah **function**, `__name__` berisi nama functionnya, bukan nama file.

```
meow.__name__     "meow"        diisi Python
meow.__doc__      docstring     diisi saya
```

---

## PR kemarin: flag tanpa label

Tebakan saya benar — `python train.py 3` dengan `-n` terdaftar ditolak:

```
unrecognized arguments: 3
```

Lalu dibuktikan lebih tajam dengan DUA flag:

```python
parser.add_argument("-n", default=1, type=int)
parser.add_argument("-v", default=1, type=int)
```

`python train.py 3` tetap ditolak, dan sekarang alasannya kelihatan: **angka 3 itu untuk `n` atau untuk `v`?** Tidak ada yang bisa menjawab. Dengan satu flag saya masih bisa berkilah "ya jelas untuk n, kan cuma dia satu-satunya"; dengan dua flag kilah itu hilang.

```
flag        boleh dilewat  ->  urutan tidak bisa dihitung  ->  butuh label
positional  wajib ada      ->  urutan pasti bisa dihitung  ->  tidak butuh label
```

## Namespace, dibongkar sampai tuntas

Ini bagian terpanjang hari ini. Saya kira `Namespace` itu cuma istilah, ternyata itu **nama class**.

```
namespace    istilah umum, lembar absen        (sudah saya pakai sejak Week 4)
Namespace    nama class di argparse            (huruf besar)
```

Jadi bukan yang satu menggantikan yang lain. Argparse menamai classnya dengan istilah itu karena tugasnya memang memegang daftar nama.

Susunannya:

```
args                 variabel, nama panggilan
  └─ Namespace(...)  WADAHNYA, si lembar absen
        └─ n = 1     satu baris isi di dalamnya
```

Percobaan yang paling membuka, `print(n)` dan `print(args.n)` berdampingan:

```
NameError: name 'n' is not defined
```

Jadi `n` memang **bukan variabel**. Dia ada, tapi di dalam absen milik `args`, bukan di absen file saya. Ini error yang sama persis dengan soal nomor 15 di kuis pagi itu:

```
import random     lalu  choice([1,2,3])    NameError
parse_args()      lalu  print(n)           NameError
```

Dan `print(args.n)` di baris bawahnya tidak sempat jalan, karena program berhenti begitu error muncul.

### Membuat Namespace sendiri

Percobaan ini yang bikin semuanya klik — saya jadi argparse-nya sendiri:

```python
import argparse

kosong = argparse.Namespace()
print("1.", kosong)

kosong.n = 3
print("2.", kosong)
print("3.", kosong.n)
```

Hasilnya:

```
1. Namespace()
2. Namespace(n=3)
3. 3
```

Yang saya lakukan di baris `kosong.n = 3` itu **persis yang argparse lakukan untuk saya**. Label `-n` cuma memberitahu dia nama apa yang harus dipakai.

### Atribut tidak harus lahir di `__init__`

Ini salah paham saya yang terbesar hari ini. Saya kira atribut cuma bisa dibuat di dalam `__init__`. Padahal saya sudah membuktikan kebalikannya 24 November lewat `b.MEOWS = 10`.

Aturannya cuma satu, dan dia berlaku di mana saja:

```
objek.nama = nilai

nama belum ada  ->  LAHIR     (kosong.n = 3)
nama sudah ada  ->  DITIMPA   (a.n = 99)
```

`self.x = x` di dalam `__init__` itu cuma **salah satu tempat** aturan ini berlaku. `self` kebetulan objeknya, `__init__` kebetulan tempatnya.

### Dua error yang jadi pasangan

Dalam satu pagi saya menabrak dua error yang membentuk pasangan rapi:

```
print(n)     NameError        nama n tidak ada di absen FILE
args.n       AttributeError   objeknya ADA, tapi n tidak ada di absen OBJEK
```

Yang kedua saya dapat dengan mendaftarkan `-v` saja lalu memanggil `args.n`:

```
AttributeError: 'Namespace' object has no attribute 'n'
```

Bedanya: `NameError` berarti Python tidak tahu harus mencari ke mana. `AttributeError` berarti dia sudah sampai ke objeknya, lalu tidak menemukan namanya di dalam. Sama dengan yang saya tabrak 24 November waktu `del Cat.MEOWS`.

Lalu `args.n()` keluar `'int' object is not callable` — bukti `n` itu **data, bukan function**. Kembaran `jar.capacity(12)` dan `print = 5`.

Jadi namanya **atribut**, bukan property. Property itu yang pakai `@property` dengan getter dan setter, seperti `house` dan `capacity` di Cookie Jar. Istilah ini pernah tertukar juga 20 November waktu membahas `.size`.

## Urutan tidak berpengaruh untuk flag

Dibuktikan dengan dua flag dibolak-balik:

```
python train.py -v 5 -n 3     Namespace(v=5, n=3)
python train.py -n 3 -v 5     Namespace(v=5, n=3)
```

Sama persis. Dan David mengatakan hal yang sama di menit 1:03 — `no matter what order they appeared in`, bahkan tidak perlu alfabetis. Saya sampai di kesimpulan ini sehari lebih dulu dari lecture-nya.

Yang saya perhatikan sendiri: tampilannya selalu `v` dulu, dan itu mengikuti **urutan pendaftaran** di kode saya (`-v` baris 24, `-n` baris 25), bukan urutan ketikan.

Dan urutan pendaftaran punya dua akibat yang sangat berbeda:

```
flag        urutan pendaftaran  ->  cuma urutan TAMPILAN dan urutan di --help
positional  urutan pendaftaran  ->  MENENTUKAN kata keberapa masuk ke mana
```

Untuk flag itu kosmetik. Untuk positional itu seluruh mekanismenya.

### Dua istilah saya yang dikoreksi

Saya sempat menyebut sifat menempelnya flag itu "kayak hardcode". Bukan.

```
hardcoded    nilainya tetap, tidak bisa diganti siapa pun
menempel     nilainya bebas, tapi PASANGANNYA terkunci
```

Lalu saya menyebut positional "kayak random". Juga bukan, dan ini yang lebih penting. Positional sama sekali tidak acak — kata pertama masuk ke yang didaftarkan pertama, selalu. Yang rawan bukan mesinnya tapi **manusianya**:

```
positional   mesinnya pasti, MANUSIANYA yang bisa salah urut, tidak ada yang menegur
flag         manusianya menyebut namanya, salah urut pun tidak berakibat
```

Itu sebabnya ini masuk daftar "salah tanpa error" — bukan karena programnya tidak bisa diandalkan, tapi karena kesalahan manusianya lewat tanpa ketahuan.

## Dua class, bukan class di dalam class

Pertanyaan saya: ini sebenarnya pakai objek dari berapa class?

```python
print(type(parser))    <class 'argparse.ArgumentParser'>
print(type(args))      <class 'argparse.Namespace'>
```

Dua class, dan **sejajar di dalam satu file**, bukan bersarang. Ini yang saya pelajari 23 November: satu file bisa berisi variabel, function, dan class sekaligus (`math.pi`, `random.choice`, `datetime.date`, `fpdf.FPDF`). Titiknya artinya tetap sama: ambil yang di dalamnya.

Hubungan keduanya: `parser` yang bekerja, `Namespace` yang jadi hasilnya. Method `parse_args()` itu **membuat dan menyerahkan** objek baru.

Waktu kalimat "satu objek melahirkan objek lain" tidak masuk, yang menyelesaikan bukan penjelasan tambahan tapi kodenya:

```python
def buat_namespace():
    hasil = argparse.Namespace()
    hasil.n = 3
    return hasil

args = buat_namespace()
```

Itu function yang kerjanya membuat objek lalu menyerahkannya. `parse_args()` kerjanya sama, bedanya dia tidak memaku angka 3 — dia membaca dulu apa yang saya ketik di terminal.

Koreksi untuk saya: `args = buat_namespace()` itu **bukan instantiation**. Instantiationnya cuma satu dan letaknya di dalam, yaitu `argparse.Namespace()`. Yang di luar cuma memanggil dan menampung, sama saja dengan `x = tambah(3, 5)`.

Koreksi kedua: function **tidak menyimpan apa pun**. Tiap dipanggil dia membuat objek baru dari nol. Dibuktikan:

```python
a = buat_namespace()
b = buat_namespace()
a.n = 99
```

```
Namespace(n=99)
Namespace(n=3)
```

`b` tidak tersentuh. Temuan lama 6 November waktu `a.cat` tidak menyentuh `b`.

## Yang paling berharga hari ini: urutan baris menentukan siapa menang

Saya sempat bilang kalau `n = 1` dipaku di dalam `parse_args()`, ketikan user akan diabaikan. Saya tanya balik: bukannya ditimpa? Ternyata pertanyaan saya yang benar, dan kalimat sebelumnya yang kurang tepat.

Yang menentukan bukan kata "dipaku" atau "default", tapi **baris mana yang jalan belakangan**:

```python
def versi_a(ketikan):
    ns = argparse.Namespace()
    ns.n = ketikan      # isi dari user
    ns.n = 1            # MENIMPA tulisan user
    return ns

def versi_b(ketikan):
    ns = argparse.Namespace()
    ns.n = 1            # dipasang duluan
    ns.n = ketikan      # user MENIMPA angka 1
    return ns
```

Dua function itu isinya sama persis, cuma dua barisnya ditukar, dan hasilnya beda. `versi_b` itu yang dipakai argparse beneran.

Jadi koreksi penting: **`default` bukan cadangan yang diperiksa di akhir, tapi nilai yang dipasang di awal lalu boleh ditimpa.** Bedanya dengan yang dipaku:

```
dipaku      SELALU jalan, tidak peduli user mengetik apa
default     dipasang duluan, lalu MUNDUR kalau user mengisi
```

Aturan "yang belakangan menang" ini sama dengan temuan 11 November waktu dekorator `@property` dihapus dan `def house` kedua menimpa yang pertama, persis `x = 5` lalu `x = 10`.

Dan satu catatan cara belajar yang saya sadari sendiri: kalau penjelasannya mulai berputar, **minta kodenya**. Lebih cepat sampai daripada menambah kalimat.

## Di lecture

David menulis versi manual dulu sebelum argparse:

```python
import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")
```

`usage` artinya **cara pakai** — kebiasaan baku program terminal: kalau user salah mengetik, program memberitahu bentuk yang benar. Saya sudah dua kali ketemu kata ini: `sys.exit("Invalid usage")` yang saya tulis sendiri di Figlet, dan baris paling atas `--help` kemarin.

David juga menyebut `switches or flags` — dua nama untuk benda yang sama. Nama `switch` datang dari bendera yang tidak butuh nilai sama sekali, cuma hidup atau mati seperti saklar; `--help` itu saklar murni, `-n 3` lebih mirip pengaturan.

Terakhir, David kena `TypeError: int() argument must be a string... not 'NoneType'`. Sebabnya dia **tidak menulis** `default`, jadi `args.n` isinya `None`, lalu `int(None)` meledak. Ini jawaban PR saya yang belum sempat dijalankan.

```
-n tidak diketik, ada default=1    args.n = 1
-n tidak diketik, tanpa default    args.n = None
```

Catatan supaya tidak salah obat: `type=int` **tidak** menyelamatkan di sini, karena dia cuma mengubah apa yang diketik user; kalau tidak ada yang diketik, tidak ada yang bisa diubah. Kode saya kemarin punya dua-duanya, makanya tidak pernah kena.

Dan kode David pakai `range(int(args.n))` sedangkan punya saya `range(args.n)` — karena saya menulis `type=int`, konversinya sudah terjadi lebih awal. Punya saya lebih aman: `-n cat` ditolak argparse dengan pesan rapi, sedangkan versi David meledak `ValueError` di dalam `range`.

## Kosakata

| Kata/frasa | Arti dalam konteks |
|---|---|
| usage | cara pakai; baris yang memberitahu bentuk perintah yang benar |
| switch | saklar, nama lain untuk flag, terutama yang tanpa nilai |
| no matter what order | tidak peduli urutannya seperti apa |
| compact | ringkas, padat |
| NoneType | jenis dari nilai `None` |

## Yang mau dicoba

- Tukar dua baris `add_argument`, lihat urutan tampilan `Namespace` ikut bertukar.
- Hapus `type=int`, lalu jalankan `python train.py -n 3`. Lihat `range` meledak di mana.
- Jalankan `a, b = [1, 2, 3]` dan `date(1998)` terpisah, catat nama errornya masing-masing. Patokan baru: salah jumlah saat **memanggil function** jadi `TypeError`, salah jumlah saat **unpacking** jadi `ValueError`.
- Bandingkan `help(str.strip)` di terminal dengan halaman `str.strip` di docs.python.org, buktikan sumbernya sama.
- Lanjut Lecture 9 dari **menit 1:05**.
- Pasang `pip install mypy` lalu jalankan pada salah satu file lama, lihat apa yang diadukan.
- Tambahkan docstring ke satu function lama saya, lalu cek dengan `help()`.

---

## Hari 8 – 28 November 2026

Hari pendek. Banyak kerjaan dan baru sampai dari perjalanan, jadi **lecture tidak dilanjut sama sekali**, masih di menit 1:05. Yang jalan cuma kuis dan pemanasan.

### Kuis Harian #29

Giliran Hari ke-2 (Week 1 dan Week 5). Yang salah cuma **nomor 14**, soal pytest.

Patokannya: **pytest hanya menjalankan function yang namanya diawali `test_`.** Nama lain diabaikan total, jadi `assert` di dalamnya tidak pernah dijalankan.

Ini melengkapi temuan saya 18 November soal `jar.py`. Dua aturan yang berbeda:

```
baris di DASAR file   selalu jalan waktu file di-import atau dijalankan
isi sebuah FUNCTION   cuma jalan kalau dipanggil, atau kalau pytest memungutnya
```

Waktu itu `jar.deposit(1)` meledak karena letaknya di dasar file. Kalau baris yang sama ditaruh di dalam `def periksa():` tanpa awalan `test_`, dia tidak akan meledak sama sekali — dan itu justru lebih berbahaya, karena diam.

Satu koreksi atas soal kuisnya sendiri: kalau di sebuah file **tidak ada satu pun** function berawalan `test_`, pytest tidak melaporkan hijau, melainkan `collected 0 items` dan `no tests ran`. Yang hijau itu kalau ada tetangganya yang berawalan `test_`. Intinya tetap sama — isinya tidak pernah dibaca.

Nomor 12 di kuis kemarin juga diulang hari ini dengan pilihan yang diperbaiki, dan kali ini benar.

### Pemanasan murojaah

Lima soal dari materi argparse kemarin. Nomor 2 dan 5 benar penuh. Tiga lainnya **jawabannya benar tapi buktinya meleset**, dan itu pola yang perlu saya waspadai — jawaban benar dengan alasan karangan akan runtuh di soal yang bentuknya beda. Ini kedua kalinya terjadi; yang pertama 13 November waktu saya bilang "karena punya method" padahal buktinya `print(type(Student.house))`.

**Nomor 1.** Saya bilang namespace itu "isi lembaran absennya". Bukan isinya, tapi **lembarannya**.

```
namespace    lembar absennya      (wadahnya)
n            nama yang tercatat   (barisnya)
1            isinya
```

**Nomor 3.** Jawaban benar (atribut bisa dibuat di luar `__init__`), tapi contohnya salah — saya bilang atributnya "ditempel dengan classnya". Yang saya lakukan kemarin bukan itu:

```python
kosong = argparse.Namespace()   # kosong itu OBJEK
kosong.n = 3                    # nempel ke OBJEK, bukan ke class
```

Dan temuan 24 November justru menegaskan arah ini: `b.MEOWS = 10` membuat atribut di objek `b`, sementara `Cat.MEOWS` di class tidak tersentuh.

**Nomor 4.** Jawabannya benar (`default` itu nilai yang dipasang di awal), tapi alasan yang saya sebut justru **alasan jawaban yang salah** — saya bilang "kalau user tidak mengetik apa pun, defaultnya jadi cadangan yang keluar", dan kalimat itu menggambarkan cadangan yang diperiksa di akhir, yang barusan saya tolak sendiri.

Bukti yang benar itu dua function kemarin:

```
ns.n = ketikan  lalu  ns.n = 1        user kalah
ns.n = 1        lalu  ns.n = ketikan  user menang
```

Isinya sama persis, cuma barisnya ditukar, hasilnya beda.

**Nomor 2** benar: `NameError` berarti namanya tidak ada di absen file, `AttributeError` berarti Python sudah masuk ke objeknya lalu tidak menemukan namanya di dalam.

**Nomor 5** benar: yang muncul di `help()` itu docstring, dan yang menulisnya manusia pembuat library.

## Yang mau dicoba

- Jalankan percobaan pytest: satu file berisi `periksa_angka()` dengan `assert 1 == 2` dan `test_angka()` dengan `assert 1 == 1`, lalu ganti nama yang pertama jadi `test_periksa` dan bandingkan hasilnya.
- Lanjut Lecture 9 dari **menit 1:05**.
