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
