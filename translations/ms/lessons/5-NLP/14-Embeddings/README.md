# Penyematan

## [Kuis pra-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Ketika melatih pengklasifikasi berdasarkan BoW atau TF/IDF, kami bekerja pada vektor bag-of-words berdimensi tinggi dengan panjang `vocab_size`, dan kami secara eksplisit mengubah dari vektor representasi posisi berdimensi rendah menjadi representasi one-hot yang jarang. Namun, representasi one-hot ini tidak efisien dalam penggunaan memori. Selain itu, setiap kata diperlakukan secara independen satu sama lain, yaitu vektor yang di-encode one-hot tidak mengekspresikan kesamaan semantik antara kata-kata.

Ide dari **penyematan** adalah untuk merepresentasikan kata-kata dengan vektor padat berdimensi lebih rendah, yang entah bagaimana mencerminkan makna semantik dari sebuah kata. Kita akan membahas lebih lanjut bagaimana membangun penyematan kata yang bermakna, tetapi untuk saat ini mari kita anggap penyematan sebagai cara untuk mengurangi dimensi dari vektor kata.

Jadi, lapisan penyematan akan mengambil sebuah kata sebagai input, dan menghasilkan vektor output dengan panjang yang ditentukan `embedding_size`. Dalam hal ini, ini sangat mirip dengan lapisan `Linear`, tetapi alih-alih mengambil vektor yang di-encode one-hot, ia akan dapat menerima nomor kata sebagai input, memungkinkan kita untuk menghindari pembuatan vektor yang besar dengan encoding one-hot.

Dengan menggunakan lapisan penyematan sebagai lapisan pertama dalam jaringan pengklasifikasi kita, kita dapat beralih dari model bag-of-words ke model **embedding bag**, di mana kita pertama-tama mengonversi setiap kata dalam teks kita menjadi penyematan yang sesuai, dan kemudian menghitung beberapa fungsi agregat atas semua penyematan tersebut, seperti `sum`, `average` atau `max`.

![Gambar yang menunjukkan pengklasifikasi penyematan untuk lima kata urutan.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.ms.png)

> Gambar oleh penulis

## ✍️ Latihan: Penyematan

Lanjutkan pembelajaran Anda di notebook berikut:
* [Penyematan dengan PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Penyematan TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Penyematan Semantik: Word2Vec

Sementara lapisan penyematan belajar untuk memetakan kata-kata ke representasi vektor, representasi ini tidak selalu memiliki banyak makna semantik. Akan sangat baik jika kita dapat belajar representasi vektor sedemikian rupa sehingga kata-kata yang serupa atau sinonim berkorespondensi dengan vektor yang dekat satu sama lain dalam hal jarak vektor tertentu (misalnya, jarak Euclidean).

Untuk melakukan itu, kita perlu melatih model penyematan kita terlebih dahulu pada koleksi teks besar dengan cara tertentu. Salah satu cara untuk melatih penyematan semantik disebut [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Ini didasarkan pada dua arsitektur utama yang digunakan untuk menghasilkan representasi terdistribusi dari kata-kata:

 - **Continuous bag-of-words** (CBoW) — dalam arsitektur ini, kita melatih model untuk memprediksi sebuah kata dari konteks sekitarnya. Mengingat ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, tujuan model adalah untuk memprediksi $W_0$ dari $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** adalah kebalikan dari CBoW. Model ini menggunakan jendela kata konteks di sekitarnya untuk memprediksi kata saat ini.

CBoW lebih cepat, sementara skip-gram lebih lambat, tetapi lebih baik dalam merepresentasikan kata-kata yang jarang.

![Gambar yang menunjukkan algoritma CBoW dan Skip-Gram untuk mengonversi kata menjadi vektor.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.ms.png)

> Gambar dari [makalah ini](https://arxiv.org/pdf/1301.3781.pdf)

Penyematan yang sudah dilatih sebelumnya dengan Word2Vec (serta model serupa lainnya, seperti GloVe) juga dapat digunakan sebagai pengganti lapisan penyematan dalam jaringan saraf. Namun, kita perlu menangani kosakata, karena kosakata yang digunakan untuk melatih Word2Vec/GloVe kemungkinan berbeda dari kosakata dalam korpus teks kita. Lihatlah notebook di atas untuk melihat bagaimana masalah ini dapat diatasi.

## Penyematan Kontekstual

Salah satu keterbatasan utama dari representasi penyematan yang dilatih sebelumnya seperti Word2Vec adalah masalah disambiguasi makna kata. Meskipun penyematan yang dilatih sebelumnya dapat menangkap beberapa makna kata dalam konteks, setiap kemungkinan makna dari sebuah kata dienkode ke dalam penyematan yang sama. Ini dapat menyebabkan masalah dalam model hilir, karena banyak kata seperti kata 'play' memiliki makna yang berbeda tergantung pada konteks di mana kata tersebut digunakan.

Misalnya, kata 'play' dalam dua kalimat berbeda ini memiliki makna yang cukup berbeda:

- Saya pergi ke **pertunjukan** di teater.
- John ingin **bermain** dengan teman-temannya.

Penyematan yang dilatih sebelumnya di atas merepresentasikan kedua makna dari kata 'play' dalam penyematan yang sama. Untuk mengatasi keterbatasan ini, kita perlu membangun penyematan berdasarkan **model bahasa**, yang dilatih pada korpus teks besar, dan *tahu* bagaimana kata-kata dapat disusun dalam konteks yang berbeda. Membahas penyematan kontekstual berada di luar cakupan tutorial ini, tetapi kita akan kembali ke topik tersebut saat membahas model bahasa nanti dalam kursus.

## Kesimpulan

Dalam pelajaran ini, Anda telah menemukan cara membangun dan menggunakan lapisan penyematan di TensorFlow dan Pytorch untuk lebih mencerminkan makna semantik dari kata-kata.

## 🚀 Tantangan

Word2Vec telah digunakan untuk beberapa aplikasi menarik, termasuk menghasilkan lirik lagu dan puisi. Lihatlah [artikel ini](https://www.politetype.com/blog/word2vec-color-poems) yang menjelaskan bagaimana penulis menggunakan Word2Vec untuk menghasilkan puisi. Tonton juga [video ini oleh Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) untuk menemukan penjelasan berbeda tentang teknik ini. Kemudian coba terapkan teknik ini pada korpus teks Anda sendiri, mungkin diambil dari Kaggle.

## [Kuis pasca-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Tinjauan & Studi Mandiri

Baca makalah ini tentang Word2Vec: [Estimasi Efisien Representasi Kata dalam Ruang Vektor](https://arxiv.org/pdf/1301.3781.pdf)

## [Tugas: Notebook](assignment.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia yang profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.