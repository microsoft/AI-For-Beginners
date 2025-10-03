<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-26T09:33:44+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "mo"
}
-->
# 寵物臉部分類

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗作業。

## 任務

想像一下，你需要為寵物托育中心開發一個應用程式，用來記錄所有的寵物。這樣的應用程式其中一個很棒的功能就是能夠自動從照片中辨識寵物的品種。這可以透過神經網路成功實現。

你需要訓練一個卷積神經網路，使用 **Pet Faces** 資料集來分類不同品種的貓和狗。

## 資料集

我們將使用 **Pet Faces** 資料集，這是從 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 寵物資料集中衍生出來的。該資料集包含 35 種不同品種的狗和貓。

![我們將處理的資料集](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.mo.png)

要下載資料集，請使用以下程式碼片段：

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 開始使用 Notebook

通過打開 [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) 開始這次實驗。

## 收穫

你已經從零開始解決了一個相對複雜的影像分類問題！雖然有相當多的分類，但你仍然能夠獲得合理的準確率！此外，測量 top-k 準確率也是有意義的，因為有些分類即使對人類來說也不容易區分清楚。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。