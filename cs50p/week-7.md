# CS50P Week 7: Regular Expressions

Dua hari pertama Week 7 diisi menonton lecture saja, masing-masing sekitar 10 menit video.

## Hari 1 – 27 Oktober 2026

Mulai Lecture 7, **10 menit pertama**. Ngoding 1 jam, bahasa Inggris 10 menit.

### Masalah: memeriksa apakah teks itu "bentuknya" email
David membuat `validate.py`: minta user mengetik email, lalu program menentukan **valid** atau **invalid**. Percobaannya dari yang paling sederhana, dan setiap percobaan **masih ada celahnya**:

| Percobaan | Aturan | Celah (yang masih lolos) |
|---|---|---|
| 1 | `"@" in email` | Hampir semua teks yang mengandung `@` |
| 2 | ditambah `"." in email` | `@.` (cuma dua simbol) tetap lolos |
| 3 | `split("@")` jadi `username` dan `domain`, username tidak boleh kosong, domain harus ada titik | `malan@harvard` ditolak, tapi masih longgar |
| 4 | `domain.endswith(".edu")` | `malan@.edu` (domain tanpa nama) lolos |

- Setiap kali satu lubang ditutup, muncul lubang baru, dan kodenya makin panjang. Ibarat satpam pesantren yang tiap kali kecolongan ditambah satu aturan lagi, tapi pintunya tetap bisa disiasati.
- Ini sama dengan pelajaran Week 5 dan 6: tes dan aturan harus menutup **kasus aneh**, bukan hanya kasus normal.

### Gagasan: cocokkan pola, bukan satu-satu
- **Regular expression** (disingkat *regex*) = **pola** untuk mencocokkan teks. Bukan bertanya "apakah ada huruf ini?", tapi "apakah teks ini **berbentuk** seperti ini?"
- Analogi: memeriksa kartu santri. Kita tidak peduli nama siapa, yang dicek bentuknya: ada foto, ada nomor induk, ada stempel.
- Di Python dipakai lewat library `re` (*regular expressions*): `import re`.
- `re.search(pola, teks)` mencari apakah **pola** ada di dalam **teks**. Kalau cocok, hasilnya sebuah objek kecocokan (`re.Match`). Kalau tidak cocok, hasilnya `None`. Jadi bisa langsung dipakai di `if`.
- Langkah pertama David: `re.search("@", email)`. Ini baru mencari huruf `@` apa adanya, hasilnya sama dengan `"@" in email`, jadi belum ada kemajuan. Tapi sekarang ada **tempat untuk memasang pola**, dan itu yang dikembangkan di bagian berikutnya.

### Yang mau dicoba
- Ketik ulang percobaan 1 sampai 4 sendiri, lalu uji dengan `@.`, `malan@harvard`, dan `malan@.edu`. Lihat sendiri celahnya.
- Di Python interaktif: `import re`, lalu `re.search("@", "a@b")` dan `re.search("@", "ab")`. Bandingkan hasilnya (objek vs `None`).

---

## Hari 2 – 28 Oktober 2026

Lanjut Lecture 7, **10 menit kedua**. Ngoding 1 jam, bahasa Inggris 10 menit.

### Metacharacter: karakter yang punya arti khusus
- Di dalam pola, sebagian karakter **tidak berarti dirinya sendiri**. Namanya **metacharacter**. Analogi: tanda tajwid di mushaf. Hurufnya sama, tapi tanda di atasnya memberi aturan cara membaca.

| Tanda | Artinya |
|---|---|
| `.` | satu karakter **apa saja** (kecuali pindah baris) |
| `*` | karakter sebelumnya muncul **nol kali atau lebih** |
| `+` | karakter sebelumnya muncul **satu kali atau lebih** |
| `?` | karakter sebelumnya muncul **nol atau satu kali** (boleh ada, boleh tidak) |
| `{m}` | tepat **m** kali |
| `{m,n}` | antara **m** sampai **n** kali |

### `.*@.*` lalu `.+@.+`
- `.*@.*` artinya: apa saja (boleh kosong), lalu `@`, lalu apa saja (boleh kosong). Hasilnya **`@` saja lolos**, jadi belum menutup celah. Di lecture ini dijelaskan lewat diagram kotak dan panah (**state machine**): setiap karakter yang masuk menentukan kita pindah ke "pintu" berikutnya.
- `.+@.+` artinya: **minimal satu** karakter sebelum `@` dan **minimal satu** sesudahnya. Sekarang `@` saja ditolak (`None`), `a@b` lolos.
- Beda `*` dan `+` cuma soal **boleh nol atau tidak**. Itu yang menutup celah tadi.

### Yang mau dicoba
- `re.search(".+@.+", "@")` dan `re.search(".+@.+", "a@b")`.
- Ganti `+` jadi `*` pada pola email, lihat apa yang berubah.

---

## Hari 3 – 29 Oktober 2026

Lanjut Lecture 7 sampai sekitar **menit 50**. Ngoding 2 jam, bahasa Inggris 10 menit. Hari ini paling banyak diskusinya, dan hampir semua konsep saya buktikan sendiri di terminal.

### Pemanasan (murojaah)
Lima pertanyaan dari materi Hari 1 dan 2. Tiga benar, dua perlu dikoreksi.

| Pertanyaan | Jawaban saya | Koreksi |
|---|---|---|
| `endswith(".edu")` masih meloloskan apa? | domain kosong | Benar, contohnya `malan@.edu` |
| `re.search` mengembalikan apa? | string, kalau gagal error | **Salah.** Cocok → objek **Match**, tidak cocok → **`None`**. Tidak ada error |
| Beda `.*@.*` dan `.+@.+` | `*` boleh nol, `+` minimal satu | Benar. Contoh yang beda: `@` saja |
| Kenapa `.+@.+.edu` meloloskan `malan@harvardXedu`? | belum tahu | Dibahas di bawah |
| Kenapa pola pakai `r"..."`? | backslash punya arti khusus | Benar, tapi alasannya saya kira "dianggap satu baris". Bukan itu |

Karena `re.search` mengembalikan objek atau `None`, hasilnya bisa langsung dipakai di `if`. Objek dianggap benar, `None` dianggap salah.

### Kuis Kosakata #6
30 soal sekaligus, karena tiga hari terakhir tidak ada kuis. Hasilnya **83%**, 25 benar 5 salah. Yang salah: *regular expression*, *case-sensitive*, *ambiguous*, *from scratch*, dan *involved* (yang artinya rumit, bukan terlibat). Kelimanya diulang di kuis berikutnya.

### Titik itu "apa saja", bukan titik
- David menambah `.edu` jadi `.+@.+.edu`. Masalahnya `.` di dalam pola berarti **karakter apa saja**, jadi `malan@harvardXedu` (titiknya diganti huruf X) tetap lolos.
- Solusi: **escape** dengan garis miring terbalik `\.`, artinya "titik yang betul-betul titik". Sekarang `malan@harvardXedu` ditolak, `malan@harvard.edu` lolos.
- Saya sempat salah tulis `/` padahal yang dipakai `\` (garis miring **terbalik**, di atas tombol Enter).

### Raw string: ada dua pembaca
Ini yang tadinya saya salah paham. Raw string **bukan** berarti "dianggap satu baris". Yang benar: ada **dua pembaca** yang berbeda.

| Tahap | Siapa yang membaca | Tugasnya |
|---|---|---|
| 1 | **Python** | membaca kode saya, menghasilkan sebuah string |
| 2 | **`re`** | membaca string itu sebagai pola |

- `r` itu urusan tahap 1. `\.` itu pesan untuk tahap 2. Jadi `r` **tidak bisa menggantikan** backslash, karena keduanya bicara ke pembaca yang berbeda.
- Saya buktikan: `r".edu"` masih meloloskan `harvardXedu`. Jadi pakai `r` saja tanpa backslash tidak menyelesaikan apa-apa.
- Gunanya `r` adalah menjaga backslash **sampai utuh** ke `re`. Tanpa `r`, `"\n"` sudah berubah jadi pindah baris sungguhan sebelum sampai ke `re`.
- Analogi: `\.` itu isi suratnya, pesan untuk `re`. `r` itu perintah ke tukang pos supaya suratnya tidak dibuka dan diubah di jalan. Kalau isi suratnya tidak ditulis, mau tukang posnya sejujur apa pun, `re` tetap tidak tahu maksud saya.
- Kalau `\.` ditulis tanpa `r`, Python memberi **SyntaxWarning: invalid escape sequence**. Itu **peringatan, bukan error**, programnya tetap jalan. Artinya `\.` bukan escape sequence yang dikenal Python, tapi dibiarkan apa adanya.
- Escape sequence yang dikenal Python: `\n` (pindah baris), `\t` (tab), `\\` (backslash sungguhan), `\"` (tanda kutip). `\.` tidak termasuk.
- Kesimpulan: **pola regex selalu ditulis `r"..."`**, jangan bergantung pada kebetulan.

### State machine: diagram lingkaran dan panah
Saya awalnya tidak kebayang maksud diagram ini.

| Bentuk | Artinya |
|---|---|
| Lingkaran | satu pos pemeriksaan (namanya *state*, diberi label q1, q2, ...) |
| Panah **melengkung** balik ke lingkaran sendiri | baca satu karakter, lalu **tetap di sini**. Boleh berulang |
| Panah **lurus** ke lingkaran berikutnya | syaratnya terpenuhi, **pindah** pos |
| Lingkaran **dobel** | pos akhir. Kalau teks habis di sini, berarti cocok |

- Jalannya `malan@harvard.edu`: huruf `m`, `a`, `l`, `a`, `n` berputar di panah melengkung, lalu `@` lewat panah lurus dan pindah pos.
- Makanya David bilang *"follow this curved edge up and around"*.
- Beda `*` dan `+` kelihatan dari jumlah lingkarannya: `.*` cukup **satu** lingkaran (boleh nol karakter), sedangkan `.+` butuh **dua** (satu langkah wajib dulu, baru boleh berputar).
- Istilah *nondeterministic finite automaton* yang disebut David itu cuma selingan teori, tidak dipakai di problem set. Analogi saya: setoran hafalan berurutan, harus lewat ayat 1 dulu baru boleh ayat 2, tidak bisa meloncat.

### Tiga lubang yang masih bocor
Setelah polanya jadi `.+@.+\.edu`, ternyata masih banyak yang lolos padahal salah.

| No | Masalah | Contoh yang lolos |
|---|---|---|
| 1 | `@` boleh lebih dari satu | `malan@@harvard.edu` |
| 2 | ada teks nyangkut di belakang | `malan@harvard.edux` |
| 3 | ada kalimat nyangkut di depan | `My email address is malan@harvard.edu` |

**Lubang 1** sebabnya: `.` itu apa saja, dan `@` juga sebuah karakter. Saya bongkar sendiri, ternyata `.+` yang pertama ikut menelan `@` pertama:

| Bagian pola | Menelan |
|---|---|
| `.+` | `malan@` ← `@` pertama termakan di sini |
| `@` | `@` kedua |
| `.+` | `harvard` |
| `\.edu` | `.edu` |

Polanya cuma menuntut "ada minimal satu `@`", tidak pernah bilang "cuma boleh satu `@`". Seperti aturan "santri harus bawa kartu", tidak melarang bawa tiga kartu.

**Lubang 2 dan 3** sebabnya sifat `re.search` sendiri. `search` bertanya "apakah pola ini **ada di dalam** teks?", bukan "apakah **seluruh** teks berbentuk seperti pola ini?". Jadi sisa di depan dan di belakang tidak diperiksa sama sekali. Ibarat satpam yang cuma mengecek "ada kartu yang sah di dalam tas?", begitu ketemu satu dia berhenti memeriksa, isi tas yang lain tidak diurus.

Kenapa ini penting di dunia nyata, kata David: kalau formulir meloloskan kalimat utuh sebagai alamat email, nanti saat hasilnya disalin ke program email (*mailer*), yang masuk kalimat panjang, bukan alamat. Ini relevan kalau nanti saya bikin formulir pendaftaran di TahfidzFlow.

### `^` dan `$`: awal dan akhir
- `^` = cocokkan dari **awal** teks. `$` = sampai **akhir** teks.
- David sendiri mengaku simbolnya aneh, karena `^` dan `$` tidak terlihat sepasang seperti `(` dan `)`. Katanya *"those are the symbols the world chose many years ago"*, jadi memang harus dihafal.
- Cara saya mengingat: `^` seperti panah menunjuk ke atas (ke awal), `$` biasanya ditulis di akhir hitungan seperti total harga.
- Saya sempat bingung: kalau `.+` itu apa saja minimal satu, kalimat `My email address is malan@harvard.edu.` gagalnya di mana? Ternyata **yang menolak bukan `^`, tapi `$`**, dan bukan karena spasi. Spasi tetap diterima `.+`, yang menggagalkan cuma titik nyangkut di ujung.
- Buktinya: begitu titik di ujung dihapus, kalimat panjang itu **lolos lagi**. Jadi `^` dan `$` baru menambal lubang 2, belum lubang 3.

### `..*` ternyata sama dengan `.+`
- Aturan yang baru saya tahu: **tanda pengulang (`*`, `+`, `?`) hanya mengikat satu hal tepat di depannya.**
- Jadi `..*` itu dua potong: titik pertama = tepat satu karakter (wajib, karena tidak ada pengulang di belakangnya), lalu `.*` = nol atau lebih. Dijumlahkan jadi minimal satu, sama persis dengan `.+`.
- Saya uji dan hasilnya identik di semua kasus. Analogi: wajib setor satu ayat, setelah itu boleh nambah berapa pun atau tidak sama sekali.
- `+` itu cuma singkatan yang lebih enak dipakai (*the handier syntax*). `..*` cukup dikenali kalau ketemu di kode orang.
- Aturan "pengulang mengikat satu hal" ini penting: `ab*` artinya `a` lalu `b` berulang, sedangkan `(ab)*` artinya `ab` yang berulang. Kurung dipakai untuk membungkus dulu jadi satu kesatuan.

### Kurung siku: set dan komplemen
| Tanda | Artinya |
|---|---|
| `[ ]` | *set of characters*, daftar karakter yang boleh |
| `[^ ]` | *complementing the set*, semua **kecuali** yang disebut |

- **`^` punya dua arti tergantung letaknya.** Di luar kurung siku dan di awal pola artinya "mulai dari awal". Di **dalam** kurung siku dan di depan artinya "kecuali". Di pola `^[^@]+@[^@]+\.edu$` tanda `^` muncul tiga kali dengan dua arti berbeda.
- `[^@]+` = satu atau lebih karakter yang bukan `@`. Ini menambal lubang 1, karena `@` sekarang dikecualikan.
- **complement** di sini maksudnya komplemen himpunan seperti pelajaran matematika: semua yang di luar himpunan itu. Tetap nyambung dengan arti "melengkapi", karena himpunan digabung komplemennya baru jadi utuh. Analogi absensi: daftar yang hadir dan daftar yang tidak hadir, digabung baru lengkap seluruh santri.
- Ada mahasiswa bertanya: bisakah melarang suatu karakter di **seluruh** teks? David: bisa, tapi merepotkan, karena larangannya harus ditulis ulang di **setiap** kurung siku. Saya buktikan: dengan `[^@ ]` (spasi ikut dilarang) di kedua tempat, kalimat panjang akhirnya ditolak. Lubang 3 tertutup.

### `\w` dan saudaranya
Daripada menyebut yang dilarang, lebih rapi menyebut yang **diizinkan**. `[a-zA-Z0-9_]` bisa dipersingkat jadi `\w`.

| Tanda | Artinya |
|---|---|
| `\w` | *word character*: huruf, angka, dan garis bawah |
| `\d` | digit, angka saja |
| `\s` | spasi dan sejenisnya (termasuk tab dan pindah baris) |

- Kalau hurufnya **besar**, artinya kebalikannya: `\W`, `\D`, `\S`. Jadi huruf besar di sini berfungsi seperti `^` di dalam kurung siku.
- **alphanumeric** = gabungan *alphabet* (huruf) dan *numeric* (angka). Jadi `\w` itu alphanumeric plus underscore.
- Yang **tidak** termasuk `\w`: spasi, titik, koma, `@`, strip, tanda baca lain. Karena spasi tidak termasuk, pola `^\w+@...` otomatis menolak kalimat panjang, dengan cara yang lebih rapi daripada menulis `[^@ ]` berulang-ulang.

### Status ketiga lubang
| No | Masalah | Penambalnya |
|---|---|---|
| 1 | `@` lebih dari satu | `[^@]` atau `\w` |
| 2 | sisa di belakang | `$` |
| 3 | kalimat di depan | `\w` (spasi tidak termasuk) |

### Regex ternyata ada di mana-mana
- **Google Forms**: waktu **membuat** formulir (bukan mengisi), tiap pertanyaan punya menu **Response validation**. Isinya bisa email, URL, panjang teks, dan yang paling canggih **Regular expression**. Jadi saya bisa menulis pola sendiri, misalnya NIS harus 8 angka atau nomor HP harus diawali `08`.
- **VS Code**: `Ctrl+F` lalu klik tombol `.*` (atau `Alt+R`) supaya kotak pencarian dibaca sebagai pola.

Tiga tombol di kotak pencarian VS Code:

| Tombol | Nama | Artinya |
|---|---|---|
| `Aa` | Match Case | membedakan huruf besar-kecil |
| `ab` | Match Whole Word | hanya kata utuh |
| `.*` | Use Regular Expression | kotak dibaca sebagai pola |

Dua kesalahan saya waktu mencoba:
1. Saya ketik `.*` ke dalam kotak pencarian, padahal itu nama tombolnya. Akibatnya seluruh file kuning, karena `.*` cocok dengan **setiap** baris (`23 of 31`).
2. Mencari `sys\.exit\(.+\)` hasilnya **No results**, padahal polanya benar. Ternyata tombol **`ab` masih menyala**. Saat Match Whole Word aktif, VS Code diam-diam menambah syarat "harus kata utuh" di kedua ujung, padahal pola saya berakhir dengan `)` yang bukan huruf, jadi syaratnya tidak akan pernah terpenuhi. Setelah `ab` dimatikan, ketemu **5 hasil**.
- `Ctrl+F` hanya mencari di **file yang sedang terbuka**. Untuk seluruh folder pakai **`Ctrl+Shift+F`**.
- Cara mencari bug di pola: mulai dari yang paling pendek lalu tambah sedikit demi sedikit (`sys` → `sys\.exit` → `sys\.exit\(.+\)`), sampai ketahuan bagian mana yang bikin hasilnya hilang. Sama persis dengan cara mencari bug di kode.

### Kosakata
| Kata | Arti |
|---|---|
| word character | huruf, angka, underscore |
| alphanumeric | gabungan huruf dan angka |
| complement | pelengkap, komplemen (himpunan) |
| compliment | pujian. Beda satu huruf dengan complement, artinya jauh |
| opposites | kebalikan, pasangan berlawanan |
| to exclude | mengecualikan, mengeluarkan dari daftar |
| encompassing | mencakup terlalu luas |
| precise | tepat, presisi |
| mailer | program email seperti Gmail |
| typographical error | salah ketik (disingkat *typo*) |
| to notice | memperhatikan, menyadari sesuatu yang ada di depan mata |
| to realize | menyadari dalam arti baru paham |
| may never have noticed | mungkin belum pernah diperhatikan |
| handier syntax | cara penulisan yang lebih enak dipakai |
| straightforward | sederhana, lugas |
| caret | tanda `^` |

### Yang mau dicoba
- Buat formulir Google Forms percobaan, pasang Response validation dengan regex, misalnya NIS 8 angka.
- Di VS Code coba `Ctrl+Shift+F` dengan regex untuk mencari di seluruh folder `cs50p`.
- Uji sendiri: `\w` menerima apa saja, dan tolak apa saja. Bandingkan dengan `\W`.
- Coba `ab*` dan `(ab)*` untuk membuktikan aturan "pengulang mengikat satu hal di depannya".

---

## Hari 4 – 30 Oktober 2026

Lanjut Lecture 7 dari menit 50 sampai sekitar **menit 1:31** (Walrus Operator). Ngoding 2 jam, bahasa Inggris 10 menit.

### Kuis Kosakata #7
15 soal: lima kata yang kemarin salah (bentuk soal diubah) dan sepuluh kata baru. Hasilnya **15/15**. Mulai hari ini soal kuis diberi nomor, supaya kalau ada yang salah langsung ketahuan nomor berapa.

### Pemanasan (murojaah)
Lima pertanyaan dari materi Hari 3. Tiga benar, dua perlu diluruskan.

| Pertanyaan | Jawaban saya | Koreksi |
|---|---|---|
| `re.search` mengembalikan apa? | objek kalau cocok, `None` kalau tidak | Benar |
| Dua arti `^` | di luar kurung = diawali, di dalam kurung = pengecualian | Benar. Tambahan: `^` berarti "kecuali" hanya kalau letaknya **paling depan** di dalam kurung siku. Di tengah seperti `[a^b]` dia karakter biasa |
| Kenapa `r"..."` saja tidak cukup? | karena `r` dan backslash dua pembaca berbeda | Arahnya benar, tapi saya masih bilang `r` artinya "dianggap satu baris". **Salah.** `r` artinya Python **tidak mengolah backslash**-nya |
| Kenapa `..*` sama dengan `.+`? | titik pertama tidak punya pengait jadi wajib satu, titik kedua pengaitnya `*` | Benar, dan istilah "pengait" ini saya pakai sendiri |
| Isi `\w` | semua karakter **kecuali** digit | **Salah.** Angka justru **termasuk** `\w` |

Koreksi `\w` saya buktikan sendiri:

| Karakter | `\w` | `\d` | `\s` |
|---|---|---|---|
| `a`, `Z` | True | False | False |
| `7` | **True** | **True** | False |
| `_` | True | False | False |
| spasi | False | False | True |
| `.` `@` `-` | False | False | False |

Angka `7` cocok di `\w` **dan** `\d` sekaligus. Jadi `\d` itu **bagian dari** `\w`, bukan dikecualikan. Seperti "santri kelas 7" itu bagian dari "santri", bukan lawannya.

Kalimat pegangan untuk raw string, supaya tidak salah lagi: **"`r` itu bukan soal baris, tapi soal backslash."**

### Kurung: stabilo dan pagar
Bagian ini yang paling lama saya pahami hari ini. Awalnya saya bilang terus terang belum paham, lalu dipecah pelan-pelan.

Kuncinya: selama ini `re.search` cuma saya pakai untuk bertanya "cocok atau tidak". Ternyata regex juga bisa **mengambilkan potongan** teksnya. Caranya, potongan yang mau diambil **distabilo pakai kurung**.

Saya buktikan sendiri di `latihan.py`:

```python
import re
m = re.search(r"(\w+)@(\w+)", "azka@nusaputra")
print(m.group(1))
print(m.group(2))
```

Hasilnya `azka` dan `nusaputra`, terpisah, padahal yang saya kasih cuma satu teks utuh. Istilahnya **capturing**.

Gunanya di dunia nyata: dari teks `Ahmad-7A` bisa langsung dipisah nama dan kelasnya tanpa `split`. Cocok untuk membersihkan data yang masuk berantakan.

Jadi kurung punya **dua tugas**:

| Tanda | Memagari | Bisa diambil? |
|---|---|---|
| `( )` | ya | ya, pakai `.group()` |
| `(?: )` | ya | tidak |

`(?:` itu **satu kesatuan tiga karakter**, bukan tiga tanda terpisah. `?` di situ bukan `?` yang artinya "nol atau satu".

Logikanya: `(` sudah terpakai untuk kurung biasa, jadi perancang regex membuat aturan **`(` lalu `?` = ini kurung jenis khusus**, dan karakter sesudah `?` menyebutkan jenisnya. Jadi `:` cuma label jenis.

Analogi saya sendiri: seperti plat nomor. Huruf F di plat menandakan wilayah Sukabumi, tapi F itu bukan singkatan dari nama kotanya. Cuma kode yang disepakati. Tiga karakter `(?:` juga begitu, tidak punya makna masing-masing.

Satu bukti bahwa `?` di situ bukan `?` biasa: `?` yang biasa selalu menempel pada sesuatu di depannya, padahal di `(?:` yang ada di depannya cuma kurung buka, tidak ada yang bisa diulang.

### Kenapa `|` butuh dipagari
Saya menebak sendiri bahwa pagar itu berguna untuk `|`, dan ternyata benar. Buktinya:

| Teks | `^\w+@\w+\.edu|com$` | `^\w+@\w+\.(?:edu|com)$` |
|---|---|---|
| `azka@nusaputra.edu` | True | True |
| `azka@nusaputra.com` | True | True |
| `com` | **True** | False |
| `ini bukan email com` | **True** | False |

Tanpa kurung, `|` membelah **seluruh pola** jadi dua pilihan: `^\w+@\w+\.edu` **atau** `com$`. Jadi apa pun yang berakhiran `com` lolos lewat pilihan kanan, tidak peduli ada `@` atau tidak.

Kurung di sini jadi **pagar** yang membatasi sampai mana `|` boleh memilih. Mirip tanda kurung di matematika yang menentukan operasi mana dikerjakan duluan.

### Teks biasa itu peka huruf besar-kecil
David mengetik `MALAN@HARVARD.EDU` dan hasilnya **Invalid**, padahal polanya pakai `\w` yang menerima huruf besar maupun kecil. Saya kira `\w`-nya yang bermasalah. Ternyata bukan.

| Pola | Hasil untuk `MALAN@HARVARD.EDU` |
|---|---|
| `^\w+@\w+\.edu$` (edu huruf **kecil**) | **False** |
| `^\w+@\w+\.EDU$` (EDU huruf **besar**) | True |

Biangnya tulisan **`edu`** itu sendiri. Di dalam pola ada dua jenis isi:

| Jenis | Contoh | Peka huruf besar-kecil? |
|---|---|---|
| Simbol / singkatan | `\w`, `\d`, `.`, `+` | tidak |
| Teks biasa | `edu`, `@`, `harvard` | **ya**, harus sama persis |

Prinsipnya sama dengan Linux yang membedakan `HASIL.JPG` dan `hasil.jpg` waktu `shirt.py` kemarin. Komputer tidak menganggap huruf besar dan kecil itu sama kecuali disuruh.

### Flags
**flag** artinya bendera. Di pemrograman, penanda yang dikibarkan untuk menyalakan suatu perilaku. Istilah ini pernah saya pakai sendiri di Vanity Plates dengan sebutan **variabel penanda**.

`flags` juga cuma keyword argument biasa, sama seperti `end=""` di `print`, `reverse=True` di `sorted`, dan `font=` di Figlet.

| Flag | Gunanya |
|---|---|
| `re.IGNORECASE` | abaikan huruf besar-kecil |
| `re.MULTILINE` | `^` dan `$` berlaku **per baris** |
| `re.DOTALL` | `.` ikut mencocokkan pindah baris |

David cuma menampilkan tiga, padahal sebenarnya ada **delapan** (ditambah `ASCII`, `LOCALE`, `UNICODE`, `VERBOSE`, `DEBUG`). Lima sisanya tidak dipakai di CS50P.

`re.DOTALL` menarik karena menghapus pengecualian yang saya catat di Hari 2: `.` itu apa saja **kecuali** pindah baris.

Flag bisa digabung pakai `|`, misalnya `flags=re.IGNORECASE | re.DOTALL`. Perhatikan `|` di sini **bukan** "atau" seperti di dalam pola. Ini `|` milik Python untuk menggabungkan flag. Simbol sama, tempat beda, arti beda, persis seperti `^`.

Contoh MULTILINE yang saya coba:

```
Ahmad 7A lancar
Budi 7B mengulang
Ahmad 8C lancar
```

| | Arti `^` | Hasil `findall(r"^Ahmad.*")` |
|---|---|---|
| Tanpa MULTILINE | awal **seluruh teks** | ketemu 1 |
| Pakai MULTILINE | awal **setiap baris** | ketemu 2 |

Dari situ saya kenal **`re.findall`**, saudaranya `re.search`. Bedanya `search` berhenti di kecocokan pertama, `findall` mengumpulkan **semua** dan mengembalikan list.

### Pola email resmi
David menampilkan regex resmi yang dipakai browser untuk memeriksa kolom email, panjangnya berbaris-baris dan penuh simbol seperti `!#$%&'*+`. Dia bercanda kelihatan seperti orang **swearing** (mengumpat), karena di komik kata kasar memang diganti simbol acak seperti `@#$%&!`. Padahal karakter-karakter itu memang sah secara resmi.

Pelajarannya: pola resminya ada, tapi **tidak perlu dihafal**. Kalau suatu saat butuh validasi email sungguhan, tinggal salin pola yang sudah teruji.

Istilah penting: **syntactically valid** = sah secara **bentuk penulisannya**. Regex cuma bisa memeriksa bentuk, tidak bisa tahu alamat itu benar-benar ada. `tidakada@harvard.edu` bentuknya sah, tapi kotak suratnya mungkin tidak pernah ada.

### `search`, `match`, `fullmatch`
Tiga bersaudara, bedanya cuma soal di mana polanya boleh menempel. Diuji dengan pola `\w+@\w+\.edu` **tanpa** `^` dan `$`:

| Teks | `search` | `match` | `fullmatch` |
|---|---|---|---|
| `malan@harvard.edu` | True | True | True |
| `kirim ke malan@harvard.edu` | True | **False** | False |
| `malan@harvard.edux` | True | True | **False** |

| Function | Mulai dari | Harus habis sampai ujung? | Setara dengan |
|---|---|---|---|
| `re.search` | di mana saja | tidak | pola apa adanya |
| `re.match` | wajib dari awal | tidak | pola dengan `^` |
| `re.fullmatch` | wajib dari awal | **ya** | pola dengan `^` dan `$` |

Jadi pakai `fullmatch` berarti **tidak perlu menulis `^` dan `$`** lagi. Untuk memvalidasi input, `fullmatch` biasanya paling aman.

Ini menyambung ke tiga lubang Hari 3: lubang 2 dan 3 sebenarnya bisa tertutup cuma dengan mengganti `search` jadi `fullmatch`, tanpa menambah simbol apa pun.

Saya sempat mengira `group()` cuma bisa dipakai dengan `re.search`. **Salah.** Ketiganya menghasilkan **objek Match** yang sama, jadi ketiganya punya `.group()`. Ini kembali ke pola Week 6: **panggil function → dapat objek → pakai method-nya.** Yang beda sendiri cuma `re.findall`, karena dia menghasilkan list, bukan objek Match.

### f-string bukan milik `print`
Penemuan saya hari ini. Selama ini f-string selalu saya lihat langsung masuk ke `print`, jadi saya kira menempel di situ. Ternyata dua langkah terpisah:

1. `f"{first} {last}"` **menghasilkan string baru**
2. String itu mau diapakan terserah

```python
nama = f"{first} {last}"
daftar.append(f"{first} {last}")
file.write(f"{first} {last}\n")
return f"{first} {last}"
```

Ini tema yang berulang di catatan saya: banyak hal menghasilkan nilai baru, dan nilai itu harus ditangkap kalau mau dipakai. Sama seperti `ImageOps.fit`, `replace`, dan `strip`.

Istilah menggabungkan string itu **concatenate**. Cara lamanya pakai `+`: `first + " " + last`. Hasilnya sama, f-string lebih enak dibaca.

### Method string tidak mengerti regex
Dugaan saya benar: `split` bawaan string tidak mendukung regex, jadi harus `import re`.

| Teks | `str.split(", ")` | `re.split(r",\s*")` |
|---|---|---|
| `Malan, David` | terbelah benar | terbelah benar |
| `Malan,David` | **tidak terbelah** | terbelah benar |
| `Malan,   David` | terbelah, **spasi ikut terbawa** | terbelah bersih |

`str.split(", ")` mencari persis koma-lalu-satu-spasi. Kalau user mengetik tanpa spasi atau dengan tiga spasi, langsung meleset. `\s*` artinya "spasi, nol atau lebih", jadi ketiganya tertangani sekali jalan.

Polanya, tiap method string punya saudara di `re`:

| Method string | Padanannya di `re` |
|---|---|
| `"x" in teks` | `re.search` |
| `teks.split(...)` | `re.split(...)` |
| `teks.replace(...)` | `re.sub(...)` |

Yang kiri cukup untuk kasus sederhana. Yang kanan dipakai kalau bentuk datanya bisa bermacam-macam, seperti input user yang tidak bisa ditebak.

### Walrus operator `:=`
Saya bertanya: `matches` kan variabel yang belum dideklarasikan, kok bisa langsung dibuat di dalam `if`? Ternyata memang **tidak bisa** pakai `=` biasa. Yang David tampilkan di layar itu justru kode yang **error**, dia sengaja mencoba yang gagal dulu.

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Pesan errornya sendiri sudah menyebut jalan keluarnya.

**Kenapa `=` dilarang di dalam `if`?** Untuk mencegah salah ketik yang berbahaya. Di bahasa lain seperti C, `if (x = 5)` itu sah, padahal maksud orang biasanya `==`. Programnya jalan tapi salah, dan bug begitu sulit dicari. Python melarangnya sama sekali.

| Tanda | Nama | Tugasnya | Boleh di dalam `if`? |
|---|---|---|---|
| `=` | assignment | menyimpan ke variabel | **tidak** |
| `==` | perbandingan | membandingkan dua nilai | ya |
| `:=` | walrus | menyimpan **sekaligus** memakai nilainya | ya |

Jadi kalau betul-betul mau menyimpan di dalam `if`, harus ditulis **terang-terangan** dengan `:=`, bukan diam-diam dengan `=`.

Yang terjadi waktu pakai walrus:

1. `re.search` dijalankan
2. Hasilnya (objek Match atau `None`) disimpan ke `matches`
3. `if` menilai hasil itu: objek dianggap benar, `None` dianggap salah
4. `matches` **tetap hidup** setelah itu

Namanya walrus karena `:=` kalau dimiringkan mirip wajah singa laut dengan dua taring.

### Scope: `if` tidak membuat ruang lingkup baru
Saya bertanya apakah variabel walrus masih bisa dipakai **di luar** `if`. Ternyata bisa.

| Blok | Variabel di dalamnya bocor ke luar? |
|---|---|
| `if`, `for`, `while` | **ya**, tetap bisa dipakai |
| `def` (function) | tidak, hanya hidup di dalam |

Jadi yang membuat ruang lingkup baru cuma **function**. Ini nyambung ke pelajaran *scope* di Week 0.

Tapi ada jebakannya. Waktu polanya **tidak cocok**, variabelnya tetap ada, isinya `None`. Kalau dipakai di luar tanpa dicek dulu, muncul `AttributeError: 'NoneType' object has no attribute 'group'`. Ini keluarga error yang sudah sering saya temui: memanggil method pada `None`.

| Kondisi | Isi variabelnya | Dipakai di luar `if` |
|---|---|---|
| Polanya cocok | objek Match | aman |
| Polanya tidak cocok | `None` | kena `AttributeError` |

Kebiasaan yang aman: **pakai hasilnya di dalam blok `if`**, karena di situ sudah dipastikan bukan `None`. Polanya sama dengan `KeyError` di Week 2: jangan langsung mengambil, pastikan dulu isinya ada.

Untuk sekarang saya pakai cara **dua baris** dulu waktu mengerjakan problem set, karena lebih mudah dibaca ulang saat murojaah dan lebih gampang dilacak kalau error. Walrus cukup dikenali dulu supaya tidak bingung kalau ketemu di kode orang.

### Regex ada di mana-mana (lanjutan)
Ada mahasiswa bertanya: bisakah yang diketik **user** itu justru sebuah regex, bukan teks biasa? David: secara teknis bisa, tapi bukan itu yang dikerjakan di sini.

Contoh nyatanya Google Forms, dan ternyata ada **dua lapis**:

| Lapis | Siapa penggunanya | Dia memberi apa |
|---|---|---|
| Google membuat Google Forms | penggunanya **saya** (pembuat formulir) | saya memberi **regex** |
| Saya membuat formulir | penggunanya **wali santri** (pengisi) | mereka memberi **teks biasa** |

Jadi regexnya mengalir dari saya ke program Google, lalu dipakai memeriksa jawaban orang lain. Misalnya kolom NIS diberi pola `^[0-9]{8}$`, maka yang mengetik `abc` langsung ditolak dan formulirnya tidak bisa dikirim.

Gunanya: **data yang masuk sudah bersih sejak awal**, tidak perlu dibersihkan belakangan.

### Membersihkan data
**canonicalize** = membakukan ke satu bentuk standar. Nama orang bisa ditulis `David Malan` atau `Malan, David`, tapi di database sebaiknya disimpan satu bentuk saja.

| Yang diketik user | Bentuk baku yang disimpan |
|---|---|
| `David Malan` | `David Malan` |
| `Malan, David` | `David Malan` |
| `malan, david` | `David Malan` |

Analogi: **rasm Utsmani**. Satu mushaf baku yang disepakati supaya semua salinan seragam.

Kalau tersimpan campur-campur, pencarian dan pengurutan jadi kacau, dan nama yang sama bisa terbaca sebagai dua orang berbeda. Di TahfidzFlow ini persis masalah yang muncul kalau nama santri diketik beda-beda oleh tiap guru.

### Kosakata
| Kata | Arti |
|---|---|
| flag | bendera; penanda yang menyalakan suatu perilaku |
| swearing | mengumpat, memaki |
| syntactically valid | sah secara bentuk penulisannya |
| too restrictive | terlalu ketat, terlalu banyak menolak |
| excessively long | panjang berlebihan, kepanjangan |
| retool | merombak alatnya, menyesuaikan ulang |
| at our disposal | tersedia untuk kita pakai |
| regression | kemunduran, mundur ke masalah lama |
| preemptively | mendahului, sebelum masalahnya muncul |
| refine | memperhalus, menyempurnakan |
| forge ahead | maju terus, melanjutkan |
| unbeknownst to us | tanpa kita sadari |
| up until now | selama ini, sampai sekarang |
| presumably | agaknya, kemungkinan besar |
| rub someone the wrong way | bikin tidak nyaman, mengganjal |
| canonicalize | membakukan ke satu bentuk standar |
| backwardness | keterbalikan, urutan terbalik |
| concatenate | menggabungkan string |
| alphanumeric | gabungan huruf dan angka |
| non-capturing | tidak disimpan, tidak bisa diambil |

### Yang mau dicoba
- Uji sendiri `re.match` dan `re.fullmatch` dengan pola tanpa `^` dan `$`, bandingkan dengan `re.search`.
- Coba `re.findall` pada teks beberapa baris, dengan dan tanpa `re.MULTILINE`.
- Coba `re.split(r",\s*")` pada nama yang ditulis tanpa spasi dan dengan banyak spasi.
- Buat sendiri contoh walrus, lalu pakai variabelnya di luar `if` saat polanya tidak cocok, dan lihat `AttributeError`-nya.
- Buat formulir Google Forms percobaan dengan Response validation regex, misalnya NIS 8 angka.

---

## Hari 5 – 31 Oktober 2026

Lanjut Lecture 7 dari menit 1:31 sampai **selesai (2:04:59)**. Ngoding 2 jam, bahasa Inggris 10 menit. **Lecture 7 tamat.**

### Kuis Harian #8
Skema kuisnya saya ubah mulai hari ini: bukan kosakata saja, tapi **dicampur konsep dari lecture lama**, supaya materi lama ikut ter-recall dan tidak ditinggal begitu saja. Alasannya sama dengan murojaah hafalan: yang lama perlu disentuh berkala.

Giliran hari ini Week 1 dan Week 5. Isinya 8 kosakata, 4 soal Week 1 (if terpisah vs elif, `case _`, kapan harus pakai if), dan 3 soal Week 5 (pytest tanpa assert, `pytest.raises`, function tanpa return). Hasilnya **15/15**.

### Membebani program, bukan user
David: jangan membebani user dengan aturan ketat. Biarkan dia mengetik sesukanya, **programmer yang membereskan**. Kata kuncinya *take on the burden* = memikul bebannya.

Ini kebalikan dari contoh Google Forms kemarin yang justru **menolak** input salah. Dua-duanya sah, tergantung keadaan:

| Keadaan | Sikapnya |
|---|---|
| Maksud user masih bisa ditebak (URL tanpa `https`) | bereskan sendiri |
| Tidak bisa ditebak (NIS salah ketik) | tolak sejak awal |

### `re.sub`: cari lalu ganti
Bentuknya: `re.sub(pattern, repl, string, count=0, flags=0)`

| Urutan | Nama | Isinya |
|---|---|---|
| ke-1 | `pattern` | yang dicari |
| ke-2 | `repl` | penggantinya |
| ke-3 | `string` | teks yang dikerjakan |
| ke-4 | `count` | berapa kali diganti, bawaan `0` |
| ke-5 | `flags` | bendera, bawaan `0` |

Saya sempat mengira parameter `string` berarti "harus disimpan di variabel dulu". **Bukan.** Itu cuma menyebut jenis isinya, yaitu teks. Boleh ditulis langsung pakai kutip, boleh lewat variabel. Yang menentukan posisinya adalah **urutannya**.

Yang gampang tertukar: **pola di depan, teksnya di belakang.** Sama seperti `re.search(pola, teks)`.

Kalau penggantinya string kosong `""`, efeknya **menghapus**. Jadi `re.sub` juga dipakai untuk membuang, bukan cuma mengganti.

### Jebakan `count=0`
`count=0` **bukan** berarti "tidak ada yang diganti", tapi **"tanpa batas"**, alias semua.

Percobaan saya dengan teks `Ahmad-7A-Juz30-Lancar` yang punya tiga tanda minus:

| count | Yang diganti | Hasil |
|---|---|---|
| tidak diisi (0) | ketiganya | `Ahmad \| 7A \| Juz30 \| Lancar` |
| 1 | minus pertama saja | `Ahmad \| 7A-Juz30-Lancar` |
| 2 | minus pertama dan kedua | `Ahmad \| 7A \| Juz30-Lancar` |

Hitungannya **dari kiri**, bukan pilih-pilih. Jumlah penggantinya selalu sama dengan angka count-nya.

Konvensi `0 = tanpa batas` ini sudah pernah saya temui di Week 6: `loop=0` pada animated GIF artinya **berulang selamanya**, dan angka lain justru membatasi.

### `flags` di `re.sub`
Percobaan `IGNORECASE` dengan teks `Ahmad LANCAR, Budi lancar, Citra Lancar` dan pola `lancar` huruf kecil:

| | Hasil |
|---|---|
| tanpa flags | **cuma punya Budi** yang berubah |
| `flags=re.IGNORECASE` | ketiganya berubah |

Sebabnya pola `lancar` huruf kecil cuma cocok dengan `lancar` huruf kecil. `LANCAR` dan `Lancar` dilewati, karena bagi komputer `L` dan `l` itu dua karakter berbeda. Masalah yang sama dengan `edu` kemarin dan `HASIL.JPG` di `shirt.py`.

Percobaan `MULTILINE` yang paling kelihatan: pola `^` diganti dengan `"- "` pada teks tiga baris.

| | Hasil |
|---|---|
| tanpa MULTILINE | cuma baris pertama dapat `- ` |
| pakai MULTILINE | ketiga baris dapat `- ` |

Ringkasnya: **`count` mengatur berapa banyak, `flags` mengatur cara mencocokkan.**

### Contoh `re.sub` yang saya coba
1. Membuang awalan URL, diganti string kosong.
2. `\s+` jadi satu spasi, untuk merapikan spasi berlebih dari ketikan orang.
3. `\d` jadi `*`, untuk menyensor angka.
4. Membalik urutan tanggal.

Nomor 4 yang paling menarik, karena penggantinya `r"\3-\2-\1"`:

| Bagian pola | Menangkap | Nomornya |
|---|---|---|
| `(\d{2})` | `31` | 1 |
| `(\d{2})` | `10` | 2 |
| `(\d{4})` | `2026` | 3 |

Lalu `\1`, `\2`, `\3` **memanggil kembali** isi kurung itu di dalam string pengganti. Ditulis `\3-\2-\1`, urutannya jadi terbalik: `2026-10-31`.

Jadi kurung yang saya pelajari sebagai **stabilo** bisa dipakai dua arah: diambil lewat `.group()`, atau dipanggil ulang di dalam pengganti `re.sub`. Cocok untuk membakukan format tanggal yang ditulis macam-macam.

### Kenapa `re.sub` tidak pakai `$`
Polanya `^https?://(www\.)?twitter\.com/` memakai `^` tapi **tidak** memakai `$`. Saya uji sendiri kenapa:

| Pola | Hasil untuk `https://twitter.com/davidjmalan` |
|---|---|
| tanpa `$` | `davidjmalan` |
| pakai `$` | **tidak berubah sama sekali** |

Dengan `$`, polanya menuntut teks habis tepat di garis miring. Padahal setelah itu masih ada username, jadi tidak pernah cocok.

| Tujuan | Polanya |
|---|---|
| Memeriksa seluruh teks (validasi) | `^` dan `$` dua-duanya |
| Membuang sepotong bagian | cuma `^`, tanpa `$` |

Kata David: *"I want to tolerate a username there"* — sengaja memberi ruang untuk username. Dan `^` tetap dipakai supaya yang dibuang memang awalan **di depan**, bukan tulisan serupa yang nyempil di tengah.

### Method string tidak mengerti regex
Dugaan saya benar. `str.split(", ")` mencari persis koma-lalu-satu-spasi, jadi gampang meleset.

| Teks | `str.split(", ")` | `re.split(r",\s*")` |
|---|---|---|
| `Malan, David` | benar | benar |
| `Malan,David` | **tidak terbelah** | benar |
| `Malan,   David` | spasi ikut terbawa | bersih |

Tiap method string punya saudara di `re`:

| Method string | Padanannya di `re` |
|---|---|
| `"x" in teks` | `re.search` |
| `teks.split(...)` | `re.split(...)` |
| `teks.replace(...)` | `re.sub(...)` |

Yang kiri mencocokkan **teks apa adanya**, yang kanan mencocokkan **bentuk**.

### Non-capturing menggeser nomor grup
Ini saya sadari sendiri waktu melihat kode David. Ternyata `(?:...)` bukan cuma soal "tidak disimpan", tapi juga **menggeser penomoran**:

| Pola | Hasilnya |
|---|---|
| `(www\.)?twitter\.com/(.+)` | `group(1)` = `None`, username di `group(2)` |
| `(?:www\.)?twitter\.com/(.+)` | username naik jadi `group(1)` |

Jadi itu alasan praktis memakai non-capturing: supaya nomor `.group()` tidak kacau oleh kurung yang sebenarnya cuma pagar. Perhatikan juga `group(1)` bisa berisi `None` kalau kurung opsionalnya tidak terpakai.

### Kurung bersarang
Ada mahasiswa bertanya: kalau ada kurung di dalam kurung, apakah saling mengganggu? Jawab David: tidak masalah.

Penomorannya mengikuti **urutan kurung buka dari kiri**:

| | Isinya |
|---|---|
| `group(0)` | seluruh bagian yang cocok |
| `group(1)` | kurung yang buka paling kiri (terluar) |
| `group(2)`, `group(3)` | kurung-kurung di dalamnya |

Lalu David menyebut ini *the reassuring lesson*: sepanjang apa pun polanya kelihatan, **isinya cuma aturan yang sama diulang-ulang**. Tidak ada simbol baru, cuma dirangkai lebih panjang.

### Usul mahasiswa yang ditolak
Ada yang mengusulkan: `^` dipindah saja ke depan `twitter.com`, lalu urusan protokol dan `www` dibuang. Kelihatannya lebih sederhana. Saya uji dengan pola `^twitter\.com/(.+)$`:

| Yang diketik user | Hasil |
|---|---|
| `twitter.com/azka` | lolos |
| `https://twitter.com/azka` | **ditolak** |
| `www.twitter.com/azka` | **ditolak** |

Sebabnya: `^` bukan berarti "mulai membaca dari sini", tapi **teksnya harus dimulai persis di sini**. Jadi user dipaksa mengetik tanpa `https://`. Itu yang David sebut **regression**, kemunduran.

### Menangani banyak akhiran domain
Pertanyaan saya sendiri: kalau mau menerima `com`, `org`, dan `edu` sekaligus, pakai apa supaya tidak panjang seperti `if` berantai? Ada dua cara, dan saya uji dua-duanya:

**Cara 1, di dalam pola:** `twitter\.(?:com|org|edu)/` — kurung memagari, `|` memilih, `?:` supaya tidak distabilo.

**Cara 2, ambil dulu lalu cek di Python:** polanya `twitter\.(\w+)/`, lalu `if m.group(1).lower() in DIIZINKAN`. Ini yang David sebut *factoring out the logic*.

| Keadaan | Pilih |
|---|---|
| Daftar pendek dan tetap | Cara 1, lebih ringkas |
| Daftar panjang atau bisa bertambah | Cara 2 |
| Daftar datang dari file atau pengaturan | Cara 2 |

Keunggulan cara 2: menambah `.co.id` cukup menambah satu kata di daftar Python, **tanpa menyentuh regex**. Regex yang sering diubah-ubah itu rawan salah.

`in` sudah saya pakai sejak Week 2 untuk mengecek key dictionary. Prinsipnya sama: menanyakan "ada di dalam daftar ini atau tidak". Satu baris, menggantikan `if` berantai yang panjang.

### Kenapa `[a-z0-9_]` masih perlu `+`
Kurung siku cuma menentukan **karakter apa yang boleh**, bukan berapa banyak. Tanpa `+`, yang diterima cuma username satu huruf:

| Nama | tanpa `+` | pakai `+` |
|---|---|---|
| `a` | lolos | lolos |
| `azka` | **ditolak** | lolos |
| `azka_123` | **ditolak** | lolos |

Ini aturan lama: **pengulang mengikat satu hal tepat di depannya.** Di sini "satu hal" itu seluruh kurung siku. Bentuknya sama dengan `\w+` dan `.+`: sebutkan satu karakter dulu, lalu ulang.

Catatan: David menulis `a-z` huruf kecil saja, tapi huruf besar tetap diterima karena ada `re.IGNORECASE` di ujung baris.

### Terlalu longgar dan terlalu ketat
Pola `(.+)` untuk username ternyata **terlalu longgar** (*too generous*), karena `.` menerima spasi dan tanda baca. Menurut dokumentasi Twitter, username cuma boleh huruf, angka, dan garis bawah. Itu **persis isi `\w`**.

Sepanjang lecture ini David bolak-balik mengatur timbangan:

| Istilah | Artinya |
|---|---|
| stringent / restrictive | terlalu ketat, menolak yang seharusnya diterima |
| generous | terlalu longgar, menerima yang seharusnya ditolak |

Membuat pola itu soal mencari titik tengahnya.

### `re.sub` tidak bisa menolak
Bug yang David tunjukkan: user mengetik alamat Google, lalu program mencetak `Username: https://www.google.com/`.

Sebabnya `re.sub` **tidak pernah memberi tahu** apakah dia menemukan sesuatu. Kalau tidak cocok, teksnya dikembalikan utuh, dan program menganggapnya berhasil.

| | Hasilnya | Bisa menolak? |
|---|---|---|
| `re.sub` | selalu string | tidak |
| `re.search` | objek Match atau `None` | **ya** |

Makanya David kembali ke `re.search`, supaya bisa dipakai di `if`. Alasan praktisnya: di backend, username hanya **disimpan ke database** kalau memang cocok polanya. Jangan sampai alamat Google ikut tersimpan.

Dan `re.search` sekaligus bisa **mengambil** username lewat kurung dan `.group()`, jadi satu function mengerjakan dua hal: memeriksa dan mengambil.

### `re.split` dan `re.findall`
Dua function yang disebut sekilas di penutup.

**`re.split`** membelah teks jadi list, dengan pemisah berupa **pola**. Contoh teks berantakan `Ahmad, Budi;Citra   Dadang` yang pemisahnya campur koma, titik koma, dan spasi berlebih: `str.split(",")` gagal, satu pola `re.split` membereskan semuanya.

**`re.findall`** mengumpulkan **semua** yang cocok.

| | Berhenti di mana | Hasilnya |
|---|---|---|
| `re.search` | yang pertama ketemu | objek Match |
| `re.findall` | tidak berhenti | list |

Dari `Ahmad juz 30, Budi juz 29, Citra juz 28`, `search` cuma dapat `30`, `findall` dapat `['30', '29', '28']`.

**Jebakan `findall`:** kurung mengubah isi hasilnya.

| Pola | Hasil |
|---|---|
| `r"juz \d+"` tanpa kurung | `['juz 30', 'juz 29', 'juz 28']` |
| `r"juz (\d+)"` pakai kurung | `['30', '29', '28']` |

Karena hasilnya list, `.group()` **tidak berlaku** di `findall`. Itu satu-satunya yang beda sendiri.

### Rekap enam function `re`
| Function | Tugasnya | Hasilnya |
|---|---|---|
| `re.search` | cari pola di mana saja | objek Match / `None` |
| `re.match` | cari dari awal teks | objek Match / `None` |
| `re.fullmatch` | harus cocok seluruh teks | objek Match / `None` |
| `re.split` | belah teks pakai pola | list |
| `re.sub` | cari lalu ganti | string baru |
| `re.findall` | kumpulkan semua yang cocok | list |

Tiga yang pertama cuma **memeriksa**. Tiga sisanya **mengubah atau mengambil**.

### Cara kerja yang diajarkan hari ini
Beberapa nasihat David yang bukan soal sintaks:

- **chip away at the problems one by one** — selesaikan satu per satu, jangan sekaligus.
- **avoid the inclination to write long regexes all at once** — kalau langsung panjang lalu salah, kita cuma melotot ke layar mencari kesalahannya. Kalau bertahap, kesalahannya ketahuan sejak langkah kecil.
- **stipulate** — sengaja mempersempit masalah dulu. Tanda `?` dan `#` di URL diabaikan untuk sekarang.

Cara bertahap ini sebenarnya sudah saya praktikkan kemarin waktu pencarian VS Code tidak ketemu: naik dari `sys`, lalu `sys\.exit`, baru `sys\.exit\(.+\)`. Dari situ ketahuan tombol `ab` yang jadi biangnya.

### Kosakata
| Kata | Arti |
|---|---|
| burden | beban, tanggungan |
| to take on the burden | memikul beban itu |
| tolerant of | mau menerima, tidak rewel terhadap |
| lend | meminjamkan (lawannya borrow = meminjam) |
| perhaps | barangkali |
| suboptimal | kurang optimal, di bawah yang terbaik |
| critique | mengkritik, menelaah |
| find fault with | mencari kekurangan pada |
| fragile | rapuh, gampang pecah |
| contrive | mengarang, merekayasa skenario |
| chip away at | mengikis sedikit demi sedikit |
| wave my hands at | menjelaskan sekilas lalu melewatinya |
| viable | bisa dijalankan, layak |
| succinct | ringkas, padat |
| explicit | ditulis jelas, gamblang |
| pluck off | memetik, mengambil satu dari sekian |
| mouthful | panjang dan sulit diucapkan |
| reassuring | menenangkan, melegakan |
| to interfere | mengganggu, saling campur |
| admittedly | harus diakui |
| inclination | kecenderungan, dorongan |
| sophisticated | rumit, canggih |
| all at once | sekaligus |
| incrementally | sedikit demi sedikit, bertahap |
| to stare at | melotot, memandangi lama-lama |
| stipulate | menetapkan, menyepakati sebagai ketentuan |
| for simplicity | demi kesederhanaan |
| stringent | ketat, keras aturannya |
| generous | longgar, terlalu banyak menerima |
| trailing | di bagian belakang, di ujung |
| leading | di bagian depan |

Dua kata lama yang muncul lagi: **regression** (kemunduran) dan **stipulate**, yang sudah ada di catatan Week 5.

### Yang mau dicoba
- Jalankan `contoh2.py` lagi, ubah angkanya dan hapus flagnya untuk melihat bedanya.
- Coba `re.sub` dengan pengganti `r"\2 \1"` untuk menukar urutan nama depan dan belakang.
- Coba `re.findall` pada catatan setoran, dengan dan tanpa kurung di polanya.
- Buat formulir Google Forms percobaan dengan Response validation regex, misalnya NIS 8 angka.
- Mulai **Problem Set 7**.

---

## Yang masih tertunda
- [x] Murojaah materi Hari 1 dan Hari 2, lalu kuis kosakata: selesai 29 Oktober pagi (Kuis Kosakata #6, 30 soal, 83%).
- [x] **Perbaiki `shirt.py` (Pset 6)**: selesai 29 Oktober, tidak submit ulang. Pembahasannya di `pset-6.md`.
- [x] **Lecture 7 selesai** (31 Oktober).
- [ ] Mulai **Problem Set 7**.
