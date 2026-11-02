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

## 3. Working 9 to 5 — selesai (2 November 2026)

(Pembahasan lengkap menyusul.)
