<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-29T11:55:11+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural: Perceptron

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Salah satu percubaan pertama untuk melaksanakan sesuatu yang serupa dengan rangkaian neural moden dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ia adalah pelaksanaan perkakasan yang dipanggil "Mark-1", direka untuk mengenali bentuk geometri primitif, seperti segitiga, segi empat sama, dan bulatan.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imej [daripada Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Imej input diwakili oleh susunan fotocell 20x20, jadi rangkaian neural mempunyai 400 input dan satu output binari. Rangkaian mudah ini mengandungi satu neuron, yang juga dipanggil sebagai **unit logik ambang**. Berat rangkaian neural bertindak seperti potensiometer yang memerlukan pelarasan manual semasa fasa latihan.

> ✅ Potensiometer ialah alat yang membolehkan pengguna melaraskan rintangan dalam litar.

> The New York Times menulis tentang perceptron pada masa itu: *embrio komputer elektronik yang [Tentera Laut] jangka akan dapat berjalan, bercakap, melihat, menulis, membiak sendiri dan sedar akan kewujudannya.*

## Model Perceptron

Katakan kita mempunyai N ciri dalam model kita, di mana vektor input akan menjadi vektor bersaiz N. Perceptron ialah model **klasifikasi binari**, iaitu ia boleh membezakan antara dua kelas data input. Kita akan mengandaikan bahawa untuk setiap vektor input x, output perceptron kita akan sama ada +1 atau -1, bergantung pada kelasnya. Output akan dikira menggunakan formula:

y(x) = f(w<sup>T</sup>x)

di mana f ialah fungsi pengaktifan langkah

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Melatih Perceptron

Untuk melatih perceptron, kita perlu mencari vektor berat w yang mengklasifikasikan kebanyakan nilai dengan betul, iaitu menghasilkan **ralat** terkecil. Ralat E ini ditakrifkan oleh **kriteria perceptron** seperti berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil pada titik data latihan i yang menghasilkan klasifikasi salah
* x<sub>i</sub> ialah data input, dan t<sub>i</sub> ialah sama ada -1 atau +1 untuk contoh negatif dan positif masing-masing.

Kriteria ini dianggap sebagai fungsi berat w, dan kita perlu meminimumkannya. Selalunya, kaedah yang dipanggil **penurunan kecerunan** digunakan, di mana kita bermula dengan beberapa berat awal w<sup>(0)</sup>, dan kemudian pada setiap langkah mengemas kini berat mengikut formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η dipanggil **kadar pembelajaran**, dan ∇E(w) menunjukkan **kecerunan** E. Selepas kita mengira kecerunan, kita akan mendapat

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

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

Dalam pelajaran ini, anda telah mempelajari tentang perceptron, yang merupakan model klasifikasi binari, dan cara melatihnya dengan menggunakan vektor berat.

## 🚀 Cabaran

Jika anda ingin mencuba membina perceptron anda sendiri, cuba [makmal ini di Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) yang menggunakan [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Ulasan & Kajian Kendiri

Untuk melihat bagaimana kita boleh menggunakan perceptron untuk menyelesaikan masalah mainan serta masalah dunia sebenar, dan untuk terus belajar - pergi ke buku nota [Perceptron](Perceptron.ipynb).

Berikut adalah [artikel menarik tentang perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) juga.

## [Tugasan](lab/README.md)

Dalam pelajaran ini, kita telah melaksanakan perceptron untuk tugas klasifikasi binari, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam makmal ini, anda diminta untuk menyelesaikan masalah klasifikasi digit sepenuhnya, iaitu menentukan digit mana yang paling mungkin sepadan dengan imej yang diberikan.

* [Arahan](lab/README.md)
* [Buku Nota](lab/PerceptronMultiClass.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.