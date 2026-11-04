# Trik Pelatihan Deep Learning

Seiring dengan semakin dalamnya jaringan saraf, proses pelatihannya menjadi semakin menantang. Salah satu masalah utama adalah yang disebut [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) atau [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tulisan ini](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) memberikan pengantar yang baik tentang masalah-masalah tersebut.

Untuk membuat pelatihan jaringan dalam lebih efisien, ada beberapa teknik yang dapat digunakan.

## Menjaga nilai dalam interval yang masuk akal

Untuk membuat perhitungan numerik lebih stabil, kita ingin memastikan semua nilai dalam jaringan saraf berada dalam skala yang masuk akal, biasanya [-1..1] atau [0..1]. Ini bukan persyaratan yang sangat ketat, namun sifat perhitungan floating point adalah bahwa nilai dengan magnitudo berbeda tidak dapat dimanipulasi secara akurat bersama. Misalnya, jika kita menambahkan 10<sup>-10</sup> dan 10<sup>10</sup>, kita kemungkinan mendapatkan 10<sup>10</sup>, karena nilai yang lebih kecil akan "dikonversi" ke orde yang sama dengan nilai yang lebih besar, dan sehingga mantissa akan hilang.

Sebagian besar fungsi aktivasi memiliki non-linearitas di sekitar [-1..1], dan oleh karena itu masuk akal untuk mengskala semua data input ke interval [-1..1] atau [0..1].

## Inisialisasi Bobot Awal

Idealnya, kita ingin nilai berada dalam rentang yang sama setelah melewati lapisan jaringan. Oleh karena itu penting untuk menginisialisasi bobot sedemikian rupa agar mempertahankan distribusi nilai.

Distribusi normal **N(0,1)** bukan ide yang baik, karena jika kita memiliki *n* input, standar deviasi output akan menjadi *&radic;n*, dan nilai mungkin melompat keluar dari interval [0..1].

Inisialisasi berikut sering digunakan:

 * Distribusi uniform -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** menjamin bahwa untuk input dengan mean nol dan standar deviasi 1, mean/standar deviasi yang sama akan tetap ada
 * **N(0,&radic;2/(n_in+n_out))** -- yang disebut **inisialisasi Xavier** (`glorot`), membantu menjaga sinyal dalam rentang selama propagasi maju dan mundur

## Batch Normalization

Bahkan dengan inisialisasi bobot yang tepat, bobot bisa menjadi sangat besar atau kecil selama pelatihan, dan akan membuat sinyal keluar dari rentang yang tepat. Kita bisa mengembalikan sinyal dengan menggunakan salah satu teknik **normalisasi**. Ada beberapa di antaranya (Weight normalization, Layer Normalization), yang paling sering digunakan adalah Batch Normalization.

Ide **batch normalization** adalah untuk mempertimbangkan semua nilai di seluruh minibatch, dan melakukan normalisasi (yaitu mengurangi mean dan membagi dengan standar deviasi) berdasarkan nilai tersebut. Ini diimplementasikan sebagai lapisan jaringan yang melakukan normalisasi setelah penerapan bobot, namun sebelum fungsi aktivasi. Akibatnya, kita cenderung melihat akurasi akhir yang lebih tinggi dan pelatihan yang lebih cepat.

Ini adalah [makalah asli](https://arxiv.org/pdf/1502.03167.pdf) tentang batch normalization, [penjelasan di Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), dan [posting blog pengantar yang bagus](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (dan yang satu [dalam Bahasa Rusia](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** adalah teknik menarik yang menghilangkan persentase tertentu dari neuron secara acak selama pelatihan. Ini juga diimplementasikan sebagai lapisan dengan satu parameter (persentase neuron yang dihapus, biasanya 10%-50%), dan selama pelatihan itu meng-nol-kan elemen acak dari vektor input, sebelum meneruskannya ke lapisan berikutnya.

Meskipun ini terdengar seperti ide aneh, Anda dapat melihat efek dropout pada pelatihan pengklasifikasi digit MNIST di notebook [`Dropout.ipynb`](Dropout.ipynb). Ini mempercepat pelatihan dan memungkinkan kita mencapai akurasi lebih tinggi dalam lebih sedikit epoch pelatihan.

Efek ini dapat dijelaskan dengan beberapa cara:

 * Ini dapat dianggap sebagai faktor kejutan acak bagi model, yang mengeluarkan optimasi dari minimum lokal
 * Ini dapat dianggap sebagai *pemusatan model implisit*, karena kita dapat mengatakan bahwa selama dropout kita melatih model yang sedikit berbeda

> *Beberapa orang mengatakan bahwa ketika seseorang yang mabuk mencoba belajar sesuatu, dia akan lebih mengingatnya keesokan paginya dibandingkan orang yang sadar, karena otak dengan neuron yang berfungsi tidak sepenuhnya mencoba beradaptasi lebih baik untuk menangkap makna. Kami tidak pernah menguji sendiri apakah ini benar atau tidak*

## Mencegah overfitting

Salah satu aspek yang sangat penting dalam deep learning adalah kemampuan untuk mencegah [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Meskipun mungkin menggoda untuk menggunakan model jaringan saraf yang sangat kuat, kita harus selalu menyeimbangkan jumlah parameter model dengan jumlah sampel pelatihan.

> Pastikan Anda memahami konsep [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) yang sudah kami perkenalkan sebelumnya!

Ada beberapa cara untuk mencegah overfitting:

 * Early stopping -- memantau terus-menerus kesalahan pada set validasi dan menghentikan pelatihan saat kesalahan validasi mulai meningkat.
 * Explicit Weight Decay / Regularization -- menambahkan penalti ekstra pada fungsi kehilangan untuk nilai bobot absolut yang tinggi, yang mencegah model menghasilkan hasil yang sangat tidak stabil
 * Model Averaging -- melatih beberapa model dan kemudian meratakan hasilnya. Ini membantu meminimalkan varians.
 * Dropout (Pemodelan Rata-rata Implisit)

## Optimizer / Algoritma Pelatihan

Aspek penting lain dari pelatihan adalah memilih algoritma pelatihan yang baik. Meski **gradient descent** klasik adalah pilihan yang wajar, kadang kala bisa terlalu lambat, atau menimbulkan masalah lain.

Dalam deep learning, kita menggunakan **Stochastic Gradient Descent** (SGD), yaitu gradient descent yang diterapkan pada minibatch yang dipilih acak dari set pelatihan. Bobot disesuaikan menggunakan rumus:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Dalam **momentum SGD**, kita menyimpan sebagian dari gradien langkah sebelumnya. Ini mirip dengan ketika kita bergerak dengan inerasi, dan menerima pukulan ke arah berbeda, lintasan kita tidak langsung berubah, tetapi mempertahankan sebagian dari gerakan awal. Di sini kita memperkenalkan vektor lain v untuk mewakili *kecepatan*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parameter &gamma; menunjukkan sejauh mana kita mempertimbangkan inersia: &gamma;=0 sesuai dengan SGD klasik; &gamma;=1 adalah persamaan gerak murni.

### Adam, Adagrad, dll.

Karena di setiap lapisan kita mengalikan sinyal dengan beberapa matriks W<sub>i</sub>, tergantung pada ||W<sub>i</sub>||, gradien bisa mengecil mendekati 0, atau naik tak terbatas. Ini adalah inti dari masalah Exploding/Vanishing Gradients.

Salah satu solusi masalah ini adalah menggunakan hanya arah gradien dalam persamaan, dan mengabaikan nilai absolutnya, yaitu

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), di mana ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Algoritma ini disebut **Adagrad**. Algoritma lain yang menggunakan ide serupa: **RMSProp**, **Adam**

> **Adam** dianggap sebagai algoritma yang sangat efisien untuk banyak aplikasi, jadi jika Anda tidak yakin menggunakan yang mana - gunakan Adam.

### Gradient clipping

Gradient clipping adalah perpanjangan dari ide di atas. Ketika ||&nabla;&lagran;|| &le; &theta;, kita mempertimbangkan gradien asli dalam optimasi bobot, dan ketika ||&nabla;&lagran;|| > &theta; - kita membagi gradien dengan normanya. Di sini &theta; adalah parameter, dalam sebagian besar kasus kita bisa mengambil &theta;=1 atau &theta;=10.

### Penurunan learning rate

Keberhasilan pelatihan sering bergantung pada parameter learning rate &eta;. Logis untuk mengasumsikan bahwa nilai &eta; yang lebih besar menghasilkan pelatihan yang lebih cepat, yang biasanya kita inginkan di awal pelatihan, dan kemudian nilai &eta; yang lebih kecil memungkinkan penyetelan jaringan. Oleh karena itu, dalam sebagian besar kasus kita ingin menurunkan &eta; selama proses pelatihan.

Ini bisa dilakukan dengan mengalikan &eta; dengan angka tertentu (misalnya 0.98) setelah setiap epoch pelatihan, atau menggunakan **learning rate schedule** yang lebih rumit.

## Arsitektur Jaringan Berbeda

Memilih arsitektur jaringan yang tepat untuk masalah Anda bisa jadi sulit. Biasanya, kita akan mengambil arsitektur yang telah terbukti berhasil untuk tugas spesifik kita (atau yang serupa). Berikut ini adalah [ulasan bagus](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) mengenai arsitektur jaringan saraf untuk computer vision.

> Penting memilih arsitektur yang akan cukup kuat untuk jumlah sampel pelatihan yang kita miliki. Memilih model yang terlalu kuat bisa mengakibatkan [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Cara bagus lain adalah menggunakan arsitektur yang akan secara otomatis menyesuaikan dengan kompleksitas yang diperlukan. Sampai batas tertentu, arsitektur **ResNet** dan **Inception** adalah self-adjusting. [Lebih lanjut tentang arsitektur computer vision](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->