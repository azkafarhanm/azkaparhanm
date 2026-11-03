# CS50P Problem Set 7: Regular Expressions

## 1. NUMB3RS — selesai, check50 hijau 15/15 (1 November 2026)

Soalnya: memeriksa apakah sebuah teks berbentuk alamat IPv4 yang sah, yaitu empat oktet bernilai 0–255 yang dipisahkan titik.

### Pelajaran terbesar
**Regex memeriksa bentuk, bukan nilai.** Rentang `0-255` tidak bisa ditulis langsung. Harus dipecah dulu per jumlah digit, lalu per digit:

| Kelompok | Polanya |
|---|---|
| 0–9 | `[0-9]` |
| 10–99 | `[1-9][0-9]` |
| 100–199 | `1[0-9][0-9]` |
| 200–249 | `2[0-4][0-9]` |
| 250–255 | `25[0-5]` |

Hampir semua kebingungan saya hari ini berakar dari sini.

### Kebingungan dan koreksinya
| Yang saya kira | Yang benar |
|---|---|
| `[10-99]` bisa berarti angka 10 sampai 99 | Kurung siku cuma **satu karakter**. `[10-99]` dibaca sebagai pilihan karakter, bukan rentang angka |
| `|` bisa dipakai di dalam kurung siku | Di dalam `[...]`, `|` jadi karakter biasa. Untuk "atau" perlu kurung biasa |
| `[1-9]{2}` cocok untuk angka dua digit | `{2}` memaksa kedua digit punya rentang sama, jadi `10` ditolak |
| `[1-9]+` bisa membatasi | `+` tidak membatasi, `123456789` tetap lolos |
| `[1-9]|[0-9]` artinya dua digit | `|` artinya **pilih salah satu**, bukan berdampingan |
| Oktet tidak boleh `0` | Boleh. `192.168.0.1` sah |
| `\.{3}` artinya grup diulang tiga kali | Artinya **tiga titik berturut-turut** |
| Escape pakai `/` | Pakai garis miring **terbalik** `\.` |

### Menyusun strukturnya
Empat oktet berarti **tiga titik**, bukan empat. Percobaan saya berurutan:

1. `(oktet){4}\.{3}` → titiknya menumpuk di ujung, bukan di antara oktet
2. `(oktet\.){4}` → muncul **titik ekstra** setelah oktet terakhir
3. `(oktet\.){3}oktet` → benar

Satu jebakan lagi: di `([0-9]|...|25[0-5]\.)`, titiknya cuma menempel pada alternatif **terakhir**, karena `|` membelah sampai batas kurung. Perlu kurung ganda supaya titik berlaku untuk semua pilihan.

### Error yang saya temui
- `IndentationError: unexpected indent`
- `SyntaxError: unmatched ')'` dan `unterminated string literal`
- `TypeError: search() missing 1 required positional argument: 'string'` — lupa menulis argumen kedua
- `assert` saya kira nama library, ternyata **keyword bawaan** Python

### Cara debug yang lebih enak
Dulu saya mengomentari baris satu per satu untuk menguji pola. Ternyata tidak perlu:

- Ketik `python` di terminal untuk masuk **REPL** (mode interaktif), lalu `from numb3rs import validate` dan panggil langsung. Bisa begitu karena ada penjaga `__name__`, jadi `input()` tidak ikut jalan.
- `Ctrl+/` di VS Code menjadikan **beberapa baris sekaligus** sebagai komentar.
- Kalau filenya diubah, keluar dulu dari REPL dengan `exit()`, lalu masuk lagi.

### Merapikan kode
- Nama `ip` sempat saya pakai dua kali, sebagai parameter dan sebagai hasil pencarian. Membingungkan.
- Walrus `:=` tidak perlu di sini, karena hasilnya cuma dicek sekali dan tidak dipakai lagi.
- `if ... return True else return False` bisa dipadatkan jadi satu baris, karena hasilnya sudah berupa benar/salah. Ini pelajaran **Pythonic** dari Week 1.
- Pola oktet yang sama ditulis empat kali bisa disimpan ke satu variabel, lalu dirakit dengan f-string. Hasil rakitannya **sama persis**, jadi `re` tidak tahu bedanya. Yang berubah cuma kemudahan saya mengubahnya nanti.

### Yang saya pelajari
- Regex mencocokkan **pola karakter**, bukan nilai angka.
- Kurung siku menentukan **karakter apa**, pengulang menentukan **berapa banyak**.
- Empat bagian dipisah titik berarti tiga pemisah, bukan empat.
- REPL plus penjaga `__name__` jauh lebih cepat daripada mengomentari kode.

## 2. Watch on YouTube — selesai, check50 hijau semua (2 November 2026)

Soalnya: mengambil URL video YouTube dari atribut src elemen iframe, lalu mengubahnya menjadi link pendek youtu.be. Kalau masukan tidak berisi URL YouTube yang benar di dalam iframe, fungsi harus mengembalikan None.

Percakapan dengan CS50 Duck sudah ter-reset. Jadi bagian ini saya susun dari log terminal, kode akhir yang tersimpan, dan hasil check50. Saya tidak bisa memastikan semua pertanyaan yang dulu saya ajukan; catatan ini fokus pada kesalahan yang terlihat dan cara saya memperbaikinya.

### Kebingungan dan kesalahan yang terlihat

#### 1. Mengambil group saat regex tidak menemukan kecocokan

Saat saya memasukkan URL biasa seperti http://youtube.com/embed/... atau iframe yang src-nya mengarah ke situs lain, regex tidak menemukan pola yang dicari. Hasil re.search saat tidak cocok adalah None. Karena itu, pemanggilan matches.group(1) menimbulkan:

`AttributeError: 'NoneType' object has no attribute 'group'`

Awalnya program langsung mengambil group seolah-olah kecocokan pasti ada. Solusinya adalah memeriksa matches lebih dulu. Jika tidak ada kecocokan, parse mengembalikan None; kalau ada, barulah group URL digunakan.

#### 2. URL hasil gabungan kehilangan tanda pemisah

Dalam salah satu percobaan, hasilnya menjadi:

`http://youtu.bexvFZjo5PgG0`

Domain dan ID video menempel karena garis miring setelah domain belum ikut dirangkai. Hasil yang diinginkan punya pemisah:

`https://youtu.be/xvFZjo5PgG0`

Ini mengingatkan saya bahwa saat bagian URL dibentuk dari beberapa group regex, setiap karakter yang tidak berasal dari group—seperti `s://`, `.be/`, dan garis miring sebelum ID—harus ditambahkan secara sengaja.

Saya juga sempat menghasilkan `http://youtu.be/...`. Kode akhir mengambil awalan `http` dari URL yang ditemukan, lalu menambahkan `s://`, sehingga hasil akhirnya memakai HTTPS baik ketika masukan memakai HTTP maupun HTTPS. Ini sesuai hasil yang diperiksa check50.

#### 3. Group ID terlalu pendek atau terlalu panjang

Saat menguji HTML iframe lengkap, satu hasil ikut membawa teks atribut setelah URL seperti `title`, `frameborder`, dan `allowfullscreen`. Di percobaan lain, hasil ID-nya hanya `xv`, padahal ID lengkapnya `xvFZjo5PgG0`.

Keduanya menunjukkan batas pola belum tepat:
- Jika bagian setelah ID ikut tercocokkan, hasil URL mencakup sisa HTML.
- Jika pola ID terlalu sempit, group berhenti sebelum seluruh ID tertangkap.

Di kode akhir, pola untuk ID menerima satu atau lebih karakter huruf besar, huruf kecil, atau angka, lalu pola ditutup pada batas URL/atribut berikutnya. Prinsip yang saya pelajari: group harus menangkap seluruh nilai yang dibutuhkan dan berhenti sebelum teks yang bukan bagian nilai itu.

#### 4. Menemukan URL saja belum cukup

Check50 menunjukkan dua syarat tambahan:
- URL YouTube harus menjadi nilai atribut `src`, bukan sekadar muncul di tempat lain dalam HTML.
- URL itu harus berada di dalam elemen `iframe`, bukan di teks atau elemen lain.

Pada pemeriksaan awal, kasus URL di luar `src` dan di luar iframe masih diterima. Setelah pola diperketat, kasus di luar `src` lulus lebih dahulu, sedangkan kasus di luar iframe masih gagal. Beberapa perubahan kemudian sempat membuat URL valid ikut menghasilkan None. Saya perlu menjaga dua sisi sekaligus: menerima variasi URL yang sah dan menolak URL yang berada di konteks yang salah.

#### 5. Memahami pola regex dari group hasilnya

Kode akhir menggunakan group terpisah untuk bagian protokol, nama `youtu`, dan ID video. Bagian-bagian itu kemudian disusun ulang menjadi URL pendek. Membaca nomor group saja terasa membingungkan; lebih mudah bila setiap group dihubungkan dengan bagian konkret dari input:
- group 1: bagian `http`
- group 2: teks `youtu`
- group 3: ID video

Teks tetap seperti `s://`, `.be/` ditambahkan di antara group. Dari log, saya sempat lupa atau keliru menaruh sebagian pemisah itu.

### Perjalanan check50

- Awalnya beberapa variasi iframe valid lolos, tetapi URL di luar `src` dan di luar iframe belum ditolak.
- Setelah perubahan, kasus URL di luar `src` sudah tertangani, tetapi link di luar iframe masih ditemukan.
- Saat pola diperketat, sebagian URL valid sempat tidak cocok dan menghasilkan None.
- Pada percobaan terakhir, semua pemeriksaan lulus: URL HTTP, HTTPS, dan www; iframe dengan satu atau banyak atribut; iframe tanpa link YouTube; salah ketik pada link; serta link yang muncul di luar `src` atau di luar iframe.

### Pelajaran dan solusi yang saya bawa

- Cek apakah hasil pencarian regex ada sebelum memanggil `.group()`; hasil tidak cocok adalah None.
- Saat menggabungkan URL, tulis dan cek kembali pemisahnya satu per satu.
- Tentukan dengan jelas karakter apa yang boleh menjadi bagian ID video dan kapan group itu harus berhenti.
- Validasi lokasi URL, bukan hanya bentuk URL-nya: harus menjadi nilai `src` dalam iframe.
- Setelah mengubah regex, jalankan kembali kasus valid dan invalid. Perbaikan untuk satu kasus bisa membuat kasus lain gagal.
- Check50 memberi contoh konkret tentang syarat yang belum terpenuhi. Saya bisa memakai nama pemeriksaannya untuk mencari kelas input yang perlu diuji, lalu mengecek perilaku program sendiri.

Catatan ini merangkum hal yang tampak dari log dan kode akhir. Rincian diskusi Duck yang tidak terekam masih bisa saya tambahkan kalau nanti saya ingat kembali.

## 3. Working 9 to 5 — selesai, check50 hijau semua (2 November 2026)

Soalnya: mengubah dua waktu dari format 12 jam menjadi format 24 jam. Contoh `9 AM to 5 PM` menjadi `09:00 to 17:00`. Menit boleh tidak ditulis; jika tidak ada, hasilnya `:00`. Format atau nilai waktu yang tidak sah harus menghasilkan `ValueError`.

Saya mengerjakannya dari pagi sampai sore menjelang Maghrib, dengan jeda karena juga menjalankan tugas sebagai asisten guru dan guru tahfiz. Percakapan Duck sudah ter-reset, tetapi log terminal, kode akhir, dan tangkapan layar file tes membantu saya mengingat kembali bagian yang membingungkan.

### Kebingungan dan kesalahan yang saya temui

#### 1. Berapa yang ditambahkan untuk PM?

Saya sempat memperkirakan jam PM perlu ditambah 13. Contoh sederhana membetulkan hitungan itu: jam 1 PM harus menjadi 13, jadi 1 ditambah 12. Aturannya:
- AM selain 12: jam tetap.
- 12 AM: menjadi 00.
- PM selain 12: tambahkan 12.
- 12 PM: tetap 12.

Kesalahan awalnya adalah belum memeriksa aturan dengan contoh batas. Solusinya: uji setiap cabang dengan angka yang mudah diverifikasi, terutama 12 AM, 12 PM, 1 PM, dan 1 AM.

#### 2. Membandingkan AM/PM dari hasil regex

Saya sempat bingung apakah hasil `matches.group(...)` bisa dibandingkan langsung. Bisa: group berisi string seperti `"AM"` atau `"PM"`, jadi dapat dibandingkan menggunakan `==`. Di kode akhir, group penanda disimpan ke variabel `penanda1` dan `penanda2`, lalu diberikan bersama jam ke fungsi pembantu `helper`.

Pemisahan ke `helper(jam, penanda)` menghindari menulis aturan AM/PM dua kali. Fungsi itu mengembalikan jam dua digit sebagai string; setelah itu `convert` merangkai jam dan menit untuk waktu awal serta akhir.

#### 3. Menyusun pola regex untuk jam dan menit opsional

Regex perlu mengenali rentang waktu lengkap, bukan sekadar menemukan potongan yang mirip. `re.fullmatch` dipakai agar seluruh input harus sesuai susunan: jam, menit opsional, penanda AM/PM, kata `to`, lalu bagian waktu kedua.

Menit opsional menjadi kebingungan tersendiri:
- `9 AM` sah tanpa menit.
- `9:00 AM` sah dengan menit.
- `9:60 AM` tidak sah karena menit hanya boleh 00 sampai 59.

Tanda titik dua dan dua digit menit perlu menjadi satu kelompok opsional. Kalau hanya tanda titik duanya yang opsional, pola dapat menerima bentuk yang tidak lengkap; kalau seluruh bagian tidak opsional, input tanpa menit ikut ditolak. Batas digit menit di pola membuat 60 tidak cocok.

#### 4. Mengapa muncul AttributeError?

Pada input yang tidak sesuai pola, `re.fullmatch` mengembalikan `None`. Kode saya lalu mencoba menjalankan `matches.group(1)`, padahal `matches` bukan objek hasil pencocokan. Error yang muncul:

`AttributeError: 'NoneType' object has no attribute 'group'`

Solusinya adalah menangani keadaan saat tidak ada kecocokan dan mengubahnya menjadi `ValueError`, sesuai kontrak fungsi. Kode akhir menangkap `AttributeError` yang timbul ketika group diminta dari hasil None, lalu menaikkan `ValueError`.

#### 5. Mengapa `raise "ValueError"` salah?

Saya pernah mencoba menaikkan nama exception sebagai string. Python menjawab:

`TypeError: exceptions must derive from BaseException`

`raise` membutuhkan kelas atau objek exception, bukan teks biasa. Perbaikannya adalah `raise ValueError`. Ini berbeda dari mencetak tulisan “ValueError”: yang satu benar-benar melempar exception dan dapat diuji pytest, yang lain hanya menghasilkan teks.

#### 6. Memperbaiki format menit dan titik dua

Saya sempat menghasilkan `0900` tanpa titik dua, lalu `09::00` dengan titik dua ganda. Akar masalahnya: kadang nilai menit yang disimpan sudah berisi tanda titik dua, tetapi saat dirangkai saya menambahkan tanda itu lagi atau tidak menambahkannya sama sekali.

Pada kode akhir, group menit yang cocok mencakup tanda titik dua beserta menitnya, misalnya `:30`. Jika group itu kosong/None karena menit tidak ditulis, saya mengisinya dengan `:00`. Dengan demikian output dapat dirangkai secara konsisten sebagai jam hasil konversi ditambah string menit.

#### 7. Salah memahami pesan check50 tentang tes

File tes pada tangkapan layar menguji contoh valid dan invalid. Untuk input invalid, tiap pemanggilan fungsi dibungkus dalam `with pytest.raises(ValueError)` tersendiri. Awalnya saya menaruh beberapa pemanggilan dalam satu blok. Begitu pemanggilan pertama melempar ValueError, Python keluar dari blok itu, sehingga pemanggilan berikutnya tidak ikut diuji. Solusinya: satu blok `pytest.raises` untuk setiap input yang diharapkan gagal.

Pesan seperti “catches working.py not raising ValueError” juga sempat membingungkan. Check50 menjalankan tes saya pada versi program yang sengaja diubah agar salah. Tes saya harus gagal pada program rusak itu supaya membuktikan bahwa tes mampu menangkap masalahnya. Jadi:
- program benar + tes benar → tes lulus;
- program sengaja rusak + tes cukup kuat → tes gagal, dan itu berarti pemeriksaan check50 untuk kemampuan tes berhasil.

Pemeriksaan “hours off by one” dan “minutes off by five” memakai gagasan yang sama: apakah tes saya akan mendeteksi jika hasil konversi dibuat meleset?

### Hasil pengujian

- Contoh valid tanpa menit dan dengan menit menghasilkan format `HH:MM`.
- Input dengan menit di luar 00–59 ditolak.
- Format keliru, pemisah yang salah, atau jam di luar rentang tidak cocok dan harus menghasilkan `ValueError`.
- Awalnya beberapa pemeriksaan check50 untuk kekuatan tes belum lulus. Setelah setiap input invalid diberi pemeriksaan sendiri dan tes diperbaiki, check50 terakhir lulus semua.
- Tangkapan layar tes menunjukkan empat contoh valid serta tiga contoh invalid: menit 60, pemisah `-` menggantikan `to`, dan format waktu 24 jam yang tidak sesuai format input soal.

### Yang saya pelajari

- Contoh batas membantu memeriksa aturan konversi, khususnya 12 AM dan 12 PM.
- Regex memvalidasi susunan karakter dan rentang menit; hasil pencocokan tetap perlu diperiksa sebelum group dipakai.
- `None` dari regex bukan exception dengan sendirinya. Error muncul saat saya mencoba mengakses group darinya; fungsi lalu perlu mengubah input yang tidak cocok menjadi `ValueError`.
- Nilai yang disimpan untuk menit harus punya format konsisten agar tanda titik dua tidak hilang atau ganda.
- Setiap kasus exception perlu diuji sendiri supaya tidak terlewat.
- Check50 tidak hanya memeriksa fungsi konversi, tetapi juga apakah tes buatan saya mampu menemukan beberapa jenis bug.
## Catatan proses belajar

Pada problem set ini saya menggunakan CS50 Duck untuk petunjuk dan pertanyaan pemandu, sesuai aturan CS50P yang saya ikuti. Saya tetap menulis, mengubah, dan menguji kode sendiri.
