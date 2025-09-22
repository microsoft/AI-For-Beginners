<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-29T11:48:15+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "ms"
}
-->
# Rangkaian Pra-latih dan Pembelajaran Pemindahan

Melatih CNN boleh mengambil masa yang lama, dan memerlukan banyak data untuk tugas tersebut. Walau bagaimanapun, sebahagian besar masa dihabiskan untuk mempelajari penapis tahap rendah terbaik yang boleh digunakan oleh rangkaian untuk mengekstrak corak daripada imej. Satu persoalan semula jadi timbul - bolehkah kita menggunakan rangkaian neural yang telah dilatih pada satu set data dan menyesuaikannya untuk mengklasifikasikan imej yang berbeza tanpa memerlukan proses latihan penuh?

## [Kuiz Pra-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Pendekatan ini dipanggil **pembelajaran pemindahan**, kerana kita memindahkan sebahagian pengetahuan daripada satu model rangkaian neural kepada yang lain. Dalam pembelajaran pemindahan, kita biasanya bermula dengan model pra-latih, yang telah dilatih pada set data imej yang besar, seperti **ImageNet**. Model-model ini sudah mampu melakukan tugas yang baik dalam mengekstrak ciri-ciri berbeza daripada imej generik, dan dalam banyak kes, hanya dengan membina pengklasifikasi di atas ciri-ciri yang diekstrak tersebut boleh memberikan hasil yang baik.

> ✅ Pembelajaran Pemindahan adalah istilah yang juga ditemui dalam bidang akademik lain, seperti Pendidikan. Ia merujuk kepada proses mengambil pengetahuan daripada satu domain dan menerapkannya kepada domain lain.

## Model Pra-latih sebagai Pengekstrak Ciri

Rangkaian konvolusi yang telah kita bincangkan dalam bahagian sebelumnya mengandungi beberapa lapisan, setiap satunya bertujuan untuk mengekstrak beberapa ciri daripada imej, bermula daripada kombinasi piksel tahap rendah (seperti garis mendatar/menegak atau strok), sehingga kombinasi ciri tahap tinggi, yang berkaitan dengan perkara seperti mata api. Jika kita melatih CNN pada set data imej yang cukup besar dan pelbagai, rangkaian tersebut sepatutnya dapat belajar untuk mengekstrak ciri-ciri umum tersebut.

Kedua-dua Keras dan PyTorch mengandungi fungsi untuk memuatkan berat rangkaian neural pra-latih dengan mudah untuk beberapa seni bina biasa, kebanyakannya telah dilatih pada imej ImageNet. Model yang paling kerap digunakan diterangkan pada halaman [Seni Bina CNN](../07-ConvNets/CNN_Architectures.md) daripada pelajaran sebelumnya. Secara khusus, anda mungkin ingin mempertimbangkan untuk menggunakan salah satu daripada berikut:

* **VGG-16/VGG-19** yang merupakan model yang agak mudah tetapi masih memberikan ketepatan yang baik. Selalunya menggunakan VGG sebagai percubaan pertama adalah pilihan yang baik untuk melihat bagaimana pembelajaran pemindahan berfungsi.
* **ResNet** adalah keluarga model yang dicadangkan oleh Microsoft Research pada tahun 2015. Model ini mempunyai lebih banyak lapisan, dan oleh itu memerlukan lebih banyak sumber.
* **MobileNet** adalah keluarga model dengan saiz yang dikurangkan, sesuai untuk peranti mudah alih. Gunakan model ini jika anda kekurangan sumber dan boleh mengorbankan sedikit ketepatan.

Berikut adalah contoh ciri yang diekstrak daripada gambar seekor kucing oleh rangkaian VGG-16:

![Ciri yang diekstrak oleh VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.ms.png)

## Dataset Kucing vs. Anjing

Dalam contoh ini, kita akan menggunakan dataset [Kucing dan Anjing](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), yang sangat hampir dengan senario klasifikasi imej kehidupan sebenar.

## ✍️ Latihan: Pembelajaran Pemindahan

Mari kita lihat pembelajaran pemindahan dalam tindakan dalam buku nota yang berkaitan:

* [Pembelajaran Pemindahan - PyTorch](TransferLearningPyTorch.ipynb)
* [Pembelajaran Pemindahan - TensorFlow](TransferLearningTF.ipynb)

## Memvisualkan Kucing Adversarial

Rangkaian neural pra-latih mengandungi pelbagai corak dalam "otaknya", termasuk konsep **kucing ideal** (serta anjing ideal, zebra ideal, dll.). Ia akan menjadi menarik untuk **memvisualkan imej ini**. Walau bagaimanapun, ia tidak mudah, kerana corak-corak ini tersebar di seluruh berat rangkaian, dan juga disusun dalam struktur hierarki.

Satu pendekatan yang boleh kita ambil adalah bermula dengan imej rawak, dan kemudian cuba menggunakan teknik **pengoptimuman penurunan kecerunan** untuk menyesuaikan imej tersebut sedemikian rupa sehingga rangkaian mula berfikir bahawa ia adalah seekor kucing.

![Gelung Pengoptimuman Imej](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.ms.png)

Walau bagaimanapun, jika kita melakukan ini, kita akan mendapat sesuatu yang sangat mirip dengan bunyi rawak. Ini kerana *terdapat banyak cara untuk membuat rangkaian berfikir imej input adalah seekor kucing*, termasuk beberapa yang tidak masuk akal secara visual. Walaupun imej-imej tersebut mengandungi banyak corak yang tipikal untuk seekor kucing, tiada apa yang menghalang mereka daripada menjadi jelas secara visual.

Untuk memperbaiki hasilnya, kita boleh menambah satu lagi istilah ke dalam fungsi kehilangan, yang dipanggil **kehilangan variasi**. Ia adalah metrik yang menunjukkan betapa serupa piksel-piksel bersebelahan dalam imej. Meminimumkan kehilangan variasi menjadikan imej lebih licin, dan menghilangkan bunyi - dengan itu mendedahkan corak yang lebih menarik secara visual. Berikut adalah contoh imej "ideal" seperti itu, yang diklasifikasikan sebagai kucing dan zebra dengan kebarangkalian tinggi:

![Kucing Ideal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.ms.png) | ![Zebra Ideal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.ms.png)
-----|-----
 *Kucing Ideal* | *Zebra Ideal*

Pendekatan serupa boleh digunakan untuk melakukan **serangan adversarial** pada rangkaian neural. Katakan kita ingin mengelirukan rangkaian neural dan membuat seekor anjing kelihatan seperti seekor kucing. Jika kita mengambil imej anjing, yang dikenali oleh rangkaian sebagai anjing, kita kemudian boleh mengubahnya sedikit menggunakan pengoptimuman penurunan kecerunan, sehingga rangkaian mula mengklasifikasikannya sebagai kucing:

![Gambar Anjing](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.ms.png) | ![Gambar anjing yang diklasifikasikan sebagai kucing](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.ms.png)
-----|-----
*Gambar asal seekor anjing* | *Gambar seekor anjing yang diklasifikasikan sebagai kucing*

Lihat kod untuk menghasilkan semula hasil di atas dalam buku nota berikut:

* [Kucing Ideal dan Adversarial - TensorFlow](AdversarialCat_TF.ipynb)

## Kesimpulan

Dengan menggunakan pembelajaran pemindahan, anda dapat dengan cepat membina pengklasifikasi untuk tugas klasifikasi objek tersuai dan mencapai ketepatan yang tinggi. Anda dapat melihat bahawa tugas yang lebih kompleks yang kita selesaikan sekarang memerlukan kuasa pengkomputeran yang lebih tinggi, dan tidak dapat diselesaikan dengan mudah pada CPU. Dalam unit seterusnya, kita akan cuba menggunakan pelaksanaan yang lebih ringan untuk melatih model yang sama menggunakan sumber pengkomputeran yang lebih rendah, yang menghasilkan ketepatan yang hanya sedikit lebih rendah.

## 🚀 Cabaran

Dalam buku nota yang disertakan, terdapat nota di bahagian bawah tentang bagaimana pengetahuan pemindahan berfungsi dengan baik dengan data latihan yang agak serupa (mungkin jenis haiwan baru). Lakukan beberapa eksperimen dengan jenis imej yang benar-benar baru untuk melihat sejauh mana atau buruknya model pengetahuan pemindahan anda berfungsi.

## [Kuiz Pasca-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Kajian & Pembelajaran Kendiri

Baca melalui [TrainingTricks.md](TrainingTricks.md) untuk mendalami pengetahuan anda tentang beberapa cara lain untuk melatih model anda.

## [Tugasan](lab/README.md)

Dalam makmal ini, kita akan menggunakan dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kehidupan sebenar dengan 35 baka kucing dan anjing, dan kita akan membina pengklasifikasi pembelajaran pemindahan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.