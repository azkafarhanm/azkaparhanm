# Problem Set 5

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

Sama seperti sebelumnya: petunjuk saat mengerjakan soal saya minta ke CS50 Duck. Claude saya pakai untuk murojaah lecture sebelum mulai, dan untuk membahas setelah submit.

Problem Set 5 bukan soal baru. Saya menulis ulang program dari problem set sebelumnya supaya bisa dites, lalu membuat file `test_...` untuk masing-masing.

## Pemanasan sebelum mulai (19 Oktober 2026 pagi)

Tiga pertanyaan dari Lecture 5, dijawab dari ingatan. Ketiganya benar.

1. **`hello()` pakai print, dites `assert hello("David") == "hello, David"`.** Tanpa return, function tidak "hand off" nilainya, jadi yang diserahkan **None**. Yang dibandingkan: `None == "hello, David"`, hasilnya False, tes gagal.
2. **Kenapa tes dipecah per kategori.** Assert pertama yang gagal me-raise error dan **menghentikan** function itu. Kalau dipecah, setiap kategori dicek sendiri, jadi semua masalah ketahuan sekaligus.
3. **`with pytest.raises(ValueError):`** = selama di dalam blok ini, saya mengharapkan ValueError. Lolos kalau error itu muncul, gagal kalau tidak muncul. Tambahan dari Claude: **gagal juga kalau yang muncul error jenis lain** (misalnya ZeroDivisionError). Lolos hanya kalau jenisnya persis sama.

## 1. Testing my twttr — selesai, check50 hijau semua 8/8 (19 Oktober 2026)

Yang diminta soal: tulis ulang `twttr.py` dari Problem Set 2 dengan function `shorten(word)` yang **me-return** kata tanpa vokal, lalu buat `test_twttr.py` untuk mengetesnya.

### Kebingungan 1: file harus satu folder
- Waktu `from twttr import shorten`, muncul `ModuleNotFoundError: No module named 'twttr'`. Padahal namanya jelas-jelas twttr.
- Ternyata Python mencari file yang di-import **di folder yang sama** dengan file yang dijalankan (dan di tempat library yang sudah diinstal). Folder lain tidak dicari.
- Saya sempat mengubah kode lama di folder `twttr/`. Padahal yang benar: **buat salinan** `twttr.py` di folder `test_twttr/`. Jadi di dalam `test_twttr/` ada dua file: yang dites dan yang mengetes.
- Kode lama yang sudah ter-ubah saya kembalikan dari GitHub me50 (branch `cs50/problems/2022/python/twttr`).

### Kebingungan 2: return di dalam loop
- `shorten("Sy")` malah hasilnya `"S"`. Ternyata return saya taruh di dalam loop, jadi begitu ketemu huruf pertama yang bukan vokal, function langsung berhenti.
- Yang benar: kumpulkan dulu hurufnya di variabel, baru return setelah loop selesai.

### Kebingungan 3: nilai setelah `==` itu output, bukan input
- Saya sempat menulis `assert shorten("SaYa") == "SaYa"`. Saya kira harus sama persis dengan inputnya.
- Ternyata nilai setelah `==` adalah **output yang seharusnya**, yaitu hasil olahan function. `"SaYa"` tanpa vokal ya `"SY"`.
- Sebelumnya juga saya tulis `== "Sy"` untuk semua input. Itu salah, setiap input punya output-nya sendiri.

### Kebingungan 4: check50 "sengaja membuat yang salah"
Ini yang paling lama baru paham.

- Awalnya tes saya cuma `shorten("Sy")`, dan check50 merah banyak: `expected exit code 1, not 0`.
- Kuncinya: **di soal ini yang dinilai bukan `twttr.py` saya, tapi `test_twttr.py` saya.** check50 ingin tahu apakah tes saya pintar menangkap kesalahan.
- check50 punya beberapa `twttr.py` buatannya sendiri: satu versi **benar**, beberapa versi **sengaja dirusak**. Di belakang layar, dia mengganti `twttr.py` saya dengan versi-versi itu, lalu menjalankan **tes saya**.

| Versi `twttr.py` milik check50 | Tes saya harus... | exit code |
|---|---|---|
| Benar | Lolos (hijau) | 0 |
| Rusak, misalnya lupa vokal kapital | Gagal (menangkap kesalahannya) | 1 |

- pytest juga punya exit code seperti `sys.exit` di Pset 4: **0 kalau semua lolos, 1 kalau ada yang gagal**.
- `expected exit code 1, not 0` artinya: versi rusak itu **lolos** dari tes saya, padahal seharusnya ketahuan.
- `"Sy"` tidak punya vokal, angka, atau tanda baca, jadi versi rusak pun tetap mengembalikan `"Sy"`. Sama seperti bug `n + n` yang lolos di angka 2.
- Nama-nama cek check50 itu petunjuk kasus yang harus dites: vokal kecil, vokal kapital, angka, tanda baca, huruf besar.
- Analogi dari Claude: mudir pesantren menguji **ustadz penyimak**. Dia mengirim satu santri yang benar dan beberapa santri yang sengaja salah. Penyimak yang baik harus meluluskan yang benar dan menegur setiap yang salah. **check50 = mudir, versi `twttr.py` = santri, tes saya = ustadz penyimak.**

### Yang saya pahami juga
- `collected 1 item` = satu function tes, berapa pun jumlah assert di dalamnya. Kalau satu assert gagal, yang dinyatakan FAILED adalah **function-nya**, bukan assert-nya.
- Waktu submit, yang dikirim cuma `test_twttr.py`. `twttr.py` tidak dikirim. Itu normal, karena check50 memakai `twttr.py` miliknya sendiri.
- Saya sempat tidak sengaja membatalkan submit dengan Ctrl+C (`Submission cancelled`). Harus dijalankan lagi dan ketik `yes`.

### Bisa nggak satu assert untuk semua kasus?
- Saya kira tidak bisa. Ternyata **bisa**, kalau inputnya satu kalimat yang memuat semua jenis karakter sekaligus.
- Tapi tidak dianjurkan: kalau gagal, tidak ketahuan bagian mana yang salah, dan string panjang rawan salah ketik di tesnya sendiri. Lebih baik per kasus atau per kategori.
- Ibarat ujian tahfidz: bisa saja satu bacaan panjang yang memuat semua hukum tajwid, tapi kalau salah, penguji harus mencari dulu salahnya di hukum mana.

## 2. Back to the Bank — selesai, check50 hijau semua 5/5 (19 Oktober 2026)

Yang diminta soal: tulis ulang `bank.py` dari Problem Set 1 dengan function `value(greeting)` yang **me-return int**: 0 kalau diawali "hello", 20 kalau diawali "h" (tapi bukan hello), 100 selain itu, **case-insensitive**. Lalu buat `test_bank.py` dengan **tiga function tes atau lebih**.

### Kebingungan 1: kurang teliti baca soal, `value` me-return int
- Awalnya `value` saya me-return `"$0"`, `"$20"`, `"$100"` (string pakai dolar), dan tes saya juga membandingkan dengan string itu.
- Anehnya, **pytest di Codespace lolos, tapi check50 merah** di "correct bank.py passes all test_bank checks".
- Sebabnya: **tes saya cocok dengan kode saya sendiri yang salah**, tapi tidak cocok dengan `bank.py` versi benar milik check50 yang me-return int.
- **Pelajaran besarnya: tes harus mengikuti spesifikasi soal, bukan mengikuti kode saya sendiri.** Kalau tes ditulis meniru kode yang salah, tesnya ikut salah dan pytest tetap hijau.
- Tanda `$` itu urusan `main` waktu print. Kita fokus ke function yang dipinjam, dan `value` cukup menyerahkan angka.

### Kebingungan 2: `.lower()` harus di dalam `value`
- Awalnya `.lower()` ada di `main`, di baris input. Program dijalankan biasa memang benar.
- Tapi waktu dites, `value("Hello")` hasilnya 100, bukan 0. Karena **tes memanggil `value` langsung, tanpa lewat `main`**.
- Pelajaran: **semua logika yang mau dites harus ada di dalam function yang dites.** `main` cuma urusan input dan print.
- `.lower()` bisa disimpan dulu di variabel, atau langsung dipakai waktu membandingkan. Dua-duanya benar.

### Kebingungan 3: arti case-insensitive
- Saya kira artinya besar semua atau kecil semua. Ternyata artinya **huruf besar dan kecil dianggap sama**: hello, Hello, HELLO, hElLo semuanya 0.
- Istilahnya **case**, bukan "cash". Case = jenis huruf (uppercase = huruf besar, lowercase = huruf kecil).
- check50 punya `bank.py` rusak yang sengaja dibuat tanpa `.lower()`. Kalau semua input di tes saya huruf kecil, versi rusak itu tetap lolos. Makanya tes harus pakai huruf besar juga:

| Input di tes | Versi benar | Versi rusak (tanpa lower) | Ketahuan? |
|---|---|---|---|
| `"hello"` | 0 | 0 | Tidak |
| `"Hello"` | 0 | 100 | Ya |

### Kebingungan 4: "not allowing for entire phrase"
- **allow for** artinya bukan "menyetujui", tapi **memberi ruang untuk / bisa menerima**. Jadi *"bank.py not allowing for entire phrase"* = bank.py yang **tidak memberi ruang untuk kalimat utuh**.
- Kemungkinan versi rusaknya membandingkan **seluruh** string dengan `==`, bukan pakai `startswith`. Kita tidak bisa melihat kode check50, tapi itu dugaan dari nama ceknya.
  - `startswith`: cukup lihat **awal** kalimat, setelah "hello" boleh ada kata apa pun.
  - `==`: seluruh kalimat harus **persis** "hello", tidak boleh ada kata tambahan.
- Jadi supaya ketahuan, tesnya harus pakai kalimat yang **diawali "hello" lalu ada kata tambahan**. Versi benar memberi 0, versi rusak memberi angka lain.
- Kalimat yang diawali "what's up" tidak bisa menangkap versi rusak itu, karena versi benar dan rusak sama-sama memberi 100.
- Analogi: satpam pesantren yang hanya membuka gerbang kalau tamu mengucapkan **persis** "Assalamu'alaikum". Kalau tamunya bilang "Assalamu'alaikum, Pak, saya mau menjenguk anak saya", satpam itu bingung. Satpam yang benar cukup mendengar **awal** ucapannya.

### Kebingungan 5: assert tanpa `==`
- Saya sempat menulis assert dengan kalimat panjang tapi **lupa `==`**. check50 tetap hijau.
- `assert` sebenarnya cuma bertanya: "apakah yang di kanan saya ini True?" Tanpa `==`, `value(...)` yang hasilnya 100 menjadi `assert 100`.
- Di Python setiap nilai bisa dianggap True atau False (sama seperti `bool(":)")` di murojaah Making Faces):

| Nilai | bool |
|---|---|
| 100, 20 | True |
| 0 | False |
| `""`, None | False |

- Jadi `assert 100` dan `assert 20` sama-sama lolos. Seandainya `bank.py` keliru memberi 20, tes tetap hijau. Tesnya cuma mengecek "bukan nol", bukan angka berapa yang keluar. Seperti ustadz yang cuma bertanya "santri ini membaca sesuatu atau tidak?" tanpa menyimak bacaannya.

### Kebingungan 6: syarat tiga function
- Spesifikasi minta **three or more functions**. Sempat cuma satu function (`test_hello`), yang lain di-comment, tapi check50 tetap hijau.
- Pelajaran lagi: **check50 hijau belum tentu semua aturan soal terpenuhi.** Akhirnya saya pecah jadi empat function.
- Saran Claude (tidak wajib): beri nama function sesuai apa yang dites, bukan nama cek di check50. Misalnya `test_without_case_insensitivity` sebenarnya menguji bahwa case-insensitive berjalan, jadi namanya agak terbalik.

## Pemanasan sebelum mulai (20 Oktober 2026 pagi)

Tiga pertanyaan dari soal kemarin, dijawab dari ingatan. Ketiganya benar, tinggal dipertajam:

1. **Kenapa yang terkirim hanya `test_twttr.py`?** Karena yang dinilai cuma tesnya. `twttr.py` tidak dikirim karena check50 memakai `twttr.py` buatannya sendiri (yang benar dan yang sengaja dirusak).
2. **Assert tanpa `==`.** Saya bilang assert "menyimpan" nilainya seperti boolean. Lebih tepatnya assert **memeriksa** apakah nilainya dianggap True. Akibatnya 100 dan 20 sama-sama lolos, jadi tes tidak bisa membedakan jawaban benar dari jawaban salah.
3. **Kenapa `.lower()` di dalam `value`.** Karena tes memanggil `value` langsung, tanpa lewat `main`. `.lower()` di `main` tidak pernah dijalankan waktu dites.

## 3. Re-requesting a Vanity Plate — selesai, check50 hijau semua 7/7 (20 Oktober 2026)

Dikerjakan **tanpa CS50 Duck**. Saya baca ulang soalnya, lihat lagi logika kode lama (mana yang return False, mana yang return True), dan belajar dari kesalahan soal-soal sebelumnya. Sekarang saya tidak tertipu lagi: fokus ke soal dan ke function yang dipinjam.

Cara saya menyusun tes: pastikan dulu plat yang valid hasilnya True, lalu satu per satu masukkan plat yang melanggar setiap aturan dan harus False. Satu function tes untuk satu aturan, sesuai nama cek di check50 (huruf di awal, panjang, letak angka, angka nol, tanda baca). Panjang plat diuji dua arah: terlalu pendek dan terlalu panjang.

### Kebingungan 1: `OSError: pytest: reading from stdin while output is captured!`
- Jejak errornya: `plates.py:30: in <module> main()`. Begitu tes melakukan `from plates import is_valid`, seluruh `plates.py` dijalankan dari atas, termasuk `main()` dan `input("Plate: ")`. pytest tidak bisa menerima ketikan, jadi error.
- Penyebabnya: penjaga `if __name__ == "__main__":` belum ada di `plates.py`.
- Ini persis catatan Week 5 Hari 1: **penjaga wajib ada di file yang dipinjam.** Sekarang saya merasakan sendiri akibatnya.

### Kebingungan 2: `assert None == True`
- `is_valid("CS50")` me-return None, artinya function selesai tanpa sampai ke `return True`.
- Pelajaran yang sama untuk ketiga kalinya: Making Faces, `hello()`, sekarang `is_valid`. Function tanpa return = None.

### Kebingungan 3: check50 sudah hijau, tapi pytest saya merah
- Urutannya: check50 hijau semua dulu, **baru setelah itu** pytest saya `1 failed` (`None == True`).
- Kuncinya ada di istilah:
  - **Tes** = file `test_....py` yang saya tulis, isinya baris-baris assert. Cuma ada satu.
  - **Penguji** = alat yang menjalankan tes itu. **pytest** menjalankannya pada **kode saya**. **check50** menjalankannya pada **kode milik check50** (versi benar dan versi rusak).
- Jadi tesnya sama, tapi programnya beda, makanya hasilnya bisa beda.

| | Tes saya | Kode saya | pytest | check50 |
|---|---|---|---|---|
| Bank (kemarin) | Salah, ikut kode saya (`"$0"`) | Salah | Hijau (sama-sama salah) | Merah |
| Plates (hari ini) | Benar, ikut soal | Salah (None) | Merah (kesalahan ketahuan) | Hijau |

- Kemarin **tesnya** yang salah. Hari ini **tesnya benar**, yang salah kode saya, dan tes itulah yang memergokinya. Itu fungsi tes yang sesungguhnya.
- Versi benar milik check50 itu sesuai **spesifikasi soal**, bukan sesuai kode saya. Kalau kode saya sudah sesuai soal, **hasilnya** pasti sama (cara penulisan kodenya belum tentu sama). Tes hanya memeriksa hasil, bukan cara kerja di dalam function.

## 4. Refueling — selesai, check50 hijau semua 9/9 (20 Oktober 2026)

Yang diminta soal: `convert(fraction)` menerima **satu** string `"X/Y"` dan me-return persentase (int). Kalau X atau Y bukan bilangan bulat, atau X > Y, raise **ValueError**. Kalau Y = 0, raise **ZeroDivisionError**. `gauge(percentage)` me-return `"E"` kalau ≤ 1, `"F"` kalau ≥ 99, selain itu `"Z%"`.

### Kebingungan 1: pembagian tugas, siapa raise siapa menangkap
- Awalnya saya kira `while True` dan `try/except` ada di dalam `convert`, dan `convert` harus punya dua parameter (X dan Y).
- Ternyata:
  - **`convert`** cukup menerima **satu** string `"X/Y"`, memecahnya sendiri pakai split, mengolah, lalu **raise** kalau tidak valid.
  - **`main`** yang meminta input, **menangkap** error dengan try/except, dan **mengulang** dengan `while True`.
  - **`gauge`** dipanggil oleh `main`, bukan oleh `convert`. `main` yang mengalirkan nilai dari `convert` ke `gauge`, lalu `main` yang print.
- Sempat split dua kali (di `main` dan di `convert`). Cukup sekali, di `convert`.
- Dua jenis error bisa ditangkap sekaligus di `except` pakai tuple: `except (ZeroDivisionError, ValueError):`.

### Kebingungan 2: menulis `raise`
- Saya sempat menulis raise dengan nama error di dalam tanda kutip, dua error sekaligus. Salah tiga hal:
  - Nama error **tanpa tanda kutip**, karena itu nama class, bukan teks.
  - Tanda kutipnya juga tidak lengkap.
  - **Satu `raise` hanya bisa melempar satu error.** Tuple hanya berlaku di `except` untuk **menangkap**, bukan untuk melempar.
- `raise` tidak butuh print di bawahnya, dan tidak bisa berpasangan wajib seperti try/except. Dia bisa berdiri sendiri.
- Hanya satu error yang muncul per eksekusi, yaitu yang pertama terjadi.

### Kebingungan 3: `raise` vs `return`
- Saya kira untuk "mengirim" ValueError harus pakai return.
- `return` = mengirim **nilai** ke pemanggil, ditangkap oleh variabel.
- `raise` = melempar **sinyal error**, ditangkap oleh `except`, tidak butuh return.
- `return ValueError` cuma mengembalikan nama error sebagai nilai biasa, tidak ada except yang terpicu.
- Tanpa raise di `else`, function selesai tanpa return, jadi None. Pelajaran yang sama untuk keempat kalinya.

### Temuan penting: error "naik" lewat rantai pemanggilan
- Saya baru sadar: raise di `convert` bisa ditangkap oleh except di **`main`**, walaupun beda function.
- Error naik mengikuti **siapa memanggil siapa** (call stack): raise di `convert`, `convert` dipanggil `main`, jadi dicari except di `main`. Kalau tidak ada, terus naik. Kalau sampai atas tetap tidak ada, program crash.
- Yang menentukan siapa memanggil siapa, bukan letak function di file. except di `gauge` tidak akan menangkap error dari `convert`, kecuali `gauge` yang memanggil `convert`.
- Nama di `except` harus cocok dengan jenis error yang di-raise.

### Kebingungan 4: lupa tanda kutip di tes
- `convert(2/4)` tanpa tanda kutip: error `'float' object has no attribute 'split'`. Python **menghitung 2/4 dulu** (jadi 0.5), baru hasilnya dikirim ke `convert`.
- `convert(2/0)` tanpa tanda kutip: ZeroDivisionError muncul **di baris tes saya sendiri**, sebelum `convert` dipanggil. `pytest.raises` tetap melihat error itu, jadi tes lolos bahkan pada versi rusak, akibatnya versi rusak **tidak tertangkap**. Makanya check50 sempat merah di "not raising ZeroDivisionError". Setelah pakai tanda kutip (`"2/0"`), errornya muncul **di dalam** `convert`.
- `convert("cat")` tanpa garis miring: pemecahannya gagal di baris pertama `convert`, sebelum sampai pengecekan angka. Versi rusak pun gagal di baris yang sama, jadi tidak ketahuan. Dengan `"cat/2"`, yang benar-benar diuji adalah pengecekan "cat bukan angka".

### Kebingungan 5: apakah `pytest.raises` itu "mandiri"?
- Di `convert` saya tidak ada `raise ZeroDivisionError`, tapi tesnya lolos. Saya kira `pytest.raises` mengangkat error sendiri.
- Ternyata **tidak**. `pytest.raises` hanya **menunggu** apakah ada error. Error bisa muncul dua cara:

| Cara | Contoh | Siapa yang raise |
|---|---|---|
| Otomatis | `int("cat")` jadi ValueError, `3 / 0` jadi ZeroDivisionError | Python |
| Manual | `raise ValueError` waktu X > Y atau negatif | Saya |

- Buktinya: check50 punya versi rusak yang **sengaja tidak** memunculkan ZeroDivisionError, dan tes saya **protes** (gagal) di versi itu. Protes itu justru yang diinginkan check50, artinya versi rusak ketahuan.
- Ibaratnya `pytest.raises` itu **petugas yang menunggu alarm berbunyi**, bukan **orang yang membunyikan alarm**.

### Kebingungan 6: urutan pemeriksaan di `convert`
- Setelah submit, saya jalankan pytest dengan `fuel.py` saya sendiri: `test_ZeroDivisionError` gagal, yang keluar **ValueError**.
- Ditelusuri dengan `"2/0"`: syarat `int(x) > int(y)` diperiksa duluan, 2 > 0 True, langsung `raise ValueError`. Baris pembagian tidak pernah dicapai.
- Saya coba tukar urutan syarat di dalam `if` yang sama, hasilnya tetap ValueError. Karena semua syarat digabung pakai `or`, cukup satu yang True, dan semuanya berujung di satu `else` yang sama. Lagipula tidak ada satu pun yang memeriksa Y = 0 (`y < 0` tidak mencakup nol).
- Yang benar: **pemeriksaan Y = 0 dibuat terpisah, sebelum** pemeriksaan yang lain, dengan raise ZeroDivisionError sendiri. Boleh punya beberapa pemeriksaan, masing-masing dengan raise-nya sendiri.
- `0/0` jadinya ZeroDivisionError, sesuai spesifikasi.
- Ini kasus Plates lagi: **tes saya benar, kode saya yang perlu diperbaiki.**
- Tidak perlu submit ulang, karena yang diubah `fuel.py`, dan file itu tidak ikut dikirim.

### Lain-lain
- `pip paytest` dan `pip pytest` error. pip butuh kata kerja: `pip install pytest`. Tapi di Codespace pytest sudah terpasang, cek dengan `pytest --version`.
- Saran Claude (saya putuskan tidak ditambahkan): tes untuk kasus X > Y, misalnya `"3/2"` harus ValueError.

## Penutup Problem Set 5

Problem Set 5 selesai, keempat soal hijau dan di-submit.

| Soal | check50 |
|---|---|
| Testing my twttr | 8/8 |
| Back to the Bank | 5/5 |
| Re-requesting a Vanity Plate | 7/7 |
| Refueling | 9/9 |

### Pelajaran umum
- Yang dinilai di Pset 5 itu **tes saya**. check50 menjalankannya pada versi benar (harus lolos) dan versi rusak (harus gagal). Mirip mudir yang menguji ustadz penyimak.
- Waktu menulis tes, bayangkan **kesalahan apa yang mungkin dibuat programmer**, lalu buat input yang memberi hasil **berbeda** antara versi benar dan versi salah. Nama-nama cek di check50 sudah memberi petunjuk.
- **Tes ikut spesifikasi soal, bukan ikut kode sendiri.**
- Logika yang dites harus ada di dalam function yang dites, bukan di `main`. `main` cuma urusan input dan print.
- Function yang dites harus **return**, bukan print. Tanpa return = None.
- Penjaga `__name__` wajib di file yang dipinjam.
- Selalu pakai `==` di assert.
- Input di tes harus **string dengan tanda kutip**, supaya yang diuji benar-benar function-nya.
- check50 hijau belum tentu semua aturan soal terpenuhi, dan pytest hijau di kode sendiri juga belum tentu kode itu benar. Dua-duanya perlu dicek.

## Yang ingin dicoba
- Pastikan Vanity Plate sudah di-submit (`submit50 cs50/problems/2022/python/tests/plates`).
- Ganti nama function tes supaya sesuai dengan yang dites (misalnya `test_length`, bukan `test_without_length`).
- Lanjut **Week 6: File I/O**. Di sana `with` akan muncul lagi.
