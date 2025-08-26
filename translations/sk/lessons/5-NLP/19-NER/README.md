<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-25T22:10:52+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "sk"
}
-->
# Rozpoznávanie pomenovaných entít

Doteraz sme sa väčšinou sústredili na jednu NLP úlohu - klasifikáciu. Existujú však aj iné NLP úlohy, ktoré je možné riešiť pomocou neurónových sietí. Jednou z týchto úloh je **[Rozpoznávanie pomenovaných entít](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), ktoré sa zaoberá identifikáciou konkrétnych entít v texte, ako sú miesta, mená osôb, časové intervaly, chemické vzorce a podobne.

## [Kvíz pred prednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Príklad použitia NER

Predstavte si, že chcete vyvinúť chatbot na spracovanie prirodzeného jazyka, podobný Amazon Alexe alebo Google Asistentovi. Inteligentné chatboty fungujú tak, že *rozumejú*, čo používateľ chce, prostredníctvom klasifikácie textu v zadanej vete. Výsledkom tejto klasifikácie je tzv. **intencia**, ktorá určuje, čo by mal chatbot vykonať.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Obrázok od autora

Používateľ však môže poskytnúť niektoré parametre ako súčasť frázy. Napríklad pri otázke na počasie môže špecifikovať miesto alebo dátum. Chatbot by mal byť schopný rozpoznať tieto entity a vyplniť príslušné parametre pred vykonaním akcie. A práve tu prichádza na rad NER.

> ✅ Ďalším príkladom by mohlo byť [analyzovanie vedeckých lekárskych článkov](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Jednou z hlavných vecí, ktoré potrebujeme hľadať, sú konkrétne lekárske termíny, ako sú choroby a liečivá. Zatiaľ čo malý počet chorôb by sa pravdepodobne dal extrahovať pomocou vyhľadávania podreťazcov, zložitejšie entity, ako sú chemické zlúčeniny a názvy liekov, vyžadujú komplexnejší prístup.

## NER ako klasifikácia tokenov

NER modely sú v podstate **modely na klasifikáciu tokenov**, pretože pre každý vstupný token musíme rozhodnúť, či patrí k nejakej entite, a ak áno, do akej triedy entity.

Zvážte nasledujúci názov článku:

**Regurgitácia trikuspidálnej chlopne** a **toxickosť lítia karbonátu** u novorodenca.

Entity v tomto texte sú:

* Regurgitácia trikuspidálnej chlopne je choroba (`DIS`)
* Lítium karbonát je chemická látka (`CHEM`)
* Toxicita je tiež choroba (`DIS`)

Všimnite si, že jedna entita môže pozostávať z viacerých tokenov. A ako v tomto prípade, musíme rozlíšiť medzi dvoma po sebe idúcimi entitami. Preto je bežné používať dve triedy pre každú entitu - jednu, ktorá špecifikuje prvý token entity (často sa používa predpona `B-` pre **začiatok**), a druhú pre pokračovanie entity (`I-`, pre **vnútorný token**). Triedu `O` používame na označenie všetkých **ostatných** tokenov. Takéto označovanie tokenov sa nazýva [BIO označovanie](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (alebo IOB). Po označení bude náš názov vyzerať takto:

Token | Značka
------|-------
Trikuspidálnej | B-DIS  
chlopne | I-DIS  
regurgitácia | I-DIS  
a | O  
lítium | B-CHEM  
karbonát | I-CHEM  
toxickosť | B-DIS  
u | O  
novorodenca | O  
. | O  

Keďže potrebujeme vytvoriť jednoznačnú korešpondenciu medzi tokenmi a triedami, môžeme trénovať pravostranný **many-to-many** model neurónovej siete podľa tohto obrázku:

![Obrázok zobrazujúci bežné vzory rekurentných neurónových sietí.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.sk.jpg)

> *Obrázok z [tohto blogového príspevku](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) od [Andreja Karpathyho](http://karpathy.github.io/). Modely na klasifikáciu tokenov pre NER zodpovedajú pravostrannému vzoru siete na tomto obrázku.*

## Trénovanie NER modelov

Keďže NER model je v podstate model na klasifikáciu tokenov, môžeme na túto úlohu použiť RNN, s ktorými sme sa už oboznámili. V tomto prípade každý blok rekurentnej siete vráti ID tokenu. Nasledujúci príkladový notebook ukazuje, ako trénovať LSTM na klasifikáciu tokenov.

## ✍️ Príkladové notebooky: NER

Pokračujte v učení pomocou nasledujúceho notebooku:

* [NER s TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Záver

NER model je **model na klasifikáciu tokenov**, čo znamená, že ho možno použiť na vykonávanie klasifikácie tokenov. Ide o veľmi bežnú úlohu v NLP, ktorá pomáha rozpoznávať konkrétne entity v texte vrátane miest, mien, dátumov a ďalších.

## 🚀 Výzva

Dokončite zadanie uvedené nižšie, aby ste vytrénovali model na rozpoznávanie pomenovaných entít pre lekárske termíny, a potom ho vyskúšajte na inom datasete.

## [Kvíz po prednáške](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Prehľad a samoštúdium

Prečítajte si blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) a postupujte podľa sekcie Ďalšie čítanie v tomto článku, aby ste si prehĺbili svoje vedomosti.

## [Zadanie](lab/README.md)

V zadaní pre túto lekciu budete musieť vytrénovať model na rozpoznávanie lekárskych entít. Môžete začať trénovaním LSTM modelu, ako je popísané v tejto lekcii, a pokračovať použitím modelu BERT. Prečítajte si [pokyny](lab/README.md), aby ste získali všetky podrobnosti.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.