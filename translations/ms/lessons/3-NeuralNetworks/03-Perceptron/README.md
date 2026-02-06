# Pengenalan kepada Rangkaian Neural: Perceptron

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Salah satu usaha pertama untuk melaksanakan sesuatu yang serupa dengan rangkaian neural moden dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ia adalah pelaksanaan perkakasan yang dipanggil "Mark-1", direka untuk mengenali bentuk geometri primitif seperti segitiga, segi empat sama, dan bulatan.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/ms/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/ms/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Imej [dari Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Imej input diwakili oleh susunan fotocell 20x20, jadi rangkaian neural mempunyai 400 input dan satu output binari. Rangkaian mudah ini mengandungi satu neuron, yang juga dipanggil **threshold logic unit**. Berat rangkaian neural bertindak seperti potensiometer yang memerlukan pelarasan manual semasa fasa latihan.

> ✅ Potensiometer adalah alat yang membolehkan pengguna melaraskan rintangan dalam litar.

> The New York Times menulis tentang perceptron pada masa itu: *embrio komputer elektronik yang [Tentera Laut] jangka akan dapat berjalan, bercakap, melihat, menulis, membiak sendiri dan sedar akan kewujudannya.*

## Model Perceptron

Katakan kita mempunyai N ciri dalam model kita, di mana vektor input akan menjadi vektor bersaiz N. Perceptron adalah model **klasifikasi binari**, iaitu ia boleh membezakan antara dua kelas data input. Kita akan menganggap bahawa untuk setiap vektor input x, output perceptron kita akan sama ada +1 atau -1, bergantung pada kelas. Output akan dikira menggunakan formula:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi pengaktifan langkah

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/ms/activation-func.b4924007c7ce7764.webp"/>

## Melatih Perceptron

Untuk melatih perceptron, kita perlu mencari vektor berat w yang mengklasifikasikan kebanyakan nilai dengan betul, iaitu menghasilkan **ralat** yang paling kecil. Ralat E ini ditakrifkan oleh **kriteria perceptron** dengan cara berikut:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil pada titik data latihan i yang menghasilkan klasifikasi yang salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah sama ada -1 atau +1 untuk contoh negatif dan positif masing-masing.

Kriteria ini dianggap sebagai fungsi berat w, dan kita perlu meminimumkannya. Selalunya, kaedah yang dipanggil **gradient descent** digunakan, di mana kita bermula dengan beberapa berat awal w<sup>(0)</sup>, dan kemudian pada setiap langkah mengemas kini berat mengikut formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Di sini &eta; adalah **kadar pembelajaran**, dan &nabla;E(w) merujuk kepada **kecerunan** E. Selepas kita mengira kecerunan, kita akan mendapat

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritma dalam Python kelihatan seperti ini:

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

Dalam pelajaran ini, anda telah mempelajari tentang perceptron, iaitu model klasifikasi binari, dan cara melatihnya dengan menggunakan vektor berat.

## 🚀 Cabaran

Jika anda ingin mencuba membina perceptron anda sendiri, cuba [makmal ini di Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) yang menggunakan [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Ulasan & Kajian Kendiri

Untuk melihat bagaimana kita boleh menggunakan perceptron untuk menyelesaikan masalah mainan serta masalah kehidupan sebenar, dan untuk terus belajar - pergi ke notebook [Perceptron](Perceptron.ipynb).

Berikut adalah artikel menarik tentang [perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Tugasan](lab/README.md)

Dalam pelajaran ini, kita telah melaksanakan perceptron untuk tugas klasifikasi binari, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam makmal ini, anda diminta untuk menyelesaikan masalah klasifikasi digit sepenuhnya, iaitu menentukan digit mana yang paling mungkin sepadan dengan imej yang diberikan.

* [Arahan](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

