# Rangkaian Adversarial Generatif

Dalam bagian sebelumnya, kita telah mempelajari tentang **model generatif**: model yang dapat menghasilkan gambar baru yang mirip dengan yang ada di dataset pelatihan. VAE adalah contoh yang baik dari model generatif.

## [Kuis Pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Namun, jika kita mencoba untuk menghasilkan sesuatu yang benar-benar bermakna, seperti lukisan dengan resolusi yang wajar, dengan VAE, kita akan melihat bahwa pelatihan tidak konvergen dengan baik. Untuk kasus penggunaan ini, kita perlu mempelajari arsitektur lain yang ditargetkan secara khusus pada model generatif - **Rangkaian Adversarial Generatif**, atau GAN.

Ide utama dari GAN adalah memiliki dua jaringan saraf yang akan dilatih satu sama lain:

<img src="images/gan_architecture.png" width="70%"/>

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Kosakata sedikit:
> * **Generator** adalah jaringan yang mengambil beberapa vektor acak, dan menghasilkan gambar sebagai hasilnya.
> * **Discriminator** adalah jaringan yang mengambil gambar, dan seharusnya dapat memberitahu apakah itu adalah gambar nyata (dari dataset pelatihan), atau dihasilkan oleh generator. Ini pada dasarnya adalah pengklasifikasi gambar.

### Discriminator

Arsitektur discriminator tidak berbeda dari jaringan klasifikasi gambar biasa. Dalam kasus paling sederhana, itu bisa menjadi pengklasifikasi terhubung penuh, tetapi kemungkinan besar itu akan menjadi [jaringan konvolusional](../07-ConvNets/README.md).

> ✅ GAN yang berbasis pada jaringan konvolusional disebut [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Discriminator CNN terdiri dari lapisan-lapisan berikut: beberapa konvolusi+pooling (dengan ukuran spasial yang semakin berkurang) dan satu atau lebih lapisan terhubung penuh untuk mendapatkan "vektor fitur", pengklasifikasi biner akhir.

> ✅ 'Pooling' dalam konteks ini adalah teknik yang mengurangi ukuran gambar. "Lapisan pooling mengurangi dimensi data dengan menggabungkan keluaran kluster neuron pada satu lapisan menjadi satu neuron di lapisan berikutnya." - [sumber](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator sedikit lebih rumit. Anda dapat menganggapnya sebagai discriminator terbalik. Dimulai dari vektor laten (sebagai pengganti vektor fitur), ia memiliki lapisan terhubung penuh untuk mengubahnya menjadi ukuran/bentuk yang diperlukan, diikuti oleh dekonvolusi+peningkatan skala. Ini mirip dengan bagian *decoder* dari [autoencoder](../09-Autoencoders/README.md).

> ✅ Karena lapisan konvolusi diimplementasikan sebagai filter linier yang melintasi gambar, dekonvolusi pada dasarnya mirip dengan konvolusi, dan dapat diimplementasikan menggunakan logika lapisan yang sama.

<img src="images/gan_arch_detail.png" width="70%"/>

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

### Melatih GAN

GAN disebut **adversarial** karena ada kompetisi konstan antara generator dan discriminator. Selama kompetisi ini, baik generator maupun discriminator meningkat, sehingga jaringan belajar untuk menghasilkan gambar yang semakin baik.

Pelatihan dilakukan dalam dua tahap:

* **Melatih discriminator**. Tugas ini cukup sederhana: kita menghasilkan sekumpulan gambar oleh generator, memberi label 0, yang menunjukkan gambar palsu, dan mengambil sekumpulan gambar dari dataset input (dengan label 1, gambar nyata). Kita memperoleh *kerugian discriminator*, dan melakukan backprop.
* **Melatih generator**. Ini sedikit lebih rumit, karena kita tidak tahu output yang diharapkan untuk generator secara langsung. Kita mengambil seluruh jaringan GAN yang terdiri dari generator diikuti oleh discriminator, memberi umpan dengan beberapa vektor acak, dan mengharapkan hasilnya menjadi 1 (yang sesuai dengan gambar nyata). Kita kemudian membekukan parameter discriminator (kita tidak ingin ia dilatih pada langkah ini), dan melakukan backprop.

Selama proses ini, baik kerugian generator maupun discriminator tidak turun secara signifikan. Dalam situasi ideal, mereka harus berosilasi, sesuai dengan kedua jaringan yang meningkatkan kinerja mereka.

## ✍️ Latihan: GANs

* [Notebook GAN di TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook GAN di PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Masalah dengan pelatihan GAN

GAN dikenal sangat sulit untuk dilatih. Berikut beberapa masalah:

* **Mode Collapse**. Dengan istilah ini, kami maksudkan bahwa generator belajar untuk menghasilkan satu gambar sukses yang menipu discriminator, dan bukan variasi gambar yang berbeda.
* **Sensitivitas terhadap hiperparameter**. Sering kali Anda dapat melihat bahwa GAN tidak konvergen sama sekali, dan kemudian tiba-tiba menurun dalam laju pembelajaran yang mengarah ke konvergensi.
* Menjaga **keseimbangan** antara generator dan discriminator. Dalam banyak kasus, kerugian discriminator dapat turun ke nol relatif cepat, yang mengakibatkan generator tidak dapat dilatih lebih lanjut. Untuk mengatasi ini, kita dapat mencoba mengatur laju pembelajaran yang berbeda untuk generator dan discriminator, atau melewatkan pelatihan discriminator jika kerugian sudah terlalu rendah.
* Pelatihan untuk **resolusi tinggi**. Mencerminkan masalah yang sama seperti dengan autoencoder, masalah ini dipicu karena merekonstruksi terlalu banyak lapisan jaringan konvolusional mengarah pada artefak. Masalah ini biasanya diatasi dengan yang disebut **pertumbuhan progresif**, ketika pertama beberapa lapisan dilatih pada gambar resolusi rendah, dan kemudian lapisan "dibuka" atau ditambahkan. Solusi lain adalah menambahkan koneksi ekstra antara lapisan dan melatih beberapa resolusi sekaligus - lihat [makalah Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) untuk rincian.

## Transfer Gaya

GAN adalah cara yang hebat untuk menghasilkan gambar artistik. Teknik menarik lainnya adalah yang disebut **transfer gaya**, yang mengambil satu **gambar konten**, dan menggambarnya kembali dalam gaya yang berbeda, menerapkan filter dari **gambar gaya**.

Cara kerjanya adalah sebagai berikut:
* Kita mulai dengan gambar kebisingan acak (atau dengan gambar konten, tetapi demi pemahaman, lebih mudah untuk memulai dari kebisingan acak).
* Tujuan kita adalah untuk menciptakan gambar sedemikian rupa, sehingga dekat dengan gambar konten dan gambar gaya. Ini akan ditentukan oleh dua fungsi kerugian:
   - **Kerugian konten** dihitung berdasarkan fitur yang diekstrak oleh CNN di beberapa lapisan dari gambar saat ini dan gambar konten.
   - **Kerugian gaya** dihitung antara gambar saat ini dan gambar gaya dengan cara yang cerdas menggunakan matriks Gram (lebih banyak rincian dalam [notebook contoh](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Untuk membuat gambar lebih halus dan menghilangkan kebisingan, kita juga memperkenalkan **Kerugian Variasi**, yang menghitung jarak rata-rata antara piksel tetangga.
* Loop optimisasi utama menyesuaikan gambar saat ini menggunakan penurunan gradien (atau beberapa algoritma optimisasi lainnya) untuk meminimalkan total kerugian, yang merupakan jumlah tertimbang dari ketiga kerugian.

## ✍️ Contoh: [Transfer Gaya](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Kuis Pasca-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Kesimpulan

Dalam pelajaran ini, Anda belajar tentang GAN dan cara melatihnya. Anda juga belajar tentang tantangan khusus yang dapat dihadapi oleh jenis Jaringan Saraf ini, dan beberapa strategi tentang cara mengatasinya.

## 🚀 Tantangan

Jalankan [notebook Transfer Gaya](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) menggunakan gambar Anda sendiri.

## Tinjauan & Studi Mandiri

Sebagai referensi, baca lebih lanjut tentang GAN di sumber-sumber ini:

* Marco Pasini, [10 Pelajaran yang Saya Pelajari Melatih GAN selama Satu Tahun](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), arsitektur GAN *de facto* yang perlu dipertimbangkan
* [Membuat Seni Generatif menggunakan GAN di Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tugas

Kunjungi kembali salah satu dari dua notebook yang terkait dengan pelajaran ini dan latih ulang GAN pada gambar Anda sendiri. Apa yang dapat Anda ciptakan?

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.