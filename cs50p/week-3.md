# CS50P Week 3: Exceptions

## Hari 1 – 4 Oktober 2026

Menonton lecture sampai sekitar menit 20 (bagian try, except, else).

### Pemanasan sebelum menonton
- Pertanyaan: di soal Coke saya menulis `int(input(...))`. Kalau user mengetik `cat`, apa yang terjadi?
- Jawabannya ternyata error baru: ValueError.

### ValueError
- `int("cat")` menghasilkan `ValueError: invalid literal for int() with base 10: 'cat'`.
- Artinya: tulisan 'cat' tidak bisa diubah jadi angka biasa.
- "Literal" artinya apa yang benar-benar diketik. "Base 10" artinya sistem bilangan biasa (0 sampai 9).
- Beda dengan TypeError: TypeError itu jenis datanya salah, ValueError itu jenisnya benar tapi isinya tidak masuk akal.

### f-string dan interpolate
- "Interpolate" artinya menyisipkan nilai variabel ke dalam teks.
- `print("x is {x}")` tanpa huruf f tidak menyisipkan apa-apa. Harus `print(f"x is {x}")`.

### try dan except
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```
- try: coba jalankan baris ini.
- except ValueError: kalau muncul ValueError, jalankan ini, jangan berhenti dengan error.
- Begitu ada error di satu baris dalam try, sisa baris di dalam try langsung dilewati, lalu loncat ke except.
- Setelah except selesai, Python lanjut normal ke baris di bawahnya.

### Saran David soal except (menit 12.11 sampai 13.07)
- Bisa menulis `except:` saja tanpa nama error, supaya semua error ditangkap. Tapi itu bad practice dan lazy, karena bisa menyembunyikan bug lain. Kalau tidak tahu apa yang salah, bagaimana bisa menanganinya dengan benar?
- Lebih baik sebutkan jenis error-nya secara jelas, seperti `except ValueError:`.
- Masalahnya, dokumentasi Python tidak selalu memberi tahu error apa saja yang mungkin muncul. Jadi sarannya agak bertentangan (contradictory): sebutkan error spesifik, padahal tidak selalu jelas error apa yang harus disebutkan.
- Solusinya: makin sering latihan, makin hafal. Kadang dokumentasi juga menyebutkannya.
- Seperti musyrif: yang baik mencari tahu masalah spesifik santri. Yang malas bilang "pokoknya ulang dari awal" untuk semua masalah.

### try sebaiknya pendek
- try sebaiknya hanya membungkus baris yang memang bisa error.
- Kalau terlalu banyak baris dibungkus, tidak jelas baris mana yang ditangani, dan bisa ikut menyembunyikan error lain.

### NameError karena urutan pengerjaan
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
- Kalau user mengetik cat, hasilnya "x is not an integer" lalu `NameError: name 'x' is not defined`.
- Awalnya saya kira karena scope: x dibuat di dalam try, jadi tidak bisa dipakai di luarnya. Mahasiswa di video juga menebak begitu, David bilang good instincts, tapi bukan itu penyebabnya. try tidak seperti function. Variabel yang dibuat di dalam try tetap bisa dipakai di luarnya.
- Buktinya: kalau inputnya 50, hasilnya `x is 50`, padahal print ada di luar try.
- Penyebab sebenarnya: urutan pengerjaan (order of operations). Baris `x = int(input(...))` dikerjakan dari kanan ke kiri:
  1. input() minta ketikan user → "cat"
  2. int() mengubah jadi angka → gagal, ValueError
  3. x = ... menyimpan ke x → tidak pernah terjadi
- Jadi x tidak pernah dibuat. Waktu print di luar try memanggil x, muncul NameError.
- Kalau print ada di dalam try, tidak error, karena print ikut dilewati.
- Seperti buku mutaba'ah: nilai baru ditulis kalau setoran sah. Setoran gagal di tengah, kolom nilai tidak pernah diisi. Bukan karena bukunya di ruangan lain (scope), tapi karena memang tidak pernah ditulis.
- ValueError biasanya karena nilai dari user. NameError biasanya karena kodenya sendiri, memakai nama variabel dengan cara yang tidak seharusnya.

### else di try
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
- try selalu dicoba lebih dulu.
- Ada error → except jalan, else dilewati.
- Tidak ada error → except dilewati, else jalan.
- except dan else itu pasangan, hanya salah satu yang jalan.
- else tidak menangkap error. else = tempat untuk baris yang hanya boleh jalan kalau try berhasil.
- Kalau try berhasil, x pasti sudah ada, jadi NameError tidak mungkin terjadi.
- Versi ini mengambil kelebihan dua versi sebelumnya: try tetap pendek, dan tidak ada NameError.
- Seperti setoran: nasihat murojaah (except) kalau salah, tulis nilai (else) kalau lancar. Tidak mungkin dua-duanya.

### else di if dan else di try
- Benang merahnya sama: else jalan kalau yang di atasnya tidak terjadi.
- Di if/elif, else jalan kalau tidak ada syarat yang True. Seperti kolom "lain-lain" (catchall).
- Di try, else jalan kalau except tidak terjadi, artinya try berhasil tanpa error.
- Bedanya: isi if belum tentu dijalankan, tapi isi try selalu dicoba dulu.

### Kosakata
- somehow: entah bagaimana caranya.
- somewhere: di suatu tempat.
- somewhat: agak (bukan "sesuatu").
- interpolate: menyisipkan nilai variabel ke dalam teks.
- mouthful: kalimat yang panjang dan ribet diucapkan.
- roughly: kira-kira, garis besarnya.
- proactively: sebelum diminta, bertindak lebih dulu. Lawannya reactively.
- invariably: selalu, tanpa kecuali.
- contradictory: saling bertentangan.
- raise (error): memunculkan error, bukan "menaikkan". DeepL sempat salah menerjemahkan jadi "dinaikkan".
- shouldn't: should not, tidak seharusnya. "that you shouldn't [do]", kata kerjanya dihilangkan.
- boil down to: intinya adalah. Arti asalnya merebus sampai tinggal sarinya.
- kind of: semacam, bisa dibilang.
- catchall: penampung semua sisa, seperti kolom "lain-lain".

### Jenis error yang sudah saya kenal
- SyntaxError, NameError, AttributeError, TypeError, ValueError, IndexError, KeyError.

### Yang ingin dicoba
- Jalankan tiga versi kode (print di dalam try, di luar try, di else) dengan input 50 dan cat, bandingkan hasilnya.
- Lanjutkan video dari menit 20: membuat program terus bertanya sampai user mengetik angka.

## Hari 2 – 5 Oktober 2026

Melanjutkan lecture dari menit 20 sampai selesai.

### NameError dipikirkan secara deduktif
- Deductive: menarik kesimpulan dari aturan yang sudah pasti, langkah demi langkah. Bukan menebak.
- Kalau user mengetik `cat`, yang gagal bukan `input()`. `input()` berhasil menerima "cat" sebagai teks. Yang gagal adalah `int("cat")`.
- Rantainya: `int("cat")` gagal → sisi kanan tidak menghasilkan nilai → `=` tidak pernah dijalankan → x tidak pernah dibuat → NameError.
- x itu bukan "kosong", tapi "tidak pernah ada". Bedanya:

| Keadaan | Contoh | `print(x)` |
|---|---|---|
| Kosong | `x = ""` | mencetak baris kosong, tidak error |
| Tidak pernah dibuat | `=` tidak sempat jalan | NameError |

- Seperti lemari: kosong artinya lemarinya ada tapi tidak ada isinya. Tidak pernah dibuat artinya lemarinya memang tidak ada.

### while True dan break
```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
```
- `while True` artinya ulangi terus, tanpa syarat berhenti.
- Awalnya saya kira True di sini artinya "jawaban user benar". Ternyata bukan. True itu nilai tetap yang tidak pernah berubah, jadi jawabannya selalu "ya, ulangi". while True sama sekali tidak tahu apa yang diketik user.
- `break` artinya keluar dari loop. Bisa dipakai di loop mana saja (while maupun for), tidak harus bersama try.
- Yang menentukan break jalan atau tidak adalah try: kalau try berhasil, masuk else, lalu break. Kalau input salah, masuk except, break tidak terbaca, loop bertanya lagi.
- David sempat memindahkan break ke dalam try, tepat di bawah baris x. Itu juga benar. Kalau baris x error, sisa baris di try ditinggalkan dan Python langsung lompat ke except, jadi break tidak tersentuh.
- Bedanya dengan if yang False: if False melewati isinya lalu lanjut ke baris sesudah if. Error di try langsung lompat ke except.
- Seperti halaqah: `while i < 3` itu "ulangi ayat ini selama belum 3 kali". `while True` itu "ulangi terus", berhentinya hanya kalau ustadz bilang cukup (break).

### while False
- Saya coba sendiri di interactive mode: `while False:` lalu `print("halo")`. Hasilnya tidak tercetak apa-apa.
- while selalu mengecek kondisi dulu sebelum isi loop jalan, di setiap putaran, termasuk putaran pertama.
- Kalau dari awal sudah False, isi loop tidak pernah dimasuki sama sekali (nol kali), termasuk break di dalamnya.

| Loop | Berapa kali isinya jalan |
|---|---|
| `while True:` | terus, sampai ketemu break |
| `while i < 3:` | selama kondisinya True |
| `while False:` | nol kali |

### Membuat function get_int
- David memindahkan loop tadi ke function sendiri, `get_int`, lalu dipanggil dari main.
- `return x` ditaruh di bawah loop, sejajar dengan while. Urutannya: try berhasil → else → break keluar dari loop (hanya loop, bukan function) → sampai ke `return x`.
- Kalau `return x` ditaruh di dalam try, else dan break jadi tidak perlu. Karena return langsung menghentikan seluruh function, dan loop di dalamnya ikut berhenti.
- Kalau inputnya salah, return di dalam try tidak tersentuh, Python ke except, lalu loop bertanya lagi sampai benar.
- Dua-duanya benar. Ini soal pertimbangan (trade-off): try pendek sesuai nasihat David kemarin, atau lebih ringkas dengan return di dalam try. Nasihat try pendek itu pedoman, bukan aturan mutlak. Akhirnya David memilih return di dalam try.

### Variabel yang tidak perlu
```python
x = int(input("What's x? "))
return x
```
- x di sini cuma dititipi sebentar lalu langsung dikembalikan. Bisa langsung: `return int(input("What's x? "))`.
- `input(...)` itu argumen untuk `int()`. Python mengerjakan dari dalam ke luar: input dulu, lalu int, lalu return.
- Ringkas itu bagus, tapi mudah dibaca lebih penting. Satu atau dua lapis function seperti ini masih wajar.

### pass
```python
except ValueError:
    pass
```
- pass artinya tidak melakukan apa-apa. Error tetap ditangkap, program tidak crash, tapi tidak ada pesan.
- Hasilnya user hanya ditanya `What's x?` berulang-ulang, tidak "berisik" lagi.
- Kenapa tidak dikosongkan saja? Karena Python wajib ada minimal satu baris berindentasi sesudah `except ...:`. pass adalah cara bilang "saya sengaja tidak melakukan apa-apa di sini".
- Seperti musyawarah: nama saya dipanggil (error terjadi), saya tidak keluar ruangan (tidak crash), saya bilang "cukup, tidak ada tambahan" (pass), lalu lanjut ke orang berikutnya (loop bertanya lagi).
- Trade-off: print memberi tahu user kesalahannya tapi bisa terasa cerewet. pass lebih tenang tapi user tidak diberi petunjuk. Di problem set, ikuti apa yang diminta soal.

### Indentasi di Python wajib
- Di Python, indentasi menentukan baris mana yang termasuk isi def, while, try, except.
- Di C, C++, Java, isi blok ditandai kurung kurawal `{ }`. Spasinya cuma supaya rapi, tidak wajib (tidak di-enforce).
- Seperti harakat dalam Al-Qur'an: posisinya menentukan makna. Sedangkan di bahasa lain seperti kerapian khat, bagus kalau rapi tapi tidak mengubah arti.
- Ini juga alasan Python butuh pass. Java cukup `{ }` kosong, Python tidak punya kurung kurawal.

### Caller, callee, dan abstraksi
- Caller: yang memanggil function (di sini main). Callee: yang dipanggil (di sini get_int).
- Semua urusan repot (loop, try, user mengetik cat, dog, bird) terjadi di dalam get_int. main tidak tahu apa-apa soal itu, cuma menerima angka yang sudah pasti valid.
- Ini namanya abstraction: detail yang rumit disembunyikan di dalam function, jadi main tetap pendek dan mudah dibaca.
- Seperti ustadz menyuruh santri menanyakan nama tamu di gerbang. Mungkin santri harus bertanya tiga kali karena tamunya tidak jelas, tapi ustadz cuma menerima nama yang benar.

### Pythonic
- Pythonic: gaya menulis kode yang khas dan dianggap paling wajar di Python.
- Ada dua cara menangani input yang mungkin bukan angka:
  1. Cek dulu pakai if, misalnya `s.isnumeric()`, baru diubah jadi int.
  2. Langsung coba pakai try, kalau gagal baru ditangani di except.
- Menurut David, cara kedua itu yang Pythonic. Tapi cara pertama juga "totally reasonable".
- Saya buktikan sendiri di interactive mode kenapa cara kedua sering lebih kuat:

| Input | `.isnumeric()` | `int()` |
|---|---|---|
| `"-5"` | False | -5 |
| `" 5 "` | False | 5 |
| `"cat"` | False | ValueError |

- isnumeric mengecek setiap karakter, jadi tanda minus dan spasi membuatnya False. Padahal int() bisa menerima keduanya. Hanya "cat" yang memang seharusnya ditolak.
- Kesimpulan: cara "cek dulu" bisa salah menolak input yang sebenarnya valid. Cara try membiarkan int() sendiri yang memutuskan.
- Seperti mengecek hafalan santri: paling pasti langsung disimak setorannya, bukan menebak dari seberapa sering dia membawa mushaf.

### Parameter prompt
- Sebelumnya get_int selalu bertanya "What's x?". Kebetulan cocok dengan variabel x di main, tapi tidak ada yang memaksa cocok. David menyebutnya honor system, seperti kantin kejujuran.
- Kalau main ingin `y = get_int()`, pertanyaannya tetap "What's x?". Tidak nyambung.
- Solusinya: main yang menentukan pertanyaannya, lalu dikirim lewat parameter.

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```

- Awalnya saya kira parameter itu cuma untuk memberi nilai (angka). Ternyata teks juga termasuk nilai. Parameter itu variabel yang isinya diberikan oleh pemanggil, isinya bebas.
- Sebenarnya saya sudah melakukan ini sejak Week 0: `input("Name: ")` itu mengirim teks sebagai argumen ke function input.
- Parameter dan return itu dua jalan yang berlawanan arah:

| | Arah | Gunanya |
|---|---|---|
| Parameter | main → function | bahan masuk |
| return | function → main | hasil keluar |

- Function tidak wajib punya parameter. get_int versi awal tanpa parameter tetap bisa, karena bahannya diambil sendiri lewat input. Seperti santri yang disuruh menanyakan nama tamu: ustadz tidak perlu memberi apa-apa, santri pulang membawa nama (return).

### Penutup David
- "As you write more code in Python, you'll see that errors are inevitable." Error itu pasti terjadi. Bukan tanda gagal, tapi bagian normal dari menulis kode. Yang penting bisa membaca dan menanganinya.

### Kosakata
- deductively: secara deduktif, menyimpulkan dari aturan yang pasti.
- suffice it to say: singkatnya, intinya. Suffice = cukup, satu keluarga dengan sufficient.
- pretty darn correct: sudah benar banget. Darn itu versi sopan dari damn, untuk menekankan. Pretty di sini artinya "cukup", bukan "cantik".
- convenient: praktis, memudahkan. Beda dengan comfortable (nyaman).
- artificially: secara buatan, dibuat-buat. DeepL sempat salah menerjemahkan jadi "secara sengaja".
- enforce: mewajibkan, menegakkan aturan.
- looser: lebih longgar.
- caller / callee: yang memanggil / yang dipanggil.
- invoke: memanggil, sama dengan call.
- honor system: sistem yang mengandalkan kepercayaan, seperti kantin kejujuran.
- presumptuously: dengan main anggap, berasumsi seenaknya. DeepL menerjemahkan "dengan sombong", kurang pas di sini.
- inevitable: tidak bisa dihindari, pasti terjadi.
- yell: berteriak. Program yang terus mengeluarkan pesan error seperti "yelling at the user".

### Kata kunci baru hari ini
- `break`, `pass`, dan pemakaian `return` di dalam loop.

### Berikutnya
- Problem Set 3, dikerjakan bersama CS50 Duck.
