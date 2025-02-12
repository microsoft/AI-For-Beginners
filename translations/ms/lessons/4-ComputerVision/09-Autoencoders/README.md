# Autoencoders

Apabila melatih CNN, salah satu masalah yang dihadapi adalah kita memerlukan banyak data berlabel. Dalam kes klasifikasi imej, kita perlu memisahkan imej kepada pelbagai kelas, yang merupakan usaha manual.

## [Kuiz sebelum kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Namun, kita mungkin ingin menggunakan data mentah (tidak berlabel) untuk melatih pengekstrak ciri CNN, yang dikenali sebagai **pembelajaran kendiri**. Sebagai ganti label, kita akan menggunakan imej latihan sebagai input dan output rangkaian. Idea utama **autoencoder** adalah kita akan mempunyai **rangkaian pengekod** yang menukarkan imej input kepada **ruang laten** (biasanya ia hanya merupakan vektor dengan saiz yang lebih kecil), kemudian **rangkaian dekoder**, yang bertujuan untuk membina semula imej asal.

> ✅ An [autoencoder](https://wikipedia.org/wiki/Autoencoder) adalah "sejenis rangkaian neural tiruan yang digunakan untuk mempelajari pengkodan yang cekap bagi data tidak berlabel."

Oleh kerana kita melatih autoencoder untuk menangkap sebanyak mungkin maklumat dari imej asal untuk pembinaan semula yang tepat, rangkaian tersebut berusaha untuk mencari **penyematan** terbaik bagi imej input untuk menangkap makna.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.ms.jpg)

> Imej dari [blog Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Senario untuk menggunakan Autoencoders

Walaupun membina semula imej asal tidak kelihatan berguna dengan sendirinya, terdapat beberapa senario di mana autoencoders sangat berguna:

* **Mengurangkan dimensi imej untuk visualisasi** atau **melatih penyematan imej**. Biasanya autoencoders memberikan hasil yang lebih baik daripada PCA, kerana ia mengambil kira sifat spatial imej dan ciri hierarki.
* **Pengurangan bunyi**, iaitu menghapuskan bunyi dari imej. Kerana bunyi membawa banyak maklumat yang tidak berguna, autoencoder tidak dapat memuatkan semuanya ke dalam ruang laten yang relatif kecil, dan oleh itu ia hanya menangkap bahagian penting imej. Apabila melatih pengurang bunyi, kita bermula dengan imej asal, dan menggunakan imej dengan bunyi yang ditambah secara artifisial sebagai input untuk autoencoder.
* **Super-resolusi**, meningkatkan resolusi imej. Kita bermula dengan imej beresolusi tinggi, dan menggunakan imej dengan resolusi lebih rendah sebagai input autoencoder.
* **Model generatif**. Setelah kita melatih autoencoder, bahagian dekoder boleh digunakan untuk mencipta objek baru bermula dari vektor laten rawak.

## Autoencoders Variasional (VAE)

Autoencoders tradisional mengurangkan dimensi data input dengan cara tertentu, mengenal pasti ciri penting imej input. Namun, vektor laten sering kali tidak memberikan makna yang jelas. Dengan kata lain, mengambil set data MNIST sebagai contoh, menentukan digit mana yang sepadan dengan vektor laten yang berbeza bukanlah tugas yang mudah, kerana vektor laten yang dekat tidak semestinya sepadan dengan digit yang sama.

Sebaliknya, untuk melatih model *generatif*, adalah lebih baik untuk mempunyai pemahaman tentang ruang laten. Idea ini membawa kita kepada **autoencoder variational** (VAE).

VAE adalah autoencoder yang belajar untuk meramalkan *taburan statistik* bagi parameter laten, yang dikenali sebagai **taburan laten**. Sebagai contoh, kita mungkin ingin vektor laten didistribusikan secara normal dengan beberapa min z<sub>mean</sub> dan sisihan piawai z<sub>sigma</sub> (kedua-dua min dan sisihan piawai adalah vektor dengan dimensi tertentu d). Pengekod dalam VAE belajar untuk meramalkan parameter tersebut, dan kemudian dekoder mengambil vektor rawak dari taburan ini untuk membina semula objek.

Untuk merumuskan:

 * Dari vektor input, kita meramalkan `z_mean` dan `z_log_sigma` (daripada meramalkan sisihan piawai itu sendiri, kita meramalkan logaritmnya)
 * Kita mengambil sampel vektor `sample` dari taburan N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Dekoder berusaha untuk mendekod imej asal menggunakan `sample` sebagai vektor input

 <img src="images/vae.png" width="50%">

> Imej dari [post blog ini](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) oleh Isaak Dykeman

Autoencoders variational menggunakan fungsi kerugian yang kompleks yang terdiri daripada dua bahagian:

* **Kerugian pembinaan semula** adalah fungsi kerugian yang menunjukkan betapa dekatnya imej yang dibina semula dengan sasaran (ia boleh menjadi Mean Squared Error, atau MSE). Ia adalah fungsi kerugian yang sama seperti dalam autoencoders biasa.
* **Kerugian KL**, yang memastikan bahawa taburan pembolehubah laten tetap dekat dengan taburan normal. Ia berdasarkan kepada konsep [divergensi Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - satu metrik untuk menganggarkan seberapa mirip dua taburan statistik.

Satu kelebihan penting VAE adalah bahawa ia membolehkan kita menjana imej baru dengan agak mudah, kerana kita tahu taburan dari mana untuk mengambil vektor laten. Sebagai contoh, jika kita melatih VAE dengan vektor laten 2D pada MNIST, kita boleh mengubah komponen vektor laten untuk mendapatkan digit yang berbeza:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

Perhatikan bagaimana imej bercampur antara satu sama lain, apabila kita mula mendapatkan vektor laten dari bahagian yang berbeza dalam ruang parameter laten. Kita juga boleh memvisualisasikan ruang ini dalam 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Latihan: Autoencoders

Ketahui lebih lanjut tentang autoencoders dalam notebook yang berkaitan ini:

* [Autoencoders dalam TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders dalam PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Ciri-ciri Autoencoders

* **Spesifik Data** - mereka hanya berfungsi dengan baik dengan jenis imej yang telah mereka latih. Sebagai contoh, jika kita melatih rangkaian super-resolusi pada bunga, ia tidak akan berfungsi dengan baik pada potret. Ini kerana rangkaian boleh menghasilkan imej beresolusi tinggi dengan mengambil butiran halus dari ciri yang dipelajari daripada set data latihan.
* **Rugi** - imej yang dibina semula tidak sama dengan imej asal. Sifat kerugian ditentukan oleh *fungsi kerugian* yang digunakan semasa latihan.
* Berfungsi pada **data tidak berlabel**.

## [Kuiz selepas kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Kesimpulan

Dalam pelajaran ini, anda telah mempelajari pelbagai jenis autoencoders yang tersedia untuk saintis AI. Anda telah belajar bagaimana untuk membinanya, dan bagaimana untuk menggunakannya untuk membina semula imej. Anda juga telah belajar tentang VAE dan bagaimana untuk menggunakannya untuk menjana imej baru.

## 🚀 Cabaran

Dalam pelajaran ini, anda telah belajar tentang menggunakan autoencoders untuk imej. Tetapi ia juga boleh digunakan untuk muzik! Semak projek Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), yang menggunakan autoencoders untuk belajar membina semula muzik. Lakukan beberapa [eksperimen](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) dengan perpustakaan ini untuk melihat apa yang boleh anda cipta.

## [Kuiz selepas kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Ulasan & Pembelajaran Sendiri

Sebagai rujukan, baca lebih lanjut tentang autoencoders dalam sumber-sumber ini:

* [Membina Autoencoders dalam Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Post blog tentang NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencoders Variational Dijelaskan](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencoders Variational Bersyarat](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tugasan

Di akhir [notebook ini menggunakan TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), anda akan menemui 'tugas' - gunakan ini sebagai tugasan anda.

**Penafian**: 
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia yang profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.