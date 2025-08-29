<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-29T12:00:31+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "ms"
}
-->
# Pembenaman

## [Kuiz Pra-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Semasa melatih pengklasifikasi berdasarkan BoW atau TF/IDF, kita bekerja dengan vektor bag-of-words berdimensi tinggi dengan panjang `vocab_size`, dan kita secara eksplisit menukar daripada vektor perwakilan posisi berdimensi rendah kepada perwakilan one-hot yang jarang. Walau bagaimanapun, perwakilan one-hot ini tidak cekap dari segi memori. Selain itu, setiap perkataan dianggap secara bebas antara satu sama lain, iaitu vektor one-hot yang dikodkan tidak menyatakan sebarang persamaan semantik antara perkataan.

Idea **pembenaman** adalah untuk mewakili perkataan dengan vektor berdimensi rendah yang padat, yang mencerminkan makna semantik sesuatu perkataan. Kita akan membincangkan kemudian bagaimana untuk membina pembenaman perkataan yang bermakna, tetapi buat masa ini mari kita anggap pembenaman sebagai cara untuk mengurangkan dimensi vektor perkataan.

Jadi, lapisan pembenaman akan mengambil satu perkataan sebagai input, dan menghasilkan vektor output dengan `embedding_size` yang ditentukan. Dalam satu pengertian, ia sangat serupa dengan lapisan `Linear`, tetapi bukannya mengambil vektor one-hot yang dikodkan, ia akan dapat mengambil nombor perkataan sebagai input, membolehkan kita mengelakkan penciptaan vektor one-hot yang besar.

Dengan menggunakan lapisan pembenaman sebagai lapisan pertama dalam rangkaian pengklasifikasi kita, kita boleh beralih daripada model bag-of-words kepada model **embedding bag**, di mana kita mula-mula menukar setiap perkataan dalam teks kita kepada pembenaman yang sepadan, dan kemudian mengira beberapa fungsi agregat ke atas semua pembenaman tersebut, seperti `sum`, `average` atau `max`.

![Imej menunjukkan pengklasifikasi pembenaman untuk lima perkataan dalam urutan.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.ms.png)

> Imej oleh penulis

## ✍️ Latihan: Pembenaman

Teruskan pembelajaran anda dalam buku nota berikut:
* [Pembenaman dengan PyTorch](EmbeddingsPyTorch.ipynb)
* [Pembenaman TensorFlow](EmbeddingsTF.ipynb)

## Pembenaman Semantik: Word2Vec

Walaupun lapisan pembenaman belajar memetakan perkataan kepada perwakilan vektor, perwakilan ini tidak semestinya mempunyai banyak makna semantik. Adalah lebih baik untuk belajar perwakilan vektor sedemikian rupa sehingga perkataan yang serupa atau sinonim sepadan dengan vektor yang dekat antara satu sama lain dari segi jarak vektor tertentu (contohnya, jarak Euclidean).

Untuk melakukan itu, kita perlu melatih model pembenaman kita terlebih dahulu pada koleksi teks yang besar dengan cara tertentu. Salah satu cara untuk melatih pembenaman semantik dipanggil [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Ia berdasarkan dua seni bina utama yang digunakan untuk menghasilkan perwakilan teragih bagi perkataan:

 - **Continuous bag-of-words** (CBoW) — dalam seni bina ini, kita melatih model untuk meramalkan satu perkataan daripada konteks sekeliling. Diberikan ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, matlamat model adalah untuk meramalkan $W_0$ daripada $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** adalah bertentangan dengan CBoW. Model ini menggunakan tetingkap perkataan konteks sekeliling untuk meramalkan perkataan semasa.

CBoW lebih pantas, manakala skip-gram lebih perlahan, tetapi lebih baik dalam mewakili perkataan yang jarang ditemui.

![Imej menunjukkan algoritma CBoW dan Skip-Gram untuk menukar perkataan kepada vektor.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.ms.png)

> Imej daripada [kertas ini](https://arxiv.org/pdf/1301.3781.pdf)

Pembenaman Word2Vec yang telah dilatih terlebih dahulu (serta model serupa lain, seperti GloVe) juga boleh digunakan sebagai ganti lapisan pembenaman dalam rangkaian neural. Walau bagaimanapun, kita perlu menangani kosa kata, kerana kosa kata yang digunakan untuk melatih Word2Vec/GloVe mungkin berbeza daripada kosa kata dalam korpus teks kita. Lihat buku nota di atas untuk melihat bagaimana masalah ini boleh diselesaikan.

## Pembenaman Kontekstual

Satu had utama perwakilan pembenaman pralatih tradisional seperti Word2Vec ialah masalah penyahkekaburan makna perkataan. Walaupun pembenaman pralatih boleh menangkap sebahagian daripada makna perkataan dalam konteks, setiap kemungkinan makna sesuatu perkataan dikodkan ke dalam pembenaman yang sama. Ini boleh menyebabkan masalah dalam model hiliran, kerana banyak perkataan seperti 'play' mempunyai makna yang berbeza bergantung pada konteks penggunaannya.

Sebagai contoh, perkataan 'play' dalam dua ayat berikut mempunyai makna yang agak berbeza:

- Saya pergi ke **play** di teater.
- John mahu **play** dengan kawan-kawannya.

Pembenaman pralatih di atas mewakili kedua-dua makna perkataan 'play' dalam pembenaman yang sama. Untuk mengatasi had ini, kita perlu membina pembenaman berdasarkan **model bahasa**, yang dilatih pada korpus teks yang besar, dan *tahu* bagaimana perkataan boleh disusun dalam konteks yang berbeza. Perbincangan tentang pembenaman kontekstual adalah di luar skop tutorial ini, tetapi kita akan kembali kepada topik ini apabila membincangkan model bahasa kemudian dalam kursus.

## Kesimpulan

Dalam pelajaran ini, anda telah mempelajari cara membina dan menggunakan lapisan pembenaman dalam TensorFlow dan Pytorch untuk lebih mencerminkan makna semantik perkataan.

## 🚀 Cabaran

Word2Vec telah digunakan untuk beberapa aplikasi menarik, termasuk menjana lirik lagu dan puisi. Lihat [artikel ini](https://www.politetype.com/blog/word2vec-color-poems) yang menerangkan bagaimana penulis menggunakan Word2Vec untuk menjana puisi. Tonton juga [video ini oleh Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) untuk penjelasan lain tentang teknik ini. Kemudian cuba gunakan teknik ini pada korpus teks anda sendiri, mungkin daripada sumber seperti Kaggle.

## [Kuiz Pasca-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Kajian & Pembelajaran Kendiri

Baca kertas ini tentang Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Tugasan: Buku Nota](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.