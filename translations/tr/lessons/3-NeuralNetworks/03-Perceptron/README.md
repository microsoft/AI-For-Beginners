# Sinir Ağlarına Giriş: Perceptron

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Modern sinir ağlarına benzer bir şeyi uygulama girişimlerinden biri, 1957 yılında Cornell Aeronautical Laboratory'dan Frank Rosenblatt tarafından yapılmıştır. Bu, üçgenler, kareler ve daireler gibi ilkel geometrik şekilleri tanımak için tasarlanmış "Mark-1" adlı bir donanım uygulamasıydı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Görseller [Wikipedia'dan](https://en.wikipedia.org/wiki/Perceptron)

Bir giriş resmi, 20x20 fotocel array ile temsil edildi, bu nedenle sinir ağının 400 girişi ve bir ikili çıktısı vardı. Basit bir ağ, bir **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayarlama gerektiren potansiyometreler gibi işlev görüyordu.

> ✅ Potansiyometre, kullanıcının bir devrenin direncini ayarlamasına olanak tanıyan bir cihazdır.

> New York Times o dönemde perceptron hakkında şunları yazdı: *[Donanmanın] yürüyebilen, konuşabilen, görebilen, yazabilen, kendini üretebilen ve varlığının farkında olabilen bir elektronik bilgisayar embriyosu.*

## Perceptron Modeli

Modelimizde N özellik olduğunu varsayalım, bu durumda giriş vektörü N boyutunda bir vektör olacaktır. Perceptron, **ikili sınıflandırma** modeli olup, yani iki sınıf arasındaki giriş verilerini ayırt edebilir. Her giriş vektörü x için perceptron'un çıktısının ya +1 ya da -1 olacağını varsayacağız, bu da sınıfa bağlıdır. Çıktı, aşağıdaki formül kullanılarak hesaplanacaktır:

y(x) = f(w<sup>T</sup>x)

burada f, bir adım aktivasyon fonksiyonudur.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Perceptronu Eğitmek

Bir perceptronu eğitmek için, çoğu değeri doğru sınıflandıran bir ağırlık vektörü w bulmamız gerekiyor, yani en küçük **hata** sonucunu vermek. Bu hata E, aşağıdaki şekilde **perceptron kriteri** ile tanımlanır:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırmaya neden olan o eğitim veri noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisi ve t<sub>i</sub> sırasıyla negatif ve pozitif örnekler için -1 veya +1'dir.

Bu kriter, ağırlıklar w'nin bir fonksiyonu olarak kabul edilir ve bunu minimize etmemiz gerekiyor. Genellikle, başlangıçta bazı ağırlıklar w<sup>(0)</sup> ile başladığımız ve her adımda ağırlıkları aşağıdaki formüle göre güncellediğimiz bir yöntem olan **gradyan inişi** kullanılır:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Burada η, sözde **öğrenme oranı**dır ve ∇E(w) E'nin **gradyanı**nı ifade eder. Gradyanı hesapladıktan sonra şunları elde ederiz:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python'daki algoritma şu şekilde görünmektedir:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Sonuç

Bu derste, ikili sınıflandırma modeli olan bir perceptron hakkında bilgi edindiniz ve bunu bir ağırlık vektörü kullanarak nasıl eğiteceğinizi öğrendiniz.

## 🚀 Zorluk

Kendi perceptron'unuzu oluşturmayı denemek isterseniz, [Microsoft Learn'deki bu laboratuvara](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) göz atabilirsiniz. Bu laboratuvar, [Azure ML tasarımcısını](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) kullanmaktadır.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Gözden Geçirme & Kendi Kendine Çalışma

Perceptron'un nasıl bir oyuncak problemi çözdüğünü ve gerçek yaşam problemlerini nasıl çözebileceğimizi görmek ve öğrenmeye devam etmek için [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) defterine gidin.

Ayrıca, perceptronlar hakkında ilginç bir [makale](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) da var.

## [Ödev](lab/README.md)

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve iki el yazısı rakamı arasında sınıflandırma yapmak için kullandık. Bu laboratuvar, bir görüntüye en uygun rakamın hangisi olduğunu belirleyerek rakam sınıflandırma problemini tamamen çözmenizi istiyor.

* [Talimatlar](lab/README.md)
* [Defter](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.