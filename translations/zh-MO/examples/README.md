# 初學者友善的 AI 範例

歡迎！此目錄包含簡單、獨立的範例，幫助您開始學習 AI 和機器學習。每個範例都設計為適合初學者，並附有詳細的註解和逐步解說。

## 📚 範例概覽

| 範例 | 描述 | 難度 | 先決條件 |
|------|------|------|----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | 您的第一個 AI 程式 - 簡單的模式識別 | ⭐ 初學者 | Python 基礎 |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | 從零開始建立神經網絡 | ⭐⭐ 初學者+ | Python、基礎數學 |
| [Image Classifier](./03-image-classifier.ipynb) | 使用預訓練模型進行圖像分類 | ⭐⭐ 初學者+ | Python、numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | 分析文本情感（正面/負面） | ⭐⭐ 初學者+ | Python |

## 🚀 開始使用

### 先決條件

請確保您已安裝 Python（建議使用 3.8 或更高版本）。安裝所需的套件：

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

或者使用主課程中的 conda 環境：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 執行範例

**對於 Python 腳本 (.py 檔案):**
```bash
python 01-hello-ai-world.py
```

**對於 Jupyter 筆記本 (.ipynb 檔案):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 學習路徑

我們建議按照以下順序進行學習：

1. **從 "Hello AI World" 開始** - 學習模式識別的基礎
2. **建立簡單的神經網絡** - 理解神經網絡的運作方式
3. **嘗試圖像分類器** - 使用真實圖像體驗 AI 的應用
4. **分析文本情感** - 探索自然語言處理

## 💡 初學者提示

- **仔細閱讀程式碼註解** - 它們解釋了每行程式碼的作用
- **多嘗試！** - 嘗試更改數值並觀察結果
- **不用擔心完全理解** - 學習需要時間
- **提出問題** - 使用 [討論板](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 下一步

完成這些範例後，探索完整課程：
- [AI 簡介](../lessons/1-Intro/README.md)
- [神經網絡](../lessons/3-NeuralNetworks/README.md)
- [電腦視覺](../lessons/4-ComputerVision/README.md)
- [自然語言處理](../lessons/5-NLP/README.md)

## 🤝 貢獻

覺得這些範例有幫助嗎？幫助我們改進：
- 回報問題或提出改進建議
- 添加更多適合初學者的範例
- 改善文件和註解

---

*記住：每位專家都曾是初學者。祝您學習愉快！ 🎓*

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。