# Oxford Evcil Hayvanlarının Transfer Öğrenimi ile Sınıflandırılması

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) için Laboratuvar Görevi.

## Görev

Bir evcil hayvan kreşi için tüm evcil hayvanları kataloglamak üzere bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan otomatik olarak cinsi keşfetmektir. Bu görevde, [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri setinden gerçek hayattaki evcil hayvan görüntülerini sınıflandırmak için transfer öğrenimini kullanacağız.

## Veri Seti

35 farklı köpek ve kedi cinsini içeren orijinal [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri setini kullanacağız.

Veri setini indirmek için bu kod parçasını kullanın:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Not Defterini Başlatma

Laboratuvara [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) dosyasını açarak başlayın.

## Önemli Nokta

Transfer öğrenimi ve önceden eğitilmiş ağlar, gerçek dünya görüntü sınıflandırma problemlerini nispeten kolay bir şekilde çözmemizi sağlar. Ancak, önceden eğitilmiş ağlar benzer türdeki görüntüler üzerinde iyi çalışır ve çok farklı görüntüleri (örneğin, tıbbi görüntüler) sınıflandırmaya başlarsak, muhtemelen çok daha kötü sonuçlar alırız.

**Sorumluluk Reddi**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.