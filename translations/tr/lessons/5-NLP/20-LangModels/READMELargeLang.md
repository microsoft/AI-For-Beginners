# Önceden Eğitilmiş Büyük Dil Modelleri

Önceki görevlerimizde, etiketlenmiş veri seti kullanarak belirli bir görevi yerine getirmek için bir sinir ağı eğitiyorduk. BERT gibi büyük dönüştürücü modellerle, dil modellemesini kendi kendine denetimli bir şekilde kullanarak bir dil modeli oluşturuyoruz; bu model daha sonra belirli bir alt görev için daha fazla alan spesifik eğitimi ile özelleştiriliyor. Ancak, büyük dil modellerinin herhangi bir alan spesifik eğitimi olmadan birçok görevi de çözebileceği gösterilmiştir. Bunu yapabilen modeller ailesine **GPT** denir: Üretken Önceden Eğitilmiş Dönüştürücü.

## [Öncesi ders sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Metin Üretimi ve Perpleksite

Bir sinir ağının alt görev eğitimi olmadan genel görevleri yerine getirebilmesi fikri, [Dil Modelleri Denetimsiz Çoklu Görev Öğrenicileridir](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) makalesinde sunulmuştur. Ana fikir, birçok diğer görevin **metin üretimi** kullanılarak modellenebileceğidir; çünkü metni anlamak, esasen onu üretebilme yeteneği anlamına gelir. Model, insan bilgisini kapsayan devasa bir metin miktarı üzerinde eğitildiğinden, çeşitli konularda da bilgi sahibi olur.

> Metni anlamak ve üretebilmek, çevremizdeki dünya hakkında bir şeyler bilmekle de ilgilidir. İnsanlar da büyük ölçüde okuyarak öğrenirler ve GPT ağı bu açıdan benzerlik gösterir.

Metin üretim ağları, bir sonraki kelimenin olasılığını $$P(w_N)$$ tahmin ederek çalışır. Ancak, bir sonraki kelimenin koşulsuz olasılığı, bu kelimenin metin koleksiyonundaki sıklığına eşittir. GPT, önceki kelimeleri göz önünde bulundurarak bir sonraki kelimenin **koşullu olasılığını** bize verebilir: $$P(w_N | w_{n-1}, ..., w_0)$$

> Olasılıklar hakkında daha fazla bilgi için [Veri Bilimi Başlangıç Curriculum'umuza](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) göz atabilirsiniz.

Dil üreten modelin kalitesi **perpleksite** ile tanımlanabilir. Bu, görev spesifik veri setine ihtiyaç duymadan model kalitesini ölçmemizi sağlayan içsel bir metriktir. Bir cümlenin *olasılığı* kavramına dayanmaktadır - model, gerçek olma olasılığı yüksek olan bir cümleye yüksek olasılık atar (yani model bu cümleye **perpleks** değildir) ve daha az anlam ifade eden cümlelere düşük olasılık atar (örneğin, *Bunu yapabilir mi?*). Modelimize gerçek metin koleksiyonundan cümleler verdiğimizde, bu cümlelerin yüksek olasılığa ve düşük **perpleksiteye** sahip olmasını bekleriz. Matematiksel olarak, test setinin normalize edilmiş ters olasılığı olarak tanımlanır:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Metin üretimi ile deney yapabilirsiniz [Hugging Face'den GPT destekli metin editörü](https://transformer.huggingface.co/doc/gpt2-large)**. Bu editörde, metninizi yazmaya başlarsınız ve **[TAB]** tuşuna basmak size birkaç tamamlama seçeneği sunar. Eğer bunlar çok kısa ise veya memnun kalmazsanız - tekrar [TAB] tuşuna basın, daha fazla seçenek elde edersiniz; bunlar arasında daha uzun metin parçaları da bulunur.

## GPT Bir Ailedir

GPT, tek bir model değil, [OpenAI](https://openai.com) tarafından geliştirilen ve eğitilen modellerin bir koleksiyonudur.

GPT modelleri altında, şunlar bulunmaktadır:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 1.5 milyar parametreye kadar dil modeli. | 175 milyar parametreye kadar dil modeli | 100T parametre ve hem görsel hem de metin girdilerini kabul edip metin çıktısı verir. |

GPT-3 ve GPT-4 modelleri [Microsoft Azure'dan bilişsel bir hizmet olarak](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ve [OpenAI API'si](https://openai.com/api/) olarak mevcuttur.

## İstek Mühendisliği

GPT, dil ve kodu anlamak için geniş veri hacimlerinde eğitildiğinden, girdilere (isteklere) yanıt olarak çıktılar sağlar. İstekler, bir modelin tamamlayacağı görevler hakkında talimatlar veren GPT girdileri veya sorgularıdır. İstenilen bir sonucu elde etmek için, doğru kelimeleri, formatları, ifadeleri veya hatta sembolleri seçmek gibi en etkili isteğe ihtiyacınız vardır. Bu yaklaşım [İstek Mühendisliği](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) olarak adlandırılır.

[Bu belgede](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) istek mühendisliği hakkında daha fazla bilgi bulabilirsiniz.

## ✍️ Örnek Not Defteri: [OpenAI-GPT ile Oynama](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Aşağıdaki not defterlerinde öğrenmeye devam edin:

* [OpenAI-GPT ve Hugging Face Dönüştürücüleri ile metin üretimi](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Sonuç

Yeni genel önceden eğitilmiş dil modelleri sadece dil yapısını modellemekle kalmaz, aynı zamanda büyük miktarda doğal dil içerir. Bu nedenle, bazı NLP görevlerini sıfırdan veya az sayıda örnekle çözmek için etkili bir şekilde kullanılabilirler.

## [Ders sonrası sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa önem vermemize rağmen, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Belgenin orijinal metni, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.