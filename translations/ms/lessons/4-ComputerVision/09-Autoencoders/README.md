<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-29T11:50:47+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "ms"
}
-->
# Autoencoders

Apabila melatih CNN, salah satu masalahnya ialah kita memerlukan banyak data berlabel. Dalam kes klasifikasi imej, kita perlu memisahkan imej ke dalam kelas yang berbeza, yang memerlukan usaha manual.

## [Kuiz sebelum kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Namun, kita mungkin ingin menggunakan data mentah (tidak berlabel) untuk melatih pengekstrak ciri CNN, yang dipanggil **pembelajaran kendiri**. Sebagai ganti label, kita akan menggunakan imej latihan sebagai input dan output rangkaian. Idea utama **autoencoder** ialah kita akan mempunyai **rangkaian pengekod** yang menukar imej input kepada **ruang laten** (biasanya ia hanya vektor bersaiz lebih kecil), kemudian **rangkaian penyahkod**, yang bertujuan untuk membina semula imej asal.

> ✅ [Autoencoder](https://wikipedia.org/wiki/Autoencoder) ialah "sejenis rangkaian neural tiruan yang digunakan untuk mempelajari pengekodan cekap data tidak berlabel."

Oleh kerana kita melatih autoencoder untuk menangkap sebanyak mungkin maklumat daripada imej asal bagi pembinaan semula yang tepat, rangkaian cuba mencari **pengepaduan** terbaik imej input untuk menangkap maknanya.

![Diagram AutoEncoder](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.ms.jpg)

> Imej daripada [blog Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Senario penggunaan Autoencoders

Walaupun membina semula imej asal tidak kelihatan berguna dengan sendirinya, terdapat beberapa senario di mana autoencoders sangat berguna:

* **Mengurangkan dimensi imej untuk visualisasi** atau **melatih pengepaduan imej**. Biasanya autoencoders memberikan hasil yang lebih baik daripada PCA, kerana ia mengambil kira sifat spatial imej dan ciri hierarki.
* **Penyahbunyi**, iaitu menghilangkan bunyi daripada imej. Oleh kerana bunyi membawa banyak maklumat yang tidak berguna, autoencoder tidak dapat memuatkan semuanya ke dalam ruang laten yang agak kecil, dan oleh itu ia hanya menangkap bahagian penting imej. Apabila melatih penyahbunyi, kita bermula dengan imej asal, dan menggunakan imej dengan bunyi yang ditambah secara tiruan sebagai input untuk autoencoder.
* **Resolusi tinggi**, meningkatkan resolusi imej. Kita bermula dengan imej resolusi tinggi, dan menggunakan imej dengan resolusi lebih rendah sebagai input autoencoder.
* **Model generatif**. Setelah kita melatih autoencoder, bahagian penyahkod boleh digunakan untuk mencipta objek baharu bermula daripada vektor laten rawak.

## Variational Autoencoders (VAE)

Autoencoders tradisional mengurangkan dimensi data input dengan cara tertentu, mengenal pasti ciri penting imej input. Walau bagaimanapun, vektor laten sering tidak masuk akal. Sebagai contoh, mengambil dataset MNIST, mengenal pasti digit yang sepadan dengan vektor laten yang berbeza bukanlah tugas yang mudah, kerana vektor laten yang berdekatan tidak semestinya sepadan dengan digit yang sama.

Sebaliknya, untuk melatih model *generatif* adalah lebih baik untuk memahami ruang laten. Idea ini membawa kita kepada **variational auto-encoder** (VAE).

VAE ialah autoencoder yang belajar untuk meramalkan *taburan statistik* parameter laten, yang dipanggil **taburan laten**. Sebagai contoh, kita mungkin mahu vektor laten diedarkan secara normal dengan beberapa min z<sub>mean</sub> dan sisihan piawai z<sub>sigma</sub> (kedua-dua min dan sisihan piawai adalah vektor dengan beberapa dimensi d). Pengekod dalam VAE belajar untuk meramalkan parameter tersebut, dan kemudian penyahkod mengambil vektor rawak daripada taburan ini untuk membina semula objek.

Ringkasnya:

* Daripada vektor input, kita meramalkan `z_mean` dan `z_log_sigma` (bukannya meramalkan sisihan piawai itu sendiri, kita meramalkan logaritmanya)
* Kita mengambil sampel vektor `sample` daripada taburan N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
* Penyahkod cuba menyahkod imej asal menggunakan `sample` sebagai vektor input

<img src="images/vae.png" width="50%">

> Imej daripada [blog post ini](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) oleh Isaak Dykeman

Variational auto-encoders menggunakan fungsi kehilangan kompleks yang terdiri daripada dua bahagian:

* **Kehilangan pembinaan semula** ialah fungsi kehilangan yang menunjukkan sejauh mana imej yang dibina semula hampir dengan sasaran (ia boleh menjadi Mean Squared Error, atau MSE). Ia adalah fungsi kehilangan yang sama seperti dalam autoencoders biasa.
* **Kehilangan KL**, yang memastikan taburan pembolehubah laten kekal dekat dengan taburan normal. Ia berdasarkan konsep [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metrik untuk menganggarkan sejauh mana dua taburan statistik serupa.

Satu kelebihan penting VAE ialah ia membolehkan kita menjana imej baharu dengan agak mudah, kerana kita tahu taburan mana yang perlu diambil sampel vektor laten. Sebagai contoh, jika kita melatih VAE dengan vektor laten 2D pada MNIST, kita boleh mengubah komponen vektor laten untuk mendapatkan digit yang berbeza:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

Perhatikan bagaimana imej bercampur antara satu sama lain, apabila kita mula mendapatkan vektor laten daripada bahagian yang berbeza dalam ruang parameter laten. Kita juga boleh memvisualisasikan ruang ini dalam 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Latihan: Autoencoders

Ketahui lebih lanjut tentang autoencoders dalam buku nota berikut:

* [Autoencoders dalam TensorFlow](AutoencodersTF.ipynb)
* [Autoencoders dalam PyTorch](AutoEncodersPyTorch.ipynb)

## Sifat Autoencoders

* **Spesifik Data** - ia hanya berfungsi dengan baik dengan jenis imej yang telah dilatih. Sebagai contoh, jika kita melatih rangkaian resolusi tinggi pada bunga, ia tidak akan berfungsi dengan baik pada potret. Ini kerana rangkaian boleh menghasilkan imej resolusi tinggi dengan mengambil butiran halus daripada ciri yang dipelajari daripada dataset latihan.
* **Kehilangan** - imej yang dibina semula tidak sama seperti imej asal. Sifat kehilangan ditentukan oleh *fungsi kehilangan* yang digunakan semasa latihan.
* Berfungsi pada **data tidak berlabel**

## [Kuiz selepas kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Kesimpulan

Dalam pelajaran ini, anda telah mempelajari pelbagai jenis autoencoders yang tersedia untuk saintis AI. Anda telah belajar cara membinanya, dan cara menggunakannya untuk membina semula imej. Anda juga telah mempelajari tentang VAE dan cara menggunakannya untuk menjana imej baharu.

## 🚀 Cabaran

Dalam pelajaran ini, anda telah mempelajari tentang penggunaan autoencoders untuk imej. Tetapi ia juga boleh digunakan untuk muzik! Lihat projek Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), yang menggunakan autoencoders untuk belajar membina semula muzik. Lakukan beberapa [eksperimen](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) dengan perpustakaan ini untuk melihat apa yang boleh anda cipta.

## [Kuiz selepas kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Kajian & Pembelajaran Kendiri

Sebagai rujukan, baca lebih lanjut tentang autoencoders dalam sumber berikut:

* [Membina Autoencoders dalam Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post di NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Dijelaskan](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tugasan

Di akhir [buku nota ini menggunakan TensorFlow](AutoencodersTF.ipynb), anda akan menemui 'tugas' - gunakan ini sebagai tugasan anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.