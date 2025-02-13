### YOLO - Anda Hanya Melihat Sekali

YOLO adalah algoritma satu kali yang berjalan secara langsung. Idea utamanya adalah seperti berikut:

* Imej dibahagikan kepada $S\times S$ kawasan
* Untuk setiap kawasan, **CNN** meramalkan $n$ objek yang mungkin, koordinat *bounding box* dan *confidence* = *probability* * IoU.

![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.ms.png)
> Gambar dari [kertas rasmi](https://arxiv.org/abs/1506.02640)

### Algoritma Lain

* RetinaNet: [kertas rasmi](https://arxiv.org/abs/1708.02002)
   - [Pelaksanaan PyTorch dalam Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Pelaksanaan Keras](https://github.com/fizyr/keras-retinanet)
   - [Pengesanan Objek dengan RetinaNet](https://keras.io/examples/vision/retinanet/) dalam Contoh Keras
* SSD (Detektor Satu Tembakan): [kertas rasmi](https://arxiv.org/abs/1512.02325)

## ✍️ Latihan: Pengesanan Objek

Teruskan pembelajaran anda dalam buku nota berikut:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Kesimpulan

Dalam pelajaran ini, anda telah mengambil lawatan pantas melalui pelbagai cara pengesanan objek boleh dicapai!

## 🚀 Cabaran

Baca artikel dan buku nota ini tentang YOLO dan cuba sendiri

* [Catatan blog yang baik](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) yang menerangkan YOLO
 * [Laman rasmi](https://pjreddie.com/darknet/yolo/)
 * Yolo: [pelaksanaan Keras](https://github.com/experiencor/keras-yolo2), [buku nota langkah demi langkah](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [pelaksanaan Keras](https://github.com/experiencor/keras-yolo2), [buku nota langkah demi langkah](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Kuiz selepas kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Ulasan & Kajian Diri

* [Pengesanan Objek](https://tjmachinelearning.com/lectures/1718/obj/) oleh Nikhil Sardana
* [Perbandingan yang baik tentang algoritma pengesanan objek](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Ulasan Algoritma Pembelajaran Mendalam untuk Pengesanan Objek](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Pengenalan Langkah demi Langkah kepada Algoritma Pengesanan Objek Asas](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Pelaksanaan Faster R-CNN dalam Python untuk Pengesanan Objek](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Tugasan: Pengesanan Objek](lab/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.