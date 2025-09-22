<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-26T07:35:41+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş: Perceptron

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Modern sinir ağına benzer bir şeyin ilk uygulama girişimlerinden biri, 1957 yılında Cornell Havacılık Laboratuvarı'ndan Frank Rosenblatt tarafından gerçekleştirildi. Bu, "Mark-1" olarak adlandırılan ve üçgenler, kareler ve daireler gibi basit geometrik şekilleri tanımak için tasarlanmış bir donanım uygulamasıydı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Mark 1 Perceptron' />|

> Görseller [Wikipedia'dan](https://en.wikipedia.org/wiki/Perceptron)

Giriş görüntüsü, 20x20 fotohücre dizisi ile temsil ediliyordu, bu nedenle sinir ağının 400 girişi ve bir ikili çıkışı vardı. Basit bir ağ, **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayar gerektiren potansiyometreler gibi davranıyordu.

> ✅ Potansiyometre, kullanıcıya bir devrenin direncini ayarlama imkanı veren bir cihazdır.

> New York Times o dönemde perceptron hakkında şunları yazmıştı: *[Donanma'nın] yürüyebilen, konuşabilen, görebilen, yazabilen, kendini çoğaltabilen ve varlığının farkında olabilen bir elektronik bilgisayar embriyosu.*

## Perceptron Modeli

Modelimizde N özellik olduğunu varsayalım, bu durumda giriş vektörü N boyutunda bir vektör olacaktır. Bir perceptron, **ikili sınıflandırma** modelidir, yani iki sınıf giriş verisini ayırt edebilir. Her giriş vektörü x için perceptronumuzun çıktısının sınıfa bağlı olarak ya +1 ya da -1 olacağını varsayacağız. Çıktı şu formülle hesaplanacaktır:

y(x) = f(w<sup>T</sup>x)

burada f bir basamak aktivasyon fonksiyonudur.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Perceptron Eğitimi

Bir perceptronu eğitmek için, çoğu değeri doğru bir şekilde sınıflandıran, yani en küçük **hata** ile sonuçlanan bir ağırlık vektörü w bulmamız gerekir. Bu hata E, **perceptron kriteri** ile şu şekilde tanımlanır:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırma ile sonuçlanan eğitim veri noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisidir ve t<sub>i</sub> negatif ve pozitif örnekler için sırasıyla -1 veya +1'dir.

Bu kriter, ağırlıklar w'nin bir fonksiyonu olarak kabul edilir ve bunu minimize etmemiz gerekir. Genellikle, **gradyan inişi** adı verilen bir yöntem kullanılır; bu yöntemde başlangıçta bazı ağırlıklar w<sup>(0)</sup> ile başlar ve her adımda ağırlıkları şu formüle göre güncelleriz:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Burada η, **öğrenme oranı** olarak adlandırılır ve ∇E(w), E'nin **gradyanı** anlamına gelir. Gradyanı hesapladıktan sonra şu formüle ulaşırız:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python'daki algoritma şu şekilde görünür:

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

Bu derste, ikili sınıflandırma modeli olan perceptronu ve ağırlık vektörü kullanarak nasıl eğitileceğini öğrendiniz.

## 🚀 Meydan Okuma

Kendi perceptronunuzu oluşturmayı denemek isterseniz, [Microsoft Learn'deki bu laboratuvarı](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) deneyebilirsiniz. Bu laboratuvar, [Azure ML tasarımcısını](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) kullanır.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Gözden Geçirme ve Kendi Kendine Çalışma

Perceptronun bir oyuncak problemi ve gerçek hayattaki problemleri nasıl çözebileceğini görmek ve öğrenmeye devam etmek için [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) not defterine gidin.

İşte perceptronlar hakkında ilginç bir [makale](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Ödev](lab/README.md)

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve bunu iki el yazısı rakam arasında sınıflandırma yapmak için kullandık. Bu laboratuvarda, rakam sınıflandırma problemini tamamen çözmeniz isteniyor, yani verilen bir görüntünün en olası hangi rakama karşılık geldiğini belirlemeniz gerekiyor.

* [Talimatlar](lab/README.md)
* [Not Defteri](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.