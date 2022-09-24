# Algılayıcı ile Çok Sınıflı Sınıflandırma

[Yeni Başlayanlar için Yapay Zeka Müfredatı](https://github.com/microsoft/ai-for-beginners)'ndan Laboratuvar Ödevi.

## Görevs

MNIST el yazısı rakamlarının ikili sınıflandırması için bu derste geliştirdiğimiz kodu kullanarak, herhangi bir rakamı tanıyabilecek çok sınıflı bir sınıflandırma oluşturun. Eğitim ve test veri kümesindeki sınıflandırma doğruluğunu hesaplayın ve hata matrisini yazdırın.

## İpuçları

1. Her rakam için, "bu rakam ve diğer tüm rakamlar" ikili sınıflandırıcısı için bir veri kümesi oluşturun.
1. İkili sınıflandırma için 10 farklı algılayıcı eğitin (her rakam için bir tane).
1. Bir girdi rakamını sınıflandıracak bir fonksiyon tanımlayın.

> **Hint**: If we combine weights of all 10 perceptrons into one matrix, we should be able to apply all 10 perceptrons to the input digits by one matrix multiplication. Most probable digit can then be found just by applying `argmax` operation on the output.

**İpucu**: Tüm 10 algılayıcının ağırlıklarını tek bir matriste birleştirirsek, 10 algılayıcının tümünü bir matris çarpımı ile girdi rakamlarına uygulayabilmeliyiz. En olası basamak, çıktıya yalnızca `argmax` işlemi uygulanarak bulunabilir.

## Başlangıç Not Defteri

[PerceptronMultiClass.tr.ipynb](PerceptronMultiClass.tr.ipynb) dosyasını açarak laboratuvarı başlatın.
