<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T10:39:30+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "mo"
}
-->
# 使用感知器進行多類別分類

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗作業。

## 任務

使用我們在本課程中開發的 MNIST 手寫數字二元分類程式碼，建立一個多類別分類器，能夠辨識任意數字。計算訓練集和測試集的分類準確率，並列印混淆矩陣。

## 提示

1. 對於每個數字，建立一個二元分類器的資料集，將「該數字」與「所有其他數字」進行分類。
1. 訓練 10 個不同的感知器進行二元分類（每個數字一個感知器）。
1. 定義一個函數，用於分類輸入的數字。

> **提示**：如果我們將所有 10 個感知器的權重合併成一個矩陣，我們應該能夠透過一次矩陣乘法將所有 10 個感知器應用於輸入數字。最可能的數字可以透過對輸出進行 `argmax` 操作來找到。

## 起始筆記本

開啟 [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) 開始實驗。

**免責聲明**：  
本文檔已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。