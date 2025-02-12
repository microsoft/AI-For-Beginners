# Rangkaian Pra-latih dan Pembelajaran Pemindahan

Melatih CNN boleh memakan banyak masa, dan banyak data diperlukan untuk tugas tersebut. Namun, banyak masa dihabiskan untuk mempelajari penapis rendah yang terbaik yang boleh digunakan oleh rangkaian untuk mengekstrak corak dari imej. Satu soalan yang timbul - bolehkah kita menggunakan rangkaian neural yang dilatih pada satu set data dan menyesuaikannya untuk mengklasifikasikan imej yang berbeza tanpa memerlukan proses latihan penuh?

## [Kuis Pra-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Pendekatan ini dipanggil **pembelajaran pemindahan**, kerana kita memindahkan beberapa pengetahuan dari satu model rangkaian neural ke model lain. Dalam pembelajaran pemindahan, kita biasanya bermula dengan model pra-latih, yang telah dilatih pada set data imej besar, seperti **ImageNet**. Model-model tersebut sudah boleh melakukan tugas yang baik dalam mengekstrak pelbagai ciri dari imej generik, dan dalam banyak kes, hanya membina pengklasifikasi di atas ciri-ciri yang diekstrak boleh menghasilkan keputusan yang baik.

> ✅ Pembelajaran Pemindahan adalah istilah yang anda temui dalam bidang akademik lain, seperti Pendidikan. Ia merujuk kepada proses mengambil pengetahuan dari satu domain dan menerapkannya ke domain lain.

## Model Pra-latih sebagai Pengambil Ciri

Rangkaian konvolusi yang telah kita bincangkan dalam bahagian sebelumnya mengandungi beberapa lapisan, masing-masing bertujuan untuk mengekstrak beberapa ciri dari imej, bermula dari gabungan piksel rendah (seperti garis mendatar/menegak atau strok), sehingga gabungan ciri yang lebih tinggi, yang sepadan dengan perkara seperti mata api. Jika kita melatih CNN pada set data yang cukup besar dengan imej generik dan pelbagai, rangkaian tersebut seharusnya belajar untuk mengekstrak ciri-ciri umum tersebut.

Kedua-dua Keras dan PyTorch mengandungi fungsi untuk memuatkan berat rangkaian neural pra-latih dengan mudah untuk beberapa seni bina biasa, kebanyakannya dilatih pada imej ImageNet. Yang paling sering digunakan diterangkan di halaman [Seni Bina CNN](../07-ConvNets/CNN_Architectures.md) dari pelajaran sebelumnya. Secara khusus, anda mungkin ingin mempertimbangkan untuk menggunakan salah satu daripada yang berikut:

* **VGG-16/VGG-19** yang merupakan model yang relatif sederhana tetapi masih memberikan ketepatan yang baik. Menggunakan VGG sebagai percubaan pertama sering kali merupakan pilihan yang baik untuk melihat bagaimana pembelajaran pemindahan berfungsi.
* **ResNet** adalah keluarga model yang dicadangkan oleh Microsoft Research pada tahun 2015. Mereka mempunyai lebih banyak lapisan, dan dengan itu memerlukan lebih banyak sumber.
* **MobileNet** adalah keluarga model dengan saiz yang dikurangkan, sesuai untuk peranti mudah alih. Gunakan mereka jika anda kekurangan sumber dan boleh mengorbankan sedikit ketepatan.

Berikut adalah ciri-ciri contoh yang diekstrak dari gambar kucing oleh rangkaian VGG-16:

![Ciri yang diekstrak oleh VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.ms.png)

## Dataset Kucing vs. Anjing

Dalam contoh ini, kita akan menggunakan dataset [Kucing dan Anjing](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), yang sangat dekat dengan senario pengklasifikasian imej dalam kehidupan sebenar.

## ✍️ Latihan: Pembelajaran Pemindahan

Mari kita lihat pembelajaran pemindahan dalam tindakan dalam nota-nota yang berkaitan:

* [Pembelajaran Pemindahan - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Pembelajaran Pemindahan - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Memvisualisasikan Kucing Adversarial

Rangkaian neural pra-latih mengandungi pelbagai corak di dalam *otaknya*, termasuk konsep **kucing ideal** (serta anjing ideal, zebra ideal, dan lain-lain). Ia akan menjadi menarik untuk **memvisualisasikan imej ini**. Namun, ia tidak mudah, kerana corak tersebar di seluruh berat rangkaian, dan juga teratur dalam struktur hierarki.

Salah satu pendekatan yang boleh kita ambil adalah dengan memulakan dengan imej rawak, dan kemudian cuba menggunakan teknik **pengoptimuman penurunan gradien** untuk menyesuaikan imej tersebut sedemikian rupa, sehingga rangkaian mula berfikir bahawa ia adalah kucing.

![Gelung Pengoptimuman Imej](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.ms.png)

Namun, jika kita melakukan ini, kita akan menerima sesuatu yang sangat mirip dengan bunyi rawak. Ini kerana *terdapat banyak cara untuk membuat rangkaian berfikir imej input adalah kucing*, termasuk beberapa yang tidak masuk akal secara visual. Walaupun imej-imej tersebut mengandungi banyak corak yang tipikal untuk kucing, tidak ada yang membataskan mereka untuk menjadi secara visual tersendiri.

Untuk meningkatkan hasil, kita boleh menambah satu lagi terma ke dalam fungsi kehilangan, yang dipanggil **kerugian variasi**. Ia adalah metrik yang menunjukkan betapa serupa piksel-piksel bersebelahan imej tersebut. Meminimumkan kerugian variasi menjadikan imej lebih lancar, dan menghilangkan bunyi - dengan itu mendedahkan lebih banyak corak yang menarik secara visual. Berikut adalah contoh "imej ideal" yang diklasifikasikan sebagai kucing dan sebagai zebra dengan kebarangkalian tinggi:

![Kucing Ideal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.ms.png) | ![Zebra Ideal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.ms.png)
-----|-----
 *Kucing Ideal* | *Zebra Ideal*

Pendekatan serupa boleh digunakan untuk melakukan apa yang dipanggil **serangan adversarial** pada rangkaian neural. Anggap kita ingin menipu rangkaian neural dan membuat anjing kelihatan seperti kucing. Jika kita mengambil imej anjing, yang dikenali oleh rangkaian sebagai anjing, kita boleh kemudian mengubahnya sedikit menggunakan pengoptimuman penurunan gradien, sehingga rangkaian mula mengklasifikasikannya sebagai kucing:

![Gambar Anjing](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.ms.png) | ![Gambar anjing yang diklasifikasikan sebagai kucing](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.ms.png)
-----|-----
*Gambar asal anjing* | *Gambar anjing yang diklasifikasikan sebagai kucing*

Lihat kod untuk menghasilkan keputusan di atas dalam nota berikut:

* [Kucing Ideal dan Adversarial - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)
## Kesimpulan

Dengan menggunakan pembelajaran pemindahan, anda dapat dengan cepat menyusun pengklasifikasi untuk tugas pengklasifikasian objek khusus dan mencapai ketepatan yang tinggi. Anda dapat melihat bahawa tugas yang lebih kompleks yang kita selesaikan sekarang memerlukan kuasa pengkomputeran yang lebih tinggi, dan tidak dapat diselesaikan dengan mudah di CPU. Dalam unit seterusnya, kita akan cuba menggunakan pelaksanaan yang lebih ringan untuk melatih model yang sama menggunakan sumber pengkomputeran yang lebih rendah, yang menghasilkan ketepatan yang sedikit lebih rendah.

## 🚀 Cabaran

Dalam nota-nota yang menyertai, terdapat catatan di bahagian bawah tentang bagaimana pemindahan pengetahuan berfungsi dengan terbaik dengan data latihan yang agak serupa (mungkin jenis haiwan baru). Lakukan beberapa eksperimen dengan jenis imej yang sepenuhnya baru untuk melihat seberapa baik atau buruk model pemindahan pengetahuan anda berfungsi.

## [Kuis Pasca-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Ulasan & Pembelajaran Sendiri

Baca melalui [TrainingTricks.md](TrainingTricks.md) untuk mendalami pengetahuan anda tentang beberapa cara lain untuk melatih model anda.

## [Tugasan](lab/README.md)

Dalam lab ini, kita akan menggunakan dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) dengan 35 baka kucing dan anjing, dan kita akan membina pengklasifikasi pembelajaran pemindahan.

**Penafian**: 
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.