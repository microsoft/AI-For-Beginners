# Mewakili Teks sebagai Tensor

## [Kuiz Pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Klasifikasi Teks

Sepanjang bagian pertama dari seksyen ini, kita akan fokus pada tugas **klasifikasi teks**. Kita akan menggunakan Dataset [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), yang mengandungi artikel berita seperti berikut:

* Kategori: Sains/Teknologi
* Tajuk: Syarikat Ky. Menang Geran untuk Kajian Peptida (AP)
* Isi: AP - Sebuah syarikat yang diasaskan oleh seorang penyelidik kimia di Universiti Louisville telah memenangi geran untuk membangunkan...

Matlamat kita adalah untuk mengklasifikasikan item berita ke dalam salah satu kategori berdasarkan teks.

## Mewakili teks

Jika kita ingin menyelesaikan tugas Pemprosesan Bahasa Semulajadi (NLP) dengan rangkaian neural, kita memerlukan cara untuk mewakili teks sebagai tensor. Komputer sudah mewakili watak teks sebagai nombor yang dipetakan kepada fon pada skrin anda menggunakan pengekodan seperti ASCII atau UTF-8.

<img alt="Gambar menunjukkan diagram yang memetakan watak kepada representasi ASCII dan binari" src="images/ascii-character-map.png" width="50%"/>

> [Sumber gambar](https://www.seobility.net/en/wiki/ASCII)

Sebagai manusia, kita memahami apa yang setiap huruf **wakili**, dan bagaimana semua watak bersatu untuk membentuk perkataan dalam satu ayat. Namun, komputer tidak mempunyai pemahaman tersebut, dan rangkaian neural perlu belajar makna tersebut semasa latihan.

Oleh itu, kita boleh menggunakan pelbagai pendekatan apabila mewakili teks:

* **Representasi tahap watak**, di mana kita mewakili teks dengan menganggap setiap watak sebagai nombor. Memandangkan kita mempunyai *C* watak yang berbeza dalam korpus teks kita, perkataan *Hello* akan diwakili oleh tensor 5x*C*. Setiap huruf akan sepadan dengan lajur tensor dalam pengekodan one-hot.
* **Representasi tahap perkataan**, di mana kita mencipta **perbendaharaan kata** bagi semua perkataan dalam teks kita, dan kemudian mewakili perkataan menggunakan pengekodan one-hot. Pendekatan ini adalah lebih baik, kerana setiap huruf sendiri tidak mempunyai banyak makna, dan dengan menggunakan konsep semantik yang lebih tinggi - perkataan - kita mempermudahkan tugas untuk rangkaian neural. Namun, memandangkan saiz kamus yang besar, kita perlu berhadapan dengan tensor jarang berdimensi tinggi.

Tanpa mengira representasi, kita perlu terlebih dahulu menukarkan teks kepada urutan **token**, di mana satu token boleh jadi sama ada huruf, perkataan, atau kadangkala bahkan sebahagian daripada perkataan. Kemudian, kita menukarkan token kepada nombor, biasanya menggunakan **perbendaharaan kata**, dan nombor ini boleh dimasukkan ke dalam rangkaian neural menggunakan pengekodan one-hot.

## N-Gram

Dalam bahasa semulajadi, makna tepat perkataan hanya dapat ditentukan dalam konteks. Sebagai contoh, makna *rangkaian neural* dan *rangkaian memancing* adalah sangat berbeza. Salah satu cara untuk mengambil kira ini adalah dengan membina model kita berdasarkan pasangan perkataan, dan menganggap pasangan perkataan sebagai token perbendaharaan kata yang berasingan. Dengan cara ini, ayat *Saya suka pergi memancing* akan diwakili oleh urutan token berikut: *Saya suka*, *suka pergi*, *pergi memancing*. Masalah dengan pendekatan ini adalah saiz kamus meningkat dengan ketara, dan kombinasi seperti *pergi memancing* dan *pergi membeli-belah* diwakili oleh token yang berbeza, yang tidak berkongsi sebarang persamaan semantik walaupun menggunakan kata kerja yang sama.  

Dalam beberapa kes, kita mungkin mempertimbangkan untuk menggunakan tri-gram -- kombinasi tiga perkataan -- juga. Oleh itu, pendekatan ini sering dipanggil **n-gram**. Selain itu, adalah wajar untuk menggunakan n-gram dengan representasi tahap watak, di mana n-gram akan lebih kurang sepadan dengan suku kata yang berbeza.

## Beg Perkataan dan TF/IDF

Apabila menyelesaikan tugas seperti klasifikasi teks, kita perlu dapat mewakili teks dengan satu vektor saiz tetap, yang akan kita gunakan sebagai input kepada pengklasifikasi padat akhir. Salah satu cara paling mudah untuk melakukan ini adalah dengan menggabungkan semua representasi perkataan individu, contohnya dengan menambahnya. Jika kita menambah pengekodan one-hot bagi setiap perkataan, kita akan berakhir dengan vektor frekuensi, menunjukkan berapa kali setiap perkataan muncul dalam teks. Representasi teks sedemikian dipanggil **beg perkataan** (BoW).

<img src="images/bow.png" width="90%"/>

> Gambar oleh penulis

BoW pada dasarnya mewakili perkataan mana yang muncul dalam teks dan dalam kuantiti berapa, yang sememangnya boleh menjadi petunjuk yang baik tentang apa teks tersebut. Sebagai contoh, artikel berita mengenai politik mungkin mengandungi perkataan seperti *presiden* dan *negara*, manakala penerbitan saintifik akan mempunyai sesuatu seperti *penemuan*, *collider*, dan lain-lain. Oleh itu, frekuensi perkataan boleh dalam banyak kes menjadi petunjuk yang baik tentang kandungan teks.

Masalah dengan BoW adalah bahawa beberapa perkataan umum, seperti *dan*, *adalah*, dan lain-lain muncul dalam kebanyakan teks, dan mereka mempunyai frekuensi tertinggi, menenggelamkan perkataan yang sebenarnya penting. Kita boleh mengurangkan kepentingan perkataan tersebut dengan mengambil kira frekuensi di mana perkataan muncul dalam keseluruhan koleksi dokumen. Ini adalah idea utama di sebalik pendekatan TF/IDF, yang dibincangkan dengan lebih terperinci dalam buku nota yang dilampirkan kepada pelajaran ini.

Namun, tiada satu pun daripada pendekatan tersebut dapat sepenuhnya mengambil kira **semantik** teks. Kita memerlukan model rangkaian neural yang lebih kuat untuk melakukan ini, yang akan kita bincangkan kemudian dalam seksyen ini.

## ✍️ Latihan: Representasi Teks

Teruskan pembelajaran anda dalam buku nota berikut:

* [Representasi Teks dengan PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Representasi Teks dengan TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Kesimpulan

Setakat ini, kita telah mengkaji teknik yang dapat menambah berat frekuensi kepada perkataan yang berbeza. Namun, mereka tidak dapat mewakili makna atau susunan. Seperti yang dikatakan oleh ahli linguistik terkenal J. R. Firth pada tahun 1935, "Makna lengkap sebuah perkataan sentiasa kontekstual, dan tiada kajian tentang makna yang terpisah daripada konteks boleh diambil dengan serius." Kita akan belajar kemudian dalam kursus bagaimana untuk menangkap maklumat kontekstual dari teks menggunakan pemodelan bahasa.

## 🚀 Cabaran

Cuba beberapa latihan lain menggunakan beg-perkataan dan pelbagai model data. Anda mungkin terinspirasi oleh [pertandingan ini di Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Kuiz Pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Ulasan & Pembelajaran Sendiri

Latih kemahiran anda dengan teknik embedding teks dan beg-perkataan di [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Tugasan: Buku Nota](assignment.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.