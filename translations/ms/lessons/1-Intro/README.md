<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-29T11:53:57+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "ms"
}
-->
> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Seiring berjalannya waktu, sumber daya pengkomputeran menjadi lebih murah, dan lebih banyak data tersedia, sehingga pendekatan rangkaian neural mula menunjukkan prestasi yang hebat dalam menyaingi manusia dalam banyak bidang, seperti penglihatan komputer atau pemahaman pertuturan. Dalam dekad terakhir, istilah Kecerdasan Buatan (AI) sering digunakan sebagai sinonim untuk Rangkaian Neural, kerana kebanyakan kejayaan AI yang kita dengar hari ini adalah berdasarkan teknologi ini.

Kita dapat melihat bagaimana pendekatan berubah, contohnya dalam mencipta program komputer untuk bermain catur:

* Program catur awal berdasarkan pencarian – program secara eksplisit cuba menganggarkan kemungkinan langkah lawan untuk beberapa langkah ke depan, dan memilih langkah terbaik berdasarkan kedudukan optimal yang dapat dicapai dalam beberapa langkah. Ini membawa kepada pembangunan algoritma pencarian yang dikenali sebagai [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Strategi pencarian berfungsi dengan baik pada akhir permainan, di mana ruang pencarian terhad kepada beberapa langkah yang mungkin. Namun, pada permulaan permainan, ruang pencarian sangat besar, dan algoritma dapat diperbaiki dengan belajar daripada perlawanan yang sedia ada antara pemain manusia. Eksperimen berikutnya menggunakan pendekatan yang dikenali sebagai [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), di mana program mencari kes dalam pangkalan data yang sangat mirip dengan kedudukan semasa dalam permainan.
* Program moden yang mampu mengalahkan pemain manusia kini berdasarkan rangkaian neural dan [pembelajaran pengukuhan](https://en.wikipedia.org/wiki/Reinforcement_learning), di mana program belajar bermain hanya dengan bermain melawan dirinya sendiri untuk jangka masa yang panjang dan belajar daripada kesilapan sendiri – sama seperti manusia belajar bermain catur. Namun, program komputer dapat bermain lebih banyak permainan dalam masa yang jauh lebih singkat, dan dengan itu dapat belajar dengan lebih cepat.

✅ Lakukan sedikit kajian tentang permainan lain yang telah dimainkan oleh AI.

Begitu juga, kita dapat melihat bagaimana pendekatan untuk mencipta "program bercakap" (yang mungkin lulus ujian Turing) telah berubah:

* Program awal seperti [Eliza](https://en.wikipedia.org/wiki/ELIZA), berdasarkan peraturan tatabahasa yang sangat mudah dan pembentukan semula ayat input menjadi soalan.
* Pembantu moden seperti Cortana, Siri atau Google Assistant adalah sistem hibrid yang menggunakan rangkaian neural untuk menukar pertuturan kepada teks dan mengenali niat pengguna, kemudian menggunakan beberapa penaakulan atau algoritma eksplisit untuk melaksanakan tindakan yang diperlukan.
* Pada masa depan, kita mungkin menjangkakan model berasaskan neural sepenuhnya untuk mengendalikan dialog secara sendiri. Keluarga rangkaian neural seperti GPT dan [Turing-NLG](https://turing.microsoft.com/) baru-baru ini menunjukkan kejayaan besar dalam bidang ini.

> Gambar oleh Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) oleh [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Penyelidikan AI Terkini

Pertumbuhan besar dalam penyelidikan rangkaian neural bermula sekitar tahun 2010, apabila dataset awam yang besar mula tersedia. Koleksi besar gambar yang dipanggil [ImageNet](https://en.wikipedia.org/wiki/ImageNet), yang mengandungi sekitar 14 juta gambar yang telah dianotasi, melahirkan [Cabaran Pengiktirafan Visual Skala Besar ImageNet](https://image-net.org/challenges/LSVRC/).

![Ketepatan ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Pada tahun 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) pertama kali digunakan dalam klasifikasi gambar, yang membawa kepada penurunan ketara dalam kesilapan klasifikasi (daripada hampir 30% kepada 16.4%). Pada tahun 2015, seni bina ResNet dari Microsoft Research [mencapai ketepatan setara manusia](https://doi.org/10.1109/ICCV.2015.123).

Sejak itu, Rangkaian Neural menunjukkan prestasi yang sangat berjaya dalam banyak tugas:

---

Tahun | Ketepatan Setara Manusia Dicapai
-----|--------
2015 | [Klasifikasi Gambar](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Pengiktirafan Ucapan Perbualan](https://arxiv.org/abs/1610.05256)
2018 | [Terjemahan Mesin Automatik](https://arxiv.org/abs/1803.05567) (Cina-ke-Inggeris)
2020 | [Penerangan Gambar](https://arxiv.org/abs/2009.13682)

Dalam beberapa tahun kebelakangan ini, kita telah menyaksikan kejayaan besar dengan model bahasa berskala besar, seperti BERT dan GPT-3. Ini berlaku terutamanya kerana terdapat banyak data teks umum yang tersedia yang membolehkan kita melatih model untuk menangkap struktur dan makna teks, melatih awal model pada koleksi teks umum, dan kemudian mengkhususkan model tersebut untuk tugas yang lebih spesifik. Kita akan belajar lebih lanjut tentang [Pemprosesan Bahasa Semula Jadi](../5-NLP/README.md) kemudian dalam kursus ini.

## 🚀 Cabaran

Lakukan lawatan di internet untuk menentukan di mana, pada pendapat anda, AI digunakan dengan paling berkesan. Adakah ia dalam aplikasi Pemetaan, atau perkhidmatan ucapan-ke-teks, atau permainan video? Selidik bagaimana sistem tersebut dibangunkan.

## [Kuiz selepas kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Ulasan & Kajian Kendiri

Tinjau sejarah AI dan ML dengan membaca [pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Ambil satu elemen daripada sketchnote di bahagian atas pelajaran tersebut atau pelajaran ini dan selidik dengan lebih mendalam untuk memahami konteks budaya yang mempengaruhi evolusinya.

**Tugasan**: [Game Jam](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.