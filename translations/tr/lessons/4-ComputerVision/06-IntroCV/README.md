# Bilgisayarla Görme Giriş

[Bilgisayarla Görme](https://wikipedia.org/wiki/Computer_vision), bilgisayarların dijital görüntülerin yüksek seviyede anlaşılmasını sağlamayı amaçlayan bir disiplindir. Bu oldukça geniş bir tanımdır, çünkü *anlamak* birçok farklı anlam taşıyabilir; bir resimdeki bir nesneyi bulmak (**nesne tespiti**), ne olduğunu anlamak (**olay tespiti**), bir resmi metinle tanımlamak veya bir sahneyi 3D olarak yeniden oluşturmak gibi. Ayrıca insan görüntüleriyle ilgili özel görevler de vardır: yaş ve duygu tahmini, yüz tespiti ve kimlik doğrulama, ve 3D poz tahmini gibi birkaç örnek vermek gerekirse.

## [Ders Öncesi Sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Bilgisayarla görmenin en basit görevlerinden biri **görüntü sınıflandırması**dır.

Bilgisayarla görme genellikle AI'nın bir dalı olarak kabul edilir. Günümüzde, bilgisayarla görme görevlerinin çoğu, sinir ağları kullanılarak çözülmektedir. Bu bölüm boyunca, bilgisayarla görme için kullanılan özel bir sinir ağı türü olan [konvolüsyonel sinir ağları](../07-ConvNets/README.md) hakkında daha fazla bilgi edineceğiz.

Ancak, bir görüntüyü bir sinir ağına göndermeden önce, birçok durumda görüntüyü geliştirmek için bazı algoritmik teknikler kullanmak mantıklıdır.

Görüntü işleme için mevcut olan birkaç Python kütüphanesi vardır:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** farklı görüntü formatlarını okumak/yazmak için kullanılabilir. Ayrıca video karelerini görüntülere dönüştürmek için yararlı bir araç olan ffmpeg'i de destekler.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (aynı zamanda PIL olarak da bilinir) biraz daha güçlüdür ve morfing, palet ayarlamaları gibi bazı görüntü manipülasyonlarını da destekler.
* **[OpenCV](https://opencv.org/)** C++ ile yazılmış güçlü bir görüntü işleme kütüphanesidir ve görüntü işleme için *de facto* standart haline gelmiştir. Kullanışlı bir Python arayüzü vardır.
* **[dlib](http://dlib.net/)** birçok makine öğrenimi algoritmasını, bazı Bilgisayarla Görme algoritmalarını da içeren, C++ kütüphanesidir. Ayrıca bir Python arayüzü vardır ve yüz ve yüz özellik tespiti gibi zorlu görevler için kullanılabilir.

## OpenCV

[OpenCV](https://opencv.org/) görüntü işleme için *de facto* standart olarak kabul edilir. C++ ile uygulanmış birçok yararlı algoritma içerir. OpenCV'yi Python'dan da çağırabilirsiniz.

OpenCV öğrenmek için iyi bir yer [bu Learn OpenCV kursu](https://learnopencv.com/getting-started-with-opencv/)dır. Müfredatımızda amacımız OpenCV'yi öğrenmek değil, ne zaman ve nasıl kullanılabileceğine dair bazı örnekler göstermektir.

### Görüntü Yükleme

Python'da görüntüler, NumPy dizileri ile rahatlıkla temsil edilebilir. Örneğin, 320x200 piksel boyutundaki gri tonlamalı görüntüler 200x320 boyutunda bir dizide saklanırken, aynı boyuttaki renkli görüntüler 200x320x3 şeklinde (3 renk kanalı için) saklanır. Bir görüntü yüklemek için aşağıdaki kodu kullanabilirsiniz:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Geleneksel olarak, OpenCV renkli görüntüler için BGR (Mavi-Yeşil-Kırmızı) kodlamasını kullanırken, diğer Python araçları daha geleneksel olan RGB (Kırmızı-Yeşil-Mavi) kullanır. Görüntünün doğru görünmesi için, NumPy dizisindeki boyutları değiştirerek veya bir OpenCV fonksiyonunu çağırarak görüntüyü RGB renk alanına dönüştürmeniz gerekir:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Aynı `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` fonksiyonları, genellikle parlaklık veya kontrast ayarlamaktan daha tercih edilir.
* Görüntüye farklı [dönüşümler](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) uygulamak:
    - **[Affine dönüşümler](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)**, görüntüdeki üç noktanın kaynak ve hedef konumlarını bildiğinizde döndürme, yeniden boyutlandırma ve eğme işlemlerini birleştirmeniz gerektiğinde yararlı olabilir. Affine dönüşümler, paralel çizgileri paralel tutar.
    - **[Perspektif dönüşümler](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)**, görüntüdeki 4 noktanın kaynak ve hedef konumlarını bildiğinizde yararlı olabilir. Örneğin, bir akıllı telefon kamerasıyla bir dikdörtgen belgeyi bir açıdan çektiğinizde ve belgenin kendisinin dikdörtgen bir görüntüsünü oluşturmak istediğinizde.
* Görüntü içindeki hareketi anlamak için **[optik akış](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** kullanmak.

## Bilgisayarla Görme Kullanımına Dair Örnekler

[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) dosyamızda, bilgisayarla görmenin belirli görevleri yerine getirmek için nasıl kullanılabileceğine dair bazı örnekler veriyoruz:

* **Bir Braille kitabının fotoğrafını ön işleme**. Braille sembollerini ayrı sınıflandırma için bir sinir ağı tarafından kullanmak üzere ayırmak için eşikleme, özellik tespiti, perspektif dönüşüm ve NumPy manipülasyonlarını nasıl kullanabileceğimize odaklanıyoruz.

![Braille Görüntüsü](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.tr.jpeg) | ![Braille Görüntüsü Ön İşlemden Geçmiş](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.tr.png) | ![Braille Sembolleri](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.tr.png)
----|-----|-----

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) dosyasından alınmıştır.

* **Kare farkı kullanarak videoda hareket tespiti**. Kamera sabitse, kamera akışından gelen kareler birbirine oldukça benzer olmalıdır. Kareler diziler olarak temsil edildiğinden, iki ardışık kare için bu dizileri çıkartarak piksel farkını elde ederiz; bu, statik kareler için düşük olmalı ve görüntüde önemli bir hareket olduğunda artmalıdır.

![Video kareleri ve kare farklarının görüntüsü](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.tr.png)

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) dosyasından alınmıştır.

* **Optik Akış kullanarak hareket tespiti**. [Optik akış](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html), video karelerindeki bireysel piksellerin nasıl hareket ettiğini anlamamıza olanak tanır. İki tür optik akış vardır:

   - **Yoğun Optik Akış** her piksel için hareket ettiği yeri gösteren vektör alanını hesaplar.
   - **Seyrek Optik Akış** görüntüdeki bazı belirgin özellikleri (örneğin kenarlar) alarak ve bunların her karedeki yolunu oluşturarak çalışır.

![Optik Akış Görüntüsü](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.tr.png)

> Görüntü [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) dosyasından alınmıştır.

## ✍️ Örnek Not Defterleri: OpenCV [OpenCV'yi Eylemde Deneyin](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

OpenCV ile bazı deneyler yapmak için [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) dosyasını keşfedelim.

## Sonuç

Bazen hareket tespiti veya parmak ucu tespiti gibi nispeten karmaşık görevler tamamen bilgisayarla görme ile çözülebilir. Bu nedenle, bilgisayarla görmenin temel tekniklerini bilmek ve OpenCV gibi kütüphanelerin neler yapabileceğini anlamak çok faydalıdır.

## 🚀 Meydan Okuma

Cortical Tigers projesini ve bir robot aracılığıyla bilgisayarla görme görevlerini demokratikleştirmek için nasıl blok tabanlı bir çözüm geliştirdiklerini öğrenmek için [bu videoyu](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) izleyin. Bu alanda yeni öğrenicilerin uyum sağlamalarına yardımcı olan diğer projeler hakkında araştırma yapın.

## [Ders Sonrası Sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Gözden Geçirme ve Kendi Kendine Çalışma

Optik akış hakkında daha fazla bilgi için [bu harika öğreticide](https://learnopencv.com/optical-flow-in-opencv/) okuyun.

## [Görev](lab/README.md)

Bu laboratuvarda basit jestlerle bir video çekeceksiniz ve amacınız optik akış kullanarak yukarı/aşağı/sol/sağ hareketleri çıkarmaktır.

<img src="images/palm-movement.png" width="30%" alt="Avuç Hareketi Çerçevesi"/>

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.