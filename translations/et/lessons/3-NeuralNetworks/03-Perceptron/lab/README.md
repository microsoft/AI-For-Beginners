# Mitmeklassiline klassifikatsioon perceptroniga

Laboriülesanne [AI algajatele õppekavast](https://github.com/microsoft/ai-for-beginners).

## Ülesanne

Kasutades koodi, mille oleme selles tunnis välja töötanud MNIST käsitsi kirjutatud numbrite binaarseks klassifikatsiooniks, looge mitmeklassiline klassifikaator, mis suudaks ära tunda mistahes numbri. Arvutage klassifikatsiooni täpsus treening- ja testandmestikul ning kuvage segadusmaatriks.

## Vihjed

1. Iga numbri jaoks looge binaarse klassifikaatori andmestik "see number vs. kõik teised numbrid"
1. Treenige 10 erinevat perceptronit binaarseks klassifikatsiooniks (üks iga numbri jaoks)
1. Määratlege funktsioon, mis klassifitseerib sisendnumbri

> **Vihje**: Kui kombineerime kõigi 10 perceptroni kaalud üheks maatriksiks, peaksime saama rakendada kõiki 10 perceptronit sisendnumbritele ühe maatriksikorrutusega. Kõige tõenäolisem number saab leitud lihtsalt `argmax` operatsiooni rakendamisega väljundile.

## Algusnotebook

Alustage laborit, avades [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.