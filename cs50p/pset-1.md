# Problem Set 1

Catatan proses pengerjaan. Kode jawaban tidak ditulis di sini,
sesuai aturan academic honesty CS50.

## 1. Deep Thought — selesai, check50 hijau semua (23 September 2026)

Yang diminta soal:
- Bikin logika question if else. Kalau user menjawab 42, forty-two, atau forty two, output Yes. Selain itu No.
- Di soal tertulis "case-insensitively", jadi huruf besar kecil tidak boleh berpengaruh.

Rencana saya:
1. Minta input dari user untuk menjawab pertanyaannya.
2. Nilai dari user disimpan di variabel, lalu dibandingkan di dalam match.
3. Pakai match karena rapi untuk satu nilai dengan beberapa kemungkinan yang persis sama, dan bisa pakai single bar.
4. Kalau semua tidak cocok, ditangkap oleh `case _`.

Yang saya pelajari:
- strip dan lower dipakai sebelum pencocokan, waktu menyimpan input. Karena match mencocokkan persis, kalau inputnya ada spasi atau huruf besar, tidak akan cocok.
- Kalau input sudah di-lower, tulisan di case juga harus huruf kecil semua.
- Match tidak perlu int. Soalnya juga bilang tidak perlu convert ke int kalau membandingkan dengan "42" sebagai str.
- Awalnya saya pikir strip dan lower cuma jaga-jaga untuk real case di lapangan, takutnya user typo. Ternyata check50 memang mengujinya, termasuk input 42 dengan spasi di kiri kanan.
- Pelajaran: soal tidak selalu menyebutkan semua yang diuji. Hasil check50 bisa dipakai untuk tahu apa saja yang sebenarnya diperiksa.

## 2. Home Federal Savings Bank — selesai (23 September 2026)

Yang diminta soal:
- Kalau greeting diawali "hello", output $0.
- Kalau diawali huruf h tapi bukan hello, output $20.
- Selain itu $100.

Rencana saya:
1. Minta input greeting dari user, disandingkan dengan strip dan lower.
2. Cek dengan if: pertama startswith "hello", baru elif startswith "h", lalu else.
3. startswith dipakai di bagian if, bukan waktu menyimpan input.

Yang saya pelajari:
- startswith sudah mengembalikan boolean true atau false, jadi tidak perlu `== True` lagi.
- Urutan harus hello dulu. Kalau h dulu, input hello akan tertangkap di situ dan langsung dapat $20, sisanya tidak dieksekusi.
- Error `AttributeError: 'str' object has no attribute 'startwith'` karena saya kurang huruf s. Python bahkan menawarkan koreksinya: "Did you mean: 'startswith'?".
- Saya juga sempat menulis `startswith("Hello")` dengan H besar, padahal inputnya sudah di-lower. Tidak error, tapi hasilnya salah. Ketahuannya karena saya belum menguji input "hello" sendiri.
- Pelajaran: program yang jalan belum tentu benar. Setiap cabang harus diuji satu per satu.

## 3. File Extensions — selesai (23 September 2026)

Yang diminta soal:
- Minta nama file, lalu tampilkan media type-nya sesuai akhiran: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip.
- Kalau akhirannya lain atau tidak ada, outputnya application/octet-stream.

Yang saya pelajari:
- Media type itu label jenis isi file, supaya penerima tahu isinya gambar, tulisan, atau dokumen. Bentuknya dua bagian dipisah garis miring, misalnya image/gif.
- Methodnya `endswith`. Awalnya saya cari "endwith", tidak ketemu karena kurang huruf s.
- Error baru: `TypeError: called match pattern must be a class`. Sebabnya saya mencampur match dengan endswith.
- Kesimpulannya, match tidak bisa menerima hasil pengecekan yang isinya true atau false. Match memang maunya membandingkan nilai.
- Kalau mau tetap pakai match, akhirannya harus dipotong dulu dengan split, tapi hasilnya berupa list dan saya belum belajar list. Jadi untuk sekarang pakai if dan elif.
- .jpg dan .jpeg jawabannya sama, jadi digabung dengan `or`.
- Sempat salah tulis `txt/plain`, harusnya `text/plain`.

## Catatan umum
- Tumpang tindih terjadi kalau satu input bisa memenuhi lebih dari satu syarat. Kalau tumpang tindih, yang lebih khusus harus dicek duluan.
- Di bank tumpang tindih, karena hello dan h sama-sama berawalan huruf h.
- Di extensions tidak tumpang tindih, karena yang dicek akhiran, dan satu file tidak mungkin berakhiran .jpg sekaligus .jpeg.
- Kosakata soal yang penting: case-insensitively, startswith, endswith, otherwise.

## 4. Math Interpreter — selesai (24 September 2026)

Yang diminta soal:
- User mengetik expression seperti `1 + 1`, lalu program menampilkan hasilnya.
- Operatornya empat: tambah, kurang, kali, bagi.

Rencana saya:
1. Minta input dari user, simpan di variabel.
2. Pisahkan dengan split spasi ke tiga variabel sekaligus: x, y, z.
3. x dan z diubah jadi float, y tetap string karena isinya operator.
4. Pakai match untuk memilih operatornya, lalu print hasilnya dengan format string.

Yang saya pelajari:
- Tidak bisa langsung float waktu input, karena yang diketik user itu satu kalimat utuh berisi angka dan operator.
- Tidak perlu membuat variabel baru untuk menyimpan hasil konversi. Variabel lama boleh ditimpa, misalnya `x = float(x)`. Saya tadinya terlalu saklek, mengira harus selalu bikin variabel baru.
- Kalau isi lamanya masih dibutuhkan, baru buat variabel baru.
- Aturan tampilan desimal ditulis di DALAM curly braces, setelah nilainya. Waktu saya tulis di luar, hasilnya malah `16.0:.1f`, karena dianggap tulisan biasa.
- Urutan operasi matematika berlaku sama seperti di sekolah: perkalian dan pembagian dikerjakan duluan sebelum penjumlahan.
- Error `ValueError: too many values to unpack (expected 3)` kalau jumlah potongan hasil split tidak sama dengan jumlah variabel di kiri tanda sama dengan.

Kesimpulan penting tentang match:
- Setelah `case` harus berupa NILAI, bukan pertanyaan yang hasilnya true atau false.
- Makanya kemarin `case extensions.endswith(".jpg")` error, karena itu pertanyaan, bukan nilai.
- Kalau `if`, boleh diisi apa saja yang menghasilkan true atau false, termasuk method seperti startswith dan endswith.
- Di match, tindakan tiap case boleh berbeda-beda. Yang harus cocok persis itu nilainya, bukan tindakannya.
- Single bar dipakai kalau beberapa kemungkinan menghasilkan tindakan yang sama, seperti di Deep Thought. Di sini tidak dipakai karena tiap operator tindakannya berbeda.

## 5. Meal Time — selesai (24 September 2026)

Yang diminta soal:
- User mengetik waktu format 24 jam, program menampilkan breakfast time, lunch time, atau dinner time.
- Sarapan 7:00–8:00, makan siang 12:00–13:00, makan malam 18:00–19:00, dan rentangnya inclusive.
- Kalau di luar rentang, tidak menampilkan apa-apa, jadi tidak perlu else.
- Harus ada function `convert` yang mengubah "7:30" menjadi 7.5.

Yang saya pelajari:
- split dan perhitungan ada di dalam convert, bukan di main. main cuma minta input, kirim ke convert, lalu bandingkan hasilnya.
- Yang dibandingkan adalah hasil convert, bukan jamnya saja. Kalau cuma jamnya, input 8:30 akan dianggap masih breakfast.
- Menit dibagi 60 karena satu jam berisi 60 menit, lalu ditambah jamnya.
- Untuk memeriksa rentang harus pakai `and`, bukan `or`. Kalau pakai or, input 20:00 akan dianggap breakfast, karena 20 >= 7 sudah benar.
- Kata "formatted" di soal maksudnya bentuk penulisannya, bukan format string.
- Kata "assume" artinya kita boleh menganggap input user selalu benar bentuknya.

Tentang dua baris `if __name__ == "__main__":`
- check50 mau menguji function convert saja, tanpa menjalankan seluruh program.
- Kalau `main()` ditulis telanjang di bawah, begitu file dibuka programnya langsung jalan dan malah minta input. Makanya check50 gagal menemukan 7.5.
- Dua baris itu sebenarnya cuma if biasa. Kalau file ini jadi panduan utama, main dijalankan. Kalau cuma dipinjam file lain, baris main tetap dibaca tapi tidak dijalankan.
- Detail cara kerjanya dibahas di Week 5. Untuk sekarang saya sudah paham kenapa dibutuhkan.

---

**Problem Set 1 selesai 5/5.**

## Catatan untuk diri sendiri
- Saya masih dibantu arahan waktu buntu, terutama soal letak split dan soal `__name__`.
- Tapi semua kode saya yang tulis, dan beberapa error saya temukan sendiri.
- Aturan mulai Pset 2: buntu dulu 30 menit sebelum bertanya.
- Tes kemandirian: minggu depan tulis ulang satu soal lama dari layar kosong, tanpa membuka catatan dan chat. Catat waktunya, lalu ulangi sebulan lagi.
