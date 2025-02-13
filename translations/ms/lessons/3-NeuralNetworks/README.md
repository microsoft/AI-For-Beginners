# Pengenalan kepada Rangkaian Neural

![Ringkasan kandungan Pengenalan Rangkaian Neural dalam doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.ms.png)

Seperti yang kita bincangkan dalam pengenalan, salah satu cara untuk mencapai kecerdasan adalah dengan melatih **model komputer** atau **otak buatan**. Sejak pertengahan abad ke-20, para penyelidik telah mencuba pelbagai model matematik, sehingga dalam beberapa tahun kebelakangan ini, arah ini terbukti sangat berjaya. Model matematik otak ini dikenali sebagai **rangkaian neural**.

> Kadang-kadang rangkaian neural dipanggil *Rangkaian Neural Buatan*, ANNs, untuk menunjukkan bahawa kita bercakap tentang model, bukan rangkaian neuron yang sebenar.

## Pembelajaran Mesin

Rangkaian Neural adalah sebahagian daripada disiplin yang lebih besar yang dipanggil **Pembelajaran Mesin**, yang bertujuan untuk menggunakan data untuk melatih model komputer yang mampu menyelesaikan masalah. Pembelajaran Mesin merupakan sebahagian besar daripada Kecerdasan Buatan, namun, kami tidak merangkumi ML klasik dalam kurikulum ini.

> Kunjungi kurikulum **[Pembelajaran Mesin untuk Pemula](http://github.com/microsoft/ml-for-beginners)** kami yang berasingan untuk mengetahui lebih lanjut tentang Pembelajaran Mesin klasik.

Dalam Pembelajaran Mesin, kita menganggap bahawa kita mempunyai set data contoh **X**, dan nilai output yang sepadan **Y**. Contoh sering kali adalah vektor N-dimensi yang terdiri daripada **ciri**, dan output dipanggil **label**.

Kami akan mempertimbangkan dua masalah pembelajaran mesin yang paling biasa:

* **Klasifikasi**, di mana kita perlu mengklasifikasikan objek input ke dalam dua atau lebih kelas.
* **Regresi**, di mana kita perlu meramalkan nombor numerik untuk setiap sampel input.

> Apabila mewakili input dan output sebagai tensor, set data input adalah matriks bersaiz M×N, di mana M adalah bilangan sampel dan N adalah bilangan ciri. Label output Y adalah vektor bersaiz M.

Dalam kurikulum ini, kami hanya akan memberi tumpuan kepada model rangkaian neural.

## Model Neuron

Daripada biologi, kita tahu bahawa otak kita terdiri daripada sel neural, masing-masing mempunyai beberapa "input" (akson), dan satu output (dendrit). Akson dan dendrit boleh menghantar isyarat elektrik, dan sambungan antara akson dan dendrit boleh menunjukkan pelbagai tahap konduktiviti (dikuasai oleh neuromediator).

![Model Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.ms.jpg) | ![Model Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.ms.png)
----|----
Neuron Sebenar *([Imej](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) dari Wikipedia)* | Neuron Buatan *(Imej oleh Penulis)*

Oleh itu, model matematik paling mudah bagi neuron mengandungi beberapa input X<sub>1</sub>, ..., X<sub>N</sub> dan satu output Y, serta satu siri berat W<sub>1</sub>, ..., W<sub>N</sub>. Output dikira sebagai:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

di mana f adalah beberapa **fungsi pengaktifan** bukan linear.

> Model awal neuron telah diterangkan dalam kertas klasik [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) oleh Warren McCullock dan Walter Pitts pada tahun 1943. Donald Hebb dalam bukunya "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" mencadangkan cara rangkaian tersebut boleh dilatih.

## Dalam Bahagian Ini

Dalam bahagian ini, kita akan belajar tentang:
* [Perceptron](03-Perceptron/README.md), salah satu model rangkaian neural terawal untuk klasifikasi dua kelas
* [Rangkaian berlapis](04-OwnFramework/README.md) dengan notebook berpasangan [cara membina rangkaian kami sendiri](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Rangkaian Neural Frameworks](05-Frameworks/README.md), dengan notebook ini: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) dan [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia yang profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.