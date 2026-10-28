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

### Titik itu "apa saja", bukan titik
- David mencoba menambah `.edu`: `.+@.+.edu`. Masalahnya, `.` di dalam pola berarti **karakter apa saja**, jadi `malan@harvardXedu` (tanpa titik sungguhan, diganti huruf X) tetap lolos.
- Solusi: **escape** dengan garis miring terbalik, `\.`, artinya "titik yang betul-betul titik". Dengan `.+@.+\.edu`, `malan@harvardXedu` ditolak dan `malan@harvard.edu` lolos.
- Muncul masalah baru: di string Python biasa, `\` juga punya arti khusus (misalnya `\n`). Solusinya **raw string**: awali tanda kutip dengan `r`, misalnya `r".+@.+\.edu"`, supaya Python menyerahkan garis miring itu apa adanya ke `re`.
- Analogi: raw string seperti titipan surat tertutup. Python tidak membukanya, langsung diserahkan ke `re`.

### Yang mau dicoba
- `re.search(".+@.+", "@")` dan `re.search(".+@.+", "a@b")`.
- `re.search(".+@.+.edu", "malan@harvardXedu")` lalu bandingkan dengan `r".+@.+\.edu"`.
- Ganti `+` jadi `*` pada pola email, lihat apa yang berubah.

---

## Yang masih tertunda
- [ ] Murojaah materi Hari 1 dan Hari 2, lalu kuis kosakata.
- [x] **Perbaiki `shirt.py` (Pset 6)**: selesai 29 Oktober, tidak submit ulang. Pembahasannya di `pset-6.md`.
- [ ] Lanjut Lecture 7: bagian *Case Sensitivity* (`re.IGNORECASE`, `?` untuk bagian opsional), lalu *Cleaning Up User Input*.
