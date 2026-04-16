# Jaringan Saraf Rekurens

## [Kuis Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/31)

Pada bagian sebelumnya, kita telah menggunakan representasi semantik yang kaya dari teks dan pengklasifikasi linier sederhana di atas embedding. Arsitektur ini menangkap makna agregat dari kata-kata dalam sebuah kalimat, tetapi tidak memperhatikan **urutan** kata, karena operasi agregasi pada embedding menghilangkan informasi ini dari teks asli. Karena model ini tidak mampu memodelkan urutan kata, mereka tidak dapat menyelesaikan tugas yang lebih kompleks atau ambigu seperti generasi teks atau menjawab pertanyaan.

Untuk menangkap makna dari urutan teks, kita perlu menggunakan arsitektur jaringan saraf lain yang disebut **jaringan saraf rekurens**, atau RNN. Dalam RNN, kita melewatkan kalimat kita melalui jaringan satu simbol pada satu waktu, dan jaringan menghasilkan beberapa **state**, yang kemudian kita lewati kembali ke jaringan bersama simbol berikutnya.

![RNN](../../../../../translated_images/id/rnn.27f5c29c53d727b5.webp)

> Gambar oleh penulis

Diberikan urutan input token X<sub>0</sub>,...,X<sub>n</sub>, RNN menciptakan urutan blok jaringan saraf, dan melatih urutan ini secara end-to-end menggunakan backpropagation. Setiap blok jaringan menerima pasangan (X<sub>i</sub>,S<sub>i</sub>) sebagai input, dan menghasilkan S<sub>i+1</sub> sebagai hasil. State akhir S<sub>n</sub> atau (output Y<sub>n</sub>) masuk ke pengklasifikasi linier untuk menghasilkan hasil. Semua blok jaringan berbagi bobot yang sama, dan dilatih secara end-to-end menggunakan satu pass backpropagation.

Karena vektor state S<sub>0</sub>,...,S<sub>n</sub> dilewatkan melalui jaringan, jaringan mampu mempelajari ketergantungan berurutan antar kata. Sebagai contoh, ketika kata *tidak* muncul di suatu tempat dalam urutan, jaringan dapat belajar untuk meniadakan elemen tertentu dalam vektor state, menghasilkan negasi.

> ✅ Karena bobot semua blok RNN pada gambar di atas adalah sama, gambar yang sama dapat direpresentasikan sebagai satu blok (di sebelah kanan) dengan loop umpan balik rekurens, yang melewatkan state output jaringan kembali ke input.

## Anatomi Sel RNN

Mari kita lihat bagaimana sebuah sel RNN sederhana diorganisasi. Sel ini menerima state sebelumnya S<sub>i-1</sub> dan simbol saat ini X<sub>i</sub> sebagai input, dan harus menghasilkan state output S<sub>i</sub> (dan, kadang-kadang, kita juga tertarik pada output lain Y<sub>i</sub>, seperti dalam kasus jaringan generatif).

Sebuah sel RNN sederhana memiliki dua matriks bobot di dalamnya: satu untuk mentransformasi simbol input (kita sebut W), dan satu lagi untuk mentransformasi state input (H). Dalam kasus ini, output jaringan dihitung sebagai &sigma;(W&times;X<sub>i</sub>+H&times;S<sub>i-1</sub>+b), di mana &sigma; adalah fungsi aktivasi dan b adalah bias tambahan.

<img alt="Anatomi Sel RNN" src="../../../../../translated_images/id/rnn-anatomy.79ee3f3920b3294b.webp" width="50%"/>

> Gambar oleh penulis

Dalam banyak kasus, token input dilewatkan melalui lapisan embedding sebelum masuk ke RNN untuk menurunkan dimensi. Dalam kasus ini, jika dimensi vektor input adalah *emb_size*, dan vektor state adalah *hid_size* - ukuran W adalah *emb_size*&times;*hid_size*, dan ukuran H adalah *hid_size*&times;*hid_size*.

## Long Short Term Memory (LSTM)

Salah satu masalah utama dari RNN klasik adalah masalah **vanishing gradients**. Karena RNN dilatih secara end-to-end dalam satu pass backpropagation, jaringan mengalami kesulitan dalam mempropagasi error ke lapisan pertama jaringan, sehingga jaringan tidak dapat mempelajari hubungan antara token yang jauh. Salah satu cara untuk menghindari masalah ini adalah dengan memperkenalkan **manajemen state eksplisit** menggunakan **gates**. Ada dua arsitektur terkenal dari jenis ini: **Long Short Term Memory** (LSTM) dan **Gated Relay Unit** (GRU).

![Gambar menunjukkan contoh sel long short term memory](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Sumber gambar TBD

Jaringan LSTM diorganisasi dengan cara yang mirip dengan RNN, tetapi ada dua state yang dilewatkan dari lapisan ke lapisan: state aktual C, dan vektor tersembunyi H. Pada setiap unit, vektor tersembunyi H<sub>i</sub> digabungkan dengan input X<sub>i</sub>, dan mereka mengontrol apa yang terjadi pada state C melalui **gates**. Setiap gate adalah jaringan saraf dengan aktivasi sigmoid (output dalam rentang [0,1]), yang dapat dianggap sebagai masker bitwise ketika dikalikan dengan vektor state. Ada gate berikut ini (dari kiri ke kanan pada gambar di atas):

* **Forget gate** mengambil vektor tersembunyi dan menentukan komponen mana dari vektor C yang perlu dilupakan, dan mana yang perlu dilewatkan.
* **Input gate** mengambil beberapa informasi dari input dan vektor tersembunyi dan memasukkannya ke dalam state.
* **Output gate** mentransformasi state melalui lapisan linier dengan aktivasi *tanh*, lalu memilih beberapa komponennya menggunakan vektor tersembunyi H<sub>i</sub> untuk menghasilkan state baru C<sub>i+1</sub>.

Komponen dari state C dapat dianggap sebagai beberapa flag yang dapat dihidupkan dan dimatikan. Sebagai contoh, ketika kita menemukan nama *Alice* dalam urutan, kita mungkin ingin mengasumsikan bahwa itu merujuk pada karakter perempuan, dan mengaktifkan flag dalam state bahwa kita memiliki kata benda perempuan dalam kalimat. Ketika kita kemudian menemukan frasa *dan Tom*, kita akan mengaktifkan flag bahwa kita memiliki kata benda jamak. Dengan memanipulasi state, kita dapat melacak properti gramatikal dari bagian-bagian kalimat.

> ✅ Sumber yang sangat baik untuk memahami internal LSTM adalah artikel hebat ini [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) oleh Christopher Olah.

## RNN Bidirectional dan Multilayer

Kita telah membahas jaringan rekurens yang beroperasi dalam satu arah, dari awal urutan hingga akhir. Ini terlihat alami, karena menyerupai cara kita membaca dan mendengarkan ucapan. Namun, karena dalam banyak kasus praktis kita memiliki akses acak ke urutan input, mungkin masuk akal untuk menjalankan komputasi rekurens dalam kedua arah. Jaringan semacam itu disebut **RNN bidirectional**. Saat berurusan dengan jaringan bidirectional, kita membutuhkan dua vektor state tersembunyi, satu untuk setiap arah.

Jaringan rekurens, baik satu arah maupun bidirectional, menangkap pola tertentu dalam urutan, dan dapat menyimpannya ke dalam vektor state atau melewatkannya ke output. Seperti pada jaringan konvolusi, kita dapat membangun lapisan rekurens lain di atas yang pertama untuk menangkap pola tingkat tinggi dan membangun dari pola tingkat rendah yang diekstraksi oleh lapisan pertama. Ini membawa kita pada konsep **RNN multilayer** yang terdiri dari dua atau lebih jaringan rekurens, di mana output dari lapisan sebelumnya dilewatkan ke lapisan berikutnya sebagai input.

![Gambar menunjukkan RNN LSTM multilayer](../../../../../translated_images/id/multi-layer-lstm.dd975e29bb2a59fe.webp)

*Gambar dari [postingan luar biasa ini](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) oleh Fernando López*

## ✍️ Latihan: Embedding

Lanjutkan pembelajaran Anda dalam notebook berikut:

* [RNNs dengan PyTorch](RNNPyTorch.ipynb)
* [RNNs dengan TensorFlow](RNNTF.ipynb)

## Kesimpulan

Dalam unit ini, kita telah melihat bahwa RNN dapat digunakan untuk klasifikasi urutan, tetapi sebenarnya, mereka dapat menangani banyak tugas lainnya, seperti generasi teks, terjemahan mesin, dan lainnya. Kita akan membahas tugas-tugas tersebut di unit berikutnya.

## 🚀 Tantangan

Baca beberapa literatur tentang LSTM dan pertimbangkan aplikasinya:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Kuis Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Tinjauan & Studi Mandiri

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) oleh Christopher Olah.

## [Tugas: Notebook](assignment.md)

---

