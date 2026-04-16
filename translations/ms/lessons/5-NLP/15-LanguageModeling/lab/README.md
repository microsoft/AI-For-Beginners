# Melatih Model Skip-Gram

Tugasan Makmal daripada [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugasan

Dalam makmal ini, kami mencabar anda untuk melatih model Word2Vec menggunakan teknik Skip-Gram. Latih rangkaian dengan embedding untuk meramalkan perkataan berdekatan dalam tingkap Skip-Gram selebar $N$ token. Anda boleh menggunakan [kod daripada pelajaran ini](../CBoW-TF.ipynb), dan ubah sedikit.

## Dataset

Anda dialu-alukan untuk menggunakan mana-mana buku. Anda boleh menemui banyak teks percuma di [Project Gutenberg](https://www.gutenberg.org/), contohnya, berikut adalah pautan langsung ke [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) oleh Lewis Carroll. Atau, anda boleh menggunakan drama Shakespeare, yang boleh anda dapatkan menggunakan kod berikut:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Terokai!

Jika anda mempunyai masa dan ingin mendalami subjek ini, cuba terokai beberapa perkara:

* Bagaimana saiz embedding mempengaruhi hasil?
* Bagaimana gaya teks yang berbeza mempengaruhi hasil?
* Ambil beberapa jenis perkataan yang sangat berbeza dan sinonimnya, dapatkan representasi vektor mereka, gunakan PCA untuk mengurangkan dimensi kepada 2, dan plotkan dalam ruang 2D. Adakah anda melihat sebarang corak?

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.