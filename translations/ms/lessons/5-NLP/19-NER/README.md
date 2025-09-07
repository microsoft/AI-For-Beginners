<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-29T11:59:23+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "ms"
}
-->
# Pengenalan Entiti Bernama

Sehingga kini, kita telah banyak menumpukan perhatian kepada satu tugas NLP - klasifikasi. Walau bagaimanapun, terdapat juga tugas-tugas NLP lain yang boleh diselesaikan dengan rangkaian neural. Salah satu tugas tersebut ialah **[Pengenalan Entiti Bernama](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), yang berkaitan dengan mengenal pasti entiti tertentu dalam teks, seperti tempat, nama orang, selang masa, formula kimia, dan sebagainya.

## [Kuiz Pra-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Contoh Penggunaan NER

Bayangkan anda ingin membangunkan bot sembang bahasa semula jadi, seperti Amazon Alexa atau Google Assistant. Cara bot sembang pintar berfungsi adalah dengan *memahami* apa yang pengguna mahukan melalui klasifikasi teks pada ayat input. Hasil daripada klasifikasi ini dikenali sebagai **niat**, yang menentukan apa yang bot sembang perlu lakukan.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Gambar oleh penulis

Namun, pengguna mungkin memberikan beberapa parameter sebagai sebahagian daripada frasa. Sebagai contoh, apabila bertanya tentang cuaca, dia mungkin menyatakan lokasi atau tarikh. Bot perlu dapat memahami entiti tersebut, dan mengisi slot parameter dengan sewajarnya sebelum melaksanakan tindakan. Inilah tepatnya di mana NER memainkan peranan.

> ✅ Contoh lain ialah [menganalisis kertas kerja perubatan saintifik](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Salah satu perkara utama yang perlu dicari ialah istilah perubatan tertentu, seperti penyakit dan bahan perubatan. Walaupun sebilangan kecil penyakit mungkin boleh diekstrak menggunakan carian substring, entiti yang lebih kompleks, seperti sebatian kimia dan nama ubat, memerlukan pendekatan yang lebih kompleks.

## NER sebagai Klasifikasi Token

Model NER pada asasnya adalah **model klasifikasi token**, kerana untuk setiap token input kita perlu menentukan sama ada ia tergolong dalam entiti atau tidak, dan jika ya - kepada kelas entiti yang mana.

Pertimbangkan tajuk kertas kerja berikut:

**Tricuspid valve regurgitation** dan **lithium carbonate** **toxicity** dalam bayi baru lahir.

Entiti di sini ialah:

* Tricuspid valve regurgitation ialah penyakit (`DIS`)
* Lithium carbonate ialah bahan kimia (`CHEM`)
* Toxicity juga merupakan penyakit (`DIS`)

Perhatikan bahawa satu entiti boleh merangkumi beberapa token. Dan, seperti dalam kes ini, kita perlu membezakan antara dua entiti berturutan. Oleh itu, adalah biasa untuk menggunakan dua kelas bagi setiap entiti - satu untuk menentukan token pertama entiti (sering menggunakan awalan `B-` untuk **b**eginning), dan satu lagi untuk kesinambungan entiti (`I-`, untuk token **i**nner). Kita juga menggunakan `O` sebagai kelas untuk mewakili semua token **o**ther. Penandaan token seperti ini dipanggil [penandaan BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (atau IOB). Apabila ditandakan, tajuk kita akan kelihatan seperti ini:

Token | Tag
------|-----
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Oleh kerana kita perlu membina korespondensi satu-ke-satu antara token dan kelas, kita boleh melatih model rangkaian neural **many-to-many** paling kanan daripada gambar ini:

![Imej menunjukkan corak rangkaian neural berulang yang biasa.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.ms.jpg)

> *Imej daripada [catatan blog ini](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) oleh [Andrej Karpathy](http://karpathy.github.io/). Model klasifikasi token NER sepadan dengan seni bina rangkaian paling kanan dalam gambar ini.*

## Melatih Model NER

Oleh kerana model NER pada asasnya adalah model klasifikasi token, kita boleh menggunakan RNN yang telah kita pelajari untuk tugas ini. Dalam kes ini, setiap blok rangkaian berulang akan mengembalikan ID token. Notebook contoh berikut menunjukkan cara melatih LSTM untuk klasifikasi token.

## ✍️ Notebook Contoh: NER

Teruskan pembelajaran anda dalam notebook berikut:

* [NER dengan TensorFlow](NER-TF.ipynb)

## Kesimpulan

Model NER ialah **model klasifikasi token**, yang bermaksud ia boleh digunakan untuk melaksanakan klasifikasi token. Ini adalah tugas yang sangat biasa dalam NLP, membantu mengenal pasti entiti tertentu dalam teks termasuk tempat, nama, tarikh, dan banyak lagi.

## 🚀 Cabaran

Lengkapkan tugasan yang dipautkan di bawah untuk melatih model pengenalan entiti bernama untuk istilah perubatan, kemudian cuba pada set data yang berbeza.

## [Kuiz Pasca-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Kajian Semula & Kajian Kendiri

Baca melalui blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) dan ikuti bahagian Bacaan Lanjut dalam artikel tersebut untuk memperdalam pengetahuan anda.

## [Tugasan](lab/README.md)

Dalam tugasan untuk pelajaran ini, anda perlu melatih model pengenalan entiti perubatan. Anda boleh bermula dengan melatih model LSTM seperti yang diterangkan dalam pelajaran ini, dan teruskan dengan menggunakan model transformer BERT. Baca [arahan](lab/README.md) untuk mendapatkan semua butiran.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.