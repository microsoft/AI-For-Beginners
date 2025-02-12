# Pengenalan Entiti Bernama

Setakat ini, kita telah banyak memberi tumpuan kepada satu tugas NLP - pengelasan. Walau bagaimanapun, terdapat juga tugas NLP lain yang boleh dilaksanakan dengan rangkaian neural. Salah satu tugas tersebut adalah **[Pengenalan Entiti Bernama](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), yang berkaitan dengan pengenalan entiti tertentu dalam teks, seperti tempat, nama orang, selang tarikh-masa, formula kimia dan sebagainya.

## [Kuiz Pra-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Contoh Penggunaan NER

Anggaplah anda ingin membangunkan bot sembang bahasa semula jadi, yang serupa dengan Amazon Alexa atau Google Assistant. Cara bot sembang pintar berfungsi adalah untuk *memahami* apa yang dikehendaki pengguna dengan melakukan pengelasan teks pada ayat input. Hasil pengelasan ini dipanggil **niat**, yang menentukan apa yang sepatutnya dilakukan oleh bot sembang.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Gambar oleh penulis

Walau bagaimanapun, pengguna mungkin memberikan beberapa parameter sebagai sebahagian daripada frasa. Contohnya, apabila meminta cuaca, dia mungkin menentukan lokasi atau tarikh. Bot seharusnya dapat memahami entiti-entiti tersebut dan mengisi slot parameter dengan sewajarnya sebelum melakukan tindakan. Di sinilah NER berperanan.

> ✅ Contoh lain adalah [menganalisis kertas perubatan saintifik](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Salah satu perkara utama yang perlu kita cari adalah istilah perubatan tertentu, seperti penyakit dan bahan perubatan. Walaupun sejumlah kecil penyakit mungkin dapat diekstrak menggunakan carian substring, entiti yang lebih kompleks, seperti sebatian kimia dan nama ubat, memerlukan pendekatan yang lebih kompleks.

## NER sebagai Pengelasan Token

Model NER pada dasarnya adalah **model pengelasan token**, kerana untuk setiap token input kita perlu memutuskan sama ada ia tergolong dalam entiti atau tidak, dan jika ya - kepada kelas entiti mana.

Pertimbangkan tajuk kertas berikut:

**Regurgitasi injap trikuspid** dan **karbonat litium** **toksisiti** pada bayi baru lahir.

Entiti di sini adalah:

* Regurgitasi injap trikuspid adalah penyakit (`DIS`)
* Karbonat litium adalah bahan kimia (`CHEM`)
* Toksisiti juga merupakan penyakit (`DIS`)

Perhatikan bahawa satu entiti boleh meliputi beberapa token. Dan, seperti dalam kes ini, kita perlu membezakan antara dua entiti berturut-turut. Oleh itu, adalah biasa untuk menggunakan dua kelas bagi setiap entiti - satu yang menentukan token pertama entiti (selalunya awalan `B-` digunakan, untuk **b**ermula), dan satu lagi - sambungan entiti (`I-`, untuk **i**nner token). Kita juga menggunakan `O` sebagai kelas untuk mewakili semua token **o**ther. Penandaan token sedemikian dipanggil [penandaan BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (atau IOB). Apabila ditandakan, tajuk kita akan kelihatan seperti ini:

Token | Tag
------|-----
Trikuspid | B-DIS
injap | I-DIS
regurgitasi | I-DIS
dan | O
litium | B-CHEM
karbonat | I-CHEM
toksisiti | B-DIS
dalam | O
sebuah | O
bayi | O
baru | O
lahir | O
. | O

Oleh kerana kita perlu membina padanan satu-ke-satu antara token dan kelas, kita boleh melatih model rangkaian neural **banyak-ke-banyak** yang paling kanan daripada gambar ini:

![Gambar menunjukkan corak rangkaian neural berulang yang biasa.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.ms.jpg)

> *Gambar dari [catatan blog ini](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) oleh [Andrej Karpathy](http://karpathy.github.io/). Model pengelasan token NER sepadan dengan seni bina rangkaian paling kanan dalam gambar ini.*

## Melatih Model NER

Oleh kerana model NER pada dasarnya adalah model pengelasan token, kita boleh menggunakan RNN yang sudah kita kenali untuk tugas ini. Dalam kes ini, setiap blok rangkaian berulang akan mengembalikan ID token. Contoh notebook berikut menunjukkan cara melatih LSTM untuk pengelasan token.

## ✍️ Contoh Notebook: NER

Teruskan pembelajaran anda dalam notebook berikut:

* [NER dengan TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Kesimpulan

Model NER adalah **model pengelasan token**, yang bermaksud ia boleh digunakan untuk melaksanakan pengelasan token. Ini adalah tugas yang sangat biasa dalam NLP, membantu mengenali entiti tertentu dalam teks termasuk tempat, nama, tarikh, dan banyak lagi.

## 🚀 Cabaran

Lengkapkan tugasan yang dipautkan di bawah untuk melatih model pengenalan entiti bernama untuk istilah perubatan, kemudian cuba pada dataset yang berbeza.

## [Kuiz Pasca-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Ulasan & Pembelajaran Sendiri

Baca blog [Keberkesanan Rangkaian Neural Berulang yang Tidak Masuk Akal](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) dan ikuti bahagian Bacaan Lanjut dalam artikel itu untuk mendalami pengetahuan anda.

## [Tugasan](lab/README.md)

Dalam tugasan untuk pelajaran ini, anda perlu melatih model pengenalan entiti perubatan. Anda boleh memulakan dengan melatih model LSTM seperti yang diterangkan dalam pelajaran ini, dan teruskan dengan menggunakan model transformer BERT. Baca [arahan](lab/README.md) untuk mendapatkan semua butiran.

**Penafian**: 
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia yang profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.