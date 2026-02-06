# Trik Pelatihan Deep Learning

Saat jaringan neural menjadi semakin dalam, proses pelatihannya menjadi semakin menantang. Salah satu masalah utama adalah yang disebut [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) atau [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Postingan ini](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) memberikan pengantar yang baik tentang masalah tersebut.

Untuk membuat pelatihan jaringan yang dalam lebih efisien, ada beberapa teknik yang dapat digunakan.

## Menjaga Nilai dalam Interval yang Wajar

Untuk membuat perhitungan numerik lebih stabil, kita ingin memastikan bahwa semua nilai dalam jaringan neural kita berada dalam skala yang wajar, biasanya [-1..1] atau [0..1]. Ini bukan persyaratan yang sangat ketat, tetapi sifat perhitungan floating point adalah bahwa nilai dengan magnitudo berbeda tidak dapat dimanipulasi secara akurat bersama-sama. Sebagai contoh, jika kita menambahkan 10<sup>-10</sup> dan 10<sup>10</sup>, kemungkinan besar kita akan mendapatkan 10<sup>10</sup>, karena nilai yang lebih kecil akan "diubah" ke urutan yang sama dengan yang lebih besar, sehingga mantissa akan hilang.

Sebagian besar fungsi aktivasi memiliki non-linearitas di sekitar [-1..1], sehingga masuk akal untuk menskalakan semua data input ke interval [-1..1] atau [0..1].

## Inisialisasi Bobot Awal

Idealnya, kita ingin nilai tetap berada dalam rentang yang sama setelah melewati lapisan jaringan. Oleh karena itu, penting untuk menginisialisasi bobot sedemikian rupa sehingga distribusi nilai tetap terjaga.

Distribusi normal **N(0,1)** bukanlah ide yang baik, karena jika kita memiliki *n* input, standar deviasi output akan menjadi *n*, dan nilai kemungkinan besar akan melompat keluar dari interval [0..1].

Inisialisasi berikut sering digunakan:

- Distribusi uniform -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** menjamin bahwa untuk input dengan rata-rata nol dan standar deviasi 1, rata-rata/standar deviasi yang sama akan tetap ada
- **N(0,√2/(n_in+n_out))** -- yang disebut **Xavier initialization** (`glorot`), membantu menjaga sinyal tetap dalam rentang selama propagasi maju dan mundur

## Normalisasi Batch

Bahkan dengan inisialisasi bobot yang tepat, bobot dapat menjadi sangat besar atau kecil selama pelatihan, dan ini akan membawa sinyal keluar dari rentang yang sesuai. Kita dapat mengembalikan sinyal ke rentang yang sesuai dengan menggunakan salah satu teknik **normalisasi**. Meskipun ada beberapa teknik (Normalisasi Bobot, Normalisasi Lapisan), yang paling sering digunakan adalah Normalisasi Batch.

Ide dari **normalisasi batch** adalah mempertimbangkan semua nilai di seluruh minibatch, dan melakukan normalisasi (misalnya mengurangi rata-rata dan membagi dengan standar deviasi) berdasarkan nilai-nilai tersebut. Ini diimplementasikan sebagai lapisan jaringan yang melakukan normalisasi ini setelah menerapkan bobot, tetapi sebelum fungsi aktivasi. Hasilnya, kita cenderung melihat akurasi akhir yang lebih tinggi dan pelatihan yang lebih cepat.

Berikut adalah [makalah asli](https://arxiv.org/pdf/1502.03167.pdf) tentang normalisasi batch, [penjelasan di Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), dan [postingan blog pengantar yang baik](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (dan yang [dalam bahasa Rusia](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** adalah teknik menarik yang menghapus persentase tertentu dari neuron secara acak selama pelatihan. Ini juga diimplementasikan sebagai lapisan dengan satu parameter (persentase neuron yang dihapus, biasanya 10%-50%), dan selama pelatihan, elemen-elemen acak dari vektor input di-nol-kan sebelum diteruskan ke lapisan berikutnya.

Meskipun ini mungkin terdengar seperti ide yang aneh, Anda dapat melihat efek dropout pada pelatihan pengklasifikasi digit MNIST di notebook [`Dropout.ipynb`](Dropout.ipynb). Ini mempercepat pelatihan dan memungkinkan kita mencapai akurasi yang lebih tinggi dalam lebih sedikit epoch pelatihan.

Efek ini dapat dijelaskan dengan beberapa cara:

- Ini dapat dianggap sebagai faktor kejutan acak untuk model, yang membawa optimasi keluar dari minimum lokal
- Ini dapat dianggap sebagai *model averaging implisit*, karena kita dapat mengatakan bahwa selama dropout kita melatih model yang sedikit berbeda

> *Beberapa orang mengatakan bahwa ketika seseorang yang mabuk mencoba belajar sesuatu, dia akan mengingatnya lebih baik keesokan paginya dibandingkan dengan orang yang sadar, karena otak dengan beberapa neuron yang tidak berfungsi mencoba beradaptasi lebih baik untuk memahami makna. Kami tidak pernah menguji sendiri apakah ini benar atau tidak*

## Mencegah Overfitting

Salah satu aspek yang sangat penting dalam deep learning adalah kemampuan untuk mencegah [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Meskipun mungkin menggoda untuk menggunakan model jaringan neural yang sangat kuat, kita harus selalu menyeimbangkan jumlah parameter model dengan jumlah sampel pelatihan.

> Pastikan Anda memahami konsep [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) yang telah kami perkenalkan sebelumnya!

Ada beberapa cara untuk mencegah overfitting:

- Early stopping -- secara terus-menerus memantau error pada set validasi dan menghentikan pelatihan ketika error validasi mulai meningkat.
- Explicit Weight Decay / Regularization -- menambahkan penalti ekstra ke fungsi loss untuk nilai absolut bobot yang tinggi, yang mencegah model menghasilkan hasil yang sangat tidak stabil
- Model Averaging -- melatih beberapa model dan kemudian merata-ratakan hasilnya. Ini membantu meminimalkan variansi.
- Dropout (Implicit Model Averaging)

## Optimizer / Algoritma Pelatihan

Aspek penting lainnya dari pelatihan adalah memilih algoritma pelatihan yang baik. Meskipun **gradient descent** klasik adalah pilihan yang masuk akal, terkadang ini bisa terlalu lambat atau menyebabkan masalah lainnya.

Dalam deep learning, kita menggunakan **Stochastic Gradient Descent** (SGD), yang merupakan gradient descent yang diterapkan pada minibatch yang dipilih secara acak dari set pelatihan. Bobot disesuaikan menggunakan formula ini:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Dalam **momentum SGD**, kita mempertahankan sebagian gradien dari langkah sebelumnya. Ini mirip dengan ketika kita bergerak ke suatu arah dengan inersia, dan kita menerima dorongan ke arah yang berbeda, lintasan kita tidak langsung berubah, tetapi tetap mempertahankan sebagian dari gerakan awal. Di sini kita memperkenalkan vektor lain v untuk mewakili *kecepatan*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Di sini parameter γ menunjukkan sejauh mana kita mempertimbangkan inersia: γ=0 sesuai dengan SGD klasik; γ=1 adalah persamaan gerak murni.

### Adam, Adagrad, dll.

Karena di setiap lapisan kita mengalikan sinyal dengan beberapa matriks W<sub>i</sub>, tergantung pada ||W<sub>i</sub>||, gradien dapat mengecil dan mendekati 0, atau meningkat tanpa batas. Ini adalah inti dari masalah Exploding/Vanishing Gradients.

Salah satu solusi untuk masalah ini adalah hanya menggunakan arah gradien dalam persamaan, dan mengabaikan nilai absolutnya, yaitu:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), di mana ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Algoritma ini disebut **Adagrad**. Algoritma lain yang menggunakan ide yang sama: **RMSProp**, **Adam**

> **Adam** dianggap sebagai algoritma yang sangat efisien untuk banyak aplikasi, jadi jika Anda tidak yakin mana yang harus digunakan - gunakan Adam.

### Gradient clipping

Gradient clipping adalah perpanjangan dari ide di atas. Ketika ||∇ℒ|| ≤ θ, kita mempertimbangkan gradien asli dalam optimasi bobot, dan ketika ||∇ℒ|| > θ - kita membagi gradien dengan normanya. Di sini θ adalah parameter, dalam banyak kasus kita dapat mengambil θ=1 atau θ=10.

### Learning rate decay

Keberhasilan pelatihan sering kali bergantung pada parameter learning rate η. Logis untuk mengasumsikan bahwa nilai η yang lebih besar menghasilkan pelatihan yang lebih cepat, yang biasanya kita inginkan di awal pelatihan, dan kemudian nilai η yang lebih kecil memungkinkan kita untuk menyempurnakan jaringan. Oleh karena itu, dalam sebagian besar kasus kita ingin mengurangi η dalam proses pelatihan.

Ini dapat dilakukan dengan mengalikan η dengan beberapa angka (misalnya 0.98) setelah setiap epoch pelatihan, atau dengan menggunakan **learning rate schedule** yang lebih rumit.

## Arsitektur Jaringan yang Berbeda

Memilih arsitektur jaringan yang tepat untuk masalah Anda bisa menjadi hal yang rumit. Biasanya, kita akan memilih arsitektur yang telah terbukti bekerja untuk tugas spesifik kita (atau yang serupa). Berikut adalah [ikhtisar yang baik](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) tentang arsitektur jaringan neural untuk computer vision.

> Penting untuk memilih arsitektur yang cukup kuat untuk jumlah sampel pelatihan yang kita miliki. Memilih model yang terlalu kuat dapat menyebabkan [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Cara lain yang baik adalah menggunakan arsitektur yang akan secara otomatis menyesuaikan dengan kompleksitas yang diperlukan. Sampai batas tertentu, arsitektur **ResNet** dan **Inception** bersifat self-adjusting. [Lebih lanjut tentang arsitektur computer vision](../07-ConvNets/CNN_Architectures.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.