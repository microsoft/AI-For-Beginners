# Hollywood Heads Veri Seti Kullanarak Kafa Tespiti

[AI for Beginners Müfredatı](https://github.com/microsoft/ai-for-beginners) kapsamında bir laboratuvar çalışması.

## Görev

Video gözetim kamera akışında kişi sayısını saymak, mağazalardaki ziyaretçi sayısını, restoranlardaki yoğun saatleri vb. tahmin etmemizi sağlayan önemli bir görevdir. Bu görevi çözmek için, insan kafalarını farklı açılardan tespit edebilmemiz gerekir. İnsan kafalarını tespit etmek için bir nesne algılama modeli eğitmek amacıyla [Hollywood Heads Veri Seti](https://www.di.ens.fr/willow/research/headdetection/) kullanılabilir.

## Veri Seti

[Hollywood Heads Veri Seti](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip), Hollywood filmlerinden alınmış 224,740 film karesinde 369,846 insan kafası anotasyonunu içerir. Veri seti, [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) formatında sunulmaktadır. Her bir görüntü için aşağıdaki gibi bir XML açıklama dosyası bulunmaktadır:

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

Bu veri setinde yalnızca bir nesne sınıfı vardır: `head`. Her bir kafa için, sınırlayıcı kutunun koordinatları sağlanır. XML dosyalarını Python kütüphaneleri kullanarak ayrıştırabilir veya doğrudan PASCAL VOC formatıyla çalışmak için [bu kütüphaneyi](https://pypi.org/project/pascal-voc/) kullanabilirsiniz.

## Nesne Algılama Modeli Eğitimi

Bir nesne algılama modeli aşağıdaki yöntemlerden biriyle eğitilebilir:

* Modeli bulutta programlı bir şekilde eğitmek için [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ve Python API'sini kullanabilirsiniz. Custom Vision, modeli eğitmek için birkaç yüz görüntüden fazlasını kullanamayabilir, bu nedenle veri setini sınırlamanız gerekebilir.
* RetunaNet modelini eğitmek için [Keras eğitiminden](https://keras.io/examples/vision/retinanet/) örnek kullanabilirsiniz.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) modülünü kullanarak torchvision içindeki yerleşik modülü tercih edebilirsiniz.

## Çıkarım

Nesne algılama, endüstride sıkça ihtiyaç duyulan bir görevdir. [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) gibi nesne algılama işlemleri için kullanılabilecek bazı hizmetler olsa da, nesne algılamanın nasıl çalıştığını anlamak ve kendi modellerinizi eğitebilmek önemlidir.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.