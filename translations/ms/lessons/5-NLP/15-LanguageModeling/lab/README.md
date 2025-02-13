# Melatih Model Skip-Gram

Tugasan Makmal dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Dalam makmal ini, kami mencabar anda untuk melatih model Word2Vec menggunakan teknik Skip-Gram. Latih rangkaian dengan embedding untuk meramalkan kata-kata jiran dalam tetingkap Skip-Gram yang lebar $N$-token. Anda boleh menggunakan [kod dari pelajaran ini](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb), dan sedikit mengubahnya.

## Dataset

Anda boleh menggunakan mana-mana buku. Anda boleh menemui banyak teks percuma di [Project Gutenberg](https://www.gutenberg.org/), sebagai contoh, berikut adalah pautan langsung kepada [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) oleh Lewis Carroll. Atau, anda boleh menggunakan drama-drama Shakespeare, yang boleh anda perolehi dengan menggunakan kod berikut:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Teroka!

Jika anda mempunyai masa dan ingin mendalami subjek ini, cuba teroka beberapa perkara:

* Bagaimana saiz embedding mempengaruhi hasil?
* Bagaimana gaya teks yang berbeza mempengaruhi hasil?
* Ambil beberapa jenis kata yang sangat berbeza dan sinonimnya, peroleh representasi vektor mereka, gunakan PCA untuk mengurangkan dimensi kepada 2, dan plotkan mereka dalam ruang 2D. Adakah anda melihat sebarang corak?

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.