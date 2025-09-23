<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-29T11:54:42+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural. Multi-Layered Perceptron

Dalam bahagian sebelumnya, anda telah mempelajari model rangkaian neural yang paling mudah - perceptron satu lapisan, iaitu model klasifikasi linear dua kelas.

Dalam bahagian ini, kita akan memperluaskan model ini kepada rangka kerja yang lebih fleksibel, membolehkan kita:

* melakukan **klasifikasi pelbagai kelas** selain daripada dua kelas
* menyelesaikan **masalah regresi** selain daripada klasifikasi
* memisahkan kelas yang tidak boleh dipisahkan secara linear

Kita juga akan membangunkan rangka kerja modular kita sendiri dalam Python yang membolehkan kita membina pelbagai seni bina rangkaian neural.

## [Kuiz pra-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalisasi Pembelajaran Mesin

Mari kita mulakan dengan memformalkan masalah Pembelajaran Mesin. Katakan kita mempunyai dataset latihan **X** dengan label **Y**, dan kita perlu membina model *f* yang akan membuat ramalan paling tepat. Kualiti ramalan diukur oleh **fungsi kerugian** ℒ. Fungsi kerugian berikut sering digunakan:

* Untuk masalah regresi, apabila kita perlu meramalkan nombor, kita boleh menggunakan **ralat mutlak** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **ralat kuasa dua** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **kerugian 0-1** (yang pada dasarnya sama seperti **ketepatan** model), atau **kerugian logistik**.

Untuk perceptron satu lapisan, fungsi *f* ditakrifkan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks berat, *x* adalah vektor ciri input, dan *b* adalah vektor bias). Untuk seni bina rangkaian neural yang berbeza, fungsi ini boleh mengambil bentuk yang lebih kompleks.

> Dalam kes klasifikasi, sering kali diinginkan untuk mendapatkan kebarangkalian kelas yang sepadan sebagai output rangkaian. Untuk menukar nombor sewenang-wenang kepada kebarangkalian (contohnya untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* dipanggil **parameter** θ=⟨*w,b*⟩. Diberikan dataset ⟨**X**,**Y**⟩, kita boleh mengira ralat keseluruhan pada keseluruhan dataset sebagai fungsi parameter θ.

> ✅ **Matlamat latihan rangkaian neural adalah untuk meminimumkan ralat dengan mengubah parameter θ**

## Pengoptimuman Gradient Descent

Terdapat kaedah pengoptimuman fungsi yang terkenal dipanggil **gradient descent**. Ideanya ialah kita boleh mengira derivatif (dalam kes berbilang dimensi dipanggil **gradien**) fungsi kerugian berkenaan dengan parameter, dan mengubah parameter sedemikian rupa sehingga ralat akan berkurangan. Ini boleh diformalkan seperti berikut:

* Inisialisasi parameter dengan beberapa nilai rawak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulang langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Semasa latihan, langkah pengoptimuman sepatutnya dikira dengan mempertimbangkan keseluruhan dataset (ingat bahawa kerugian dikira sebagai jumlah melalui semua sampel latihan). Walau bagaimanapun, dalam kehidupan sebenar kita mengambil bahagian kecil dataset yang dipanggil **minibatch**, dan mengira gradien berdasarkan subset data. Oleh kerana subset diambil secara rawak setiap kali, kaedah sedemikian dipanggil **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons dan Backpropagation

Rangkaian satu lapisan, seperti yang kita lihat di atas, mampu mengklasifikasikan kelas yang boleh dipisahkan secara linear. Untuk membina model yang lebih kaya, kita boleh menggabungkan beberapa lapisan rangkaian. Secara matematik, ini bermakna fungsi *f* akan mempunyai bentuk yang lebih kompleks, dan akan dikira dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi pengaktifan tidak linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritma gradient descent akan kekal sama, tetapi ia akan menjadi lebih sukar untuk mengira gradien. Berdasarkan peraturan pembezaan rantai, kita boleh mengira derivatif sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Peraturan pembezaan rantai digunakan untuk mengira derivatif fungsi kerugian berkenaan dengan parameter.

Perhatikan bahawa bahagian paling kiri semua ekspresi tersebut adalah sama, dan oleh itu kita boleh mengira derivatif dengan berkesan bermula daripada fungsi kerugian dan bergerak "ke belakang" melalui graf pengiraan. Oleh itu, kaedah latihan perceptron berbilang lapisan dipanggil **backpropagation**, atau 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: rujukan imej

> ✅ Kita akan membincangkan backprop dengan lebih terperinci dalam contoh notebook kita.  

## Kesimpulan

Dalam pelajaran ini, kita telah membina perpustakaan rangkaian neural kita sendiri, dan kita telah menggunakannya untuk tugas klasifikasi dua dimensi yang mudah.

## 🚀 Cabaran

Dalam notebook yang disertakan, anda akan melaksanakan rangka kerja anda sendiri untuk membina dan melatih perceptron berbilang lapisan. Anda akan dapat melihat secara terperinci bagaimana rangkaian neural moden beroperasi.

Teruskan ke notebook [OwnFramework](OwnFramework.ipynb) dan selesaikan latihan tersebut.

## [Kuiz pasca-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Kajian & Pembelajaran Kendiri

Backpropagation adalah algoritma biasa yang digunakan dalam AI dan ML, yang patut dikaji [dengan lebih terperinci](https://wikipedia.org/wiki/Backpropagation)

## [Tugasan](lab/README.md)

Dalam makmal ini, anda diminta menggunakan rangka kerja yang anda bina dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* [Arahan](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.