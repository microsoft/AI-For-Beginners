<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-29T11:44:38+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "ms"
}
-->
# Algoritma Genetik

## [Kuiz pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algoritma Genetik** (GA) berasaskan pendekatan **evolusi** dalam AI, di mana kaedah evolusi populasi digunakan untuk mendapatkan penyelesaian optimum bagi sesuatu masalah. Ia dicadangkan pada tahun 1975 oleh [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algoritma Genetik berasaskan idea berikut:

* Penyelesaian yang sah untuk masalah boleh diwakili sebagai **gen**
* **Crossover** membolehkan kita menggabungkan dua penyelesaian untuk mendapatkan penyelesaian baru yang sah
* **Pemilihan** digunakan untuk memilih penyelesaian yang lebih optimum menggunakan beberapa **fungsi kecergasan**
* **Mutasi** diperkenalkan untuk mengganggu pengoptimuman dan mengelakkan kita terperangkap dalam minimum tempatan

Jika anda ingin melaksanakan Algoritma Genetik, anda memerlukan perkara berikut:

 * Mencari kaedah untuk mengekod penyelesaian masalah kita menggunakan **gen** g∈Γ
 * Pada set gen Γ, kita perlu mentakrifkan **fungsi kecergasan** fit: Γ→**R**. Nilai fungsi yang lebih kecil menunjukkan penyelesaian yang lebih baik.
 * Mentakrifkan mekanisme **crossover** untuk menggabungkan dua gen bagi mendapatkan penyelesaian baru yang sah crossover: Γ<sup>2</sub>→Γ.
 * Mentakrifkan mekanisme **mutasi** mutate: Γ→Γ.

Dalam banyak kes, crossover dan mutasi adalah algoritma yang agak mudah untuk memanipulasi gen sebagai jujukan angka atau vektor bit.

Pelaksanaan khusus algoritma genetik boleh berbeza dari satu kes ke kes lain, tetapi struktur keseluruhannya adalah seperti berikut:

1. Pilih populasi awal G⊂Γ
2. Pilih secara rawak salah satu operasi yang akan dilakukan pada langkah ini: crossover atau mutasi
3. **Crossover**:
  * Pilih secara rawak dua gen g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Kira crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jika fit(g)<fit(g<sub>1</sub>) atau fit(g)<fit(g<sub>2</sub>) - gantikan gen yang sepadan dalam populasi dengan g.
4. **Mutasi** - pilih gen rawak g∈G dan gantikannya dengan mutate(g)
5. Ulang dari langkah 2, sehingga kita mendapat nilai fit yang cukup kecil, atau sehingga had bilangan langkah tercapai.

## Tugas Biasa

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

## [Kuiz pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Kajian & Pembelajaran Kendiri

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membincangkan bagaimana komputer boleh belajar bermain Super Mario menggunakan rangkaian neural yang dilatih oleh algoritma genetik. Kita akan belajar lebih lanjut tentang komputer yang belajar bermain permainan seperti itu [dalam bahagian seterusnya](../22-DeepRL/README.md).

## [Tugasan: Persamaan Diofantin](Diophantine.ipynb)

Matlamat anda adalah untuk menyelesaikan apa yang dipanggil **persamaan Diofantin** - persamaan dengan akar integer. Sebagai contoh, pertimbangkan persamaan a+2b+3c+4d=30. Anda perlu mencari akar integer yang memenuhi persamaan ini.

*Tugasan ini diilhamkan oleh [catatan ini](https://habr.com/post/128704/).*

Petunjuk:

1. Anda boleh mempertimbangkan akar dalam selang [0;30]
1. Sebagai gen, pertimbangkan untuk menggunakan senarai nilai akar

Gunakan [Diophantine.ipynb](Diophantine.ipynb) sebagai titik permulaan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.