# Segmentering av människokroppen

Labuppgift från [AI för nybörjare-kursen](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Inom videoproduktion, till exempel i väderprognoser, behöver vi ofta klippa ut en mänsklig bild från kameran och placera den ovanpå annat material. Detta görs vanligtvis med hjälp av **chroma key**-tekniker, där en person filmas framför en enhetligt färgad bakgrund som sedan tas bort. I denna labb kommer vi att träna en neuralt nätverksmodell för att klippa ut människosilhuetter.

## Datasetet

Vi kommer att använda [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) från Kaggle. Ladda ner datasetet manuellt från Kaggle.

## Startande Notebook

Börja labben genom att öppna [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Slutsats

Segmentering av människokroppen är bara en av de vanliga uppgifterna vi kan utföra med bilder av människor. Andra viktiga uppgifter inkluderar **skelettdetektion** och **posdetektion**. Utforska [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-biblioteket för att se hur dessa uppgifter kan implementeras.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.