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
