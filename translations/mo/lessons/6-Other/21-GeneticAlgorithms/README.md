<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-26T09:54:24+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "mo"
}
-->
# 基因演算法

## [課前測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**基因演算法** (GA) 是基於**演化方法**的人工智慧技術，透過模仿族群演化的方式來尋求特定問題的最佳解。此方法由 [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) 在1975年提出。

基因演算法的核心概念包括：

* 問題的有效解可以用**基因**來表示
* **交叉**允許我們結合兩個解，生成新的有效解
* **選擇**透過某種**適應度函數**來挑選更優的解
* **突變**用於打破局部最小值的限制，促進全域最佳化

若要實現基因演算法，您需要以下步驟：

* 找到一種方法，使用**基因** g∈Γ 來編碼問題的解
* 在基因集合 Γ 上定義**適應度函數** fit: Γ→**R**，函數值越小表示解越好
* 定義**交叉**機制，結合兩個基因以生成新的有效解 crossover: Γ<sup>2</sub>→Γ
* 定義**突變**機制 mutate: Γ→Γ

在許多情況下，交叉和突變是相對簡單的算法，用於操作基因作為數字序列或位元向量。

基因演算法的具體實現可能因案例而異，但其整體結構如下：

1. 選擇初始族群 G⊂Γ
2. 隨機選擇本步驟要執行的操作：交叉或突變
3. **交叉**：
   * 隨機選擇兩個基因 g<sub>1</sub>, g<sub>2</sub> ∈ G
   * 計算交叉結果 g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * 如果 fit(g)<fit(g<sub>1</sub>) 或 fit(g)<fit(g<sub>2</sub>)，則用 g 替換族群中的相應基因
4. **突變** - 隨機選擇基因 g∈G，並用 mutate(g) 替換
5. 重複步驟2，直到適應度函數值足夠小，或達到步驟數限制為止

## 常見任務

基因演算法通常用於解決以下任務：

1. 排程最佳化
1. 最佳化物品打包
1. 最佳化切割
1. 加速窮舉搜索

## ✍️ 練習：基因演算法

繼續學習以下筆記本中的內容：

前往 [此筆記本](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb)，查看基因演算法的兩個應用範例：

1. 公平分配寶藏
1. 八皇后問題

## 結論

基因演算法被廣泛用於解決許多問題，包括物流和搜索問題。這個領域的靈感來自心理學與計算機科學的交叉研究。

## 🚀 挑戰

「基因演算法易於實現，但其行為難以理解。」[來源](https://wikipedia.org/wiki/Genetic_algorithm)  
進行一些研究，找到基因演算法的實現範例，例如解數獨問題，並以草圖或流程圖的形式解釋其工作原理。

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## 回顧與自學

觀看 [這部精彩影片](https://www.youtube.com/watch?v=qv6UVOQ0F44)，了解電腦如何透過基因演算法訓練的神經網路學習玩《超級瑪利歐》。我們將在[下一節](../22-DeepRL/README.md)中深入探討電腦學習玩遊戲的相關內容。

## [作業：丟番圖方程](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

您的目標是解決所謂的**丟番圖方程**——一種具有整數根的方程。例如，考慮方程 a+2b+3c+4d=30，您需要找到滿足此方程的整數根。

*此作業的靈感來自 [這篇文章](https://habr.com/post/128704/)。*

提示：

1. 您可以將根值限制在區間 [0;30]
1. 作為基因，考慮使用根值列表

使用 [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) 作為起點。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。