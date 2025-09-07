<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:34:44+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "id"
}
-->
# Pengantar Jaringan Neural

![Ringkasan konten Pengantar Jaringan Neural dalam bentuk doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.id.png)

Seperti yang telah kita bahas dalam pengantar, salah satu cara untuk mencapai kecerdasan adalah dengan melatih **model komputer** atau **otak buatan**. Sejak pertengahan abad ke-20, para peneliti mencoba berbagai model matematika, hingga beberapa tahun terakhir arah ini terbukti sangat berhasil. Model matematika otak semacam ini disebut **jaringan neural**.

> Kadang-kadang jaringan neural disebut *Artificial Neural Networks* atau ANNs, untuk menunjukkan bahwa kita sedang berbicara tentang model, bukan jaringan neuron yang sebenarnya.

## Pembelajaran Mesin

Jaringan Neural adalah bagian dari disiplin yang lebih besar yang disebut **Pembelajaran Mesin** (Machine Learning), yang bertujuan menggunakan data untuk melatih model komputer agar dapat menyelesaikan masalah. Pembelajaran Mesin merupakan bagian besar dari Kecerdasan Buatan, namun, kita tidak akan membahas Pembelajaran Mesin klasik dalam kurikulum ini.

> Kunjungi kurikulum terpisah kami **[Machine Learning for Beginners](http://github.com/microsoft/ml-for-beginners)** untuk mempelajari lebih lanjut tentang Pembelajaran Mesin klasik.

Dalam Pembelajaran Mesin, kita mengasumsikan bahwa kita memiliki beberapa dataset contoh **X**, dan nilai keluaran yang sesuai **Y**. Contoh sering kali berupa vektor N-dimensi yang terdiri dari **fitur**, dan keluaran disebut **label**.

Kita akan mempertimbangkan dua masalah pembelajaran mesin yang paling umum:

* **Klasifikasi**, di mana kita perlu mengklasifikasikan objek input ke dalam dua atau lebih kelas.
* **Regresi**, di mana kita perlu memprediksi angka numerik untuk setiap sampel input.

> Saat merepresentasikan input dan output sebagai tensor, dataset input adalah matriks berukuran M×N, di mana M adalah jumlah sampel dan N adalah jumlah fitur. Label keluaran Y adalah vektor berukuran M.

Dalam kurikulum ini, kita hanya akan fokus pada model jaringan neural.

## Model Neuron

Dari biologi kita tahu bahwa otak kita terdiri dari sel-sel neural, masing-masing memiliki banyak "input" (akson), dan satu output (dendrit). Akson dan dendrit dapat menghantarkan sinyal listrik, dan koneksi antara akson dan dendrit dapat menunjukkan tingkat konduktivitas yang berbeda (dikendalikan oleh neurotransmiter).

![Model Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.id.jpg) | ![Model Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.id.png)
----|----
Neuron Asli *([Gambar](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) dari Wikipedia)* | Neuron Buatan *(Gambar oleh Penulis)*

Dengan demikian, model matematika paling sederhana dari neuron memiliki beberapa input X<sub>1</sub>, ..., X<sub>N</sub> dan satu output Y, serta serangkaian bobot W<sub>1</sub>, ..., W<sub>N</sub>. Output dihitung sebagai:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

di mana f adalah beberapa **fungsi aktivasi** non-linear.

> Model awal neuron dijelaskan dalam makalah klasik [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) oleh Warren McCullock dan Walter Pitts pada tahun 1943. Donald Hebb dalam bukunya "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" mengusulkan cara jaringan tersebut dapat dilatih.

## Dalam Bagian Ini

Dalam bagian ini kita akan mempelajari tentang:
* [Perceptron](03-Perceptron/README.md), salah satu model jaringan neural paling awal untuk klasifikasi dua kelas
* [Jaringan berlapis-lapis](04-OwnFramework/README.md) dengan notebook pendamping [cara membangun kerangka kerja kita sendiri](04-OwnFramework/OwnFramework.ipynb)
* [Kerangka Kerja Jaringan Neural](05-Frameworks/README.md), dengan notebook berikut: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) dan [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.