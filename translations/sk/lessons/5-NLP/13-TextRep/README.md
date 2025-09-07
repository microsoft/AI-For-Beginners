<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-25T21:50:01+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "sk"
}
-->
# Reprezentácia textu ako tenzorov

## [Kvíz pred prednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Klasifikácia textu

V prvej časti tejto sekcie sa zameriame na úlohu **klasifikácie textu**. Použijeme dataset [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), ktorý obsahuje spravodajské články, ako napríklad:

* Kategória: Veda/Technológie  
* Názov: Ky. spoločnosť získala grant na štúdium peptidov (AP)  
* Text: AP - Spoločnosť založená chemickým výskumníkom na Univerzite v Louisville získala grant na vývoj...

Naším cieľom bude klasifikovať spravodajský článok do jednej z kategórií na základe textu.

## Reprezentácia textu

Ak chceme riešiť úlohy spracovania prirodzeného jazyka (NLP) pomocou neurónových sietí, potrebujeme spôsob, ako reprezentovať text ako tenzory. Počítače už reprezentujú textové znaky ako čísla, ktoré mapujú na fonty na vašej obrazovke pomocou kódovaní, ako sú ASCII alebo UTF-8.

<img alt="Obrázok zobrazujúci diagram mapujúci znak na ASCII a binárnu reprezentáciu" src="images/ascii-character-map.png" width="50%"/>

> [Zdroj obrázku](https://www.seobility.net/en/wiki/ASCII)

Ako ľudia rozumieme, čo každý znak **reprezentuje**, a ako všetky znaky spolu tvoria slová vo vete. Počítače však samy o sebe takémuto významu nerozumejú, a neurónová sieť sa musí tento význam naučiť počas tréningu.

Preto môžeme použiť rôzne prístupy na reprezentáciu textu:

* **Reprezentácia na úrovni znakov**, kde reprezentujeme text tak, že každý znak považujeme za číslo. Ak máme *C* rôznych znakov v našom textovom korpuse, slovo *Hello* by bolo reprezentované ako tenzor veľkosti 5x*C*. Každé písmeno by zodpovedalo stĺpcu tenzora v one-hot kódovaní.  
* **Reprezentácia na úrovni slov**, kde vytvoríme **slovník** všetkých slov v našom texte a potom slová reprezentujeme pomocou one-hot kódovania. Tento prístup je o niečo lepší, pretože jednotlivé písmená samy o sebe nemajú veľký význam, a tak použitím vyšších sémantických konceptov - slov - zjednodušujeme úlohu pre neurónovú sieť. Avšak vzhľadom na veľkosť slovníka musíme pracovať s vysoko dimenzionálnymi riedkymi tenzormi.

Bez ohľadu na spôsob reprezentácie musíme najprv text previesť na sekvenciu **tokenov**, pričom jeden token môže byť znak, slovo alebo niekedy aj časť slova. Potom token prevedieme na číslo, zvyčajne pomocou **slovníka**, a toto číslo môžeme vložiť do neurónovej siete pomocou one-hot kódovania.

## N-Gramy

V prirodzenom jazyku je presný význam slov určený iba v kontexte. Napríklad významy *neurónová sieť* a *rybárska sieť* sú úplne odlišné. Jedným zo spôsobov, ako to zohľadniť, je vytvoriť model na základe dvojíc slov a považovať dvojice slov za samostatné tokeny slovníka. Týmto spôsobom bude veta *Rád chodím na ryby* reprezentovaná nasledujúcou sekvenciou tokenov: *Rád chodím*, *chodím na*, *na ryby*. Problémom tohto prístupu je, že veľkosť slovníka sa výrazne zväčšuje a kombinácie ako *na ryby* a *na nákupy* sú reprezentované rôznymi tokenmi, ktoré nezdieľajú žiadnu sémantickú podobnosť napriek rovnakému slovesu.

V niektorých prípadoch môžeme zvážiť použitie tri-gramov – kombinácií troch slov. Tento prístup sa preto často nazýva **n-gramy**. Tiež má zmysel používať n-gramy s reprezentáciou na úrovni znakov, v takom prípade n-gramy približne zodpovedajú rôznym slabikám.

## Bag-of-Words a TF/IDF

Pri riešení úloh, ako je klasifikácia textu, potrebujeme byť schopní reprezentovať text jedným vektorom pevnej veľkosti, ktorý použijeme ako vstup do konečného hustého klasifikátora. Jedným z najjednoduchších spôsobov, ako to dosiahnuť, je kombinovať všetky individuálne reprezentácie slov, napr. ich sčítaním. Ak sčítame one-hot kódovania každého slova, skončíme s vektorom frekvencií, ktorý ukazuje, koľkokrát sa každé slovo v texte objavilo. Takáto reprezentácia textu sa nazýva **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Obrázok od autora

BoW v podstate reprezentuje, ktoré slová sa v texte objavujú a v akých množstvách, čo môže byť dobrým indikátorom toho, o čom text je. Napríklad spravodajský článok o politike pravdepodobne obsahuje slová ako *prezident* a *krajina*, zatiaľ čo vedecká publikácia by mohla obsahovať slová ako *urýchľovač*, *objavený* atď. Frekvencie slov môžu teda v mnohých prípadoch byť dobrým indikátorom obsahu textu.

Problémom BoW je, že určité bežné slová, ako *a*, *je* atď., sa objavujú vo väčšine textov a majú najvyššie frekvencie, čím zakrývajú slová, ktoré sú skutočne dôležité. Môžeme znížiť dôležitosť týchto slov tým, že zohľadníme frekvenciu, s akou sa slová vyskytujú v celej kolekcii dokumentov. Toto je hlavná myšlienka prístupu TF/IDF, ktorý je podrobnejšie vysvetlený v poznámkových blokoch pripojených k tejto lekcii.

Žiadny z týchto prístupov však nedokáže plne zohľadniť **sémantiku** textu. Na to potrebujeme výkonnejšie modely neurónových sietí, o ktorých budeme diskutovať neskôr v tejto sekcii.

## ✍️ Cvičenia: Reprezentácia textu

Pokračujte vo svojom učení v nasledujúcich poznámkových blokoch:

* [Reprezentácia textu s PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Reprezentácia textu s TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)  

## Záver

Doteraz sme študovali techniky, ktoré môžu pridať váhu frekvencie rôznym slovám. Nedokážu však reprezentovať význam alebo poradie. Ako povedal slávny lingvista J. R. Firth v roku 1935: "Úplný význam slova je vždy kontextuálny a žiadna štúdia významu mimo kontextu nemôže byť braná vážne." Neskôr v kurze sa naučíme, ako zachytiť kontextové informácie z textu pomocou jazykového modelovania.

## 🚀 Výzva

Vyskúšajte ďalšie cvičenia s bag-of-words a rôznymi dátovými modelmi. Môžete sa inšpirovať touto [súťažou na Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Kvíz po prednáške](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Prehľad a samostatné štúdium

Precvičte si svoje zručnosti s textovými embeddingmi a technikami bag-of-words na [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Úloha: Poznámkové bloky](assignment.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.