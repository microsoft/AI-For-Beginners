<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-29T11:51:41+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "ms"
}
-->
# Rangkaian Adversarial Generatif

Dalam bahagian sebelumnya, kita telah belajar tentang **model generatif**: model yang boleh menghasilkan imej baru yang serupa dengan imej dalam dataset latihan. VAE adalah contoh yang baik bagi model generatif.

## [Kuiz pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Namun, jika kita cuba menghasilkan sesuatu yang benar-benar bermakna, seperti lukisan dengan resolusi yang munasabah, menggunakan VAE, kita akan melihat bahawa latihan tidak berkumpul dengan baik. Untuk kes penggunaan ini, kita perlu belajar tentang satu lagi seni bina yang khusus untuk model generatif - **Rangkaian Adversarial Generatif**, atau GAN.

Idea utama GAN adalah mempunyai dua rangkaian neural yang akan dilatih melawan satu sama lain:

<img src="images/gan_architecture.png" width="70%"/>

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Sedikit perbendaharaan kata:
> * **Generator** adalah rangkaian yang mengambil beberapa vektor rawak, dan menghasilkan imej sebagai hasilnya
> * **Discriminator** adalah rangkaian yang mengambil imej, dan ia harus menentukan sama ada ia adalah imej sebenar (daripada dataset latihan), atau ia dihasilkan oleh generator. Ia pada dasarnya adalah pengklasifikasi imej.

### Discriminator

Seni bina discriminator tidak berbeza daripada rangkaian pengklasifikasi imej biasa. Dalam kes paling mudah, ia boleh menjadi pengklasifikasi sepenuhnya bersambung, tetapi kemungkinan besar ia akan menjadi [rangkaian konvolusi](../07-ConvNets/README.md).

> ✅ GAN berdasarkan rangkaian konvolusi dipanggil [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Discriminator CNN terdiri daripada lapisan berikut: beberapa konvolusi+pooling (dengan saiz spatial yang semakin berkurang) dan satu atau lebih lapisan sepenuhnya bersambung untuk mendapatkan "vektor ciri", pengklasifikasi binari akhir.

> ✅ 'Pooling' dalam konteks ini adalah teknik yang mengurangkan saiz imej. "Lapisan pooling mengurangkan dimensi data dengan menggabungkan output kluster neuron pada satu lapisan ke dalam satu neuron pada lapisan seterusnya." - [sumber](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator sedikit lebih rumit. Anda boleh menganggapnya sebagai discriminator yang terbalik. Bermula dari vektor laten (menggantikan vektor ciri), ia mempunyai lapisan sepenuhnya bersambung untuk menukarnya kepada saiz/bentuk yang diperlukan, diikuti oleh dekonvolusi+peningkatan. Ini serupa dengan bahagian *decoder* dalam [autoencoder](../09-Autoencoders/README.md).

> ✅ Oleh kerana lapisan konvolusi dilaksanakan sebagai penapis linear yang melintasi imej, dekonvolusi pada dasarnya serupa dengan konvolusi, dan boleh dilaksanakan menggunakan logik lapisan yang sama.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

### Melatih GAN

GAN dipanggil **adversarial** kerana terdapat persaingan berterusan antara generator dan discriminator. Semasa persaingan ini, kedua-dua generator dan discriminator bertambah baik, dengan itu rangkaian belajar menghasilkan imej yang semakin baik.

Latihan berlaku dalam dua peringkat:

* **Melatih discriminator**. Tugas ini agak mudah: kita menghasilkan satu batch imej oleh generator, melabelkannya 0, yang bermaksud imej palsu, dan mengambil satu batch imej daripada dataset input (dengan label 1, imej sebenar). Kita memperoleh beberapa *discriminator loss*, dan melakukan backprop.
* **Melatih generator**. Ini sedikit lebih rumit, kerana kita tidak tahu output yang dijangkakan untuk generator secara langsung. Kita mengambil keseluruhan rangkaian GAN yang terdiri daripada generator diikuti oleh discriminator, memberinya beberapa vektor rawak, dan mengharapkan hasilnya menjadi 1 (bersesuaian dengan imej sebenar). Kita kemudian membekukan parameter discriminator (kita tidak mahu ia dilatih pada langkah ini), dan melakukan backprop.

Semasa proses ini, kedua-dua generator dan discriminator loss tidak turun dengan ketara. Dalam situasi ideal, mereka sepatutnya berayun, menunjukkan kedua-dua rangkaian meningkatkan prestasi mereka.

## ✍️ Latihan: GANs

* [Notebook GAN dalam TensorFlow/Keras](GANTF.ipynb)
* [Notebook GAN dalam PyTorch](GANPyTorch.ipynb)

### Masalah dengan Latihan GAN

GAN diketahui sangat sukar untuk dilatih. Berikut adalah beberapa masalah:

* **Mode Collapse**. Istilah ini merujuk kepada generator yang belajar menghasilkan satu imej berjaya yang menipu discriminator, dan bukannya pelbagai imej yang berbeza.
* **Sensitiviti kepada hiperparameter**. Selalunya anda boleh melihat bahawa GAN tidak berkumpul sama sekali, dan kemudian tiba-tiba penurunan kadar pembelajaran membawa kepada pengumpulan.
* Menjaga **keseimbangan** antara generator dan discriminator. Dalam banyak kes, discriminator loss boleh turun ke sifar dengan cepat, yang menyebabkan generator tidak dapat dilatih lebih lanjut. Untuk mengatasi ini, kita boleh cuba menetapkan kadar pembelajaran yang berbeza untuk generator dan discriminator, atau melangkau latihan discriminator jika loss sudah terlalu rendah.
* Latihan untuk **resolusi tinggi**. Masalah ini mencerminkan masalah yang sama seperti dengan autoencoder, yang dicetuskan kerana pembinaan semula terlalu banyak lapisan rangkaian konvolusi membawa kepada artifak. Masalah ini biasanya diselesaikan dengan **pertumbuhan progresif**, di mana beberapa lapisan pertama dilatih pada imej resolusi rendah, dan kemudian lapisan "dibuka" atau ditambah. Penyelesaian lain adalah menambah sambungan tambahan antara lapisan dan melatih beberapa resolusi sekaligus - lihat kertas [Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) untuk butiran.

## Pemindahan Gaya

GAN adalah cara yang hebat untuk menghasilkan imej artistik. Teknik menarik lain adalah **pemindahan gaya**, yang mengambil satu **imej kandungan**, dan melukis semula dalam gaya yang berbeza, menggunakan penapis daripada **imej gaya**.

Cara ia berfungsi adalah seperti berikut:
* Kita bermula dengan imej bunyi rawak (atau dengan imej kandungan, tetapi untuk pemahaman lebih mudah, kita bermula dengan bunyi rawak)
* Matlamat kita adalah untuk mencipta imej yang dekat dengan kedua-dua imej kandungan dan imej gaya. Ini ditentukan oleh dua fungsi loss:
   - **Content loss** dikira berdasarkan ciri yang diekstrak oleh CNN pada beberapa lapisan daripada imej semasa dan imej kandungan
   - **Style loss** dikira antara imej semasa dan imej gaya dengan cara yang bijak menggunakan matriks Gram (butiran lanjut dalam [notebook contoh](StyleTransfer.ipynb))
* Untuk menjadikan imej lebih licin dan menghilangkan bunyi, kita juga memperkenalkan **Variation loss**, yang mengira jarak purata antara piksel yang berdekatan
* Gelung pengoptimuman utama menyesuaikan imej semasa menggunakan penurunan kecerunan (atau beberapa algoritma pengoptimuman lain) untuk meminimumkan jumlah loss, yang merupakan jumlah berwajaran semua tiga loss.

## ✍️ Contoh: [Pemindahan Gaya](StyleTransfer.ipynb)

## [Kuiz pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Kesimpulan

Dalam pelajaran ini, anda telah belajar tentang GAN dan cara melatihnya. Anda juga telah belajar tentang cabaran khas yang dihadapi oleh jenis Rangkaian Neural ini, dan beberapa strategi untuk mengatasinya.

## 🚀 Cabaran

Jalankan notebook [Pemindahan Gaya](StyleTransfer.ipynb) menggunakan imej anda sendiri.

## Kajian & Pembelajaran Kendiri

Sebagai rujukan, baca lebih lanjut tentang GAN dalam sumber berikut:

* Marco Pasini, [10 Pengajaran yang Saya Pelajari Melatih GAN selama Satu Tahun](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), seni bina GAN *de facto* untuk dipertimbangkan
* [Mencipta Seni Generatif menggunakan GAN di Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tugasan

Kaji semula salah satu daripada dua notebook yang berkaitan dengan pelajaran ini dan latih semula GAN menggunakan imej anda sendiri. Apa yang boleh anda cipta?

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.