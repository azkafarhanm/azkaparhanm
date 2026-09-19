# Problem Set 0

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

## 1. Indoor Voice — selesai, check50 4/4 (19 September 2026)

Yang diminta soal:
- Minta promptan dari user.
- Case-nya user menulis pakai capital semua, lalu dibuat jadi lower dan di-print.
- Kalau ada punctuation seperti titik dan lain sebagainya, itu tetap seperti itu dan tidak berubah.

Rencana yang saya tulis sebelum coding:
1. Minta input dari user.
2. Hasil inputan disimpan ke variabel, hurufnya dibuat lower semua dengan method lower.
3. Lalu di-print.

Error yang saya temui:
- `NameError: name 'lower' is not defined` — sebabnya lower ini bukan function yang bisa berdiri sendiri.
- `AttributeError: 'builtin_function_or_method' object has no attribute 'lower'` — sebabnya method lower-nya menempel ke function input, bukan ke string hasil inputan.
- Waktu lower ditulis tanpa parentheses, yang muncul `<built-in method lower of str object...>`. Artinya methodnya cuma disebut, belum dijalankan.
- `check50` tanpa slug juga error. Perintahnya harus lengkap dengan alamat soalnya.

Pelajaran:
- Kalau mau menempelkan method, yang ditempeli itu hasil string dari inputannya, bukan function input-nya.
- Jadi caranya: parentheses input dulu, baru titik, baru nama methodnya.

## 2. Playback Speed — selesai (19 September 2026)

Yang diminta soal:
- Minta inputan dari user.
- Kalau inputan berisi white space, itu diganti dengan titik tiga.
- Semua white space dari inputan user diganti dengan titik tiga.

Rencana yang saya tulis sebelum coding:
1. Minta input dari user.
2. Semua white space dari inputan diganti dengan titik tiga.
3. Lalu di-print.

Salah tebak di awal:
- Awalnya saya kira pakai `split` dengan argument titik tiga. Ternyata salah, karena `split` itu memisahkan dan hasilnya jadi list, sedangkan soal minta tulisannya tetap utuh, hanya spasinya yang ditukar.
- Method yang benar `replace`, dan butuh dua argument: yang dicari, lalu penggantinya.

Kendala yang saya rasakan:
- Terkadang saya bingung method apa yang cocok untuk case ini.

Cara mengatasinya:
- Tulis dulu langkahnya dalam bahasa Indonesia, lalu ambil kata kerjanya.
- Terjemahkan kata kerja itu ke bahasa Inggris, misalnya "mengganti" jadi `replace`, "huruf kecil" jadi `lower`, "memisahkan" jadi `split`.
- Cari kata itu dengan Ctrl + F di halaman string methods. Halamannya juga sudah dikelompokkan, misalnya Searching and Replacing dan Splitting and Joining.

## 3. Making Faces — belum
## 4. Einstein — belum
## 5. Tip Calculator — belum
