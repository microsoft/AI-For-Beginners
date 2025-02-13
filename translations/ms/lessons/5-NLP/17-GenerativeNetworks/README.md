# Jaringan Generatif

## [Kuiz Pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Jaringan Saraf Tiruan Berulang (RNN) dan varian sel tergeraknya seperti Sel Memori Jangka Panjang Pendek (LSTM) dan Unit Berulang Tergerak (GRU) menyediakan mekanisme untuk pemodelan bahasa dengan cara mereka dapat mempelajari urutan kata dan memberikan prediksi untuk kata berikutnya dalam sebuah urutan. Ini memungkinkan kita menggunakan RNN untuk **tugas generatif**, seperti pembuatan teks biasa, terjemahan mesin, dan bahkan penulisan keterangan gambar.

> ✅ Pikirkan tentang semua kali Anda mendapat manfaat dari tugas generatif seperti penyelesaian teks saat Anda mengetik. Lakukan riset tentang aplikasi favorit Anda untuk melihat apakah mereka memanfaatkan RNN.

Dalam arsitektur RNN yang kita diskusikan di unit sebelumnya, setiap unit RNN menghasilkan keadaan tersembunyi berikutnya sebagai output. Namun, kita juga dapat menambahkan output lain ke setiap unit berulang, yang memungkinkan kita untuk mengeluarkan sebuah **urutan** (yang panjangnya sama dengan urutan asli). Selain itu, kita dapat menggunakan unit RNN yang tidak menerima input di setiap langkah, dan hanya mengambil beberapa vektor keadaan awal, lalu menghasilkan urutan output.

Ini memungkinkan berbagai arsitektur neural yang ditunjukkan dalam gambar di bawah ini:

![Gambar yang menunjukkan pola jaringan saraf berulang yang umum.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.ms.jpg)

> Gambar dari pos blog [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) oleh [Andrej Karpaty](http://karpathy.github.io/)

* **Satu-ke-satu** adalah jaringan saraf tradisional dengan satu input dan satu output
* **Satu-ke-banyak** adalah arsitektur generatif yang menerima satu nilai input, dan menghasilkan urutan nilai output. Misalnya, jika kita ingin melatih jaringan **penulisan keterangan gambar** yang akan menghasilkan deskripsi teks dari sebuah gambar, kita dapat menggunakan gambar sebagai input, mengoperasikannya melalui CNN untuk mendapatkan keadaan tersembunyi, dan kemudian memiliki rantai berulang yang menghasilkan keterangan kata demi kata
* **Banyak-ke-satu** sesuai dengan arsitektur RNN yang kita jelaskan di unit sebelumnya, seperti klasifikasi teks
* **Banyak-ke-banyak**, atau **urutan-ke-urutan** sesuai dengan tugas seperti **terjemahan mesin**, di mana kita memiliki RNN pertama yang mengumpulkan semua informasi dari urutan input ke dalam keadaan tersembunyi, dan rantai RNN lainnya menguraikan keadaan ini menjadi urutan output.

Dalam unit ini, kita akan fokus pada model generatif sederhana yang membantu kita menghasilkan teks. Untuk kesederhanaan, kita akan menggunakan tokenisasi tingkat karakter.

Kita akan melatih RNN ini untuk menghasilkan teks langkah demi langkah. Pada setiap langkah, kita akan mengambil urutan karakter dengan panjang `nchars`, dan meminta jaringan untuk menghasilkan karakter output berikutnya untuk setiap karakter input:

![Gambar yang menunjukkan contoh RNN menghasilkan kata 'HELLO'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.ms.png)

Saat menghasilkan teks (selama inferensi), kita mulai dengan beberapa **prompt**, yang diteruskan melalui sel RNN untuk menghasilkan keadaan intermediatenya, dan kemudian dari keadaan ini, generasi dimulai. Kita menghasilkan satu karakter pada satu waktu, dan meneruskan keadaan dan karakter yang dihasilkan ke sel RNN lainnya untuk menghasilkan karakter berikutnya, sampai kita menghasilkan cukup karakter.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Gambar oleh penulis

## ✍️ Latihan: Jaringan Generatif

Lanjutkan pembelajaran Anda di notebook berikut:

* [Jaringan Generatif dengan PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Jaringan Generatif dengan TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Generasi teks lembut dan suhu

Output dari setiap sel RNN adalah distribusi probabilitas karakter. Jika kita selalu mengambil karakter dengan probabilitas tertinggi sebagai karakter berikutnya dalam teks yang dihasilkan, teks sering kali bisa menjadi "terulang" antara urutan karakter yang sama berulang kali, seperti dalam contoh ini:

```
today of the second the company and a second the company ...
```

Namun, jika kita melihat distribusi probabilitas untuk karakter berikutnya, bisa jadi bahwa perbedaan antara beberapa probabilitas tertinggi tidak besar, misalnya, satu karakter bisa memiliki probabilitas 0.2, karakter lain - 0.19, dan seterusnya. Misalnya, saat mencari karakter berikutnya dalam urutan '*play*', karakter berikutnya bisa sama baiknya menjadi spasi, atau **e** (seperti dalam kata *player*).

Ini membawa kita pada kesimpulan bahwa tidak selalu "adil" untuk memilih karakter dengan probabilitas lebih tinggi, karena memilih karakter kedua tertinggi mungkin masih membawa kita ke teks yang bermakna. Lebih bijaksana untuk **mengambil sampel** karakter dari distribusi probabilitas yang diberikan oleh output jaringan. Kita juga dapat menggunakan parameter, **suhu**, yang akan meratakan distribusi probabilitas, jika kita ingin menambahkan lebih banyak kebetulan, atau membuatnya lebih curam, jika kita ingin tetap lebih pada karakter dengan probabilitas tertinggi.

Jelajahi bagaimana generasi teks lembut ini diimplementasikan dalam notebook yang terhubung di atas.

## Kesimpulan

Meskipun generasi teks mungkin berguna dengan sendirinya, manfaat utama datang dari kemampuan untuk menghasilkan teks menggunakan RNN dari beberapa vektor fitur awal. Misalnya, generasi teks digunakan sebagai bagian dari terjemahan mesin (urutan-ke-urutan, dalam hal ini vektor keadaan dari *encoder* digunakan untuk menghasilkan atau *menguraikan* pesan yang diterjemahkan), atau menghasilkan deskripsi tekstual dari sebuah gambar (di mana vektor fitur akan berasal dari ekstraktor CNN).

## 🚀 Tantangan

Ambil beberapa pelajaran di Microsoft Learn tentang topik ini

* Generasi Teks dengan [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Kuiz Pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Tinjauan & Studi Mandiri

Berikut adalah beberapa artikel untuk memperluas pengetahuan Anda

* Berbagai pendekatan untuk generasi teks dengan Rantai Markov, LSTM, dan GPT-2: [pos blog](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Contoh generasi teks dalam [dokumentasi Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Tugas](lab/README.md)

Kita telah melihat bagaimana cara menghasilkan teks karakter demi karakter. Dalam lab, Anda akan menjelajahi generasi teks tingkat kata.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.