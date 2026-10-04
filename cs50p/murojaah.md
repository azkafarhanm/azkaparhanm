## Murojaah 1: Math Interpreter, ditulis ulang dari layar kosong (4 Oktober 2026)

# Murojaah CS50P

Catatan menulis ulang soal lama dari layar kosong.
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Boleh buka dokumentasi.
Jadwal: setiap Minggu jam 05.20.

| No | Soal | Tanggal | Waktu | Hasil |
|---|---|---|---|---|
| 1 | Math Interpreter (Pset 1) | 4 okt | 60 menit | check50 6/6 |
- Murojaah: lihat [murojaah.md](murojaah.md)

Waktu mengerjakan: 60 menit
Hasil: check50 hijau semua (6/6)
Aturan: tidak membuka kode lama, tidak bertanya ke AI, Copilot dimatikan. Boleh buka dokumentasi.

Yang saya cari di dokumentasi:
- Cara menampilkan satu angka di belakang koma. Nama resminya di dokumentasi Python adalah "format specification mini-language", bagian precision.

Error yang saya temui:
- `SyntaxError: invalid syntax` karena saya menulis tiga variabel berjajar tanpa operator. Python tidak tahu maksudnya apa.
- `TypeError: unsupported format string passed to tuple.__format__` karena di dalam curly braces saya menulis beberapa nilai dipisah koma. Koma itu membuat Python mengikatnya jadi satu paket namanya tuple. Aturan desimal tidak bisa dipakai untuk satu paket berisi beberapa angka.
- Saya juga sempat pakai `d`. Ternyata `d` itu untuk bilangan bulat (int), sedangkan untuk float pakai `f`.
- `TypeError: unsupported operand type(s) for +: 'float' and 'str'` karena saya menjumlahkan angka dengan y, padahal y isinya operator (tulisan), bukan angka kedua. Harusnya angka pertama dengan angka ketiga.
- Aturan desimal sempat saya tulis di luar curly braces lagi, jadi ikut tercetak sebagai tulisan. Ini kesalahan yang sama seperti waktu pertama mengerjakan.
- check50 sempat merah di "2 - 3" dengan actual kosong. Kalau tidak ada case yang cocok, match diam saja, tidak error dan tidak mencetak apa-apa.

Yang saya pelajari:
- Yang membuat tuple itu komanya, bukan kurungnya. `print(x, y, z)` tidak error, karena komanya memisahkan argument untuk print.
- Di dalam curly braces f-string, Python hanya mau satu nilai. Aturan setelah titik dua berlaku untuk seluruh isi curly braces, bukan cuma ke nilai yang paling dekat.
- Bedanya dengan not: not justru menempel ke syarat yang paling dekat, kecuali diberi kurung.
- Perhitungan boleh langsung ditulis di dalam curly braces f-string. Waktu pertama mengerjakan, saya membuat variabel result. Kemungkinan dulu saya kena error yang sama (salah variabel), lalu mengira format string-nya yang tidak bisa.
- Kode lama dan kode baru beda bentuk tapi logikanya sama. Yang baru lebih ringkas karena split langsung ditempel ke hasil input.

Perbandingan dengan pertama kali:
- Pertama kali (24 September) masih dibantu arahan. Sekarang dari layar kosong, error saya baca dan perbaiki sendiri.
- Murojaah berikutnya: sekitar awal November. Bandingkan waktunya.
