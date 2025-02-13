# Çoklu Sınıf Sınıflandırması ile Perceptron

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) projesinden laboratuvar ödevi.

## Görev

Bu derste geliştirdiğimiz MNIST el yazısı rakamlarının ikili sınıflandırması için yazdığımız kodu kullanarak, herhangi bir rakamı tanıyabilen çoklu sınıf sınıflandırıcısı oluşturun. Eğitim ve test veri setinde sınıflandırma doğruluğunu hesaplayın ve karışıklık matrisini yazdırın.

## İpuçları

1. Her rakam için "bu rakam vs. diğer tüm rakamlar" için bir ikili sınıflandırıcı veri seti oluşturun.
1. İkili sınıflandırma için 10 farklı perceptron eğitin (her rakam için bir tane).
1. Bir girdi rakamını sınıflandıracak bir fonksiyon tanımlayın.

> **İpucu**: Tüm 10 perceptronun ağırlıklarını tek bir matriste birleştirirsek, girdi rakamlarına tüm 10 perceptronu bir matris çarpımı ile uygulayabilmemiz gerekir. En olası rakamı, çıktıya `argmax` işlemi uygulayarak bulabiliriz.

## Not Defteri Açma

Laboratuvarı [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) dosyasını açarak başlatın.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk konusunda çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alın. Orijinal belge, ana dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.