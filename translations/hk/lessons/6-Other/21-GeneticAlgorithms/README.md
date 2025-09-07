<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-24T22:03:59+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "hk"
}
-->
# 遺傳算法

## [課前測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**遺傳算法**（Genetic Algorithms, GA）基於一種**進化式方法**來解決人工智能問題，通過模擬群體進化的方式來尋找給定問題的最佳解。這一方法由 [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) 在1975年提出。

遺傳算法基於以下幾個核心概念：

* 問題的有效解可以用**基因**來表示
* **交叉**（Crossover）允許我們將兩個解結合起來，生成一個新的有效解
* **選擇**（Selection）通過某種**適應度函數**來選擇更優的解
* **突變**（Mutations）被引入以打破優化過程中的穩定性，幫助跳出局部最小值

如果你想實現一個遺傳算法，你需要以下幾步：

* 找到一種方法，用**基因** g∈Γ 來編碼問題的解
* 在基因集合 Γ 上定義**適應度函數** fit: Γ→**R**，函數值越小表示解越優
* 定義**交叉**機制，用於將兩個基因結合生成新的有效解 crossover: Γ<sup>2</sub>→Γ
* 定義**突變**機制 mutate: Γ→Γ

在許多情況下，交叉和突變是相對簡單的算法，用於操作基因作為數字序列或位向量。

遺傳算法的具體實現可能因情況而異，但其整體結構如下：

1. 選擇初始群體 G⊂Γ
2. 隨機選擇本步要執行的操作：交叉或突變
3. **交叉**：
   * 隨機選擇兩個基因 g<sub>1</sub>, g<sub>2</sub> ∈ G
   * 計算交叉結果 g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * 如果 fit(g)<fit(g<sub>1</sub>) 或 fit(g)<fit(g<sub>2</sub>)，則用 g 替換群體中的相應基因
4. **突變** - 隨機選擇一個基因 g∈G，並用 mutate(g) 替換它
5. 從第2步重複，直到適應度函數值足夠小，或達到步數限制

## 常見任務

遺傳算法通常用於解決以下任務：

1. 排程優化
1. 最佳裝箱
1. 最佳切割
1. 加速窮舉搜索

## ✍️ 練習：遺傳算法

在以下筆記本中繼續學習：

前往 [這個筆記本](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) 查看兩個使用遺傳算法的例子：

1. 財寶的公平分配
1. 八皇后問題

## 總結

遺傳算法被用於解決許多問題，包括物流和搜索問題。這一領域的靈感來自於心理學和計算機科學的交叉研究。

## 🚀 挑戰

「遺傳算法易於實現，但其行為難以理解。」[來源](https://wikipedia.org/wiki/Genetic_algorithm) 請進行一些研究，找到一個遺傳算法的實現，例如解數獨問題，並用草圖或流程圖解釋其工作原理。

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## 回顧與自學

觀看 [這段精彩的影片](https://www.youtube.com/watch?v=qv6UVOQ0F44)，了解計算機如何通過使用遺傳算法訓練的神經網絡學習玩《超級瑪利奧》。我們將在[下一節](../22-DeepRL/README.md)中學習更多關於計算機學習玩遊戲的內容。

## [作業：丟番圖方程](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

你的目標是解決所謂的**丟番圖方程**——一種具有整數根的方程。例如，考慮方程 a+2b+3c+4d=30。你需要找到滿足該方程的整數根。

*此作業靈感來自於[這篇文章](https://habr.com/post/128704/)。*

提示：

1. 你可以考慮根的範圍為 [0;30]
1. 作為基因，可以考慮使用根值的列表

使用 [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) 作為起點。

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。