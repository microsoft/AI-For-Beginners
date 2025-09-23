<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-26T08:08:15+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "mo"
}
-->
# 循環神經網路

## [課前測驗](https://ff-quizzes.netlify.app/en/ai/quiz/31)

在之前的章節中，我們使用了豐富的文本語義表示以及嵌入層之上的簡單線性分類器。這種架構的作用是捕捉句子中單詞的整體意義，但它並未考慮單詞的**順序**，因為嵌入層上的聚合操作移除了原始文本中的這種信息。由於這些模型無法建模單詞的順序，因此無法解決更複雜或更具歧義的任務，例如文本生成或問題回答。

為了捕捉文本序列的意義，我們需要使用另一種神經網路架構，稱為**循環神經網路**（Recurrent Neural Network，簡稱 RNN）。在 RNN 中，我們將句子逐個符號地傳遞給網路，網路會生成某種**狀態**，然後將該狀態與下一個符號一起再次傳遞給網路。

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.mo.png)

> 圖片由作者提供

給定輸入的符號序列 X<sub>0</sub>,...,X<sub>n</sub>，RNN 會創建一系列神經網路模塊，並通過反向傳播對這個序列進行端到端的訓練。每個網路模塊接受一對輸入 (X<sub>i</sub>,S<sub>i</sub>)，並生成 S<sub>i+1</sub> 作為結果。最終的狀態 S<sub>n</sub> 或輸出 Y<sub>n</sub> 會進入線性分類器以生成結果。所有的網路模塊共享相同的權重，並通過一次反向傳播進行端到端訓練。

由於狀態向量 S<sub>0</sub>,...,S<sub>n</sub> 在網路中傳遞，RNN 能夠學習單詞之間的順序依賴性。例如，當單詞 *not* 出現在序列中的某處時，網路可以學會在狀態向量中否定某些元素，從而實現否定的效果。

> ✅ 由於上圖中所有 RNN 模塊的權重是共享的，因此可以將該圖表示為一個具有循環反饋迴路的單一模塊（如右圖所示），該迴路將網路的輸出狀態傳回輸入。

## RNN 單元的結構

讓我們來看看一個簡單的 RNN 單元是如何組織的。它接受前一個狀態 S<sub>i-1</sub> 和當前符號 X<sub>i</sub> 作為輸入，並生成輸出狀態 S<sub>i</sub>（有時我們也對其他輸出 Y<sub>i</sub> 感興趣，例如在生成式網路的情況下）。

一個簡單的 RNN 單元內部有兩個權重矩陣：一個用於轉換輸入符號（我們稱之為 W），另一個用於轉換輸入狀態（H）。在這種情況下，網路的輸出計算公式為 σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b)，其中 σ 是激活函數，b 是額外的偏置。

<img alt="RNN 單元結構" src="images/rnn-anatomy.png" width="50%"/>

> 圖片由作者提供

在許多情況下，輸入符號會在進入 RNN 之前通過嵌入層以降低維度。在這種情況下，如果輸入向量的維度為 *emb_size*，狀態向量的維度為 *hid_size*，則 W 的大小為 *emb_size*×*hid_size*，H 的大小為 *hid_size*×*hid_size*。

## 長短期記憶網路（LSTM）

經典 RNN 的主要問題之一是所謂的**梯度消失**問題。由於 RNN 是通過一次反向傳播進行端到端訓練的，因此很難將誤差傳遞到網路的前幾層，從而無法學習遠距離符號之間的關係。解決這個問題的一種方法是通過使用所謂的**門控機制**來引入**顯式的狀態管理**。有兩種著名的架構：**長短期記憶網路**（Long Short Term Memory，簡稱 LSTM）和**門控循環單元**（Gated Relay Unit，簡稱 GRU）。

![顯示長短期記憶單元的示例圖片](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> 圖片來源待定

LSTM 網路的組織方式與 RNN 類似，但有兩個狀態在層與層之間傳遞：實際狀態 C 和隱藏向量 H。在每個單元中，隱藏向量 H<sub>i</sub> 與輸入 X<sub>i</sub> 連接在一起，並通過**門控機制**控制狀態 C 的變化。每個門控機制都是一個帶有 sigmoid 激活函數（輸出範圍為 [0,1]）的神經網路，可以被視為在與狀態向量相乘時的位掩碼。以下是這些門控機制（從左到右對應上圖）：

* **遺忘門**：接收隱藏向量，決定狀態向量 C 的哪些部分需要遺忘，哪些需要保留。
* **輸入門**：從輸入和隱藏向量中提取一些信息，並插入到狀態中。
* **輸出門**：通過帶有 *tanh* 激活函數的線性層轉換狀態，然後使用隱藏向量 H<sub>i</sub> 選擇其部分組件以生成新狀態 C<sub>i+1</sub>。

狀態 C 的組件可以被視為某些標誌，可以開啟或關閉。例如，當我們在序列中遇到名字 *Alice* 時，我們可能會假設它指的是一個女性角色，並在狀態中設置一個標誌，表示句子中有一個女性名詞。當我們進一步遇到短語 *and Tom* 時，我們會設置一個標誌，表示句子中有一個複數名詞。因此，通過操作狀態，我們可以追蹤句子部分的語法屬性。

> ✅ 理解 LSTM 內部結構的一個極佳資源是 Christopher Olah 的這篇精彩文章 [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)。

## 雙向與多層 RNN

我們已經討論了單向運行的循環網路，從序列的開始到結束。這看起來很自然，因為它類似於我們閱讀和聽取語音的方式。然而，在許多實際情況下，我們可以隨機訪問輸入序列，因此在兩個方向上運行循環計算可能更有意義。這樣的網路稱為**雙向 RNN**。在處理雙向網路時，我們需要兩個隱藏狀態向量，每個方向一個。

無論是單向還是雙向的循環網路，都能捕捉序列中的某些模式，並將其存儲到狀態向量中或傳遞到輸出中。與卷積網路類似，我們可以在第一層之上構建另一個循環層，以捕捉更高層次的模式，並基於第一層提取的低層次模式進行構建。這引出了**多層 RNN** 的概念，它由兩層或更多的循環網路組成，其中前一層的輸出作為下一層的輸入。

![顯示多層長短期記憶 RNN 的圖片](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.mo.jpg)

*圖片來自 Fernando López 的[這篇精彩文章](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3)*

## ✍️ 練習：嵌入

通過以下筆記本繼續學習：

* [使用 PyTorch 的 RNN](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [使用 TensorFlow 的 RNN](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## 總結

在本單元中，我們了解到 RNN 可用於序列分類，但事實上，它們還可以處理許多其他任務，例如文本生成、機器翻譯等。我們將在下一單元中探討這些任務。

## 🚀 挑戰

閱讀一些關於 LSTM 的文獻並考慮其應用：

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## 回顧與自學

- Christopher Olah 的 [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)。

## [作業：筆記本](assignment.md)

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。