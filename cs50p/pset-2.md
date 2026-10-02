# Problem Set 2

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

## 1. camelCase — selesai, check50 hijau semua (30 September 2026)

Yang diminta soal:
- Di bahasa pemrograman lain, convention nama variabel pakai camel case: kata pertama lowercase, kata berikutnya diawali uppercase.
- Di Python, convention-nya snake case: kata-katanya disambung dengan underscore, semua lowercase.
- Program minta input nama variabel camel case dari user, lalu output-nya versi snake case.

Rencana yang saya tulis sebelum coding (dari kerja tangan dulu):
- Untuk setiap huruf:
  - kalau hurufnya besar, tulis garis bawah, lalu hurufnya versi kecil
  - kalau tidak, tulis hurufnya apa adanya
- Huruf kecil tidak diapa-apakan, cukup disalin.
- Saya tulis rencananya sebagai komentar # dulu di file, lalu terjemahkan satu baris komentar jadi satu baris kode.

Yang saya pelajari:
- String itu iterable, bisa disusuri huruf per huruf dengan for, sama seperti list disusuri anggota per anggota. Input tidak jadi list, tetap string.
- `for c in camel_case` berputar sebanyak jumlah hurufnya. Loop tidak mengulang dari awal, tetap maju dari kiri ke kanan.
- Method untuk cek huruf besar ada di keluarga `is...`, yaitu `isupper`. Hasilnya true atau false.
- Kalau hint di soal ada contoh kode, jalankan dulu contoh itu supaya paham maksudnya.

Salah yang saya buat:
- `if c.isupper:` tanpa tanda kurung. Hasilnya semua huruf diberi garis bawah, misalnya name jadi _n_a_m_e. Method tanpa kurung cuma disebut, tidak dijalankan, dan oleh if selalu dianggap benar.
- Label "snake_case: " saya taruh di dalam cabang if, jadinya muncul di tengah, tepat saat ketemu huruf besar. Label cukup dicetak sekali, sebelum loop, pakai end="".
- Waktu end="" di cabang if saya hilangkan, hasilnya azka_p lalu arhan pindah ke baris bawah. Enter-nya terjadi sekali, tepat setelah _p, karena print itu yang tidak punya end="".
- Waktu print() di akhir saya hilangkan, tanda `camel/ $` di terminal ikut menyambung di ujung hasil. Ternyata tanda dolar itu juga tulisan yang dicetak di mana pun kursor berada.

Tentang autocomplete:
- Awalnya di VS Code laptop saya dibantu autocomplete. Tulisan abu-abu yang melengkapi baris itu dari AI (Copilot), bukan bawaan VS Code.
- IntelliSense (kotak daftar nama method) itu bawaan VS Code. Tulisan abu-abu yang melanjutkan kode itu AI.
- Untuk latihan CS50, AI autocomplete dimatikan, dan soal dikerjakan ulang di cs50.dev dari layar kosong.

Kendala yang saya rasakan:
- Kalau stuck, saya malah bengong, bingung mau coba apa.
- Cara mengatasinya: tulis pseudocode sebagai komentar dulu, lalu kerjakan satu baris saja. Tanyakan kata kerjanya: minta = input, untuk setiap = for, kalau = if, tulis = print.

## 2. Just setting up my twttr — selesai, check50 hijau semua (1 Oktober 2026)

Yang diminta soal:
- Program minta input teks dari user.
- Output-nya teks yang sama, tapi semua vowel (a, i, u, e, o) dihilangkan, baik huruf besar maupun kecil.
- Huruf lain tetap seperti aslinya. Contoh: Twitter jadi Twttr (bukan twttr), What's your name? jadi Wht's yr nm?, CS50 tetap CS50.

Rencana yang saya tulis sebelum coding:
- Minta input dari user, simpan di variabel.
- Untuk setiap huruf (c) di input:
  - kalau c (setelah dikecilkan) tidak termasuk "aeiou", cetak c yang asli
  - kalau vowel, tidak dicetak apa-apa
- Soal ini mirip camelCase: sama-sama menyusuri string huruf per huruf dan mencetak menyambung.

Yang saya pelajari:
- `in` artinya "termasuk dalam", kebalikannya `not in` artinya "tidak termasuk". Hasilnya true atau false (boolean).
- `in` dan `not in` itu bukan function. Namanya membership operator (operator keanggotaan). Function itu ada kurungnya dan dipanggil, contohnya print(). Operator ditulis di antara dua hal, seperti + atau ==.
- Kata `in` punya dua tugas. Di `for c in teks` artinya "ambil satu per satu". Di `if c in "aeiou"` artinya "apakah termasuk?".
- Arah pengecekannya: yang di kiri satu huruf, yang di kanan kumpulan vowel. Pertanyaannya "huruf ini termasuk daftar vowel atau tidak?", bukan "ada vowel di kalimat ini atau tidak?".
- Yang dikecilkan cukup c di dalam pengecekan, bukan seluruh kalimat. lower() tidak mengubah variabel aslinya, jadi yang dicetak tetap huruf asli.
- Urutan "aiueo" atau "aeiou" tidak berpengaruh, karena yang dicek hanya ada atau tidak.
- print() bawaannya menambahkan Enter di akhir. Parameter `end=""` membuat cetakan berikutnya menyambung. print() kosong di luar loop dipakai sekali supaya prompt terminal turun ke baris baru.
- Ada dua pasangan method yang mirip tapi beda tugas: upper() mengubah jadi huruf besar, isupper() bertanya "apakah semua hurufnya besar?" dan hasilnya true atau false. Nama yang diawali `is...` biasanya pertanyaan.
- isupper() hanya menghitung huruf. Angka dan spasi diabaikan. Saya cek di interactive mode: "A1" hasilnya True, "1" hasilnya False karena tidak ada huruf sama sekali, "A b" hasilnya False karena ada huruf kecil b (bukan karena spasinya), "A B" hasilnya True.

Salah yang saya buat:
- Awalnya arah in-nya kebalik, kepikiran "kalau vowel ada di kalimat".
- Sempat kepikiran mengecilkan seluruh input di awal. Kalau begitu, Twitter jadi twttr, huruf T-nya ikut berubah.
- Uji pertama Azka hasilnya Azk, karena A besar masih lolos. Setelah c dikecilkan dulu sebelum dicek, hasilnya benar: zk.
- Label "Output: " sempat tercetak berulang di tengah hasil. Label cukup dicetak sekali sebelum loop, pakai end="".

Catatan:
- Bertanya untuk memahami soal dan menyusun rencana tidak melanggar aturan 30 menit saya. Aturan 30 menit berlaku setelah rencana selesai, saat menulis kode dan membaca error.

## 3. Vanity Plates — selesai, check50 hijau semua (2 Oktober 2026)

Ini soal paling berat di Problem Set 2. Saya mengerjakannya dari jam 7 pagi sampai siang, sempat berhenti karena otak panas, lalu lanjut lagi.

Yang diminta soal:
- Program minta input plat nomor, lalu mencetak Valid kalau memenuhi semua aturan, atau Invalid kalau tidak.
- Kerangka kodenya sudah diberi soal: main() memanggil is_valid(s), dan is_valid mengembalikan True atau False.
- Ada lima aturan yang harus dipenuhi semuanya:
  1. Dua karakter pertama harus huruf.
  2. Panjangnya minimal 2 karakter dan maksimal 6 karakter.
  3. Angka hanya boleh di akhir, tidak boleh di tengah. AAA222 boleh, AAA22A tidak boleh.
  4. Angka pertama tidak boleh 0.
  5. Tidak boleh ada titik, spasi, atau tanda baca.

Kerja tangan sebelum coding:
- CS50 sah. CS05 tidak sah (angka pertama 0). CS50P tidak sah (angka di tengah). PI3.14 tidak sah (ada titik).
- AB sah. A1 tidak sah (karakter kedua angka). ABCDEFG tidak sah (7 karakter).
- Awalnya saya bingung, aturan 1 bilang harus huruf, aturan 2 bilang "letters or numbers". Ternyata keduanya membicarakan bagian yang berbeda. Aturan 1 soal awal plat, aturan 2 soal panjang total. Seperti syarat halaqah: "hafalan 2 sampai 6 juz" dan "dua juz pertama harus Juz 30 dan Juz 29", dua syarat yang harus dipenuhi sekaligus.
- Kalimat "Assume that any letters in the user's input will be uppercase" artinya soal menjamin inputnya sudah huruf besar. Jadi tidak perlu upper().

Yang saya pelajari:
- `and` artinya semua syarat harus True baru hasilnya True. `or` cukup salah satu. is_valid butuh `and` karena plat sah hanya kalau semua aturan lolos.
- Slicing `s[0:2]` mengambil dua karakter pertama, lalu bisa langsung disambung method: `s[0:2].isalpha()`.
- `isalpha()` bertanya "apakah huruf semua?". `isalnum()` bertanya "apakah huruf atau angka semua?", cocok untuk aturan 5. Saya menemukannya sendiri di dokumentasi Python (link dari Hints soal).
- isalnum() memeriksa semua karakter tanpa kecuali, termasuk spasi dan tanda baca. Beda dengan isupper() yang mengabaikan angka dan spasi. Jadi dua method `is...` bisa punya cara mengecek yang berbeda, harus dibaca dokumentasinya dan diuji.
- "at least one character" di dokumentasi artinya string-nya tidak boleh kosong, bukan "minimal ada satu angka".
- `len()` untuk menghitung jumlah karakter. Bukan length.
- `not` membalik True jadi False dan sebaliknya. Tanpa kurung, not hanya menempel ke syarat terdekat. `not 8 >= 2 and 8 <= 6` hasilnya False, sedangkan `not (8 >= 2 and 8 <= 6)` hasilnya True. Untuk aturan 2 harus pakai kurung supaya seluruh syaratnya yang dibalik. Seperti "bukan (kelas 7 dan hafal Juz 30)" beda dengan "(bukan kelas 7) dan hafal Juz 30".
- Variabel penanda (flag): variabel yang dibuat sebelum loop dengan nilai awal False, untuk mengingat "sudah pernah ketemu angka atau belum". Program tidak perlu menoleh ke karakter sebelumnya, cukup bertanya ke penandanya. Sama seperti amount_due di Coke yang membawa sisa tagihan dari putaran ke putaran.
- Penanda hanya berubah sekali, dari False ke True, saat ketemu angka pertama. Seperti bendera yang dinaikkan saat barisan santri putri dimulai, lalu tidak diturunkan lagi.
- Di setiap putaran cukup lihat dua hal, karakter sekarang dan isi penanda. Ada empat kemungkinan:

| Karakter | Penanda | Artinya | Yang dilakukan |
|---|---|---|---|
| angka | False | angka pertama | cek apakah 0, kalau 0 gagal, kalau bukan penanda jadi True |
| angka | True | angka lanjutan | aman |
| huruf | False | masih bagian huruf | aman |
| huruf | True | huruf setelah angka | gagal |

- Karena isi penanda sudah True atau False, cukup tulis `if penanda:` tanpa `== True`.
- `c` itu teks, jadi `"0" != 0` hasilnya True. Teks "0" dan angka 0 dianggap berbeda, seperti tulisan "lima" di kertas dan lima butir kurma. Harus disamakan dulu jenisnya, misalnya pakai int().
- Pola penting: ketemu pelanggaran langsung `return False`. Kalau semua aturan lolos, baru `return True` sekali di paling akhir. Seperti setoran: satu ayat salah langsung dihentikan, lulus baru dinyatakan setelah semua ayat benar.
- `return` menghentikan function seketika, loop-nya ikut berhenti. Kode di bawah return tidak dijalankan, makanya VS Code membuatnya abu-abu.
- Function yang selesai tanpa return diam-diam mengembalikan None, dan if menganggapnya seperti False.
- Lebih mudah menulis aturan berjajar (if ... return False, if ... return False) daripada bersarang (if di dalam if di dalam if).

Salah yang saya buat:
- Menulis `def is_valid(length(s)):`. Di dalam kurung def hanya boleh nama parameter, bukan perhitungan. SyntaxError.
- Pakai `length()`, padahal namanya `len()`. NameError.
- Pakai `s.allnum()` dan `s.alnum()`. AttributeError, dan Python menyarankan "Did you mean: 'isalnum'?".
- Lupa indentasi baris pertama di bawah def.
- Strukturnya bersarang. Kalau aturan 1 atau 2 gagal, kodenya cuma diam lalu jatuh ke aturan 5, jadi H dan OUTATIME keluar Valid. Kegagalan harus langsung diumumkan dengan return False.
- Setelah diubah, semua plat malah Invalid, termasuk CS50, karena belum ada return True di akhir.
- Aturan 2 tanpa kurung setelah not, jadi OUTATIME sempat lolos.
- `c == 0` tidak pernah True karena c teks.
- Penanda saya ubah jadi False saat ketemu huruf, padahal seharusnya tidak pernah diturunkan.
- Menulis `if not penanda == False:`. Dua penyangkalan saling membatalkan, jadi artinya malah "penanda sudah True".
- WWW09 dan WWW02 keluar Valid sebelum semua itu diperbaiki.

Cara membaca error yang saya pelajari:
- Traceback dibaca dari bawah. Baris terakhir itu error-nya, baris di atasnya jalurnya.
- Tanda ^ menunjuk titik di mana Python mulai bingung.
- Baris terakhir kadang ada saran "Did you mean ...?".

Catatan kejujuran:
- Untuk soal ini saya banyak dibantu petunjuk dan pertanyaan pancingan dari Claude (AI). Kodenya saya tulis sendiri, tapi setelah membaca aturan academic honesty CS50P, AI selain milik CS50 tidak boleh dipakai untuk mengerjakan problem set. Mulai soal berikutnya saya pakai CS50 Duck.
- Saya jadwalkan menulis ulang soal ini dari layar kosong tanpa bantuan, untuk membuktikan ilmunya sudah benar-benar milik saya.

## 4. Nutrition Facts — selesai, check50 hijau semua (3 Oktober 2026)

Soal pertama yang saya kerjakan dengan CS50 Duck, bukan Claude.

Yang diminta soal:
- Program minta input nama buah, lalu mencetak kalori untuk satu porsi buah itu, sesuai poster buah dari FDA.
- Input harus diterima case-insensitively, jadi Apple, APPLE, apple sama saja.
- Anggap user mengetik nama buah persis seperti di poster (strawberries, bukan strawberry).
- Kalau input bukan buah, diabaikan, tidak mencetak apa-apa.
- Hati-hati: yang dicetak kalori buahnya, bukan kalori dari lemak.

Rencana saya:
- Data buah diambil dari link poster di soal (ada versi teksnya juga), lalu disimpan di dictionary: nama buah jadi key, kalori jadi value.
- Key di dictionary saya tulis huruf kecil semua, dan input user juga saya kecilkan dengan lower(), supaya selalu cocok. Ini keputusan saya sendiri.
- Cek dulu apakah input ada di dictionary pakai `if ... in ...`. Kalau ada, cetak kalorinya. Kalau tidak ada, tidak perlu else, program selesai tanpa mencetak apa-apa.

Yang saya pelajari:
- Dictionary cocok untuk data yang berpasangan. Seperti daftar santri: nama santri jadi key, data hafalannya jadi value. Key harus unik, seperti nama di daftar absen.
- Mengambil value: nama dictionary, kurung siku, key. Seperti mencari nama Ahmad di daftar lalu melihat hafalannya.
- Tidak perlu for loop karena pertanyaannya cuma sekali. Loop baru dipakai kalau ada yang diulang, atau mau menampilkan semua isi dictionary.
- Kalau if salah, Python tetap membaca dan memeriksa syaratnya, hanya isinya dilewati.
- `if ... in dictionary` sebelum mengambil value membuat program tidak pernah meminta key yang tidak ada, jadi aman dari KeyError.

Salah yang saya buat:
- Awalnya mau pakai for loop, ternyata tidak perlu.
- Ada key yang kurang satu tanda kutip. Error-nya SyntaxError: unterminated string literal, artinya teks belum ditutup.
- Sempat lupa cara menampilkan value, lalu ingat lagi dari lecture.

Tentang belajar dengan CS50 Duck:
- Pertanyaan ke Duck dibatasi dengan "hati" (bar biru) yang terisi lagi setelah beberapa waktu. Jadi pertanyaan harus disiapkan baik-baik, tidak dipakai untuk basa-basi.
- Duck juga memberi petunjuk, bukan jawaban jadi, misalnya mengingatkan pilihan lower() atau upper() untuk menyamakan key dan input. Keputusannya tetap saya.
- Sebelum memakai hati, coba dulu yang gratis: baca error, uji di interactive mode, telusuri dengan tangan, tonton ulang lecture, dan jelaskan kode dengan suara keras (rubber duck debugging).
- Template pertanyaan ke Duck: soal apa, yang ingin dilakukan, yang sudah dicoba, hasilnya, yang diharapkan, satu pertanyaan spesifik.

Latihan tambahan setelah submit (di luar soal):
- `for nama in hafalan` memegang key satu per satu. Value-nya diambil dengan `hafalan[nama]`. Jadi `print(nama, hafalan[nama])` mencetak nama dan jumlah juz.
- Kalau hanya satu nama, tidak perlu loop. Tulis key langsung, atau simpan dulu di variabel `nama = "Ahmad"`, lalu pakai print yang sama.
- `nama["ahmad"]` menghasilkan TypeError: string indices must be integers. Saya salah membuka `nama` (isinya teks "Ahmad"), padahal yang dibuka harusnya `hafalan`. Teks dan list dibuka pakai index (nomor posisi), dictionary dibuka pakai key.
- `hafalan["ahmad"]` menghasilkan KeyError: 'ahmad', karena key-nya "Ahmad" dengan A besar. Python membedakan huruf besar dan kecil. Inilah kenapa lower() di Nutrition Facts penting.
- Key datang dari mana: ditulis langsung, dari variabel, dari input user (seperti Nutrition Facts), atau dari for loop (untuk semua key).

## 5. Coke Machine — selesai, check50 hijau semua (1 Oktober 2026)

Yang diminta soal:
- Mesin minuman harganya 50 sen. User memasukkan koin satu per satu, dan mesin hanya menerima 25, 10, dan 5.
- Setiap kali, tampilkan "Amount Due" (sisa tagihan). Koin selain itu diabaikan.
- Kalau sudah lunas, tampilkan "Change Owed" (kembalian).

Rencana yang saya tulis sebelum coding:
- Tagihan awal 50.
- Selama tagihan masih lebih dari 0:
  - tampilkan sisa tagihan
  - minta koin, ubah jadi angka
  - kalau koinnya 25, 10, atau 5, kurangi tagihan
- Setelah lunas, tampilkan kembalian (dibuat positif).

Yang saya pelajari:
- while vs for: for dipakai kalau jumlah putarannya sudah jelas (setiap huruf, setiap isi list, range). while dipakai kalau saya tidak tahu berapa kali harus berputar, yang saya tahu hanya kapan berhentinya (sampai lunas).
- Syaratnya bisa ditulis langsung di while, jadi loop berhenti sendiri tanpa break. while True itu pola lain: selalu berputar dan baru berhenti kalau ada break.
- Kalau if salah, loop tidak berhenti. if cuma melewati isinya, tagihan tidak berubah, lalu balik lagi ke while. Yang menghentikan loop hanya syarat while (atau break).
- Bentuk `-=` itu sama seperti `+=`, hanya dikurangi.
- Posisi print itu penting. "Change Owed" ditaruh di luar loop supaya muncul sekali saja setelah selesai.
- abs() itu function (bukan method) untuk membuat angka jadi positif. Saya cek di interactive mode: abs(-5) = 5, abs(0) = 0, jadi aman untuk kasus bayar pas.
- "Amount Due" sudah dicetak di awal tiap putaran, jadi tidak perlu else. Kalau di else juga dicetak, tulisannya muncul dua kali.

Salah yang saya buat:
- Awalnya kepikiran pakai for, padahal jumlah koinnya tidak bisa ditebak.
- Kurung di baris int(input(...)) sempat kurang satu.
- "Change Owed" sempat di dalam loop, jadi tercetak berkali-kali.
- Sempat mengira kalau if salah, loop langsung berhenti.
- Sempat mau menambahkan else untuk mencetak ulang "Amount Due".
- Masih bingung cara membuat -5 jadi 5, sampai ingat matematika SD dan menemukan abs().

Boleh buka dokumentasi?
- Boleh. Nonton ulang video while atau baca dokumentasi itu bukan nyontek, tapi belajar. Yang tidak boleh: lihat jawaban orang.

## Penutup Problem Set 2 — selesai semua (3 Oktober 2026)

Jenis error yang sudah saya temui:

| Error | Artinya |
|---|---|
| SyntaxError | tata bahasa kode salah, program belum sempat jalan |
| NameError | ada nama yang tidak dikenal Python |
| AttributeError | object tidak punya method dengan nama itu |
| TypeError | jenis data tidak cocok dengan cara memakainya |
| KeyError | key tidak ada di dictionary |

Cara belajar mulai sekarang:
- Mengerjakan problem set: sendiri dulu, macet lebih dari 30 menit tanya CS50 Duck, lalu check50 dan submit50.
- Setelah submit: cerita ke Claude dengan bahasa sendiri untuk murojaah, membahas cara lain, dan menyusun catatan ini.
- Murojaah terjadwal setiap Minggu jam 05.20: menulis ulang satu soal lama dari layar kosong dan menjawab pertanyaan konsep.
- Kalau lupa saat murojaah: coba dulu dari ingatan, baru buka kode lama sendiri. Mengenali tidak sama dengan mengingat.

