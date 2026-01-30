# 使用遷移學習對牛津寵物進行分類

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗作業。

## 任務

想像一下，你需要為一間寵物托兒所開發一個應用程式，用來記錄所有的寵物。這個應用程式的一個很棒的功能就是能夠從照片中自動識別寵物的品種。在這次作業中，我們將使用遷移學習來對 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 寵物數據集中的真實寵物圖片進行分類。

## 數據集

我們將使用原始的 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 寵物數據集，該數據集包含 35 種不同品種的狗和貓。

要下載數據集，請使用以下程式碼片段：

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 開始筆記本

通過打開 [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) 開始這次實驗。

## 重點

遷移學習和預訓練網絡使我們能夠相對輕鬆地解決現實世界中的圖像分類問題。然而，預訓練網絡在處理類似類型的圖像時效果較好，如果我們開始分類非常不同的圖像（例如醫學圖像），結果可能會差得多。

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。