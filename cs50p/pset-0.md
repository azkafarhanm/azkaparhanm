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

## 2. Playback Speed — belum
## 3. Making Faces — belum
## 4. Einstein — belum
## 5. Tip Calculator — belum
