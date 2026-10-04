# CS50P Week 3: Exceptions

## Hari 1 – 4 Oktober 2026

Menonton lecture sampai sekitar menit 20 (bagian try, except, else).

### Pemanasan sebelum menonton
- Pertanyaan: di soal Coke saya menulis `int(input(...))`. Kalau user mengetik `cat`, apa yang terjadi?
- Jawabannya ternyata error baru: ValueError.

### ValueError
- `int("cat")` menghasilkan `ValueError: invalid literal for int() with base 10: 'cat'`.
- Artinya: tulisan 'cat' tidak bisa diubah jadi angka biasa.
- "Literal" artinya apa yang benar-benar diketik. "Base 10" artinya sistem bilangan biasa (0 sampai 9).
- Beda dengan TypeError: TypeError itu jenis datanya salah, ValueError itu jenisnya benar tapi isinya tidak masuk akal.

### f-string dan interpolate
- "Interpolate" artinya menyisipkan nilai variabel ke dalam teks.
- `print("x is {x}")` tanpa huruf f tidak menyisipkan apa-apa. Harus `print(f"x is {x}")`.

### try dan except
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```
- try: coba jalankan baris ini.
- except ValueError: kalau muncul ValueError, jalankan ini, jangan berhenti dengan error.
- Begitu ada error di satu baris dalam try, sisa baris di dalam try langsung dilewati, lalu loncat ke except.
- Setelah except selesai, Python lanjut normal ke baris di bawahnya.

### Saran David soal except (menit 12.11 sampai 13.07)
- Bisa menulis `except:` saja tanpa nama error, supaya semua error ditangkap. Tapi itu bad practice dan lazy, karena bisa menyembunyikan bug lain. Kalau tidak tahu apa yang salah, bagaimana bisa menanganinya dengan benar?
- Lebih baik sebutkan jenis error-nya secara jelas, seperti `except ValueError:`.
- Masalahnya, dokumentasi Python tidak selalu memberi tahu error apa saja yang mungkin muncul. Jadi sarannya agak bertentangan (contradictory): sebutkan error spesifik, padahal tidak selalu jelas error apa yang harus disebutkan.
- Solusinya: makin sering latihan, makin hafal. Kadang dokumentasi juga menyebutkannya.
- Seperti musyrif: yang baik mencari tahu masalah spesifik santri. Yang malas bilang "pokoknya ulang dari awal" untuk semua masalah.

### try sebaiknya pendek
- try sebaiknya hanya membungkus baris yang memang bisa error.
- Kalau terlalu banyak baris dibungkus, tidak jelas baris mana yang ditangani, dan bisa ikut menyembunyikan error lain.

### NameError karena urutan pengerjaan
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
- Kalau user mengetik cat, hasilnya "x is not an integer" lalu `NameError: name 'x' is not defined`.
- Awalnya saya kira karena scope: x dibuat di dalam try, jadi tidak bisa dipakai di luarnya. Mahasiswa di video juga menebak begitu, David bilang good instincts, tapi bukan itu penyebabnya. try tidak seperti function. Variabel yang dibuat di dalam try tetap bisa dipakai di luarnya.
- Buktinya: kalau inputnya 50, hasilnya `x is 50`, padahal print ada di luar try.
- Penyebab sebenarnya: urutan pengerjaan (order of operations). Baris `x = int(input(...))` dikerjakan dari kanan ke kiri:
  1. input() minta ketikan user → "cat"
  2. int() mengubah jadi angka → gagal, ValueError
  3. x = ... menyimpan ke x → tidak pernah terjadi
- Jadi x tidak pernah dibuat. Waktu print di luar try memanggil x, muncul NameError.
- Kalau print ada di dalam try, tidak error, karena print ikut dilewati.
- Seperti buku mutaba'ah: nilai baru ditulis kalau setoran sah. Setoran gagal di tengah, kolom nilai tidak pernah diisi. Bukan karena bukunya di ruangan lain (scope), tapi karena memang tidak pernah ditulis.
- ValueError biasanya karena nilai dari user. NameError biasanya karena kodenya sendiri, memakai nama variabel dengan cara yang tidak seharusnya.

### else di try
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
- try selalu dicoba lebih dulu.
- Ada error → except jalan, else dilewati.
- Tidak ada error → except dilewati, else jalan.
- except dan else itu pasangan, hanya salah satu yang jalan.
- else tidak menangkap error. else = tempat untuk baris yang hanya boleh jalan kalau try berhasil.
- Kalau try berhasil, x pasti sudah ada, jadi NameError tidak mungkin terjadi.
- Versi ini mengambil kelebihan dua versi sebelumnya: try tetap pendek, dan tidak ada NameError.
- Seperti setoran: nasihat murojaah (except) kalau salah, tulis nilai (else) kalau lancar. Tidak mungkin dua-duanya.

### else di if dan else di try
- Benang merahnya sama: else jalan kalau yang di atasnya tidak terjadi.
- Di if/elif, else jalan kalau tidak ada syarat yang True. Seperti kolom "lain-lain" (catchall).
- Di try, else jalan kalau except tidak terjadi, artinya try berhasil tanpa error.
- Bedanya: isi if belum tentu dijalankan, tapi isi try selalu dicoba dulu.

### Kosakata
- somehow: entah bagaimana caranya.
- somewhere: di suatu tempat.
- somewhat: agak (bukan "sesuatu").
- interpolate: menyisipkan nilai variabel ke dalam teks.
- mouthful: kalimat yang panjang dan ribet diucapkan.
- roughly: kira-kira, garis besarnya.
- proactively: sebelum diminta, bertindak lebih dulu. Lawannya reactively.
- invariably: selalu, tanpa kecuali.
- contradictory: saling bertentangan.
- raise (error): memunculkan error, bukan "menaikkan". DeepL sempat salah menerjemahkan jadi "dinaikkan".
- shouldn't: should not, tidak seharusnya. "that you shouldn't [do]", kata kerjanya dihilangkan.
- boil down to: intinya adalah. Arti asalnya merebus sampai tinggal sarinya.
- kind of: semacam, bisa dibilang.
- catchall: penampung semua sisa, seperti kolom "lain-lain".

### Jenis error yang sudah saya kenal
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError.

### Yang ingin dicoba
- Jalankan tiga versi kode (print di dalam try, di luar try, di else) dengan input 50 dan cat, bandingkan hasilnya.
- Lanjutkan video dari menit 20: membuat program terus bertanya sampai user mengetik angka.
