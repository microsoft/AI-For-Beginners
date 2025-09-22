<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-29T12:44:45+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "ms"
}
-->
# Mekanisme Perhatian dan Transformer

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/35)

Salah satu masalah paling penting dalam bidang NLP ialah **terjemahan mesin**, tugas penting yang menjadi asas kepada alat seperti Google Translate. Dalam bahagian ini, kita akan memberi tumpuan kepada terjemahan mesin, atau secara lebih umum, kepada sebarang tugas *sequence-to-sequence* (yang juga dipanggil **transduksi ayat**).

Dengan RNN, sequence-to-sequence dilaksanakan oleh dua rangkaian berulang, di mana satu rangkaian, iaitu **encoder**, memampatkan urutan input ke dalam keadaan tersembunyi, manakala rangkaian lain, iaitu **decoder**, mengembangkan keadaan tersembunyi ini kepada hasil terjemahan. Terdapat beberapa masalah dengan pendekatan ini:

* Keadaan akhir rangkaian encoder sukar untuk mengingati permulaan ayat, menyebabkan kualiti model yang rendah untuk ayat yang panjang.
* Semua perkataan dalam satu urutan mempunyai kesan yang sama terhadap hasil. Walau bagaimanapun, dalam realiti, perkataan tertentu dalam urutan input sering mempunyai kesan yang lebih besar terhadap output berurutan berbanding yang lain.

**Mekanisme Perhatian** menyediakan cara untuk memberi berat kepada kesan kontekstual setiap vektor input pada setiap ramalan output RNN. Cara ia dilaksanakan adalah dengan mencipta jalan pintas antara keadaan perantaraan RNN input dan RNN output. Dengan cara ini, apabila menghasilkan simbol output y<sub>t</sub>, kita akan mengambil kira semua keadaan tersembunyi input h<sub>i</sub>, dengan pekali berat yang berbeza α<sub>t,i</sub>.

![Imej menunjukkan model encoder/decoder dengan lapisan perhatian tambahan](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.ms.png)

> Model encoder-decoder dengan mekanisme perhatian tambahan dalam [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), dipetik daripada [blog post ini](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Matriks perhatian {α<sub>i,j</sub>} akan mewakili tahap di mana perkataan input tertentu memainkan peranan dalam penjanaan perkataan tertentu dalam urutan output. Berikut adalah contoh matriks seperti itu:

![Imej menunjukkan penjajaran sampel yang ditemui oleh RNNsearch-50, diambil daripada Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.ms.png)

> Rajah daripada [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Rajah 3)

Mekanisme perhatian bertanggungjawab untuk sebahagian besar kemajuan terkini atau hampir terkini dalam NLP. Walau bagaimanapun, menambah perhatian secara signifikan meningkatkan bilangan parameter model yang membawa kepada isu penskalaan dengan RNN. Satu kekangan utama penskalaan RNN ialah sifat berulang model yang menjadikannya mencabar untuk melatih secara batch dan selari. Dalam RNN, setiap elemen urutan perlu diproses secara berurutan, yang bermaksud ia tidak boleh dengan mudah diparalelkan.

![Encoder Decoder dengan Perhatian](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Rajah daripada [Blog Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Penggunaan mekanisme perhatian bersama kekangan ini membawa kepada penciptaan Model Transformer yang kini menjadi standard seperti BERT hingga Open-GPT3.

## Model Transformer

Salah satu idea utama di sebalik transformer ialah untuk mengelakkan sifat berurutan RNN dan mencipta model yang boleh diparalelkan semasa latihan. Ini dicapai dengan melaksanakan dua idea:

* pengekodan kedudukan
* menggunakan mekanisme perhatian kendiri untuk menangkap corak dan bukannya RNN (atau CNN) (itulah sebabnya kertas yang memperkenalkan transformer dipanggil *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Pengekodan/Pemadanan Kedudukan

Idea pengekodan kedudukan adalah seperti berikut. 
1. Apabila menggunakan RNN, kedudukan relatif token diwakili oleh bilangan langkah, dan oleh itu tidak perlu diwakili secara eksplisit. 
2. Walau bagaimanapun, apabila kita beralih kepada perhatian, kita perlu mengetahui kedudukan relatif token dalam urutan. 
3. Untuk mendapatkan pengekodan kedudukan, kita menambah urutan token kita dengan urutan kedudukan token dalam urutan (iaitu, urutan nombor 0,1, ...).
4. Kita kemudian mencampurkan kedudukan token dengan vektor pemadanan token. Untuk mengubah kedudukan (integer) menjadi vektor, kita boleh menggunakan pendekatan yang berbeza:

* Pemadanan yang boleh dilatih, serupa dengan pemadanan token. Ini adalah pendekatan yang kita pertimbangkan di sini. Kita menggunakan lapisan pemadanan di atas kedua-dua token dan kedudukan mereka, menghasilkan vektor pemadanan dengan dimensi yang sama, yang kemudian kita tambahkan bersama.
* Fungsi pengekodan kedudukan tetap, seperti yang dicadangkan dalam kertas asal.

<img src="images/pos-embedding.png" width="50%"/>

> Imej oleh penulis

Hasil yang kita peroleh dengan pemadanan kedudukan menggabungkan kedua-dua token asal dan kedudukannya dalam urutan.

### Perhatian Kendiri Multi-Kepala

Seterusnya, kita perlu menangkap beberapa corak dalam urutan kita. Untuk melakukan ini, transformer menggunakan mekanisme **perhatian kendiri**, yang pada asasnya adalah perhatian yang diterapkan pada urutan yang sama sebagai input dan output. Menerapkan perhatian kendiri membolehkan kita mengambil kira **konteks** dalam ayat, dan melihat perkataan mana yang saling berkaitan. Sebagai contoh, ia membolehkan kita melihat perkataan mana yang dirujuk oleh koreferensi, seperti *ia*, dan juga mengambil kira konteks:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.ms.png)

> Imej daripada [Blog Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Dalam transformer, kita menggunakan **Perhatian Multi-Kepala** untuk memberikan kuasa kepada rangkaian untuk menangkap beberapa jenis kebergantungan yang berbeza, contohnya hubungan perkataan jangka panjang vs. jangka pendek, koreferensi vs. sesuatu yang lain, dsb.

[Notebook TensorFlow](TransformersTF.ipynb) mengandungi lebih banyak perincian tentang pelaksanaan lapisan transformer.

### Perhatian Encoder-Decoder

Dalam transformer, perhatian digunakan di dua tempat:

* Untuk menangkap corak dalam teks input menggunakan perhatian kendiri
* Untuk melaksanakan terjemahan urutan - iaitu lapisan perhatian antara encoder dan decoder.

Perhatian encoder-decoder sangat mirip dengan mekanisme perhatian yang digunakan dalam RNN, seperti yang diterangkan pada permulaan bahagian ini. Diagram animasi ini menerangkan peranan perhatian encoder-decoder.

![GIF Animasi menunjukkan bagaimana evaluasi dilakukan dalam model transformer.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Oleh kerana setiap kedudukan input dipetakan secara bebas kepada setiap kedudukan output, transformer boleh diparalelkan dengan lebih baik daripada RNN, yang membolehkan model bahasa yang lebih besar dan lebih ekspresif. Setiap kepala perhatian boleh digunakan untuk mempelajari hubungan yang berbeza antara perkataan yang meningkatkan tugas Pemprosesan Bahasa Semula Jadi.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) ialah rangkaian transformer berbilang lapisan yang sangat besar dengan 12 lapisan untuk *BERT-base*, dan 24 untuk *BERT-large*. Model ini mula-mula dilatih awal pada korpus teks yang besar (WikiPedia + buku) menggunakan latihan tanpa pengawasan (meramalkan perkataan yang disembunyikan dalam ayat). Semasa latihan awal, model menyerap tahap pemahaman bahasa yang signifikan yang kemudiannya boleh dimanfaatkan dengan set data lain menggunakan penalaan halus. Proses ini dipanggil **pembelajaran pemindahan**.

![gambar daripada http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.ms.png)

> Sumber imej [di sini](http://jalammar.github.io/illustrated-bert/)

## ✍️ Latihan: Transformer

Teruskan pembelajaran anda dalam notebook berikut:

* [Transformer dalam PyTorch](TransformersPyTorch.ipynb)
* [Transformer dalam TensorFlow](TransformersTF.ipynb)

## Kesimpulan

Dalam pelajaran ini, anda telah mempelajari tentang Transformer dan Mekanisme Perhatian, semua alat penting dalam kotak alat NLP. Terdapat banyak variasi seni bina Transformer termasuk BERT, DistilBERT, BigBird, OpenGPT3 dan banyak lagi yang boleh disesuaikan. Pakej [HuggingFace](https://github.com/huggingface/) menyediakan repositori untuk melatih banyak seni bina ini dengan PyTorch dan TensorFlow.

## 🚀 Cabaran

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/36)

## Kajian & Pembelajaran Kendiri

* [Blog post](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), yang menerangkan kertas klasik [Attention is all you need](https://arxiv.org/abs/1706.03762) tentang transformer.
* [Siri blog post](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) tentang transformer, yang menerangkan seni bina secara terperinci.

## [Tugasan](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.