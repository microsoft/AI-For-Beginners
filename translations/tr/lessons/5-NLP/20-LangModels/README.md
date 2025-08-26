<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-26T08:45:37+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "tr"
}
-->
# Önceden Eğitilmiş Büyük Dil Modelleri

Önceki tüm görevlerimizde, etiketlenmiş bir veri kümesi kullanarak belirli bir görevi yerine getirmek için bir sinir ağı eğitiyorduk. BERT gibi büyük transformer modelleriyle, dil modellemesini kendi kendine denetimli bir şekilde kullanarak bir dil modeli oluşturuyoruz ve ardından bu modeli belirli bir alt görev için alanına özel eğitimle özelleştiriyoruz. Ancak, büyük dil modellerinin herhangi bir alanına özel eğitim olmadan birçok görevi çözebileceği gösterilmiştir. Bu tür görevleri gerçekleştirebilen model ailesine **GPT** (Generative Pre-Trained Transformer) adı verilir.

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Metin Üretimi ve Karmaşıklık (Perplexity)

Bir sinir ağının alt görev eğitimi olmadan genel görevleri yapabilme fikri, [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) makalesinde sunulmuştur. Ana fikir, birçok başka görevin **metin üretimi** kullanılarak modellenebileceğidir, çünkü metni anlamak aslında onu üretebilmek anlamına gelir. Model, insan bilgisini kapsayan büyük miktarda metin üzerinde eğitildiği için, geniş bir konu yelpazesi hakkında bilgi sahibi olur.

> Metni anlamak ve üretebilmek, çevremizdeki dünya hakkında bir şeyler bilmeyi de gerektirir. İnsanlar da büyük ölçüde okuyarak öğrenir ve GPT ağı bu açıdan benzerdir.

Metin üretim ağları, bir sonraki kelimenin olasılığını tahmin ederek çalışır $$P(w_N)$$. Ancak, bir sonraki kelimenin koşulsuz olasılığı, bu kelimenin metin korpusundaki sıklığına eşittir. GPT, önceki kelimeler göz önüne alındığında bir sonraki kelimenin **koşullu olasılığını** verebilir: $$P(w_N | w_{n-1}, ..., w_0)$$

> Olasılıklar hakkında daha fazla bilgi edinmek için [Başlangıç Seviyesi Veri Bilimi Müfredatımızı](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) okuyabilirsiniz.

Dil üretim modelinin kalitesi, **karmaşıklık (perplexity)** kullanılarak tanımlanabilir. Bu, model kalitesini herhangi bir göreve özel veri kümesi olmadan ölçmemizi sağlayan içsel bir metriktir. *Bir cümlenin olasılığı* kavramına dayanır - model, gerçek olma olasılığı yüksek bir cümleye yüksek olasılık atar (yani model bu cümle karşısında **şaşkın** değildir) ve daha az anlamlı cümlelere düşük olasılık atar (örneğin, *Can it does what?*). Modelimize gerçek bir metin korpusundan cümleler verdiğimizde, bunların yüksek olasılığa ve düşük **karmaşıklığa** sahip olmasını bekleriz. Matematiksel olarak, test kümesinin normalleştirilmiş ters olasılığı olarak tanımlanır:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face'in GPT destekli metin editörü](https://transformer.huggingface.co/doc/gpt2-large)** ile metin üretimi deneyebilirsiniz. Bu editörde, metninizi yazmaya başlarsınız ve **[TAB]** tuşuna bastığınızda size birkaç tamamlama seçeneği sunulur. Eğer seçenekler çok kısa gelirse veya memnun kalmazsanız, [TAB] tuşuna tekrar basarak daha fazla seçenek, hatta daha uzun metin parçaları alabilirsiniz.

## GPT Bir Ailedir

GPT, tek bir model değil, [OpenAI](https://openai.com) tarafından geliştirilen ve eğitilen bir model koleksiyonudur.

GPT modelleri şunlardır:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 1.5 milyar parametreye kadar dil modeli. | 175 milyar parametreye kadar dil modeli. | 100T parametreye sahip ve hem görsel hem de metin girdilerini kabul edip metin çıktıları üretebilir. |

GPT-3 ve GPT-4 modelleri, [Microsoft Azure'dan bir bilişsel hizmet](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ve [OpenAI API](https://openai.com/api/) olarak kullanılabilir.

## Prompt Mühendisliği

GPT, dil ve kodu anlamak için büyük miktarda veri üzerinde eğitildiğinden, girdilere (prompts) yanıt olarak çıktılar sağlar. Prompts, GPT'ye verilen girdiler veya sorgulardır; bu girdilerle modellerin bir sonraki görevlerini tamamlamaları için talimatlar verilir. İstenen bir sonucu elde etmek için en etkili promptu oluşturmak gerekir; bu, doğru kelimeleri, formatları, ifadeleri veya hatta sembolleri seçmeyi içerir. Bu yaklaşım, [Prompt Mühendisliği](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) olarak adlandırılır.

[Bu dokümantasyon](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum), prompt mühendisliği hakkında daha fazla bilgi sağlar.

## ✍️ Örnek Notebook: [OpenAI-GPT ile Oynamak](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Aşağıdaki notebook'larda öğrenmeye devam edin:

* [OpenAI-GPT ve Hugging Face Transformers ile Metin Üretimi](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Sonuç

Yeni genel önceden eğitilmiş dil modelleri yalnızca dil yapısını modellemekle kalmaz, aynı zamanda büyük miktarda doğal dil bilgisi içerir. Bu nedenle, bazı NLP görevlerini sıfır atış (zero-shot) veya az atış (few-shot) ayarlarında etkili bir şekilde çözmek için kullanılabilirler.

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı bir yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.