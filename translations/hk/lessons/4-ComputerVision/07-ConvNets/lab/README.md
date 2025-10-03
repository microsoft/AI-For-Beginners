<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T22:00:15+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "hk"
}
-->
# 寵物面孔分類

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗課題。

## 任務

假設你需要開發一個寵物托管應用程式，用來記錄所有的寵物。這個應用程式的一個重要功能是能夠根據照片自動辨識寵物的品種。這可以通過神經網絡成功實現。

你需要訓練一個卷積神經網絡，使用 **Pet Faces** 數據集來分類不同品種的貓和狗。

## 數據集

我們將使用 **Pet Faces** 數據集，該數據集源自 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 寵物數據集。它包含 35 種不同品種的狗和貓。

![我們將處理的數據集](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.hk.png)

要下載數據集，請使用以下代碼片段：

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 啟動筆記本

通過打開 [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) 開始實驗。

## 收穫

你已經成功解決了一個相對複雜的圖像分類問題！儘管有很多類別，你仍然能夠獲得合理的準確率！此外，測量 top-k 準確率也是有意義的，因為有些類別即使對人類來說也不容易區分。

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。