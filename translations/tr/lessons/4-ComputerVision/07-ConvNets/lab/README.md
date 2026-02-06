# Evcil Hayvan Yüzlerinin Sınıflandırılması

[AI for Beginners Müfredatı](https://github.com/microsoft/ai-for-beginners) kapsamında bir laboratuvar görevi.

## Görev

Bir evcil hayvan yuvası için tüm evcil hayvanları kataloglamak amacıyla bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan otomatik olarak cinsin keşfedilmesi olacaktır. Bu, sinir ağları kullanılarak başarıyla yapılabilir.

**Pet Faces** veri setini kullanarak farklı kedi ve köpek cinslerini sınıflandırmak için bir evrişimli sinir ağı eğitmeniz gerekiyor.

## Veri Seti

[Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/) veri setini kullanacağız. Bu veri seti, 37 farklı köpek ve kedi cinsine ait görüntüler içerir.

![Çalışacağımız veri seti](../../../../../../translated_images/tr/data.50b2a9d5484bdbf0.webp)

Veri setini indirmek için şu kod parçacığını kullanın:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

**Not:** Oxford-IIIT Pet Dataset görüntüleri dosya adına göre düzenlenmiştir (örneğin, `Abyssinian_1.jpg`, `Bengal_2.jpg`). Notebook, bu görüntüleri daha kolay sınıflandırma için cinslere özgü alt dizinlere organize etmek üzere kod içerir.

## Başlangıç Notebook'u

Laboratuvara [PetFaces.ipynb](PetFaces.ipynb) dosyasını açarak başlayın.

## Çıkarım

Sıfırdan nispeten karmaşık bir görüntü sınıflandırma problemini çözdünüz! Oldukça fazla sınıf vardı ve yine de makul bir doğruluk elde edebildiniz! Ayrıca, top-k doğruluğu ölçmek mantıklıdır, çünkü bazı sınıfları karıştırmak kolaydır; hatta insanlar için bile açıkça farklı olmayan sınıflar olabilir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.