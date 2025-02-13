# Segmentering av den mänskliga kroppen

Laborationsuppgift från [AI för nybörjare-kursen](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Vid videoproduktion, till exempel i väderprognoser, behöver vi ofta klippa ut en mänsklig bild från kameran och placera den ovanpå annat material. Detta görs vanligtvis med hjälp av **chroma key**-tekniker, där en människa filmas framför en enhetlig färgbakgrund som sedan tas bort. I denna laboration kommer vi att träna en neuralt nätverksmodell för att klippa ut människans silhuett.

## Datasetet

Vi kommer att använda [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) från Kaggle. Ladda ner datasetet manuellt från Kaggle.

## Starta anteckningsboken

Börja laborationen genom att öppna [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Sammanfattning

Segmentering av kroppen är bara en av de vanliga uppgifterna som vi kan utföra med bilder på människor. Andra viktiga uppgifter inkluderar **skelettdetektering** och **ställningsdetektering**. Kolla in [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) biblioteket för att se hur dessa uppgifter kan implementeras.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller felaktiga tolkningar som kan uppstå genom användning av denna översättning.