# Evcil Hayvan Yüzlerinin Sınıflandırılması

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) dersinden laboratuvar ödevi.

## Görev

Bir evcil hayvan kreşi için tüm evcil hayvanları kataloglamak üzere bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan cinsi otomatik olarak keşfetmektir. Bu, sinir ağları kullanılarak başarıyla yapılabilir.

Farklı kedi ve köpek ırklarını sınıflandırmak için bir konvolüsyonel sinir ağını **Pet Faces** veri setini kullanarak eğitmeniz gerekiyor.

## Veri Seti

**Pet Faces** veri setini kullanacağız, bu veri seti [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri setinden türetilmiştir. 35 farklı köpek ve kedi ırkını içermektedir.

![İşleyeceğimiz veri seti](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.tr.png)

Veri setini indirmek için bu kod parçasını kullanın:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Not Defterini Açma

Laboratuvara [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) dosyasını açarak başlayın.

## Alınacak Ders

Sıfırdan bir görüntü sınıflandırma problemini oldukça karmaşık bir şekilde çözdünüz! Oldukça fazla sınıf vardı ve yine de makul bir doğruluk elde etmeyi başardınız! Ayrıca, bazı sınıfların insanlara bile belirgin şekilde farklı gelmediği durumlarda, en iyi-k doğruluğunu ölçmek mantıklıdır.

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucu ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.