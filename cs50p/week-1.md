# CS50P Week 1: Conditionals

## Hari 1 – 21 September 2026
Coding: 90 menit | Inggris: 60 menit

### Boolean expression
- Boolean expression itu hasilnya true atau false.
- Bisa dipakai lewat if dan else.

### Flowchart
- Flowchart itu diagram program logic. Logic-nya seperti apa, dibuat diagramnya.
- Diagram if dan else ada perbedaan. Kalau pakai elif, diagramnya agak lebih lebar.
- Ternyata bukan cuma beda di diagram, tapi beda di cara kerjanya juga. Diagram itu gambar dari cara kerja programnya.

### else
- else untuk menutup kalau kemungkinan satu dan dua salah atau false, berarti kemungkinan ketiga yang muncul.
- Jadi tidak perlu ada pertanyaan lagi.

### if terpisah vs elif
- Kalau if semuanya (if, if, if), programnya menjalankan dan mengecek satu per satu, semuanya.
- Kalau elif atau else, ketika satu sudah benar, sisanya tidak dijalankan.
- if terpisah menampilkan sebanyak syarat yang benar. Kalau benarnya cuma satu, ya satu yang ditampilkan.
- Kalau ada kemungkinan dua-duanya benar, if terpisah tampil dua baris, sedangkan elif tetap satu baris.
- Percobaan: angka 20 dengan `if user > 0` dan `if user > 1`, hasilnya muncul "positif" dan "negatif" sekaligus. Tidak error, tapi hasilnya salah, karena syaratnya tumpang tindih.

### elif sama dengan else + if
- else yang di dalamnya ada if, secara fungsi sama saja dengan elif.
- Tapi elif lebih readable, karena tidak makin menjorok ke kanan.

### Tanya jawab menit 15:38
- Pertanyaannya: kenapa masih pakai pertanyaan ketiga `x == y`?
- Kalau dua kemungkinan pertama salah (x tidak lebih kecil dan tidak lebih besar dari y), secara logika otomatis yang benar pilihan terakhir, yaitu x sama dengan y.
- Jadi pertanyaan ketiga tidak perlu dimasukkan, cukup pakai `else`.
