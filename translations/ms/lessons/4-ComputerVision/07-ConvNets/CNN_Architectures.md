# Arsitektur CNN Yang Dikenal

### VGG-16

VGG-16 adalah jaringan yang mencapai akurasi 92,7% dalam klasifikasi top-5 ImageNet pada tahun 2014. Jaringan ini memiliki struktur lapisan sebagai berikut:

![Lapisan ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.ms.jpg)

Seperti yang dapat Anda lihat, VGG mengikuti arsitektur piramida tradisional, yang merupakan urutan lapisan konvolusi-pooling.

![Piramida ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.ms.jpg)

> Gambar dari [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet adalah keluarga model yang diusulkan oleh Microsoft Research pada tahun 2015. Ide utama dari ResNet adalah menggunakan **blok residual**:

<img src="images/resnet-block.png" width="300"/>

> Gambar dari [makalah ini](https://arxiv.org/pdf/1512.03385.pdf)

Alasan menggunakan identitas pass-through adalah untuk membuat lapisan kami memprediksi **perbedaan** antara hasil lapisan sebelumnya dan keluaran blok residual - sehingga dinamakan *residual*. Blok-blok ini jauh lebih mudah dilatih, dan seseorang dapat membangun jaringan dengan beberapa ratus blok tersebut (varian yang paling umum adalah ResNet-52, ResNet-101, dan ResNet-152).

Anda juga dapat memikirkan jaringan ini sebagai jaringan yang dapat menyesuaikan kompleksitasnya dengan dataset. Awalnya, ketika Anda mulai melatih jaringan, nilai bobot kecil, dan sebagian besar sinyal melewati lapisan identitas pass-through. Seiring berjalannya pelatihan dan bobot menjadi lebih besar, signifikansi parameter jaringan meningkat, dan jaringan menyesuaikan untuk memenuhi kekuatan ekspresif yang diperlukan untuk mengklasifikasikan gambar pelatihan dengan benar.

### Google Inception

Arsitektur Google Inception membawa ide ini selangkah lebih jauh, dan membangun setiap lapisan jaringan sebagai kombinasi dari beberapa jalur yang berbeda:

<img src="images/inception.png" width="400"/>

> Gambar dari [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Di sini, kita perlu menekankan peran konvolusi 1x1, karena pada awalnya mereka tidak masuk akal. Mengapa kita perlu menjalankan filter 1x1 melalui gambar? Namun, Anda perlu ingat bahwa filter konvolusi juga bekerja dengan beberapa saluran kedalaman (aslinya - warna RGB, di lapisan berikutnya - saluran untuk filter yang berbeda), dan konvolusi 1x1 digunakan untuk mencampur saluran input tersebut menggunakan bobot yang dapat dilatih. Ini juga dapat dilihat sebagai downsampling (pooling) di atas dimensi saluran.

Berikut adalah [posting blog yang bagus](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) tentang subjek ini, dan [makalah asli](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet adalah keluarga model dengan ukuran yang lebih kecil, cocok untuk perangkat mobile. Gunakan mereka jika Anda kekurangan sumber daya, dan dapat mengorbankan sedikit akurasi. Ide utama di balik mereka adalah **konvolusi terpisah berdasarkan kedalaman**, yang memungkinkan mewakili filter konvolusi dengan komposisi konvolusi spasial dan konvolusi 1x1 di atas saluran kedalaman. Ini secara signifikan mengurangi jumlah parameter, membuat jaringan lebih kecil, dan juga lebih mudah dilatih dengan data yang lebih sedikit.

Berikut adalah [posting blog yang bagus tentang MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Kesimpulan

Dalam unit ini, Anda telah mempelajari konsep utama di balik jaringan saraf visi komputer - jaringan konvolusi. Arsitektur nyata yang mendukung klasifikasi gambar, deteksi objek, dan bahkan jaringan generasi gambar semuanya didasarkan pada CNN, hanya dengan lebih banyak lapisan dan beberapa trik pelatihan tambahan.

## 🚀 Tantangan

Dalam buku catatan yang menyertai, ada catatan di bagian bawah tentang bagaimana mendapatkan akurasi yang lebih tinggi. Lakukan beberapa eksperimen untuk melihat apakah Anda dapat mencapai akurasi yang lebih tinggi.

## [Kuis pasca kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Tinjauan & Studi Mandiri

Meskipun CNN paling sering digunakan untuk tugas Visi Komputer, mereka umumnya baik untuk mengekstrak pola berukuran tetap. Misalnya, jika kita berurusan dengan suara, kita juga mungkin ingin menggunakan CNN untuk mencari pola tertentu dalam sinyal audio - dalam hal ini filter akan 1-dimensi (dan CNN ini akan disebut 1D-CNN). Juga, terkadang 3D-CNN digunakan untuk mengekstrak fitur di ruang multi-dimensi, seperti peristiwa tertentu yang terjadi di video - CNN dapat menangkap pola tertentu dari perubahan fitur seiring waktu. Lakukan beberapa tinjauan dan studi mandiri tentang tugas lain yang dapat dilakukan dengan CNN.

## [Tugas](lab/README.md)

Dalam lab ini, Anda ditugaskan untuk mengklasifikasikan berbagai ras kucing dan anjing. Gambar-gambar ini lebih kompleks daripada dataset MNIST dan memiliki dimensi yang lebih tinggi, dan ada lebih dari 10 kelas.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berkuasa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.