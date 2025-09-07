<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "365f0decfe0f47b460bbde8227c5009d",
  "translation_date": "2025-08-25T22:37:42+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/lab/README.md",
  "language_code": "sl"
}
-->
# Segmentacija človeškega telesa

Laboratorijska naloga iz [Učnega načrta za začetnike v AI](https://github.com/microsoft/ai-for-beginners).

## Naloga

Pri video produkciji, na primer pri vremenskih napovedih, pogosto potrebujemo izrezati podobo človeka iz posnetka kamere in jo postaviti na drugo ozadje. To se običajno izvaja z uporabo tehnik **chroma key**, kjer je oseba posneta pred enobarvnim ozadjem, ki se nato odstrani. V tej nalogi bomo trenirali nevronsko mrežo za izrez silhuete človeka.

## Podatkovni niz

Uporabljali bomo [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) s Kaggle. Podatkovni niz prenesite ročno s Kaggle.

## Začetni zvezek

Začnite laboratorijsko nalogo z odpiranjem [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Ključne točke

Segmentacija telesa je le ena izmed pogostih nalog, ki jih lahko izvedemo s slikami ljudi. Druge pomembne naloge vključujejo **zaznavanje okostja** in **zaznavanje drže**. Oglejte si knjižnico [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), da vidite, kako se te naloge lahko implementirajo.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.