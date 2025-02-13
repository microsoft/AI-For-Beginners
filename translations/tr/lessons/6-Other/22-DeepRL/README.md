# Derin Pekiştirmeli Öğrenme

Pekiştirmeli öğrenme (RL), denetimli öğrenme ve denetimsiz öğrenme ile birlikte temel makine öğrenimi paradigmalardan biri olarak görülmektedir. Denetimli öğrenmede bilinen sonuçlara sahip bir veri setine dayanırken, RL **yaparak öğrenme** temellidir. Örneğin, bir bilgisayar oyunu ile ilk kez karşılaştığımızda, kuralları bilmeden oynamaya başlarız ve kısa süre içinde oynama ve davranışımızı ayarlama süreci sayesinde becerilerimizi geliştirmeye başlarız.

## [Ön ders anketi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

RL gerçekleştirmek için şunlara ihtiyacımız var:

* Oyun kurallarını belirleyen bir **çevre** veya **simülatör**. Simülatörde deneyleri gerçekleştirebilmeli ve sonuçları gözlemleyebilmeliyiz.
* Deneyimizin ne kadar başarılı olduğunu gösteren bir **ödül fonksiyonu**. Bir bilgisayar oyunu oynamayı öğrenme durumunda, ödül nihai puanımız olur.

Ödül fonksiyonuna dayanarak, davranışımızı ayarlayıp becerilerimizi geliştirmeliyiz, böylece bir sonraki oyunumuzda daha iyi oynayabiliriz. Diğer makine öğrenimi türleri ile RL arasındaki ana fark, RL'de oyunu bitirene kadar kazandığımızı veya kaybettiğimizi bilmememizdir. Bu nedenle, belirli bir hamlenin iyi mi kötü mü olduğunu söyleyemeyiz - yalnızca oyunun sonunda bir ödül alırız.

RL sırasında genellikle birçok deney gerçekleştiririz. Her deneyde, şimdiye kadar öğrendiğimiz optimal stratejiyi takip etme (**sömürü**) ve yeni olası durumları keşfetme (**keşif**) arasında denge kurmamız gerekir.

## OpenAI Gym

RL için harika bir araç olan [OpenAI Gym](https://gym.openai.com/) - farklı çevreleri simüle edebilen bir **simülasyon ortamı**. Atari oyunlarından, denge çubuğunun arkasındaki fiziğe kadar birçok farklı çevreyi simüle edebilir. Pekiştirmeli öğrenme algoritmalarını eğitmek için en popüler simülasyon ortamlarından biridir ve [OpenAI](https://openai.com/) tarafından bakım yapılmaktadır.

> **Not**: OpenAI Gym'de mevcut olan tüm çevreleri [buradan](https://gym.openai.com/envs/#classic_control) görebilirsiniz.

## CartPole Dengeleme

Muhtemelen *Segway* veya *Gyroscooter* gibi modern dengeleme cihazlarını görmüşsünüzdür. Bu cihazlar, bir ivmeölçer veya jiroskoptan gelen bir sinyale yanıt olarak tekerleklerini ayarlayarak otomatik olarak denge sağlarlar. Bu bölümde, benzer bir problemi - bir direği dengelemeyi - öğreneceğiz. Bu, bir sirk sanatçısının elinde bir direği dengelemesi durumuna benzer - ancak bu direk dengesi yalnızca 1D'de gerçekleşir.

Dengelemenin basitleştirilmiş bir versiyonu **CartPole** problemi olarak bilinir. CartPole dünyasında, sola veya sağa hareket edebilen yatay bir kaydırıcıya sahibiz ve amaç, kaydırıcının üstünde dik bir direği dengede tutmaktır.

<img alt="bir cartpole" src="images/cartpole.png" width="200"/>

Bu çevreyi oluşturmak ve kullanmak için birkaç satır Python koduna ihtiyacımız var:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Her çevre tam olarak aynı şekilde erişilebilir:
* `env.reset` starts a new experiment
* `env.step` bir simülasyon adımı gerçekleştirir. **Eylem** alanından bir **eylem** alır ve bir **gözlem** (gözlem alanından), ayrıca bir ödül ve bir sonlandırma bayrağı döndürür.

Yukarıdaki örnekte, her adımda rastgele bir eylem gerçekleştiriyoruz, bu nedenle deneyin ömrü çok kısadır:

![dengelemeyen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Bir RL algoritmasının amacı, belirli bir duruma yanıt olarak eylemi döndüren bir modeli - sözde **politika** π - eğitmektir. Politikanın olasılıksal olarak da düşünülebileceğini, örneğin, herhangi bir durum *s* ve eylem *a* için *s* durumunda *a* eylemini alma olasılığını π(*a*|*s*) döndürmesi gerektiğini de belirtebiliriz.

## Politika Gradyanları Algoritması

Bir politikayı modellemenin en belirgin yolu, durumları girdi olarak alacak ve karşılık gelen eylemleri (veya daha doğrusu tüm eylemlerin olasılıklarını) döndürecek bir sinir ağı oluşturmaktır. Bir bakıma, bu, her adımda hangi eylemleri almamız gerektiğini önceden bilmediğimiz için normal bir sınıflandırma görevine benzer.

Buradaki fikir, bu olasılıkları tahmin etmektir. Deneyin her adımındaki toplam ödülümüzü gösteren bir **kümülatif ödül** vektörü oluşturuyoruz. Ayrıca, daha önceki ödüllerin rolünü azaltmak için daha önceki ödülleri bir katsayı γ=0.99 ile çarparak **ödül indirimleme** uyguluyoruz. Ardından, daha büyük ödüller getiren deney yolu boyunca bu adımları pekiştiriyoruz.

> Politika Gradyanı algoritması hakkında daha fazla bilgi edinin ve [örnek defterde](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb) bunu eylemde görün.

## Aktör-Kritik Algoritması

Politika Gradyanları yaklaşımının geliştirilmiş bir versiyonu **Aktör-Kritik** olarak adlandırılır. Bunun arkasındaki ana fikir, sinir ağının iki şeyi döndürmek üzere eğitilmesidir:

* Hangi eylemin alınacağını belirleyen politika. Bu kısım **aktör** olarak adlandırılır.
* Bu durumda bekleyebileceğimiz toplam ödülün tahmini - bu kısım ise **kritik** olarak adlandırılır.

Bir bakıma, bu mimari, birbirlerine karşı eğitilen iki ağa sahip bir [GAN](../../4-ComputerVision/10-GANs/README.md) ile benzerlik gösterir. Aktör-kritik modelinde, aktör almamız gereken eylemi önerir ve kritik, sonucu tahmin etmeye çalışır. Ancak, amacımız bu ağları birlikte eğitmektir.

Deney sırasında hem gerçek kümülatif ödülleri hem de kritik tarafından döndürülen sonuçları bildiğimiz için, bunlar arasındaki farkı minimize edecek bir kayıp fonksiyonu oluşturmak oldukça kolaydır. Bu, bize **kritik kaybı** verir. **Aktör kaybını** ise politika gradyanı algoritmasındaki aynı yaklaşımı kullanarak hesaplayabiliriz.

Bu algoritmalardan birini çalıştırdıktan sonra, CartPole'umuzun şöyle davranmasını bekleyebiliriz:

![bir dengeleyen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Alıştırmalar: Politika Gradyanları ve Aktör-Kritik RL

Aşağıdaki defterlerde öğreniminize devam edin:

* [TensorFlow'da RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [PyTorch'ta RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Diğer RL Görevleri

Günümüzde Pekiştirmeli Öğrenme, hızla büyüyen bir araştırma alanıdır. Pekiştirmeli öğrenmenin bazı ilginç örnekleri şunlardır:

* Bir bilgisayarı **Atari Oyunları** oynamayı öğretmek. Bu problemin zorluğu, durumun bir vektör olarak basit bir şekilde temsil edilmemesi, daha ziyade bir ekran görüntüsü olmasıdır - ve bu ekran görüntüsünü bir özellik vektörüne dönüştürmek veya ödül bilgisini çıkarmak için CNN kullanmamız gerekir. Atari oyunları Gym'de mevcuttur.
* Bir bilgisayarı satranç ve go gibi masa oyunları oynamayı öğretmek. Son zamanlarda **Alpha Zero** gibi son teknoloji programlar, iki ajanın birbirine karşı oynayarak ve her adımda gelişerek sıfırdan eğitilmiştir.
* Endüstride, RL simülasyondan kontrol sistemleri oluşturmak için kullanılır. [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) adlı bir hizmet bunun için özel olarak tasarlanmıştır.

## Sonuç

Artık, ajansları iyi sonuçlar elde etmek için sadece onlara oyunun istenen durumunu tanımlayan bir ödül fonksiyonu sağlayarak ve arama alanını akıllıca keşfetme fırsatı vererek nasıl eğiteceğimizi öğrendik. İki algoritmayı başarıyla denedik ve oldukça kısa bir süre içinde iyi bir sonuç elde ettik. Ancak, bu, RL yolculuğunuzun sadece başlangıcıdır ve daha derinlemesine incelemek isterseniz ayrı bir kurs almayı kesinlikle düşünmelisiniz.

## 🚀 Zorluk

'Diğer RL Görevleri' bölümünde listelenen uygulamaları keşfedin ve birini uygulamaya çalışın!

## [Ders sonrası anket](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Gözden Geçirme ve Kendi Kendine Çalışma

Klasik pekiştirmeli öğrenme hakkında daha fazla bilgi edinin [Makine Öğrenimi için Başlangıç Müfredatı](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) üzerinden.

Bir bilgisayarın Süper Mario oynamayı nasıl öğrenebileceğini anlatan [bu harika videoyu](https://www.youtube.com/watch?v=qv6UVOQ0F44) izleyin.

## Ödev: [Bir Dağ Aracını Eğit](lab/README.md)

Bu ödev sırasında amacınız farklı bir Gym çevresini - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) - eğitmek olacaktır.

**Sorumluluk Reddi**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak değerlendirilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.