# Segmentasi

Kita telah mempelajari sebelumnya tentang Deteksi Objek, yang memungkinkan kita untuk menemukan objek dalam gambar dengan memprediksi *kotak pembatas* mereka. Namun, untuk beberapa tugas, kita tidak hanya memerlukan kotak pembatas, tetapi juga lokalisi objek yang lebih tepat. Tugas ini disebut **segmentasi**.

## [Kuis pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentasi dapat dilihat sebagai **klasifikasi piksel**, di mana untuk **setiap** piksel dalam gambar kita harus memprediksi kelasnya (*latar belakang* menjadi salah satu kelas). Ada dua algoritma segmentasi utama:

* **Segmentasi semantik** hanya memberi tahu kelas piksel, dan tidak membedakan antara objek yang berbeda dari kelas yang sama.
* **Segmentasi instansi** membagi kelas menjadi instansi yang berbeda.

Untuk segmentasi instansi, domba-domba ini adalah objek yang berbeda, tetapi untuk segmentasi semantik semua domba diwakili oleh satu kelas.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Gambar dari [posting blog ini](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Ada berbagai arsitektur neural untuk segmentasi, tetapi semuanya memiliki struktur yang sama. Dalam hal ini, ini mirip dengan autoencoder yang telah Anda pelajari sebelumnya, tetapi alih-alih mendekonstruksi gambar asli, tujuan kita adalah mendekonstruksi **masker**. Dengan demikian, jaringan segmentasi memiliki bagian-bagian berikut:

* **Encoder** mengekstrak fitur dari gambar input
* **Decoder** mengubah fitur-fitur tersebut menjadi **gambar masker**, dengan ukuran dan jumlah saluran yang sama sesuai dengan jumlah kelas.

<img src="images/segm.png" width="80%">

> Gambar dari [publikasi ini](https://arxiv.org/pdf/2001.05566.pdf)

Kita harus menyebutkan fungsi kehilangan yang digunakan untuk segmentasi. Saat menggunakan autoencoder klasik, kita perlu mengukur kesamaan antara dua gambar, dan kita dapat menggunakan kesalahan kuadrat rata-rata (MSE) untuk melakukannya. Dalam segmentasi, setiap piksel dalam gambar masker target mewakili nomor kelas (one-hot-encoded di sepanjang dimensi ketiga), jadi kita perlu menggunakan fungsi kehilangan yang spesifik untuk klasifikasi - kehilangan cross-entropy, yang dirata-ratakan di seluruh piksel. Jika masker bersifat biner - **loss binary cross-entropy** (BCE) digunakan.

> ✅ One-hot encoding adalah cara untuk mengkodekan label kelas menjadi vektor dengan panjang yang sama dengan jumlah kelas. Lihat [artikel ini](https://datagy.io/sklearn-one-hot-encode/) tentang teknik ini.

## Segmentasi untuk Pencitraan Medis

Dalam pelajaran ini, kita akan melihat segmentasi dalam aksi dengan melatih jaringan untuk mengenali nevus manusia (juga dikenal sebagai tahi lalat) pada gambar medis. Kita akan menggunakan <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> dari gambar dermatoskopi sebagai sumber gambar. Dataset ini berisi 200 gambar dari tiga kelas: nevus tipikal, nevus atipikal, dan melanoma. Semua gambar juga mengandung **masker** yang sesuai yang menggambarkan nevus.

> ✅ Teknik ini sangat sesuai untuk jenis pencitraan medis ini, tetapi aplikasi dunia nyata lainnya apa yang dapat Anda bayangkan?

<img alt="navi" src="images/navi.png"/>

> Gambar dari PH<sup>2</sup> Database

Kita akan melatih model untuk mengsegmentasi nevus dari latar belakangnya.

## ✍️ Latihan: Segmentasi Semantik

Buka notebook di bawah ini untuk mempelajari lebih lanjut tentang berbagai arsitektur segmentasi semantik, berlatih bekerja dengan mereka, dan melihatnya dalam aksi.

* [Segmentasi Semantik Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentasi Semantik TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Kuis pasca-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Kesimpulan

Segmentasi adalah teknik yang sangat kuat untuk klasifikasi gambar, bergerak melampaui kotak pembatas menuju klasifikasi tingkat piksel. Ini adalah teknik yang digunakan dalam pencitraan medis, di antara aplikasi lainnya.

## 🚀 Tantangan

Segmentasi tubuh hanyalah salah satu dari tugas umum yang dapat kita lakukan dengan gambar orang. Tugas penting lainnya termasuk **deteksi kerangka** dan **deteksi pose**. Cobalah pustaka [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) untuk melihat bagaimana deteksi pose dapat digunakan.

## Tinjauan & Studi Mandiri

Artikel [wikipedia ini](https://wikipedia.org/wiki/Image_segmentation) menawarkan gambaran yang baik tentang berbagai aplikasi teknik ini. Pelajari lebih lanjut secara mandiri tentang subdomain segmentasi instansi dan segmentasi panoptik dalam bidang penyelidikan ini.

## [Tugas](lab/README.md)

Dalam lab ini, coba **segmentasi tubuh manusia** menggunakan [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) dari Kaggle.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.