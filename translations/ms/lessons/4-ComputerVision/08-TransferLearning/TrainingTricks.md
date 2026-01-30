# Helah Latihan Pembelajaran Mendalam

Apabila rangkaian neural menjadi semakin mendalam, proses latihannya menjadi semakin mencabar. Salah satu masalah utama ialah apa yang dipanggil [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) atau [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Pos ini](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) memberikan pengenalan yang baik tentang masalah tersebut.

Untuk menjadikan latihan rangkaian mendalam lebih efisien, terdapat beberapa teknik yang boleh digunakan.

## Menjaga Nilai dalam Julat yang Wajar

Untuk menjadikan pengiraan numerik lebih stabil, kita perlu memastikan semua nilai dalam rangkaian neural berada dalam skala yang wajar, biasanya [-1..1] atau [0..1]. Ini bukanlah keperluan yang sangat ketat, tetapi sifat pengiraan titik terapung adalah sedemikian rupa sehingga nilai dengan magnitud berbeza tidak dapat dimanipulasi dengan tepat bersama-sama. Sebagai contoh, jika kita menambah 10<sup>-10</sup> dan 10<sup>10</sup>, kita mungkin akan mendapat 10<sup>10</sup>, kerana nilai yang lebih kecil akan "ditukar" kepada susunan yang sama seperti yang lebih besar, dan mantissa akan hilang.

Kebanyakan fungsi pengaktifan mempunyai ketaklinearan sekitar [-1..1], dan oleh itu masuk akal untuk menskalakan semua data input kepada julat [-1..1] atau [0..1].

## Inisialisasi Berat Awal

Secara ideal, kita mahu nilai berada dalam julat yang sama selepas melalui lapisan rangkaian. Oleh itu, adalah penting untuk memulakan berat dengan cara yang mengekalkan taburan nilai.

Taburan normal **N(0,1)** bukanlah idea yang baik, kerana jika kita mempunyai *n* input, sisihan piawai output akan menjadi *n*, dan nilai cenderung melompat keluar dari julat [0..1].

Inisialisasi berikut sering digunakan:

 * Taburan seragam -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** menjamin bahawa untuk input dengan purata sifar dan sisihan piawai 1, purata/sisihan piawai yang sama akan kekal
 * **N(0,√2/(n_in+n_out))** -- dipanggil **Xavier initialization** (`glorot`), ia membantu mengekalkan isyarat dalam julat semasa propagasi ke hadapan dan ke belakang

## Normalisasi Batch

Walaupun dengan inisialisasi berat yang betul, berat boleh menjadi sangat besar atau kecil semasa latihan, dan ini akan membawa isyarat keluar dari julat yang sesuai. Kita boleh membawa isyarat kembali dengan menggunakan salah satu teknik **normalisasi**. Walaupun terdapat beberapa teknik (Normalisasi Berat, Normalisasi Lapisan), yang paling kerap digunakan ialah Normalisasi Batch.

Idea **normalisasi batch** adalah untuk mengambil kira semua nilai merentasi minibatch, dan melakukan normalisasi (iaitu menolak purata dan membahagi dengan sisihan piawai) berdasarkan nilai-nilai tersebut. Ia dilaksanakan sebagai lapisan rangkaian yang melakukan normalisasi ini selepas menerapkan berat, tetapi sebelum fungsi pengaktifan. Hasilnya, kita cenderung melihat ketepatan akhir yang lebih tinggi dan latihan yang lebih cepat.

Berikut adalah [kertas asal](https://arxiv.org/pdf/1502.03167.pdf) tentang normalisasi batch, [penjelasan di Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), dan [pos blog pengenalan yang baik](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (dan satu lagi [dalam bahasa Rusia](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** adalah teknik menarik yang membuang peratusan tertentu neuron secara rawak semasa latihan. Ia juga dilaksanakan sebagai lapisan dengan satu parameter (peratusan neuron untuk dibuang, biasanya 10%-50%), dan semasa latihan ia menetapkan elemen rawak dalam vektor input kepada sifar sebelum menghantarnya ke lapisan seterusnya.

Walaupun ini mungkin kedengaran seperti idea yang pelik, anda boleh melihat kesan dropout pada latihan pengklasifikasi digit MNIST dalam buku nota [`Dropout.ipynb`](Dropout.ipynb). Ia mempercepatkan latihan dan membolehkan kita mencapai ketepatan yang lebih tinggi dalam bilangan epoch latihan yang lebih sedikit.

Kesan ini boleh dijelaskan dengan beberapa cara:

 * Ia boleh dianggap sebagai faktor kejutan rawak kepada model, yang membawa pengoptimuman keluar dari minimum tempatan
 * Ia boleh dianggap sebagai *penggabungan model secara tidak langsung*, kerana kita boleh mengatakan bahawa semasa dropout kita melatih model yang sedikit berbeza

> *Sesetengah orang mengatakan bahawa apabila seseorang yang mabuk cuba belajar sesuatu, dia akan mengingati ini dengan lebih baik keesokan paginya, berbanding dengan orang yang tidak mabuk, kerana otak dengan beberapa neuron yang tidak berfungsi cuba menyesuaikan diri dengan lebih baik untuk memahami maksudnya. Kami tidak pernah menguji sendiri sama ada ini benar atau tidak.*

## Mencegah Overfitting

Salah satu aspek yang sangat penting dalam pembelajaran mendalam ialah keupayaan untuk mencegah [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Walaupun mungkin menggoda untuk menggunakan model rangkaian neural yang sangat berkuasa, kita harus sentiasa mengimbangi bilangan parameter model dengan bilangan sampel latihan.

> Pastikan anda memahami konsep [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) yang telah kami perkenalkan sebelum ini!

Terdapat beberapa cara untuk mencegah overfitting:

 * Early stopping -- sentiasa memantau ralat pada set validasi dan menghentikan latihan apabila ralat validasi mula meningkat.
 * Explicit Weight Decay / Regularization -- menambah penalti tambahan kepada fungsi kehilangan untuk nilai mutlak berat yang tinggi, yang menghalang model daripada menghasilkan keputusan yang sangat tidak stabil
 * Model Averaging -- melatih beberapa model dan kemudian merata-rata hasilnya. Ini membantu meminimumkan varians.
 * Dropout (Implicit Model Averaging)

## Pengoptimum / Algoritma Latihan

Satu lagi aspek penting dalam latihan ialah memilih algoritma latihan yang baik. Walaupun **gradient descent** klasik adalah pilihan yang munasabah, ia kadangkala boleh menjadi terlalu perlahan, atau menyebabkan masalah lain.

Dalam pembelajaran mendalam, kita menggunakan **Stochastic Gradient Descent** (SGD), iaitu gradient descent yang digunakan pada minibatch yang dipilih secara rawak daripada set latihan. Berat disesuaikan menggunakan formula ini:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Dalam **momentum SGD**, kita mengekalkan sebahagian daripada kecerunan daripada langkah sebelumnya. Ia serupa dengan apabila kita bergerak ke suatu tempat dengan inersia, dan kita menerima hentakan ke arah yang berbeza, trajektori kita tidak berubah serta-merta, tetapi mengekalkan sebahagian daripada pergerakan asal. Di sini kita memperkenalkan vektor lain v untuk mewakili *kelajuan*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Di sini parameter γ menunjukkan sejauh mana kita mengambil kira inersia: γ=0 sepadan dengan SGD klasik; γ=1 adalah persamaan gerakan tulen.

### Adam, Adagrad, dll.

Oleh kerana dalam setiap lapisan kita mendarabkan isyarat dengan beberapa matriks W<sub>i</sub>, bergantung pada ||W<sub>i</sub>||, kecerunan boleh sama ada berkurangan dan hampir kepada 0, atau meningkat tanpa had. Ini adalah intipati masalah Exploding/Vanishing Gradients.

Salah satu penyelesaian kepada masalah ini ialah menggunakan hanya arah kecerunan dalam persamaan, dan mengabaikan nilai mutlak, iaitu

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), di mana ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Algoritma ini dipanggil **Adagrad**. Algoritma lain yang menggunakan idea yang sama: **RMSProp**, **Adam**

> **Adam** dianggap sebagai algoritma yang sangat efisien untuk banyak aplikasi, jadi jika anda tidak pasti mana yang hendak digunakan - gunakan Adam.

### Gradient clipping

Gradient clipping adalah lanjutan kepada idea di atas. Apabila ||∇ℒ|| ≤ θ, kita mempertimbangkan kecerunan asal dalam pengoptimuman berat, dan apabila ||∇ℒ|| > θ - kita membahagikan kecerunan dengan normanya. Di sini θ adalah parameter, dalam kebanyakan kes kita boleh mengambil θ=1 atau θ=10.

### Learning rate decay

Kejayaan latihan sering bergantung pada parameter kadar pembelajaran η. Adalah logik untuk menganggap bahawa nilai η yang lebih besar menghasilkan latihan yang lebih cepat, yang merupakan sesuatu yang biasanya kita mahukan pada permulaan latihan, dan kemudian nilai η yang lebih kecil membolehkan kita melaras rangkaian dengan lebih baik. Oleh itu, dalam kebanyakan kes kita mahu mengurangkan η dalam proses latihan.

Ini boleh dilakukan dengan mendarabkan η dengan beberapa nombor (contohnya 0.98) selepas setiap epoch latihan, atau dengan menggunakan **jadual kadar pembelajaran** yang lebih rumit.

## Pelbagai Seni Bina Rangkaian

Memilih seni bina rangkaian yang betul untuk masalah anda boleh menjadi rumit. Biasanya, kita akan mengambil seni bina yang telah terbukti berfungsi untuk tugas tertentu kita (atau yang serupa). Berikut adalah [tinjauan yang baik](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) tentang seni bina rangkaian neural untuk penglihatan komputer.

> Adalah penting untuk memilih seni bina yang cukup berkuasa untuk bilangan sampel latihan yang kita ada. Memilih model yang terlalu berkuasa boleh menyebabkan [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Cara lain yang baik ialah menggunakan seni bina yang akan menyesuaikan diri secara automatik dengan kerumitan yang diperlukan. Hingga tahap tertentu, seni bina **ResNet** dan **Inception** adalah bersifat menyesuaikan diri. [Maklumat lanjut tentang seni bina penglihatan komputer](../07-ConvNets/CNN_Architectures.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.