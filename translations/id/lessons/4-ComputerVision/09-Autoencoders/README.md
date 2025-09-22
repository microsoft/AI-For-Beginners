<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-29T12:26:03+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "id"
}
-->
# Autoencoders

Saat melatih CNN, salah satu masalahnya adalah kita membutuhkan banyak data yang diberi label. Dalam kasus klasifikasi gambar, kita perlu memisahkan gambar ke dalam berbagai kelas, yang merupakan pekerjaan manual.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Namun, kita mungkin ingin menggunakan data mentah (tanpa label) untuk melatih ekstraktor fitur CNN, yang disebut **pembelajaran mandiri**. Alih-alih menggunakan label, kita akan menggunakan gambar pelatihan sebagai input dan output jaringan. Ide utama dari **autoencoder** adalah kita akan memiliki **encoder network** yang mengubah gambar input menjadi **latent space** (biasanya hanya berupa vektor dengan ukuran lebih kecil), lalu **decoder network**, yang bertujuan untuk merekonstruksi gambar asli.

> ✅ [Autoencoder](https://wikipedia.org/wiki/Autoencoder) adalah "jenis jaringan saraf buatan yang digunakan untuk mempelajari pengkodean yang efisien dari data tanpa label."

Karena kita melatih autoencoder untuk menangkap sebanyak mungkin informasi dari gambar asli agar rekonstruksi akurat, jaringan mencoba menemukan **embedding** terbaik dari gambar input untuk menangkap maknanya.

![Diagram AutoEncoder](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.id.jpg)

> Gambar dari [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Skenario Penggunaan Autoencoders

Meskipun merekonstruksi gambar asli tampaknya tidak terlalu berguna dengan sendirinya, ada beberapa skenario di mana autoencoders sangat berguna:

* **Mengurangi dimensi gambar untuk visualisasi** atau **melatih embedding gambar**. Biasanya autoencoders memberikan hasil yang lebih baik daripada PCA, karena mempertimbangkan sifat spasial gambar dan fitur hierarkis.
* **Denoising**, yaitu menghilangkan noise dari gambar. Karena noise membawa banyak informasi yang tidak berguna, autoencoder tidak dapat memuat semuanya ke dalam latent space yang relatif kecil, sehingga hanya menangkap bagian penting dari gambar. Saat melatih denoiser, kita mulai dengan gambar asli, dan menggunakan gambar dengan noise yang ditambahkan secara artifisial sebagai input untuk autoencoder.
* **Super-resolution**, meningkatkan resolusi gambar. Kita mulai dengan gambar beresolusi tinggi, dan menggunakan gambar dengan resolusi lebih rendah sebagai input autoencoder.
* **Model generatif**. Setelah kita melatih autoencoder, bagian decoder dapat digunakan untuk membuat objek baru mulai dari vektor laten acak.

## Variational Autoencoders (VAE)

Autoencoder tradisional mengurangi dimensi data input dengan cara tertentu, menemukan fitur penting dari gambar input. Namun, vektor laten sering kali tidak memiliki makna yang jelas. Dengan kata lain, mengambil dataset MNIST sebagai contoh, menentukan digit mana yang sesuai dengan vektor laten yang berbeda bukanlah tugas yang mudah, karena vektor laten yang berdekatan tidak selalu sesuai dengan digit yang sama.

Di sisi lain, untuk melatih *model generatif* lebih baik memiliki pemahaman tentang latent space. Ide ini membawa kita ke **variational auto-encoder** (VAE).

VAE adalah autoencoder yang belajar memprediksi *distribusi statistik* dari parameter laten, yang disebut **latent distribution**. Sebagai contoh, kita mungkin ingin vektor laten didistribusikan secara normal dengan rata-rata z<sub>mean</sub> dan standar deviasi z<sub>sigma</sub> (baik rata-rata maupun standar deviasi adalah vektor dengan dimensi tertentu d). Encoder dalam VAE belajar memprediksi parameter tersebut, lalu decoder mengambil vektor acak dari distribusi ini untuk merekonstruksi objek.

Ringkasnya:

* Dari vektor input, kita memprediksi `z_mean` dan `z_log_sigma` (alih-alih memprediksi standar deviasi itu sendiri, kita memprediksi logaritmanya)
* Kita mengambil sampel vektor `sample` dari distribusi N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
* Decoder mencoba mendekode gambar asli menggunakan `sample` sebagai vektor input

<img src="images/vae.png" width="50%">

> Gambar dari [blog post ini](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) oleh Isaak Dykeman

Variational auto-encoders menggunakan fungsi loss yang kompleks yang terdiri dari dua bagian:

* **Reconstruction loss** adalah fungsi loss yang menunjukkan seberapa dekat gambar yang direkonstruksi dengan target (bisa berupa Mean Squared Error, atau MSE). Ini adalah fungsi loss yang sama seperti pada autoencoders biasa.
* **KL loss**, yang memastikan distribusi variabel laten tetap dekat dengan distribusi normal. Ini didasarkan pada konsep [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metrik untuk memperkirakan seberapa mirip dua distribusi statistik.

Salah satu keuntungan penting dari VAE adalah memungkinkan kita untuk menghasilkan gambar baru dengan relatif mudah, karena kita tahu distribusi mana yang digunakan untuk mengambil sampel vektor laten. Sebagai contoh, jika kita melatih VAE dengan vektor laten 2D pada MNIST, kita kemudian dapat memvariasikan komponen vektor laten untuk mendapatkan digit yang berbeda:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Perhatikan bagaimana gambar saling menyatu, saat kita mulai mendapatkan vektor laten dari bagian yang berbeda dari ruang parameter laten. Kita juga dapat memvisualisasikan ruang ini dalam 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Latihan: Autoencoders

Pelajari lebih lanjut tentang autoencoders dalam notebook berikut:

* [Autoencoders di TensorFlow](AutoencodersTF.ipynb)
* [Autoencoders di PyTorch](AutoEncodersPyTorch.ipynb)

## Properti Autoencoders

* **Spesifik Data** - mereka hanya bekerja dengan baik pada jenis gambar yang telah dilatih. Sebagai contoh, jika kita melatih jaringan super-resolution pada bunga, itu tidak akan bekerja dengan baik pada potret. Hal ini karena jaringan dapat menghasilkan gambar beresolusi lebih tinggi dengan mengambil detail halus dari fitur yang dipelajari dari dataset pelatihan.
* **Lossy** - gambar yang direkonstruksi tidak sama dengan gambar asli. Sifat loss ditentukan oleh *fungsi loss* yang digunakan selama pelatihan.
* Bekerja pada **data tanpa label**

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Kesimpulan

Dalam pelajaran ini, Anda belajar tentang berbagai jenis autoencoders yang tersedia untuk ilmuwan AI. Anda belajar cara membangunnya, dan cara menggunakannya untuk merekonstruksi gambar. Anda juga belajar tentang VAE dan cara menggunakannya untuk menghasilkan gambar baru.

## 🚀 Tantangan

Dalam pelajaran ini, Anda belajar tentang penggunaan autoencoders untuk gambar. Tetapi mereka juga dapat digunakan untuk musik! Lihat proyek Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), yang menggunakan autoencoders untuk belajar merekonstruksi musik. Lakukan beberapa [eksperimen](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) dengan pustaka ini untuk melihat apa yang dapat Anda buat.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Tinjauan & Studi Mandiri

Sebagai referensi, baca lebih lanjut tentang autoencoders dalam sumber berikut:

* [Membangun Autoencoders di Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post di NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Dijelaskan](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tugas

Di akhir [notebook ini menggunakan TensorFlow](AutoencodersTF.ipynb), Anda akan menemukan 'tugas' - gunakan ini sebagai tugas Anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.