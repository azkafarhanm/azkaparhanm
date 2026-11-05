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


## 4. Um — selesai, check50 dan submit berhasil (3 November 2026)

Soalnya: menghitung berapa kali kata `um` muncul sebagai kata utuh dalam teks. Pencocokan harus mengabaikan perbedaan huruf besar dan kecil. Jadi `um`, `Um`, dan `UM` dihitung; bagian dari kata lain seperti `yummy`, `album`, atau `umm` tidak dihitung.

Soal ini terasa jauh lebih ringan daripada soal Working. Saya membaca ulang permintaan soal dan dokumentasi regex di GitHub serta dokumentasi Python, lalu mencoba pola dan contoh langsung di VS Code sebelum memastikan dengan pytest dan check50.

### Kebingungan 1: bagaimana membedakan kata utuh dari potongan kata?

Awalnya saya berpikir mungkin perlu memakai caret `^` dan dolar `$` untuk melarang karakter sebelum atau sesudah `um`. Namun keduanya menandai awal dan akhir string. Karena `um` bisa muncul di tengah kalimat, keduanya tidak menyatakan batas kata di posisi mana pun dalam teks.

Petunjuk yang saya temukan di dokumentasi `re` adalah word boundary, ditulis `\b`. Pola akhirnya adalah:

`\bum\b`

- `\b` pertama meminta batas kata sebelum huruf `u`.
- `um` mencocokkan huruf yang dicari.
- `\b` kedua meminta batas kata setelah huruf `m`.

Anggap `\b` sebagai penanda di pinggir kata. `um` dihitung kalau tidak menempel pada huruf, angka, atau garis bawah (`_`) di kiri maupun kanannya. Jadi `um,`, `(um)`, dan `um?` dihitung karena tanda baca memisahkannya. `yummy`, `album`, `um7`, dan `um_` tidak dihitung karena `um` menempel pada karakter kata (`\w`). Pemisahnya tidak harus spasi; tanda baca juga bisa.

### Kebingungan 2: apakah fungsi hanya mengembalikan 0 atau 1?

Saya sempat mengira hasilnya 1 kalau `um` ditemukan dan 0 kalau tidak. Duck mengingatkan bahwa fungsi harus menghitung **semua** kemunculan sebagai kata utuh.

Contoh:
- `um, um, um` menghasilkan 3.
- `hello, um, world` menghasilkan 1.
- `yummy` menghasilkan 0.
- `Um, thanks, um...` menghasilkan 2.

Untuk itu, `re.findall` mengumpulkan semua kecocokan, lalu `len(matches)` menghitung jumlahnya. Kalau daftar kecocokannya kosong, panjangnya memang 0. Di kode akhir ada cabang yang mengembalikan `len(matches)` jika ada hasil dan 0 jika tidak ada.

### Kebingungan 3: menerima huruf besar-kecil

Soal meminta pencarian case-insensitive. Artinya pola yang sama harus mengenali `um`, `Um`, `uM`, dan `UM`. Daripada menulis semua variasi huruf di pola, saya menggunakan flag `re.IGNORECASE` pada `re.findall`. Dengan begitu regex tetap ringkas dan pencarian mengabaikan kapitalisasi.

### Error dan percobaan yang membantu

- Saya sempat menulis `re findall(...)` tanpa titik di antara `re` dan `findall`. Python menampilkan `SyntaxError: invalid syntax`. Perbaikannya adalah pemanggilan fungsi melalui modul: `re.findall(...)`.
- Saya mencoba `pytest um.py`. Pytest menjawab “no tests ran” karena file itu berisi program, bukan file tes. Menjalankan `pytest test_um.py` menemukan tes yang benar.
- Tes pertama gagal pada `count("Um, thanks, um...")`: fungsi memberi 2, sedangkan ekspektasi tes saya tertulis 1. Setelah dihitung ulang, ternyata input itu memang memiliki dua kata `um`; ekspektasi yang perlu diperbaiki menjadi 2.
- Saya mencoba `UMMM` dengan mengetiknya di prompt shell, bukan setelah prompt `Text:`. Shell menganggapnya nama perintah dan menjawab `command not found`. Untuk menguji program interaktif, jalankan `python um.py` lebih dulu, kemudian masukkan teks saat diminta.
- Uji manual juga membantu memastikan tanda baca tetap diperbolehkan: `um?` dan `(um)` dihitung, sedangkan `u m` tidak.

### Tes dan hasil akhir

File tes memeriksa beberapa hal terpisah:
- variasi kapitalisasi dan tanda baca;
- lebih dari satu kemunculan dalam satu kalimat;
- potongan `um` yang ada di dalam kata lain, seperti `yummy`;
- `um` yang dikelilingi spasi saja, untuk memastikan solusinya benar-benar memakai batas kata dan tidak hanya mencari pola dengan spasi di kiri-kanan.

Setelah ekspektasi tes diperbaiki, `pytest test_um.py` lulus. Check50 juga lulus semua pemeriksaan, termasuk pemeriksaan bahwa tes dapat menangkap tiga implementasi keliru: menghitung `um` di dalam kata lain, hanya menerima spasi di sekitar `um`, atau tidak mengabaikan kapitalisasi. Setelah itu saya berhasil menjalankan `submit50).

### Yang saya pelajari

- `^` dan `$` menandai tepi seluruh string; `\b` menandai batas kata di mana pun kata itu muncul.
- Batas kata dapat bersebelahan dengan spasi atau tanda baca. Kita tidak harus mensyaratkan spasi di kiri dan kanan.
- `re.findall` berguna untuk menghitung semua kemunculan; `len` menghasilkan jumlahnya, termasuk 0 ketika tidak ada.
- `re.IGNORECASE` menangani variasi kapitalisasi tanpa memperpanjang pola.
- Tes juga perlu diperiksa: kegagalan tadi berasal dari angka ekspektasi yang salah, bukan dari hasil fungsi.
- Membaca dokumentasi, mencoba contoh sendiri di VS Code, lalu membandingkan hasilnya dengan spesifikasi membuat konsep word boundary lebih mudah saya pahami.

## 5. Response Validation — selesai, check50 dan submit berhasil (4 November 2026)

Soalnya: meminta alamat email dari pengguna, lalu mencetak `Valid` jika bentuk alamatnya sah atau `Invalid` jika tidak. Soal melarang penggunaan `re` dan meminta memakai salah satu dari dua library: `validators` atau `validator-collection`. Soal juga menegaskan bahwa program tidak perlu mengecek apakah domain email itu benar-benar ada.

Saya mengerjakan soal ini tanpa CS50 Duck. Saya membaca spesifikasi soal dan dokumentasi library, mencoba program di VS Code, lalu memeriksanya dengan contoh manual, check50, dan submit50.

### Kebingungan dan kesalahan yang saya temui

#### 1. Nama paket yang dipasang berbeda dengan nama yang di-import

Saya mulai dengan perintah:

`pip install validator-collection`

Instalasi berhasil, tetapi kode saya menggunakan:

`import validators`

Saat dijalankan, Python memberi:

`ModuleNotFoundError: No module named 'validators'`

Penyebabnya: `validator-collection` dan `validators` adalah dua paket berbeda. Nama paket yang ditulis ke `pip install` tidak selalu sama dengan nama modul yang dipakai dalam `import`. Dokumentasi keduanya juga menunjukkan cara pemakaian yang berbeda:
- Paket `validators` dipasang dengan `pip install validators`, lalu dipakai dengan `import validators` dan `validators.email(...)`.
- Paket `validator-collection` dipasang dengan `pip install validator-collection`, lalu validator-nya diimpor dari `validator_collection`, misalnya `from validator_collection import validators`.

Kode akhir saya memakai API paket pertama. Jadi perbaikannya adalah memasang paket yang cocok dengan import tersebut. Setelah saya menjalankan `pip install validators`, import berhasil dan program dapat berjalan.

#### 2. Memilih library dan membaca hasil validasinya

Awalnya saya mencoba `validator-collection`, lalu berpindah ke `validators` setelah melihat nama import yang dipakai kode saya. Dokumentasi membantu saya membedakan keduanya, walaupun nama keduanya mirip.

Pada kode akhir:
1. `validators.email(email)` memeriksa bentuk alamat email.
2. Hasil pemeriksaan disimpan dalam `validation`.
3. Kondisi `if validation` memilih tulisan `Valid` atau `Invalid`.

Saya tidak perlu menulis regex sendiri. Ini juga sesuai batas soal yang melarang `re`. Check50 mengonfirmasi bahwa program menggunakan library yang diizinkan dan tidak menggunakan `re`.

#### 3. Mengapa input diproses dengan `strip()`?

Program mengambil teks dengan `input(...)`. Saya menambahkan `.strip()` untuk membuang spasi atau karakter whitespace di awal dan akhir input sebelum memeriksanya. Contohnya, input yang diketik sebagai ` alifsetia@yahoo.edu ` dibersihkan menjadi `alifsetia@yahoo.edu`.

`.strip()` tidak menghapus spasi di tengah alamat. Setelah dibersihkan, nilai yang sama itulah yang diberikan ke `validators.email`.

#### 4. Apa arti “valid” menurut soal?

Yang diperiksa adalah apakah alamat email ditulis dengan bentuk yang diterima validator. Program tidak mencari domain di internet atau mengirim email untuk memastikan alamat itu aktif. Jadi “Valid” pada soal berarti bentuk alamatnya lolos pemeriksaan library, bukan bukti bahwa kotak surat tersebut benar-benar ada.

### Percobaan dan hasil

- Memasukkan `azka` menghasilkan `Invalid`.
- `azka@gmail.com`, `alifsetia@yahoo.edu`, dan `malan@harvard.edu` menghasilkan `Valid`.
- `malan@@@harvard.edu` dan `azka@gmail..com` menghasilkan `Invalid`.
- Check50 lulus semua pemeriksaan: file ada, tidak memakai `re`, memakai salah satu library yang diperbolehkan, dan memberi hasil yang diharapkan untuk beberapa alamat valid dan invalid.
- Setelah check50 hijau, saya menjalankan submit50 dan proses pengiriman selesai.

Saat memasang `validator-collection`, pip juga menampilkan peringatan konflik versi dependency: `compare50` meminta `attrs<21`, sedangkan proses instalasi memasang `attrs 26.1.0`. Instalasi tetap selesai dan check50 untuk soal ini lulus. Ini saya catat sebagai pesan dari lingkungan Codespace yang muncul selama instalasi.

### Rujukan yang saya baca

- [Spesifikasi Response Validation — CS50P](https://cs50.harvard.edu/python/psets/7/response/)
- [Dokumentasi validator-collection](https://validator-collection.readthedocs.io/en/latest/)
- [Dokumentasi validators.email](https://python-validators.github.io/validators/reference/email/)

### Yang saya pelajari

- Periksa dokumentasi untuk mencocokkan nama paket instalasi dengan nama modul dan cara import.
- Dua library dengan tujuan serupa belum tentu punya API atau cara melaporkan hasil yang sama.
- Baca spesifikasi untuk mengetahui batas tugas: di sini cukup memeriksa bentuk email, tidak perlu mengecek keberadaan domain.
- Mencoba beberapa contoh valid dan invalid membantu memastikan program menghasilkan dua keluaran yang diminta.
- Untuk soal ini saya belajar dari spesifikasi dan dokumentasi library, kemudian menguji sendiri program di VS Code.
## Merapikan kode soal 1, 2, dan 3 (5 November 2026)

Setelah semua soal hijau, saya membahas ulang kodenya bersama Claude. Ternyata ketiganya punya penyakit yang sama, dan sebagian sudah saya tulis sendiri di catatan ini tapi belum saya terapkan ke kodenya. Setelah dirapikan, ketiganya check50 hijau lagi dan saya submit ulang.

### Prinsip yang berlaku di ketiga soal

| Prinsip | Maksudnya |
|---|---|
| Kurung untuk yang berubah-ubah | Bagian yang isinya selalu sama tidak perlu ditangkap, cukup diketik langsung sebagai teks |
| Perlu dikelompokkan tapi tidak dipakai | Tulis `(?:...)`, bukan `(...)` |
| Pola yang berulang | Simpan ke variabel, rakit dengan f-string |
| Periksa hasil regex langsung | Jangan menunggu kodenya meledak dulu |
| Alternatif terpanjang di depan | Supaya polanya benar berdiri sendiri |

### 1. NUMB3RS

Yang saya perbaiki:

- Tiga pasang kurung di pola, tidak satu pun isinya saya ambil dengan `group()`. Semuanya jadi `(?:...)`. Kurungnya tetap perlu, karena `{3}` butuh sesuatu untuk dipegang dan tanda pilihan perlu dibatasi — tapi tidak perlu disimpan.
- Walrus `:=` saya pakai untuk menyimpan hasil pencarian ke variabel `ip`, padahal `ip` itu nama parameter yang isinya alamat IP asli. Alamat aslinya jadi tertimpa objek match. Dan hasilnya tidak saya pakai lagi setelah `if`, jadi walrus-nya tidak menyelesaikan masalah apa pun. Saya kira itu bikin kode lebih ringkas, ternyata cuma bikin bingung.
- `if ... return True else return False` jadi satu baris dengan `bool(...)`. Ini pelajaran Pythonic Week 1 yang sudah saya catat tapi belum dipakai.
- `^` dan `$` dengan `re.search` diganti `re.fullmatch`, supaya niatnya langsung terbaca.
- Pola oktet yang ditulis empat kali disimpan ke satu variabel, lalu dirakit dengan f-string. Jebakannya: `{3}` harus ditulis `{{3}}` di dalam f-string.

#### Kebingungan baru: kenapa 200–255 harus dipecah dua?

Naluri saya bilang cukup ditulis angka 2, lalu dua kurung siku berisi 0 sampai 5. Saya pikir hasilnya sama saja. Ternyata itu **too stringent** — terlalu ketat, istilah yang baru keluar di kuis pagi tadi.

```
2[0-5][0-5]   → 206, 217, 238 DITOLAK, padahal semuanya oktet yang sah
2[0-4][0-9]   → 200 sampai 249, satuan bebas
25[0-5]       → 250 sampai 255, satuan dibatasi
```

Sebabnya: batas 5 pada satuan **hanya berlaku kalau puluhannya tepat 5**. Selama puluhannya 0–4, satuannya masih aman sampai 9. Regex tidak bisa menyatakan "tergantung", jadi harus dipecah jadi dua jalur terpisah.

Posisi kurung sikunya supaya tidak tertukar:

```
2  [0-5]  [0-5]
↑    ↑      ↑
ratusan  puluhan  satuan
```

Dan caranya memecah rentang bukan tebak-tebakan. Dua lapis: pecah dulu per **jumlah digit**, lalu untuk yang tiga digit pecah per **digit pertama**, terus sampai tiap kelompok punya batas yang bisa ditulis dengan satu `[ ]`. Bonusnya, `01` dan `007` otomatis ditolak karena kelompok dua digit mewajibkan digit pertama 1–9.

### 2. Watch on YouTube

Bagian ini melengkapi catatan di atas, yang dulu saya susun dari log karena percakapan Duck sudah ter-reset. Empat celah yang baru ketahuan:

| Celah | Akibatnya |
|---|---|
| Titik di `www.` tidak di-escape | Titik artinya karakter apa pun, jadi `wwwXyoutube.com` ikut diterima |
| `.+` di awal terlalu serakah | Bisa menembus tanda lebih-besar dan keluar dari tag iframe, jadi link di elemen lain ikut lolos. Diganti dengan "karakter apa pun kecuali tanda tutup tag" |
| ID video cuma huruf dan angka | ID asli YouTube bisa mengandung tanda hubung dan garis bawah, jadi ID seperti `dQw4w9-Wg_XcQ` terpotong |
| Group terakhir ditangkap tapi tidak dipakai | Sifatnya opsional dan isinya tidak pernah diambil, jadi tidak menjaga apa pun. Dihapus |

Yang paling membuka pikiran: saya menangkap bagian `http` dan `youtu` sebagai group, lalu merakit ulang URL-nya dari potongan-potongan itu. Padahal isi kedua group itu **selalu sama**, apa pun inputnya. Jadi tiga baris perakitan itu cuma cara berputar untuk menulis satu teks tetap.

Ada efek sampingnya juga: input `http://` ikut keluar jadi `https://`. Kebetulan itu yang check50 harapkan, tapi kodenya tidak memperlihatkan niat itu — kelihatan seperti mengikuti protokol aslinya, padahal tidak.

Pertanyaan saya waktu itu: kalau tidak di-capture, bagaimana menyambungnya? Jawabannya ternyata **tidak perlu disambung dari input sama sekali**. Teks tetapnya diketik langsung di f-string, yang diambil dari input cuma ID videonya.

Patokan untuk menentukan mana yang perlu ditangkap, tanyakan ini ke tiap bagian:

> Kalau input-nya ganti video lain, bagian ini ikut berubah atau tidak?

Seperti blangko rapor santri: format "Nama: ___, Juz: ___" sudah tercetak di kertasnya, tidak perlu disalin ulang dari data tiap santri. Yang diambil dari data cuma isian titik-titiknya.

Dari empat group tinggal satu, dan yang satu itu memang satu-satunya bagian yang berubah-ubah.

### 3. Working 9 to 5

| Yang saya tulis | Yang diperbaiki |
|---|---|
| `import sys` | Tidak dipakai, dihapus |
| Kurung non-capturing di sekitar satu kelas karakter | Tidak dipegang pengulang dan tidak membatasi pilihan, jadi tidak perlu kurung sama sekali |
| Penanda AM dan PM dibungkus kurung masing-masing | Cukup satu kurung siku untuk huruf depannya, karena isinya cuma beda satu karakter |
| Kata penghubung di tengah pola ikut ditangkap | Tidak pernah dipakai, dan membuat nomor group waktu kedua bergeser jadi 5, 6, 7 |
| Pola waktu ditulis dua kali | Disimpan ke variabel, dirakit dua kali dengan f-string |
| `matches.group()` dipanggil enam kali di enam baris | Diambil sekaligus dengan `matches.groups()` lalu dibongkar |
| `try/except AttributeError` | Diganti pemeriksaan langsung terhadap hasil regex |
| `\s` sebagai pemisah | Soal minta spasi, sedangkan `\s` juga menerima tab dan baris baru |
| `helper` punya beberapa jalur return | Dirapikan jadi satu `return`, supaya tidak ada jalur yang diam-diam menghasilkan `None` |

#### Kenapa try/except itu kurang tepat

Catatan saya di atas sudah menulis kalimatnya: *"`None` dari regex bukan exception dengan sendirinya. Error muncul saat saya mencoba mengakses group darinya."* Saya paham sebabnya, tapi kodenya belum ikut menyatakan itu.

```
matches = None        ← ini yang terjadi kalau tidak cocok
matches.group(1)      ← None tidak punya method group, jadi meledak
```

`AttributeError` itu cuma **gejala** (symptom, kata dari Week 6). Penyakitnya: input tidak valid. Kode saya berbunyi "coba saja, kalau meledak berarti salah", padahal saya sudah tahu persis kapan tidak cocok — begitu hasil `fullmatch` jadi `None`. Jadi diperiksa langsung saja, jangan menunggu meledak.

Bahayanya kalau pakai `try`: seandainya suatu saat ada `AttributeError` dari sebab **lain** di dalam blok itu, dia ikut tertangkap dan disalahartikan sebagai input tidak valid.

#### Membongkar enam group sekaligus

Ini bukan hal baru, cuma saya belum sadar. Sama persis dengan `name, home = line.rstrip().split(",")` di Week 6.

```python
m = re.fullmatch(r"(1[0-2]|[1-9])(:[0-5][0-9])? ([AP]M)", "9:30 AM")
print(m.groups())
jam, menit, penanda = m.groups()
```

Jumlah penampung di kiri **wajib** sama dengan jumlah kurung di pola. Karena variabel waktu berisi tiga capture dan dirakit dua kali, totalnya enam. Dan di sinilah kata penghubung tadi harus dibuang: kalau ikut tertangkap, isinya jadi tujuh dan saya harus menyediakan satu penampung untuk sesuatu yang tidak pernah dipakai. Kalau jumlahnya tidak cocok, muncul error yang sudah saya kenal:

```
ValueError: too many values to unpack
```

Error yang sama persis dengan alamat Harry berkoma di Week 6.

#### Kode saya selamat bukan karena benar

Alternatif jam saya tulis yang pendek dulu baru yang panjang. Kodenya tetap benar — tapi bukan karena polanya benar, melainkan karena `fullmatch` memaksa regex mundur dan mencoba alternatif berikutnya. Kalau pola itu suatu saat dipakai dengan `re.search` atau `re.match`, jam 12 bisa terbaca jadi 1 tanpa error apa pun. Rinciannya saya tulis di `week-7.md` Hari 6.

### Yang saya pelajari dari merapikan

- Menulis pelajaran di catatan tidak sama dengan menerapkannya ke kode. Tiga hal yang saya perbaiki hari ini sudah tertulis di catatan ini sejak 1 November.
- check50 hijau tidak berarti kodenya sudah benar. Tema lama yang muncul lagi.
- Kurung punya dua tugas terpisah, mengelompokkan dan menangkap. Dulu saya kira cuma satu.
- Kode yang berputar-putar biasanya tanda saya mengambil dari input sesuatu yang sebenarnya tidak pernah berubah.

## Catatan proses belajar

Pada problem set ini saya menggunakan CS50 Duck untuk petunjuk dan pertanyaan pemandu, sesuai aturan CS50P yang saya ikuti. Saya tetap menulis, mengubah, dan menguji kode sendiri.
