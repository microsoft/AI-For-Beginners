<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-29T12:33:22+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "id"
}
-->
> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Seiring waktu, sumber daya komputasi menjadi lebih murah, dan lebih banyak data tersedia, sehingga pendekatan jaringan saraf mulai menunjukkan kinerja yang luar biasa dalam bersaing dengan manusia di banyak bidang, seperti penglihatan komputer atau pemahaman ucapan. Dalam dekade terakhir, istilah Kecerdasan Buatan sebagian besar digunakan sebagai sinonim untuk Jaringan Saraf, karena sebagian besar keberhasilan AI yang kita dengar didasarkan pada teknologi ini.

Kita dapat mengamati bagaimana pendekatan berubah, misalnya, dalam menciptakan program komputer yang bermain catur:

* Program catur awal didasarkan pada pencarian – program secara eksplisit mencoba memperkirakan kemungkinan langkah lawan untuk sejumlah langkah berikutnya, dan memilih langkah optimal berdasarkan posisi terbaik yang dapat dicapai dalam beberapa langkah. Hal ini mengarah pada pengembangan algoritma pencarian yang disebut [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Strategi pencarian bekerja dengan baik menjelang akhir permainan, di mana ruang pencarian terbatas oleh sejumlah kecil langkah yang mungkin. Namun, pada awal permainan, ruang pencarian sangat besar, dan algoritma dapat ditingkatkan dengan belajar dari pertandingan yang sudah ada antara pemain manusia. Eksperimen berikutnya menggunakan pendekatan yang disebut [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), di mana program mencari kasus dalam basis pengetahuan yang sangat mirip dengan posisi saat ini dalam permainan.
* Program modern yang mengalahkan pemain manusia didasarkan pada jaringan saraf dan [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), di mana program belajar bermain hanya dengan bermain dalam waktu lama melawan dirinya sendiri dan belajar dari kesalahan mereka sendiri – mirip dengan cara manusia belajar bermain catur. Namun, program komputer dapat memainkan lebih banyak permainan dalam waktu yang jauh lebih singkat, sehingga dapat belajar jauh lebih cepat.

✅ Lakukan sedikit penelitian tentang permainan lain yang telah dimainkan oleh AI.

Demikian pula, kita dapat melihat bagaimana pendekatan terhadap penciptaan program "berbicara" (yang mungkin lulus uji Turing) telah berubah:

* Program awal seperti [Eliza](https://en.wikipedia.org/wiki/ELIZA), didasarkan pada aturan tata bahasa yang sangat sederhana dan reformulasi kalimat masukan menjadi sebuah pertanyaan.
* Asisten modern, seperti Cortana, Siri, atau Google Assistant adalah sistem hibrida yang menggunakan jaringan saraf untuk mengubah ucapan menjadi teks dan mengenali maksud kita, lalu menggunakan beberapa penalaran atau algoritma eksplisit untuk melakukan tindakan yang diperlukan.
* Di masa depan, kita mungkin mengharapkan model berbasis jaringan saraf sepenuhnya untuk menangani dialog secara mandiri. Keluarga jaringan saraf GPT dan [Turing-NLG](https://turing.microsoft.com/) baru-baru ini menunjukkan keberhasilan besar dalam hal ini.

> Gambar oleh Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) oleh [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Penelitian AI Terkini

Pertumbuhan besar dalam penelitian jaringan saraf mulai sekitar tahun 2010, ketika dataset publik besar mulai tersedia. Sebuah koleksi besar gambar yang disebut [ImageNet](https://en.wikipedia.org/wiki/ImageNet), yang berisi sekitar 14 juta gambar beranotasi, melahirkan [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Akurasi ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Pada tahun 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) pertama kali digunakan dalam klasifikasi gambar, yang menyebabkan penurunan signifikan dalam kesalahan klasifikasi (dari hampir 30% menjadi 16,4%). Pada tahun 2015, arsitektur ResNet dari Microsoft Research [mencapai akurasi setara manusia](https://doi.org/10.1109/ICCV.2015.123).

Sejak saat itu, Jaringan Saraf menunjukkan performa yang sangat sukses dalam banyak tugas:

---

Tahun | Paritas dengan Manusia Dicapai
-----|--------
2015 | [Klasifikasi Gambar](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Pengakuan Ucapan Percakapan](https://arxiv.org/abs/1610.05256)
2018 | [Penerjemahan Mesin Otomatis](https://arxiv.org/abs/1803.05567) (Cina-ke-Inggris)
2020 | [Pembuatan Caption Gambar](https://arxiv.org/abs/2009.13682)

Selama beberapa tahun terakhir, kita telah menyaksikan keberhasilan besar dengan model bahasa besar, seperti BERT dan GPT-3. Hal ini sebagian besar terjadi karena banyaknya data teks umum yang tersedia, yang memungkinkan kita melatih model untuk menangkap struktur dan makna teks, melatih model tersebut pada koleksi teks umum, dan kemudian mengkhususkan model tersebut untuk tugas yang lebih spesifik. Kita akan mempelajari lebih lanjut tentang [Natural Language Processing](../5-NLP/README.md) nanti dalam kursus ini.

## 🚀 Tantangan

Lakukan penelusuran di internet untuk menentukan, menurut pendapat Anda, di mana AI paling efektif digunakan. Apakah itu di aplikasi peta, layanan pengubah ucapan ke teks, atau video game? Teliti bagaimana sistem tersebut dibangun.

## [Kuis setelah kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Tinjauan & Studi Mandiri

Tinjau sejarah AI dan ML dengan membaca [pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Ambil satu elemen dari sketchnote di awal pelajaran tersebut atau pelajaran ini dan teliti lebih dalam untuk memahami konteks budaya yang memengaruhi evolusinya.

**Tugas**: [Game Jam](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.