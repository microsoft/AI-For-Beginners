# Rangkaian Neural Recurrent

## [Kuis pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Dalam bagian sebelumnya, kita telah menggunakan representasi semantik yang kaya dari teks dan pengklasifikasi linier sederhana di atas embedding. Apa yang dilakukan arsitektur ini adalah menangkap makna agregat kata-kata dalam sebuah kalimat, tetapi tidak mempertimbangkan **urutan** kata, karena operasi agregasi di atas embedding menghilangkan informasi ini dari teks asli. Karena model-model ini tidak dapat memodelkan urutan kata, mereka tidak dapat menyelesaikan tugas yang lebih kompleks atau ambigu seperti generasi teks atau menjawab pertanyaan.

Untuk menangkap makna urutan teks, kita perlu menggunakan arsitektur jaringan saraf lain, yang disebut **rangkaian neural recurrent**, atau RNN. Dalam RNN, kita mengalirkan kalimat kita melalui jaringan satu simbol pada satu waktu, dan jaringan menghasilkan **status** tertentu, yang kemudian kita kirimkan kembali ke jaringan dengan simbol berikutnya.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.ms.png)

> Gambar oleh penulis

Mengingat urutan input token X<sub>0</sub>,...,X<sub>n</sub>, RNN menciptakan urutan blok jaringan saraf, dan melatih urutan ini dari awal hingga akhir menggunakan backpropagation. Setiap blok jaringan mengambil pasangan (X<sub>i</sub>,S<sub>i</sub>) sebagai input, dan menghasilkan S<sub>i+1</sub> sebagai hasil. Status akhir S<sub>n</sub> atau (output Y<sub>n</sub>) masuk ke pengklasifikasi linier untuk menghasilkan hasil. Semua blok jaringan berbagi bobot yang sama, dan dilatih dari awal hingga akhir menggunakan satu kali backpropagation.

Karena vektor status S<sub>0</sub>,...,S<sub>n</sub> dikirim melalui jaringan, ia dapat mempelajari ketergantungan berurutan antara kata-kata. Misalnya, ketika kata *not* muncul di suatu tempat dalam urutan, ia dapat belajar untuk menegasikan elemen tertentu dalam vektor status, yang menghasilkan negasi.

> ✅ Karena bobot semua blok RNN pada gambar di atas dibagikan, gambar yang sama dapat direpresentasikan sebagai satu blok (di sebelah kanan) dengan loop umpan balik berulang, yang mengirimkan status output jaringan kembali ke input.

## Anatomi Sel RNN

Mari kita lihat bagaimana sel RNN sederhana diorganisasi. Ia menerima status sebelumnya S<sub>i-1</sub> dan simbol saat ini X<sub>i</sub> sebagai input, dan harus menghasilkan status output S<sub>i</sub> (dan, terkadang, kita juga tertarik pada output lain Y<sub>i</sub>, seperti dalam kasus dengan jaringan generatif).

Sel RNN sederhana memiliki dua matriks bobot di dalamnya: satu mengubah simbol input (sebut saja W), dan satu lagi mengubah status input (H). Dalam hal ini, output jaringan dihitung sebagai σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), di mana σ adalah fungsi aktivasi dan b adalah bias tambahan.

<img alt="Anatomi Sel RNN" src="images/rnn-anatomy.png" width="50%"/>

> Gambar oleh penulis

Dalam banyak kasus, token input dikirim melalui lapisan embedding sebelum masuk ke RNN untuk mengurangi dimensi. Dalam hal ini, jika dimensi vektor input adalah *emb_size*, dan vektor status adalah *hid_size* - ukuran W adalah *emb_size*×*hid_size*, dan ukuran H adalah *hid_size*×*hid_size*.

## Memori Jangka Panjang Pendek (LSTM)

Salah satu masalah utama RNN klasik adalah masalah **gradien yang menghilang**. Karena RNN dilatih dari awal hingga akhir dalam satu kali backpropagation, ia mengalami kesulitan dalam menyebarkan kesalahan ke lapisan pertama jaringan, dan dengan demikian jaringan tidak dapat mempelajari hubungan antara token yang jauh. Salah satu cara untuk menghindari masalah ini adalah dengan memperkenalkan **manajemen status eksplisit** dengan menggunakan yang disebut **gerbang**. Ada dua arsitektur terkenal dari jenis ini: **Memori Jangka Panjang Pendek** (LSTM) dan **Unit Relay Tergerbang** (GRU).

![Gambar yang menunjukkan contoh sel memori jangka panjang pendek](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Sumber gambar TBD

Jaringan LSTM diorganisasi dengan cara yang mirip dengan RNN, tetapi ada dua status yang diteruskan dari lapisan ke lapisan: status aktual C, dan vektor tersembunyi H. Di setiap unit, vektor tersembunyi H<sub>i</sub> digabungkan dengan input X<sub>i</sub>, dan mereka mengontrol apa yang terjadi pada status C melalui **gerbang**. Setiap gerbang adalah jaringan saraf dengan aktivasi sigmoid (output dalam rentang [0,1]), yang dapat dianggap sebagai masker bitwise saat dikalikan dengan vektor status. Ada gerbang berikut (dari kiri ke kanan pada gambar di atas):

* **Gerbang lupa** mengambil vektor tersembunyi dan menentukan komponen mana dari vektor C yang perlu kita lupakan, dan mana yang harus diteruskan.
* **Gerbang input** mengambil beberapa informasi dari vektor input dan tersembunyi dan menyisipkannya ke dalam status.
* **Gerbang output** mengubah status melalui lapisan linier dengan aktivasi *tanh*, kemudian memilih beberapa komponen menggunakan vektor tersembunyi H<sub>i</sub> untuk menghasilkan status baru C<sub>i+1</sub>.

Komponen dari status C dapat dianggap sebagai beberapa bendera yang dapat diaktifkan dan dinonaktifkan. Misalnya, ketika kita menemui nama *Alice* dalam urutan, kita mungkin ingin menganggap bahwa itu merujuk pada karakter perempuan, dan mengangkat bendera dalam status bahwa kita memiliki kata benda perempuan dalam kalimat. Ketika kita lebih lanjut menemui frasa *dan Tom*, kita akan mengangkat bendera bahwa kita memiliki kata benda jamak. Dengan demikian, dengan memanipulasi status kita, kita dapat menjaga jejak sifat-sifat tata bahasa dari bagian kalimat.

> ✅ Sumber yang sangat baik untuk memahami bagian dalam LSTM adalah artikel hebat ini [Memahami Jaringan LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) oleh Christopher Olah.

## RNN Dua Arah dan Multilapis

Kita telah membahas jaringan berulang yang beroperasi dalam satu arah, dari awal urutan hingga akhir. Ini terlihat alami, karena menyerupai cara kita membaca dan mendengarkan ucapan. Namun, karena dalam banyak kasus praktis kita memiliki akses acak ke urutan input, mungkin masuk akal untuk menjalankan komputasi berulang dalam kedua arah. Jaringan semacam itu disebut **RNN dua arah**. Ketika berurusan dengan jaringan dua arah, kita memerlukan dua vektor status tersembunyi, satu untuk setiap arah.

Jaringan berulang, baik satu arah maupun dua arah, menangkap pola tertentu dalam urutan, dan dapat menyimpannya ke dalam vektor status atau meneruskannya ke output. Seperti pada jaringan konvolusional, kita dapat membangun lapisan berulang lain di atas yang pertama untuk menangkap pola tingkat tinggi dan membangun dari pola tingkat rendah yang diekstrak oleh lapisan pertama. Ini membawa kita pada gagasan **RNN multilapis** yang terdiri dari dua atau lebih jaringan berulang, di mana output dari lapisan sebelumnya diteruskan ke lapisan berikutnya sebagai input.

![Gambar yang menunjukkan RNN multilapis memori jangka pendek](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.ms.jpg)

*Gambar dari [pos yang luar biasa ini](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) oleh Fernando López*

## ✍️ Latihan: Embedding

Lanjutkan pembelajaran Anda di notebook berikut:

* [RNN dengan PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNN dengan TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Kesimpulan

Dalam unit ini, kita telah melihat bahwa RNN dapat digunakan untuk klasifikasi urutan, tetapi sebenarnya, mereka dapat menangani banyak tugas lainnya, seperti generasi teks, penerjemahan mesin, dan lainnya. Kita akan mempertimbangkan tugas-tugas tersebut di unit berikutnya.

## 🚀 Tantangan

Baca beberapa literatur tentang LSTM dan pertimbangkan aplikasinya:

- [Memori Jangka Pendek Jaringan Grid](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Tampilkan, Perhatikan dan Ceritakan: Generasi Keterangan Gambar Neural dengan Perhatian Visual](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Kuis pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Tinjauan & Studi Mandiri

- [Memahami Jaringan LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) oleh Christopher Olah.

## [Tugas: Notebook](assignment.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.