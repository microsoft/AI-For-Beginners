<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-25T21:49:38+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "cs"
}
-->
# Reprezentace textu jako tenzorů

## [Kvíz před přednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Klasifikace textu

V první části této sekce se zaměříme na úkol **klasifikace textu**. Použijeme dataset [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), který obsahuje zpravodajské články, například:

* Kategorie: Věda/Technika  
* Titulek: Ky. společnost získala grant na studium peptidů (AP)  
* Text: AP - Společnost založená výzkumníkem chemie na Univerzitě v Louisville získala grant na vývoj...

Naším cílem bude klasifikovat zpravodajský článek do jedné z kategorií na základě textu.

## Reprezentace textu

Pokud chceme řešit úkoly z oblasti zpracování přirozeného jazyka (NLP) pomocí neuronových sítí, potřebujeme způsob, jak reprezentovat text jako tenzory. Počítače již reprezentují textové znaky jako čísla, která mapují na fonty na obrazovce, pomocí kódování, jako je ASCII nebo UTF-8.

<img alt="Obrázek zobrazující diagram mapující znak na ASCII a binární reprezentaci" src="images/ascii-character-map.png" width="50%"/>

> [Zdroj obrázku](https://www.seobility.net/en/wiki/ASCII)

Jako lidé rozumíme, co každý znak **znamená**, a jak všechny znaky dohromady tvoří slova ve větě. Počítače však samy o sobě takové porozumění nemají a neuronová síť se musí význam naučit během trénování.

Proto můžeme použít různé přístupy při reprezentaci textu:

* **Reprezentace na úrovni znaků**, kdy reprezentujeme text tak, že každý znak považujeme za číslo. Pokud máme *C* různých znaků v našem textovém korpusu, slovo *Hello* by bylo reprezentováno jako tenzor o rozměrech 5x*C*. Každé písmeno by odpovídalo sloupci tenzoru v one-hot kódování.  
* **Reprezentace na úrovni slov**, kdy vytvoříme **slovník** všech slov v našem textu a poté reprezentujeme slova pomocí one-hot kódování. Tento přístup je o něco lepší, protože jednotlivá písmena sama o sobě nemají velký význam, a použitím vyšších sémantických konceptů - slov - úkol pro neuronovou síť zjednodušíme. Nicméně, vzhledem k velké velikosti slovníku musíme pracovat s vysoce dimenzionálními řídkými tenzory.

Bez ohledu na zvolenou reprezentaci musíme nejprve převést text na sekvenci **tokenů**, přičemž token může být znak, slovo nebo někdy i část slova. Poté token převedeme na číslo, obvykle pomocí **slovníku**, a toto číslo lze do neuronové sítě předat pomocí one-hot kódování.

## N-Gramy

V přirozeném jazyce lze přesný význam slov určit pouze v kontextu. Například významy *neuronová síť* a *rybářská síť* jsou zcela odlišné. Jedním ze způsobů, jak toto zohlednit, je vytvořit model založený na dvojicích slov a považovat dvojice slov za samostatné tokeny slovníku. Tímto způsobem bude věta *Rád chodím na ryby* reprezentována následující sekvencí tokenů: *Rád chodím*, *chodím na*, *na ryby*. Problémem tohoto přístupu je, že velikost slovníku výrazně narůstá a kombinace jako *na ryby* a *na nákupy* jsou reprezentovány různými tokeny, které nesdílejí žádnou sémantickou podobnost, přestože obsahují stejné sloveso.

V některých případech můžeme zvážit použití tri-gramů – kombinací tří slov. Tento přístup se proto často nazývá **n-gramy**. Dává také smysl používat n-gramy s reprezentací na úrovni znaků, kdy n-gramy přibližně odpovídají různým slabikám.

## Bag-of-Words a TF/IDF

Při řešení úkolů, jako je klasifikace textu, potřebujeme být schopni reprezentovat text jako jeden vektor pevné velikosti, který použijeme jako vstup pro konečný hustý klasifikátor. Jedním z nejjednodušších způsobů, jak to udělat, je kombinovat všechny jednotlivé reprezentace slov, například jejich sečtením. Pokud sečteme one-hot kódování každého slova, získáme vektor frekvencí, který ukazuje, kolikrát se každé slovo v textu objevuje. Taková reprezentace textu se nazývá **bag-of-words** (BoW).

<img src="images/bow.png" width="90%"/>

> Obrázek od autora

BoW v podstatě reprezentuje, která slova se v textu objevují a v jakém množství, což může být dobrým ukazatelem toho, o čem text je. Například zpravodajský článek o politice pravděpodobně obsahuje slova jako *prezident* a *země*, zatímco vědecká publikace by mohla obsahovat slova jako *urychlovač*, *objeveno* atd. Frekvence slov tedy v mnoha případech mohou být dobrým indikátorem obsahu textu.

Problémem BoW je, že určitá běžná slova, jako *a*, *je* atd., se objevují ve většině textů a mají nejvyšší frekvence, čímž zastírají slova, která jsou skutečně důležitá. Můžeme snížit důležitost těchto slov tím, že vezmeme v úvahu frekvenci, s jakou se slova objevují v celé kolekci dokumentů. To je hlavní myšlenka přístupu TF/IDF, který je podrobněji popsán v přiložených poznámkových blocích k této lekci.

Nicméně žádný z těchto přístupů nedokáže plně zohlednit **sémantiku** textu. K tomu potřebujeme výkonnější modely neuronových sítí, o kterých budeme diskutovat později v této sekci.

## ✍️ Cvičení: Reprezentace textu

Pokračujte ve svém učení v následujících poznámkových blocích:

* [Reprezentace textu s PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Reprezentace textu s TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Závěr

Doposud jsme studovali techniky, které mohou přidat váhu frekvencím různých slov. Tyto techniky však nejsou schopny reprezentovat význam nebo pořadí. Jak slavný lingvista J. R. Firth řekl v roce 1935: "Úplný význam slova je vždy kontextový a žádná studie významu oddělená od kontextu nemůže být brána vážně." Později v kurzu se naučíme, jak zachytit kontextové informace z textu pomocí jazykového modelování.

## 🚀 Výzva

Vyzkoušejte další cvičení s použitím bag-of-words a různých datových modelů. Můžete se inspirovat touto [soutěží na Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Kvíz po přednášce](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Přehled a samostudium

Procvičte si své dovednosti s technikami vkládání textu a bag-of-words na [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Úkol: Poznámkové bloky](assignment.md)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.