# 人體分割

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗作業。

## 任務

在視頻製作中，例如天氣預報，我們經常需要將攝像機中的人像剪裁出來，並將其放置在其他畫面上。這通常是通過 **色度鍵** 技術來完成的，當人站在一個統一顏色的背景前拍攝時，該背景會被移除。在這個實驗中，我們將訓練一個神經網絡模型來剪裁出人像輪廓。

## 數據集

我們將使用來自 Kaggle 的 [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)。請從 Kaggle 手動下載該數據集。

## 起始筆記本

通過打開 [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) 開始這個實驗。

## 收穫

人體分割只是我們可以對人物圖像進行的常見任務之一。其他重要的任務還包括 **骨架檢測** 和 **姿勢檢測**。可以查看 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 庫，了解如何實現這些任務。

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。如涉及關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。