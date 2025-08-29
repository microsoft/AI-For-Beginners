<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-29T11:49:54+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "ms"
}
-->
# Pengesanan Objek

Model klasifikasi imej yang telah kita pelajari sebelum ini mengambil imej dan menghasilkan keputusan kategori, seperti kelas 'nombor' dalam masalah MNIST. Walau bagaimanapun, dalam banyak kes, kita bukan sahaja ingin mengetahui bahawa gambar menggambarkan objek - kita juga ingin menentukan lokasi tepat objek tersebut. Inilah tujuan utama **pengesanan objek**.

## [Kuiz Pra-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Pengesanan Objek](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.ms.png)

> Gambar dari [laman web YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Pendekatan Naif untuk Pengesanan Objek

Jika kita ingin mencari seekor kucing dalam gambar, pendekatan naif untuk pengesanan objek adalah seperti berikut:

1. Pecahkan gambar kepada beberapa jubin.
2. Jalankan klasifikasi imej pada setiap jubin.
3. Jubin yang menghasilkan pengaktifan yang cukup tinggi boleh dianggap mengandungi objek yang dicari.

![Pengesanan Objek Naif](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.ms.png)

> *Gambar dari [Exercise Notebook](ObjectDetection-TF.ipynb)*

Namun, pendekatan ini jauh dari ideal kerana ia hanya membolehkan algoritma menentukan kotak sempadan objek dengan sangat tidak tepat. Untuk lokasi yang lebih tepat, kita perlu menjalankan sejenis **regresi** untuk meramalkan koordinat kotak sempadan - dan untuk itu, kita memerlukan set data khusus.

## Regresi untuk Pengesanan Objek

[Blog post ini](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) memberikan pengenalan yang baik tentang pengesanan bentuk.

## Set Data untuk Pengesanan Objek

Anda mungkin akan menemui set data berikut untuk tugas ini:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 kelas
* [COCO](http://cocodataset.org/#home) - Common Objects in Context. 80 kelas, kotak sempadan dan topeng segmentasi

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.ms.jpg)

## Metrik Pengesanan Objek

### Intersection over Union

Untuk klasifikasi imej, mudah untuk mengukur sejauh mana algoritma berfungsi, tetapi untuk pengesanan objek, kita perlu mengukur ketepatan kelas serta ketepatan lokasi kotak sempadan yang diramalkan. Untuk yang terakhir, kita menggunakan **Intersection over Union** (IoU), yang mengukur sejauh mana dua kotak (atau dua kawasan sewenang-wenangnya) bertindih.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.ms.png)

> *Rajah 2 dari [blog post yang sangat baik tentang IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Ideanya mudah - kita membahagikan kawasan persilangan antara dua bentuk dengan kawasan gabungan mereka. Untuk dua kawasan yang sama, IoU akan menjadi 1, manakala untuk kawasan yang tidak bertindih langsung, ia akan menjadi 0. Jika tidak, ia akan berbeza dari 0 hingga 1. Kita biasanya hanya mempertimbangkan kotak sempadan yang mempunyai IoU melebihi nilai tertentu.

### Purata Ketepatan (Average Precision)

Misalkan kita ingin mengukur sejauh mana satu kelas objek $C$ dikenali. Untuk mengukurnya, kita menggunakan metrik **Purata Ketepatan** yang dikira seperti berikut:

1. Pertimbangkan lengkung Precision-Recall yang menunjukkan ketepatan bergantung pada nilai ambang pengesanan (dari 0 hingga 1).
2. Bergantung pada ambang, kita akan mendapatkan lebih banyak atau lebih sedikit objek yang dikesan dalam imej, dan nilai ketepatan serta ingatan yang berbeza.
3. Lengkungnya akan kelihatan seperti ini:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Gambar dari [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Purata Ketepatan untuk kelas $C$ tertentu adalah kawasan di bawah lengkung ini. Lebih tepat lagi, paksi Recall biasanya dibahagikan kepada 10 bahagian, dan Ketepatan diambil purata pada semua titik tersebut:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP dan IoU

Kita hanya akan mempertimbangkan pengesanan yang mempunyai IoU melebihi nilai tertentu. Sebagai contoh, dalam set data PASCAL VOC, biasanya $\mbox{IoU Threshold} = 0.5$ diandaikan, manakala dalam COCO, AP diukur untuk pelbagai nilai $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Gambar dari [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Purata Ketepatan Mean - mAP

Metrik utama untuk Pengesanan Objek dipanggil **Purata Ketepatan Mean**, atau **mAP**. Ia adalah nilai Purata Ketepatan, diambil purata merentasi semua kelas objek, dan kadang-kadang juga merentasi $\mbox{IoU Threshold}$. Proses pengiraan **mAP** dijelaskan dengan lebih terperinci
[dalam blog post ini](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), dan juga [di sini dengan contoh kod](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Pendekatan Berbeza untuk Pengesanan Objek

Terdapat dua kelas utama algoritma pengesanan objek:

* **Region Proposal Networks** (R-CNN, Fast R-CNN, Faster R-CNN). Idea utama adalah untuk menjana **Regions of Interests** (ROI) dan menjalankan CNN ke atasnya, mencari pengaktifan maksimum. Ia agak serupa dengan pendekatan naif, kecuali ROI dijana dengan cara yang lebih bijak. Salah satu kelemahan utama kaedah ini adalah ia perlahan kerana memerlukan banyak laluan pengklasifikasi CNN ke atas imej.
* **Satu-laluan** (YOLO, SSD, RetinaNet). Dalam seni bina ini, rangkaian direka untuk meramalkan kedua-dua kelas dan ROI dalam satu laluan.

### R-CNN: CNN Berasaskan Wilayah

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) menggunakan [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) untuk menjana struktur hierarki kawasan ROI, yang kemudian dilalui oleh pengekstrak ciri CNN dan pengklasifikasi SVM untuk menentukan kelas objek, serta regresi linear untuk menentukan koordinat *kotak sempadan*. [Kertas Rasmi](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.ms.png)

> *Gambar dari van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.ms.png)

> *Gambar dari [blog ini](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Pendekatan ini serupa dengan R-CNN, tetapi kawasan ditentukan selepas lapisan konvolusi diterapkan.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.ms.png)

> Gambar dari [Kertas Rasmi](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Idea utama pendekatan ini adalah menggunakan rangkaian neural untuk meramalkan ROI - yang dipanggil *Region Proposal Network*. [Kertas](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.ms.png)

> Gambar dari [kertas rasmi](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Rangkaian Konvolusi Sepenuhnya Berasaskan Wilayah

Algoritma ini lebih pantas daripada Faster R-CNN. Idea utamanya adalah seperti berikut:

1. Ekstrak ciri menggunakan ResNet-101.
2. Ciri-ciri diproses oleh **Position-Sensitive Score Map**. Setiap objek dari $C$ kelas dibahagikan kepada $k\times k$ kawasan, dan kita melatih untuk meramalkan bahagian objek.
3. Untuk setiap bahagian dari $k\times k$ kawasan, semua rangkaian mengundi untuk kelas objek, dan kelas objek dengan undian maksimum dipilih.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.ms.png)

> Gambar dari [kertas rasmi](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO adalah algoritma satu-laluan masa nyata. Idea utamanya adalah seperti berikut:

 * Imej dibahagikan kepada $S\times S$ kawasan.
 * Untuk setiap kawasan, **CNN** meramalkan $n$ objek yang mungkin, koordinat *kotak sempadan* dan *keyakinan*=*kebarangkalian* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.ms.png)

> Gambar dari [kertas rasmi](https://arxiv.org/abs/1506.02640)

### Algoritma Lain

* RetinaNet: [kertas rasmi](https://arxiv.org/abs/1708.02002)
   - [Implementasi PyTorch dalam Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementasi Keras](https://github.com/fizyr/keras-retinanet)
   - [Pengesanan Objek dengan RetinaNet](https://keras.io/examples/vision/retinanet/) dalam Keras Samples
* SSD (Single Shot Detector): [kertas rasmi](https://arxiv.org/abs/1512.02325)

## ✍️ Latihan: Pengesanan Objek

Teruskan pembelajaran anda dalam notebook berikut:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Kesimpulan

Dalam pelajaran ini, anda telah mengambil lawatan pantas tentang pelbagai cara pengesanan objek dapat dicapai!

## 🚀 Cabaran

Baca artikel dan notebook ini tentang YOLO dan cuba sendiri:

* [Blog post yang baik](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) yang menerangkan YOLO
 * [Laman rasmi](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Implementasi Keras](https://github.com/experiencor/keras-yolo2), [notebook langkah demi langkah](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Implementasi Keras](https://github.com/experiencor/keras-yolo2), [notebook langkah demi langkah](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Kuiz Pasca-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Ulasan & Kajian Kendiri

* [Pengesanan Objek](https://tjmachinelearning.com/lectures/1718/obj/) oleh Nikhil Sardana
* [Perbandingan yang baik tentang algoritma pengesanan objek](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Ulasan Algoritma Pembelajaran Mendalam untuk Pengesanan Objek](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Pengenalan Langkah demi Langkah kepada Algoritma Pengesanan Objek Asas](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementasi Faster R-CNN dalam Python untuk Pengesanan Objek](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Tugasan: Pengesanan Objek](lab/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.