# CS50P Week 5: Unit Tests

## Hari 1 – 16 Oktober 2026

Hari ini capek sekali, baru perjalanan lumayan jauh. Cuma sempat nonton sekitar 8 menit awal lecture, sisanya dipakai bertanya. Paginya juga memperbaiki bitcoin.py dulu (catatannya di pset-4.md).

### Kenapa harus menulis tes?
- Kata David: lebih baik membiasakan diri menulis tes **sejak awal**, selagi programnya masih kecil, daripada nanti sesudah programnya besar dan rumit.
- Ini nyambung dengan pengalaman saya di Pset 4: tiga kali check50 hijau, padahal ada kasus yang tidak dites (figlet tiga argumen, Guessing Game level 0, Little Professor raise). Dengan tes sendiri, kasus-kasus seperti itu bisa ketahuan sebelum submit.

### Mulai dari calculator.py (Week 0)
```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
```
- `square` itu pangkat dua (kuadrat): 2 × 2 = 4, 3 × 3 = 9.
- Sekarang mau dites, tapi bukan dengan menjalankan program lalu mengetik angka manual satu-satu. Dibuat program lain yang khusus untuk menguji.

### Program penguji: test_calculator.py
```python
from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
```
- Ini program yang sama sekali berbeda, yang **satu-satunya tujuannya** (sole purpose) menguji calculator.py.
- `from calculator import square` → meminjam function square dari file lain. Persis pelajaran import dan `__name__` di Week 4.
- Angka 2 dan 3 sudah **ditanam** langsung di kode (baked in / hardcoded).

### Tes itu memeriksa, bukan menghasilkan jawaban
- Saya kira test_square itu "memberikan hasil yang sesuai". Ternyata yang menghitung tetap square. test_square cuma **mengecek**: jawaban square sama tidak dengan yang seharusnya?
- `if square(2) != 4: print(...)`:
  - Kalau square benar → syarat `!= 4` salah → **tidak tercetak apa-apa**.
  - Kalau square rusak → baru muncul pesan `2 squared was not 4`.
- Jadi di tes ini, **diam artinya lulus**.
- Tesnya juga bukan berulang sendiri seperti loop. Jalan sekali setiap kali file tes dijalankan. Istimewanya: bisa diulang kapan saja (misalnya setiap habis mengubah calculator.py), dan pemeriksaannya selalu sama persis.
- Ibarat penguji tahfidz: penguji sudah pegang mushaf, tahu ayat yang benar (4 dan 9). Dia minta santri (square) membaca ayat tertentu (2 dan 3). Kalau benar, penguji diam dan lanjut. Kalau salah, baru ditegur. Penguji tidak ikut membaca, cuma mencocokkan.

### Baked in / hardcoded: bukan berarti tidak bisa diubah
- Saya kira "baked in" artinya kodenya tidak bisa diganggu gugat lagi. **Ternyata bukan.** Kodenya tetap bisa diubah kapan saja, buka file, ganti angkanya.
- Maksudnya: nilainya tidak bisa diubah **dari luar saat program jalan**. Satu-satunya cara mengubah ya mengedit kodenya sendiri.

| Cara | Nilainya dari mana | Untuk menggantinya |
|---|---|---|
| Baked in / hardcoded | ditulis langsung di kode | buka file, edit kodenya |
| `input()` | diketik user saat program jalan | ketik nilai lain, kode tidak disentuh |
| `sys.argv` | diketik di terminal saat menjalankan | ketik `python file.py 5`, kode tidak disentuh |

- Ibarat jadwal pelajaran: hardcoded = jadwal yang dicetak lalu ditempel di dinding, bisa diubah tapi harus cetak ulang. input() = setiap pagi ustadz bertanya ke santri "hari ini murojaah surat apa?".
- Untuk tes, hardcoded justru disengaja. Tes harus memeriksa hal yang sama persis setiap kali dijalankan, supaya kalau suatu hari hasilnya berubah, langsung ketahuan ada yang rusak.
- Contoh hardcoded dari pekerjaan saya sendiri: API key di bitcoin.py.

### Boilerplate dan dua penjaga `__name__`
- **Boilerplate** = kode kerangka baku yang selalu ditulis sama di banyak program, bukan inti programnya. Ibarat kop dan format surat resmi pesantren: selalu ada kop, nomor, salam pembuka, tanda tangan. Isinya yang penting justru di tengah.
- Kata David: banyak dari test_calculator.py ini cuma boilerplate, yaitu `def main()`, pemanggilan test_square di dalamnya, dan `if __name__ == "__main__":`. Intinya cuma test_square.
- Saya bertanya: kenapa file tes juga pakai main dan penangkal `__name__` seperti calculator.py? Saya kira untuk meminjam function tidak harus meniru isi file yang dipinjam. **Dugaan saya benar.**

| | Penjaga di calculator.py | main + penjaga di test_calculator.py |
|---|---|---|
| Wajib? | Ya, penting | Tidak wajib, cuma kebiasaan |
| Gunanya | Supaya waktu square dipinjam, main() milik calculator (yang tanya "What's x?") tidak ikut jalan | Biar rapi dan konsisten |

- Penjaga yang benar-benar dibutuhkan ada di **file yang dipinjam**, bukan di file yang meminjam. Sama dengan percobaan saya di Pset 4: percobaan.py bisa import professor.py tanpa ditanya Level, karena penjaganya ada di professor.py.
- File tesnya bisa saja cukup `test_square()` di paling bawah. Kemungkinan nanti di lecture boilerplate ini dihapus, sesudah dikenalkan alat tes yang bisa menjalankan function `test_...` otomatis.

### Kosakata
| Kata | Arti |
|---|---|
| sooner | lebih cepat, lebih awal (dari soon). Bukan "sonner", itu bahasa Prancis artinya berbunyi/berdering |
| get into the habit | membiasakan diri |
| left off | berhenti di suatu titik untuk dilanjutkan nanti. *Where did we leave off?* = kemarin sampai mana? Ibarat pembatas mushaf |
| purpose | tujuan (kata benda), dibaca *PER-pes* |
| sole purpose | satu-satunya tujuan. sole ≠ soul (jiwa) |
| propose | mengusulkan (kata kerja), dibaca *pro-POUZ*. *Let me propose that we...* = izinkan saya mengusulkan agar kita... |
| on purpose | sengaja |
| bake (into) | arti harfiah memanggang. Kiasan: menanamkan secara permanen ke dalam, seperti telur yang sudah dipanggang dalam kue |
| hardcoded | nilainya ditulis mati di dalam kode |
| boilerplate | kode kerangka baku, selalu sama di banyak program |

### Catatan pakai DeepL
- Bahasa asal sempat masih French, jadi "sonner" diterjemahkan "bunyi lonceng". Pastikan bahasa kiri English atau Detect language.

### Yang mau dicoba
- Buat calculator.py dan test_calculator.py sendiri, jalankan test_calculator.py. Harusnya tidak keluar apa-apa (diam = lulus).
- Sengaja rusak square (misalnya `n + n`), jalankan tesnya lagi. Pesan mana yang muncul? (Petunjuk: 2 + 2 juga 4.)
- Lanjut lecture dari menit 8.
