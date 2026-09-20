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

## 3. Making Faces — selesai (19 September 2026)

Yang diminta soal:
- Buat function `convert` yang menerima str, lalu `:)` diganti emoji senyum dan `:(` diganti emoji cemberut. Teks lain dikembalikan apa adanya.
- Buat function `main` yang minta prompt dari user, memanggil `convert` pada input itu, lalu print hasilnya.
- `main` dipanggil di bagian paling bawah file.

Rencana saya:
- Resep `convert`: menerima tulisan lewat parameter, ganti dua emotikon dengan `replace` dua kali, lalu `return`.
- Resep `main`: minta input, panggil `convert`, print hasilnya.
- Di luar semua resep: panggil `main()`.

Error yang saya temui:
- `TypeError: convert() missing 1 required positional argument: 'emoticon'` — karena `convert` dipanggil tanpa argument, padahal resepnya minta satu isian.
- `NameError: name 'emoticon' is not defined` — karena hasil `convert` belum ditampung ke variabel, tapi sudah saya print.
- Sebelum itu programnya juga sempat jalan tanpa error tapi hasilnya tidak berubah, karena `convert` dipanggil tanpa ditampung, lalu yang saya print malah input aslinya.

Pelajaran:
- Ketika `convert` dipanggil di dalam `main`, dia menjalankan isinya dan mengembalikan nilai baru. Tapi kalau tidak ada tampungan, nilai itu hilang.
- Jadi setiap function yang `return`, hasilnya harus ditangkap, entah oleh variabel atau langsung dipakai di tempat lain.
- Dua `replace` bisa disambung, karena hasil `replace` pertama juga berupa string, jadi bisa ditempeli method lagi.

Kendala yang saya rasakan:
- Soal tidak menjelaskan spesifik bahwa kita harus membuat variabel dulu. Jadi memang kita yang harus berpikir sendiri. Di situ saya masih lemah, karena terbiasa kalau sudah spesifik baru tahu harus bagaimana.
- Membaca error di terminal juga masih kaku, belum terlalu paham.

Catatan untuk diri sendiri:
- Kalau soal berbunyi "calls X on Y and prints the result", artinya tiga langkah: kirim Y ke X, tangkap hasilnya, lalu tampilkan.

## 4. Einstein — selesai (20 September 2026)

Yang diminta soal:
- Minta massa dari user sebagai integer, lalu tampilkan energinya pakai rumus E = mc².
- c itu kecepatan cahaya, 300000000.

Rencana saya:
1. Minta input user dengan prompt `m: `.
2. Convert jadi integer.
3. Hitung sesuai rumus: c dipangkatkan 2, lalu dikali m.
4. Print dengan awalan `E: `.

Salah yang saya buat:
- Awalnya saya tulis `m ** 300000000`, terbalik. Yang dipangkatkan 2 itu kecepatan cahayanya, bukan massanya.
- Nama file salah ketik `einsten.py`, padahal harus `einstein.py`. Diganti pakai `mv`.
- Sempat bingung di terminal karena mengganti nama folder sambil berada di dalam folder itu. Keluar dulu pakai `cd ..`.

Pelajaran:
- `"3" * 2` hasilnya `"33"`, bukan 6, karena string dikali angka artinya diulang. Tidak error tapi hasilnya salah.
- `int("3") * 2` baru hasilnya 6.
- Yang ditampilkan `print` itu selalu sebagai string, tapi isi value variabelnya tidak berubah. Kalau integer ya tetap integer.
- Makanya kalau mau menggabung integer dengan string, cara mudahnya pakai f-string. Kalau pakai plus operator, integernya harus di-convert dulu dengan `str()`.
- Pangkat di Python pakai `**`.

## 5. Tip Calculator — selesai (20 September 2026)

Yang diminta soal:
- Sebagian kode sudah diberikan CS50. Yang dikerjakan cuma dua function bertanda TODO.
- `dollars_to_float`: dari `$50.00` jadi `50.0`.
- `percent_to_float`: dari `15%` jadi `0.15`.

Rencana saya:
- Kedua function menerima lewat parameter dari main.
- `dollars_to_float`: hilangkan `$` pakai replace, lalu jadikan float, lalu return.
- `percent_to_float`: hilangkan `%` pakai replace, jadikan float, dibagi 100, lalu return.

Salah yang saya buat:
- Awalnya saya kira desimal di belakang koma harus dihilangkan pakai round. Ternyata tidak perlu, yang dibuang cuma tanda `$`.
- `TypeError: unsupported operand type(s) for /: 'str' and 'int'` — karena pembagian 100 saya taruh di dalam kurung float, jadi yang dibagi masih string hasil replace.

Pelajaran:
- Python mengerjakan kurung yang paling dalam dulu, baru yang di luar.
- Hasil `replace` masih berupa string, belum bisa dihitung. Jadi pembagian 100 harus di luar kurung float, setelah jadi angka.
- `float` untuk angka berdesimal, `int` untuk bilangan bulat.
- Persen artinya per seratus, jadi 15% sama dengan 15 dibagi 100.

---

**Problem Set 0 selesai 5/5.**
