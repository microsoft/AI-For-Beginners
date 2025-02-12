# Doğal Dil İşleme

![NLP görevlerinin özetini gösteren bir doodle](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.tr.png)

Bu bölümde, **Doğal Dil İşleme (NLP)** ile ilgili görevleri ele almak için Sinir Ağlarını kullanmaya odaklanacağız. Bilgisayarların çözmesini istediğimiz birçok NLP sorunu bulunmaktadır:

* **Metin sınıflandırması**, metin dizileri ile ilgili tipik bir sınıflandırma problemidir. Örnekler arasında e-posta mesajlarını spam ve spam olmayan olarak sınıflandırmak veya makaleleri spor, iş, siyaset vb. kategorilere ayırmak yer alır. Ayrıca, sohbet botları geliştirirken, genellikle bir kullanıcının ne demek istediğini anlamamız gerekir; bu durumda **niyet sınıflandırması** ile ilgileniyoruz. Niyet sınıflandırmasında genellikle birçok kategori ile başa çıkmamız gerekir.
* **Duygu analizi**, bir cümlenin anlamının ne kadar olumlu/olumsuz olduğunu karşılık gelen bir sayıya (bir duyguya) atfetmemiz gereken tipik bir regresyon problemidir. Duygu analizinin daha gelişmiş bir versiyonu, cümlenin tamamına değil, farklı kısımlarına (aspektlere) duygu atfettiğimiz **aspekt bazlı duygu analizi** (ABSA) olarak bilinir; örneğin, *Bu restoranda mutfağı beğendim, ama atmosfer berbat*.
* **Adlandırılmış Varlık Tanıma** (NER), metinden belirli varlıkları çıkarma problemine atıfta bulunur. Örneğin, *Yarın Paris'e uçmam gerekiyor* ifadesinde *yarın* kelimesinin TARİH'e, *Paris* kelimesinin ise LOKASYON'a karşılık geldiğini anlamamız gerekebilir.
* **Anahtar kelime çıkarımı**, NER'ye benzer, ancak cümlenin anlamı için önemli kelimeleri otomatik olarak, belirli varlık türleri için ön eğitim yapmadan çıkarmamız gerekir.
* **Metin kümeleme**, benzer cümleleri bir araya gruplamak istediğimizde yararlı olabilir; örneğin, teknik destek konuşmalarındaki benzer talepler.
* **Soru yanıtlama**, bir modelin belirli bir soruyu yanıtlayabilme yeteneğine atıfta bulunur. Model, bir metin parçası ve bir soru alır ve sorunun yanıtının bulunduğu metindeki yeri sağlaması gerekir (veya bazen yanıt metnini oluşturması).
* **Metin Üretimi**, bir modelin yeni metin oluşturabilme yeteneğidir. Bu, bazı *metin istemleri* temelinde bir sonraki harf/kelimeyi tahmin eden bir sınıflandırma görevi olarak düşünülebilir. GPT-3 gibi gelişmiş metin üretim modelleri, [istek programlama](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) veya [istek mühendisliği](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29) gibi bir teknik kullanarak sınıflandırma gibi diğer NLP görevlerini çözebilir.
* **Metin özetleme**, bir bilgisayarın uzun metni "okumasını" ve birkaç cümlede özetlemesini istediğimiz bir tekniktir.
* **Makine çevirisi**, bir dilde metin anlayışının ve diğer bir dilde metin üretiminin bir kombinasyonu olarak görülebilir.

Başlangıçta, çoğu NLP görevi geleneksel yöntemlerle, örneğin dilbilgileri kullanılarak çözülüyordu. Örneğin, makine çevirisinde, başlangıç cümlesini bir sözdizim ağaçına dönüştürmek için ayrıştırıcılar kullanılıyordu, ardından cümlenin anlamını temsil etmek için daha yüksek düzeyde anlamsal yapılar çıkarılıyordu ve bu anlam ile hedef dilin dilbilgisine dayanarak sonuç üretiliyordu. Günümüzde birçok NLP görevi, sinir ağları kullanılarak daha etkili bir şekilde çözülmektedir.

> Birçok klasik NLP yöntemi, [Doğal Dil İşleme Araç Takımı (NLTK)](https://www.nltk.org) Python kütüphanesinde uygulanmıştır. Farklı NLP görevlerinin NLTK kullanılarak nasıl çözülebileceğini kapsayan harika bir [NLTK Kitabı](https://www.nltk.org/book/) çevrimiçi olarak mevcuttur.

Kursumuzda, genellikle NLP için Sinir Ağlarını kullanmaya odaklanacağız ve gerektiğinde NLTK kullanacağız.

Daha önce, sinir ağlarını tablo verileri ve görüntülerle başa çıkmak için kullanmayı öğrendik. Bu veri türleri ile metin arasındaki ana fark, metnin değişken uzunlukta bir dizi olmasıdır; oysa görüntüler durumunda girdi boyutu önceden bilinir. Konvolüsyonel ağlar girdi verilerinden kalıpları çıkarabilirken, metindeki kalıplar daha karmaşıktır. Örneğin, birçok kelime için öznenin olumsuzluğunun ayrılmasının rastgele olması mümkündür (örneğin, *Portakalları sevmiyorum*, vs. *O büyük renkli lezzetli portakalları sevmiyorum*), ve bu hala bir kalıp olarak yorumlanmalıdır. Bu nedenle, dili ele almak için *tekrarlayan ağlar* ve *dönüştürücüler* gibi yeni sinir ağı türlerini tanıtmamız gerekir.

## Kütüphaneleri Yükle

Bu kursu çalıştırmak için yerel Python yüklemesi kullanıyorsanız, NLP için gerekli tüm kütüphaneleri aşağıdaki komutları kullanarak yüklemeniz gerekebilir:

**PyTorch için**
```bash
pip install -r requirements-torch.txt
```
**TensorFlow için**
```bash
pip install -r requirements-tf.txt
```

> TensorFlow ile NLP'yi [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste) üzerinde deneyebilirsiniz.

## GPU Uyarısı

Bu bölümde, bazı örneklerde oldukça büyük modelleri eğiteceğiz.
* **GPU Destekli Bilgisayar Kullanın**: Büyük modellerle çalışırken bekleme sürelerini azaltmak için not defterlerinizi GPU destekli bir bilgisayarda çalıştırmanız önerilir.
* **GPU Bellek Kısıtlamaları**: Bir GPU'da çalışmak, özellikle büyük modelleri eğitirken GPU belleğinin tükenmesi durumlarına yol açabilir.
* **GPU Bellek Tüketimi**: Eğitim sırasında tüketilen GPU belleği miktarı, minibatch boyutu gibi çeşitli faktörlere bağlıdır.
* **Minibatch Boyutunu Küçültün**: GPU bellek sorunlarıyla karşılaşırsanız, kodunuzda minibatch boyutunu azaltmayı düşünebilirsiniz.
* **TensorFlow GPU Bellek Salımı**: Eski TensorFlow sürümleri, bir Python çekirdeği içinde birden fazla modeli eğitirken GPU belleğini doğru bir şekilde serbest bırakmayabilir. GPU bellek kullanımını etkili bir şekilde yönetmek için TensorFlow'u yalnızca gerektiğinde GPU belleği ayıracak şekilde yapılandırabilirsiniz.
* **Kod Dahil Etme**: TensorFlow'un GPU bellek tahsisini yalnızca gerektiğinde artırması için not defterlerinize aşağıdaki kodu ekleyin:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Klasik ML perspektifinden NLP hakkında daha fazla bilgi edinmek isterseniz, [bu dersler dizisine](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP) göz atın.

## Bu Bölümde
Bu bölümde şunları öğreneceğiz:

* [Metni tensörler olarak temsil etme](13-TextRep/README.md)
* [Kelime Gömme](14-Emdeddings/README.md)
* [Dil Modelleme](15-LanguageModeling/README.md)
* [Tekrarlayan Sinir Ağları](16-RNN/README.md)
* [Üretken Ağlar](17-GenerativeNetworks/README.md)
* [Dönüştürücüler](18-Transformers/README.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Yerel dilindeki orijinal belge, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.