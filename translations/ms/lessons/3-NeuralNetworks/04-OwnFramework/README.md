# Pengenalan kepada Rangkaian Neural. Perceptron Berbilang Lapisan

Dalam bahagian sebelum ini, anda telah mempelajari tentang model rangkaian neural yang paling mudah - perceptron satu lapisan, sebuah model pengelasan dua kelas yang linear.

Dalam bahagian ini, kita akan memperluas model ini ke dalam rangka kerja yang lebih fleksibel, membolehkan kita untuk:

* melakukan **pengelasan berbilang kelas** di samping pengelasan dua kelas
* menyelesaikan **masalah regresi** di samping pengelasan
* memisahkan kelas yang tidak boleh dipisahkan secara linear

Kita juga akan membangunkan rangka kerja modular kita sendiri dalam Python yang akan membolehkan kita membina pelbagai seni bina rangkaian neural.

## [Kuis Pra-Lecture](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalisasi Pembelajaran Mesin

Mari kita mulakan dengan memformalkan masalah Pembelajaran Mesin. Anggap kita mempunyai dataset latihan **X** dengan label **Y**, dan kita perlu membina model *f* yang akan membuat ramalan yang paling tepat. Kualiti ramalan diukur dengan **Fungsi Kerugian** ℒ. Fungsi kerugian berikut sering digunakan:

* Untuk masalah regresi, apabila kita perlu meramalkan sebuah nombor, kita boleh menggunakan **kesilapan mutlak** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **kesilapan kuadrat** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk pengelasan, kita menggunakan **kerugian 0-1** (yang pada dasarnya sama dengan **ketepatan** model), atau **kerugian logistik**.

Untuk perceptron satu lapisan, fungsi *f* ditakrifkan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks berat, *x* adalah vektor ciri input, dan *b* adalah vektor bias). Untuk pelbagai seni bina rangkaian neural, fungsi ini boleh mengambil bentuk yang lebih kompleks.

> Dalam kes pengelasan, sering kali diinginkan untuk mendapatkan kebarangkalian kelas yang bersesuaian sebagai output rangkaian. Untuk menukar nombor yang sewenang-wenangnya kepada kebarangkalian (contohnya, untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* dipanggil **parameter** θ=⟨*w,b*⟩. Memandangkan dataset ⟨**X**,**Y**⟩, kita boleh mengira kesilapan keseluruhan pada keseluruhan dataset sebagai fungsi parameter θ.

> ✅ **Matlamat latihan rangkaian neural adalah untuk meminimumkan kesilapan dengan mengubah parameter θ**

## Pengoptimuman Penurunan Gradyen

Terdapat satu kaedah pengoptimuman fungsi yang terkenal dipanggil **penurunan gradyen**. Idea di sebalik ini adalah bahawa kita boleh mengira derivatif (dalam kes berbilang dimensi dipanggil **gradyen**) fungsi kerugian berkenaan dengan parameter, dan mengubah parameter sedemikian rupa sehingga kesilapan akan berkurang. Ini boleh diformalkan seperti berikut:

* Inisialisasi parameter dengan beberapa nilai rawak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulang langkah berikut banyak kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Semasa latihan, langkah pengoptimuman sepatutnya dikira dengan mempertimbangkan keseluruhan dataset (ingat bahawa kerugian dikira sebagai jumlah melalui semua sampel latihan). Walau bagaimanapun, dalam kehidupan sebenar, kita mengambil bahagian kecil dari dataset yang dipanggil **minibatches**, dan mengira gradyen berdasarkan subset data. Oleh kerana subset diambil secara rawak setiap kali, kaedah ini dipanggil **penurunan gradyen stokastik** (SGD).

## Perceptron Berbilang Lapisan dan Backpropagation

Rangkaian satu lapisan, seperti yang kita lihat di atas, mampu mengklasifikasikan kelas yang boleh dipisahkan secara linear. Untuk membina model yang lebih kaya, kita boleh menggabungkan beberapa lapisan rangkaian. Dari segi matematik, ini bermakna bahawa fungsi *f* akan mempunyai bentuk yang lebih kompleks, dan akan dikira dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi pengaktifan tidak linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*.

Algoritma penurunan gradyen akan kekal sama, tetapi lebih sukar untuk mengira gradyen. Dengan menggunakan peraturan pembezaan rantaian, kita boleh mengira derivatif sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Peraturan pembezaan rantaian digunakan untuk mengira derivatif fungsi kerugian berkenaan dengan parameter.

Perhatikan bahawa bahagian paling kiri dari semua ungkapan tersebut adalah sama, dan oleh itu kita boleh mengira derivatif secara berkesan bermula dari fungsi kerugian dan pergi "ke belakang" melalui graf pengiraan. Oleh itu, kaedah untuk melatih perceptron berbilang lapisan dipanggil **backpropagation**, atau 'backprop'.

<img alt="graf pengiraan" src="images/ComputeGraphGrad.png"/>

> TODO: petikan gambar

> ✅ Kita akan membincangkan backprop dengan lebih terperinci dalam contoh buku nota kita.  

## Kesimpulan

Dalam pelajaran ini, kita telah membina perpustakaan rangkaian neural kita sendiri, dan kita telah menggunakannya untuk tugas pengelasan dua dimensi yang mudah.

## 🚀 Cabaran

Dalam buku nota yang menyertainya, anda akan melaksanakan rangka kerja anda sendiri untuk membina dan melatih perceptron berbilang lapisan. Anda akan dapat melihat dengan lebih terperinci bagaimana rangkaian neural moden beroperasi.

Teruskan ke buku nota [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) dan kerjakan melalui itu.

## [Kuis Pasca-Lecture](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Ulasan & Pembelajaran Sendiri

Backpropagation adalah algoritma biasa yang digunakan dalam AI dan ML, berbaloi untuk dipelajari [dengan lebih terperinci](https://wikipedia.org/wiki/Backpropagation)

## [Tugasan](lab/README.md)

Dalam lab ini, anda diminta untuk menggunakan rangka kerja yang anda bina dalam pelajaran ini untuk menyelesaikan pengelasan digit tulisan tangan MNIST.

* [Arahan](lab/README.md)
* [Buku Nota](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.