# Eğitim Skip-Gram Modeli

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) dersinden laboratuvar ödevi.

## Görev

Bu laboratuvar çalışmasında, size Word2Vec modelini Skip-Gram tekniği kullanarak eğitme challenge'ı veriyoruz. $N$-token genişliğinde bir Skip-Gram penceresinde komşu kelimeleri tahmin etmek için gömme ile bir ağ eğitin. Bu dersten [bu kodu](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) kullanabilir ve biraz değiştirebilirsiniz.

## Veri Seti

Herhangi bir kitabı kullanabilirsiniz. [Project Gutenberg](https://www.gutenberg.org/) adresinde birçok ücretsiz metin bulabilirsiniz; örneğin, Lewis Carroll'un [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) adlı eserine doğrudan bağlantı. Ya da, aşağıdaki kodu kullanarak Shakespeare'in oyunlarını edinebilirsiniz:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Keşfet!

Eğer zamanınız varsa ve konuya daha derinlemesine dalmak istiyorsanız, birkaç şeyi keşfetmeyi deneyin:

* Gömme boyutunun sonuçları nasıl etkilediği?
* Farklı metin stillerinin sonuçları nasıl etkilediği?
* Çok farklı türde kelimeler ve eşanlamlılarını alın, vektör temsillerini elde edin, boyutları 2'ye indirmek için PCA uygulayın ve bunları 2D alanda çizin. Herhangi bir desen görüyor musunuz?

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.