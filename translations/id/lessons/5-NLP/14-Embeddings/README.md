<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-29T12:49:07+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "id"
}
-->
# Embeddings

## [Kuis Pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Saat melatih classifier berdasarkan BoW atau TF/IDF, kita bekerja dengan vektor bag-of-words berdimensi tinggi dengan panjang `vocab_size`, dan secara eksplisit mengonversi dari vektor representasi posisi berdimensi rendah menjadi representasi one-hot yang jarang. Namun, representasi one-hot ini tidak efisien dalam penggunaan memori. Selain itu, setiap kata diperlakukan secara independen satu sama lain, yaitu vektor one-hot tidak mengekspresikan kesamaan semantik antara kata-kata.

Ide dari **embedding** adalah untuk merepresentasikan kata-kata dengan vektor berdimensi rendah yang padat, yang entah bagaimana mencerminkan makna semantik dari sebuah kata. Kita akan membahas lebih lanjut bagaimana membangun embedding kata yang bermakna, tetapi untuk saat ini mari kita anggap embedding sebagai cara untuk menurunkan dimensi vektor kata.

Jadi, lapisan embedding akan mengambil sebuah kata sebagai input, dan menghasilkan vektor output dengan ukuran `embedding_size` yang ditentukan. Dalam arti tertentu, ini sangat mirip dengan lapisan `Linear`, tetapi alih-alih mengambil vektor one-hot sebagai input, lapisan ini dapat mengambil nomor kata sebagai input, memungkinkan kita untuk menghindari pembuatan vektor one-hot yang besar.

Dengan menggunakan lapisan embedding sebagai lapisan pertama dalam jaringan classifier kita, kita dapat beralih dari model bag-of-words ke model **embedding bag**, di mana kita pertama-tama mengonversi setiap kata dalam teks kita menjadi embedding yang sesuai, dan kemudian menghitung beberapa fungsi agregat atas semua embedding tersebut, seperti `sum`, `average`, atau `max`.

![Gambar menunjukkan classifier embedding untuk lima kata dalam urutan.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.id.png)

> Gambar oleh penulis

## ✍️ Latihan: Embeddings

Lanjutkan pembelajaran Anda di notebook berikut:
* [Embeddings dengan PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](EmbeddingsTF.ipynb)

## Embedding Semantik: Word2Vec

Meskipun lapisan embedding belajar memetakan kata-kata ke representasi vektor, representasi ini belum tentu memiliki banyak makna semantik. Akan lebih baik jika kita dapat mempelajari representasi vektor sedemikian rupa sehingga kata-kata yang mirip atau sinonim memiliki vektor yang dekat satu sama lain dalam hal jarak vektor tertentu (misalnya, jarak Euclidean).

Untuk melakukannya, kita perlu melatih model embedding kita sebelumnya pada koleksi teks yang besar dengan cara tertentu. Salah satu cara untuk melatih embedding semantik disebut [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Word2Vec didasarkan pada dua arsitektur utama yang digunakan untuk menghasilkan representasi terdistribusi dari kata-kata:

 - **Continuous bag-of-words** (CBoW) — dalam arsitektur ini, kita melatih model untuk memprediksi sebuah kata dari konteks sekitarnya. Diberikan ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, tujuan model adalah memprediksi $W_0$ dari $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** adalah kebalikan dari CBoW. Model menggunakan jendela kata-kata konteks di sekitar untuk memprediksi kata saat ini.

CBoW lebih cepat, sedangkan skip-gram lebih lambat, tetapi lebih baik dalam merepresentasikan kata-kata yang jarang muncul.

![Gambar menunjukkan algoritma CBoW dan Skip-Gram untuk mengonversi kata menjadi vektor.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.id.png)

> Gambar dari [makalah ini](https://arxiv.org/pdf/1301.3781.pdf)

Embedding yang telah dilatih sebelumnya dengan Word2Vec (serta model serupa lainnya, seperti GloVe) juga dapat digunakan sebagai pengganti lapisan embedding dalam jaringan neural. Namun, kita perlu menangani kosakata, karena kosakata yang digunakan untuk melatih Word2Vec/GloVe kemungkinan berbeda dari kosakata dalam korpus teks kita. Lihatlah ke dalam Notebook di atas untuk melihat bagaimana masalah ini dapat diselesaikan.

## Embedding Kontekstual

Salah satu keterbatasan utama dari representasi embedding yang telah dilatih sebelumnya seperti Word2Vec adalah masalah disambiguasi makna kata. Meskipun embedding yang telah dilatih sebelumnya dapat menangkap sebagian makna kata dalam konteks, setiap kemungkinan makna dari sebuah kata dikodekan ke dalam embedding yang sama. Hal ini dapat menyebabkan masalah dalam model lanjutan, karena banyak kata seperti 'play' memiliki makna yang berbeda tergantung pada konteks penggunaannya.

Sebagai contoh, kata 'play' dalam dua kalimat berikut memiliki makna yang sangat berbeda:

- Saya pergi ke sebuah **play** di teater.
- John ingin **play** dengan teman-temannya.

Embedding yang telah dilatih sebelumnya di atas merepresentasikan kedua makna kata 'play' ini dalam embedding yang sama. Untuk mengatasi keterbatasan ini, kita perlu membangun embedding berdasarkan **model bahasa**, yang dilatih pada korpus teks yang besar, dan *memahami* bagaimana kata-kata dapat disusun dalam berbagai konteks. Membahas embedding kontekstual berada di luar cakupan tutorial ini, tetapi kita akan kembali ke topik ini saat membahas model bahasa di bagian kursus selanjutnya.

## Kesimpulan

Dalam pelajaran ini, Anda mempelajari cara membangun dan menggunakan lapisan embedding di TensorFlow dan PyTorch untuk lebih mencerminkan makna semantik dari kata-kata.

## 🚀 Tantangan

Word2Vec telah digunakan untuk beberapa aplikasi menarik, termasuk menghasilkan lirik lagu dan puisi. Lihat [artikel ini](https://www.politetype.com/blog/word2vec-color-poems) yang menjelaskan bagaimana penulis menggunakan Word2Vec untuk menghasilkan puisi. Tonton juga [video ini oleh Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) untuk menemukan penjelasan berbeda tentang teknik ini. Kemudian coba terapkan teknik-teknik ini pada korpus teks Anda sendiri, mungkin bersumber dari Kaggle.

## [Kuis Pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Tinjauan & Studi Mandiri

Baca makalah ini tentang Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Tugas: Notebook](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.