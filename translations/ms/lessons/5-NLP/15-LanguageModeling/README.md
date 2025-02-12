# Pemodelan Bahasa

Penyematan semantik, seperti Word2Vec dan GloVe, sebenarnya adalah langkah pertama menuju **pemodelan bahasa** - menciptakan model yang entah bagaimana *memahami* (atau *merepresentasikan*) sifat bahasa.

## [Kuis Pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Ide utama di balik pemodelan bahasa adalah melatih model tersebut pada dataset yang tidak diberi label dengan cara yang tidak diawasi. Ini penting karena kita memiliki jumlah teks tidak berlabel yang sangat besar, sementara jumlah teks berlabel selalu akan terbatas oleh jumlah usaha yang dapat kita habiskan untuk memberi label. Sebagian besar waktu, kita dapat membangun model bahasa yang dapat **memprediksi kata yang hilang** dalam teks, karena mudah untuk menyembunyikan kata acak dalam teks dan menggunakannya sebagai sampel pelatihan.

## Melatih Penyematan

Dalam contoh-contoh sebelumnya, kita menggunakan penyematan semantik yang sudah dilatih, tetapi menarik untuk melihat bagaimana penyematan tersebut dapat dilatih. Ada beberapa ide yang dapat digunakan:

* Pemodelan bahasa **N-Gram**, ketika kita memprediksi sebuah token dengan melihat N token sebelumnya (N-gram)
* **Continuous Bag-of-Words** (CBoW), ketika kita memprediksi token tengah $W_0$ dalam urutan token $W_{-N}$, ..., $W_N$.
* **Skip-gram**, di mana kita memprediksi sekumpulan token tetangga {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} dari token tengah $W_0$.

![gambar dari makalah tentang mengubah kata menjadi vektor](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.ms.png)

> Gambar dari [makalah ini](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Contoh Notebook: Melatih model CBoW

Lanjutkan pembelajaran Anda di notebook berikut:

* [Melatih CBoW Word2Vec dengan TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Melatih CBoW Word2Vec dengan PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Kesimpulan

Dalam pelajaran sebelumnya, kita telah melihat bahwa penyematan kata bekerja seperti sihir! Sekarang kita tahu bahwa melatih penyematan kata bukanlah tugas yang sangat kompleks, dan kita seharusnya dapat melatih penyematan kata kita sendiri untuk teks spesifik domain jika diperlukan.

## [Kuis Pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Tinjauan & Studi Mandiri

* [Tutorial Resmi PyTorch tentang Pemodelan Bahasa](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial Resmi TensorFlow tentang melatih model Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Menggunakan kerangka **gensim** untuk melatih penyematan yang paling umum digunakan dalam beberapa baris kode dijelaskan [dalam dokumentasi ini](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tugas: Latih Model Skip-Gram](lab/README.md)

Dalam lab, kami menantang Anda untuk memodifikasi kode dari pelajaran ini untuk melatih model skip-gram alih-alih CBoW. [Baca detailnya](lab/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.