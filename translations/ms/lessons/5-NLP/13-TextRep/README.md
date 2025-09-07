<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-29T12:01:00+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "ms"
}
-->
# Mewakili Teks sebagai Tensor

## [Kuiz Pra-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Pengelasan Teks

Sepanjang bahagian pertama seksyen ini, kita akan memberi tumpuan kepada tugas **pengelasan teks**. Kita akan menggunakan Dataset [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), yang mengandungi artikel berita seperti berikut:

* Kategori: Sci/Tech  
* Tajuk: Ky. Company Wins Grant to Study Peptides (AP)  
* Isi: AP - Sebuah syarikat yang diasaskan oleh seorang penyelidik kimia di Universiti Louisville memenangi geran untuk membangunkan...

Matlamat kita adalah untuk mengelaskan item berita ke dalam salah satu kategori berdasarkan teks.

## Mewakili teks

Jika kita ingin menyelesaikan tugas Pemprosesan Bahasa Semula Jadi (NLP) dengan rangkaian neural, kita memerlukan cara untuk mewakili teks sebagai tensor. Komputer sudah mewakili aksara teks sebagai nombor yang memetakan kepada fon pada skrin anda menggunakan pengekodan seperti ASCII atau UTF-8.

<img alt="Imej menunjukkan diagram pemetaan aksara kepada representasi ASCII dan binari" src="images/ascii-character-map.png" width="50%"/>

> [Sumber imej](https://www.seobility.net/en/wiki/ASCII)

Sebagai manusia, kita memahami apa yang setiap huruf **wakili**, dan bagaimana semua aksara bergabung untuk membentuk perkataan dalam ayat. Walau bagaimanapun, komputer sendiri tidak mempunyai pemahaman seperti itu, dan rangkaian neural perlu mempelajari makna semasa latihan.

Oleh itu, kita boleh menggunakan pendekatan yang berbeza untuk mewakili teks:

* **Representasi peringkat aksara**, di mana kita mewakili teks dengan menganggap setiap aksara sebagai nombor. Memandangkan kita mempunyai *C* aksara yang berbeza dalam korpus teks kita, perkataan *Hello* akan diwakili oleh tensor 5x*C*. Setiap huruf akan sepadan dengan lajur tensor dalam pengekodan satu-panas (one-hot encoding).  
* **Representasi peringkat perkataan**, di mana kita mencipta **perbendaharaan kata** semua perkataan dalam teks kita, dan kemudian mewakili perkataan menggunakan pengekodan satu-panas. Pendekatan ini agak lebih baik, kerana setiap huruf secara individu tidak mempunyai banyak makna, dan dengan menggunakan konsep semantik peringkat lebih tinggi - perkataan - kita mempermudahkan tugas untuk rangkaian neural. Walau bagaimanapun, memandangkan saiz kamus yang besar, kita perlu menangani tensor jarang berdimensi tinggi.

Tidak kira representasi yang digunakan, kita perlu terlebih dahulu menukar teks kepada urutan **token**, satu token boleh menjadi aksara, perkataan, atau kadangkala sebahagian daripada perkataan. Kemudian, kita menukar token kepada nombor, biasanya menggunakan **perbendaharaan kata**, dan nombor ini boleh dimasukkan ke dalam rangkaian neural menggunakan pengekodan satu-panas.

## N-Gram

Dalam bahasa semula jadi, makna tepat sesuatu perkataan hanya boleh ditentukan dalam konteks. Sebagai contoh, makna *neural network* dan *fishing network* adalah sangat berbeza. Salah satu cara untuk mengambil kira perkara ini adalah dengan membina model kita berdasarkan pasangan perkataan, dan menganggap pasangan perkataan sebagai token perbendaharaan kata yang berasingan. Dengan cara ini, ayat *I like to go fishing* akan diwakili oleh urutan token berikut: *I like*, *like to*, *to go*, *go fishing*. Masalah dengan pendekatan ini adalah saiz kamus bertambah dengan ketara, dan kombinasi seperti *go fishing* dan *go shopping* diwakili oleh token yang berbeza, yang tidak berkongsi sebarang persamaan semantik walaupun menggunakan kata kerja yang sama.

Dalam beberapa kes, kita mungkin mempertimbangkan untuk menggunakan tri-gram -- kombinasi tiga perkataan -- juga. Oleh itu, pendekatan ini sering dipanggil **n-gram**. Ia juga masuk akal untuk menggunakan n-gram dengan representasi peringkat aksara, di mana n-gram akan lebih kurang sepadan dengan pelbagai suku kata.

## Bag-of-Words dan TF/IDF

Apabila menyelesaikan tugas seperti pengelasan teks, kita perlu dapat mewakili teks dengan satu vektor bersaiz tetap, yang akan kita gunakan sebagai input kepada pengelas padat akhir. Salah satu cara paling mudah untuk melakukannya adalah dengan menggabungkan semua representasi perkataan individu, contohnya dengan menambahnya. Jika kita menambah pengekodan satu-panas setiap perkataan, kita akan mendapat vektor frekuensi, yang menunjukkan berapa kali setiap perkataan muncul dalam teks. Representasi teks seperti ini dipanggil **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Imej oleh penulis

BoW pada asasnya mewakili perkataan mana yang muncul dalam teks dan dalam kuantiti apa, yang sememangnya boleh menjadi petunjuk yang baik tentang apa teks itu. Sebagai contoh, artikel berita tentang politik mungkin mengandungi perkataan seperti *president* dan *country*, manakala penerbitan saintifik mungkin mempunyai sesuatu seperti *collider*, *discovered*, dan sebagainya. Oleh itu, frekuensi perkataan dalam banyak kes boleh menjadi petunjuk yang baik tentang kandungan teks.

Masalah dengan BoW adalah bahawa perkataan biasa tertentu, seperti *and*, *is*, dan sebagainya, muncul dalam kebanyakan teks, dan mereka mempunyai frekuensi tertinggi, menutupi perkataan yang benar-benar penting. Kita boleh mengurangkan kepentingan perkataan tersebut dengan mengambil kira frekuensi di mana perkataan muncul dalam keseluruhan koleksi dokumen. Ini adalah idea utama di sebalik pendekatan TF/IDF, yang dibincangkan dengan lebih terperinci dalam buku nota yang dilampirkan pada pelajaran ini.

Walau bagaimanapun, tiada satu pun pendekatan ini dapat sepenuhnya mengambil kira **semantik** teks. Kita memerlukan model rangkaian neural yang lebih berkuasa untuk melakukannya, yang akan kita bincangkan kemudian dalam seksyen ini.

## ✍️ Latihan: Representasi Teks

Teruskan pembelajaran anda dalam buku nota berikut:

* [Representasi Teks dengan PyTorch](TextRepresentationPyTorch.ipynb)  
* [Representasi Teks dengan TensorFlow](TextRepresentationTF.ipynb)  

## Kesimpulan

Setakat ini, kita telah mengkaji teknik yang boleh menambah berat frekuensi kepada perkataan yang berbeza. Walau bagaimanapun, teknik ini tidak dapat mewakili makna atau susunan. Seperti yang dikatakan oleh ahli linguistik terkenal J. R. Firth pada tahun 1935, "Makna lengkap sesuatu perkataan sentiasa bersifat kontekstual, dan tiada kajian makna yang terpisah daripada konteks boleh dianggap serius." Kita akan belajar kemudian dalam kursus ini bagaimana untuk menangkap maklumat kontekstual daripada teks menggunakan pemodelan bahasa.

## 🚀 Cabaran

Cuba beberapa latihan lain menggunakan bag-of-words dan model data yang berbeza. Anda mungkin mendapat inspirasi daripada [pertandingan ini di Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Kuiz Pasca-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Ulasan & Kajian Kendiri

Amalkan kemahiran anda dengan teknik embedding teks dan bag-of-words di [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Tugasan: Buku Nota](assignment.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.