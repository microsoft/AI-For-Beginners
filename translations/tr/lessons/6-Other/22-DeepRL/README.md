<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-26T07:32:49+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "tr"
}
-->
# Derin Pekiştirmeli Öğrenme

Pekiştirmeli öğrenme (RL), denetimli öğrenme ve denetimsiz öğrenme ile birlikte temel makine öğrenimi paradigmalarından biri olarak görülür. Denetimli öğrenmede bilinen sonuçlara sahip bir veri setine dayanırken, RL **yaparak öğrenme** ilkesine dayanır. Örneğin, bir bilgisayar oyununu ilk kez gördüğümüzde, kuralları bilmeden oynamaya başlarız ve sadece oynama ve davranışlarımızı ayarlama süreciyle becerilerimizi geliştirebiliriz.

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

RL gerçekleştirmek için ihtiyacımız olanlar:

* Oyunun kurallarını belirleyen bir **ortam** veya **simülatör**. Deneyleri simülatörde çalıştırabilmeli ve sonuçları gözlemleyebilmeliyiz.
* Deneyimizin ne kadar başarılı olduğunu gösteren bir **ödül fonksiyonu**. Örneğin, bir bilgisayar oyununu öğrenirken ödül, nihai puanımız olabilir.

Ödül fonksiyonuna dayanarak davranışlarımızı ayarlayabilir ve becerilerimizi geliştirebiliriz, böylece bir sonraki sefer daha iyi oynarız. Diğer makine öğrenimi türleri ile RL arasındaki temel fark, RL'de genellikle oyunu bitirene kadar kazanıp kazanmadığımızı bilmememizdir. Bu nedenle, belirli bir hamlenin tek başına iyi olup olmadığını söyleyemeyiz - ödülü yalnızca oyunun sonunda alırız.

RL sırasında genellikle birçok deney gerçekleştiririz. Her deney sırasında, şimdiye kadar öğrendiğimiz en iyi stratejiyi takip etmek (**sömürü**) ile yeni olası durumları keşfetmek (**keşif**) arasında bir denge kurmamız gerekir.

## OpenAI Gym

RL için harika bir araç [OpenAI Gym](https://gym.openai.com/) - birçok farklı ortamı simüle edebilen bir **simülasyon ortamı**. Atari oyunlarından, direk dengeleme fiziğine kadar çeşitli ortamları simüle edebilir. Pekiştirmeli öğrenme algoritmalarını eğitmek için en popüler simülasyon ortamlarından biridir ve [OpenAI](https://openai.com/) tarafından geliştirilmiştir.

> **Note**: OpenAI Gym'deki tüm mevcut ortamları [buradan](https://gym.openai.com/envs/#classic_control) görebilirsiniz.

## CartPole Dengeleme

Muhtemelen hepiniz modern dengeleme cihazlarını, örneğin *Segway* veya *Gyroscooter* görmüşsünüzdür. Bu cihazlar, bir ivmeölçer veya jiroskoptan gelen sinyale yanıt olarak tekerleklerini ayarlayarak otomatik olarak dengede durabilir. Bu bölümde, benzer bir problemi - bir direği dengelemeyi - nasıl çözeceğimizi öğreneceğiz. Bu, bir sirk sanatçısının elinde bir direği dengelemesi gibi bir duruma benzer - ancak bu dengeleme yalnızca 1D'de gerçekleşir.

Dengelemenin basitleştirilmiş bir versiyonu **CartPole** problemi olarak bilinir. CartPole dünyasında, sola veya sağa hareket edebilen yatay bir kaydırıcı vardır ve hedef, kaydırıcının hareketi sırasında dikey bir direği dengede tutmaktır.

<img alt="bir cartpole" src="images/cartpole.png" width="200"/>

Bu ortamı oluşturmak ve kullanmak için birkaç satır Python koduna ihtiyacımız var:

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

Her ortam aynı şekilde erişilebilir:
* `env.reset` yeni bir deneyi başlatır
* `env.step` bir simülasyon adımı gerçekleştirir. **Eylem alanından** bir **eylem** alır ve bir **gözlem** (gözlem alanından), ödül ve bir bitiş bayrağı döndürür.

Yukarıdaki örnekte her adımda rastgele bir eylem gerçekleştiriyoruz, bu yüzden deneyin ömrü çok kısa:

![dengelemeyen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Bir RL algoritmasının amacı, bir model - **politika** π - eğitmek ve bu modelin verilen bir duruma yanıt olarak eylemi döndürmesini sağlamaktır. Politikayı olasılıksal olarak da düşünebiliriz, örneğin herhangi bir durum *s* ve eylem *a* için π(*a*|*s*) olasılığını döndürür, yani *s* durumunda *a* eylemini gerçekleştirmemiz gerektiğini belirtir.

## Politika Gradyanları Algoritması

Bir politikayı modellemenin en açık yolu, durumları giriş olarak alacak ve karşılık gelen eylemleri (veya daha doğrusu tüm eylemlerin olasılıklarını) döndürecek bir sinir ağı oluşturmaktır. Bir anlamda, bu normal bir sınıflandırma görevine benzer olurdu, ancak büyük bir farkla - her adımda hangi eylemleri gerçekleştirmemiz gerektiğini önceden bilmiyoruz.

Buradaki fikir, bu olasılıkları tahmin etmektir. Deneyin her adımında toplam ödülümüzü gösteren bir **kümülatif ödüller** vektörü oluştururuz. Ayrıca, önceki ödüllerin rolünü azaltmak için önceki ödülleri γ=0.99 gibi bir katsayı ile çarparak **ödül indirgeme** uygularız. Daha sonra, daha büyük ödüller sağlayan deney yolundaki adımları güçlendiririz.

> Politika Gradyanları algoritması hakkında daha fazla bilgi edinin ve [örnek not defterinde](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb) uygulamasını görün.

## Aktör-Kritik Algoritması

Politika Gradyanları yaklaşımının geliştirilmiş bir versiyonu **Aktör-Kritik** olarak adlandırılır. Bunun arkasındaki temel fikir, sinir ağının iki şeyi döndürecek şekilde eğitilmesidir:

* Hangi eylemi gerçekleştireceğimizi belirleyen politika. Bu kısma **aktör** denir.
* Bu durumdaki toplam ödül beklentimizi tahmin eden kısım - bu kısma **kritik** denir.

Bir anlamda, bu yapı [GAN](../../4-ComputerVision/10-GANs/README.md)'a benzer, burada iki ağ birbirine karşı eğitilir. Aktör-kritik modelde, aktör gerçekleştirmemiz gereken eylemi önerir ve kritik, sonucu tahmin etmeye çalışır. Ancak, amacımız bu ağları uyum içinde eğitmektir.

Deney sırasında hem gerçek kümülatif ödülleri hem de kritiğin döndürdüğü sonuçları bildiğimiz için, aralarındaki farkı en aza indirecek bir kayıp fonksiyonu oluşturmak nispeten kolaydır. Bu bize **kritik kaybı** verir. **Aktör kaybını** ise politika gradyanları algoritmasında olduğu gibi hesaplayabiliriz.

Bu algoritmalardan birini çalıştırdıktan sonra, CartPole'umuzun şu şekilde davranmasını bekleyebiliriz:

![dengeleyen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Alıştırmalar: Politika Gradyanları ve Aktör-Kritik RL

Aşağıdaki not defterlerinde öğrenmeye devam edin:

* [TensorFlow ile RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [PyTorch ile RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Diğer RL Görevleri

Pekiştirmeli öğrenme günümüzde hızla büyüyen bir araştırma alanıdır. Pekiştirmeli öğrenmenin bazı ilginç örnekleri şunlardır:

* Bilgisayara **Atari Oyunları** oynatmayı öğretmek. Bu problemin zorlu kısmı, basit bir durumun bir vektör olarak temsil edilmemesi, bunun yerine bir ekran görüntüsü olmasıdır - ve bu ekran görüntüsünü bir özellik vektörüne dönüştürmek veya ödül bilgisi çıkarmak için CNN kullanmamız gerekir. Atari oyunları Gym'de mevcuttur.
* Bilgisayara satranç ve Go gibi masa oyunları oynamayı öğretmek. Son zamanlarda **Alpha Zero** gibi en son teknoloji programlar, iki ajanın birbirine karşı oynayıp her adımda gelişmesiyle sıfırdan eğitildi.
* Endüstride, RL simülasyondan kontrol sistemleri oluşturmak için kullanılır. [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) adlı bir hizmet özellikle bunun için tasarlanmıştır.

## Sonuç

Artık bir ödül fonksiyonu sağlayarak ve arama alanını akıllıca keşfetme fırsatı vererek, ajanları iyi sonuçlar elde etmek için nasıl eğiteceğimizi öğrendik. İki algoritmayı başarıyla denedik ve nispeten kısa bir sürede iyi bir sonuç elde ettik. Ancak, bu RL yolculuğunuzun sadece başlangıcıdır ve daha derinlemesine öğrenmek istiyorsanız ayrı bir kurs almayı kesinlikle düşünmelisiniz.

## 🚀 Meydan Okuma

'Diğer RL Görevleri' bölümünde listelenen uygulamaları keşfedin ve birini uygulamayı deneyin!

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## İnceleme ve Kendi Kendine Çalışma

[Başlangıç Seviyesi için Makine Öğrenimi Müfredatımızda](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) klasik pekiştirmeli öğrenme hakkında daha fazla bilgi edinin.

Bilgisayarın Super Mario oynamayı nasıl öğrenebileceğini anlatan [bu harika videoyu](https://www.youtube.com/watch?v=qv6UVOQ0F44) izleyin.

## Ödev: [Bir Dağ Arabasını Eğitin](lab/README.md)

Bu ödev sırasında hedefiniz farklı bir Gym ortamını - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) - eğitmek olacaktır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.