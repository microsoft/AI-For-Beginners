# Jaringan Generatif

## [Kuis Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Recurrent Neural Networks (RNNs) dan varian sel ber-gate seperti Long Short Term Memory Cells (LSTMs) dan Gated Recurrent Units (GRUs) menyediakan mekanisme untuk pemodelan bahasa karena mereka dapat mempelajari urutan kata dan memberikan prediksi untuk kata berikutnya dalam sebuah urutan. Hal ini memungkinkan kita menggunakan RNN untuk **tugas generatif**, seperti pembuatan teks biasa, penerjemahan mesin, dan bahkan pembuatan keterangan gambar.

> ✅ Pikirkan semua momen di mana Anda mendapat manfaat dari tugas generatif seperti pelengkapan teks saat mengetik. Lakukan penelitian tentang aplikasi favorit Anda untuk melihat apakah mereka menggunakan RNN.

Dalam arsitektur RNN yang kita bahas di unit sebelumnya, setiap unit RNN menghasilkan status tersembunyi berikutnya sebagai output. Namun, kita juga dapat menambahkan output lain ke setiap unit rekuren, yang memungkinkan kita menghasilkan **urutan** (yang panjangnya sama dengan urutan asli). Selain itu, kita dapat menggunakan unit RNN yang tidak menerima input di setiap langkah, melainkan hanya mengambil vektor status awal, dan kemudian menghasilkan urutan output.

Hal ini memungkinkan berbagai arsitektur neural yang ditunjukkan pada gambar di bawah:

![Gambar menunjukkan pola umum jaringan neural rekuren.](../../../../../translated_images/id/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> Gambar dari blog post [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) oleh [Andrej Karpaty](http://karpathy.github.io/)

* **One-to-one** adalah jaringan neural tradisional dengan satu input dan satu output
* **One-to-many** adalah arsitektur generatif yang menerima satu nilai input, dan menghasilkan urutan nilai output. Misalnya, jika kita ingin melatih jaringan **image captioning** yang menghasilkan deskripsi teks dari sebuah gambar, kita dapat memberikan gambar sebagai input, melewatkannya melalui CNN untuk mendapatkan status tersembunyinya, dan kemudian rantai rekuren menghasilkan keterangan kata demi kata
* **Many-to-one** sesuai dengan arsitektur RNN yang kita bahas di unit sebelumnya, seperti klasifikasi teks
* **Many-to-many**, atau **sequence-to-sequence** sesuai dengan tugas seperti **penerjemahan mesin**, di mana kita memiliki RNN pertama yang mengumpulkan semua informasi dari urutan input ke dalam status tersembunyi, dan rantai RNN lainnya menguraikan status ini menjadi urutan output.

Di unit ini, kita akan fokus pada model generatif sederhana yang membantu kita menghasilkan teks. Untuk kesederhanaan, kita akan menggunakan tokenisasi tingkat karakter.

Kita akan melatih RNN ini untuk menghasilkan teks langkah demi langkah. Pada setiap langkah, kita akan mengambil urutan karakter dengan panjang `nchars`, dan meminta jaringan untuk menghasilkan karakter output berikutnya untuk setiap karakter input:

![Gambar menunjukkan contoh RNN menghasilkan kata 'HELLO'.](../../../../../translated_images/id/rnn-generate.56c54afb52f9781d.webp)

Saat menghasilkan teks (selama inferensi), kita mulai dengan beberapa **prompt**, yang dilewatkan melalui sel RNN untuk menghasilkan status intermediate-nya, dan kemudian dari status ini proses generasi dimulai. Kita menghasilkan satu karakter pada satu waktu, dan melewatkan status serta karakter yang dihasilkan ke sel RNN lainnya untuk menghasilkan karakter berikutnya, hingga kita menghasilkan cukup karakter.

<img src="../../../../../translated_images/id/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> Gambar oleh penulis

## ✍️ Latihan: Jaringan Generatif

Lanjutkan pembelajaran Anda di notebook berikut:

* [Jaringan Generatif dengan PyTorch](GenerativePyTorch.ipynb)
* [Jaringan Generatif dengan TensorFlow](GenerativeTF.ipynb)

## Pembuatan Teks Lunak dan Temperatur

Output dari setiap sel RNN adalah distribusi probabilitas karakter. Jika kita selalu mengambil karakter dengan probabilitas tertinggi sebagai karakter berikutnya dalam teks yang dihasilkan, teks sering kali dapat menjadi "berulang" antara urutan karakter yang sama berulang kali, seperti dalam contoh ini:

```
today of the second the company and a second the company ...
```

Namun, jika kita melihat distribusi probabilitas untuk karakter berikutnya, bisa jadi perbedaan antara beberapa probabilitas tertinggi tidak besar, misalnya satu karakter dapat memiliki probabilitas 0.2, dan karakter lainnya 0.19, dll. Sebagai contoh, saat mencari karakter berikutnya dalam urutan '*play*', karakter berikutnya bisa sama-sama berupa spasi, atau **e** (seperti dalam kata *player*).

Hal ini membawa kita pada kesimpulan bahwa tidak selalu "adil" untuk memilih karakter dengan probabilitas lebih tinggi, karena memilih yang kedua tertinggi masih dapat menghasilkan teks yang bermakna. Lebih bijaksana untuk **mengambil sampel** karakter dari distribusi probabilitas yang diberikan oleh output jaringan. Kita juga dapat menggunakan parameter, **temperature**, yang akan meratakan distribusi probabilitas, jika kita ingin menambahkan lebih banyak keacakan, atau membuatnya lebih curam, jika kita ingin lebih berpegang pada karakter dengan probabilitas tertinggi.

Jelajahi bagaimana pembuatan teks lunak ini diimplementasikan di notebook yang ditautkan di atas.

## Kesimpulan

Meskipun pembuatan teks mungkin berguna dengan sendirinya, manfaat utama datang dari kemampuan untuk menghasilkan teks menggunakan RNN dari beberapa vektor fitur awal. Misalnya, pembuatan teks digunakan sebagai bagian dari penerjemahan mesin (sequence-to-sequence, dalam hal ini vektor status dari *encoder* digunakan untuk menghasilkan atau *decode* pesan terjemahan), atau menghasilkan deskripsi teks dari sebuah gambar (dalam hal ini vektor fitur berasal dari ekstraktor CNN).

## 🚀 Tantangan

Ambil beberapa pelajaran di Microsoft Learn tentang topik ini

* Pembuatan Teks dengan [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Kuis Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Tinjauan & Studi Mandiri

Berikut beberapa artikel untuk memperluas pengetahuan Anda

* Pendekatan berbeda untuk pembuatan teks dengan Markov Chain, LSTM, dan GPT-2: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Contoh pembuatan teks dalam [dokumentasi Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Tugas](lab/README.md)

Kita telah melihat bagaimana menghasilkan teks karakter demi karakter. Di lab, Anda akan mengeksplorasi pembuatan teks tingkat kata.

---

