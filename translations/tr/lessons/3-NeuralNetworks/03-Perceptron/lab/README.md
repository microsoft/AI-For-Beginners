<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T07:36:02+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "tr"
}
-->
# Perceptron ile Çok Sınıflı Sınıflandırma

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) içindeki Lab Görevi.

## Görev

Bu derste MNIST el yazısı rakamlarının ikili sınıflandırması için geliştirdiğimiz kodu kullanarak, herhangi bir rakamı tanıyabilen bir çok sınıflı sınıflandırıcı oluşturun. Eğitim ve test veri setlerindeki sınıflandırma doğruluğunu hesaplayın ve karışıklık matrisini yazdırın.

## İpuçları

1. Her rakam için, "bu rakam vs. diğer tüm rakamlar" şeklinde bir ikili sınıflandırıcı veri seti oluşturun.
1. İkili sınıflandırma için 10 farklı perceptron eğitin (her rakam için bir tane).
1. Bir giriş rakamını sınıflandıracak bir fonksiyon tanımlayın.

> **İpucu**: Eğer 10 perceptronun ağırlıklarını bir matris içinde birleştirirsek, tüm 10 perceptronu giriş rakamlarına tek bir matris çarpımıyla uygulayabiliriz. En olası rakam, çıktıya `argmax` işlemi uygulanarak bulunabilir.

## Başlangıç Not Defteri

Laba [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) dosyasını açarak başlayın.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.