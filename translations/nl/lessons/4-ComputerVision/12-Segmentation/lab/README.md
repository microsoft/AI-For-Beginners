<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "365f0decfe0f47b460bbde8227c5009d",
  "translation_date": "2025-08-28T19:36:35+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/lab/README.md",
  "language_code": "nl"
}
-->
# Segmentatie van het Menselijk Lichaam

Praktijkopdracht uit [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Taak

Bij videoproductie, zoals bij weersvoorspellingen, moeten we vaak een menselijk beeld uit de camera knippen en dit bovenop andere beelden plaatsen. Dit wordt meestal gedaan met behulp van **chroma key**-technieken, waarbij een persoon wordt gefilmd tegen een achtergrond met een uniforme kleur, die vervolgens wordt verwijderd. In deze opdracht gaan we een neuraal netwerkmodel trainen om de menselijke silhouet uit te snijden.

## De Dataset

We maken gebruik van [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) van Kaggle. Download de dataset handmatig van Kaggle.

## Start Notebook

Begin de opdracht door [BodySegmentation.ipynb](BodySegmentation.ipynb) te openen.

## Belangrijkste Leerpunten

Lichaamssegmentatie is slechts een van de veelvoorkomende taken die we kunnen uitvoeren met afbeeldingen van mensen. Andere belangrijke taken zijn **skeletdetectie** en **houdingdetectie**. Bekijk de [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) bibliotheek om te zien hoe deze taken kunnen worden geïmplementeerd.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.