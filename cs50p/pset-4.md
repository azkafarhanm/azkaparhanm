# Problem Set 4

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

Sama seperti Problem Set 3: petunjuk saat mengerjakan soal saya minta ke CS50 Duck. Claude saya pakai untuk murojaah lecture sebelum mulai, dan untuk membahas setelah submit.

## Pemanasan sebelum mulai (13 Oktober 2026 pagi)

Murojaah Lecture 4, empat pertanyaan dari Claude, dijawab tanpa buka catatan. Keempatnya benar di intinya, tinggal dipertajam:

- **Slice:** `python hello.py Ali Umar Hasan` → `sys.argv[1:]` hasilnya `["Ali", "Umar", "Hasan"]`, `sys.argv[1:-1]` hasilnya `["Ali", "Umar"]`.
  - Hasil slice tetap list, jadi ditulis pakai kurung siku dan tanda kutip.
  - Hasan hilang bukan karena angka kanannya "tidak disebutkan". Angkanya disebutkan (`-1`, artinya Hasan), dan slice berhenti **sebelum** angka itu, sama seperti range.
- **pip vs import:** pip memasang library **ke komputer** (ke Python-nya), bukan ke dalam program. pip diketik di terminal, sekali saja. import diketik di setiap file yang butuh, jalan setiap kali program dijalankan.
- **JSON bersarang:** sesudah lewat `response.json()`, isi `o` sudah jadi dictionary Python, bukan JSON lagi. JSON itu bentuknya waktu masih di perjalanan dari server.
- **`__name__`:** Python membaca dari **atas ke bawah** (bukan kanan ke kiri, saya salah ucap). Baris `def` cuma mendefinisikan, tidak menampilkan apa-apa. Yang menampilkan itu baris `main()` di bawah, karena dia memanggil. Kesimpulan: **import itu menjalankan seluruh file dari atas.**

## 1. Emojize — selesai, check50 hijau semua 5/5 (13 Oktober 2026)

Dikerjakan **tanpa Duck**, cuma baca soal dan dokumentasi.

Yang diminta soal:
- User mengetik teks yang isinya kode emoji dalam bahasa Inggris, misalnya `:thumbsup:`.
- Program mengubahnya jadi emoji betulan, misalnya 👍.
- Soal juga kasih link daftar kode emoji dan pasangannya.

### Perjalanan
1. Pasang library `emoji` dulu pakai pip, karena third-party.
2. Baca dokumentasinya sedikit-sedikit, cari function untuk mengubah kode jadi emoji.
3. check50 pertama: 3 hijau, 2 merah. `:thumbsup:` dan `hello, :earth_asia:` tidak berubah jadi emoji, tercetak apa adanya.
4. Di dokumentasi saya ketemu parameter `language`, lalu saya kasih nilai `"alias"`. Dijalankan lagi, check50 hijau semua, lalu submit.

### Apa itu alias? (dibahas dengan Claude setelah submit)
- Alias = **nama panggilan**. Seperti absen santri: nama resmi Muhammad Ali Hasan, nama panggilannya Ali.
- Setiap emoji punya nama resmi dan nama panggilan:

| Emoji | Nama resmi | Alias |
|---|---|---|
| 👍 | `:thumbs_up:` | `:thumbsup:`, `:+1:` |
| 🌏 | `:globe_showing_Asia-Australia:` | `:earth_asia:` |

- Tanpa `language="alias"`, library-nya cuma kenal nama resmi. Makanya `:1st_place_medal:`, `:candy:`, `:ice_cream:` lolos dari awal (itu nama resmi), sedangkan `:thumbsup:` dan `:earth_asia:` gagal (itu nama panggilan).
- Dugaan awal saya: bedanya soal pakai underscore atau tidak. **Ternyata bukan.** `:earth_asia:` juga pakai underscore. Bedanya nama resmi vs nama panggilan.
- `language` itu nama parameternya, `"alias"` itu nilai yang saya kirim. Cara tulis `nama=nilai` begini namanya **keyword argument**. Ternyata sudah pernah saya pakai di Week 0: `print("hello", end="")`.

### Yang saya pelajari
- Membaca dokumentasi library sendiri itu bisa, dan jawabannya memang ada di sana.
- Pesan check50 `expected` vs `actual` itu petunjuk: `actual` masih berupa `:thumbsup:` berarti kodenya tidak dikenali, bukan programnya error.

## 2. Frank, Ian and Glen's Letters (figlet) — sudah submit (13 Oktober 2026)

Soal ini lumayan struggle. Banyak bertanya ke Duck, tapi Duck tidak kasih jawaban, cuma petunjuk dan pertanyaan pancingan. Akhirnya selesai, dan saya paham alur kodenya.

Yang diminta soal:
- Program menerima **nol** atau **dua** command-line argument.
  - Nol: teksnya ditampilkan pakai font **acak**.
  - Dua: argumen pertama harus `-f` atau `--font`, argumen kedua nama font-nya.
- Program minta user mengetik teks, lalu menampilkannya dalam font itu (ASCII art).
- Kalau argumennya salah (argumen pertama bukan `-f`/`--font`, atau font-nya tidak ada), program keluar pakai `sys.exit` dengan pesan error.
- Library-nya `pyfiglet`. Soalnya sendiri bilang dokumentasi pyfiglet "isn't very clear", dan memang waktu saya baca kurang jelas.

Petunjuk dari soal (bukan jawaban, ini ada di soalnya):
```python
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=f)
print(figlet.renderText(s))
```

### Perjalanan dan yang membuat saya tersendat

1. Salah paham "zero" dan "two"
   - Awalnya saya kira zero itu index 0. Ternyata maksudnya **jumlah argumen dari user**.
   - Karena `sys.argv[0]` selalu nama file, maka:
     - zero argumen dari user → `len(sys.argv)` = **1**
     - two argumen dari user → `len(sys.argv)` = **3**
   - Sama seperti murojaah tadi pagi: yang dari user dihitung mulai indeks 1.

2. Bingung `-f` dan `--font`
   - Saya baca di soal tapi tidak paham apa bedanya.
   - Ternyata ini kebiasaan di command line: **satu strip untuk versi pendek** (`-f`), **dua strip untuk versi panjang** (`--font`). Artinya sama, dua-duanya harus diterima.
   - Jadi `sys.argv[1]` isinya penanda (`-f` atau `--font`), `sys.argv[2]` isinya nama font-nya. Dua-duanya harus dicek, tujuannya beda.

3. `random.choice(figlet)` → `TypeError: object of type 'Figlet' has no len()`
   - choice butuh list (toples). `figlet` itu bukan list, itu objek.
   - List font-nya didapat dari `figlet.getFonts()`. Itu yang masuk ke choice.

4. `figlet = Figlet()` itu buat apa?
   - Baris itu **membuat objek** Figlet, lalu disimpan di variabel `figlet`.
   - Method `getFonts`, `setFont`, `renderText` itu milik objek ini. Tanpa membuat objeknya dulu, method-nya tidak bisa dipakai. Ibarat harus punya alatnya dulu, baru bisa pakai fungsi-fungsi alat itu.

5. Tugas tiga method itu
   - `getFonts()` → mengembalikan list semua nama font. Tidak butuh argumen.
   - `setFont(font=...)` → "memasang" font ke objek figlet.
   - `renderText(teks)` → mengubah teks jadi ASCII art pakai font yang sudah dipasang. Hasilnya ini yang di-print.
   - Urutannya: pilih dan cek font → setFont → renderText.

6. Mencari dokumentasi lewat terminal: `help()` dan `dir()`
   - Duck kasih tips `dir()` = menampilkan daftar method milik sebuah objek. `help()` = menampilkan penjelasannya.
   - Sempat salah: saya ketik `help()` langsung di terminal bash, hasilnya `bash: syntax error`. Harus masuk Python dulu (`python`), baru di dalam `>>>`.
   - Sempat juga `dir(figlet)` di Python baru → `NameError`, karena di sesi Python yang baru belum ada import dan belum ada objek figlet-nya.
   - Sempat menempel `...` ikut ke kode → SyntaxError. Sama seperti catatan Pset 3: `>>>` dan `...` bukan bagian dari kode.
   - Akhirnya berhasil pakai `from pyfiglet import Figlet` lalu `help(Figlet)`. Ketemu tiga baris ini:
     ```
     getFonts(self) -> 'list[str]'
     renderText(self, text: 'str') -> 'FigletString'
     setFont(self, **kwargs: 'str') -> 'None'
     ```
   - Tanda `->` itu menunjukkan apa yang dikembalikan. getFonts mengembalikan list of string. setFont mengembalikan None. `**kwargs` artinya argumennya harus pakai nama (keyword).

7. `figlet.setFont(font)` → `TypeError: Figlet.setFont() takes 1 positional argument but 2 were given`
   - Error baru buat saya. Kata Duck: angka 1 itu `self`, yang otomatis terkirim waktu saya tulis `figlet.setFont(...)`. Jadi kalau saya tambah `font` tanpa nama, totalnya 2.
   - setFont tidak mau argumen biasa (positional). Harus pakai keyword: `font=...`.

8. setFont tidak perlu disimpan ke variabel
   - Saya kira hasil setFont disimpan dulu ke variabel, lalu variabel itu yang di-render.
   - Ternyata setFont **mengubah objek figlet itu sendiri** (objeknya jadi "ingat" font-nya), dan kembaliannya None. Mirip shuffle di lecture: mengubah langsung, tidak mengembalikan apa-apa.
   - Jadi cukup dipanggil, lalu renderText otomatis memakai font yang sudah dipasang.

9. `figlet.getFonts(sys.argv[2])` → TypeError yang sama
   - getFonts tidak butuh argumen, jadi kalau saya kasih satu, totalnya 2 (dengan self).
   - Sempat juga `sys.argv[3]` → IndexError, karena isi sys.argv cuma sampai indeks 2.

10. Mengecek font ada atau tidak: `in`
    - Pakai keyword `in` untuk mengecek apakah nama font dari user ada di dalam list `getFonts()`.

11. `else` pasangan dengan if yang mana?
    - Pengecekannya bertingkat (cek jumlah argumen → cek penanda → cek font). Duck bertanya: else itu pasangan if yang mana? Satu else cukup atau tidak?
    - Ternyata setiap tingkat yang bisa salah butuh jalan keluarnya sendiri.
    - Sempat juga kena IndentationError dan `SyntaxError` di else waktu menyusun tingkatannya.

12. check50 merah: `timed out while waiting for program to exit`
    - 3 tes merah: satu argumen, argumen pertama salah, argumen kedua salah.
    - Perasaan saya sudah pasang sys.exit di semua cabang. Ternyata masalahnya di **urutan**: `input()` saya taruh paling atas, sebelum pengecekan. Jadi program berhenti menunggu ketikan dulu, padahal check50 tidak mengetik apa-apa, cuma menunggu program keluar. Waktunya habis.
    - Kesimpulan saya: input baru diminta **setelah** argumennya dipastikan benar. Dan karena Python membaca dari atas ke bawah, variabel teksnya harus sudah ada sebelum dipakai di renderText.

13. check50 merah lagi: `Expected non-zero exit code`
    - Sudah tidak timed out, tapi sekarang pesannya beda.
    - Ternyata `sys.exit()` tanpa isi itu keluarnya dianggap **berhasil** (exit code 0). Padahal program keluar karena error, jadi harusnya exit code bukan nol.
    - Kalau sys.exit diberi pesan, misalnya `sys.exit("Error")`, pesannya tampil dan exit code-nya bukan nol. Setelah itu check50 hijau semua 8/8.

14. Tanda `;` di terminal
    - Saya coba `python figlet.py ;`, kok keluar font acak? Saya kira harusnya salah.
    - Ternyata `;` di terminal itu pemisah perintah, bukan argumen. Jadi sama saja dengan `python figlet.py` biasa.

### Catatan: check50 terakhir sebelum submit
- check50 sempat **hijau semua 8/8**. Tapi check50 yang terakhir, tepat sebelum submit, merah satu: `exits given one command-line argument → Expected non-zero exit code`.
- Berarti ada yang berubah di antara dua check50 itu. Perlu dicek lagi besok, lalu lihat hasilnya di submit.cs50.io. Kalau masih merah, boleh submit ulang.

### Yang saya pelajari
- Zero/two argumen itu dihitung dari user, jadi `len(sys.argv)` 1 dan 3.
- Satu strip = versi pendek, dua strip = versi panjang (`-f` / `--font`).
- Objek harus dibuat dulu (`figlet = Figlet()`), baru method-nya bisa dipakai.
- `help()` dan `dir()` di dalam Python untuk membaca dokumentasi kalau dokumentasi online kurang jelas.
- `->` di help menunjukkan apa yang dikembalikan sebuah method.
- Parameter = nama slot waktu function dibuat. Argument = nilai yang dikirim waktu dipanggil. Positional argument dikirim berdasarkan urutan, keyword argument dikirim pakai nama (`font=...`).
- Ada method yang mengubah objeknya sendiri dan mengembalikan None (setFont, mirip shuffle).
- Minta input setelah pengecekan, supaya program bisa langsung keluar kalau argumennya salah.
- `sys.exit()` kosong = exit code 0 (berhasil). Untuk keluar karena error, kasih pesan di dalamnya.

### Salah yang saya buat
- `random.choice(figlet)`: memasukkan objek, bukan list.
- `figlet.getFonts(sys.argv[2])`: memberi argumen ke method yang tidak butuh argumen.
- `figlet.setFont(font)`: lupa keyword `font=`.
- `sys.argv[3]`: indeks di luar jangkauan.
- `input()` di paling atas, sebelum pengecekan.
- `sys.exit()` tanpa pesan, jadi exit code 0.
- Mengetik `help()` di bash, bukan di Python.

### Jenis error yang sudah saya kenal (update)
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError, ZeroDivisionError, IndentationError, KeyboardInterrupt (Ctrl+C).
- TypeError ternyata bisa juga karena **jumlah argumen** salah (`takes 1 positional argument but 2 were given`) atau karena memberi objek yang tidak punya panjang ke choice (`has no len()`).
- Pesan check50 baru: `timed out while waiting for program to exit` dan `Expected non-zero exit code`.

### Yang mau ditanyakan dan didiskusikan besok
- Kalau pakai `import pyfiglet` saja (bukan `from pyfiglet import Figlet`), berarti tinggal ditambahkan `pyfiglet.` di depan Figlet?
- Lebih detail soal getFonts yang "mengembalikan" list.
- Kenapa check50 terakhir merah satu, padahal sebelumnya hijau semua.

### Yang ingin dicoba
- Jalankan `python figlet.py -f slant ekstra` (tiga argumen). Apa yang terjadi? Sesuai soal tidak?
- Coba `dir(figlet)` di interactive mode setelah membuat objeknya, lihat ada method apa saja.
