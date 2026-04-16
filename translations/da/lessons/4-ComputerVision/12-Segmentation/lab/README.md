# Segmentering af menneskekroppen

Laboratorieopgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

I videoproduktion, for eksempel i vejrudsigter, har vi ofte brug for at klippe et menneskebillede ud fra kameraet og placere det oven på andet materiale. Dette gøres typisk ved hjælp af **chroma key**-teknikker, hvor en person filmes foran en ensfarvet baggrund, som derefter fjernes. I denne opgave vil vi træne en neuralt netværksmodel til at klippe menneskesilhuetten ud.

## Datasættet

Vi vil bruge [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) fra Kaggle. Download datasættet manuelt fra Kaggle.

## Startnotebook

Start laboratorieopgaven ved at åbne [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Læringspunkt

Segmentering af kroppen er blot en af de almindelige opgaver, vi kan udføre med billeder af mennesker. Andre vigtige opgaver inkluderer **skeletdetektion** og **posedetektion**. Undersøg [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-biblioteket for at se, hvordan disse opgaver kan implementeres.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.