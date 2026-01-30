# Segmentácia ľudského tela

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

Pri produkcii videa, napríklad v predpovediach počasia, často potrebujeme vystrihnúť obraz človeka z kamery a umiestniť ho na iné zábery. To sa zvyčajne robí pomocou techník **chroma key**, keď je človek natočený pred jednotným farebným pozadím, ktoré sa následne odstráni. V tejto úlohe budeme trénovať model neurónovej siete na vystrihnutie siluety človeka.

## Dataset

Použijeme [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) z Kaggle. Dataset si manuálne stiahnite z Kaggle.

## Začiatočný notebook

Začnite úlohu otvorením [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Záver

Segmentácia tela je len jednou z bežných úloh, ktoré môžeme vykonávať s obrázkami ľudí. Medzi ďalšie dôležité úlohy patrí **detekcia kostry** a **detekcia póz**. Pozrite si knižnicu [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), aby ste zistili, ako sa dajú tieto úlohy implementovať.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.