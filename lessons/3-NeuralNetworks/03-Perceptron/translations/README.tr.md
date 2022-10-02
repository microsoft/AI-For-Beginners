# Sinir Ağlarına Giriş: Algılayıcı

## [Ders öncesi sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Modern bir sinir ağına benzer bir şeyi uygulamaya yönelik ilk girişimlerden biri, 1957'de Cornell Havacılık Laboratuvarı'ndan Frank Rosenblatt tarafından yapıldı. Üçgenler, kareler ve daireler gibi ilkel geometrik şekilleri tanımak için tasarlanmış "Mark-1" adlı bir donanım uygulamasıydı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='../images/Mark_I_perceptron_wikipedia.jpg' alt='Mark 1 Algılayıcısı' />|

> İmgeler [Wikipedia'dan](https://en.wikipedia.org/wiki/Perceptron)

Bir girdi imgesi 20x20'lik fotosel dizisi ile temsil edildi, bu nedenle sinir ağının 400 girdisi ve bir ikili çıktısı vardı. Basit bir ağ, **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında elle ayar gerektiren potansiyometreler gibi davrandı.

> ✅ Potansiyometre, kullanıcının bir devrenin direncini ayarlamasını sağlayan bir cihazdır.

> New York Times o dönemde algılayıcı hakkında şunları yazmıştı: *[Donanmanın] beklediği, yürüyebilecek, konuşabilecek, görebilecek, yazabilecek, kendini yeniden üretebilecek ve varlığının bilincinde olabilecek bir elektronik bilgisayarın embriyosu.*

## Algılayıcı Modeli

Modelimizde N tane özniteliğimiz olduğunu varsayalım, bu durumda girdi vektörü N boyutunda bir vektör olacaktır. Bir algılayıcı bir **ikili sınıflandırma** modelidir, yani iki girdi verisi sınıfını ayırt edebilir. Her x girdi vektörü için algılayıcımızın çıktısının sınıfa bağlı olarak +1 veya -1 olacağını varsayacağız. Çıktı, aşağıdaki formül kullanılarak hesaplanacaktır:

y(x) = f(w<sup>T</sup>x)

burada f basamak etkinleştirme fonksiyonudur.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../images/activation-func.png"/>

## Algılayıcıyı Eğitme

Bir algılayıcıyı eğitmek için değerlerin çoğunu doğru şekilde sınıflandıran, yani en küçük **hata** ile sonuçlanan bir w ağırlık vektörü bulmamız gerekir. Bu hata, **algılayıcı kriteri** tarafından aşağıdaki şekilde tanımlanır:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* yanlış sınıflandırmaya neden olan i eğitim veri noktalarının toplamı alınır.
* x<sub>i</sub> girdi verisidir ve buna göre olumsuz ve olumlu örnekler için t<sub>i</sub> -1 veya +1'dir.

Bu kriter w ağırlıklarının bir fonksiyonu olarak kabul edilir ve bunu en aza indirmemiz gerekir. Genellikle, bazı ilk ağırlıkları w<sup>(0)</sup> ile başladığımız ve ardından her adımda ağırlıkları aşağıdaki formüle göre güncellediğimiz **gradyan inişi** adlı bir yöntem kullanılır:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Burada &eta; sözde **öğrenme oranı** ve &nabla;E(w) E'nin **gradyanını** belirtir. Gradyanı hesapladıktan sonra, aşağıdaki işleme varırız:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python'daki algoritma şöyle görünür:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Ağırlıkları ilkle (neredeyse rastgele :))
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # algılayıcı çıktısını hesapla
        if z < 0: # pozitif örnek negatif sınıflandırıldı
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negatif örnek pozitif sınıflandırıldı
            weights = weights - eta*weights.shape

    return weights
```

## Vargılar

Bu derste, ikili sınıflandırma modeli olan algılayıcıyı ve ağırlık vektörü kullanarak onu nasıl eğiteceğinizi öğrendiniz.

## 🚀 Kendini Sınama

Kendi algılayıcınızı oluşturmaya çalışmak istiyorsanız, [Azure ML tasarımcısını (Azure ML designer)](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) kullanan [Microsoft Learn'deki bu laboratuvarı](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) deneyin.

## [Ders sonrası sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Gözden Geçirme ve Bireysel Çalışma

Bir oyuncak probleminin yanı sıra gerçek hayattaki problemleri çözmek için algılayıcıyı nasıl kullanabileceğimizi görmek ve öğrenmeye devam etmek için [Algılayıcı](./Perceptron.tr.ipynb) not defterine gidin.

İşte ilave olarak ilginç bir [algılayıcılar makalesi](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Ödev](../lab/translations/README.tr.md)

Bu dersimizde ikili sınıflandırma görevi için bir algılayıcı uyguladık ve bunu iki el yazısı rakamı arasından sınıflandırmak için kullandık. Bu laboratuvarda, rakam sınıflandırma problemini tamamen çözmeniz, yani hangi rakamın belirli bir imgeye karşılık gelme olasılığının en yüksek olduğunu belirlemeniz istenmektedir.

* [Talimatlar](../lab/translations/README.tr.md)
* [Not Defteri](../lab/translations/PerceptronMultiClass.tr.ipynb)
