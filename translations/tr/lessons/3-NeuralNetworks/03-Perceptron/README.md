# Sinir Ağlarına Giriş: Perceptron

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Modern sinir ağına benzer bir şeyin ilk uygulama girişimlerinden biri, 1957 yılında Cornell Havacılık Laboratuvarı'ndan Frank Rosenblatt tarafından gerçekleştirildi. Bu, "Mark-1" adı verilen ve üçgen, kare ve daire gibi basit geometrik şekilleri tanımak için tasarlanmış bir donanım uygulamasıydı.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/tr/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/tr/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='Mark 1 Perceptron' />|

> Görseller [Wikipedia'dan](https://en.wikipedia.org/wiki/Perceptron)

Giriş görüntüsü, 20x20 fotohücre dizisiyle temsil ediliyordu, bu nedenle sinir ağının 400 girişi ve bir ikili çıkışı vardı. Basit bir ağ, **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayar gerektiren potansiyometreler gibi çalışıyordu.

> ✅ Potansiyometre, kullanıcıya bir devrenin direncini ayarlama imkanı veren bir cihazdır.

> New York Times o dönemde perceptron hakkında şöyle yazmıştı: *[Donanma'nın] yürüyebilen, konuşabilen, görebilen, yazabilen, kendini çoğaltabilen ve varlığının farkında olabilen bir elektronik bilgisayar embriyosu.*

## Perceptron Modeli

Modelimizde N özellik olduğunu varsayalım, bu durumda giriş vektörü N boyutunda bir vektör olacaktır. Bir perceptron, **ikili sınıflandırma** modeli olup, giriş verilerini iki sınıf arasında ayırt edebilir. Her bir giriş vektörü x için perceptron çıkışının sınıfa bağlı olarak ya +1 ya da -1 olacağını varsayacağız. Çıkış şu formülle hesaplanır:

y(x) = f(w<sup>T</sup>x)

burada f bir adım aktivasyon fonksiyonudur.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/tr/activation-func.b4924007c7ce7764.webp"/>

## Perceptron Eğitimi

Bir perceptron eğitmek için, çoğu değeri doğru bir şekilde sınıflandıran, yani en küçük **hata**yı veren bir ağırlık vektörü w bulmamız gerekir. Bu hata E, **perceptron kriteri** ile şu şekilde tanımlanır:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırmaya neden olan eğitim veri noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisi, t<sub>i</sub> ise negatif ve pozitif örnekler için sırasıyla -1 veya +1'dir.

Bu kriter, ağırlıklar w'nin bir fonksiyonu olarak kabul edilir ve bunu minimize etmemiz gerekir. Genellikle, **gradyan inişi** adı verilen bir yöntem kullanılır. Bu yöntemde, başlangıçta bir ağırlık w<sup>(0)</sup> seçilir ve her adımda ağırlıklar şu formüle göre güncellenir:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Burada &eta; **öğrenme oranı** olarak adlandırılır ve &nabla;E(w) ise E'nin **gradyanı**dır. Gradyanı hesapladıktan sonra şu sonuca ulaşırız:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python'daki algoritma şu şekildedir:

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

Bu derste, ikili sınıflandırma modeli olan perceptron hakkında bilgi edindiniz ve ağırlık vektörü kullanarak nasıl eğitileceğini öğrendiniz.

## 🚀 Meydan Okuma

Kendi perceptronunuzu oluşturmayı denemek isterseniz, [Microsoft Learn'deki bu laboratuvarı](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) deneyebilirsiniz. Bu laboratuvar, [Azure ML tasarımcısını](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) kullanır.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Gözden Geçirme ve Kendi Kendine Çalışma

Perceptronun bir oyuncak problemi ve gerçek hayat problemlerini nasıl çözebileceğini görmek ve öğrenmeye devam etmek için [Perceptron](Perceptron.ipynb) not defterine göz atabilirsiniz.

İlginç bir [perceptron makalesi](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) de mevcut.

## [Ödev](lab/README.md)

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve bunu iki el yazısı rakamı arasında sınıflandırma yapmak için kullandık. Bu laboratuvarda, rakam sınıflandırma problemini tamamen çözmeniz isteniyor, yani verilen bir görüntünün en olası rakamını belirlemeniz gerekiyor.

* [Talimatlar](lab/README.md)
* [Not Defteri](lab/PerceptronMultiClass.ipynb)

---

