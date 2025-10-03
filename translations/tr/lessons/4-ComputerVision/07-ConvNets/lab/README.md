<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-26T07:29:00+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "tr"
}
-->
# Evcil Hayvan Yüzlerinin Sınıflandırılması

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) kapsamında bir laboratuvar ödevi.

## Görev

Bir evcil hayvan yuvası için tüm evcil hayvanları kataloglayacak bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan otomatik olarak cinsin tespit edilmesi olurdu. Bu, sinir ağları kullanılarak başarıyla yapılabilir.

**Pet Faces** veri kümesini kullanarak farklı kedi ve köpek cinslerini sınıflandırmak için bir evrişimli sinir ağı eğitmeniz gerekiyor.

## Veri Kümesi

**Pet Faces** veri kümesini kullanacağız. Bu veri kümesi, [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri kümesinden türetilmiştir. 35 farklı köpek ve kedi cinsini içerir.

![Ele alacağımız veri kümesi](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.tr.png)

Veri kümesini indirmek için şu kod parçasını kullanın:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Başlangıç Not Defteri

Laboratuvara [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) dosyasını açarak başlayın.

## Çıkarım

Sıfırdan bir görüntü sınıflandırma problemini çözmeyi başardınız! Oldukça fazla sınıf vardı ve yine de makul bir doğruluk elde edebildiniz! Ayrıca, top-k doğruluğunu ölçmek mantıklıdır, çünkü insanlar için bile açıkça farklı olmayan bazı sınıfları karıştırmak kolaydır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.