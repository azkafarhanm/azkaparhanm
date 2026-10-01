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

## 2. Just setting up my twttr — selesai 
## 3. Vanity Plates — selesai
## 4. Nutrition Facts — belum
## 5. Coke Machine — belum
