# Pemprosesan Bahasa Semulajadi

![Ringkasan tugas NLP dalam doodle](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.ms.png)

Dalam bahagian ini, kita akan memberi tumpuan kepada penggunaan Rangkaian Neural untuk menangani tugas-tugas berkaitan dengan **Pemprosesan Bahasa Semulajadi (NLP)**. Terdapat banyak masalah NLP yang kita mahu komputer dapat selesaikan:

* **Klasifikasi teks** adalah masalah klasifikasi tipikal yang berkaitan dengan urutan teks. Contohnya termasuk mengklasifikasikan mesej e-mel sebagai spam atau tidak spam, atau mengkategorikan artikel sebagai sukan, perniagaan, politik, dan lain-lain. Juga, semasa membangunkan bot sembang, kita sering perlu memahami apa yang ingin disampaikan oleh pengguna -- dalam kes ini kita berurusan dengan **klasifikasi niat**. Selalunya, dalam klasifikasi niat kita perlu berurusan dengan banyak kategori.
* **Analisis sentimen** adalah masalah regresi tipikal, di mana kita perlu memberikan nombor (sentimen) yang sepadan dengan betapa positif/negatifnya makna satu ayat. Versi yang lebih maju dari analisis sentimen adalah **analisis sentimen berasaskan aspek** (ABSA), di mana kita memberikan sentimen bukan kepada keseluruhan ayat, tetapi kepada bahagian-bahagian yang berbeza (aspek), contohnya *Di restoran ini, saya suka masakannya, tetapi suasananya sangat teruk*.
* **Pengenalan Entiti Bernama** (NER) merujuk kepada masalah mengekstrak entiti tertentu dari teks. Sebagai contoh, kita mungkin perlu memahami bahawa dalam frasa *Saya perlu terbang ke Paris esok* perkataan *esok* merujuk kepada TARIKH, dan *Paris* adalah LOKASI.  
* **Pengeluaran kata kunci** adalah serupa dengan NER, tetapi kita perlu mengekstrak kata-kata yang penting untuk makna ayat secara automatik, tanpa pra-latihan untuk jenis entiti tertentu.
* **Pengelompokan teks** boleh berguna apabila kita ingin mengumpulkan ayat-ayat yang serupa, contohnya, permintaan serupa dalam perbualan sokongan teknikal.
* **Menjawab soalan** merujuk kepada kemampuan model untuk menjawab soalan tertentu. Model menerima petikan teks dan soalan sebagai input, dan ia perlu memberikan lokasi dalam teks di mana jawapan kepada soalan tersebut terkandung (atau, kadang-kadang, untuk menghasilkan teks jawapan).
* **Penjanaan Teks** adalah kemampuan model untuk menghasilkan teks baru. Ia boleh dianggap sebagai tugas klasifikasi yang meramalkan huruf/perkataan seterusnya berdasarkan *prompt teks* tertentu. Model penjanaan teks yang lebih maju, seperti GPT-3, mampu menyelesaikan tugas NLP lain seperti klasifikasi menggunakan teknik yang dipanggil [pemrograman prompt](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) atau [rekayasa prompt](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Pemadatan teks** adalah teknik di mana kita ingin komputer "membaca" teks yang panjang dan merangkumkannya dalam beberapa ayat.
* **Terjemahan mesin** boleh dilihat sebagai gabungan pemahaman teks dalam satu bahasa, dan penjanaan teks dalam bahasa lain.

Pada mulanya, kebanyakan tugas NLP diselesaikan menggunakan kaedah tradisional seperti tatabahasa. Sebagai contoh, dalam terjemahan mesin, pengurai digunakan untuk mengubah ayat awal menjadi pokok sintaks, kemudian struktur semantik tahap tinggi diekstrak untuk mewakili makna ayat, dan berdasarkan makna ini dan tatabahasa bahasa sasaran, hasilnya dijana. Kini, banyak tugas NLP diselesaikan dengan lebih berkesan menggunakan rangkaian neural.

> Banyak kaedah NLP klasik dilaksanakan dalam [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org) pustaka Python. Terdapat [Buku NLTK](https://www.nltk.org/book/) yang hebat tersedia dalam talian yang membincangkan bagaimana pelbagai tugas NLP boleh diselesaikan menggunakan NLTK.

Dalam kursus kita, kita akan lebih fokus kepada penggunaan Rangkaian Neural untuk NLP, dan kita akan menggunakan NLTK apabila perlu.

Kita telah pun belajar tentang penggunaan rangkaian neural untuk menangani data tabular dan gambar. Perbezaan utama antara jenis data tersebut dan teks adalah bahawa teks adalah urutan dengan panjang yang berubah-ubah, sementara saiz input dalam kes gambar diketahui terlebih dahulu. Walaupun rangkaian konvolusi boleh mengekstrak corak dari data input, corak dalam teks adalah lebih kompleks. Contohnya, kita boleh mempunyai penolakan yang dipisahkan dari subjek yang boleh menjadi sewenang-wenangnya untuk banyak perkataan (contohnya *Saya tidak suka oren*, berbanding *Saya tidak suka oren yang besar berwarna-warni dan lazat*), dan itu masih perlu ditafsirkan sebagai satu corak. Oleh itu, untuk menangani bahasa kita perlu memperkenalkan jenis rangkaian neural baru, seperti *rangkaian berulang* dan *transformer*.

## Pasang Pustaka

Jika anda menggunakan pemasangan Python tempatan untuk menjalankan kursus ini, anda mungkin perlu memasang semua pustaka yang diperlukan untuk NLP menggunakan arahan berikut:

**Untuk PyTorch**
```bash
pip install -r requirements-torch.txt
```
**Untuk TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Anda boleh mencuba NLP dengan TensorFlow di [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Amaran GPU

Dalam bahagian ini, dalam beberapa contoh kita akan melatih model yang agak besar.
* **Gunakan Komputer yang Dikuasakan GPU**: Adalah disyorkan untuk menjalankan buku nota anda pada komputer yang dikuasakan GPU untuk mengurangkan masa menunggu ketika bekerja dengan model yang besar.
* **Kekangan Memori GPU**: Menjalankan pada GPU mungkin menyebabkan situasi di mana anda kehabisan memori GPU, terutama ketika melatih model yang besar.
* **Penggunaan Memori GPU**: Jumlah memori GPU yang digunakan semasa latihan bergantung kepada pelbagai faktor, termasuk saiz minibatch.
* **Kurangkan Saiz Minibatch**: Jika anda menghadapi masalah memori GPU, pertimbangkan untuk mengurangkan saiz minibatch dalam kod anda sebagai penyelesaian yang berpotensi.
* **Pelepasan Memori GPU TensorFlow**: Versi TensorFlow yang lebih lama mungkin tidak melepaskan memori GPU dengan betul apabila melatih pelbagai model dalam satu kernel Python. Untuk mengurus penggunaan memori GPU dengan berkesan, anda boleh mengkonfigurasi TensorFlow untuk memperuntukkan memori GPU hanya apabila diperlukan.
* **Inklusi Kod**: Untuk menetapkan TensorFlow agar hanya mengembangkan pengagihan memori GPU apabila diperlukan, sertakan kod berikut dalam buku nota anda:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Jika anda berminat untuk belajar tentang NLP dari perspektif ML klasik, lawati [suite pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## Dalam Bahagian Ini
Dalam bahagian ini kita akan belajar tentang:

* [Mewakili teks sebagai tensor](13-TextRep/README.md)
* [Penyisipan Kata](14-Emdeddings/README.md)
* [Pemodelan Bahasa](15-LanguageModeling/README.md)
* [Rangkaian Neural Berulang](16-RNN/README.md)
* [Rangkaian Generatif](17-GenerativeNetworks/README.md)
* [Transformers](18-Transformers/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa ibundanya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.