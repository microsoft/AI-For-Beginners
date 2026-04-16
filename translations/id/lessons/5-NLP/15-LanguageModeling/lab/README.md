# Melatih Model Skip-Gram

Tugas Praktikum dari [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tugas

Dalam praktikum ini, kami menantang Anda untuk melatih model Word2Vec menggunakan teknik Skip-Gram. Latih sebuah jaringan dengan embedding untuk memprediksi kata-kata yang berdekatan dalam jendela Skip-Gram selebar $N$ token. Anda dapat menggunakan [kode dari pelajaran ini](../CBoW-TF.ipynb), dan sedikit memodifikasinya.

## Dataset

Anda dipersilakan menggunakan buku apa saja. Anda dapat menemukan banyak teks gratis di [Project Gutenberg](https://www.gutenberg.org/), misalnya, berikut adalah tautan langsung ke [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) oleh Lewis Carroll. Atau, Anda dapat menggunakan drama-drama Shakespeare, yang dapat Anda unduh menggunakan kode berikut:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Eksplorasi!

Jika Anda memiliki waktu dan ingin mendalami topik ini, coba eksplorasi beberapa hal berikut:

* Bagaimana ukuran embedding memengaruhi hasil?
* Bagaimana gaya teks yang berbeda memengaruhi hasil?
* Ambil beberapa jenis kata yang sangat berbeda dan sinonimnya, dapatkan representasi vektor mereka, terapkan PCA untuk mengurangi dimensi menjadi 2, dan plot mereka dalam ruang 2D. Apakah Anda melihat pola tertentu?

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.