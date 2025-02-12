# Pengenalan kepada Visi Komputer

[Visi Komputer](https://wikipedia.org/wiki/Computer_vision) adalah disiplin yang bertujuan untuk membolehkan komputer memperoleh pemahaman yang mendalam tentang imej digital. Ini adalah definisi yang agak luas, kerana *pemahaman* boleh bermaksud banyak perkara yang berbeza, termasuk mencari objek dalam gambar (**pengesanan objek**), memahami apa yang berlaku (**pengesanan peristiwa**), menggambarkan gambar dalam teks, atau membina semula satu adegan dalam 3D. Terdapat juga tugas khusus yang berkaitan dengan imej manusia: penilaian umur dan emosi, pengesanan dan pengenalan wajah, serta penilaian pose 3D, untuk menyebut beberapa.

## [Kuiz pra-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Salah satu tugas paling mudah dalam visi komputer adalah **klasifikasi imej**.

Visi komputer sering dianggap sebagai cabang AI. Pada masa kini, kebanyakan tugas visi komputer diselesaikan menggunakan rangkaian neural. Kita akan belajar lebih lanjut tentang jenis khusus rangkaian neural yang digunakan untuk visi komputer, [rangkaian neural konvolusional](../07-ConvNets/README.md), sepanjang bahagian ini.

Namun, sebelum anda menghantar imej ke rangkaian neural, dalam banyak kes adalah masuk akal untuk menggunakan beberapa teknik algoritma untuk meningkatkan imej.

Terdapat beberapa pustaka Python yang tersedia untuk pemprosesan imej:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** boleh digunakan untuk membaca/menulis pelbagai format imej. Ia juga menyokong ffmpeg, alat berguna untuk menukar bingkai video kepada imej.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (juga dikenali sebagai PIL) adalah sedikit lebih berkuasa, dan juga menyokong beberapa manipulasi imej seperti morfing, penyesuaian palet, dan banyak lagi.
* **[OpenCV](https://opencv.org/)** adalah pustaka pemprosesan imej yang kuat ditulis dalam C++, yang telah menjadi standard *de facto* untuk pemprosesan imej. Ia mempunyai antara muka Python yang mudah digunakan.
* **[dlib](http://dlib.net/)** adalah pustaka C++ yang melaksanakan banyak algoritma pembelajaran mesin, termasuk beberapa algoritma Visi Komputer. Ia juga mempunyai antara muka Python, dan boleh digunakan untuk tugas yang mencabar seperti pengesanan wajah dan tanda landmark wajah.

## OpenCV

[OpenCV](https://opencv.org/) dianggap sebagai standard *de facto* untuk pemprosesan imej. Ia mengandungi banyak algoritma berguna, dilaksanakan dalam C++. Anda juga boleh memanggil OpenCV dari Python.

Tempat yang baik untuk belajar OpenCV adalah [kursus Learn OpenCV ini](https://learnopencv.com/getting-started-with-opencv/). Dalam kurikulum kami, matlamat kami bukan untuk belajar OpenCV, tetapi untuk menunjukkan kepada anda beberapa contoh di mana ia boleh digunakan, dan bagaimana.

### Memuatkan Imej

Imej dalam Python boleh diwakili dengan mudah oleh array NumPy. Sebagai contoh, imej grayscale dengan saiz 320x200 piksel akan disimpan dalam array 200x320, dan imej berwarna dengan dimensi yang sama akan mempunyai bentuk 200x320x3 (untuk 3 saluran warna). Untuk memuatkan imej, anda boleh menggunakan kod berikut:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Secara tradisional, OpenCV menggunakan pengkodan BGR (Biru-Hijau-Merah) untuk imej berwarna, sementara alat Python yang lain menggunakan RGB (Merah-Hijau-Biru) yang lebih tradisional. Agar imej kelihatan betul, anda perlu menukarnya ke ruang warna RGB, sama ada dengan menukar dimensi dalam array NumPy, atau dengan memanggil fungsi OpenCV:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Fungsi `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` yang sama, yang sering lebih baik daripada menyesuaikan kecerahan atau kontras.
* Menerapkan pelbagai [transformasi](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) pada imej:
    - **[Transformasi Afine](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** boleh berguna jika anda perlu menggabungkan putaran, pengubahsuaian saiz dan penggayaan pada imej dan anda tahu lokasi sumber dan destinasi bagi tiga titik dalam imej. Transformasi afine mengekalkan garis selari.
    - **[Transformasi Perspektif](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** boleh berguna apabila anda tahu posisi sumber dan destinasi bagi 4 titik dalam imej. Sebagai contoh, jika anda mengambil gambar dokumen segi empat tepat melalui kamera telefon pintar dari sudut tertentu, dan anda ingin menghasilkan imej segi empat tepat dokumen itu sendiri.
* Memahami pergerakan dalam imej dengan menggunakan **[aliran optik](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Contoh penggunaan Visi Komputer

Dalam [Notebook OpenCV kami](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb), kami memberikan beberapa contoh di mana visi komputer boleh digunakan untuk melaksanakan tugas tertentu:

* **Pra-pemprosesan gambar buku Braille**. Kami memberi tumpuan kepada bagaimana kami boleh menggunakan penetapan ambang, pengesanan ciri, transformasi perspektif dan manipulasi NumPy untuk memisahkan simbol Braille individu untuk pengelasan selanjutnya oleh rangkaian neural.

![Imej Braille](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.ms.jpeg) | ![Imej Braille yang telah dipra-pemproses](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.ms.png) | ![Simbol Braille](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.ms.png)
----|-----|-----

> Imej dari [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Mengesan pergerakan dalam video menggunakan perbezaan bingkai**. Jika kamera tetap, maka bingkai dari suapan kamera seharusnya sangat serupa antara satu sama lain. Memandangkan bingkai diwakili sebagai array, dengan hanya menolak array tersebut untuk dua bingkai berturut-turut, kita akan mendapatkan perbezaan piksel, yang seharusnya rendah untuk bingkai statik, dan menjadi lebih tinggi apabila terdapat pergerakan yang ketara dalam imej.

![Imej bingkai video dan perbezaan bingkai](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.ms.png)

> Imej dari [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Mengesan pergerakan menggunakan Aliran Optik**. [Aliran optik](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) membolehkan kita memahami bagaimana piksel individu pada bingkai video bergerak. Terdapat dua jenis aliran optik:

   - **Aliran Optik Padat** mengira medan vektor yang menunjukkan untuk setiap piksel di mana ia bergerak
   - **Aliran Optik Jarang** berdasarkan pengambilan beberapa ciri khas dalam imej (contohnya, tepi), dan membina trajektori mereka dari bingkai ke bingkai.

![Imej Aliran Optik](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.ms.png)

> Imej dari [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Notebook Contoh: OpenCV [cuba OpenCV dalam Tindakan](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Mari kita lakukan beberapa eksperimen dengan OpenCV dengan meneroka [Notebook OpenCV](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## Kesimpulan

Kadang-kadang, tugas yang agak kompleks seperti pengesanan pergerakan atau pengesanan hujung jari boleh diselesaikan hanya dengan visi komputer. Oleh itu, adalah sangat berguna untuk mengetahui teknik asas visi komputer, dan apa yang boleh dilakukan oleh pustaka seperti OpenCV.

## 🚀 Cabaran

Tonton [video ini](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) dari rancangan AI untuk belajar tentang projek Cortic Tigers dan bagaimana mereka membina penyelesaian berasaskan blok untuk mendemokrasikan tugas visi komputer melalui robot. Lakukan sedikit penyelidikan tentang projek lain seperti ini yang membantu memudahkan pembelajaran baru dalam bidang ini.

## [Kuiz pasca-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Ulasan & Pembelajaran Sendiri

Baca lebih lanjut mengenai aliran optik [dalam tutorial hebat ini](https://learnopencv.com/optical-flow-in-opencv/).

## [Tugasan](lab/README.md)

Dalam lab ini, anda akan merakam video dengan gerakan sederhana, dan matlamat anda adalah untuk mengekstrak pergerakan atas/bawah/kiri/kanan menggunakan aliran optik.

<img src="images/palm-movement.png" width="30%" alt="Kerangka Pergerakan Telapak Tangan"/>

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.