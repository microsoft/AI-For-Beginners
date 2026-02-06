# 多模態網絡

在 Transformer 模型成功解決 NLP 任務後，相同或類似的架構也被應用於計算機視覺任務。如今，越來越多的研究致力於構建能夠**結合**視覺和自然語言能力的模型。其中一個嘗試是由 OpenAI 開發的 CLIP 和 DALL.E。

## 對比式圖像預訓練（CLIP）

CLIP 的核心思想是能夠比較文本提示與圖像，並判斷圖像與提示的匹配程度。

![CLIP 架構](../../../../../translated_images/zh-MO/clip-arch.b3dbf20b4e8ed8be.webp)

> *圖片來源於[這篇博客](https://openai.com/blog/clip/)*

該模型基於從互聯網獲取的圖像及其標題進行訓練。對於每個批次，我們取 N 對 (圖像, 文本)，並將它們轉換為一些向量表示 I 和 T。這些表示隨後會進行匹配。損失函數的定義是最大化同一對（例如 I 和 T）之間向量的餘弦相似度，同時最小化所有其他對之間的餘弦相似度。因此，這種方法被稱為**對比式**。

CLIP 模型/庫可以從 [OpenAI GitHub](https://github.com/openai/CLIP) 獲取。該方法的介紹可以參考[這篇博客](https://openai.com/blog/clip/)，更詳細的描述則在[這篇論文](https://arxiv.org/pdf/2103.00020.pdf)中。

在模型預訓練完成後，我們可以提供一批圖像和一批文本提示，模型會返回一個概率張量。CLIP 可以用於多種任務：

**圖像分類**

假設我們需要在貓、狗和人之間對圖像進行分類。在這種情況下，我們可以將圖像和一系列文本提示輸入模型，例如：“*一張貓的照片*”、“*一張狗的照片*”、“*一張人的照片*”。在結果的 3 個概率向量中，我們只需選擇值最大的索引。

![CLIP 用於圖像分類](../../../../../translated_images/zh-MO/clip-class.3af42ef0b2b19369.webp)

> *圖片來源於[這篇博客](https://openai.com/blog/clip/)*

**基於文本的圖像搜索**

我們也可以反過來操作。如果我們有一組圖像，可以將這組圖像和一個文本提示輸入模型，模型會返回與該提示最相似的圖像。

## ✍️ 範例：[使用 CLIP 進行圖像分類和圖像搜索](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

打開 [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) 筆記本，查看 CLIP 的實際應用。

## 使用 VQGAN+CLIP 進行圖像生成

CLIP 還可以用於從文本提示生成圖像。為此，我們需要一個**生成器模型**，該模型能夠基於某些向量輸入生成圖像。其中一個生成器模型是 [VQGAN](https://compvis.github.io/taming-transformers/)（向量量化生成對抗網絡）。

VQGAN 與普通 [GAN](../../4-ComputerVision/10-GANs/README.md) 的主要區別在於：
* 使用自回歸 Transformer 架構生成一系列具有上下文的視覺部分，這些部分構成了圖像。這些視覺部分由 [CNN](../../4-ComputerVision/07-ConvNets/README.md) 學習。
* 使用子圖像鑑別器來檢測圖像的部分是否為“真實”或“偽造”（與傳統 GAN 的“全有或全無”方法不同）。

可以在 [Taming Transformers](https://compvis.github.io/taming-transformers/) 網站上了解更多關於 VQGAN 的信息。

VQGAN 與傳統 GAN 的一個重要區別是，後者可以從任何輸入向量生成一個體面的圖像，而 VQGAN 可能生成不連貫的圖像。因此，我們需要進一步引導圖像創建過程，這可以通過 CLIP 完成。

![VQGAN+CLIP 架構](../../../../../translated_images/zh-MO/vqgan.5027fe05051dfa31.webp)

為了生成與文本提示相符的圖像，我們從一些隨機編碼向量開始，將其通過 VQGAN 生成圖像。然後使用 CLIP 生成一個損失函數，該函數顯示圖像與文本提示的匹配程度。接下來的目標是最小化這個損失，通過反向傳播調整輸入向量參數。

一個實現 VQGAN+CLIP 的優秀庫是 [Pixray](http://github.com/pixray/pixray)。

![Pixray 生成的圖片](../../../../../translated_images/zh-MO/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d0.webp) |  ![Pixray 生成的圖片](../../../../../translated_images/zh-MO/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a4390.webp) | ![Pixray 生成的圖片](../../../../../translated_images/zh-MO/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683.webp)
----|----|----
根據提示 *一幅年輕男性文學教師手持書本的水彩特寫肖像* 生成的圖片 | 根據提示 *一幅年輕女性計算機科學教師手持電腦的油畫特寫肖像* 生成的圖片 | 根據提示 *一幅年長男性數學教師站在黑板前的油畫特寫肖像* 生成的圖片

> 圖片來自 [Dmitry Soshnikov](http://soshnikov.com) 的 **人工教師** 系列

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E 是一個基於 GPT-3 的模型，專門用於從文本提示生成圖像。該模型擁有 120 億個參數。

與 CLIP 不同，DALL-E 將文本和圖像作為單一的 token 流處理。因此，通過多個提示，可以基於文本生成圖像。

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1 和 DALL-E 2 的主要區別在於，後者能生成更真實的圖像和藝術作品。

以下是使用 DALL-E 生成圖像的示例：
![DALL-E 生成的圖片](../../../../../translated_images/zh-MO/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.png) |  ![DALL-E 生成的圖片](../../../../../translated_images/zh-MO/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.png) | ![DALL-E 生成的圖片](../../../../../translated_images/zh-MO/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.png)
----|----|----
根據提示 *一幅年輕男性文學教師手持書本的水彩特寫肖像* 生成的圖片 | 根據提示 *一幅年輕女性計算機科學教師手持電腦的油畫特寫肖像* 生成的圖片 | 根據提示 *一幅年長男性數學教師站在黑板前的油畫特寫肖像* 生成的圖片

## 參考資料

* VQGAN 論文：[Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP 論文：[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。