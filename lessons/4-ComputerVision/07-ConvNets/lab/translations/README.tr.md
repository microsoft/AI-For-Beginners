# Evcil Hayvan Yüzlerinin Sınıflandırılması

[Yeni Başlayanlar için YZ Müfredatı](https://github.com/microsoft/ai-for-beginners)'dan Laboratuvar Ödevi.

## Görev

Tüm evcil hayvanları kataloglamak için evcil hayvan bakımı için bir uygulama geliştirmeniz gerektiğini hayal edin. Böyle bir uygulamanın harika özelliklerinden biri, bir fotoğraftan türün otomatik olarak keşfedilmesi olacaktır. Bu, sinir ağları kullanılarak başarıyla yapılabilir.

**Evcil Hayvan Yüzleri** veri kümesini kullanarak farklı kedi ve köpek türlerini sınıflandırmak için evrişimli bir sinir ağı eğitmeniz gerekir.

## Veri Kümesi

[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) evcil hayvan veri kümesinden türetilen **Evcil Hayvan Yüzleri** veri kümesini kullanacağız. 35 farklı cins köpek ve kedi içerir.

![Ele alacağımız veri kümesi](../images/data.png)

Veri kümesini indirmek için şu kod parçacığını kullanın:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Not Defterini Başlatma

[PetFaces.tr.ipynb](PetFaces.tr.ipynb)'yi açarak laboratuvarı başlatın.

## Ana Fikirler

You have solved a relatively complex problem of image classification from scratch! There were quite a lot of classes, and you were still able to get reasonable accuracy! It also makes sense to measure top-k accuracy, because it is easy to confuse some of the classes which are not clearly different even to human beings.

Nispeten karmaşık bir imge sınıflandırma problemini sıfırdan çözdünüz! Oldukça fazla sınıf vardı ve yine de makul bir doğruluk elde edebildiniz! İlk-k doğruluğunu ölçmek de mantıklıdır, çünkü insanlar için bile açıkça farklı olmayan bazı sınıfları karıştırmak kolaydır.
