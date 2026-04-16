# Segmentacja Ciała Ludzkiego

Zadanie laboratoryjne z [Kursu AI dla Początkujących](https://github.com/microsoft/ai-for-beginners).

## Zadanie

W produkcji wideo, na przykład w prognozach pogody, często musimy wyciąć obraz człowieka z kamery i umieścić go na innym materiale filmowym. Zazwyczaj odbywa się to za pomocą technik **chroma key**, gdzie człowiek jest filmowany na tle jednolitego koloru, który następnie jest usuwany. W tym laboratorium wytrenujemy model sieci neuronowej, aby wyciąć sylwetkę człowieka.

## Zbiór Danych

Będziemy korzystać z [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) z Kaggle. Pobierz zbiór danych ręcznie z Kaggle.

## Notatnik Startowy

Rozpocznij laboratorium, otwierając [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Wnioski

Segmentacja ciała to tylko jedno z powszechnych zadań, które możemy wykonywać z obrazami ludzi. Inne ważne zadania to **detekcja szkieletu** i **detekcja pozycji**. Sprawdź bibliotekę [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), aby zobaczyć, jak można zaimplementować te zadania.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.