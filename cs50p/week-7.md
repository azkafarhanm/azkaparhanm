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

## Yang masih tertunda
- [x] Murojaah materi Hari 1 dan Hari 2, lalu kuis kosakata: selesai 29 Oktober pagi (Kuis Kosakata #6, 30 soal, 83%).
- [x] **Perbaiki `shirt.py` (Pset 6)**: selesai 29 Oktober, tidak submit ulang. Pembahasannya di `pset-6.md`.
- [ ] Lanjut Lecture 7 dari sekitar menit 50: bagian *Case Sensitivity* (`re.IGNORECASE`, `?` untuk bagian opsional), lalu *Cleaning Up User Input*.
