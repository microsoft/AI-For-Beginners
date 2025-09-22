<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-29T12:35:58+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "id"
}
-->
# Pengantar Jaringan Saraf: Perceptron

## [Kuis Pra-Pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Salah satu upaya pertama untuk mengimplementasikan sesuatu yang mirip dengan jaringan saraf modern dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ini adalah implementasi perangkat keras yang disebut "Mark-1", dirancang untuk mengenali bentuk geometris sederhana, seperti segitiga, persegi, dan lingkaran.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Gambar [dari Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Gambar input direpresentasikan oleh array fotocell 20x20, sehingga jaringan saraf memiliki 400 input dan satu output biner. Jaringan sederhana ini hanya memiliki satu neuron, yang juga disebut sebagai **threshold logic unit**. Bobot jaringan saraf bertindak seperti potensiometer yang memerlukan penyesuaian manual selama fase pelatihan.

> ✅ Potensiometer adalah perangkat yang memungkinkan pengguna untuk mengatur resistansi dalam sebuah rangkaian.

> The New York Times menulis tentang perceptron pada waktu itu: *embrio dari komputer elektronik yang [Angkatan Laut] harapkan akan mampu berjalan, berbicara, melihat, menulis, mereproduksi dirinya sendiri, dan sadar akan keberadaannya.*

## Model Perceptron

Misalkan kita memiliki N fitur dalam model kita, sehingga vektor input akan menjadi vektor berukuran N. Perceptron adalah model **klasifikasi biner**, yaitu dapat membedakan antara dua kelas data input. Kita akan mengasumsikan bahwa untuk setiap vektor input x, output dari perceptron kita akan berupa +1 atau -1, tergantung pada kelasnya. Output dihitung menggunakan rumus:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi aktivasi step

<img src="images/activation-func.png"/>

## Melatih Perceptron

Untuk melatih perceptron, kita perlu menemukan vektor bobot w yang mengklasifikasikan sebagian besar nilai dengan benar, yaitu menghasilkan **error** terkecil. Error E ini didefinisikan oleh **kriteria perceptron** sebagai berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* Penjumlahan dilakukan pada titik data pelatihan i yang menghasilkan klasifikasi salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah -1 atau +1 untuk contoh negatif dan positif masing-masing.

Kriteria ini dianggap sebagai fungsi dari bobot w, dan kita perlu meminimalkannya. Seringkali, metode yang disebut **gradient descent** digunakan, di mana kita memulai dengan bobot awal w<sup>(0)</sup>, dan kemudian pada setiap langkah memperbarui bobot sesuai dengan rumus:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η disebut sebagai **learning rate**, dan ∇E(w) menunjukkan **gradien** dari E. Setelah kita menghitung gradien, kita mendapatkan:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

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

Dalam pelajaran ini, Anda telah mempelajari tentang perceptron, yang merupakan model klasifikasi biner, dan cara melatihnya menggunakan vektor bobot.

## 🚀 Tantangan

Jika Anda ingin mencoba membangun perceptron Anda sendiri, coba [lab ini di Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) yang menggunakan [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kuis Pasca-Pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Tinjauan & Studi Mandiri

Untuk melihat bagaimana kita dapat menggunakan perceptron untuk menyelesaikan masalah sederhana maupun masalah dunia nyata, dan untuk melanjutkan pembelajaran - buka notebook [Perceptron](Perceptron.ipynb).

Berikut adalah [artikel menarik tentang perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) juga.

## [Tugas](lab/README.md)

Dalam pelajaran ini, kita telah mengimplementasikan perceptron untuk tugas klasifikasi biner, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam lab ini, Anda diminta untuk menyelesaikan masalah klasifikasi digit sepenuhnya, yaitu menentukan digit mana yang paling mungkin sesuai dengan gambar yang diberikan.

* [Instruksi](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.