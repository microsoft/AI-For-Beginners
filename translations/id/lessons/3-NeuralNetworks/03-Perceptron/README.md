# Pengantar Jaringan Neural: Perceptron

## [Kuis Pra-Pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Salah satu upaya pertama untuk mengimplementasikan sesuatu yang mirip dengan jaringan neural modern dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ini adalah implementasi perangkat keras yang disebut "Mark-1", dirancang untuk mengenali bentuk geometris sederhana, seperti segitiga, persegi, dan lingkaran.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/id/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/id/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Gambar [dari Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Gambar input direpresentasikan oleh array fotocell 20x20, sehingga jaringan neural memiliki 400 input dan satu output biner. Jaringan sederhana ini terdiri dari satu neuron, yang juga disebut sebagai **threshold logic unit**. Bobot jaringan neural berfungsi seperti potensiometer yang memerlukan penyesuaian manual selama fase pelatihan.

> ✅ Potensiometer adalah perangkat yang memungkinkan pengguna untuk mengatur resistansi dalam sebuah rangkaian.

> The New York Times menulis tentang perceptron pada saat itu: *embrio dari komputer elektronik yang [Angkatan Laut] harapkan akan dapat berjalan, berbicara, melihat, menulis, mereproduksi dirinya sendiri, dan sadar akan keberadaannya.*

## Model Perceptron

Misalkan kita memiliki N fitur dalam model kita, dalam hal ini vektor input akan menjadi vektor berukuran N. Perceptron adalah model **klasifikasi biner**, yaitu dapat membedakan antara dua kelas data input. Kita akan mengasumsikan bahwa untuk setiap vektor input x, output dari perceptron kita akan berupa +1 atau -1, tergantung pada kelasnya. Output akan dihitung menggunakan rumus:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi aktivasi langkah.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/id/activation-func.b4924007c7ce7764.webp"/>

## Melatih Perceptron

Untuk melatih perceptron, kita perlu menemukan vektor bobot w yang mengklasifikasikan sebagian besar nilai dengan benar, yaitu menghasilkan **error** terkecil. Error E ini didefinisikan oleh **kriteria perceptron** dengan cara berikut:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil dari titik data pelatihan i yang menghasilkan klasifikasi yang salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah -1 atau +1 untuk contoh negatif dan positif masing-masing.

Kriteria ini dianggap sebagai fungsi dari bobot w, dan kita perlu meminimalkannya. Sering kali, metode yang disebut **gradient descent** digunakan, di mana kita memulai dengan bobot awal w<sup>(0)</sup>, dan kemudian pada setiap langkah memperbarui bobot sesuai dengan rumus:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Di sini &eta; disebut sebagai **learning rate**, dan &nabla;E(w) menunjukkan **gradien** dari E. Setelah kita menghitung gradien, kita mendapatkan:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritma dalam Python terlihat seperti ini:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Kesimpulan

Dalam pelajaran ini, Anda telah mempelajari tentang perceptron, yang merupakan model klasifikasi biner, dan cara melatihnya dengan menggunakan vektor bobot.

## 🚀 Tantangan

Jika Anda ingin mencoba membangun perceptron sendiri, coba [lab ini di Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) yang menggunakan [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kuis Pasca-Pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Tinjauan & Studi Mandiri

Untuk melihat bagaimana kita dapat menggunakan perceptron untuk menyelesaikan masalah sederhana maupun masalah nyata, dan untuk melanjutkan pembelajaran - buka notebook [Perceptron](Perceptron.ipynb).

Berikut adalah [artikel menarik tentang perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) juga.

## [Tugas](lab/README.md)

Dalam pelajaran ini, kita telah mengimplementasikan perceptron untuk tugas klasifikasi biner, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam lab ini, Anda diminta untuk menyelesaikan masalah klasifikasi digit sepenuhnya, yaitu menentukan digit mana yang paling mungkin sesuai dengan gambar yang diberikan.

* [Instruksi](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

