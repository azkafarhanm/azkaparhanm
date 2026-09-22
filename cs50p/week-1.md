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

### Tanya jawab menit 15:38
- Pertanyaannya: kenapa masih pakai pertanyaan ketiga `x == y`?
- Kalau dua kemungkinan pertama salah (x tidak lebih kecil dan tidak lebih besar dari y), secara logika otomatis yang benar pilihan terakhir, yaitu x sama dengan y.
- Jadi pertanyaan ketiga tidak perlu dimasukkan, cukup pakai `else`.

### if terpisah vs elif
- Kalau if semuanya (if, if, if), programnya menjalankan dan mengecek satu per satu, semuanya.
- Kalau elif atau else, ketika satu sudah benar, sisanya tidak dijalankan.
- if terpisah menampilkan sebanyak syarat yang benar. Kalau benarnya cuma satu, ya satu yang ditampilkan.
- Kalau ada kemungkinan dua-duanya benar, if terpisah tampil dua baris, sedangkan elif tetap satu baris.
- Percobaan: angka 20 dengan `if user > 0` dan `if user > 1`, hasilnya muncul "positif" dan "negatif" sekaligus. Tidak error, tapi hasilnya salah, karena syaratnya tumpang tindih.

### elif sama dengan else + if
- else yang di dalamnya ada if, secara fungsi sama saja dengan elif.
- Tapi elif lebih readable, karena tidak makin menjorok ke kanan.

## Hari 2 – 22 September 2026
Coding: 90 menit | Inggris: 30 menit
Lecture Week 1 selesai ditonton.

### Pythonic
- Python bisa ditulis lebih clear dan lebih singkat.
- if else bisa di-condense, dipersingkat dari empat baris jadi satu baris.
- Yang paling simpel: langsung return modulo dibandingkan dengan nol.
- Tidak butuh variable dan tidak butuh if, karena hasilnya sudah boolean. Sintaksnya sudah menjelaskan bahwa itu akan mengembalikan value boolean antara true dan false.
- Function `is_even` mengembalikan nilai true atau false ke main dengan return.
- Di main cukup ditulis `if is_even(x):`, tidak perlu `== True`, karena is_even sudah menyerahkan true atau false.

### match
- match keyword fungsinya mirip if else. Prosesnya sama, bedanya tipis.
- Kalau di if else, kemungkinan terakhir pakai else. Kalau di match, pakai `case _` (underscore).
- Di match bisa pakai single bar `|` artinya "atau".
- Tapi di if, untuk "atau" pakai `or`, bukan `|`.

### Bedanya match dan if
- match cuma membandingkan satu nilai dengan kemungkinan yang persis sama. Seperti beberapa `==` yang disusun rapi.
- if bisa membandingkan yang lebih besar atau lebih kecil, atau menggabungkan dua syarat.
- Kalau menggabungkan dua syarat atau pakai `>` dan `<`, harus pakai if.
- Kalau cuma mencocokkan satu nilai dengan yang persis sama, lebih rapi pakai match.
- Semua yang bisa dilakukan match bisa dilakukan if, tapi tidak sebaliknya.

### Kosakata
- "very similar in spirit" artinya sangat mirip dalam maksud dan cara kerjanya, bukan "semangat".

### Yang masih bingung
- Kadang susah memahami kata-kata David yang berupa expression atau ungkapan.
