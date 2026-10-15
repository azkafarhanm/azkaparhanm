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

## 2. Frank, Ian and Glen's Letters (figlet) — selesai, check50 hijau semua 8/8 (13 Oktober 2026)

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

### Catatan: check50 yang terakhir merah
- Di riwayat terminal ada check50 merah satu sesudah yang hijau 8/8. Itu cuma saya tes-tes saja. Yang saya submit tetap kode yang hijau semua.

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

### Diskusi pagi dengan Claude (14 Oktober 2026)

1. setFont dipanggil tanpa diisi
   - `figlet.setFont(font=)` (keyword ada, nilainya kosong) → langsung SyntaxError. Python tidak mengizinkan `nama=` tanpa nilai.
   - `figlet.setFont()` (kosong sama sekali) → tidak error. Kembaliannya tetap None, dan font-nya tetap font yang terakhir dipasang. Kalau belum pernah dipasang, pakai font default namanya `standard`.
   - Ibarat ustadz bilang "pakai mushaf yang tadi saja".
   - Kalau nama font-nya tidak ada, misalnya `setFont(font="tidakada")`, pyfiglet langsung error `FontNotFound`.

2. Crash vs sys.exit
   - Saya kira pengecekan pakai `in` juga error kalau font-nya tidak ada. **Ternyata tidak.** `"tidakada" in figlet.getFonts()` hasilnya cuma `False`. Error baru muncul kalau nama font yang salah langsung dimasukkan ke setFont.
   - Jadi dengan pengecekan, error-nya tidak pernah terjadi. Saya sendiri yang memutuskan berhenti, sebelum masalahnya muncul.
   - Crash = Python yang menghentikan karena kaget, user melihat traceback panjang. Ibarat santri tiba-tiba pingsan di tengah setoran.
   - sys.exit = saya yang menghentikan dengan sengaja, user melihat pesan singkat. Ibarat ustadz bilang dengan tenang "cukup dulu, ulang besok".
   - Sama-sama berhenti, tapi yang kedua terkendali. Soalnya juga minta keluar lewat sys.exit dengan pesan.

3. `-f` vs `--font`
   - Tulisannya `-f` (huruf F, singkatan font), bukan `-v`.
   - Di program command line memang biasa ada versi ringkas (1 strip, 1 huruf) dan versi lengkap (2 strip, 1 kata). Artinya sama.
   - Contoh lain: `python -V` = `python --version`, `pip install -U` = `pip install --upgrade`.
   - Ringkas = cepat diketik. Lengkap = mudah dibaca.

4. Kalau cuma `import pyfiglet`
   - Awalan `pyfiglet.` cuma ditambahkan di depan `Figlet`, di baris pembuatan objeknya: `figlet = pyfiglet.Figlet()`.
   - Sesudah objeknya jadi, method-nya tetap dipanggil lewat objek: `figlet.setFont(...)`, `figlet.renderText(...)`.
   - Saya sempat mengira kalau `import pyfiglet` saja, method-nya bisa langsung dipakai tanpa objek. **Ternyata tidak.**

5. Kenapa harus bikin objek?
   - Tergantung library-nya, bukan aturan khusus pyfiglet. Ada dua gaya:
     - Function langsung di module, tidak perlu objek: `random.choice`, `statistics.mean`, `cowsay.cow`, `emoji.emojize`. Function-nya tidak perlu mengingat apa-apa.
     - Harus bikin objek dulu: `Figlet`. renderText itu milik objek Figlet, bukan milik module pyfiglet. Karena Figlet perlu **mengingat** font yang sedang dipakai.
   - Analogi mesin stempel: `Figlet()` = membuat mesin stempel. `setFont` = memasang cetakan huruf, mesinnya ingat cetakannya. `renderText` = menstempel pakai cetakan yang terpasang.
   - Mesinnya harus disimpan di variabel, supaya yang dipakai renderText itu mesin yang sama dengan yang tadi dipasangi font.
   - Prinsip: kalau method-nya perlu mengingat sesuatu, biasanya harus lewat objek. Nanti dibahas lengkap di Week 8 (Object-Oriented Programming).

6. Tiga argumen dengan syarat `> 2`
   - `python figlet.py -f slant ekstra` → `len(sys.argv)` = 4. Karena 4 > 2, program tetap jalan pakai slant, kata `ekstra` diabaikan.
   - Saya sempat bilang "kalau lebih ya diabaikan, karena sesuai permintaan". **Justru tidak sesuai.** Soalnya bilang nol **atau dua** argumen, jadi tiga argumen itu salah dan harus keluar pakai sys.exit.
   - check50 tetap hijau karena kasus itu kebetulan tidak dites. Pelajaran: **check50 hijau belum tentu semua aturan soal terpenuhi.**
   - Saya perbaiki pakai `==` (tepat sekian), dites ulang dengan `ekstra`, dan betul program keluar dengan pesan error.

### Yang ingin dicoba
- ~~`dir(figlet)` di interactive mode~~ → sudah dicoba, keluar daftar method dan informasinya.
- ~~Tiga argumen (`ekstra`)~~ → sudah dicoba dan diperbaiki.

## 3. Adieu, Adieu — selesai, check50 hijau semua 9/9 (14 Oktober 2026)

Yang diminta soal:
- User mengetik nama satu per satu, baris per baris, sampai menekan Ctrl+D.
- Anggap user minimal mengetik satu nama.
- Program mengucapkan perpisahan ke semua nama itu: `Adieu, adieu, to ...`
  - 1 nama: `Adieu, adieu, to Liesl`
  - 2 nama: `Adieu, adieu, to Liesl and Friedrich`
  - 3 nama atau lebih: dipisah koma, dan sebelum nama terakhir pakai `and`.
- Library-nya `inflect`.

### Perjalanan dan yang membuat saya tersendat

1. Baca dokumentasi inflect dulu
   - Yang saya tangkap dari bagian atas dokumentasi: inflect itu module untuk mengubah kata, misalnya singular jadi plural atau sebaliknya (noun, verb, adjective), ordinal, angka.
   - Saya paham isinya, tapi bingung mencocokkan dengan soal: function mana yang dibutuhkan?
   - Duck kasih petunjuk: cari yang berhubungan dengan "join". Ketemu `p.join(...)`. Sama seperti Figlet, harus bikin objeknya dulu: `p = inflect.engine()`.

2. `names = name` → list berubah jadi string
   - Saya buat `names = []` sebelum loop, lalu di dalam loop `names = name`. Saya kira list-nya jadi terisi.
   - Ternyata `if len(names) == 1` tidak pernah jalan. Saya coba `print(len(names))`, hasilnya 4 untuk "azka". Yang dihitung huruf-hurufnya, bukan jumlah nama.
   - Penyebabnya: tanda `=` itu **menimpa/mengganti**, bukan menambahkan. Jadi list kosongnya tertimpa string.
   - Saya sempat tebak pakai `index`. Salah, index itu untuk mencari posisi. Yang benar **`append`**, untuk menambahkan satu item ke akhir list.

3. Ctrl+D → EOFError, ditangkap pakai try/except
   - Waktu Ctrl+D ditekan di `input()`, muncul `EOFError`. Ini sudah pernah saya temui di Grocery List (Pset 3).

4. `TypeError: print() got an unexpected keyword argument 'conj'`
   - Saya taruh `conj='and'` di dalam kurung print. Padahal `conj` itu parameter milik `p.join`, bukan milik print. print tidak kenal conj, jadi protes.

5. Pengecekan jumlah nama: if dan elif sama persis
   - Saya tulis `if len(names) > 2` lalu `elif len(names) > 2`. Dua-duanya sama, jadi kalau cuma 2 nama, tidak ada yang jalan, tidak tampil apa-apa.

6. `Name: Name: Name: Name:` terus-terusan
   - Waktu Ctrl+D tapi belum ada `break`: EOFError tertangkap, loop lanjut, input langsung kena EOF lagi, tertangkap lagi, terus tanpa henti.
   - Bukti: **except saja tidak menghentikan loop. Yang menghentikan loop itu `break`.**

7. Sempat salah tempat di terminal
   - Saya ketik `cd ~` supaya prompt-nya kembali jadi `$` saja. Ternyata malah jadi `~/ $`, dan folder `adieu` yang saya buat di situ tidak muncul di sidebar.
   - `~` (tilde) itu home folder, beda dengan folder workspace yang tampil di sidebar. Ibarat kamar pribadi vs ruang kelas.
   - Kembali ke workspace: `cd /workspaces/237807624`. Sempat salah ketik `cd cd /workspaces/...` → `too many arguments`, karena cd-nya dua kali.
   - Menghapus folder: `rm adieu/` gagal (`Is a directory`), karena rm tanpa `-r` cuma untuk file. Folder kosong pakai `rmdir`. Folder beserta isinya pakai `rm -r` (hati-hati, permanen, tidak ada Recycle Bin).

### Setelah submit: diskusi dengan Claude

1. `sep='and'` di kode saya ternyata tidak dipakai sama sekali
   - `sep` itu milik print, bukan milik p.join. Kelihatan dari tanda kurungnya: sep ada di dalam kurung print, di luar kurung p.join.
   - sep di print cuma berpengaruh kalau print diberi beberapa argumen yang dipisah koma. Di kode saya, print cuma dapat satu argumen, karena teksnya sudah disambung pakai `+`. Jadi sep diabaikan.
   - "and"-nya datang dari p.join sendiri: parameter `conj` (conjunction, kata sambung) default-nya sudah `'and'`.

2. Koma otomatis: aturan p.join

| Isi list | Hasil `p.join(...)` |
|---|---|
| `["Ali"]` | `Ali` |
| `["Ali", "Umar"]` | `Ali and Umar` |
| `["Ali", "Umar", "Hasan"]` | `Ali, Umar, and Hasan` |

   - Jadi if/else saya (2 nama atau lebih vs else) sebenarnya hasilnya sama persis. Tidak perlu dibedakan, join sudah menangani semua jumlah.

3. Kenapa pakai inflect, bukan print sep saja?
   - `print("Ali", "Umar", "Hasan", sep=" and ")` → `Ali and Umar and Hasan`. sep memasang pemisah yang **sama** di setiap celah.
   - `", ".join(["Ali", "Umar", "Hasan"])` → `Ali, Umar, Hasan`, tanpa "and".
   - Yang diminta soal: pemisahnya beda tergantung posisi dan jumlah. Bisa dibuat sendiri pakai if/elif dan slice (`names[:-1]`), tapi ribet. Gunanya library: tidak perlu menulis ulang yang sudah dibuat orang lain.

4. `", ".join(...)`: objeknya kok koma?
   - Di Python, **string juga objek**. `", "` itu objek string, dan join itu method milik string.
   - Sebenarnya sudah sering saya pakai: `name.strip()`, `"hello".upper()`, bahkan `names.append()` (method milik list).
   - Di join bawaan string, string itulah yang jadi perekat di antara setiap item. Ibarat merangkai tasbih: names itu biji-bijinya, `", "` itu talinya. Yang diperintah merangkai itu talinya.
   - Ada dua join yang berbeda: `", ".join()` milik objek string (bawaan Python, satu perekat sama), `p.join()` milik objek inflect (ikut aturan bahasa Inggris). Namanya sama, pemiliknya beda. Sama seperti pelajaran namespace: yang menentukan join mana itu objek sebelum titiknya.

5. Pengecekan ditaruh di mana: di dalam try, di dalam except, atau di luar loop?

| Posisi | Yang terjadi |
|---|---|
| Di dalam try | Jalan setiap kali satu nama masuk. Ini terjadi di terminal saya: sesudah ketik `azki` langsung muncul `azka and azki`, lalu ditanya lagi. |
| Di dalam except (kode saya) | Jalan sekali, waktu Ctrl+D. Benar. |
| Di luar loop, sesudah while | Juga benar, asal except-nya berisi break. |

   - Saya sempat mengira "kalau Ctrl+D menghentikan program, pengecekan di luar loop tidak kebaca". Itu cuma benar kalau EOFError **tidak ditangkap**. Kalau ditangkap lalu break, yang berhenti cuma loop-nya, Python lanjut ke baris di bawah loop.
   - Pembagian tugas yang rapi: loop mengumpulkan nama, except menghentikan loop, baris sesudah loop menampilkan hasil. Ibarat halaqah: setoran dikumpulkan dulu sampai selesai, baru ustadz mengumumkan hasilnya.

### Kosakata dari soal
- **sung** = dinyanyikan (bentuk ketiga dari sing). *sung largely in English* = sebagian besar dinyanyikan dalam bahasa Inggris.
- **rhymes with** = berima / bersajak dengan. "yieu" bukan kata sungguhan, cuma dibuat supaya berima dengan "you".

### Yang saya pelajari
- `=` itu menimpa, `append` itu menambahkan ke list.
- `print(len(...))` untuk mengecek apa yang sebenarnya dihitung.
- Parameter itu milik function yang kurungnya membungkus dia.
- except tidak menghentikan loop, break yang menghentikan.
- String dan list juga objek, punya method sendiri.
- `~` di terminal = home folder, beda dengan workspace.

### Yang ingin dicoba
- Bikin versi tanpa inflect di file terpisah, pakai if/elif dan slice. Murojaah slice yang bagus.
- Coba `" - ".join(...)` dan `"".join(...)` di interactive mode.

## 4. Guessing Game — check50 hijau semua 10/10 (14 Oktober 2026)

Yang diminta soal:
- Minta user mengetik level, bilangan bulat positif. Kalau bukan, tanya lagi.
- Program memilih angka acak dari 1 sampai level itu (inklusif).
- Minta user menebak, bilangan bulat positif. Kalau bukan, tanya lagi.
  - Tebakan lebih kecil → `Too small!`, tanya lagi.
  - Tebakan lebih besar → `Too large!`, tanya lagi.
  - Tebakan pas → `Just right!`, program selesai.

### Cara saya mulai: kumpulkan kerangka dulu
- Sekarang saya tidak menulis komentar dulu. Saya baca soalnya: minta apa dulu? Oh, input, berarti disimpan di variabel karena nanti dipakai lagi. Inputnya harus positif? Berarti perlu if/else.
- Kerangka-kerangka itu saya kumpulkan dulu, baru saya sambung-sambungkan: kerangka ini cocok tidak kalau ditaruh di sini?
- Kata Claude, cara ini namanya **memecah masalah** (decomposition). Ini cara kerja programmer sungguhan.

### Perjalanan dan yang membuat saya tersendat

1. Dua input dalam satu loop?
   - Awalnya saya buat dua try. Tapi bingung: kalau level-nya negatif, harusnya tanya level lagi, kok malah lanjut tanya guess? Karena Python membaca ke bawah.
   - Duck bertanya: struktur apa untuk "ulangi terus sampai valid"? Apakah bagian level harus selesai dulu sebelum masuk guess?
   - Akhirnya saya tebak sendiri: **dua while True**. Yang pertama menangani input level, yang kedua menangani input guess. Sejajar, satu sesudah yang lain, bukan di dalam.
   - Loop pertama harus bisa berhenti (pakai break) kalau level-nya sudah valid, baru program bisa pindah ke loop kedua.

2. while True kedua berwarna abu-abu
   - Kata Duck, editor memberi warna redup pada kode yang **tidak akan pernah dijalankan** (unreachable). Waktu itu loop pertama saya belum ada break, jadi berputar selamanya, dan loop kedua tidak pernah tercapai.

3. Function random yang mana, dan ditaruh di mana?
   - Bingung antara range, randint, randrange.
   - Angka acaknya cukup dibuat **sekali**, jadi ditaruh di luar loop guess, sebelum loop itu. Kalau di dalam loop, angkanya berganti setiap kali menebak.
   - Rentangnya 1 sampai level dari user. Batas atasnya harus ikut, jadi pakai randint yang inklusif. Beda dengan range yang tidak inklusif.

4. `NameError: name 'level' is not defined` waktu input `cat`
   - Pengecekan level jalan padahal int()-nya gagal, jadi level tidak pernah dibuat. Pelajaran yang sama dengan Fuel Gauge: baris yang memakai hasil try ditaruh di else, setelah try-nya berhasil.

5. `TypeError: '<' not supported between instances of 'str' and 'int'`
   - Guess belum diubah jadi int sebelum dibandingkan. Ini juga pernah terjadi di Fuel Gauge.

6. `SyntaxError: expected 'except' or 'finally' block`
   - Error baru. try wajib punya pasangan, yaitu except (atau finally). Kalau sesudah try langsung if, Python protes.

7. check50 merah karena huruf
   - `Too large` (kurang tanda seru) dan `Too Small!` (S besar). check50 membandingkan huruf per huruf, case-sensitive.
   - Pesan check50-nya sempat membingungkan: `Did not find "Guess:" in "Too Small!\r\nGuess: "`. Padahal "Guess:"-nya ada. Ternyata yang salah di bagian lain.

8. `rejects nonpositive guess` masih merah
   - Saya kira non-positive itu "kurang dari nol". Jadi syarat saya `< 0`, dan nol lolos. Padahal program harusnya menolak nol juga.
   - Akhirnya saya balik logikanya: `not guess > 0` (bukan lebih dari nol). Langsung hijau semua.

### Positive, negative, dan nol

| Istilah | Artinya | Nol termasuk? |
|---|---|---|
| positive | lebih dari 0 | tidak |
| negative | kurang dari 0 | tidak |
| non-positive | bukan positif = negatif atau nol | ya |
| non-negative | bukan negatif = positif atau nol | ya |

- Nol itu bukan positif dan bukan negatif.
- `not guess > 0` sama artinya dengan `guess <= 0`.

### Setelah check50 hijau: Level 0 ternyata crash
- Claude minta saya coba `Level: 0`. Ternyata langsung crash.
- Penyebabnya: pengecekan level saya masih `< 0`, jadi nol lolos. Padahal soalnya minta level bilangan bulat **positif**. Kesalahan yang sama dengan guess, cuma belum saya perbaiki di level.
- `random.randint(1, 0)` diminta memilih angka dari 1 sampai 0. Tidak ada angka di situ, toplesnya kosong.
- Saya kira error-nya SyntaxError. **Ternyata bukan**, yang muncul `ValueError: empty range in randrange(1, 1)`.
  - SyntaxError muncul **sebelum** program jalan, karena cara menulis kodenya salah.
  - ValueError (dan TypeError, NameError) muncul **saat** program jalan, kodenya benar tapi nilainya bermasalah. Buktinya program sempat minta `Level:` dulu.
- Tidak tertangkap except ValueError saya, karena baris randint ada **di luar** try. except cuma menangkap error dari baris di dalam try-nya sendiri.
- Lagi-lagi: **check50 hijau belum tentu semua aturan soal terpenuhi.** Sama seperti figlet kemarin.

### Kenapa pesannya randrange, padahal yang saya panggil randint?
- Di dalamnya, randint memanggil randrange dengan batas atas **ditambah 1**. Yang menambah satu itu randint, bukan randrange.
- randrange sendiri sama seperti range: berhenti **sebelum** batas atasnya.

| Yang saya tulis | Yang sebenarnya dijalankan | Angka yang mungkin keluar |
|---|---|---|
| `randint(1, 8)` | `randrange(1, 9)` | 1 sampai 8 |
| `randrange(1, 8)` | `randrange(1, 8)` | 1 sampai 7 |
| `randint(1, 0)` | `randrange(1, 1)` | kosong → ValueError |

- Ibarat randrange itu absen yang ditulis "sampai sebelum nomor 9". randint itu petugas yang baik hati: saya bilang "sampai nomor 8", dia otomatis tulis "sampai sebelum nomor 9" supaya nomor 8 tidak ketinggalan.
- Jadi randint inklusif karena dia cuma randrange yang sudah ditambah satu.

### Yang saya pelajari
- Dua input yang masing-masing harus diulang sampai valid → dua while True sejajar.
- Kode berwarna abu-abu di editor = tidak akan pernah dijalankan.
- Angka acak cukup dibuat sekali, di luar loop tebakan.
- Non-positive termasuk nol.
- SyntaxError (sebelum jalan) beda dengan ValueError/TypeError/NameError (saat jalan).
- except cuma menangkap error dari baris di dalam try-nya.
- check50 itu huruf per huruf, termasuk tanda seru dan huruf besar-kecil.

### Jenis error yang sudah saya kenal (update)
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError, ZeroDivisionError, IndentationError, KeyboardInterrupt, EOFError, FontNotFound (dari pyfiglet).
- SyntaxError baru: `expected 'except' or 'finally' block`.
- ValueError baru: `empty range in randrange(...)`.

### Yang ingin dicoba
- Perbaiki pengecekan level supaya nol ditolak, tes `Level: 0`, jalankan check50, lalu submit50.

## Pemanasan pagi (15 Oktober 2026)

Murojaah materi kemarin, lima pertanyaan dari Claude, dijawab tanpa buka catatan.

1. `names = []` lalu `names = "Ali"` vs `names = []` lalu `names.append("Ali")`
   - Jawaban saya: len-nya 3 dan 1. **Benar.**
   - Yang diluruskan: `=` itu bukan meng-update, tapi **mengganti seluruhnya**. List kosongnya dibuang, names sekarang menunjuk string "Ali", makanya len menghitung huruf.
   - names sudah jadi objek list sejak `names = []`, bukan baru jadi objek karena append.
2. `"-".join(["Ali", "Umar", "Hasan"])`
   - Objeknya `"-"`, method-nya join, hasilnya `Ali-Umar-Hasan`. **Benar.**
   - Tapi saya bilang join itu "memecah". **Salah, kebalikannya.** join itu menyambung/merangkai. Yang memecah itu split.
   - `"-".join([...])` → dari list jadi satu string. `"Ali-Umar-Hasan".split("-")` → dari string jadi list. Pasangan yang berlawanan.
3. Non-positive dari -3, 0, 5 → yang ditolak -3 dan 0. **Benar.**
4. `randint(1, 5)` di dalamnya jadi `randrange(1, 6)`. `randrange(1, 5)` keluarnya 1 sampai 4. **Benar.**
5. Kenapa `Name: Name: Name:` terus-terusan di Adieu?
   - Jawaban saya: karena tidak ada break. **Setengah benar.**
   - Kenapa tidak menunggu ketikan: sesudah Ctrl+D, aliran input dianggap sudah ditutup. Setiap kali loop balik ke input(), dia langsung kena EOFError lagi tanpa menunggu. Ibarat pintu kelas sudah dikunci, tapi ustadz terus memanggil "santri berikutnya!".

## raise: sengaja melempar error (diskusi pagi, 15 Oktober 2026)

Di soal Little Professor ada kata kunci `raise`. Saya lupa, jadi saya tanya ke Claude.

- **raise = sengaja memunculkan error sendiri.** Kalau except itu menangkap, raise itu melempar. Raise artinya "mengangkat", seperti santri yang mengangkat tangan karena ada masalah.
- Error yang selama ini saya temui dibuat oleh Python. Dengan raise, saya sendiri yang membuat, karena saya tahu ada aturan yang dilanggar.

Contoh di luar soal:
```python
def ambil_juz(nomor):
    if nomor < 1 or nomor > 30:
        raise ValueError("Juz hanya 1 sampai 30")
    return f"Juz {nomor}"
```

Mekanismenya:
1. Kalau baris raise jalan, function **langsung berhenti** di situ. return di bawahnya tidak dijalankan.
2. Error-nya dilempar ke **siapa pun yang memanggil** function itu.
3. Kalau pemanggil punya try/except untuk error itu → tertangkap, pemanggil yang memutuskan mau apa.
4. Kalau tidak ada yang menangkap → program crash, traceback-nya menampilkan pesan saya.

| Kata kunci | Tugas | Analogi bola |
|---|---|---|
| try | mencoba menjalankan | bermain |
| raise | melempar error | melempar bola |
| except | menangkap error | menangkap bola |

Kenapa raise, bukan print atau sys.exit?
- print: cuma menampilkan tulisan, function-nya tetap lanjut seolah tidak ada masalah, ujungnya mengembalikan None.
- sys.exit: menghentikan seluruh program. Terlalu keras.
- raise: cuma melaporkan masalah, keputusannya diserahkan ke pemanggil.
- Ibarat ustadz penguji yang menerima santri minta setoran juz 31: dia tidak menyetop seluruh halaqah (sys.exit), tidak pura-pura lanjut (print), cukup bilang "ini tidak bisa", lalu musyrif yang mengantar santri itu yang memutuskan langkah berikutnya.

Saya coba sendiri di interactive mode: `raise ValueError("coba-coba")` → keluar traceback, baris terakhirnya `ValueError: coba-coba`.

Pertanyaan saya: program-nya masih lanjut ke bawah atau berhenti?
- **Berhenti**, kecuali ditangkap. Di interactive mode (`>>>`) memang saya masih bisa mengetik lagi, karena interactive mode sengaja tidak keluar setiap ada error. Tapi di file .py, program benar-benar berhenti.

```python
try:
    print("satu")
    raise ValueError("coba")
    print("dua")
except ValueError:
    print("tertangkap")

print("tiga")
```
- Hasilnya: `satu`, `tertangkap`, `tiga`. `dua` tidak pernah dicetak, karena begitu raise jalan, Python langsung loncat ke except.

| | Baris sesudah raise (di blok yang sama) | Sisa program |
|---|---|---|
| Tidak ditangkap | dilewati | berhenti (crash) |
| Ditangkap except | dilewati | lanjut sesudah except |

Pertanyaan saya lagi: kok except-nya jalan? Saya kira try-nya berhasil, karena baris raise sudah dijalankan.
- **Ternyata raise di dalam try artinya try-nya gagal.** Try dianggap berhasil hanya kalau semua barisnya selesai tanpa error. raise itu tugasnya membuat error.
- Bagi except, tidak ada bedanya error itu dari Python (`int("cat")`) atau dari raise saya. Seperti penjaga gawang: tidak peduli bola dari kaki siapa, yang dia lihat cuma ada bola ValueError yang masuk atau tidak.
- Baris raise memang dijalankan, tapi hasil dari menjalankannya adalah error. Ibarat santri yang lancar membaca, tapi yang dibaca itu pengumuman bahwa ada kesalahan.
- Kalau ada else, else juga tidak jalan, karena else cuma jalan kalau try benar-benar berhasil.

## 5. Little Professor — selesai, check50 hijau semua 13/13 (15 Oktober 2026)

Soal ini lumayan menantang, harus berpikir sangat keras. Cocok untuk dimurojaah nanti supaya ilmunya terserap.

Yang diminta soal:
- Minta user mengetik level (n). Kalau bukan 1, 2, atau 3, tanya lagi.
- Buat 10 soal penjumlahan `X + Y = `. X dan Y bilangan bulat non-negatif dengan n digit.
- Kalau jawaban salah (atau bukan angka) → tampilkan `EEE`, tanya lagi. Maksimal 3 kali per soal. Kalau tetap salah, tampilkan jawaban yang benar.
- Terakhir tampilkan skor: berapa yang benar dari 10.
- Wajib pakai tiga function: `main`, `get_level` (minta level, return 1/2/3), `generate_integer(level)` (return satu angka acak dengan n digit, atau raise ValueError kalau level bukan 1, 2, 3). Dan wajib ada `if __name__ == "__main__":`.

### Perjalanan dan yang membuat saya tersendat

1. Bingung main() isinya apa
   - Petunjuk soal cuma ada untuk get_level dan generate_integer. Main tidak ada petunjuknya. Saya simpulkan, yang lain-lain dikerjakan di main.
   - Kata Duck: main itu "sutradara" yang mengatur alur dan memanggil function-function lain.

2. Salah fokus: tugas tiap function tercampur
   - Saya sempat mau bikin loop 3 kali di get_level. Padahal batas 3 kali itu untuk menjawab soal matematika, bukan untuk memilih level.
   - Saya juga sempat bilang "level itu bebas, berapapun diterima". Salah, level cuma 1, 2, 3, dan diulang terus sampai valid (while True, bukan for).
   - Pelajaran: harusnya fokus dulu, setiap function gunanya untuk apa. Jangan tugas main dicampur ke function lain.

3. `get_level(level)`: parameter yang tidak perlu
   - Saya bikin `def get_level(level)` lalu di main `level = get_level(level)`.
   - Muncul **error baru**: `UnboundLocalError: cannot access local variable 'level' where it is not associated with a value`. Python mengerjakan sisi kanan dulu, padahal `level` di dalam kurung belum pernah diberi nilai. Variabelnya baru dibuat setelah sisi kanan selesai.
   - Lalu saya hapus argumennya di main, muncul `TypeError: get_level() missing 1 required positional argument: 'level'`, karena di def-nya masih ada parameter.
   - Ternyata get_level tidak butuh parameter, karena dia sendiri yang membuat level dari input user.

| | Butuh bahan dari luar? | Parameter | Memberi hasil lewat |
|---|---|---|---|
| `get_level()` | Tidak, dia membuat level sendiri dari input | tidak ada | return level |
| `generate_integer(level)` | Ya, dia perlu tahu level-nya | level | return integer |

   - Aturannya: **parameter = bahan yang dibutuhkan function dari luar. return = hasil yang dia serahkan kembali.**
   - Ibarat santri: get_level itu santri yang ditugasi "tanyakan ke wali santri mau ikut kelas berapa", tidak perlu dibekali apa-apa. generate_integer itu santri yang ditugasi "ambilkan soal untuk kelas sekian", jadi harus diberi tahu kelasnya.
   - Untuk mengambil hasil get_level di main tidak perlu print. Cukup return di function-nya, lalu ditangkap pakai `=`.

4. Input di main, loop di get_level → tidak bisa reprompt
   - input() harus ada di dalam loop yang sama, supaya bisa diulang.

5. `level` berwarna abu-abu
   - Saya kira bakal error. Ternyata tidak. Abu-abu karena variabelnya disimpan tapi belum pernah dipakai. Begitu dipakai di `generate_integer(level)`, warnanya normal lagi.
   - Beda dengan abu-abu di Guessing Game kemarin (kode yang tidak akan pernah dijalankan / unreachable). Dua-duanya cuma pengingat editor, bukan error.

6. Rentang angka tiap level
   - Saya sempat mau pakai `randint(level, 10)`. Salah. Level 2 harusnya 10–99, bukan 2–10.
   - Saya tanya ke Duck: 0 itu positif? Bukan, 0 itu netral. Tapi soalnya bilang **non-negative**, jadi 0 termasuk. Level 1 = 0–9, level 2 = 10–99, level 3 = 100–999.
   - generate_integer mengembalikan **satu** angka (dari namanya, integer tunggal). Main yang memanggilnya dua kali untuk X dan Y.
   - Sempat typo `ranndint`.

7. raise atau except untuk jawaban bukan angka?
   - Saya sempat mau pakai raise. Duck bertanya: siapa yang sudah melempar error waktu `int("abc")`? Python sendiri. Jadi tugas saya cuma **menangkap**, pakai try/except.
   - raise dipakai kalau saya yang mau membuat error. except dipakai kalau mau menangkap error supaya program tetap jalan.

8. input boleh pakai f-string
   - `input(f"{x} + {y} = ")` boleh, karena input menerima string apa saja sebagai prompt.

9. Soal tidak berganti
   - X dan Y saya buat sekali di luar loop, jadi soalnya sama terus. Pembuatan soal harus di dalam loop 10 soal.

10. `total =+ 1`
    - Dibaca Python sebagai `total = +1` (positif satu). Jadi total selalu 1. Yang benar `+=`.

11. Loop di dalam loop
    - for 10 kali untuk soal, di dalamnya for 3 kali untuk kesempatan. Kalau benar, break keluar dari loop kesempatan, lanjut ke soal berikutnya.
    - print skor ditaruh paling akhir, sejajar dengan for 10 soal, tetap di dalam main. Kalau di atas, skornya tampil duluan sebelum soal dikerjakan.

12. while True + for 10 → tidak berhenti
    - Di terminal saya hitung, sudah lebih dari 10 soal kok belum berhenti. Ternyata gara-gara while True di luar for. for range(10) sudah otomatis berhenti setelah 10 kali, jadi while True tidak perlu. Saya hapus.

13. Variabel `salah` harus di-reset di dalam loop 10 soal
    - Kalau `salah = 0` ditaruh di luar loop, nilainya menumpuk antar soal. Misalnya soal pertama salah 3 kali → salah = 3, `if salah == 3` jalan. Soal kedua salah lagi → 4, 5, 6. `salah == 3` tidak akan pernah benar lagi, jadi jawaban benar tidak pernah ditampilkan.
    - Kalau `salah = 0` di dalam loop 10 soal (sebelum loop 3 kesempatan), setiap soal baru mulai dari nol lagi.
    - Variabel yang dibuat `= 0` di dalam loop akan kembali ke nilai semula setiap kali loop berulang.

14. Pemanggilan dari file lain?
    - Saya tanya Duck: function mana yang dipanggil file lain? Di soal ini tidak disebutkan. Tapi karena wajib ada `if __name__ == "__main__":`, file ini memang disiapkan untuk bisa di-import.

### Setelah check50 hijau: dua hal yang ternyata belum sesuai soal

1. generate_integer tidak me-raise ValueError
   - Saya sempat menyimpulkan: "yang diminta soal belum tentu harus dijalankan", karena saya tidak pakai raise sama sekali tapi tetap hijau. **Kesimpulan ini salah.** Soalnya bilang raise ValueError kalau level bukan 1, 2, 3. Itu syarat. check50 hijau karena kasus itu tidak dites.
   - Saya buktikan sendiri: bikin `percobaan.py` yang meng-import generate_integer, lalu `print(generate_integer(4))`. Hasilnya `None`. Karena perbandingan saya cuma sampai 3, kalau bukan 1/2/3 tidak ada yang di-return.
   - Saya tambahkan else yang me-raise ValueError. Dijalankan lagi, traceback-nya:
     ```
     File ".../percobaan.py", line 2       ← pemanggil
     File ".../professor.py", line 62      ← tempat raise
     ValueError: Error
     ```
   - Ini bukti mekanisme raise: error **dibuat** di professor.py, lalu **dilempar ke pemanggilnya** (percobaan.py). Karena tidak ada yang menangkap, crash. Traceback itu dibaca seperti jejak perjalanan bola.
   - Bonus: waktu di-import, main() tidak ikut jalan dan saya tidak ditanya Level. Bukti `if __name__ == "__main__":` saya bekerja. percobaan.py yang meng-import professor.py itu persis pelajaran custom library (sayings.py) di lecture.
   - Ini sudah ketiga kalinya minggu ini: **check50 hijau belum tentu semua aturan soal terpenuhi** (figlet tiga argumen, Guessing Game level 0, Little Professor raise).

2. Jawaban bukan angka tidak dihitung salah
   - Claude minta saya coba jawab `cat`, `cat`, `cat` di satu soal. Saya awalnya bingung, ini di level atau di soal matematika? Maksudnya di soal matematika.
   - Masalahnya: di `except ValueError`, variabel `salah` tidak ditambah. Jadi tiga kali jawab bukan angka, jawaban benar tidak ditampilkan. Padahal soalnya bilang "not correct (or not even a number)".
   - Saya perbaiki dengan menambah salah juga di except. Sekarang angka yang keliru maupun bukan angka sama-sama dihitung.

### Yang saya pelajari
- Fokus dulu: setiap function tugasnya apa.
- Parameter = bahan dari luar, return = hasil yang diserahkan kembali.
- `UnboundLocalError`: memakai variabel di sisi kanan `=` sebelum variabel itu pernah dibuat.
- `=+` itu bukan `+=`.
- for untuk jumlah pasti (10 soal, 3 kesempatan), while True untuk "sampai valid".
- Variabel penghitung per soal di-reset di dalam loop soal.
- raise untuk melempar error sendiri, try/except untuk menangkap.
- Yang diminta soal itu syarat, walaupun check50 tidak mengetesnya.

## 6. Bitcoin Price Index — selesai, check50 hijau semua 6/6 (15 Oktober 2026)

Yang diminta soal:
- User mengetik jumlah bitcoin di command line, misalnya `python bitcoin.py 2.5`.
- Kalau tidak ada argumen → exit `Missing command-line argument`. Kalau bukan angka → exit `Command-line argument is not a number`.
- Ambil harga bitcoin dari API CoinCap, lalu tampilkan harga n bitcoin dalam USD, 4 angka desimal, koma sebagai pemisah ribuan. Contoh `$38,761.0833`.
- Tangkap `requests.RequestException`.

### Daftar API key dulu
- API lama yang dulu dipakai soal ini sudah tidak bisa (CoinCap v2 dihentikan). Soalnya sudah diganti ke CoinCap v3, yang **wajib pakai API key**.
- Jadi harus bikin akun CoinCap dulu, lalu klik "Add New Key" di dashboard. Ini praktik langsung pelajaran "kartu anggota" dari lecture.
- Sempat bingung email konfirmasinya tidak masuk ke Gmail. Tips dari Claude: cek folder Spam/Promosi/Pembaruan, cari "coincap", cek apakah daftarnya pakai email lain (Outlook), tunggu beberapa menit.

### Perjalanan dan yang membuat saya tersendat
- Banyak yang lupa: cara mengambil API, requests.get, sys.argv. Saya buka lagi catatan Week 4 saya di GitHub dan video David Malan.

1. URL belum dibungkus tanda kutip
   - `SyntaxError: invalid decimal literal`, lalu `expression cannot contain assignment, perhaps you meant "=="?`. Python mengira URL itu kode, dan `=` di `apiKey=` dikira assignment.
   - Saya juga sempat salah tulis `/apiKey=` padahal yang benar `?apiKey=`. Sesudah `?` itu parameter.

2. `requests.exceptions.MissingSchema: Invalid URL ... No scheme supplied`
   - URL kurang `https://` di depannya. Error ini milik library requests. Baris terakhirnya bahkan kasih saran: "Perhaps you meant https://...".
   - Tips dari Duck: selalu baca baris paling terakhir traceback, di situ inti masalahnya.

3. Lihat dulu bentuk JSON-nya
   - Sesudah URL benar, saya print `response.json()`. Kelihatan ada key `data`, isinya dictionary lagi, di dalamnya ada `priceUsd`.
   - Lalu saya pakai `json.dumps(..., indent=2)` supaya tampilannya rapi, persis seperti di lecture.

4. `TypeError: 'Response' object is not subscriptable`
   - Saya tulis `response["data"]`. Padahal response itu objek dari requests, belum dictionary. Harus diubah dulu pakai `.json()`.

5. `TypeError: string indices must be integers, not 'str'`
   - Saya simpan hasil `json.dumps(...)` ke variabel data, lalu `data["data"]`. Ternyata json.dumps hasilnya **string**, bukan dictionary. String tidak bisa dibuka pakai `["data"]`.

6. `KeyError: 'priceUsed'`
   - Nama key-nya `priceUsd` (singkatan USD), bukan priceUsed. Salah satu huruf saja langsung KeyError.

7. Mengetik `cat` sendirian di terminal, layarnya kosong
   - Saya kira program saya yang salah. Ternyata `cat` itu **perintah Linux** (untuk menampilkan isi file). Kalau diketik tanpa nama file, dia diam menunggu ketikan, harus Ctrl+C. Yang benar `python bitcoin.py cat`.

8. Cek argumen pakai `if not float(sys.argv)`?
   - Salah, karena sys.argv itu list, bukan satu nilai. Yang dicek jumlahnya pakai `len(sys.argv)`: 1 berarti cuma nama file, user lupa mengetik angka.
   - Kalau user mengetik `cat`, `float("cat")` langsung ValueError, ditangkap except.

9. Cara menghitung
   - priceUsd itu harga untuk 1 bitcoin. Jadi jumlah dari user **dikali** priceUsd. 2.5 bitcoin = 2.5 × priceUsd.

10. `TypeError: can't multiply sequence by non-int of type 'float'`
    - Sempat `sys.argv[1] * price` (string dikali), lalu sesudah jadi float masih error. Ternyata `priceUsd` dari API itu **string**, lihat tanda kutipnya di JSON, padahal soalnya bilang "as a float". Harus diubah jadi float juga.
    - "sequence" di pesan error itu maksudnya string (string itu urutan karakter).

11. Format output
    - Pakai trik f-string dari Week 0: `:,` untuk koma ribuan dan `.4f` untuk 4 angka desimal, digabung jadi satu.

12. check50: `expected exit code 1, not 0`
    - Di except ValueError saya pakai print. Tulisannya sama persis, tapi program selesai dengan normal (exit code 0 = berhasil). Harus pakai `sys.exit("pesan")` supaya exit code-nya 1 (gagal). Sama dengan pelajaran figlet. Sesudah diganti, hijau semua.

### Kenapa `import json` abu-abu?
- Karena module json tidak dipakai lagi. Tadinya saya pakai json.dumps untuk melihat bentuk data, tapi baris itu sudah dihapus. Jadi `import json` boleh dihapus.
- `response.json()` itu **bukan** module json. Itu method milik objek response dari requests. Namanya sama, pemiliknya beda, pelajaran namespace lagi.

| | Pemiliknya | Tugasnya | Hasilnya |
|---|---|---|---|
| `response.json()` | objek response (requests) | mengubah jawaban server jadi dictionary | dictionary |
| `json.dumps(...)` | module json | mengubah dictionary jadi teks rapi | string |

- json itu module bawaan Python, tidak perlu pip. Yang perlu pip itu requests.
- `requests.RequestException` itu nama error juga, tapi milik library requests, bukan bawaan Python. Muncul kalau ada masalah waktu mengirim request (internet putus, server mati, timeout).

### API key jangan disebar
- API key saya sempat terlihat di screenshot dan di percakapan dengan Duck (percakapan Duck dicatat). Sesuai pelajaran "kartu anggota": sebaiknya buat key baru di dashboard CoinCap, pasang di kode, baru hapus key yang lama.
- Hati-hati urutannya: kalau key lama dihapus tapi kode masih pakai key lama, error-nya bukan RequestException. Server tetap menjawab, cuma isinya penolakan dan tidak ada `"data"`, jadi errornya muncul di baris `data["data"]`.
- API key tidak boleh ditulis di catatan GitHub ini, karena repo-nya publik.

### Setelah lulus: diskusi kerapian kode dengan Claude
Kode saya sudah lulus, ini soal kerapian. Menurut saya kode saya sendiri lebih mudah dibaca, tapi ada beberapa kemungkinan masalah:

1. **Urutan pengecekan.** Sekarang program menghubungi API dulu, baru cek argumen. Kalau user lupa mengetik angka atau mengetik `cat`, request-nya terbuang percuma (dan memakai kuota API key).
   - Pengecekan argumen tidak butuh data dari API sama sekali, cuma melihat yang diketik user. Jadi bisa dikerjakan duluan.
   - Data tetap dibuat sebelum dipakai, jadi aturan "Python membaca dari atas ke bawah" tetap aman.
   - Ibarat mau belanja ke pasar: pastikan dulu daftar belanjanya ada, baru berangkat. Kalau daftarnya kosong, tidak usah ke pasar.
   - Urutan yang lebih rapi: (1) cek argumen ada atau tidak, (2) ubah ke float, kalau gagal exit, (3) baru request ke API, (4) ambil priceUsd, kalikan, print.

2. **Satu try besar dipecah jadi dua try kecil.** Sesuai saran David (sudah ada di catatan Pset 3): try sebaiknya cuma berisi baris yang memang bisa error. Ada dua sumber error yang berbeda: float() → ValueError, requests.get() → RequestException. Masing-masing dapat try sendiri. Ibarat halaqah: setiap musyrif mengawasi kelompoknya sendiri.
   - Bahaya satu try besar: misalnya `float(price)` gagal karena data dari API aneh, yang tertangkap juga except ValueError, dan pesannya jadi "Command-line argument is not a number". Pesannya menyesatkan, padahal yang salah bukan argumen user.

3. **`except requests.RequestException: pass`.** Kalau internet putus, user cuma lihat layar kosong, dan program keluar seolah berhasil. Lebih baik sys.exit dengan pesan.
   - Pesannya jangan terlalu spesifik seperti "internet putus", karena RequestException menangkap banyak kemungkinan penyebab. Pesan umum lebih jujur, misalnya `Could not get Bitcoin price`.

### Yang saya pelajari
- Lihat dulu bentuk JSON-nya sebelum menulis program.
- URL di requests.get harus string lengkap dengan `https://`.
- `.json()` dulu, baru bisa dibuka pakai `[...]`.
- json.dumps hasilnya string, cuma untuk dilihat, bukan untuk diambil isinya.
- Data dari API bisa berupa string walaupun isinya angka. Cek tanda kutipnya.
- print vs sys.exit: tulisannya sama, exit code-nya beda.
- `cat` itu perintah Linux.
- API key jangan disebar.

### Jenis error yang sudah saya kenal (update)
- Baru di Pset 4 hari ini: `UnboundLocalError`, `requests.exceptions.MissingSchema`, `TypeError: 'Response' object is not subscriptable`, `TypeError: string indices must be integers`, `TypeError: can't multiply sequence by non-int of type 'float'`.
- Pesan check50 baru: `expected exit code 1, not 0`.

### Yang ingin dicoba
- Susun ulang bitcoin.py sesuai urutan yang lebih rapi (cek argumen dulu, dua try terpisah, RequestException pakai sys.exit). Tes kosong, `cat`, `1`, `2.5`, lalu check50 lagi.
- Ganti API key dengan yang baru, hapus yang lama.

## Penutup Problem Set 4 — selesai semua (15 Oktober 2026)

Enam soal selesai dalam tiga hari: Emojize, Frank Ian and Glen's Letters, Adieu Adieu, Guessing Game, Little Professor, Bitcoin Price Index.

Pelajaran paling besar minggu ini:
- **Baca dokumentasi sendiri.** Emojize selesai tanpa Duck karena ketemu `language="alias"` di dokumentasi. Figlet dokumentasinya kurang jelas, akhirnya pakai `help()` dan `dir()`.
- **check50 hijau belum tentu semua aturan soal terpenuhi.** Tiga kali kejadian: figlet (tiga argumen), Guessing Game (level 0), Little Professor (raise). Harus tes sendiri kasus-kasus yang aneh.
- **print vs sys.exit vs raise.** Tulisan di layar bisa sama, tapi cara keluarnya beda.
- **Objek dan method.** Figlet, inflect engine, string, list, response: semua objek, punya method sendiri. Nama method boleh sama (join, json), yang menentukan itu objek sebelum titiknya.
- **API.** Akhirnya praktik langsung: daftar API key, request, baca JSON, ambil nilai bersarang.
