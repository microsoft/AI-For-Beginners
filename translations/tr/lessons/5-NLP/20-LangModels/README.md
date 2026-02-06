# Önceden Eğitilmiş Büyük Dil Modelleri

Önceki tüm görevlerimizde, etiketlenmiş bir veri seti kullanarak belirli bir görevi yerine getirmek için bir sinir ağı eğitiyorduk. BERT gibi büyük transformer modelleriyle, dil modelleme işlemini kendi kendine denetimli bir şekilde kullanarak bir dil modeli oluşturuyoruz ve ardından bu modeli belirli bir alt görev için alanına özel eğitimle özelleştiriyoruz. Ancak, büyük dil modellerinin herhangi bir alanına özel eğitim olmadan birçok görevi çözebileceği gösterilmiştir. Bu tür görevleri gerçekleştirebilen model ailesine **GPT**: Generative Pre-Trained Transformer denir.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Metin Üretimi ve Perpleksite

Bir sinir ağının alt görev eğitimi olmadan genel görevleri yapabilme fikri, [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) makalesinde sunulmuştur. Ana fikir, birçok diğer görevin **metin üretimi** kullanılarak modellenebileceğidir, çünkü metni anlamak aslında onu üretebilmek anlamına gelir. Model, insan bilgisini kapsayan büyük miktarda metin üzerinde eğitildiği için, geniş bir konu yelpazesi hakkında bilgi sahibi olur.

> Metni anlamak ve üretebilmek, çevremizdeki dünya hakkında bir şeyler bilmeyi de gerektirir. İnsanlar büyük ölçüde okuyarak öğrenir ve GPT ağı bu açıdan benzer bir şekilde çalışır.

Metin üretim ağları, bir sonraki kelimenin olasılığını tahmin ederek çalışır $$P(w_N)$$ Ancak, bir sonraki kelimenin koşulsuz olasılığı, bu kelimenin metin corpusundaki sıklığına eşittir. GPT, önceki kelimeler göz önüne alındığında bir sonraki kelimenin **koşullu olasılığını** verebilir: $$P(w_N | w_{n-1}, ..., w_0)$$

> Olasılıklar hakkında daha fazla bilgi için [Data Science for Beginners Müfredatımızı](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) okuyabilirsiniz.

Dil üretim modelinin kalitesi **perpleksite** kullanılarak tanımlanabilir. Bu, herhangi bir göreve özel veri seti olmadan model kalitesini ölçmemizi sağlayan içsel bir metriktir. *Bir cümlenin olasılığı* kavramına dayanır - model, gerçek olma olasılığı yüksek bir cümleye yüksek olasılık atar (yani model bu cümle karşısında **şaşkın** değildir) ve daha az anlam ifade eden cümlelere düşük olasılık atar (örneğin, *Can it does what?*). Modelimize gerçek bir metin corpusundan cümleler verdiğimizde, bu cümlelerin yüksek olasılığa ve düşük **perpleksiteye** sahip olmasını bekleriz. Matematiksel olarak, test setinin normalize edilmiş ters olasılığı olarak tanımlanır:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face'in GPT destekli metin editörü](https://transformer.huggingface.co/doc/gpt2-large)** ile metin üretimini deneyebilirsiniz. Bu editörde, metninizi yazmaya başlarsınız ve **[TAB]** tuşuna basarak birkaç tamamlama seçeneği alırsınız. Eğer seçenekler çok kısa veya tatmin edici değilse, tekrar [TAB] tuşuna basarak daha fazla seçenek, hatta daha uzun metin parçaları alabilirsiniz.

## GPT Bir Ailedir

GPT tek bir model değil, [OpenAI](https://openai.com) tarafından geliştirilen ve eğitilen bir model koleksiyonudur.

GPT modelleri altında şunlar bulunur:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 1.5 milyar parametreye kadar dil modeli. | 175 milyar parametreye kadar dil modeli | 100T parametreye sahip ve hem görüntü hem de metin girdilerini kabul edip metin çıktıları verir. |

GPT-3 ve GPT-4 modelleri [Microsoft Azure'dan bir bilişsel hizmet olarak](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ve [OpenAI API](https://openai.com/api/) olarak kullanılabilir.

## Prompt Mühendisliği

GPT, dil ve kodu anlamak için büyük miktarda veri üzerinde eğitildiğinden, girdilere (prompts) yanıt olarak çıktılar sağlar. Prompts, GPT'ye verilen girdiler veya sorgulardır; burada modellerin tamamlaması gereken görevler için talimatlar verilir. İstenilen sonucu elde etmek için en etkili promptu oluşturmak gerekir; bu, doğru kelimeleri, formatları, ifadeleri veya hatta sembolleri seçmeyi içerir. Bu yaklaşım [Prompt Mühendisliği](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) olarak adlandırılır.

[Bu dokümantasyon](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) size prompt mühendisliği hakkında daha fazla bilgi sağlar.

## ✍️ Örnek Notebook: [OpenAI-GPT ile Oynamak](GPT-PyTorch.ipynb)

Aşağıdaki notebooklarda öğrenmeye devam edin:

* [OpenAI-GPT ve Hugging Face Transformers ile metin üretimi](GPT-PyTorch.ipynb)

## Sonuç

Yeni genel önceden eğitilmiş dil modelleri yalnızca dil yapısını modellemekle kalmaz, aynı zamanda büyük miktarda doğal dil içerir. Bu nedenle, bazı NLP görevlerini sıfır-shot veya az-shot ayarlarında etkili bir şekilde çözmek için kullanılabilirler.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

