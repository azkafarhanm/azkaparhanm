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

## 2. Watch on YouTube — selesai (1 November 2026)

Soalnya: mengambil link video dari potongan HTML `<iframe>` milik YouTube, lalu mengembalikannya dalam bentuk link pendek `youtu.be`. Kalau yang diberikan bukan iframe YouTube, kembalikan `None`.

(Pembahasan lengkap menyusul.)

## 3. Working 9 to 5 — selesai, check50 hijau semua (2 November 2026)

Soalnya: menerima rentang waktu seperti 9 AM to 5 PM, lalu mengubah kedua waktunya dari format 12 jam ke format 24 jam. Menit boleh tidak ditulis; jika tidak ada, hasilnya 00. Input yang format atau nilainya tidak sah harus menghasilkan ValueError.

Saya mengerjakan soal ini dari pagi sampai sore menjelang Maghrib, dengan jeda-jeda karena juga menjalankan tugas sebagai asisten guru dan guru tahfiz. Rasanya cukup lama, tetapi saya menyelesaikannya sendiri lewat percobaan di terminal, membaca error, dan meminta petunjuk bertahap ke CS50 Duck.

### Kebingungan 1: aturan konversi AM dan PM
- Saya sempat berpikir waktu PM harus ditambah 13. Setelah dicek dengan contoh, ternyata jam 1 PM harus menjadi 13:00, jadi yang ditambahkan adalah 12.
- Saya perlu membandingkan penanda yang ditangkap regex dengan string AM atau PM. Hasil matches.group(...) bisa disimpan di variabel, lalu dibandingkan dengan ==.
- Ada kasus khusus: 12 AM menjadi 00; 12 PM tetap 12; jam PM selain 12 ditambah 12; jam AM selain 12 tetap.
- Memisahkan konversi satu jam ke fungsi pembantu membuat aturan ini lebih mudah dilihat dan dipakai untuk waktu awal maupun akhir.

### Kebingungan 2: menyusun regex dan menangani menit opsional
- Saya mulai dari pola untuk jam, menit, AM/PM, kata to, lalu waktu kedua. re.fullmatch membantu memastikan seluruh masukan cocok dengan format, bukan hanya sebagian.
- Menit boleh tidak ada (9 AM), tetapi kalau tanda titik dua muncul, dua digit menit harus ikut ada. Saya belajar mengelompokkan bagian titik dua dan menit sebagai satu grup opsional: keduanya muncul bersama atau sama-sama tidak ada.
- Batas menit bisa dibatasi di regex ke 00–59. Karena itu 9:60 AM tidak cocok dengan pola.
- Kalau regex tidak cocok, re.fullmatch menghasilkan None, sehingga memanggil .group() langsung akan menimbulkan AttributeError. Masukan yang tidak cocok harus diubah menjadi ValueError.
- Saya sempat menulis raise "ValueError". Ternyata raise harus diberi objek exception, bukan string. Bentuk yang benar adalah menaikkan ValueError.

### Kebingungan 3: merangkai output dengan menit
- Kalau menit tidak diberikan, hasilnya tetap harus memiliki menit 00.
- Saya sempat mendapatkan output tanpa titik dua (0900) dan dengan titik dua ganda (09::00). Penyebabnya adalah saya belum konsisten apakah nilai menit sudah menyertakan tanda titik dua.
- Setelah menentukan bentuk nilai menit secara konsisten, saya bisa merangkai jam hasil konversi dan menit menjadi format HH:MM untuk masing-masing waktu.

### Kebingungan 4: apa yang sebenarnya diuji oleh pytest dan check50?
- Untuk memeriksa exception, pytest.raises(ValueError) harus mengelilingi pemanggilan fungsi yang memang diharapkan gagal.
- Setiap kasus invalid perlu punya blok with pytest.raises(...) sendiri. Begitu satu pemanggilan melempar exception, baris berikutnya dalam blok itu tidak dijalankan.
- Saya awalnya bingung membaca pesan check50 seperti “catches ... not raising ValueError”. Check50 sengaja menjalankan tes saya terhadap versi program yang dimodifikasi dan rusak. Tes yang baik harus gagal pada versi rusak itu, dan lulus pada program saya yang benar.
- Pemeriksaan “off by one” dan “minutes off by five” juga menguji mutu tes saya: apakah tes akan menangkap jika hasil jam atau menit sengaja dibuat meleset.

### Error dan hasil yang saya temui
- AttributeError: 'NoneType' object has no attribute 'group' saat input tidak cocok regex. Ini mengajari saya untuk memeriksa hasil pencocokan dan mengubah masukan tak valid menjadi ValueError.
- TypeError: exceptions must derive from BaseException saat saya mencoba raise "ValueError".
- Output sempat salah format: 0900, 09::00, dan variasi sejenis karena tanda titik dua pada menit tidak konsisten.
- Saya menguji contoh valid dan invalid di terminal, menjalankan pytest, lalu memperbaiki tes sampai setiap kasus benar-benar diperiksa.
- Pada percobaan check50 awal, beberapa pemeriksaan untuk tes invalid belum lolos. Setelah memperbaiki cakupan tes dan mengulang check50, hasil akhirnya semua pemeriksaan lulus, termasuk format valid, batas waktu/menit, dan kemampuan tes menangkap versi kode yang sengaja dirusak.

### Yang saya pelajari
- Tangani hasil regex yang tidak cocok sebelum mengambil grupnya.
- raise ValueError menaikkan exception; menulis nama exception sebagai string tidak sama.
- Menit opsional perlu diperlakukan konsisten saat membentuk output.
- Tes exception harus menguji setiap kasus secara terpisah.
- Check50 juga memeriksa apakah tes buatan saya cukup kuat untuk menangkap implementasi yang rusak.
- Percobaan gagal dan pesan error membantu saya menemukan asumsi yang keliru. Saya tidak perlu langsung tahu seluruh solusi; saya bisa menyusun logika, menguji satu kasus, membaca hasilnya, lalu memperbaiki bagian yang belum tepat.

## Catatan proses belajar

Pada problem set ini saya menggunakan CS50 Duck untuk petunjuk dan pertanyaan pemandu, sesuai aturan CS50P yang saya ikuti. Saya tetap menulis, mengubah, dan menguji kode sendiri.