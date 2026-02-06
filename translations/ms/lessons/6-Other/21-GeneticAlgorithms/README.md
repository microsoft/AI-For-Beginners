# Algoritma Genetik

## [Kuiz pra-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algoritma Genetik** (GA) berasaskan pendekatan **evolusi** dalam AI, di mana kaedah evolusi populasi digunakan untuk mendapatkan penyelesaian optimum bagi sesuatu masalah. Ia dicadangkan pada tahun 1975 oleh [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algoritma Genetik berasaskan idea berikut:

* Penyelesaian yang sah untuk masalah boleh diwakili sebagai **gen**
* **Crossover** membolehkan kita menggabungkan dua penyelesaian untuk mendapatkan penyelesaian baru yang sah
* **Pemilihan** digunakan untuk memilih penyelesaian yang lebih optimum menggunakan beberapa **fungsi kecergasan**
* **Mutasi** diperkenalkan untuk mengganggu pengoptimuman dan mengelakkan kita terperangkap dalam minimum tempatan

Jika anda ingin melaksanakan Algoritma Genetik, anda memerlukan perkara berikut:

 * Mencari kaedah untuk mengekod penyelesaian masalah menggunakan **gen** g&in;&Gamma;
 * Pada set gen &Gamma;, kita perlu mentakrifkan **fungsi kecergasan** fit: &Gamma;&rightarrow;**R**. Nilai fungsi yang lebih kecil menunjukkan penyelesaian yang lebih baik.
 * Mentakrifkan mekanisme **crossover** untuk menggabungkan dua gen bersama-sama untuk mendapatkan penyelesaian baru yang sah crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Mentakrifkan mekanisme **mutasi** mutate: &Gamma;&rightarrow;&Gamma;.

Dalam banyak kes, crossover dan mutasi adalah algoritma yang agak mudah untuk memanipulasi gen sebagai jujukan angka atau vektor bit.

Pelaksanaan spesifik algoritma genetik boleh berbeza-beza mengikut kes, tetapi struktur keseluruhannya adalah seperti berikut:

1. Pilih populasi awal G&subset;&Gamma;
2. Pilih secara rawak salah satu operasi yang akan dilakukan pada langkah ini: crossover atau mutasi
3. **Crossover**:
  * Pilih secara rawak dua gen g<sub>1</sub>, g<sub>2</sub> &in; G
  * Kira crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jika fit(g)<fit(g<sub>1</sub>) atau fit(g)<fit(g<sub>2</sub>) - gantikan gen yang sepadan dalam populasi dengan g.
4. **Mutasi** - pilih gen rawak g&in;G dan gantikannya dengan mutate(g)
5. Ulang dari langkah 2, sehingga kita mendapat nilai fit yang cukup kecil, atau sehingga had pada bilangan langkah tercapai.

## Tugas Tipikal

Tugas yang biasanya diselesaikan oleh Algoritma Genetik termasuk:

1. Pengoptimuman jadual
1. Pembungkusan optimum
1. Pemotongan optimum
1. Mempercepatkan pencarian menyeluruh

## ✍️ Latihan: Algoritma Genetik

Teruskan pembelajaran anda dalam buku nota berikut:

Pergi ke [buku nota ini](Genetic.ipynb) untuk melihat dua contoh penggunaan Algoritma Genetik:

1. Pembahagian harta yang adil
1. Masalah 8 Permaisuri

## Kesimpulan

Algoritma Genetik digunakan untuk menyelesaikan banyak masalah, termasuk logistik dan masalah pencarian. Bidang ini diilhamkan oleh penyelidikan yang menggabungkan topik dalam Psikologi dan Sains Komputer.

## 🚀 Cabaran

"Algoritma genetik mudah dilaksanakan, tetapi tingkah lakunya sukar difahami." [sumber](https://wikipedia.org/wiki/Genetic_algorithm) Lakukan sedikit penyelidikan untuk mencari pelaksanaan algoritma genetik seperti menyelesaikan teka-teki Sudoku, dan terangkan bagaimana ia berfungsi dalam bentuk lakaran atau carta alir.

## [Kuiz pasca-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Ulasan & Kajian Kendiri

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membincangkan bagaimana komputer boleh belajar bermain Super Mario menggunakan rangkaian neural yang dilatih oleh algoritma genetik. Kita akan belajar lebih lanjut tentang pembelajaran komputer untuk bermain permainan seperti itu [dalam bahagian seterusnya](../22-DeepRL/README.md).

## [Tugasan: Persamaan Diofantin](Diophantine.ipynb)

Matlamat anda adalah untuk menyelesaikan apa yang dipanggil **persamaan Diofantin** - persamaan dengan akar integer. Sebagai contoh, pertimbangkan persamaan a+2b+3c+4d=30. Anda perlu mencari akar integer yang memenuhi persamaan ini.

*Tugasan ini diilhamkan oleh [catatan ini](https://habr.com/post/128704/).*

Petunjuk:

1. Anda boleh mempertimbangkan akar dalam julat [0;30]
1. Sebagai gen, pertimbangkan untuk menggunakan senarai nilai akar

Gunakan [Diophantine.ipynb](Diophantine.ipynb) sebagai titik permulaan.

---

