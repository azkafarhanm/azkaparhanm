# CS50P Week 5: Unit Tests

## Hari 1 – 16 Oktober 2026

Hari ini capek sekali, baru perjalanan lumayan jauh. Cuma sempat nonton sekitar 8 menit awal lecture, sisanya dipakai bertanya. Paginya juga memperbaiki bitcoin.py dulu (catatannya di pset-4.md).

### Kenapa harus menulis tes?
- Kata David: lebih baik membiasakan diri menulis tes **sejak awal**, selagi programnya masih kecil, daripada nanti sesudah programnya besar dan rumit.
- Ini nyambung dengan pengalaman saya di Pset 4: tiga kali check50 hijau, padahal ada kasus yang tidak dites (figlet tiga argumen, Guessing Game level 0, Little Professor raise). Dengan tes sendiri, kasus-kasus seperti itu bisa ketahuan sebelum submit.

### Mulai dari calculator.py (Week 0)
```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
```
- `square` itu pangkat dua (kuadrat): 2 × 2 = 4, 3 × 3 = 9.
- Sekarang mau dites, tapi bukan dengan menjalankan program lalu mengetik angka manual satu-satu. Dibuat program lain yang khusus untuk menguji.

### Program penguji: test_calculator.py
```python
from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
```
- Ini program yang sama sekali berbeda, yang **satu-satunya tujuannya** (sole purpose) menguji calculator.py.
- `from calculator import square` → meminjam function square dari file lain. Persis pelajaran import dan `__name__` di Week 4.
- Angka 2 dan 3 sudah **ditanam** langsung di kode (baked in / hardcoded).

### Tes itu memeriksa, bukan menghasilkan jawaban
- Saya kira test_square itu "memberikan hasil yang sesuai". Ternyata yang menghitung tetap square. test_square cuma **mengecek**: jawaban square sama tidak dengan yang seharusnya?
- `if square(2) != 4: print(...)`:
  - Kalau square benar → syarat `!= 4` salah → **tidak tercetak apa-apa**.
  - Kalau square rusak → baru muncul pesan `2 squared was not 4`.
- Jadi di tes ini, **diam artinya lulus**.
- Tesnya juga bukan berulang sendiri seperti loop. Jalan sekali setiap kali file tes dijalankan. Istimewanya: bisa diulang kapan saja (misalnya setiap habis mengubah calculator.py), dan pemeriksaannya selalu sama persis.
- Ibarat penguji tahfidz: penguji sudah pegang mushaf, tahu ayat yang benar (4 dan 9). Dia minta santri (square) membaca ayat tertentu (2 dan 3). Kalau benar, penguji diam dan lanjut. Kalau salah, baru ditegur. Penguji tidak ikut membaca, cuma mencocokkan.

### Baked in / hardcoded: bukan berarti tidak bisa diubah
- Saya kira "baked in" artinya kodenya tidak bisa diganggu gugat lagi. **Ternyata bukan.** Kodenya tetap bisa diubah kapan saja, buka file, ganti angkanya.
- Maksudnya: nilainya tidak bisa diubah **dari luar saat program jalan**. Satu-satunya cara mengubah ya mengedit kodenya sendiri.

| Cara | Nilainya dari mana | Untuk menggantinya |
|---|---|---|
| Baked in / hardcoded | ditulis langsung di kode | buka file, edit kodenya |
| `input()` | diketik user saat program jalan | ketik nilai lain, kode tidak disentuh |
| `sys.argv` | diketik di terminal saat menjalankan | ketik `python file.py 5`, kode tidak disentuh |

- Ibarat jadwal pelajaran: hardcoded = jadwal yang dicetak lalu ditempel di dinding, bisa diubah tapi harus cetak ulang. input() = setiap pagi ustadz bertanya ke santri "hari ini murojaah surat apa?".
- Untuk tes, hardcoded justru disengaja. Tes harus memeriksa hal yang sama persis setiap kali dijalankan, supaya kalau suatu hari hasilnya berubah, langsung ketahuan ada yang rusak.
- Contoh hardcoded dari pekerjaan saya sendiri: API key di bitcoin.py.

### Boilerplate dan dua penjaga `__name__`
- **Boilerplate** = kode kerangka baku yang selalu ditulis sama di banyak program, bukan inti programnya. Ibarat kop dan format surat resmi pesantren: selalu ada kop, nomor, salam pembuka, tanda tangan. Isinya yang penting justru di tengah.
- Kata David: banyak dari test_calculator.py ini cuma boilerplate, yaitu `def main()`, pemanggilan test_square di dalamnya, dan `if __name__ == "__main__":`. Intinya cuma test_square.
- Saya bertanya: kenapa file tes juga pakai main dan penangkal `__name__` seperti calculator.py? Saya kira untuk meminjam function tidak harus meniru isi file yang dipinjam. **Dugaan saya benar.**

| | Penjaga di calculator.py | main + penjaga di test_calculator.py |
|---|---|---|
| Wajib? | Ya, penting | Tidak wajib, cuma kebiasaan |
| Gunanya | Supaya waktu square dipinjam, main() milik calculator (yang tanya "What's x?") tidak ikut jalan | Biar rapi dan konsisten |

- Penjaga yang benar-benar dibutuhkan ada di **file yang dipinjam**, bukan di file yang meminjam. Sama dengan percobaan saya di Pset 4: percobaan.py bisa import professor.py tanpa ditanya Level, karena penjaganya ada di professor.py.
- File tesnya bisa saja cukup `test_square()` di paling bawah. Kemungkinan nanti di lecture boilerplate ini dihapus, sesudah dikenalkan alat tes yang bisa menjalankan function `test_...` otomatis.

### Kosakata
| Kata | Arti |
|---|---|
| sooner | lebih cepat, lebih awal (dari soon). Bukan "sonner", itu bahasa Prancis artinya berbunyi/berdering |
| get into the habit | membiasakan diri |
| left off | berhenti di suatu titik untuk dilanjutkan nanti. *Where did we leave off?* = kemarin sampai mana? Ibarat pembatas mushaf |
| purpose | tujuan (kata benda), dibaca *PER-pes* |
| sole purpose | satu-satunya tujuan. sole ≠ soul (jiwa) |
| propose | mengusulkan (kata kerja), dibaca *pro-POUZ*. *Let me propose that we...* = izinkan saya mengusulkan agar kita... |
| on purpose | sengaja |
| bake (into) | arti harfiah memanggang. Kiasan: menanamkan secara permanen ke dalam, seperti telur yang sudah dipanggang dalam kue |
| hardcoded | nilainya ditulis mati di dalam kode |
| boilerplate | kode kerangka baku, selalu sama di banyak program |

### Yang mau dicoba
- Buat calculator.py dan test_calculator.py sendiri, jalankan test_calculator.py. Harusnya tidak keluar apa-apa (diam = lulus).
- Sengaja rusak square (misalnya `n + n`), jalankan tesnya lagi. Pesan mana yang muncul? (Petunjuk: 2 + 2 juga 4.)
- Lanjut lecture dari menit 8.

## Hari 2 – 17 Oktober 2026

Hari ini lanjut lecture 5 dari menit 8 sampai sekitar **menit 25** (bagian pytest). Ngoding 2 jam, bahasa Inggris 35 menit.

### Pemanasan (murojaah)
- Saya sempat bilang API key yang salah itu memunculkan **ValueError**. Ternyata yang muncul **KeyError**.
- **KeyError tidak ada hubungannya dengan API key.** "Key" di sini maksudnya **kunci dictionary**. KeyError muncul kalau kita meminta kunci yang tidak ada di dalam dictionary.
- Di Bitcoin, KeyError bisa muncul karena dua hal:
  1. Kita salah menyebut nama kuncinya di kode (salah ketik).
  2. Server tidak mengirim data yang kita harapkan. Misalnya API key salah, jadi server membalas dengan pesan error, dan kunci yang kita cari tidak ada di balasan itu.
- Pertanyaan saya: data dari API itu selalu sama atau tidak? Jawabannya, **bentuk/strukturnya konsisten** (nama-nama kuncinya sama), tapi **nilainya berubah-ubah** (harga Bitcoin naik turun). Strukturnya baru berubah kalau API-nya ganti versi, seperti CoinCap v2 ke v3.
- Saya juga sempat mengira kalau tes lolos akan "muncul jawaban yang benar". Ternyata **tidak muncul apa-apa**. Diam = lulus (sudah dibahas di Hari 1).

### Kenapa harus ada tes?
- Tes itu untuk menangkap **kecerobohan** kita sendiri, dan juga kesalahan yang muncul **nanti** waktu kode diubah-ubah (oleh kita atau orang lain).
- Kalau `square` diganti jadi `n + n`, hasilnya:

| n | `n * n` (benar) | `n + n` (bug) | Ketahuan? |
|---|---|---|---|
| 2 | 4 | 4 | Tidak, kebetulan sama |
| 3 | 9 | 6 | Ya |
| -2 | 4 | -4 | Ya |
| -3 | 9 | -6 | Ya |
| 0 | 0 | 0 | Tidak, kebetulan sama |

- Jadi satu angka saja tidak cukup. Harus dites dengan **beberapa macam nilai**: positif, negatif, dan nol. Istilah David: **covering your bases**, menjaga semua kemungkinan.
- Nol itu termasuk nilai yang "aneh" (**anomalous**), jadi layak dites tersendiri.
- Kita tidak mungkin mengetes semua angka di dunia. Kita tes beberapa nilai yang mewakili, lalu **ekstrapolasi**: menyimpulkan bahwa angka-angka lain juga benar.

### `assert`
- `assert` itu **keyword** Python. Artinya "saya menegaskan ini benar".
- Kalau benar, tidak terjadi apa-apa. Kalau salah, Python me-*raise* **AssertionError**.
- Saya kira pakai assert + try/except + print itu lebih ringkas. Ternyata **malah lebih panjang**: setiap satu tes butuh sekitar 4 baris (try, assert, except, print). Kalau tesnya puluhan, kodenya jadi panjang sekali. Masalah inilah yang diselesaikan pytest.

### pytest
- Saya kira pytest itu keyword seperti assert. Ternyata **bukan**. pytest itu **program pihak ketiga** (third-party), harus diinstal dulu: `pip install pytest`.
- pytest itu **tool**. Buktinya di terminal kita tidak lagi mengetik `python test_calculator.py`, tapi `pytest test_calculator.py`.
- Tapi pytest **tidak** otomatis mengetes seluruh kode saya. Cara kerjanya:
  1. Membuka file tes yang saya sebut.
  2. Mencari function yang namanya **diawali `test_`**.
  3. Menjalankan function itu satu per satu, mencatat assert mana yang lolos dan mana yang gagal.
- Pertanyaan saya: kalau tidak pakai assert dan tidak ada function `test_`, apakah function saya tetap diuji?

| Keadaan | Hasil pytest |
|---|---|
| Tidak ada function `test_...` | "no tests ran", tidak ada yang dijalankan |
| Ada `test_...` tapi tanpa `assert` | **PASSED**, asal tidak crash. Padahal tidak ada yang dicek! |
| Ada `assert` yang salah, atau crash | **FAILED** |

- Ibaratnya murid setoran hafalan, ustadznya cuma bilang "ya, lanjut" tanpa menyimak. Kelihatan lulus, padahal belum tentu benar. pytest hanya penguji yang **membacakan daftar soal buatan saya sendiri**, dia tidak mengarang soal baru.

### Framework dan library
- pytest disebut **testing framework**. Framework = kerangka. Bedanya dengan library:
  - **Library**: saya yang memanggil kodenya (seperti `requests.get(...)`).
  - **Framework**: saya menulis function, **framework yang memanggil**. Di pytest, saya tidak lagi memanggil `test_square()` sendiri, pytest yang memanggilnya.
- Framework itu untuk **efisiensi**, dan juga memberi **struktur yang sama** untuk semua orang, jadi programmer lain langsung paham aturan mainnya.
- Contoh framework: **Django, Flask, FastAPI** (Python), **Next.js** (JavaScript). Python juga punya alat tes bawaan bernama **unittest**. Sedangkan **Three.js** itu library, bukan framework.
- FastAPI penting untuk AI engineer, karena sering dipakai untuk membuat "loket" (API) yang memanggil model AI.

### Frontend dan backend (pertanyaan soal website 3D saya)
- Saya penasaran: website yang saya buat pakai AI agent kadang butuh gambar 3D. Di Python ada library seperti Three.js atau tidak?

| | Frontend | Backend |
|---|---|---|
| Jalan di mana | Browser pengunjung | Server |
| Bahasa | Hampir selalu JavaScript (plus HTML, CSS) | Bebas, Python sangat bisa |
| Tugasnya | Tampilan, animasi, grafik 3D | Data, database, API key, logika, memanggil model AI |

- Gambar 3D di website **digambar oleh browser**, dan yang **berjalan** di browser itu JavaScript. Jadi untuk 3D di website tetap pakai **Three.js**. Python mengurus belakangnya (Django/Flask/FastAPI).
- Library 3D Python ada, tapi untuk keperluan lain: **Plotly** (grafik 3D interaktif), **Matplotlib** (grafik 3D sederhana), **Blender lewat Python** (membuat model 3D yang nanti bisa ditampilkan pakai Three.js).
- Python tetap bisa membantu tampilan web:
  - **Django/Flask** bisa menyusun halaman HTML di server. Ibarat dapur: yang masak Python, tapi yang disajikan ke tamu tetap HTML biasa.
  - **Streamlit** dan **Gradio**: cukup tulis Python, tampilan webnya dibuatkan otomatis. Sering dipakai AI engineer untuk demo chatbot.
  - **PyScript**: menjalankan Python di browser, tapi masih jarang dipakai.
- Catatan untuk proyek saya: cek ekstensi file. `.js/.jsx/.ts/.tsx` berarti JavaScript/TypeScript, `.py` berarti Python.

### Membaca output pytest yang gagal
Waktu `square` masih `n + n`, assert untuk `square(2)` lolos, tapi `square(3)` gagal. Saya bingung, kenapa -2 tidak ikut dilaporkan error?

- Jawabannya ada di pelajaran **raise**: assert yang gagal me-*raise* AssertionError, dan **function langsung berhenti**. Baris -2, -3, 0 di bawahnya **belum sempat dicek**, bukan lolos.
- Ibarat ujian tahfidz: begitu salah di ayat ketiga, ustadz bilang "stop, ulang". Ayat setelahnya tidak disimak dulu.

| Bagian output | Artinya |
|---|---|
| `F` | Satu function tes gagal (Failed) |
| `>` | Panah menunjuk baris yang gagal |
| `E assert 6 == 9` | Yang dibandingkan ternyata 6 dengan 9 |
| `E + where 6 = square(3)` | Angka 6 itu berasal dari `square(3)` |
| `test_calculator.py:5` | Gagalnya di baris 5 |
| `1 failed in 0.03s` | Ringkasan: 1 tes gagal |

- Baris `E` itu sebenarnya sangat membantu: `where 6 = square(3)` membuat saya sadar 3 **ditambah** 3, bukan **dikali** 3.

### Setelah diperbaiki: kenapa lolos padahal ada angka negatif?
- Saya kaget waktu hasilnya `1 passed`, padahal ada tes angka negatif.
- Ternyata bug-nya sudah diperbaiki jadi `n * n`, dan **negatif kali negatif = positif**: (-2) × (-2) = 4, (-3) × (-3) = 9. Semua assert benar.
- Angka negatif di tes bukan untuk membuat tes gagal, tapi untuk **memastikan function tetap benar walaupun diberi angka negatif**.
- `1 passed` artinya **satu function tes** yang lolos (bukan satu assert). Kelima assert di dalamnya semua dijalankan. Titik `.` = satu tes lolos, kebalikan dari `F`.

Kode tes dari lecture:

```python
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```

### Menguji input aneh: `square("cat")`
Ada dua hal berbeda yang harus dipisahkan:

| | Siapa yang "iseng" | Ditangani di mana |
|---|---|---|
| Input salah dari user | User mengetik "cat" | **Program saya**, pakai `try`/`except` (seperti di pset). Di calculator.py, `int(input())` yang error duluan, jadi "cat" tidak sampai ke square |
| Function diberi input aneh | **Programmer** memanggil `square("cat")` langsung | **File tes**, untuk mengecek reaksi function |

- `assert square("cat") == ...` sama dengan apa? Tidak ada jawabannya, karena `"cat" * "cat"` tidak menghasilkan nilai, Python langsung raise error.
- Jadi pertanyaan tesnya diubah. Bukan "hasilnya berapa?", tapi **"apakah error yang muncul sudah tepat?"**

| Tes biasa | Tes input aneh |
|---|---|
| Berharap hasil 4 | Berharap **muncul error jenis tertentu** |
| Gagal kalau hasilnya bukan 4 | Gagal kalau **tidak ada error**, atau **errornya jenis lain** |

- Ibarat menguji alarm kebakaran asrama: sengaja diberi asap, tesnya lolos kalau alarm **berbunyi**. Asapnya = "cat", bunyi alarmnya = error yang tepat.
- Kenapa jenis error penting? Seperti di Bitcoin: kalau saya menulis `except RequestException` tapi yang muncul KeyError, program tetap crash. Programmer yang memakai function saya perlu tahu pasti error apa yang akan muncul.
- Tebakan saya: `"cat" * "cat"` memunculkan **TypeError**, karena string tidak bisa dikali string. **Tebakan saya benar.**

| Error | Masalahnya | Contoh |
|---|---|---|
| TypeError | **Jenis** datanya tidak cocok untuk operasi itu | `"cat" * "cat"` |
| ValueError | Jenisnya cocok, tapi **isinya** tidak bisa dipakai | `int("cat")` |

- Uniknya, `"cat" * 3` tidak error, hasilnya `"catcatcat"` (string diulang 3 kali).

### Kosakata
| Kata | Arti |
|---|---|
| so to speak | bisa dibilang begitu, istilahnya |
| covering your bases | menjaga semua kemungkinan |
| extrapolate | menyimpulkan hal yang lebih luas dari beberapa contoh |
| manner | cara |
| there's no science to it | tidak ada rumus pastinya, pakai perkiraan saja |
| anomalous | aneh, menyimpang dari biasanya |
| glass half full / half empty | melihat dari sisi positif / negatif |
| framework | kerangka kerja; saya tulis function, framework yang memanggil |
| edge case | kasus pinggiran, nilai-nilai ujung yang rawan salah |
| essence | inti, hakikat |
| cross my fingers | semoga berhasil (seperti "bismillah, semoga lancar") |
| arcane | rumit dan misterius, hanya dipahami orang yang sudah biasa |
| somewhat | agak |
| encouraging | memberi semangat |
| odds are | kemungkinan besar |
| the light bulb goes off | "lampu di kepala menyala", tiba-tiba paham. *Go off* di sini artinya menyala |

### Yang mau dicoba
- Ganti nama `test_square` jadi `cek_square`, jalankan `pytest test_calculator.py`. Muncul "no tests ran"?
- Kembalikan namanya, hapus semua assert, jalankan lagi. Hijau padahal tidak mengecek apa-apa?
- Coba di terminal Python: `"cat" * 3` dan `"cat" * "cat"`.
- Lanjut lecture dari menit 25: lihat bagaimana David menulis tes untuk TypeError.

## Hari 3 – 18 Oktober 2026

Lanjut lecture 5 dari menit 25 sampai **selesai** (50:53). Lecture 5 tamat.

### Pemanasan (murojaah)
1. **Tes tanpa assert.** Saya jawab: berbahaya karena kelihatan lulus padahal kebenarannya belum dicek. Betul. Yang perlu diluruskan:
   - pytest **tidak diam**. Dia terang-terangan melapor **`1 passed`** warna hijau. Itu justru jebakannya.
   - Kalau assert gagal, peringatannya **bukan lewat print**. Assert gagal me-*raise* AssertionError, lalu pytest yang menampilkan laporan merah. Cara pakai print itu cara lama sebelum ada pytest.
2. **Assert kedua gagal, yang di bawahnya dicek atau tidak?** Saya jawab tidak. Betul. Tapi alasannya bukan karena pytest "sengaja mencari error pertama dulu", melainkan **mekanisme raise**: AssertionError di-raise, function langsung berhenti.
3. **`int("cat")` dan `"cat" * "cat"`.** ValueError dan TypeError, betul. Catatan: string **bisa** dikali bilangan bulat (`"cat" * 3`). Yang tidak bisa itu string dikali **string**.

### Tes dipecah per kategori
- Lima assert yang tadinya di satu `test_square`, dipecah jadi tiga function: `test_positive`, `test_negative`, `test_zero`.
- Kenapa? Assert gagal hanya menghentikan **function itu saja**. pytest tetap memanggil function tes yang lain. Jadi semua masalah ketahuan dalam **sekali jalan**, tidak perlu bolak-balik perbaiki satu, jalankan lagi, ketemu yang berikutnya.
- Ibarat ujian tahfidz yang dibagi per juz: salah di juz 1, penguji tetap lanjut ke juz 2 dan juz 3. Di akhir kelihatan juz mana saja yang perlu diperbaiki.

**Arti tanda di output pytest** (catatan di buku saya: "F" dan "."):

| Tanda | Artinya |
|---|---|
| `.` | Satu function tes **lolos** |
| `F` | Satu function tes **gagal** (Failed) |
| `...` + `3 passed` | Tiga function tes, semuanya lolos |
| misalnya `F..` | Satu gagal, dua lolos |

- Yang dihitung itu **function tes**, bukan jumlah assert.

### Menguji error yang diharapkan: `with pytest.raises(...)`

Kode dari lecture:

```python
import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
```

- **`with`** itu **keyword** Python. Untuk sekarang cukup saya pahami sebagai **"selama berada di dalam blok ini"**. Baris yang menjorok di bawahnya diawasi. Nanti dibahas lagi di Week 6 (membuka file).
- **`pytest.raises(TypeError)`** bukan keyword, tapi **function milik pytest**. Artinya: "di blok ini saya **mengharapkan** muncul TypeError."
- Ibarat pengawas di pintu ruang ujian: "selama di dalam ruangan ini, saya menunggu satu hal, yaitu TypeError." `square("cat")` adalah yang terjadi di dalam ruangan.
- Sebenarnya mirip try/except: kalau TypeError muncul, berarti sesuai harapan, lulus. Kalau tidak ada error, gagal.

| Yang terjadi di blok `with` | Hasil |
|---|---|
| Muncul **TypeError** | PASSED, error-nya ditangkap pytest, tidak crash |
| **Tidak ada** error | FAILED: `DID NOT RAISE <class 'TypeError'>` |
| Muncul error **jenis lain** | FAILED |

- Saya sempat bingung: hasilnya `4 passed` hijau semua, berarti tidak ada error dong? Ternyata **TypeError-nya memang benar-benar terjadi**, tapi karena sudah diharapkan, dihitung lulus. Jadi hijau artinya **"semua yang terjadi sesuai harapan"**, bukan "tidak ada error".
- Contoh gagal: kalau square masih bug `n + n`, `"cat" + "cat"` malah **tidak error** (hasilnya `"catcat"`), jadi pytest bilang DID NOT RAISE.
- Jangan tertukar:
  - `raise` (keyword) = **membuat** error.
  - `pytest.raises` (function pytest) = **mengecek** bahwa error memang muncul.
- Di sini pytest dipakai dua cara sekaligus: sebagai **tool** di terminal, dan sebagai **library** yang di-import (`import pytest`).

### hello.py: print vs return
- Function-nya `def hello(to="world")`. Saya sempat salah paham: saya kira tes `hello("David") == "hello, David"` membandingkan "hello world" dengan "hello David".
- Ternyata `"world"` itu **nilai default (cadangan)**, hanya dipakai kalau tidak ada argumen:

| Pemanggilan | Isi `to` | Yang dicetak |
|---|---|---|
| `hello()` | `"world"` | hello, world |
| `hello("David")` | `"David"` | hello, David |

- Lalu kenapa tesnya tetap tidak works? Karena `hello` pakai **print**, bukan **return**. Ingat murojaah Making Faces: function tanpa return mengembalikan **None**. Jadi yang dibandingkan: `None == "hello, David"`, hasilnya False.
- **print** = menulis ke layar, untuk dilihat **manusia**. **return** = menyerahkan hasil, untuk dipakai **kode lain**. Tes itu "kode lain", jadi hanya bisa memeriksa yang di-return.
- None itu bukan string kosong `""`. None tetap sebuah nilai (amplop kosong yang tetap sampai), jadi `None == ""` juga False.
- Tebakan saya sebelum David memperbaiki: return di hello, print dipindah ke main, tambah assert di tes. **Tebakan saya benar.** Koreksi kecil: tanpa return, assert bukan "tidak menangkap", tapi **menangkap nilai yang salah** (None).
- Pola penting: **function yang mudah dites adalah function yang me-return hasilnya.** Urusan print diserahkan ke main.

Kode dari lecture setelah diperbaiki:

```python
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
```

### Mengetes pakai loop
Catatan di buku saya: "function bisa juga ngetesnya pakai loop."

```python
def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
```

- Satu assert diulang untuk tiga nama, jadi tidak perlu menulis tiga assert terpisah.
- Tetap dihitung **satu tes**, karena masih di dalam satu function. Bersama `test_default` hasilnya `2 passed`.
- Tapi David mengingatkan: tes sebaiknya **sederhana dan kecil**. Kalau kode tesnya rumit, **tesnya sendiri bisa salah** (flawed), lalu kita butuh tes untuk tes, dan tidak akan ada habisnya. Tujuannya: siapa pun, termasuk saya sendiri, cukup **melihat sekilas (eyeball)** dan langsung yakin tesnya benar.
- Ibarat penguji hafalan: kalau penguji sendiri tidak lancar, siapa yang menguji pengujinya?

### Pertanyaan mahasiswa soal recursion
- Ada yang bertanya: function di dalam function, atau rekursi, bisa dites juga? Jawab David: **bisa, caranya sama persis**. Panggil function-nya, cek hasilnya dengan assert. Tes tidak peduli *bagaimana* function bekerja di dalam, hanya peduli hasilnya.
- **Recursion** = function yang memanggil dirinya sendiri, dan harus punya **base case** (titik berhenti). Saya sudah sempat ketemu ini di kuliah kompleksitas algoritma. Tanpa base case, Python akhirnya menyerah dengan `RecursionError`.
- Rekursi **tidak** dibahas khusus di CS50P. Adanya di CS50x (minggu Algorithms). Kemungkinan akan muncul lagi di mata kuliah Algoritma dan Struktur Data.

### Package dan `__init__.py`

| Istilah | Wujudnya | Analogi |
|---|---|---|
| function | Satu bagian kode yang punya nama | Satu bab |
| module | Satu file `.py` | Satu kitab |
| package | Satu folder berisi beberapa module + `__init__.py` | Satu rak berisi kitab-kitab satu rumpun |

- **`__init__.py`** biasanya **sengaja dikosongkan**. Gunanya sebagai **penanda** bahwa folder itu package, ibarat **label nama di rak**. Boleh juga diberi isi: kodenya dijalankan pertama kali waktu package di-import. **init** = *initialize*, menyiapkan.
- Namanya harus **persis** `__init__.py`: dunder-nya, kata init-nya, dan .py-nya. `init.py`, `__mulai__.py`, `__Init__.py` tidak dikenali. Nama berpola `__...__` itu nama khusus milik Python, disebut **dunder** (*double underscore*), sama seperti `__name__` dan `__main__`. Ibarat lafaz azan: kalimatnya sudah ditetapkan, kalau diganti orang tidak mengenalinya sebagai azan.
- Tanpa `__init__.py`, Python versi baru sering masih bisa import folder itu, tapi bisa membingungkan (misalnya pytest bermasalah kalau ada dua file tes bernama sama di folder berbeda). Kebiasaan yang aman: pasang `__init__.py`.
- Kata *package* sudah muncul di Week 4, tapi maknanya "paket yang diinstal pakai pip". Sekarang pengertian teknisnya: folder berisi module. Dua-duanya nyambung, karena paket seperti requests memang berbentuk folder.
- Tidak semua yang di-import itu package. `requests` itu folder (ada `__init__.py`), sedangkan `random` cuma satu file `random.py`.
- Penutup lecture: `pytest test` (test = nama folder) membuat pytest **otomatis mencari semua tes** di folder itu.

### Kesimpulan lecture
- Daripada mengetes manual satu per satu atau menunggu orang lain menemukan kesalahan, lebih baik tulis tes sekali, lalu jalankan berulang kali dengan satu perintah.
- Tapi tes **tidak menjamin** kode bebas error selamanya. Tes itu **jaring pengaman**: setiap kali kode diubah, jalankan tes lagi. Jaringnya hanya sekuat kasus yang saya tulis (ingat `n + n` yang lolos di 2 dan 0).

### Kosakata
| Kata | Arti |
|---|---|
| intertwined | saling terjalin, saling terkait |
| honestly | jujur saja |
| incredibly painful | sangat menyiksa, sangat merepotkan |
| pow | power = pangkat. `pow(2, 3)` = 8, `pow(n, 2)` sama dengan `n * n` |
| in large part because | sebagian besar karena |
| operate on | bekerja pada, memproses |
| integer | bilangan bulat |
| rewind | memutar mundur |
| stipulate | menetapkan, menegaskan sebagai hal yang disepakati dulu (seperti syarat dalam akad). Dibaca *STIP-yu-leit* |
| recursion | function yang memanggil dirinya sendiri |
| compelling | sangat meyakinkan, punya alasan kuat |
| flawed | cacat, mengandung kesalahan |
| eyeball (kata kerja) | melihat sekilas lalu langsung menilai, cukup dengan mata |
| reasonable | wajar, masuk akal |
| yourself included | termasuk dirimu sendiri |
| granted | memang sih, diakui (mirip *admittedly*) |
| take for granted | menganggap sesuatu sudah biasa, sampai tidak menghargainya |

### Yang mau dicoba
- Di terminal Codespace, cek `__file__` beberapa library. Tebak dulu: folder atau satu file?
  - `python -c "import requests; print(requests.__file__)"`
  - `python -c "import random; print(random.__file__)"`
  - lalu coba `emoji` dan `pyfiglet` dari Pset 4.
- Latihan setelah Week 5: tulis function rekursif faktorial sendiri, lalu tes pakai pytest, termasuk base case-nya.
- Mulai **Problem Set 5**. Buka dulu halaman soalnya untuk melihat soal apa saja.
