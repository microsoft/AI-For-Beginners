# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) için Laboratuvar Görevi.

## Görev

Bu laboratuvar çalışmasında, tıbbi terimler için adlandırılmış varlık tanıma modeli eğitmeniz gerekiyor.

## Veri Seti

NER modelini eğitmek için, tıbbi varlıklarla düzgün bir şekilde etiketlenmiş bir veri setine ihtiyacımız var. [BC5CDR veri seti](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 1500'den fazla makaleden etiketlenmiş hastalıklar ve kimyasallar içeren varlıklar içerir. Veri setini indirmek için web sitelerinde kayıt olmanız gerekmektedir.

BC5CDR Veri Seti şu şekilde görünmektedir:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Bu veri setinde, ilk iki satırda makale başlığı ve özeti bulunmakta, ardından başlık+özet bloğu içinde başlangıç ve bitiş konumlarıyla birlikte bireysel varlıklar yer almaktadır. Varlık türüne ek olarak, bu varlığın belirli bir tıbbi ontolojideki ontoloji kimliğini de alırsınız.

Bunu BIO kodlamasına dönüştürmek için bazı Python kodları yazmanız gerekecek.

## Ağ

NER için ilk deneme, ders sırasında gördüğünüz gibi LSTM ağı kullanılarak yapılabilir. Ancak, NLP görevlerinde, [transformer mimarisi](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ve özellikle [BERT dil modelleri](https://en.wikipedia.org/wiki/BERT_(language_model)) çok daha iyi sonuçlar göstermektedir. Önceden eğitilmiş BERT modelleri, bir dilin genel yapısını anlamakta ve belirli görevler için nispeten küçük veri setleri ve hesaplama maliyetleri ile ince ayar yapılabilmektedir.

Tıbbi senaryoya NER uygulamayı planladığımız için, tıbbi metinler üzerinde eğitilmiş BERT modelini kullanmak mantıklıdır. Microsoft Research, [PubMedBERT][PubMedBERT] ([yayın][PubMedBERT-Pub]) adında önceden eğitilmiş bir model yayınladı; bu model, [PubMed](https://pubmed.ncbi.nlm.nih.gov/) deposundan alınan metinlerle ince ayar yapılmıştır.

Transformer modellerini eğitmek için *de facto* standart, [Hugging Face Transformers](https://huggingface.co/) kütüphanesidir. Ayrıca, PubMedBERT de dahil olmak üzere, topluluk tarafından bakım yapılan önceden eğitilmiş modellerin bir deposunu içerir. Bu modeli yüklemek ve kullanmak için sadece birkaç satır kod yazmamız yeterlidir:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Bu, girdi metnini token'lara bölebilen `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` nesnesini verir. Veri setini BIO formatına dönüştürmeniz gerekecek ve PubMedBERT tokenizasyonunu dikkate almanız önemlidir. İlham almak için [bu Python kodu parçasını](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) kullanabilirsiniz.

## Özet

Bu görev, doğal dil metinleri hakkında daha fazla içgörü elde etmek istiyorsanız muhtemelen karşılaşacağınız gerçek bir göreve çok yakındır. Bizim durumumuzda, eğitilmiş modelimizi [COVID ile ilgili makalelerin veri setine](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) uygulayabilir ve hangi içgörüleri elde edebileceğimizi görebiliriz. [Bu blog yazısı](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ve [bu makale](https://www.mdpi.com/2504-2289/6/1/4), NER kullanarak bu makaleler koleksiyonu üzerinde yapılabilecek araştırmaları tanımlamaktadır.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.