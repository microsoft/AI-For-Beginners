# Perceptron ile Çok Sınıflı Sınıflandırma

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ders planından Laboratuvar Çalışması.

## Görev

Bu derste MNIST el yazısı rakamlarının ikili sınıflandırması için geliştirdiğimiz kodu kullanarak, herhangi bir rakamı tanıyabilecek bir çok sınıflı sınıflandırıcı oluşturun. Eğitim ve test veri setlerindeki sınıflandırma doğruluğunu hesaplayın ve karışıklık matrisini yazdırın.

## İpuçları

1. Her rakam için, "bu rakam vs. diğer tüm rakamlar" ikili sınıflandırıcısı için bir veri seti oluşturun.
1. İkili sınıflandırma için 10 farklı perceptron eğitin (her rakam için bir tane).
1. Bir giriş rakamını sınıflandıracak bir fonksiyon tanımlayın.

> **İpucu**: Eğer tüm 10 perceptronun ağırlıklarını tek bir matris içinde birleştirirsek, giriş rakamlarına tüm 10 perceptronu tek bir matris çarpımıyla uygulayabiliriz. En olası rakam, çıktı üzerinde `argmax` işlemi uygulanarak bulunabilir.

## Başlangıç Not Defteri

Laboratuvara [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb) dosyasını açarak başlayın.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.