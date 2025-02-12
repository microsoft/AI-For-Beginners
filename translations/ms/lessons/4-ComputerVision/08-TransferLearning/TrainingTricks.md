# Trik Latihan Pembelajaran Dalam

Seiring dengan semakin dalamnya jaringan saraf, proses pelatihannya menjadi semakin menantang. Salah satu masalah utama adalah yang disebut [gradien menghilang](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) atau [gradien meledak](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Posting ini](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) memberikan pengantar yang baik tentang masalah ini.

Untuk membuat pelatihan jaringan dalam lebih efisien, ada beberapa teknik yang dapat digunakan.

## Menjaga nilai dalam interval yang wajar

Untuk membuat perhitungan numerik lebih stabil, kita ingin memastikan bahwa semua nilai dalam jaringan saraf kita berada dalam skala yang wajar, biasanya [-1..1] atau [0..1]. Ini bukan persyaratan yang sangat ketat, tetapi sifat perhitungan titik mengambang adalah demikian sehingga nilai dengan magnitudo yang berbeda tidak dapat dimanipulasi secara akurat bersama-sama. Sebagai contoh, jika kita menjumlahkan 10<sup>-10</sup> dan 10<sup>10</sup>, kita kemungkinan besar akan mendapatkan 10<sup>10</sup>, karena nilai yang lebih kecil akan "dikonversi" ke urutan yang sama dengan yang lebih besar, sehingga mantissa akan hilang.

Sebagian besar fungsi aktivasi memiliki non-linearitas di sekitar [-1..1], sehingga masuk akal untuk menskalakan semua data input ke interval [-1..1] atau [0..1].

## Inisialisasi Bobot Awal

Idealnya, kita ingin nilai-nilai berada dalam rentang yang sama setelah melewati lapisan jaringan. Oleh karena itu, penting untuk menginisialisasi bobot dengan cara yang mempertahankan distribusi nilai.

Distribusi normal **N(0,1)** bukanlah ide yang baik, karena jika kita memiliki *n* input, deviasi standar output akan menjadi *n*, dan nilai-nilai kemungkinan besar akan melampaui interval [0..1].

Inisialisasi berikut sering digunakan:

 * Distribusi seragam -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** menjamin bahwa untuk input dengan rata-rata nol dan deviasi standar 1, rata-rata/deviasi standar yang sama akan tetap ada
 * **N(0,√2/(n_in+n_out))** -- yang disebut **inisialisasi Xavier** (`glorot`), ini membantu menjaga sinyal dalam rentang selama propagasi maju dan mundur

## Normalisasi Batch

Bahkan dengan inisialisasi bobot yang tepat, bobot dapat menjadi sangat besar atau kecil selama pelatihan, dan ini akan membawa sinyal keluar dari rentang yang tepat. Kita dapat mengembalikan sinyal dengan menggunakan salah satu teknik **normalisasi**. Meskipun ada beberapa di antaranya (Normalisasi Bobot, Normalisasi Lapisan), yang paling sering digunakan adalah Normalisasi Batch.

Ide dari **normalisasi batch** adalah untuk mempertimbangkan semua nilai di seluruh minibatch, dan melakukan normalisasi (yaitu mengurangi rata-rata dan membagi dengan deviasi standar) berdasarkan nilai-nilai tersebut. Ini diimplementasikan sebagai lapisan jaringan yang melakukan normalisasi ini setelah menerapkan bobot, tetapi sebelum fungsi aktivasi. Sebagai hasilnya, kita kemungkinan besar akan melihat akurasi akhir yang lebih tinggi dan pelatihan yang lebih cepat.

Berikut adalah [makalah asli](https://arxiv.org/pdf/1502.03167.pdf) tentang normalisasi batch, [penjelasan di Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), dan [posting blog pengantar yang baik](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (dan yang satu [dalam bahasa Rusia](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** adalah teknik menarik yang menghapus persentase neuron acak tertentu selama pelatihan. Ini juga diimplementasikan sebagai lapisan dengan satu parameter (persentase neuron yang akan dihapus, biasanya 10%-50%), dan selama pelatihan, ia mengosongkan elemen acak dari vektor input, sebelum meneruskannya ke lapisan berikutnya.

Meskipun ini mungkin terdengar seperti ide yang aneh, Anda dapat melihat efek dropout pada pelatihan pengklasifikasi digit MNIST dalam [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) notebook. Ini mempercepat pelatihan dan memungkinkan kita mencapai akurasi yang lebih tinggi dalam lebih sedikit epoch pelatihan.

Efek ini dapat dijelaskan dengan beberapa cara:

 * Ini dapat dianggap sebagai faktor kejutan acak bagi model, yang mengeluarkan optimasi dari minimum lokal
 * Ini dapat dianggap sebagai *rata-rata model implisit*, karena kita dapat mengatakan bahwa selama dropout kita sedang melatih model yang sedikit berbeda

> *Beberapa orang mengatakan bahwa ketika seseorang yang mabuk mencoba belajar sesuatu, dia akan mengingatnya lebih baik keesokan paginya, dibandingkan dengan orang yang sadar, karena otak dengan beberapa neuron yang tidak berfungsi mencoba beradaptasi lebih baik untuk memahami makna. Kami tidak pernah menguji sendiri apakah ini benar atau tidak*

## Mencegah Overfitting

Salah satu aspek yang sangat penting dari pembelajaran dalam adalah mampu mencegah [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Meskipun mungkin menggoda untuk menggunakan model jaringan saraf yang sangat kuat, kita harus selalu menyeimbangkan jumlah parameter model dengan jumlah sampel pelatihan.

> Pastikan Anda memahami konsep [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) yang telah kami perkenalkan sebelumnya!

Ada beberapa cara untuk mencegah overfitting:

 * Penghentian dini -- terus-menerus memantau kesalahan pada set validasi dan menghentikan pelatihan ketika kesalahan validasi mulai meningkat.
 * Penurunan Bobot Eksplisit / Regulasi -- menambahkan penalti ekstra pada fungsi kerugian untuk nilai absolut bobot yang tinggi, yang mencegah model mendapatkan hasil yang sangat tidak stabil
 * Rata-rata Model -- melatih beberapa model dan kemudian merata-ratakan hasilnya. Ini membantu meminimalkan varians.
 * Dropout (Rata-rata Model Implisit)

## Pengoptimal / Algoritma Pelatihan

Aspek penting lain dari pelatihan adalah memilih algoritma pelatihan yang baik. Meskipun **penurunan gradien** klasik adalah pilihan yang wajar, terkadang bisa terlalu lambat, atau menghasilkan masalah lainnya.

Dalam pembelajaran dalam, kita menggunakan **Stochastic Gradient Descent** (SGD), yang merupakan penurunan gradien yang diterapkan pada minibatch, yang dipilih secara acak dari set pelatihan. Bobot disesuaikan menggunakan rumus ini:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Dalam **momentum SGD**, kita menyimpan sebagian gradien dari langkah sebelumnya. Ini mirip dengan ketika kita bergerak ke suatu tempat dengan inersia, dan kita menerima dorongan ke arah yang berbeda, trajektori kita tidak berubah segera, tetapi mempertahankan sebagian dari gerakan awal. Di sini kita memperkenalkan vektor lain v untuk mewakili *kecepatan*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Di sini parameter γ menunjukkan sejauh mana kita mempertimbangkan inersia: γ=0 sesuai dengan SGD klasik; γ=1 adalah persamaan gerakan murni.

### Adam, Adagrad, dll.

Karena di setiap lapisan kita mengalikan sinyal dengan beberapa matriks W<sub>i</sub>, tergantung pada ||W<sub>i</sub>||, gradien dapat berkurang dan mendekati 0, atau meningkat tanpa batas. Ini adalah inti dari masalah Gradien Meledak/Menghilang.

Salah satu solusi untuk masalah ini adalah dengan menggunakan hanya arah gradien dalam persamaan, dan mengabaikan nilai absolut, yaitu:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), di mana ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Algoritma ini disebut **Adagrad**. Algoritma lain yang menggunakan ide yang sama: **RMSProp**, **Adam**

> **Adam** dianggap sebagai algoritma yang sangat efisien untuk banyak aplikasi, jadi jika Anda tidak yakin yang mana yang harus digunakan - gunakan Adam.

### Pemotongan Gradien

Pemotongan gradien adalah perpanjangan dari ide di atas. Ketika ||∇ℒ|| ≤ θ, kita mempertimbangkan gradien asli dalam optimasi bobot, dan ketika ||∇ℒ|| > θ - kita membagi gradien dengan normanya. Di sini θ adalah parameter, dalam kebanyakan kasus kita dapat mengambil θ=1 atau θ=10.

### Penurunan laju pembelajaran

Keberhasilan pelatihan sering kali bergantung pada parameter laju pembelajaran η. Logis untuk mengasumsikan bahwa nilai η yang lebih besar menghasilkan pelatihan yang lebih cepat, yang biasanya kita inginkan di awal pelatihan, dan kemudian nilai η yang lebih kecil memungkinkan kita untuk menyempurnakan jaringan. Oleh karena itu, dalam kebanyakan kasus, kita ingin mengurangi η selama proses pelatihan.

Ini dapat dilakukan dengan mengalikan η dengan beberapa angka (misalnya, 0.98) setelah setiap epoch pelatihan, atau dengan menggunakan **jadwal laju pembelajaran** yang lebih rumit.

## Arsitektur Jaringan yang Berbeda

Memilih arsitektur jaringan yang tepat untuk masalah Anda bisa jadi rumit. Normalnya, kita akan mengambil arsitektur yang telah terbukti berhasil untuk tugas spesifik kita (atau yang serupa). Berikut adalah [tinjauan yang baik](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) tentang arsitektur jaringan saraf untuk visi komputer.

> Penting untuk memilih arsitektur yang cukup kuat untuk jumlah sampel pelatihan yang kita miliki. Memilih model yang terlalu kuat dapat mengakibatkan [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Cara lain yang baik adalah menggunakan arsitektur yang secara otomatis akan menyesuaikan dengan kompleksitas yang diperlukan. Sampai batas tertentu, arsitektur **ResNet** dan **Inception** bersifat penyesuaian diri. [Lebih lanjut tentang arsitektur visi komputer](../07-ConvNets/CNN_Architectures.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat kritikal, terjemahan manusia yang profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.