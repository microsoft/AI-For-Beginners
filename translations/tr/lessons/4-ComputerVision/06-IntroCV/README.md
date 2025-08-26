<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bedc8e702db17260cfe824d58b6cfd4",
  "translation_date": "2025-08-26T07:29:10+00:00",
  "source_file": "lessons/4-ComputerVision/06-IntroCV/README.md",
  "language_code": "tr"
}
-->
# Bilgisayarlı Görüye Giriş

[Bilgisayarlı Görü](https://wikipedia.org/wiki/Computer_vision), bilgisayarların dijital görüntüleri yüksek seviyede anlamasını sağlamayı amaçlayan bir disiplindir. Bu oldukça geniş bir tanımdır çünkü *anlama* birçok farklı şeyi ifade edebilir; bir resimdeki nesneyi bulmak (**nesne tespiti**), ne olduğunu anlamak (**olay tespiti**), bir resmi metinle açıklamak veya bir sahneyi 3D olarak yeniden oluşturmak gibi. İnsan görüntüleriyle ilgili özel görevler de vardır: yaş ve duygu tahmini, yüz tespiti ve tanımlama, 3D duruş tahmini gibi.

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Bilgisayarlı görünün en basit görevlerinden biri **görüntü sınıflandırmasıdır**.

Bilgisayarlı görü genellikle yapay zekanın bir dalı olarak kabul edilir. Günümüzde, bilgisayarlı görü görevlerinin çoğu sinir ağları kullanılarak çözülmektedir. Bu bölümde, bilgisayarlı görü için kullanılan özel bir sinir ağı türü olan [evrişimli sinir ağlarını](../07-ConvNets/README.md) öğreneceğiz.

Ancak, bir görüntüyü sinir ağına göndermeden önce, birçok durumda görüntüyü iyileştirmek için bazı algoritmik teknikleri kullanmak mantıklı olabilir.

Görüntü işleme için kullanılabilecek birkaç Python kütüphanesi vardır:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** farklı görüntü formatlarını okumak/yazmak için kullanılabilir. Ayrıca, video karelerini görüntülere dönüştürmek için kullanışlı bir araç olan ffmpeg'i destekler.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (PIL olarak da bilinir) biraz daha güçlüdür ve morfing, palet ayarlamaları gibi bazı görüntü manipülasyonlarını da destekler.
* **[OpenCV](https://opencv.org/)**, C++ ile yazılmış güçlü bir görüntü işleme kütüphanesidir ve görüntü işleme için *de facto* standart haline gelmiştir. Kullanışlı bir Python arayüzüne sahiptir.
* **[dlib](http://dlib.net/)**, birçok makine öğrenimi algoritmasını, bilgisayarlı görü algoritmaları da dahil olmak üzere, uygulayan bir C++ kütüphanesidir. Python arayüzüne sahiptir ve yüz ve yüz işaretleri tespiti gibi zorlu görevler için kullanılabilir.

## OpenCV

[OpenCV](https://opencv.org/), görüntü işleme için *de facto* standart olarak kabul edilir. C++ ile uygulanmış birçok kullanışlı algoritma içerir. OpenCV'yi Python'dan da çağırabilirsiniz.

OpenCV öğrenmek için iyi bir başlangıç noktası [bu Learn OpenCV kursudur](https://learnopencv.com/getting-started-with-opencv/). Müfredatımızda amacımız OpenCV'yi öğrenmek değil, onun ne zaman ve nasıl kullanılabileceğine dair bazı örnekler göstermektir.

### Görüntü Yükleme

Python'da görüntüler, NumPy dizileriyle kolayca temsil edilebilir. Örneğin, 320x200 piksel boyutundaki gri tonlamalı görüntüler 200x320 boyutunda bir dizi olarak saklanır ve aynı boyuttaki renkli görüntüler 200x320x3 şeklinde bir boyuta sahip olur (3 renk kanalı için). Bir görüntüyü yüklemek için şu kodu kullanabilirsiniz:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Geleneksel olarak, OpenCV renkli görüntüler için BGR (Mavi-Yeşil-Kırmızı) kodlamasını kullanır, oysa Python araçlarının geri kalanı daha geleneksel olan RGB (Kırmızı-Yeşil-Mavi) kodlamasını kullanır. Görüntünün doğru görünmesi için, renk uzayını RGB'ye dönüştürmeniz gerekir; bunu NumPy dizisindeki boyutları değiştirerek veya bir OpenCV fonksiyonunu çağırarak yapabilirsiniz:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Aynı `cvtColor` fonksiyonu, bir görüntüyü gri tonlamaya veya HSV (Ton-Doygunluk-Değer) renk uzayına dönüştürmek gibi diğer renk uzayı dönüşümleri için de kullanılabilir.

OpenCV'yi kullanarak videoyu kare kare yükleyebilirsiniz - bir örnek [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) alıştırmasında verilmiştir.

### Görüntü İşleme

Bir görüntüyü sinir ağına göndermeden önce, birkaç ön işleme adımı uygulamak isteyebilirsiniz. OpenCV birçok şeyi yapabilir, örneğin:

* Görüntüyü `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)` kullanarak **yeniden boyutlandırma**.
* Görüntüyü `im = cv2.medianBlur(im,3)` veya `im = cv2.GaussianBlur(im, (3,3), 0)` kullanarak **bulanıklaştırma**.
* Görüntünün **parlaklığını ve kontrastını değiştirme**, NumPy dizi manipülasyonlarıyla yapılabilir, [bu Stackoverflow notunda](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv) açıklandığı gibi.
* [Eşikleme](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) kullanarak `cv2.threshold`/`cv2.adaptiveThreshold` fonksiyonlarını çağırmak, genellikle parlaklık veya kontrast ayarlamaktan daha tercih edilir.
* Görüntüye farklı [dönüşümler](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) uygulamak:
    - **[Affine dönüşümler](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)**, görüntüdeki üç noktanın kaynak ve hedef konumlarını bildiğinizde döndürme, yeniden boyutlandırma ve eğme işlemlerini birleştirmeniz gerektiğinde kullanışlı olabilir. Affine dönüşümler paralel çizgileri paralel tutar.
    - **[Perspektif dönüşümler](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)**, görüntüdeki dört noktanın kaynak ve hedef konumlarını bildiğinizde kullanışlı olabilir. Örneğin, bir akıllı telefon kamerasıyla bir dikdörtgen belgeyi bir açıdan çektiğinizde, belgenin kendisinin dikdörtgen bir görüntüsünü oluşturmak istiyorsanız.
* **[Optik akış](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** kullanarak görüntü içindeki hareketi anlamak.

## Bilgisayarlı Görü Kullanım Örnekleri

[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)'ta, bilgisayarlı görünün belirli görevleri gerçekleştirmek için nasıl kullanılabileceğine dair bazı örnekler veriyoruz:

* **Bir Braille kitabının fotoğrafını ön işleme**. Eşikleme, özellik tespiti, perspektif dönüşümü ve NumPy manipülasyonlarını kullanarak bireysel Braille sembollerini ayırmaya odaklanıyoruz, böylece bunlar bir sinir ağı tarafından sınıflandırılabilir.

![Braille Görüntüsü](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.tr.jpeg) | ![Braille Görüntüsü Ön İşlenmiş](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.tr.png) | ![Braille Sembolleri](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.tr.png)
----|-----|-----

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)'den alınmıştır.

* **Kare farkı kullanarak videoda hareket tespiti**. Kamera sabitse, kamera akışındaki kareler birbirine oldukça benzer olmalıdır. Kareler diziler olarak temsil edildiğinden, iki ardışık kare için bu dizileri çıkardığınızda piksel farkını elde edersiniz; bu fark statik kareler için düşük, görüntüde önemli bir hareket olduğunda ise yüksek olur.

![Video kareleri ve kare farklarının görüntüsü](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.tr.png)

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)'den alınmıştır.

* **Optik Akış kullanarak hareket tespiti**. [Optik akış](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html), video karelerindeki bireysel piksellerin nasıl hareket ettiğini anlamamızı sağlar. İki tür optik akış vardır:

   - **Yoğun Optik Akış**, her pikselin nereye hareket ettiğini gösteren vektör alanını hesaplar.
   - **Seyrek Optik Akış**, görüntüdeki bazı belirgin özellikleri (ör. kenarlar) alır ve bunların kareden kareye hareket yolunu oluşturur.

![Optik Akış Görüntüsü](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.tr.png)

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)'den alınmıştır.

## ✍️ Örnek Not Defterleri: OpenCV [OpenCV'yi Eylemde Deneyin](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)'u keşfederek OpenCV ile bazı deneyler yapalım.

## Sonuç

Bazen, hareket tespiti veya parmak ucu tespiti gibi nispeten karmaşık görevler yalnızca bilgisayarlı görü ile çözülebilir. Bu nedenle, bilgisayarlı görünün temel tekniklerini ve OpenCV gibi kütüphanelerin neler yapabileceğini bilmek çok faydalıdır.

## 🚀 Zorluk

AI Show'daki [bu videoyu](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) izleyerek Cortic Tigers projesini ve bilgisayarlı görü görevlerini bir robot aracılığıyla demokratikleştirmek için nasıl blok tabanlı bir çözüm geliştirdiklerini öğrenin. Yeni öğrenenleri bu alana kazandırmaya yardımcı olan diğer projeler hakkında araştırma yapın.

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## İnceleme ve Kendi Kendine Çalışma

Optik akış hakkında daha fazla bilgi için [bu harika eğiticiye](https://learnopencv.com/optical-flow-in-opencv/) göz atın.

## [Ödev](lab/README.md)

Bu laboratuvarda, basit jestlerle bir video çekeceksiniz ve amacınız optik akış kullanarak yukarı/aşağı/sol/sağ hareketlerini çıkarmak olacak.

<img src="images/palm-movement.png" width="30%" alt="Avuç İçi Hareketi Çerçevesi"/>

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.