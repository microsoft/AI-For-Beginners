<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-29T12:44:17+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "id"
}
-->
# Mekanisme Perhatian dan Transformer

## [Kuis Pra-Pelajaran](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Salah satu masalah paling penting dalam domain NLP adalah **penerjemahan mesin**, sebuah tugas esensial yang mendasari alat seperti Google Translate. Dalam bagian ini, kita akan fokus pada penerjemahan mesin, atau lebih umum lagi, pada tugas *sequence-to-sequence* (yang juga disebut **transduksi kalimat**).

Dengan RNN, sequence-to-sequence diimplementasikan oleh dua jaringan berulang, di mana satu jaringan, yaitu **encoder**, merangkum urutan input menjadi keadaan tersembunyi, sementara jaringan lainnya, yaitu **decoder**, menguraikan keadaan tersembunyi ini menjadi hasil terjemahan. Ada beberapa masalah dengan pendekatan ini:

* Keadaan akhir dari jaringan encoder sulit mengingat awal kalimat, sehingga menyebabkan kualitas model yang buruk untuk kalimat panjang.
* Semua kata dalam sebuah urutan memiliki dampak yang sama pada hasil. Namun, dalam kenyataannya, kata-kata tertentu dalam urutan input sering memiliki dampak lebih besar pada output berurutan dibandingkan yang lain.

**Mekanisme Perhatian** menyediakan cara untuk memberikan bobot pada dampak kontekstual dari setiap vektor input pada setiap prediksi output dari RNN. Cara ini diimplementasikan dengan menciptakan jalur pintas antara keadaan antara dari RNN input dan RNN output. Dengan cara ini, saat menghasilkan simbol output y<sub>t</sub>, kita akan mempertimbangkan semua keadaan tersembunyi input h<sub>i</sub>, dengan koefisien bobot yang berbeda α<sub>t,i</sub>.

![Gambar menunjukkan model encoder/decoder dengan lapisan perhatian aditif](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.id.png)

> Model encoder-decoder dengan mekanisme perhatian aditif dalam [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), dikutip dari [blog ini](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Matriks perhatian {α<sub>i,j</sub>} akan merepresentasikan sejauh mana kata-kata tertentu dalam input berperan dalam menghasilkan kata tertentu dalam urutan output. Berikut adalah contoh matriks seperti itu:

![Gambar menunjukkan contoh alignment yang ditemukan oleh RNNsearch-50, diambil dari Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.id.png)

> Gambar dari [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Gambar 3)

Mekanisme perhatian bertanggung jawab atas banyak kemajuan terkini atau hampir terkini dalam NLP. Namun, menambahkan perhatian secara signifikan meningkatkan jumlah parameter model, yang menyebabkan masalah skalabilitas dengan RNN. Salah satu kendala utama dalam menskalakan RNN adalah sifat berulang dari model yang membuatnya sulit untuk melakukan pelatihan secara batch dan paralel. Dalam RNN, setiap elemen dari urutan harus diproses secara berurutan, yang berarti tidak dapat dengan mudah diparalelkan.

![Encoder Decoder dengan Perhatian](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Gambar dari [Blog Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Adopsi mekanisme perhatian yang dikombinasikan dengan kendala ini mengarah pada penciptaan Model Transformer yang kini menjadi State of the Art, seperti BERT hingga Open-GPT3.

## Model Transformer

Salah satu ide utama di balik transformer adalah menghindari sifat berurutan dari RNN dan menciptakan model yang dapat diparalelkan selama pelatihan. Hal ini dicapai dengan menerapkan dua ide:

* pengkodean posisi
* menggunakan mekanisme self-attention untuk menangkap pola alih-alih RNN (atau CNN) (itulah sebabnya makalah yang memperkenalkan transformer berjudul *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Pengkodean/Embedding Posisi

Ide pengkodean posisi adalah sebagai berikut. 
1. Saat menggunakan RNN, posisi relatif token direpresentasikan oleh jumlah langkah, sehingga tidak perlu direpresentasikan secara eksplisit. 
2. Namun, begitu kita beralih ke perhatian, kita perlu mengetahui posisi relatif token dalam sebuah urutan. 
3. Untuk mendapatkan pengkodean posisi, kita menambahkan urutan token dengan urutan posisi token dalam urutan (misalnya, urutan angka 0,1, ...).
4. Kita kemudian mencampurkan posisi token dengan vektor embedding token. Untuk mengubah posisi (integer) menjadi vektor, kita dapat menggunakan pendekatan yang berbeda:

* Embedding yang dapat dilatih, mirip dengan embedding token. Ini adalah pendekatan yang kita pertimbangkan di sini. Kita menerapkan lapisan embedding di atas token dan posisinya, menghasilkan vektor embedding dengan dimensi yang sama, yang kemudian kita tambahkan bersama.
* Fungsi pengkodean posisi tetap, seperti yang diusulkan dalam makalah asli.

<img src="images/pos-embedding.png" width="50%"/>

> Gambar oleh penulis

Hasil yang kita dapatkan dengan embedding posisi menggabungkan token asli dan posisinya dalam urutan.

### Multi-Head Self-Attention

Selanjutnya, kita perlu menangkap beberapa pola dalam urutan kita. Untuk melakukan ini, transformer menggunakan mekanisme **self-attention**, yang pada dasarnya adalah perhatian yang diterapkan pada urutan yang sama sebagai input dan output. Menerapkan self-attention memungkinkan kita mempertimbangkan **konteks** dalam kalimat, dan melihat kata-kata mana yang saling terkait. Misalnya, ini memungkinkan kita melihat kata-kata yang dirujuk oleh koreferensi, seperti *itu*, dan juga mempertimbangkan konteks:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.id.png)

> Gambar dari [Blog Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Dalam transformer, kita menggunakan **Multi-Head Attention** untuk memberikan kekuatan pada jaringan dalam menangkap beberapa jenis ketergantungan yang berbeda, misalnya hubungan kata jangka panjang vs. jangka pendek, koreferensi vs. yang lainnya, dll.

[Notebook TensorFlow](TransformersTF.ipynb) berisi detail lebih lanjut tentang implementasi lapisan transformer.

### Perhatian Encoder-Decoder

Dalam transformer, perhatian digunakan di dua tempat:

* Untuk menangkap pola dalam teks input menggunakan self-attention
* Untuk melakukan terjemahan urutan - ini adalah lapisan perhatian antara encoder dan decoder.

Perhatian encoder-decoder sangat mirip dengan mekanisme perhatian yang digunakan dalam RNN, seperti yang dijelaskan di awal bagian ini. Diagram animasi ini menjelaskan peran perhatian encoder-decoder.

![GIF Animasi menunjukkan bagaimana evaluasi dilakukan dalam model transformer.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Karena setiap posisi input dipetakan secara independen ke setiap posisi output, transformer dapat diparalelkan lebih baik daripada RNN, yang memungkinkan model bahasa yang jauh lebih besar dan lebih ekspresif. Setiap kepala perhatian dapat digunakan untuk mempelajari hubungan yang berbeda antara kata-kata yang meningkatkan tugas Pemrosesan Bahasa Alami di hilir.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) adalah jaringan transformer multi-layer yang sangat besar dengan 12 lapisan untuk *BERT-base*, dan 24 untuk *BERT-large*. Model ini pertama kali dilatih pada korpus teks besar (WikiPedia + buku) menggunakan pelatihan tanpa pengawasan (memprediksi kata yang disembunyikan dalam sebuah kalimat). Selama pelatihan awal, model menyerap tingkat pemahaman bahasa yang signifikan yang kemudian dapat dimanfaatkan dengan dataset lain menggunakan fine-tuning. Proses ini disebut **transfer learning**.

![gambar dari http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.id.png)

> Sumber gambar [di sini](http://jalammar.github.io/illustrated-bert/)

## ✍️ Latihan: Transformer

Lanjutkan pembelajaran Anda di notebook berikut:

* [Transformer di PyTorch](TransformersPyTorch.ipynb)
* [Transformer di TensorFlow](TransformersTF.ipynb)

## Kesimpulan

Dalam pelajaran ini, Anda telah mempelajari tentang Transformer dan Mekanisme Perhatian, semua alat penting dalam kotak alat NLP. Ada banyak variasi arsitektur Transformer termasuk BERT, DistilBERT, BigBird, OpenGPT3, dan lainnya yang dapat disesuaikan. Paket [HuggingFace](https://github.com/huggingface/) menyediakan repositori untuk melatih banyak arsitektur ini dengan PyTorch dan TensorFlow.

## 🚀 Tantangan

## [Kuis Pasca-Pelajaran](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Tinjauan & Studi Mandiri

* [Blog post](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), yang menjelaskan makalah klasik [Attention is all you need](https://arxiv.org/abs/1706.03762) tentang transformer.
* [Seri blog post](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) tentang transformer, yang menjelaskan arsitektur secara rinci.

## [Tugas](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.