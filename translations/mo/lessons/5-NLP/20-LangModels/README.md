<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-26T08:42:39+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "mo"
}
-->
# 預訓練大型語言模型

在我們之前的所有任務中，我們都使用標註數據集訓練神經網絡來執行特定任務。對於大型的 Transformer 模型，例如 BERT，我們使用自監督的方式進行語言建模來構建語言模型，然後通過進一步的特定領域訓練使其專門化於特定的下游任務。然而，研究表明，大型語言模型也能在沒有任何特定領域訓練的情況下解決許多任務。能夠做到這一點的一系列模型被稱為 **GPT**：生成式預訓練 Transformer。

## [課前測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## 文本生成與困惑度

神經網絡能夠在沒有下游訓練的情況下執行一般任務的概念在 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 論文中提出。主要思想是許多其他任務可以通過 **文本生成** 來建模，因為理解文本本質上意味著能夠生成文本。由於模型是在包含人類知識的大量文本上進行訓練，它也因此對各種主題有廣泛的了解。

> 理解並能夠生成文本也意味著對周圍世界有所了解。人類在很大程度上也是通過閱讀來學習，而 GPT 網絡在這方面與人類相似。

文本生成網絡通過預測下一個詞的概率 $$P(w_N)$$ 來工作。然而，下一個詞的無條件概率等於該詞在文本語料庫中的出現頻率。GPT 能夠給出基於前面詞的下一個詞的 **條件概率**：$$P(w_N | w_{n-1}, ..., w_0)$$

> 您可以在我們的 [初學者數據科學課程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) 中了解更多關於概率的內容。

語言生成模型的質量可以通過 **困惑度** 來定義。這是一種內在的度量，允許我們在沒有任何特定任務數據集的情況下衡量模型的質量。它基於 *句子的概率* 的概念——模型對可能是真實的句子賦予高概率（即模型對其不 **困惑**），而對那些不太合理的句子（例如 *Can it does what?*）賦予低概率。當我們給模型提供來自真實文本語料庫的句子時，我們期望它們具有高概率和低 **困惑度**。數學上，它被定義為測試集的歸一化逆概率：
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**您可以使用 [Hugging Face 的 GPT 驅動文本編輯器](https://transformer.huggingface.co/doc/gpt2-large)** 來嘗試文本生成。在這個編輯器中，您開始撰寫文本，按下 **[TAB]** 鍵後會提供幾個完成選項。如果選項太短或您不滿意，可以再次按下 [TAB] 鍵，您將獲得更多選項，包括更長的文本片段。

## GPT 是一個家族

GPT 不是單一模型，而是一系列由 [OpenAI](https://openai.com) 開發和訓練的模型。

在 GPT 模型家族中，我們有：

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|擁有最多 15 億參數的語言模型。 | 擁有最多 175 億參數的語言模型 | 擁有 100 萬億參數，接受圖像和文本輸入並輸出文本。 |

GPT-3 和 GPT-4 模型可通過 [Microsoft Azure 的認知服務](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) 和 [OpenAI API](https://openai.com/api/) 使用。

## 提示工程

由於 GPT 已經在大量數據上進行訓練以理解語言和代碼，它能根據輸入（提示）提供輸出。提示是 GPT 的輸入或查詢，通過提示用戶向模型提供指令以完成下一個任務。為了獲得期望的結果，您需要最有效的提示，這涉及選擇合適的詞語、格式、短語甚至符號。這種方法被稱為 [提示工程](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)。

[此文檔](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) 提供了更多關於提示工程的信息。

## ✍️ 範例筆記本：[使用 OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

繼續學習以下筆記本：

* [使用 OpenAI-GPT 和 Hugging Face Transformers 生成文本](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 結論

新的通用預訓練語言模型不僅建模語言結構，還包含大量自然語言。因此，它們可以在零樣本或少樣本設置中有效地解決一些 NLP 任務。

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用此翻譯而引起的任何誤解或誤釋不承擔責任。