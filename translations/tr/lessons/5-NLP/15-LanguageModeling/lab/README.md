# Skip-Gram Modelini Eğitme

[AI for Beginners Müfredatı](https://github.com/microsoft/ai-for-beginners) tarafından hazırlanan laboratuvar ödevi.

## Görev

Bu laboratuvarda, sizden Skip-Gram tekniğini kullanarak Word2Vec modelini eğitmeniz isteniyor. $N$-token genişliğindeki Skip-Gram penceresinde komşu kelimeleri tahmin etmek için gömme (embedding) içeren bir ağ eğitin. [Bu dersteki kodu](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) kullanabilir ve biraz değiştirebilirsiniz.

## Veri Seti

Herhangi bir kitabı kullanabilirsiniz. [Project Gutenberg](https://www.gutenberg.org/) sitesinde birçok ücretsiz metin bulabilirsiniz. Örneğin, Lewis Carroll tarafından yazılan [Alice Harikalar Diyarında](https://www.gutenberg.org/files/11/11-0.txt) kitabına doğrudan buradan ulaşabilirsiniz. Alternatif olarak, Shakespeare'in oyunlarını kullanabilirsiniz. Aşağıdaki kodu kullanarak bu oyunlara erişebilirsiniz:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Keşfet!

Eğer zamanınız varsa ve konuyu daha derinlemesine incelemek istiyorsanız, birkaç şeyi keşfetmeyi deneyin:

* Gömme boyutunun sonuçları nasıl etkilediğini inceleyin.
* Farklı metin stillerinin sonucu nasıl etkilediğini araştırın.
* Çok farklı türdeki kelimeler ve onların eş anlamlılarını seçin, bu kelimelerin vektör temsillerini elde edin, boyutları 2'ye düşürmek için PCA uygulayın ve bunları 2D uzayda çizin. Herhangi bir desen görüyor musunuz?

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.