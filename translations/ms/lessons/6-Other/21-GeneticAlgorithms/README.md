# Algoritma Genetik

## [Kuiz pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algoritma Genetik** (GA) berasaskan pada pendekatan **evolusi** untuk AI, di mana kaedah evolusi populasi digunakan untuk mendapatkan penyelesaian optimum bagi masalah tertentu. Mereka dicadangkan pada tahun 1975 oleh [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algoritma Genetik berasaskan kepada idea berikut:

* Penyelesaian yang sah kepada masalah boleh diwakili sebagai **gen**
* **Penyilangan** membolehkan kita menggabungkan dua penyelesaian untuk mendapatkan penyelesaian sah yang baru
* **Pemilihan** digunakan untuk memilih penyelesaian yang lebih optimum menggunakan beberapa **fungsi kecergasan**
* **Mutasi** diperkenalkan untuk mengganggu pengoptimuman dan mengeluarkan kita dari minimum tempatan

Jika anda ingin melaksanakan Algoritma Genetik, anda memerlukan yang berikut:

 * Untuk mencari kaedah pengkodan penyelesaian masalah kita menggunakan **gen** g∈Γ
 * Pada set gen Γ, kita perlu mendefinisikan **fungsi kecergasan** fit: Γ→**R**. Nilai fungsi yang lebih kecil berkaitan dengan penyelesaian yang lebih baik.
 * Untuk mendefinisikan mekanisme **penyilangan** untuk menggabungkan dua gen untuk mendapatkan penyelesaian sah yang baru crossover: Γ<sup>2</sub>→Γ.
 * Untuk mendefinisikan mekanisme **mutasi** mutate: Γ→Γ.

Dalam banyak kes, penyilangan dan mutasi adalah algoritma yang agak mudah untuk memanipulasi gen sebagai urutan numerik atau vektor bit.

Pelaksanaan khusus algoritma genetik boleh berbeza dari kes ke kes, tetapi struktur keseluruhannya adalah seperti berikut:

1. Pilih populasi awal G⊂Γ
2. Pilih secara rawak salah satu operasi yang akan dilakukan pada langkah ini: penyilangan atau mutasi
3. **Penyilangan**:
  * Pilih secara rawak dua gen g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Kira penyilangan g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jika fit(g)<fit(g<sub>1</sub>) atau fit(g)<fit(g<sub>2</sub>) - gantikan gen yang berkaitan dalam populasi dengan g.
4. **Mutasi** - pilih gen rawak g∈G dan gantikannya dengan mutate(g)
5. Ulang dari langkah 2, sehingga kita mendapatkan nilai fit yang cukup kecil, atau sehingga had pada bilangan langkah dicapai.

## Tugas Tipikal

Tugas yang biasanya diselesaikan oleh Algoritma Genetik termasuk:

1. Pengoptimuman jadual
1. Pengemasan optimum
1. Pemotongan optimum
1. Mempercepat pencarian menyeluruh

## ✍️ Latihan: Algoritma Genetik

Teruskan pembelajaran anda dalam notebook berikut:

Pergi ke [notebook ini](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) untuk melihat dua contoh penggunaan Algoritma Genetik:

1. Pembahagian harta yang adil
1. Masalah 8 Ratu

## Kesimpulan

Algoritma Genetik digunakan untuk menyelesaikan banyak masalah, termasuk masalah logistik dan pencarian. Bidang ini diinspirasikan oleh penyelidikan yang menggabungkan topik dalam Psikologi dan Sains Komputer. 

## 🚀 Cabaran

"Algoritma genetik mudah untuk dilaksanakan, tetapi tingkah lakunya sukar untuk difahami." [sumber](https://wikipedia.org/wiki/Genetic_algorithm) Lakukan penyelidikan untuk mencari pelaksanaan algoritma genetik seperti menyelesaikan teka-teki Sudoku, dan terangkan bagaimana ia berfungsi sebagai lakaran atau carta aliran.

## [Kuiz pasca-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Ulasan & Pembelajaran Sendiri

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membincangkan bagaimana komputer boleh belajar untuk bermain Super Mario menggunakan rangkaian neural yang dilatih oleh algoritma genetik. Kita akan belajar lebih lanjut tentang pembelajaran komputer untuk bermain permainan seperti itu [dalam seksyen seterusnya](../22-DeepRL/README.md).

## [Tugasan: Persamaan Diophantine](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Matlamat anda adalah untuk menyelesaikan apa yang dipanggil **persamaan Diophantine** - persamaan dengan akar integer. Sebagai contoh, pertimbangkan persamaan a+2b+3c+4d=30. Anda perlu mencari akar integer yang memenuhi persamaan ini.

*Tugasan ini diinspirasikan oleh [pos ini](https://habr.com/post/128704/).*

Petunjuk:

1. Anda boleh mempertimbangkan akar berada dalam selang [0;30]
1. Sebagai gen, pertimbangkan menggunakan senarai nilai akar

Gunakan [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) sebagai titik permulaan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat kritikal, terjemahan manusia yang profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.