<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-29T12:27:53+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "id"
}
-->
# Generative Adversarial Networks

Di bagian sebelumnya, kita telah mempelajari tentang **model generatif**: model yang dapat menghasilkan gambar baru yang mirip dengan yang ada di dataset pelatihan. VAE adalah contoh yang baik dari model generatif.

## [Kuis sebelum pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Namun, jika kita mencoba menghasilkan sesuatu yang benar-benar bermakna, seperti lukisan dengan resolusi yang wajar, menggunakan VAE, kita akan melihat bahwa pelatihannya tidak berjalan dengan baik. Untuk kasus ini, kita perlu mempelajari arsitektur lain yang secara khusus ditujukan untuk model generatif - **Generative Adversarial Networks**, atau GANs.

Ide utama dari GAN adalah memiliki dua jaringan neural yang dilatih saling berlawanan:

<img src="images/gan_architecture.png" width="70%"/>

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Sedikit kosakata:
> * **Generator** adalah jaringan yang mengambil vektor acak dan menghasilkan gambar sebagai hasilnya.
> * **Discriminator** adalah jaringan yang mengambil gambar dan menentukan apakah itu gambar asli (dari dataset pelatihan) atau gambar yang dihasilkan oleh generator. Ini pada dasarnya adalah pengklasifikasi gambar.

### Discriminator

Arsitektur discriminator tidak berbeda dari jaringan klasifikasi gambar biasa. Dalam kasus paling sederhana, ini bisa berupa pengklasifikasi fully-connected, tetapi kemungkinan besar akan berupa [jaringan konvolusi](../07-ConvNets/README.md).

> ✅ GAN yang berbasis jaringan konvolusi disebut [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Discriminator CNN terdiri dari lapisan-lapisan berikut: beberapa konvolusi+pooling (dengan ukuran spasial yang semakin kecil) dan satu atau lebih lapisan fully-connected untuk mendapatkan "vektor fitur", serta pengklasifikasi biner akhir.

> ✅ 'Pooling' dalam konteks ini adalah teknik yang mengurangi ukuran gambar. "Pooling layers mengurangi dimensi data dengan menggabungkan output dari kluster neuron pada satu lapisan menjadi satu neuron di lapisan berikutnya." - [sumber](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator sedikit lebih rumit. Anda dapat menganggapnya sebagai discriminator yang dibalik. Dimulai dari vektor laten (sebagai pengganti vektor fitur), generator memiliki lapisan fully-connected untuk mengubahnya menjadi ukuran/bentuk yang diperlukan, diikuti oleh dekonvolusi+upscaling. Ini mirip dengan bagian *decoder* dari [autoencoder](../09-Autoencoders/README.md).

> ✅ Karena lapisan konvolusi diimplementasikan sebagai filter linier yang melintasi gambar, dekonvolusi pada dasarnya mirip dengan konvolusi dan dapat diimplementasikan menggunakan logika lapisan yang sama.

<img src="images/gan_arch_detail.png" width="70%"/>

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

### Melatih GAN

GAN disebut **adversarial** karena ada persaingan terus-menerus antara generator dan discriminator. Selama persaingan ini, baik generator maupun discriminator meningkat, sehingga jaringan belajar menghasilkan gambar yang semakin baik.

Pelatihan dilakukan dalam dua tahap:

* **Melatih discriminator**. Tugas ini cukup sederhana: kita menghasilkan sekumpulan gambar menggunakan generator, memberi label 0 (yang berarti gambar palsu), dan mengambil sekumpulan gambar dari dataset input (dengan label 1, gambar asli). Kita mendapatkan *discriminator loss*, dan melakukan backprop.
* **Melatih generator**. Ini sedikit lebih rumit, karena kita tidak tahu output yang diharapkan untuk generator secara langsung. Kita mengambil seluruh jaringan GAN yang terdiri dari generator diikuti oleh discriminator, memberinya beberapa vektor acak, dan mengharapkan hasilnya adalah 1 (sesuai dengan gambar asli). Kemudian kita membekukan parameter discriminator (kita tidak ingin melatihnya pada langkah ini), dan melakukan backprop.

Selama proses ini, baik generator maupun discriminator loss tidak akan turun secara signifikan. Dalam situasi ideal, mereka seharusnya berosilasi, yang menunjukkan bahwa kedua jaringan meningkatkan kinerjanya.

## ✍️ Latihan: GANs

* [Notebook GAN di TensorFlow/Keras](GANTF.ipynb)
* [Notebook GAN di PyTorch](GANPyTorch.ipynb)

### Masalah dalam Melatih GAN

GAN dikenal sangat sulit untuk dilatih. Berikut beberapa masalahnya:

* **Mode Collapse**. Istilah ini berarti generator belajar menghasilkan satu gambar sukses yang dapat menipu discriminator, tetapi tidak menghasilkan berbagai gambar yang berbeda.
* **Sensitivitas terhadap hyperparameter**. Sering kali Anda akan melihat bahwa GAN tidak konvergen sama sekali, lalu tiba-tiba konvergen setelah penurunan learning rate.
* Menjaga **keseimbangan** antara generator dan discriminator. Dalam banyak kasus, discriminator loss dapat turun ke nol dengan cepat, yang menyebabkan generator tidak dapat dilatih lebih lanjut. Untuk mengatasi ini, kita dapat mencoba menetapkan learning rate yang berbeda untuk generator dan discriminator, atau melewatkan pelatihan discriminator jika loss-nya sudah terlalu rendah.
* Pelatihan untuk **resolusi tinggi**. Masalah ini mirip dengan autoencoder, di mana merekonstruksi terlalu banyak lapisan jaringan konvolusi menyebabkan artefak. Masalah ini biasanya diselesaikan dengan **progressive growing**, di mana beberapa lapisan pertama dilatih pada gambar resolusi rendah, lalu lapisan-lapisan "dibuka" atau ditambahkan. Solusi lain adalah menambahkan koneksi tambahan antar lapisan dan melatih beberapa resolusi sekaligus - lihat [Multi-Scale Gradient GANs paper](https://arxiv.org/abs/1903.06048) untuk detailnya.

## Style Transfer

GAN adalah cara yang hebat untuk menghasilkan gambar artistik. Teknik menarik lainnya adalah **style transfer**, yang mengambil satu **gambar konten** dan menggambarnya ulang dalam gaya yang berbeda, menerapkan filter dari **gambar gaya**.

Cara kerjanya adalah sebagai berikut:
* Kita mulai dengan gambar noise acak (atau dengan gambar konten, tetapi untuk pemahaman lebih mudah dimulai dari noise acak).
* Tujuan kita adalah membuat gambar yang mendekati gambar konten dan gambar gaya. Ini ditentukan oleh dua fungsi loss:
   - **Content loss** dihitung berdasarkan fitur yang diekstrak oleh CNN pada beberapa lapisan dari gambar saat ini dan gambar konten.
   - **Style loss** dihitung antara gambar saat ini dan gambar gaya dengan cara cerdas menggunakan matriks Gram (lebih detail di [notebook contoh](StyleTransfer.ipynb)).
* Untuk membuat gambar lebih halus dan menghilangkan noise, kita juga memperkenalkan **Variation loss**, yang menghitung jarak rata-rata antara piksel yang berdekatan.
* Loop optimasi utama menyesuaikan gambar saat ini menggunakan gradient descent (atau algoritma optimasi lainnya) untuk meminimalkan total loss, yang merupakan jumlah berbobot dari ketiga loss tersebut.

## ✍️ Contoh: [Style Transfer](StyleTransfer.ipynb)

## [Kuis setelah pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Kesimpulan

Dalam pelajaran ini, Anda telah mempelajari tentang GAN dan cara melatihnya. Anda juga mempelajari tantangan khusus yang dihadapi jenis Jaringan Neural ini, serta beberapa strategi untuk mengatasinya.

## 🚀 Tantangan

Jalankan [notebook Style Transfer](StyleTransfer.ipynb) menggunakan gambar Anda sendiri.

## Tinjauan & Studi Mandiri

Sebagai referensi, baca lebih lanjut tentang GAN di sumber-sumber berikut:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), arsitektur GAN *de facto* yang patut dipertimbangkan
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tugas

Kunjungi kembali salah satu dari dua notebook yang terkait dengan pelajaran ini dan latih ulang GAN menggunakan gambar Anda sendiri. Apa yang bisa Anda ciptakan?

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.