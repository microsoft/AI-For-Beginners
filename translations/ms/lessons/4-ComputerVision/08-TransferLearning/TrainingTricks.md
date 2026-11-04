# Petua Latihan Pembelajaran Mendalam

Apabila rangkaian neural menjadi lebih dalam, proses latihan mereka menjadi lebih mencabar. Satu masalah utama adalah apa yang dipanggil [kecerunan yang hilang](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) atau [kecerunan yang meletup](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Catatan ini](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) memberikan pengenalan yang baik kepada masalah tersebut.

Untuk menjadikan latihan rangkaian dalam lebih berkesan, terdapat beberapa teknik yang boleh digunakan.

## Mengekalkan nilai dalam julat yang munasabah

Untuk menjadikan pengiraan berangka lebih stabil, kita ingin memastikan semua nilai dalam rangkaian neural kita berada dalam skala yang munasabah, biasanya [-1..1] atau [0..1]. Ia bukan keperluan yang sangat ketat, tetapi sifat pengiraan titik apungan adalah sedemikian rupa sehingga nilai-nilai daripada magnitud yang berbeza tidak boleh dikendalikan bersama dengan tepat. Contohnya, jika kita menambah 10<sup>-10</sup> dan 10<sup>10</sup>, kita mungkin akan mendapat 10<sup>10</sup>, kerana nilai yang lebih kecil akan "ditukar" ke perintah yang sama dengan nilai yang lebih besar, dan dengan itu mantissa akan hilang.

Kebanyakan fungsi pengaktifan mempunyai bukan lineariti sekitar [-1..1], dan oleh itu masuk akal untuk menskala semua data input ke julat [-1..1] atau [0..1].

## Inisialisasi Berat Awal

Idealnya, kita mahu nilai berada dalam julat yang sama selepas melalui lapisan rangkaian. Oleh itu adalah penting untuk menginisialisasi berat sedemikian rupa agar mengawet taburan nilai.

Taburan normal **N(0,1)** bukanlah idea yang baik, kerana jika kita mempunyai *n* input, sisihan piawai output akan menjadi *&radic;n*, dan nilai mungkin melompat keluar dari julat [0..1].

Inisialisasi berikut kerap digunakan:

 * Taburan seragam -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** menjamin bahawa untuk input dengan min sifar dan sisihan piawai 1, min/sisihan piawai yang sama akan kekal
 * **N(0,&radic;2/(n_in+n_out))** -- dipanggil **inisialisasi Xavier** (`glorot`), ia membantu untuk mengekalkan isyarat dalam julat semasa penyebaran ke hadapan dan ke belakang

## Penormalan Kumpulan (Batch Normalization)

Walaupun dengan inisialisasi berat yang betul, berat boleh menjadi sangat besar atau kecil semasa latihan, dan ia akan membawa isyarat keluar dari julat yang betul. Kita boleh membawa isyarat kembali dengan menggunakan salah satu teknik **penormalan**. Walaupun terdapat beberapa daripadanya (Penormalan Berat, Penormalan Lapisan), yang paling kerap digunakan ialah Penormalan Kumpulan.

Idea **penormalan kumpulan** adalah untuk mengambil kira semua nilai merentas minibatch, dan melakukan penormalan (iaitu tolak min dan bahagi dengan sisihan piawai) berdasarkan nilai-nilai tersebut. Ia dilaksanakan sebagai lapisan rangkaian yang melakukan penormalan ini selepas menerapkan berat, tetapi sebelum fungsi pengaktifan. Akibatnya, kita mungkin melihat ketepatan akhir yang lebih tinggi dan latihan yang lebih cepat.

Berikut adalah [kertas asal](https://arxiv.org/pdf/1502.03167.pdf) mengenai penormalan kumpulan, [penjelasan di Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), dan [catatan blog pengenalan yang baik](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (dan yang [dalam bahasa Rusia](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** adalah teknik yang menarik yang mengeluarkan peratusan tertentu neuron secara rawak semasa latihan. Ia juga dilaksanakan sebagai lapisan dengan satu parameter (peratusan neuron yang dikeluarkan, biasanya 10%-50%), dan semasa latihan ia menetapkan elemen rawak dalam vektor input kepada sifar, sebelum meneruskannya ke lapisan seterusnya.

Walaupun ia mungkin kedengaran seperti idea yang pelik, anda boleh melihat kesan dropout ke atas latihan pengklasifikasi digit MNIST dalam buku nota [`Dropout.ipynb`](Dropout.ipynb). Ia mempercepatkan latihan dan membolehkan kita mencapai ketepatan yang lebih tinggi dalam lebih sedikit epok latihan.

Kesan ini boleh diterangkan dengan beberapa cara:

 * Ia boleh dianggap sebagai faktor kejutan rawak kepada model, yang mengeluarkan optimasi dari minimum lokal
 * Ia boleh dianggap sebagai *purata model tersirat*, kerana kita boleh katakan bahawa semasa dropout kita melatih model yang sedikit berbeza

> *Sesetengah orang berkata apabila seorang yang mabuk cuba belajar sesuatu, dia akan mengingatinya dengan lebih baik keesokan pagi, berbanding dengan orang yang sober, kerana otak dengan beberapa neuron yang tidak berfungsi cuba menyesuaikan diri dengan lebih baik untuk memahami maksud. Kami tidak pernah menguji sendiri sama ada ini benar atau tidak*

## Mencegah lebihan latihan (overfitting)

Salah satu aspek yang sangat penting dalam pembelajaran mendalam adalah untuk dapat mencegah [lebihan latihan](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Walaupun mungkin menggoda untuk menggunakan model rangkaian neural yang sangat berkuasa, kita harus sentiasa mengimbangkan bilangan parameter model dengan bilangan sampel latihan.

> Pastikan anda memahami konsep [lebihan latihan](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) yang telah kita perkenalkan sebelum ini!

Terdapat beberapa cara untuk mencegah lebihan latihan:

 * Hentian awal -- memantau secara berterusan ralat pada set pengesahan dan menghentikan latihan apabila ralat pengesahan mula meningkat.
 * Pengurangan Berat / Regularisasi Eksplisit -- menambah penalti tambahan pada fungsi rugi untuk nilai mutlak berat yang tinggi, yang mencegah model dari menghasilkan hasil yang sangat tidak stabil
 * Purata Model -- melatih beberapa model dan kemudian mengambil purata hasil. Ini membantu meminimumkan varians.
 * Dropout (Purata Model Tersirat)

## Pengoptimum / Algoritma Latihan

Aspek penting lain dalam latihan adalah memilih algoritma latihan yang baik. Walaupun **kecerunan menurun** klasik adalah pilihan munasabah, ia kadang kala boleh menjadi terlalu perlahan, atau membawa kepada masalah lain.

Dalam pembelajaran mendalam, kita menggunakan **Kecerunan Rawak Stokastik** (SGD), yang merupakan kecerunan menurun yang digunakan pada minibatch, dipilih secara rawak dari set latihan. Berat diselaraskan menggunakan formula ini:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Dalam **momentum SGD**, kita menyimpan sebahagian daripada kecerunan dari langkah sebelumnya. Ia serupa apabila kita bergerak ke suatu tempat dengan inersia, dan kita menerima hentakan ke arah yang berbeza, trajektori kita tidak berubah dengan segera, tetapi mengekalkan sebahagian daripada gerakan asal. Di sini kita memperkenalkan vektor lain v untuk mewakili *kelajuan*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parameter &gamma; menunjukkan sejauh mana kita mengambil kira inersia: &gamma;=0 bersamaan dengan SGD klasik; &gamma;=1 ialah persamaan pergerakan tulen.

### Adam, Adagrad, dan lain-lain

Oleh kerana di setiap lapisan kita mendarab isyarat oleh matriks W<sub>i</sub>, bergantung pada ||W<sub>i</sub>||, kecerunan boleh menjadi sangat kecil hingga hampir 0, atau meningkat tanpa had. Ini adalah inti masalah Kecerunan Meletup / Hilang.

Salah satu penyelesaian kepada masalah ini adalah menggunakan hanya arah kecerunan dalam persamaan, dan mengabaikan nilai mutlak, iaitu

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), di mana ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Algoritma ini dipanggil **Adagrad**. Algoritma lain yang menggunakan idea yang sama: **RMSProp**, **Adam**

> **Adam** dianggap sebagai algoritma yang sangat cekap untuk banyak aplikasi, jadi jika anda tidak pasti yang mana satu hendak digunakan - gunakan Adam.

### Pemotongan kecerunan

Pemotongan kecerunan adalah lanjutan dari idea di atas. Apabila ||&nabla;&lagran;|| &le; &theta;, kita menganggap kecerunan asal dalam pengoptimuman berat, dan apabila ||&nabla;&lagran;|| > &theta; - kita bahagi kecerunan dengan normanya. Di sini &theta; adalah parameter, dalam kebanyakan kes kita boleh mengambil &theta;=1 atau &theta;=10.

### Pengurangan kadar pembelajaran

Kejayaan latihan sering bergantung pada parameter kadar pembelajaran &eta;. Adalah logik untuk andaian bahawa nilai &eta; yang lebih besar menghasilkan latihan yang lebih cepat, yang biasanya kita mahukan pada permulaan latihan, dan kemudian nilai &eta; yang lebih kecil membolehkan kita memurnikan rangkaian. Oleh itu, dalam kebanyakan kes kita mahu mengurangkan &eta; dalam proses latihan.

Ini boleh dilakukan dengan mendarab &eta; dengan nombor tertentu (contohnya 0.98) selepas setiap epok latihan, atau dengan menggunakan **jadual kadar pembelajaran** yang lebih rumit.

## Arkitektur Rangkaian Berbeza

Memilih arkitektur rangkaian yang betul untuk masalah anda boleh menjadi sukar. Biasanya, kita akan mengambil arkitektur yang telah terbukti berfungsi untuk tugasan khusus kita (atau yang serupa). Berikut adalah [tinjauan yang baik](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) mengenai arkitektur rangkaian neural untuk penglihatan komputer.

> Penting untuk memilih arkitektur yang cukup berkuasa untuk bilangan sampel latihan yang kita ada. Memilih model yang terlalu berkuasa boleh mengakibatkan [lebihan latihan](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Cara baik lain ialah menggunakan arkitektur yang boleh menyesuaikan secara automatik dengan kerumitan yang diperlukan. Sehingga tahap tertentu, arkitektur **ResNet** dan **Inception** adalah menyesuaikan diri sendiri. [Lebih lanjut mengenai arkitektur penglihatan komputer](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->