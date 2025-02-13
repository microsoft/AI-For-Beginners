# Hollywood Heads Veri Seti ile Baş

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) laboratuvar ödevi.

## Görev

Video gözetim kameralarıyla insan sayısını saymak, mağazalardaki ziyaretçi sayısını, restoranlardaki yoğun saatleri tahmin etmemizi sağlayan önemli bir görevdir. Bu görevi çözmek için, insan başlarını farklı açılardan tespit edebilmemiz gerekiyor. İnsan başlarını tespit etmek için bir nesne tespit modeli eğitmek amacıyla [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) kullanılabilir.

## Veri Seti

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip), Hollywood filmlerinden 224,740 film karesinde 369,846 insan başı içermektedir. Her resim için ayrıca şu şekilde görünen bir XML açıklama dosyası bulunmaktadır:

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

Bu veri setinde yalnızca bir nesne sınıfı olan `head` bulunmaktadır ve her baş için sınırlayıcı kutunun koordinatlarını alırsınız. XML'yi Python kütüphaneleri kullanarak ayrıştırabilir veya PASCAL VOC formatıyla doğrudan çalışmak için [bu kütüphaneyi](https://pypi.org/project/pascal-voc/) kullanabilirsiniz.

## Nesne Tespiti Eğitimi

Aşağıdaki yöntemlerden birini kullanarak bir nesne tespit modeli eğitebilirsiniz:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ve Python API'sini kullanarak modeli bulutta programatik olarak eğitmek. Özel vizyon, modeli eğitmek için birkaç yüz resimden fazlasını kullanamayacağından, veri setini sınırlamanız gerekebilir.
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) örneğini kullanarak RetinaNet modelini eğitmek.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) modülünü torchvision içinde kullanmak.

## Önemli Nokta

Nesne tespiti, sanayide sıkça gereken bir görevdir. Nesne tespiti gerçekleştirmek için kullanılabilecek bazı hizmetler olsa da (örneğin, [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), nesne tespitinin nasıl çalıştığını anlamak ve kendi modellerinizi eğitebilmek önemlidir.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.