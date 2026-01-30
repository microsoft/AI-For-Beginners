# Klasifikácia domácich miláčikov z Oxfordu pomocou transferového učenia

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

Predstavte si, že potrebujete vyvinúť aplikáciu pre škôlku domácich miláčikov na katalogizáciu všetkých zvierat. Jednou z výnimočných funkcií takejto aplikácie by bolo automatické rozpoznanie plemena z fotografie. V tejto úlohe použijeme transferové učenie na klasifikáciu reálnych fotografií domácich miláčikov z datasetu [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Dataset

Použijeme pôvodný dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), ktorý obsahuje 35 rôznych plemien psov a mačiek.

Na stiahnutie datasetu použite tento kód:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Začiatok notebooku

Začnite laboratórnu úlohu otvorením [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Záver

Transferové učenie a predtrénované siete nám umožňujú pomerne jednoducho riešiť problémy klasifikácie obrazov zo skutočného sveta. Predtrénované siete však fungujú dobre na obrázkoch podobného typu, a ak začneme klasifikovať veľmi odlišné obrázky (napr. medicínske obrázky), pravdepodobne dosiahneme oveľa horšie výsledky.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.