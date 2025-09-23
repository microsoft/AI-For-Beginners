<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-29T12:36:56+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "id"
}
-->
# Kerangka Kerja Jaringan Saraf

Seperti yang telah kita pelajari, untuk dapat melatih jaringan saraf secara efisien, kita perlu melakukan dua hal:

* Mengoperasikan tensor, misalnya mengalikan, menjumlahkan, dan menghitung beberapa fungsi seperti sigmoid atau softmax
* Menghitung gradien dari semua ekspresi, untuk melakukan optimasi penurunan gradien

## [Kuis sebelum kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Meskipun pustaka `numpy` dapat melakukan bagian pertama, kita memerlukan mekanisme untuk menghitung gradien. Dalam [kerangka kerja kita](../04-OwnFramework/OwnFramework.ipynb) yang telah kita kembangkan di bagian sebelumnya, kita harus memprogram semua fungsi turunan secara manual di dalam metode `backward`, yang melakukan backpropagation. Idealnya, sebuah kerangka kerja harus memberi kita kesempatan untuk menghitung gradien dari *ekspresi apa pun* yang dapat kita definisikan.

Hal penting lainnya adalah kemampuan untuk melakukan komputasi di GPU, atau unit komputasi khusus lainnya, seperti [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Pelatihan jaringan saraf dalam membutuhkan *banyak* komputasi, dan kemampuan untuk melakukan paralelisasi komputasi tersebut di GPU sangatlah penting.

> ✅ Istilah 'paralelisasi' berarti mendistribusikan komputasi ke beberapa perangkat.

Saat ini, dua kerangka kerja jaringan saraf yang paling populer adalah: [TensorFlow](http://TensorFlow.org) dan [PyTorch](https://pytorch.org/). Keduanya menyediakan API tingkat rendah untuk mengoperasikan tensor di CPU maupun GPU. Di atas API tingkat rendah, terdapat juga API tingkat tinggi, yang disebut [Keras](https://keras.io/) dan [PyTorch Lightning](https://pytorchlightning.ai/) masing-masing.

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**API tingkat rendah** dalam kedua kerangka kerja memungkinkan Anda membangun apa yang disebut **graf komputasi**. Graf ini mendefinisikan bagaimana menghitung keluaran (biasanya fungsi loss) dengan parameter masukan yang diberikan, dan dapat dikirimkan untuk komputasi di GPU, jika tersedia. Terdapat fungsi untuk mendiferensiasi graf komputasi ini dan menghitung gradien, yang kemudian dapat digunakan untuk mengoptimalkan parameter model.

**API tingkat tinggi** pada dasarnya menganggap jaringan saraf sebagai **urutan lapisan**, dan membuat konstruksi sebagian besar jaringan saraf menjadi jauh lebih mudah. Melatih model biasanya hanya memerlukan persiapan data dan kemudian memanggil fungsi `fit` untuk menjalankan prosesnya.

API tingkat tinggi memungkinkan Anda membangun jaringan saraf khas dengan sangat cepat tanpa perlu khawatir tentang banyak detail. Di sisi lain, API tingkat rendah menawarkan kontrol yang jauh lebih besar atas proses pelatihan, sehingga sering digunakan dalam penelitian, terutama ketika Anda bekerja dengan arsitektur jaringan saraf baru.

Penting juga untuk memahami bahwa Anda dapat menggunakan kedua API tersebut secara bersamaan, misalnya Anda dapat mengembangkan arsitektur lapisan jaringan Anda sendiri menggunakan API tingkat rendah, lalu menggunakannya di dalam jaringan yang lebih besar yang dibangun dan dilatih dengan API tingkat tinggi. Atau Anda dapat mendefinisikan jaringan menggunakan API tingkat tinggi sebagai urutan lapisan, lalu menggunakan loop pelatihan tingkat rendah Anda sendiri untuk melakukan optimasi. Kedua API menggunakan konsep dasar yang sama, dan dirancang untuk bekerja dengan baik bersama-sama.

## Pembelajaran

Dalam kursus ini, kami menyediakan sebagian besar konten untuk PyTorch dan TensorFlow. Anda dapat memilih kerangka kerja yang Anda sukai dan hanya mempelajari notebook yang sesuai. Jika Anda tidak yakin kerangka kerja mana yang harus dipilih, bacalah beberapa diskusi di internet tentang **PyTorch vs. TensorFlow**. Anda juga dapat melihat kedua kerangka kerja tersebut untuk mendapatkan pemahaman yang lebih baik.

Jika memungkinkan, kami akan menggunakan API Tingkat Tinggi untuk kesederhanaan. Namun, kami percaya bahwa penting untuk memahami cara kerja jaringan saraf dari dasar, sehingga pada awalnya kami mulai bekerja dengan API tingkat rendah dan tensor. Namun, jika Anda ingin segera memulai dan tidak ingin menghabiskan banyak waktu mempelajari detail ini, Anda dapat melewati bagian tersebut dan langsung ke notebook API tingkat tinggi.

## ✍️ Latihan: Kerangka Kerja

Lanjutkan pembelajaran Anda di notebook berikut:

Low-Level API | [TensorFlow+Keras Notebook](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Setelah menguasai kerangka kerja, mari kita ulas kembali konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk memahaminya dengan benar!

Pertimbangkan masalah berikut dalam mendekati 5 titik (diwakili oleh `x` pada grafik di bawah):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.id.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.id.jpg)
-------------------------|--------------------------
**Model linear, 2 parameter** | **Model non-linear, 7 parameter**
Error pelatihan = 5.3 | Error pelatihan = 0
Error validasi = 5.1 | Error validasi = 20

* Di sebelah kiri, kita melihat pendekatan garis lurus yang baik. Karena jumlah parameter memadai, model memahami distribusi titik dengan benar.
* Di sebelah kanan, model terlalu kuat. Karena kita hanya memiliki 5 titik dan model memiliki 7 parameter, model dapat menyesuaikan sedemikian rupa sehingga melewati semua titik, membuat error pelatihan menjadi 0. Namun, ini mencegah model memahami pola yang benar di balik data, sehingga error validasi sangat tinggi.

Sangat penting untuk mencapai keseimbangan yang tepat antara kekayaan model (jumlah parameter) dan jumlah sampel pelatihan.

## Mengapa overfitting terjadi

  * Data pelatihan tidak cukup
  * Model terlalu kuat
  * Terlalu banyak noise dalam data masukan

## Cara mendeteksi overfitting

Seperti yang dapat Anda lihat dari grafik di atas, overfitting dapat dideteksi dengan error pelatihan yang sangat rendah, dan error validasi yang tinggi. Biasanya selama pelatihan kita akan melihat error pelatihan dan validasi mulai menurun, lalu pada titik tertentu error validasi mungkin berhenti menurun dan mulai meningkat. Ini akan menjadi tanda overfitting, dan indikator bahwa kita mungkin harus menghentikan pelatihan pada titik ini (atau setidaknya membuat snapshot model).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.id.png)

## Cara mencegah overfitting

Jika Anda melihat bahwa overfitting terjadi, Anda dapat melakukan salah satu dari berikut:

 * Menambah jumlah data pelatihan
 * Mengurangi kompleksitas model
 * Menggunakan beberapa [teknik regularisasi](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), seperti [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), yang akan kita bahas nanti.

## Overfitting dan Bias-Variance Tradeoff

Overfitting sebenarnya adalah kasus dari masalah yang lebih umum dalam statistik yang disebut [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Jika kita mempertimbangkan kemungkinan sumber error dalam model kita, kita dapat melihat dua jenis error:

* **Error bias** disebabkan oleh algoritma kita yang tidak mampu menangkap hubungan antara data pelatihan dengan benar. Ini dapat terjadi karena model kita tidak cukup kuat (**underfitting**).
* **Error varians**, yang disebabkan oleh model yang mendekati noise dalam data masukan alih-alih hubungan yang bermakna (**overfitting**).

Selama pelatihan, error bias menurun (karena model kita belajar mendekati data), dan error varians meningkat. Penting untuk menghentikan pelatihan - baik secara manual (ketika kita mendeteksi overfitting) atau secara otomatis (dengan memperkenalkan regularisasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, Anda telah mempelajari perbedaan antara berbagai API untuk dua kerangka kerja AI paling populer, TensorFlow dan PyTorch. Selain itu, Anda juga mempelajari topik yang sangat penting, overfitting.

## 🚀 Tantangan

Dalam notebook yang menyertai, Anda akan menemukan 'tugas' di bagian bawah; kerjakan notebook tersebut dan selesaikan tugasnya.

## [Kuis setelah kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Tinjauan & Studi Mandiri

Lakukan penelitian tentang topik berikut:

- TensorFlow
- PyTorch
- Overfitting

Tanyakan pada diri Anda pertanyaan berikut:

- Apa perbedaan antara TensorFlow dan PyTorch?
- Apa perbedaan antara overfitting dan underfitting?

## [Tugas](lab/README.md)

Dalam lab ini, Anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan jaringan fully-connected berlapis tunggal dan multi-lapis menggunakan PyTorch atau TensorFlow.

* [Instruksi](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.