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

## 3. Vanity Plates — belum
## 4. Nutrition Facts — belum
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
