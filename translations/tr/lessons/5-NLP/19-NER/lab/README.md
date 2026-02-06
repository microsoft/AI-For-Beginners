# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) içindeki Laboratuvar Görevi.

## Görev

Bu laboratuvarda, tıbbi terimler için adlandırılmış varlık tanıma (NER) modeli eğitmeniz gerekiyor.

## Veri Seti

NER modelini eğitmek için, tıbbi varlıklarla düzgün bir şekilde etiketlenmiş bir veri setine ihtiyacımız var. [BC5CDR veri seti](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/), 1500'den fazla makaleden etiketlenmiş hastalık ve kimyasal varlıkları içerir. Veri setini, web sitelerinde kayıt olduktan sonra indirebilirsiniz.

BC5CDR veri seti şu şekilde görünür:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Bu veri setinde, ilk iki satırda makale başlığı ve özeti bulunur, ardından başlık+özet bloğu içindeki başlangıç ve bitiş pozisyonlarıyla bireysel varlıklar yer alır. Varlık türüne ek olarak, bu varlığın bazı tıbbi ontolojiler içindeki ontoloji kimliğini de alırsınız.

Bu veriyi BIO kodlamasına dönüştürmek için biraz Python kodu yazmanız gerekecek.

## Ağ

NER için ilk deneme, ders sırasında gördüğünüz örnekte olduğu gibi LSTM ağı kullanılarak yapılabilir. Ancak, NLP görevlerinde [transformer mimarisi](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ve özellikle [BERT dil modelleri](https://en.wikipedia.org/wiki/BERT_(language_model)) çok daha iyi sonuçlar verir. Önceden eğitilmiş BERT modelleri, bir dilin genel yapısını anlar ve nispeten küçük veri setleri ve hesaplama maliyetleriyle belirli görevler için ince ayar yapılabilir.

NER'yi tıbbi bir senaryoya uygulamayı planladığımız için, tıbbi metinler üzerinde eğitilmiş bir BERT modeli kullanmak mantıklıdır. Microsoft Research, [PubMed](https://pubmed.ncbi.nlm.nih.gov/) deposundaki metinler kullanılarak ince ayar yapılmış [PubMedBERT][PubMedBERT] ([yayın][PubMedBERT-Pub]) adlı önceden eğitilmiş bir model yayınladı.

Transformer modellerini eğitmek için *de facto* standart, [Hugging Face Transformers](https://huggingface.co/) kütüphanesidir. Bu kütüphane, PubMedBERT dahil olmak üzere topluluk tarafından sürdürülen önceden eğitilmiş modellerin bir deposunu içerir. Bu modeli yüklemek ve kullanmak için sadece birkaç satır kod yeterlidir:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Bu kod bize `model` nesnesini, `classes` sayıda sınıf kullanarak token sınıflandırma görevi için oluşturulmuş bir model olarak, ve giriş metnini tokenlara bölebilen `tokenizer` nesnesini verir. Veri setini BIO formatına dönüştürmeniz gerekecek ve bunu yaparken PubMedBERT tokenizasyonunu dikkate almalısınız. [Bu Python kodu](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ilham kaynağı olarak kullanılabilir.

## Çıkarım

Bu görev, doğal dil metinlerinin büyük hacimlerinde daha fazla içgörü elde etmek istiyorsanız karşılaşabileceğiniz gerçek bir göreve oldukça yakındır. Bizim durumumuzda, eğitilmiş modelimizi [COVID ile ilgili makaleler veri setine](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) uygulayabilir ve hangi içgörüleri elde edebileceğimizi görebiliriz. [Bu blog yazısı](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ve [bu makale](https://www.mdpi.com/2504-2289/6/1/4), NER kullanılarak bu makale derlemesi üzerinde yapılabilecek araştırmaları açıklamaktadır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.