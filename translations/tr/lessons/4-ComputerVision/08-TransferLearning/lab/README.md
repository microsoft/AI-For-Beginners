# Oxford Evcil Hayvanlarının Transfer Öğrenimi ile Sınıflandırılması

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) kapsamında bir laboratuvar görevi.

## Görev

Bir evcil hayvan yuvası için tüm hayvanları kataloglayacak bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan otomatik olarak türü tanımlayabilmesi olurdu. Bu görevde, [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri setinden gerçek hayvan görüntülerini sınıflandırmak için transfer öğrenimini kullanacağız.

## Veri Seti

Orijinal [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri setini kullanacağız. Bu veri seti, 35 farklı köpek ve kedi türünü içermektedir.

Veri setini indirmek için şu kod parçasını kullanabilirsiniz:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Not Defteri Başlatma

Laboratuvara [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) dosyasını açarak başlayın.

## Çıkarım

Transfer öğrenimi ve önceden eğitilmiş ağlar, gerçek dünya görüntü sınıflandırma problemlerini nispeten kolay bir şekilde çözmemizi sağlar. Ancak, önceden eğitilmiş ağlar benzer türdeki görüntülerde iyi çalışır ve çok farklı görüntüleri (örneğin, tıbbi görüntüler) sınıflandırmaya başladığımızda muhtemelen çok daha kötü sonuçlar alırız.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.