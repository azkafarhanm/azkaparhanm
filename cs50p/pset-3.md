# Problem Set 3

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

Mulai Problem Set 3, petunjuk saat mengerjakan soal saya minta ke CS50 Duck, bukan ke AI lain. Claude saya pakai untuk murojaah lecture sebelum mulai, dan untuk membahas kode setelah submit.

## Pemanasan sebelum mulai (6 Oktober 2026 pagi)

Murojaah Lecture 3 dulu, enam pertanyaan dari Claude, dijawab tanpa buka catatan.

Yang sudah benar:
- except jalan kalau ada error, else jalan kalau try berhasil. Hanya salah satu yang jalan.
- pass dipakai karena sesudah `except ...:` wajib ada minimal satu baris yang menjorok.
- `"-5".isnumeric()` hasilnya False.
- `print(10 / 0)` saya tebak, lalu saya buktikan sendiri: ternyata ZeroDivisionError. Error baru, tidak bisa membagi dengan nol.

Yang dikoreksi:
- except tidak otomatis menampilkan pesan yang ramah. except cuma menjalankan apa pun yang saya tulis di dalamnya, bisa print, bisa juga pass.
- Waktu menebak hasil loop, saya lupa menyebut apa yang terjadi setelah user mengetik angka yang benar. Harus ditelusuri sampai program selesai.
- break tidak jalan bukan karena "variabelnya tidak terdeklarasi", tapi karena error di baris int() langsung melompat ke except, jadi break di bawahnya dilewati.
- `except:` tanpa nama error itu bad practice karena menangkap semua error, termasuk bug lain yang tidak saya duga. Bug-nya jadi tersembunyi.
- `int("-5")` hasilnya -5 (angka), bukan True.

## Perkenalan untuk CS50 Duck

Saya tempel di awal setiap percakapan baru dengan Duck, karena belum tentu Duck ingat percakapan lama:

```
Halo Duck! Sebelum mulai, perkenalan singkat tentang saya:

- Saya pemula total, tanpa latar belakang IT. Saya guru tahfidz di sebuah sekolah, dan sedang belajar CS50P untuk menjadi AI engineer.
- Saya akan bertanya dalam bahasa Indonesia. Tolong jawab dalam bahasa Indonesia yang sederhana, tapi istilah teknis (seperti loop, return, except) tetap dalam bahasa Inggris.
- Kalau menjelaskan istilah teknis, tolong pakai analogi sehari-hari yang sederhana.

Cara membantu yang saya inginkan:
- Jangan beri kode atau jawaban. Bimbing saya dengan pertanyaan, satu petunjuk kecil setiap kali.
- Biarkan saya mencoba dulu. Kalau saya salah, minta saya menelusuri kode dengan tangan memakai contoh kecil, supaya saya menemukan kesalahannya sendiri.
- Sesekali minta saya menjelaskan ide saya dengan kata-kata sendiri, untuk mengecek apakah saya benar-benar paham.

Terima kasih!
```

## 1. Fuel Gauge — selesai, check50 hijau semua 11/11 (6 Oktober 2026)

Yang diminta soal:
- User mengetik pecahan dengan format X/Y, misalnya 3/4.
- Program menampilkan berapa persen isi tangki bensinnya, dibulatkan ke bilangan bulat terdekat.
- Kalau 1% atau kurang, tampilkan E (empty, kosong).
- Kalau 99% atau lebih, tampilkan F (full, penuh).
- Kalau X atau Y bukan bilangan bulat, Y-nya 0, atau X lebih besar dari Y, program harus bertanya lagi (reprompt).

Rencana awal saya:
- Pisahkan input jadi X dan Y pakai split di tanda garis miring.
- Ubah X jadi integer, Y jadi integer, X dibagi Y, lalu dikali 100.
- Hasilnya dibungkus pakai round, lalu disimpan di variabel namanya persentase.
- Semuanya dibungkus try, lalu except untuk error yang mungkin muncul dari input.

### Perjalanan dan yang membuat saya tersendat

1. NameError di versi awal
   - Waktu awal, baris perhitungan persentase saya taruh di luar try. Hasilnya `NameError: name 'persentase' is not defined`.
   - Ini persis contoh David di lecture: kalau print ada di bawah except, dia mencetak variabel yang memang tidak pernah dibuat.
   - Dari sini saya baru sadar lagi kenapa else di try itu penting. Kalau try berhasil, except tidak loncat, jadi masuk ke else. Kalau try gagal, except yang jalan dan else tidak dijalankan. else jalan kalau semua kemungkinan di atasnya tidak berlaku.
   - Ternyata else di try itu keyword yang agak khusus, beda rasanya dengan else di if.

2. Bingung arti "1% atau kurang"
   - Saya tanya ke Duck maksudnya apa. Ternyata artinya persentase kurang dari atau sama dengan 1, operatornya `<=`.
   - Duck juga bertanya balik: apakah pengecekan if itu baris yang bisa menyebabkan error? Kalau tidak, tidak perlu ada di dalam try. Ini sesuai saran David, try sebaiknya cuma berisi baris yang memang bisa error.

3. check50 merah di 10/3 dan -1/4
   - Pesannya: `expected program to reject input, but it did not`. Program saya malah menerima. 10/3 jadi F, -1/4 jadi E.
   - Awalnya saya bingung kenapa harus reprompt. Kan sesuai aturan, kurang dari 1 jadi E, lebih dari 99 jadi F.
   - Lalu saya bingung lagi: secara matematis 10/3 dan -1/4 itu bisa dihitung. Secara sistem tidak ada nama error khusus untuk menangkapnya. Jadi menangkapnya bagaimana?
   - Ternyata ini pelajaran besar. try/except hanya menangkap hal yang Python tidak bisa lakukan, misalnya mengubah "cat" jadi angka, atau membagi dengan nol. Kalau Python bisa menghitungnya, tidak ada error. Yang membuat 10/3 dan -1/4 "salah" itu aturan soalnya sendiri (tangki tidak mungkin lebih dari penuh, bensin tidak mungkin negatif). Itu namanya error logika, dan harus saya cek sendiri pakai if.
   - Kalau error dari Python, gampang, tinggal sebut namanya di except. Yang agak ribet itu error logika, karena programnya tetap jalan.

4. TypeError karena membandingkan string dengan int
   - Waktu menambahkan pengecekan, muncul `TypeError: '<' not supported between instances of 'str' and 'int'`.
   - Saya kira X dan Y sudah integer. Padahal belum. Yang integer cuma yang ada di dalam rumus persentase. X dan Y-nya sendiri masih string hasil split.
   - Ini pelajaran yang sama dengan twttr: `c.lower()` tidak mengubah c. `int(x)` juga tidak mengubah x, kecuali hasilnya disimpan lagi pakai `=`.
   - Duck menyarankan `print(type(x))` sebelum baris yang error, untuk melihat tipe datanya yang sebenarnya.

5. 4/2 malah jadi F, padahal harusnya ditolak
   - Ada dua kesalahan sekaligus: masih membandingkan string dengan string, dan operatornya terbalik. Syaratnya X tidak boleh lebih besar dari Y, jadi yang ditolak itu kalau X lebih besar, bukan lebih kecil.
   - Penelusuran saya: "4" < "2" sebagai string hasilnya False. Syarat lainnya juga False, karena X dan Y bukan minus. Semua False, lalu ditambah not jadi True. Karena True, program jalan ke bawah, persentasenya 200, jadilah F.

6. Membandingkan string dengan string (leksikografis)
   - Kalau string dibandingkan pakai < atau >, Python membandingkannya seperti urutan kamus, huruf per huruf dari kiri.
   - Huruf yang lebih awal di abjad dianggap lebih kecil. Jadi "a" < "c" hasilnya True.
   - Bahayanya: "10" < "9" hasilnya True, karena yang dibandingkan karakter pertama, "1" dengan "9". Padahal sebagai angka 10 lebih besar dari 9.
   - "4" < "2" hasilnya False. Untuk satu digit kebetulan hasilnya sama dengan angka, tapi tidak selalu begitu.
   - Kesimpulan: untuk membandingkan nilai angka, pastikan dua-duanya sudah int.

7. Terjebak looping terus
   - Waktu input 0/100, program mencetak E, lalu bertanya lagi, E lagi, bertanya lagi, terus-terusan.
   - Penyebabnya penempatan break. break saya taruh hanya di bawah print persentase biasa. Jadi kalau yang tercetak E atau F, baris break itu tidak pernah dijalankan, dan loop terus berputar.
   - Prinsipnya: kalau print di cabang atasnya sudah dieksekusi, cabang lain di bawahnya tidak jalan. Kalau break ikut di dalam cabang yang tidak jalan, break-nya juga tidak jalan. Jadi break saya geser supaya tetap jalan apa pun yang tercetak (E, F, atau persen).
   - Sempat juga pengecekan "X > Y dan negatif" saya taruh di luar loop. Akibatnya -1/2 lolos dari try tanpa error, masuk else, break, loop selesai. Baru dicek di luar loop, padahal sudah tidak bisa bertanya lagi. Pengecekan yang menentukan harus reprompt atau tidak harus ada di dalam loop, sebelum break.

8. Terminal masih menjalankan kode lama
   - Waktu terminal sedang looping, saya ubah kodenya di VS Code. Saya kira kalau saya ketik input yang benar, dia akan break sesuai kode baru. Ternyata masih looping terus.
   - Ternyata program yang sedang jalan itu memakai kode saat dia dijalankan. Mengubah file tidak mengubah program yang sudah jalan.
   - Harus di-interrupt dulu pakai Ctrl+C, baru jalankan ulang. Barulah kode baru yang berjalan.

### Yang saya pelajari
- Satu except bisa menangkap beberapa jenis error sekaligus, dengan menulis nama-nama error-nya di dalam kurung, dipisah koma.
- Error dari Python ditangkap pakai try/except. Error logika (aturan soal) dicek sendiri pakai if.
- `int(x)` tidak mengubah x. Hasilnya harus disimpan kalau mau dipakai lagi.
- String dibandingkan secara leksikografis, bukan sebagai angka.
- Posisi break menentukan kapan loop berhenti. Pengecekan yang menentukan reprompt harus ada di dalam loop.
- Kalau mengubah kode, hentikan dulu program yang sedang jalan (Ctrl+C), baru jalankan ulang.
- Duck juga menyarankan debugging pakai print: selipkan `print("masuk else")` atau `print(type(x))` di beberapa tempat sebagai jejak, untuk melihat baris mana yang benar-benar dilewati. Belum saya coba, mau dicoba di soal berikutnya.

### Salah yang saya buat
- Perhitungan persentase di luar try, kena NameError.
- Membandingkan X dan Y yang masih string.
- Operator perbandingan terbalik (< padahal seharusnya >).
- Pengecekan X > Y dan negatif sempat ada di luar loop, jadi tidak bisa reprompt.
- break cuma di satu cabang, jadi E dan F terus looping.
- Mengubah kode tanpa menghentikan program yang sedang jalan.

### Setelah submit, murojaah kode dengan Claude
1. int() cukup sekali
   - Saya menulis int(x) dan int(y) total enam kali.
   - Lebih rapi kalau X dan Y langsung diubah jadi integer sekali setelah di-split, lalu baris-baris berikutnya tinggal pakai X dan Y yang sudah angka.
   - Baris yang mengubah ke integer itu tetap harus di dalam try, karena bisa error kalau user mengetik cat/dog.

2. Perbandingan berantai
   - Python bisa menulis perbandingan berantai seperti di matematika SD. Contoh: `0 <= nilai <= 100` artinya nilai tidak kurang dari 0 dan tidak lebih dari 100. Sama artinya dengan pakai and, tapi lebih ringkas.
   - Saya coba di interactive mode: nilai 85 hasilnya True, nilai 120 hasilnya False.
   - Syarat saya sebelumnya ditulis dari sisi "kapan pecahannya salah", lalu dibalik pakai not. Berbelit.
   - Lebih mudah dibaca kalau ditulis dari sisi "kapan pecahannya benar": X tidak negatif, dan X tidak lebih besar dari Y. Jadi tinggal berantai: 0, lalu X, lalu Y, berurutan dari kecil ke besar. Tidak perlu and, tidak perlu not.
   - Lalu Y negatif bagaimana? Saya telusuri secara deduktif: kalau X sudah pasti minimal 0, dan Y harus lebih besar atau sama dengan X, berarti Y juga minimal 0. Tidak mungkin minus. Jadi pengecekan Y negatif sudah otomatis tercakup, tidak perlu ditulis terpisah.

3. Tingkatan kode
   - Kode saya bertingkat tiga (else, lalu if not, lalu if/elif/else). Setelah dua perubahan di atas, tingkatannya bisa dikurangi.

Cara pakai interactive mode yang benar (saya sempat salah):
- Tanda `>>>` itu bukan bagian dari kode, itu tanda Python sedang menunggu ketikan. Kalau ikut disalin, jadi SyntaxError.
- Ketik satu baris, Enter, satu baris lagi, Enter. Jangan menempel beberapa baris sekaligus.
- Kalau muncul `...` padahal tidak sedang menulis if/for/while, tekan Enter kosong atau Ctrl+C. Keluar pakai `exit()`.

### Yang ingin dicoba
- Tulis versi rapinya di fuel2.py, lalu jalankan check50 lagi, pastikan tetap 11/11.
- Coba di interactive mode: `"Z" < "a"` dan `"10" < "9"`. Tebak dulu sebelum menjalankan.
- Coba debugging pakai print di soal berikutnya.

### Jenis error yang sudah saya kenal
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError, ZeroDivisionError.
- TypeError ternyata juga muncul kalau membandingkan string dengan int pakai < atau >.
