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

## 4. Math Interpreter — belum
## 5. Meal Time — belum
