# Rangkaian Neural Network

Seperti yang telah kita pelajari, untuk dapat melatih rangkaian neural dengan efisien, kita perlu melakukan dua hal:

* Beroperasi pada tensor, misalnya mengalikan, menjumlahkan, dan menghitung beberapa fungsi seperti sigmoid atau softmax
* Menghitung gradien dari semua ekspresi, untuk melakukan optimasi penurunan gradien

## [Kuis Pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Sementara pustaka `numpy` dapat melakukan bagian pertama, kita memerlukan mekanisme untuk menghitung gradien. Dalam [rangkaian kami](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) yang telah kami kembangkan di bagian sebelumnya, kami harus memprogram semua fungsi turunan secara manual di dalam metode `backward`, yang melakukan backpropagation. Idealnya, sebuah rangkaian harus memberi kita kesempatan untuk menghitung gradien dari *ekspresi apapun* yang dapat kita definisikan.

Hal penting lainnya adalah kemampuan untuk melakukan perhitungan di GPU, atau unit komputasi khusus lainnya, seperti [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Pelatihan rangkaian neural yang dalam memerlukan *banyak* perhitungan, dan kemampuan untuk memparalelkan perhitungan tersebut di GPU sangat penting.

> ✅ Istilah 'memparalelkan' berarti mendistribusikan perhitungan di beberapa perangkat.

Saat ini, dua rangkaian neural yang paling populer adalah: [TensorFlow](http://TensorFlow.org) dan [PyTorch](https://pytorch.org/). Keduanya menyediakan API tingkat rendah untuk beroperasi dengan tensor di CPU dan GPU. Di atas API tingkat rendah, ada juga API tingkat tinggi, yang disebut [Keras](https://keras.io/) dan [PyTorch Lightning](https://pytorchlightning.ai/) masing-masing.

API Tingkat Rendah | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
-------------------|-------------------------------------|--------------------------------
API Tingkat Tinggi | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**API tingkat rendah** di kedua rangkaian memungkinkan Anda untuk membangun yang disebut **grafik komputasi**. Grafik ini mendefinisikan bagaimana cara menghitung output (biasanya fungsi kerugian) dengan parameter input yang diberikan, dan dapat didorong untuk perhitungan di GPU, jika tersedia. Ada fungsi untuk membedakan grafik komputasi ini dan menghitung gradien, yang kemudian dapat digunakan untuk mengoptimalkan parameter model.

**API tingkat tinggi** sebagian besar menganggap rangkaian neural sebagai **urutan lapisan**, dan membuat konstruksi sebagian besar rangkaian neural jauh lebih mudah. Melatih model biasanya memerlukan persiapan data dan kemudian memanggil fungsi `fit` untuk melakukan pekerjaan tersebut.

API tingkat tinggi memungkinkan Anda untuk membangun rangkaian neural yang khas dengan sangat cepat tanpa khawatir tentang banyak detail. Pada saat yang sama, API tingkat rendah menawarkan kontrol yang jauh lebih besar atas proses pelatihan, sehingga sering digunakan dalam penelitian, ketika Anda berurusan dengan arsitektur rangkaian neural baru.

Penting juga untuk memahami bahwa Anda dapat menggunakan kedua API bersama-sama, misalnya, Anda dapat mengembangkan arsitektur lapisan jaringan Anda sendiri menggunakan API tingkat rendah, dan kemudian menggunakannya di dalam jaringan yang lebih besar yang dibangun dan dilatih dengan API tingkat tinggi. Atau Anda dapat mendefinisikan jaringan menggunakan API tingkat tinggi sebagai urutan lapisan, dan kemudian menggunakan loop pelatihan tingkat rendah Anda sendiri untuk melakukan optimasi. Kedua API menggunakan konsep dasar yang sama, dan mereka dirancang untuk bekerja dengan baik bersama-sama.

## Pembelajaran

Dalam kursus ini, kami menawarkan sebagian besar konten baik untuk PyTorch maupun TensorFlow. Anda dapat memilih rangkaian yang Anda sukai dan hanya melalui buku catatan yang sesuai. Jika Anda tidak yakin rangkaian mana yang harus dipilih, baca beberapa diskusi di internet mengenai **PyTorch vs. TensorFlow**. Anda juga dapat melihat kedua rangkaian tersebut untuk mendapatkan pemahaman yang lebih baik.

Jika memungkinkan, kami akan menggunakan API Tingkat Tinggi untuk kesederhanaan. Namun, kami percaya penting untuk memahami bagaimana rangkaian neural bekerja dari dasar, sehingga pada awalnya kami mulai dengan bekerja dengan API tingkat rendah dan tensor. Namun, jika Anda ingin cepat memulai dan tidak ingin menghabiskan banyak waktu untuk mempelajari detail ini, Anda dapat melewatkan bagian tersebut dan langsung masuk ke buku catatan API tingkat tinggi.

## ✍️ Latihan: Rangkaian

Lanjutkan pembelajaran Anda di buku catatan berikut:

API Tingkat Rendah | [Notebook TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
-------------------|-------------------------------------|--------------------------------
API Tingkat Tinggi | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Setelah menguasai rangkaian, mari kita ulas konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk memahaminya dengan benar!

Pertimbangkan masalah berikut dari mendekati 5 titik (diwakili oleh `x` pada grafik di bawah):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.ms.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.ms.jpg)
-------------------------|--------------------------
**Model linier, 2 parameter** | **Model non-linier, 7 parameter**
Kesalahan pelatihan = 5.3 | Kesalahan pelatihan = 0
Kesalahan validasi = 5.1 | Kesalahan validasi = 20

* Di sebelah kiri, kita melihat pendekatan garis lurus yang baik. Karena jumlah parameter memadai, model menangkap ide di balik distribusi titik dengan benar.
* Di sebelah kanan, model terlalu kuat. Karena kita hanya memiliki 5 titik dan model memiliki 7 parameter, ia dapat disesuaikan sedemikian rupa sehingga melewati semua titik, membuat kesalahan pelatihan menjadi 0. Namun, ini mencegah model memahami pola yang benar di balik data, sehingga kesalahan validasi menjadi sangat tinggi.

Sangat penting untuk menemukan keseimbangan yang tepat antara kekayaan model (jumlah parameter) dan jumlah sampel pelatihan.

## Mengapa overfitting terjadi

  * Data pelatihan tidak cukup
  * Model terlalu kuat
  * Terlalu banyak noise dalam data input

## Bagaimana mendeteksi overfitting

Seperti yang dapat Anda lihat dari grafik di atas, overfitting dapat dideteksi dengan kesalahan pelatihan yang sangat rendah, dan kesalahan validasi yang tinggi. Biasanya selama pelatihan kita akan melihat baik kesalahan pelatihan maupun validasi mulai menurun, dan kemudian pada suatu titik kesalahan validasi mungkin berhenti menurun dan mulai meningkat. Ini akan menjadi tanda overfitting, dan indikator bahwa kita mungkin harus berhenti melatih pada titik ini (atau setidaknya membuat snapshot model).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.ms.png)

## Bagaimana mencegah overfitting

Jika Anda dapat melihat bahwa overfitting terjadi, Anda dapat melakukan salah satu dari yang berikut:

 * Meningkatkan jumlah data pelatihan
 * Mengurangi kompleksitas model
 * Menggunakan beberapa [teknik regulasi](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), seperti [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), yang akan kita bahas kemudian.

## Overfitting dan Tradeoff Bias-Variance

Overfitting sebenarnya adalah kasus dari masalah yang lebih umum dalam statistik yang disebut [Tradeoff Bias-Variance](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Jika kita mempertimbangkan kemungkinan sumber kesalahan dalam model kita, kita dapat melihat dua jenis kesalahan:

* **Kesalahan bias** disebabkan oleh algoritma kita yang tidak dapat menangkap hubungan antara data pelatihan dengan benar. Ini dapat disebabkan oleh fakta bahwa model kita tidak cukup kuat (**underfitting**).
* **Kesalahan varians**, yang disebabkan oleh model yang memperkirakan noise dalam data input daripada hubungan yang berarti (**overfitting**).

Selama pelatihan, kesalahan bias menurun (saat model kita belajar untuk mendekati data), dan kesalahan varians meningkat. Penting untuk menghentikan pelatihan - baik secara manual (ketika kita mendeteksi overfitting) atau otomatis (dengan memperkenalkan regulasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, Anda belajar tentang perbedaan antara berbagai API untuk dua rangkaian AI paling populer, TensorFlow dan PyTorch. Selain itu, Anda juga belajar tentang topik yang sangat penting, overfitting.

## 🚀 Tantangan

Di buku catatan yang menyertainya, Anda akan menemukan 'tugas' di bagian bawah; kerjakan buku catatan tersebut dan selesaikan tugasnya.

## [Kuis Pasca-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Tinjauan & Studi Mandiri

Lakukan penelitian tentang topik berikut:

- TensorFlow
- PyTorch
- Overfitting

Tanyakan pada diri Anda pertanyaan berikut:

- Apa perbedaan antara TensorFlow dan PyTorch?
- Apa perbedaan antara overfitting dan underfitting?

## [Tugas](lab/README.md)

Dalam lab ini, Anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan jaringan terhubung penuh satu lapisan dan multi-lapisan menggunakan PyTorch atau TensorFlow.

* [Instruksi](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.