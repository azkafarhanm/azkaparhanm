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

## Pelajaran umum Problem Set 5 sejauh ini
- Waktu menulis tes, bayangkan **kesalahan apa yang mungkin dibuat programmer**, lalu buat input yang memberi hasil **berbeda** antara versi benar dan versi salah.
- Nama-nama cek di check50 sudah memberi petunjuk kesalahan apa yang dicari.
- Tes ikut spesifikasi, bukan ikut kode sendiri.
- Logika yang dites harus ada di dalam function yang dites, bukan di `main`.
- Selalu pakai `==` di assert.

## Yang ingin dicoba
- Ganti nama function di `test_bank.py` supaya sesuai dengan yang dites.
- Lanjut soal 3: Re-requesting a Vanity Plate.
- Lanjut soal 4: Refueling (kemungkinan butuh `pytest.raises`).
