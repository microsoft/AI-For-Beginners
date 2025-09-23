<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T21:53:11+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "tw"
}
-->
> 圖片來源：[Dmitry Soshnikov](http://soshnikov.com)

隨著時間的推移，計算資源變得更加便宜，並且可用的數據量也越來越多，因此神經網絡方法開始在許多領域中展現出與人類競爭的卓越性能，例如計算機視覺或語音理解。在過去的十年中，「人工智慧」這個詞大多被用作「神經網絡」的同義詞，因為我們聽到的大多數人工智慧的成功案例都基於神經網絡。

我們可以觀察到這些方法的演變，例如在開發一個下棋的電腦程式時：

* 早期的棋類程式基於搜索——程式會明確地嘗試估算對手在接下來幾步中的可能走法，並根據幾步內可以達到的最佳位置選擇最佳走法。這導致了所謂的 [alpha-beta 剪枝](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) 搜索算法的發展。
* 搜索策略在遊戲後期效果很好，因為搜索空間因可能走法的數量有限而受到限制。然而，在遊戲開始時，搜索空間非常龐大，算法可以通過從人類玩家的現有對局中學習來改進。隨後的實驗採用了所謂的 [案例推理](https://en.wikipedia.org/wiki/Case-based_reasoning)，程式會在知識庫中尋找與當前棋局非常相似的案例。
* 現代能夠擊敗人類玩家的程式基於神經網絡和 [強化學習](https://en.wikipedia.org/wiki/Reinforcement_learning)，這些程式僅通過長時間與自己對弈並從自己的錯誤中學習來學會下棋——就像人類學習下棋的方式一樣。然而，電腦程式可以在更短的時間內進行更多的對局，因此可以更快地學習。

✅ 研究一下其他由人工智慧參與的遊戲。

同樣，我們也可以看到「對話程式」（可能通過圖靈測試）的開發方法如何演變：

* 早期的此類程式，例如 [Eliza](https://en.wikipedia.org/wiki/ELIZA)，基於非常簡單的語法規則以及將輸入句子重新表述為問題。
* 現代的助手，例如 Cortana、Siri 或 Google Assistant，都是混合系統，使用神經網絡將語音轉換為文字並識別使用者的意圖，然後採用一些推理或明確的算法來執行所需的操作。
* 未來，我們可能期待一個完全基於神經網絡的模型能夠自行處理對話。最近的 GPT 和 [Turing-NLG](https://turing.microsoft.com/) 系列神經網絡在這方面展現了巨大的成功。

> 圖片由 Dmitry Soshnikov 提供，[照片](https://unsplash.com/photos/r8LmVbUKgns) 由 [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto) 提供，Unsplash

## 最近的人工智慧研究

神經網路研究的巨大增長始於 2010 年左右，當時大型公共數據集開始變得可用。一個名為 [ImageNet](https://en.wikipedia.org/wiki/ImageNet) 的龐大圖像集合包含約 1400 萬張註解圖像，催生了 [ImageNet 大規模視覺識別挑戰賽](https://image-net.org/challenges/LSVRC/)。

![ILSVRC 準確率](../../../../lessons/1-Intro/images/ilsvrc.gif)

> 圖片由 [Dmitry Soshnikov](http://soshnikov.com) 提供

2012 年，[卷積神經網路](../4-ComputerVision/07-ConvNets/README.md) 首次被用於圖像分類，導致分類錯誤率顯著下降（從接近 30% 降至 16.4%）。2015 年，微軟研究院的 ResNet 架構[達到人類級別的準確率](https://doi.org/10.1109/ICCV.2015.123)。

自此之後，神經網路在許多任務中展現了非常成功的表現：

---

年份 | 達到人類水平
-----|--------
2015 | [圖像分類](https://doi.org/10.1109/ICCV.2015.123)
2016 | [對話式語音識別](https://arxiv.org/abs/1610.05256)
2018 | [自動機器翻譯](https://arxiv.org/abs/1803.05567)（中英翻譯）
2020 | [圖像標註](https://arxiv.org/abs/2009.13682)

在過去幾年中，我們見證了大型語言模型的巨大成功，例如 BERT 和 GPT-3。這主要是因為有大量的通用文本數據可用，這使得我們能夠訓練模型以捕捉文本的結構和意義，先在通用文本集合上進行預訓練，然後再使這些模型專注於更具體的任務。我們將在本課程稍後學習更多關於[自然語言處理](../5-NLP/README.md)的內容。

## 🚀 挑戰

在網路上進行探索，判斷您認為人工智慧在哪些領域最有效地被使用。是地圖應用程式、語音轉文字服務還是某款電子遊戲？研究該系統是如何構建的。

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## 回顧與自學

通過閱讀[這節課](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML)來回顧人工智慧和機器學習的歷史。從該課程頂部的手繪筆記或本課程中選擇一個元素，深入研究以了解其演變的文化背景。

**作業**: [遊戲開發挑戰](assignment.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。