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

## 2. Felipe's Taqueria — selesai, check50 hijau semua 7/7 (7 Oktober 2026)

Yang diminta soal:
- Ada menu makanan dalam bentuk dictionary: nama makanan sebagai key, harganya sebagai value.
- User mengetik nama makanan satu per satu.
- Setiap kali user mengetik makanan yang ada di menu, program menampilkan total harga semua makanan yang sudah dipesan sejauh ini, dengan format dolar dan dua angka di belakang koma.
- Huruf besar kecil tidak berpengaruh (burrito, Burrito, bUrrito dianggap sama).
- Kalau makanannya tidak ada di menu, abaikan saja dan tanya lagi.
- Program berhenti kalau user menekan Ctrl+D.

Rencana saya:
- Buat variabel penanda namanya celengan, isinya 0, untuk menyimpan total.
- Loop terus: minta input makanan, rapikan hurufnya supaya cocok dengan key di dictionary.
- Kalau ada di menu, harganya ditambahkan ke celengan, lalu tampilkan totalnya.
- Kalau user menekan Ctrl+D, keluar dari loop.

### Perjalanan dan yang membuat saya tersendat

1. Error kecil di awal
   - `While True:` pakai W besar, jadinya SyntaxError. Keyword Python huruf kecil semua: while.
   - `IndentationError: unexpected indent`, ada baris yang menjorok padahal tidak seharusnya.
   - `print("Total:", menu[item"])`, tanda kutip nyasar di dalam kurung siku. Hasilnya `SyntaxError: unterminated string literal`, artinya ada string yang dibuka tapi tidak ditutup.
   - Waktu menekan Ctrl+C, muncul `KeyboardInterrupt`. Itu bukan bug, memang program saya hentikan paksa.

2. Bingung memakai method get di dictionary
   - Di soal ada pembahasan soal get. Saya sempat baca dokumentasi Python, tapi jujur kurang paham. Akhirnya saya dibantu Duck.

3. Salah yang di-print: harga atau total
   - Awalnya saya menampilkan harga makanannya, bahkan sempat menampilkan harga dan celengan dua-duanya.
   - Ternyata yang diminta itu total, yaitu isi celengan, bukan harga satu makanan. Celengan itu variabel penanda yang menyimpan jumlah semua yang sudah dipesan.
   - Format juga harus pakai tanda dolar dan dua angka desimal. Awalnya keluar `Total: 4.25` tanpa tanda dolar.

4. Kalimat soal yang membuat saya bingung
   - "After each inputted item, display the total cost of all items inputted thus far." Artinya setiap selesai satu makanan dimasukkan, langsung tampilkan total sementara. Thus far = sejauh ini, sampai sekarang.
   - Saya bingung meletakkan print totalnya di mana.

5. Salah letak print total: di luar loop
   - Awalnya print total saya taruh di luar loop. Hasilnya total cuma muncul sekali, setelah saya menekan Ctrl+D. Urutannya terbalik.
   - check50 merah di semua tes harga, pesannya `Did not find "$14.00" in "Item: "`. Artinya check50 mencari total sesudah input, tapi yang ketemu cuma tulisan "Item: ".
   - Penjelasan saya sendiri: kalau print ada di luar loop, Ctrl+D cuma menghentikan loop-nya. Python tetap lanjut membaca kode di bawah loop. Jadi print yang di luar loop itulah yang terakhir tampil di terminal.
   - Setelah print total saya pindahkan ke dalam loop, tepat sesudah harga ditambahkan ke celengan, totalnya muncul setiap kali satu makanan masuk. check50 langsung hijau semua.

6. Bingung membaca demo di halaman soal
   - Di demo, user mengetik makanan yang tidak ada di menu (large quesadilla), lalu program tidak menampilkan total. Saya kira programnya salah, atau seolah-olah menambahkan makanan yang tidak ada di menu.
   - Duck bilang logika saya sudah benar.
   - Kalau dihitung: burrito 7.50, large quesadilla tidak ada di menu jadi diabaikan, super quesadilla 9.50. Totalnya 7.50 + 9.50 = 17.00. Jadi demo itu memang benar: makanan yang tidak ada di menu tidak ditambahkan dan tidak menampilkan total, langsung tanya lagi.

7. Bingung soal \n
   - Saya sempat menulis `\n` di ujung baris kode, di luar tanda kutip. Hasilnya `SyntaxError: unexpected character after line continuation character`.
   - Ternyata \n cuma berarti "baris baru" kalau ada di dalam string (di dalam tanda kutip). Di luar tanda kutip, tanda \ punya arti lain bagi Python, yaitu "baris ini bersambung ke baris berikutnya". Karena sesudahnya masih ada huruf n, Python bingung.
   - Akhirnya saya pakai print() kosong untuk pindah baris, karena konsepnya sudah saya pahami.
   - Bedanya: print() kosong mencetak satu baris baru. print("\n") mencetak dua, karena \n-nya sendiri satu, ditambah Enter bawaan print satu lagi.

8. Ctrl+D (EOF)
   - Ctrl+D artinya user bilang "input sudah habis". Python memunculkan EOFError, dan error itu yang saya tangkap untuk keluar dari loop.
   - Sesudah Ctrl+D, saya cetak baris baru supaya tanda `$` di terminal tidak menempel di belakang tulisan "Item: ".

### Yang saya pelajari
- Variabel penanda untuk menjumlahkan (celengan) dibuat sebelum loop, isinya 0. Di dalam loop tinggal ditambah.
- Letak print menentukan kapan dia muncul. Di dalam loop: muncul setiap putaran. Di luar loop: muncul sekali setelah loop selesai.
- Huruf besar kecil dirapikan dulu supaya cocok dengan key di dictionary, sama seperti di Nutrition Facts.
- \n hanya berfungsi di dalam string.
- Membaca demo di halaman soal juga perlu dihitung manual, jangan langsung menyimpulkan.
- Error baru: IndentationError, KeyboardInterrupt, EOFError.

### Salah yang saya buat
- While pakai huruf besar.
- Indentasi berlebih.
- Tanda kutip nyasar di dalam kurung siku dictionary.
- Menampilkan harga, bukan total.
- Format total tanpa tanda dolar.
- Print total di luar loop.
- \n ditulis di luar tanda kutip.

### Yang ingin dicoba
- Pelajari lagi method get di dictionary sampai paham, lalu coba di interactive mode.

### Jenis error yang sudah saya kenal (update)
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError, ZeroDivisionError, IndentationError, KeyboardInterrupt, EOFError.

## 3. Grocery List — selesai, check50 hijau semua 5/5 (7 Oktober 2026)

Yang diminta soal:
- User mengetik barang belanjaan satu per satu, satu baris satu barang, sampai menekan Ctrl+D.
- Setelah itu tampilkan daftar belanjaannya: semua huruf besar, urut sesuai abjad, dan di depan setiap barang ada angka berapa kali barang itu diketik.
- Tidak perlu dibuat jamak (3 tomato tetap tomato).
- Huruf besar kecil dari user tidak berpengaruh.

Pelajaran dari Taqueria saya terapkan: sebelum bertanya ke Duck, saya tempel dulu soalnya, supaya Duck tahu "targetnya".

Rencana saya:
- Loop while True, minta input barang, disimpan di variabel.
- Berhenti kalau user menekan Ctrl+D, ditangkap pakai try/except EOFError seperti di Taqueria.
- Barangnya disimpan di dictionary, karena datanya berpasangan: nama barang dan berapa kali diketik.
- Menghitungnya pakai method get di dictionary.
- Terakhir, tampilkan urut sesuai abjad.

### Perjalanan dan yang membuat saya tersendat

1. Kapan membuat huruf besar
   - Awalnya saya pikir gampang, nanti saja waktu print tinggal ditambah upper. Input dibiarkan apa adanya.
   - Duck bertanya: kalau user mengetik Apple, apple, APPLE, berapa key yang tersimpan di dictionary?
   - Ternyata tiga key berbeda, karena beda huruf besar kecil saja sudah dianggap beda. Hitungannya jadi terpecah.
   - Jadi upper harus dilakukan sejak input, sebelum dimasukkan ke dictionary, supaya semua jadi satu key.

2. Lupa cara memasukkan item ke dictionary
   - Caranya: nama_dictionary[key] = value. Kiri itu tempat menyimpan, kanan itu nilai yang disimpan.
   - Awalnya saya kira value-nya selalu 1. Padahal kalau barang yang sama diketik dua kali, harus jadi 2. Jadi value-nya itu nilai lama ditambah 1.

3. get tanpa nilai cadangan
   - Saya baca dokumentasi Python: `get(key, default=None, /)`. Kalau key tidak ada, get mengembalikan default. Kalau default tidak diisi, hasilnya None, dan get tidak pernah memunculkan KeyError.
   - Awalnya saya tulis get tanpa argumen kedua, lalu ditambah 1. Hasilnya `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. None tidak bisa ditambah angka.
   - Solusinya: argumen kedua diisi 0. Kalau barangnya belum ada, 0 + 1 = 1. Kalau sudah ada, nilai lamanya + 1.
   - Tanda +1 harus di luar kurung get, bukan sebagai argumen di dalamnya.

4. Salah tempat upper
   - Saya sempat menaruh upper di ujung hasil get. Hasilnya `AttributeError: 'int' object has no attribute 'upper'`. Hasil get itu angka (hitungan), sedangkan upper cuma punya string.
   - Sempat juga menulis `1.upper()`, hasilnya `SyntaxError: invalid decimal literal`.
   - Jadi upper ditaruh di tempat pertama kali saya mendapat string dari user, yaitu langsung di input.

5. Nama dictionary tertimpa angka
   - Saya sempat menulis nama dictionary = hasil get + 1, tanpa kurung siku. Akibatnya dictionary-nya berubah jadi angka.
   - Muncul `TypeError: 'int' object is not iterable` (angka tidak bisa di-loop) dan `TypeError: 'int' object does not support item assignment` (angka tidak bisa diisi pakai kurung siku).
   - Waktu saya print dictionary-nya, isinya cuma satu angka, bukan pasangan. Ternyata hasil hitungan harus disimpan ke dictionary[barang], bukan ke dictionary-nya langsung.

6. keys, values, items
   - Saya coba di interactive mode:
     - keys() hasilnya `dict_keys(['Ahmad', 'Ake'])`, key-nya saja, bentuknya seperti list.
     - items() hasilnya `dict_items([('Ahmad', 7), ('Ake', 9)])`, seperti list yang isinya tuple. Satu tuple itu satu pasang key dan value.
   - Tulisan dict_keys dan dict_items di depannya cuma label dari Python.
   - keys, values, items tidak menerima argumen apa pun. Kurungnya selalu kosong. Tugasnya cuma mengupas dictionary.

7. Loop key dan value sekaligus
   - Saya ingat ada cara loop yang menyimpan key dan value sekaligus, tapi saya tulis `for key, value in dict:`. Kurang satu: harus pakai items(), karena items yang menghasilkan pasangannya.

8. sorted malah mengurutkan per huruf
   - Hasilnya sempat `['A', 'A', 'A', 'B', 'N', 'N']`. Ternyata yang saya kasih ke sorted itu satu string, misalnya "BANANA". Kalau sorted diberi string, dia memecahnya per huruf lalu mengurutkan hurufnya.
   - Yang saya mau itu mengurutkan kumpulan key-nya, bukan isi satu key.
   - sorted(dictionary.items()) bisa urut sesuai nama barang, karena tuple dibandingkan mulai dari anggota pertamanya, dan anggota pertama itu key-nya.

9. Misteri banana tiga kali tapi angkanya 1
   - Waktu itu saya ketik banana tiga kali, hasilnya malah 1 BANANA.
   - Kemungkinan besar karena yang dicari dan yang disimpan beda huruf. Kalau input belum di-upper, tapi get mencari versi huruf besarnya, maka get selalu tidak ketemu, selalu 0 + 1, dan disimpan di key huruf kecil. Angkanya tidak pernah naik.
   - Cara mengeceknya: print dictionary-nya tepat setelah loop, untuk melihat isi yang sebenarnya.

10. Hal kecil lainnya
    - Salah ketik nama file: grocery,py (koma) bukan grocery.py.
    - `IndentationError: expected an indented block after 'else' statement`, sesudah else tidak ada baris yang menjorok.
    - Kursor di VS Code malah menghapus huruf di sebelah kanannya. Ternyata mode Overtype aktif, matikan dengan tombol Insert di keyboard.
    - Komentar banyak baris di Python: pakai # di setiap baris. Tanda `"""..."""` itu sebenarnya string, bukan komentar sejati.

### Eksperimen setelah check50 hijau: kenapa APPLE jadi 2?
- Saya ketik banana, apple, banana. Hasilnya 2 APPLE dan 2 BANANA, padahal apple cuma sekali.
- Penyebabnya: di loop for, saya menulis dictionary[items], bukan dictionary[i]. Padahal variabel loop-nya i.
- items itu variabel dari loop while sebelumnya. Waktu Ctrl+D, input langsung error sebelum sempat menyimpan, jadi items masih berisi input terakhir yang berhasil, yaitu BANANA.
- Jadi setiap putaran mengambil hitungan BANANA, yaitu 2. Yang berganti cuma i, nama barangnya benar tapi angkanya salah.

| Putaran | i | items | Tercetak |
|---|---|---|---|
| 1 | APPLE | BANANA | 2 APPLE |
| 2 | BANANA | BANANA | 2 BANANA |

- Ini sama persis dengan bug saya di murojaah Vanity Plates: c.isalnum() padahal harusnya s.isalnum(), karena c menyimpan huruf terakhir.
- Pelajarannya: variabel dari loop sebelumnya tidak hilang, isinya nilai terakhir. Kalau hasilnya aneh dan selalu sama, cek apakah memakai variabel yang tepat.
- Bug seperti ini tidak ada error-nya. Programnya jalan, cuma angkanya salah. Ketahuan karena saya mengetes dengan barang yang jumlahnya berbeda.

### Yang saya pelajari
- Seragamkan huruf sejak input, supaya yang disimpan dan yang dicari selalu sama.
- dictionary[key] = dictionary.get(key, 0) + 1 adalah pola menghitung: ambil nilai lama (atau 0 kalau belum ada), tambah 1, simpan lagi.
- upper cuma untuk string, bukan angka.
- items() untuk mengupas pasangan key dan value. sorted pada string mengurutkan hurufnya.
- Variabel loop sebelumnya tetap menyimpan nilai terakhir.
- Beri tahu Duck soalnya dulu sebelum bertanya.

### Salah yang saya buat
- Rencana awal upper di output, bukan di input.
- get tanpa nilai default, kena NoneType.
- upper di hasil get (angka).
- Menimpa dictionary dengan angka.
- for key, value tanpa items().
- sorted diberi satu string.
- dictionary[items] padahal harusnya dictionary[i].

### Setelah lulus dan submit: murojaah kode
- Nama dict untuk variabel
  - Variabel saya awalnya namanya dict, padahal dict itu nama bawaan Python untuk tipe dictionary. Kalau ditimpa, jadi bingung ini nama tipe data atau nama variabel.
  - Akibatnya lebih dari bingung: setelah `dict = {}`, nama dict di file itu tidak lagi merujuk ke tipe dictionary bawaan. Kalau di baris lain butuh dict() yang asli, Python error.
  - Saya buktikan di interactive mode dengan `print = 5` lalu `print("halo")`. Hasilnya `TypeError: 'int' object is not callable`.
  - Callable artinya bisa dipanggil, yaitu yang ditulis sebelum kurung, seperti print atau input. Yang di dalam kurung itu argumen, bukan yang dipanggil. Setelah `print = 5`, isi print jadi angka 5, jadi `print("halo")` sama saja dengan `5("halo")`. Angka tidak bisa dipanggil, akhirnya crash.
  - Seperti papan nama "Kantor Tahfidz" yang dipindah ke pintu gudang. Kantornya masih ada, tapi tidak bisa ditemukan lewat nama itu.
  - Kalau muncul error "X object is not callable", hampir selalu ada nama function yang tertimpa variabel.
  - Aturannya: jangan pakai nama bawaan Python untuk nama variabel, seperti dict, list, str, input, print, sum.
  - Setelah percobaan itu, ketik exit() lalu buka python lagi supaya print normal kembali.
- pass di dalam except EOFError tidak perlu, karena di situ sudah ada print() dan break yang menjorok. pass cuma dipakai kalau bloknya benar-benar kosong.
- Nama variabel saya ganti: item untuk satu barang dari input, items untuk dictionary yang menyimpan banyak barang. Catatan kecil: dictionary bernama items nanti ditulis items.items(), agak membingungkan dibaca. Nama seperti grocery atau belanjaan mungkin lebih jelas.
- Sisa kode lama yang dibungkus tanda kutip tiga sebaiknya dihapus supaya file bersih.

### Yang ingin dicoba
- Murojaah Grocery List dari layar kosong sekitar seminggu lagi, tanpa Duck dan tanpa catatan.

## 4. Outdated — selesai, check50 hijau semua (8 Oktober 2026)

Yang diminta soal:
- User mengetik tanggal dengan format bulan-tanggal-tahun ala Amerika, dalam salah satu dari dua bentuk: angka dengan garis miring (9/8/1636) atau nama bulan dengan koma (September 8, 1636).
- Program menampilkan tanggal itu dalam format tahun-bulan-tanggal (ISO 8601): 1636-09-08. Bulan dan tanggal harus dua digit.
- Kalau inputnya bukan tanggal yang valid di salah satu format itu, program bertanya lagi.
- Daftar nama bulan sudah disediakan dalam bentuk list.

Rencana saya:
- Loop while True, minta input tanggal.
- Cek dulu formatnya: ada garis miring atau tidak.
- Format garis miring: split di garis miring, ubah semuanya jadi integer.
- Format nama bulan: buang komanya, split di spasi, ubah nama bulan jadi nomor pakai list bulan.
- Cek bulan tidak lebih dari 12 dan tanggal tidak lebih dari 31, baru print.
- Kalau gagal, except ValueError lalu tanya lagi.

### Perjalanan dan yang membuat saya tersendat

1. Mendapatkan nomor bulan dari list
   - Saya bingung cara mendapatkan nomor indeks sebuah bulan di dalam list. Ternyata pakai `.index()`.
   - Sempat saya kira sama dengan get di dictionary. Ternyata arahnya berbeda:

| Cara | Diberi | Menghasilkan | Kalau tidak ada |
|---|---|---|---|
| list.index(nilai) | nilai | posisi (nomor indeks) | ValueError |
| list[posisi] | posisi | nilai | IndexError |
| dict.get(key) | key | value | None, tidak error |
| dict[key] | key | value | KeyError |

   - Indeks January itu 0, padahal nomor bulannya 1. Jadi hasil index harus ditambah 1. Tanda +1 harus di luar kurung index, bukan ditambahkan ke nama bulannya, karena "September" + 1 tidak masuk akal.
   - Saya coba di interactive mode: `months.index("januari")` hasilnya `ValueError: 'januari' is not in list`. Jadi nama bulan yang tidak ada di list otomatis ditangkap oleh except ValueError.

2. Salah split
   - Awalnya saya langsung split di input. Ternyata harus dicek dulu karakter pembedanya (garis miring atau bukan), baru di-split sesuai formatnya.
   - Muncul `ValueError: not enough values to unpack (expected 3, got 1)`. Wadahnya 3 (a, b, c), tapi hasil split cuma 1 bagian, karena saya split pakai spasi padahal isinya garis miring semua. Ternyata ValueError tidak cuma dari int("cat"), tapi juga dari jumlah wadah yang tidak cocok dengan jumlah isinya.
   - Sempat juga `SyntaxError: invalid syntax` di baris except.

3. Terlalu fokus ke "bulan harus di depan"
   - Saya bingung cara membandingkan supaya bulannya ada di depan. Duck menegur: di kedua format, bulan memang selalu di depan. Yang perlu divalidasi bukan posisinya, tapi apakah setiap bagian benar-benar bisa diproses jadi tanggal yang valid.
   - Saya baca pelan-pelan lagi penjelasan Duck, akhirnya terbuka juga pemikiran saya. Daripada membandingkan manual, lebih mudah langsung coba proses inputnya (split, int, index). Kalau gagal, ditangkap pakai except.

4. Pengecekan rentang bulan dan tanggal
   - Pengecekan bulan maksimal 12 dan tanggal maksimal 31 saya taruh sebagai if bersarang di dalam masing-masing cabang format. Kalau lolos, baru print.

5. Break boleh lebih dari satu
   - Saya kira break itu cuma boleh satu. Ternyata boleh banyak. break bekerja di titik mana pun dia dijalankan. Jadi tiap cabang yang berhasil punya break sendiri.
   - Satu try juga boleh punya lebih dari satu except, dan satu while True boleh punya lebih dari satu blok try-except.

6. check50 merah
   - Hasil saya pakai garis miring (1636/09/08), padahal yang diminta pakai tanda minus (1636-09-08). Pelajarannya: bandingkan expected dan actual huruf per huruf.
   - `September 8 1636` tanpa koma harus ditolak. Awalnya lolos karena koma langsung saya buang tanpa dicek dulu. Setelah saya tambahkan pengecekan ada koma atau tidak, hijau semua.
   - `" 9/8/1636 "` dengan spasi di depan dan belakang ternyata lolos, karena int() otomatis membuang spasi, sama seperti percobaan saya `int(" 5 ")` dulu.

7. Eksperimen sendiri: bulan 0
   - Saya iseng ketik `0/20/2002`, ternyata lolos jadi `2002/00/20`, karena 0 memang kurang dari 12.
   - check50 tidak mengujinya, tapi bulan ke-0 bukan tanggal yang valid. Bisa ditolak pakai perbandingan berantai seperti di Fuel Gauge, dengan batas bawah 1, bukan 0.
   - Di interactive mode saya sempat ketik `0/2/2002` tanpa tanda kutip, hasilnya 0.0. Ternyata tanpa tanda kutip itu dianggap pembagian, bukan tanggal. Input dari user selalu string.
   - Saya juga ketik `months.index(a)` di interactive mode dan kena NameError, karena interactive mode itu sesi baru yang tidak tahu variabel di file saya.

### Yang saya pelajari
- list.index untuk mencari posisi, dict.get untuk mencari value. Arahnya beda.
- break boleh lebih dari satu.
- ValueError juga muncul kalau jumlah wadah tidak cocok saat unpack.
- Bandingkan expected dan actual di check50 dengan teliti.
- Lulus check50 tidak berarti kebal semua kasus. Biasakan bertanya "kalau input ini, apa yang terjadi?"

### Salah yang saya buat
- Split langsung di input.
- +1 di dalam kurung index.
- Format output pakai garis miring, bukan tanda minus.
- Koma dibuang tanpa dicek dulu.

### Setelah lulus: murojaah kode
- Pengecekan rentang dan print saya tulis berulang di dua cabang. Apakah bisa ditulis sekali di bawah if/else?
  - Bisa, tapi ada jebakan. Kalau input tanpa koma, cabangnya tidak mengisi bulan, tanggal, tahun. Lalu pengecekan di bawah memakai variabel yang belum pernah dibuat (NameError, crash) atau sisa dari input sebelumnya.
  - Variabel tidak otomatis terganti waktu user mengetik input baru. Yang berubah cuma variabel yang barisnya dengan tanda = benar-benar dijalankan. Sama seperti bug items vs i di Grocery dan c vs s di Vanity Plates.
  - Menangkap NameError pakai except itu salah arah. ValueError itu kesalahan user, wajar minta ulang. NameError itu kesalahan kode kita sendiri, yang harus diperbaiki kodenya. Seperti alarm asap berbunyi lalu baterainya dicabut, padahal apinya masih ada.
  - Pengecekan rentang itu bergantung pada data yang disiapkan cabangnya, jadi wajar kalau ada di dalam cabang. Kode saya yang sekarang aman karena print dan break ada di dalam tiap cabang.
  - Ada cara lain yang menulis pengecekan sekali saja dengan try/except/else, tapi keamanannya tersirat. Buat saya kode saya sendiri lebih mudah dibaca, walaupun agak berulang. Explicit is better than implicit.
  - Trade-off: pertukaran. Dapat satu keuntungan, harus merelakan keuntungan lain. Tidak ada pilihan yang sempurna.
- Nama a, b, c lebih jelas kalau diganti month, day, year.
