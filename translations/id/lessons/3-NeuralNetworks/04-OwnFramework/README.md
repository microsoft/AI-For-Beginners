<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-29T12:34:58+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "id"
}
-->
# Pengantar Jaringan Neural. Multi-Layered Perceptron

Pada bagian sebelumnya, Anda telah mempelajari model jaringan neural paling sederhana - perceptron satu lapis, sebuah model klasifikasi linear dua kelas.

Pada bagian ini, kita akan memperluas model ini ke dalam kerangka kerja yang lebih fleksibel, memungkinkan kita untuk:

* melakukan **klasifikasi multi-kelas** selain dua kelas
* menyelesaikan **masalah regresi** selain klasifikasi
* memisahkan kelas yang tidak dapat dipisahkan secara linear

Kita juga akan mengembangkan kerangka kerja modular kita sendiri dalam Python yang memungkinkan kita untuk membangun berbagai arsitektur jaringan neural.

## [Kuis sebelum kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalisasi Pembelajaran Mesin

Mari kita mulai dengan memformalkan masalah Pembelajaran Mesin. Misalkan kita memiliki dataset pelatihan **X** dengan label **Y**, dan kita perlu membangun model *f* yang akan memberikan prediksi paling akurat. Kualitas prediksi diukur dengan **fungsi kerugian** ℒ. Fungsi kerugian berikut sering digunakan:

* Untuk masalah regresi, ketika kita perlu memprediksi sebuah angka, kita dapat menggunakan **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **0-1 loss** (yang pada dasarnya sama dengan **akurasi** model), atau **logistic loss**.

Untuk perceptron satu lapis, fungsi *f* didefinisikan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks bobot, *x* adalah vektor fitur input, dan *b* adalah vektor bias). Untuk berbagai arsitektur jaringan neural, fungsi ini dapat memiliki bentuk yang lebih kompleks.

> Dalam kasus klasifikasi, sering kali diinginkan untuk mendapatkan probabilitas kelas yang sesuai sebagai output jaringan. Untuk mengubah angka sembarang menjadi probabilitas (misalnya untuk menormalisasi output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* disebut **parameter** θ=⟨*w,b*⟩. Dengan dataset ⟨**X**,**Y**⟩, kita dapat menghitung keseluruhan error pada seluruh dataset sebagai fungsi dari parameter θ.

> ✅ **Tujuan pelatihan jaringan neural adalah untuk meminimalkan error dengan mengubah parameter θ**

## Optimasi Gradient Descent

Ada metode optimasi fungsi yang terkenal yang disebut **gradient descent**. Ide dasarnya adalah kita dapat menghitung turunan (dalam kasus multi-dimensi disebut **gradient**) dari fungsi kerugian terhadap parameter, dan mengubah parameter sedemikian rupa sehingga error berkurang. Ini dapat diformalkan sebagai berikut:

* Inisialisasi parameter dengan beberapa nilai acak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulangi langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Selama pelatihan, langkah-langkah optimasi seharusnya dihitung dengan mempertimbangkan seluruh dataset (ingat bahwa kerugian dihitung sebagai jumlah dari semua sampel pelatihan). Namun, dalam praktiknya kita mengambil bagian kecil dari dataset yang disebut **minibatches**, dan menghitung gradient berdasarkan subset data. Karena subset diambil secara acak setiap kali, metode ini disebut **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons dan Backpropagation

Jaringan satu lapis, seperti yang telah kita lihat di atas, mampu mengklasifikasikan kelas yang dapat dipisahkan secara linear. Untuk membangun model yang lebih kaya, kita dapat menggabungkan beberapa lapisan jaringan. Secara matematis, ini berarti bahwa fungsi *f* akan memiliki bentuk yang lebih kompleks, dan akan dihitung dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi aktivasi non-linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritma gradient descent tetap sama, tetapi akan lebih sulit untuk menghitung gradient. Berdasarkan aturan diferensiasi rantai, kita dapat menghitung turunan sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Aturan diferensiasi rantai digunakan untuk menghitung turunan fungsi kerugian terhadap parameter.

Perhatikan bahwa bagian paling kiri dari semua ekspresi tersebut sama, sehingga kita dapat secara efektif menghitung turunan mulai dari fungsi kerugian dan bergerak "mundur" melalui grafik komputasi. Oleh karena itu, metode pelatihan perceptron multi-lapis disebut **backpropagation**, atau 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: sitasi gambar

> ✅ Kita akan membahas backprop secara lebih rinci dalam contoh notebook kita.  

## Kesimpulan

Dalam pelajaran ini, kita telah membangun pustaka jaringan neural kita sendiri, dan kita telah menggunakannya untuk tugas klasifikasi dua dimensi yang sederhana.

## 🚀 Tantangan

Dalam notebook yang menyertai, Anda akan mengimplementasikan kerangka kerja Anda sendiri untuk membangun dan melatih perceptron multi-lapis. Anda akan dapat melihat secara rinci bagaimana jaringan neural modern beroperasi.

Lanjutkan ke notebook [OwnFramework](OwnFramework.ipynb) dan kerjakan.

## [Kuis setelah kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Tinjauan & Studi Mandiri

Backpropagation adalah algoritma umum yang digunakan dalam AI dan ML, yang layak dipelajari [lebih lanjut](https://wikipedia.org/wiki/Backpropagation)

## [Tugas](lab/README.md)

Dalam lab ini, Anda diminta untuk menggunakan kerangka kerja yang Anda bangun dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* [Instruksi](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.