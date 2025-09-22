<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-25T22:10:29+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "cs"
}
-->
# Rozpoznávání pojmenovaných entit

Doposud jsme se většinou soustředili na jeden úkol NLP - klasifikaci. Existují však i další úkoly NLP, které lze řešit pomocí neuronových sítí. Jedním z těchto úkolů je **[rozpoznávání pojmenovaných entit](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), které se zabývá identifikací konkrétních entit v textu, jako jsou místa, jména osob, časové intervaly, chemické vzorce a podobně.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Příklad použití NER

Představte si, že chcete vyvinout chatbot pro přirozený jazyk, podobný Amazon Alexa nebo Google Assistant. Inteligentní chatboti fungují tak, že *rozumí* tomu, co uživatel chce, pomocí klasifikace textu na vstupní větě. Výsledkem této klasifikace je tzv. **záměr** (intent), který určuje, co by měl chatbot udělat.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Obrázek od autora

Uživatel však může jako součást fráze poskytnout některé parametry. Například při dotazu na počasí může specifikovat místo nebo datum. Bot by měl být schopen tyto entity pochopit a odpovídajícím způsobem vyplnit parametry před provedením akce. A právě zde přichází na řadu NER.

> ✅ Dalším příkladem by mohlo být [analyzování vědeckých lékařských článků](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Jednou z hlavních věcí, které je třeba hledat, jsou specifické lékařské termíny, jako jsou nemoci a lékařské látky. Zatímco malý počet nemocí lze pravděpodobně extrahovat pomocí vyhledávání podřetězců, složitější entity, jako jsou chemické sloučeniny a názvy léků, vyžadují složitější přístup.

## NER jako klasifikace tokenů

Modely NER jsou v podstatě **modely klasifikace tokenů**, protože pro každý vstupní token musíme rozhodnout, zda patří k nějaké entitě, a pokud ano, ke které třídě entity.

Zvažte následující název článku:

**Regurgitace trikuspidální chlopně** a **uhličitan lithný** **toxicita** u novorozence.

Entity zde jsou:

* Regurgitace trikuspidální chlopně je nemoc (`DIS`)
* Uhličitan lithný je chemická látka (`CHEM`)
* Toxicita je také nemoc (`DIS`)

Všimněte si, že jedna entita může zahrnovat několik tokenů. A, jako v tomto případě, musíme rozlišit mezi dvěma po sobě jdoucími entitami. Proto je běžné používat dvě třídy pro každou entitu - jednu, která specifikuje první token entity (často se používá předpona `B-` pro **b**eginning), a druhou pro pokračování entity (`I-`, pro **i**nner token). Pro všechny **o**statní tokeny používáme třídu `O`. Takové označování tokenů se nazývá [BIO označování](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (nebo IOB). Po označení bude náš název vypadat takto:

Token | Tag
------|-----
Trikuspidální | B-DIS
chlopně | I-DIS
regurgitace | I-DIS
a | O
uhličitan | B-CHEM
lithný | I-CHEM
toxicita | B-DIS
u | O
novorozence | O
. | O

Protože potřebujeme vytvořit jednoznačnou korespondenci mezi tokeny a třídami, můžeme trénovat pravostranný **many-to-many** model neuronové sítě podle tohoto obrázku:

![Obrázek ukazující běžné vzory rekurentních neuronových sítí.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.cs.jpg)

> *Obrázek z [tohoto blogového příspěvku](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) od [Andreje Karpathyho](http://karpathy.github.io/). Modely klasifikace tokenů NER odpovídají pravostranné architektuře sítě na tomto obrázku.*

## Trénování modelů NER

Protože model NER je v podstatě modelem klasifikace tokenů, můžeme pro tento úkol použít RNN, se kterými jsme se již seznámili. V tomto případě každý blok rekurentní sítě vrátí ID tokenu. Následující ukázkový notebook ukazuje, jak trénovat LSTM pro klasifikaci tokenů.

## ✍️ Ukázkové notebooky: NER

Pokračujte ve svém učení v následujícím notebooku:

* [NER s TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Závěr

Model NER je **modelem klasifikace tokenů**, což znamená, že jej lze použít k provádění klasifikace tokenů. Jedná se o velmi běžný úkol v NLP, který pomáhá rozpoznávat konkrétní entity v textu, včetně míst, jmen, dat a dalších.

## 🚀 Výzva

Dokončete úkol uvedený níže, abyste natrénovali model pro rozpoznávání pojmenovaných entit v lékařských termínech, a poté jej vyzkoušejte na jiném datasetu.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Přehled a samostudium

Projděte si blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) a následujte sekci Další čtení v tomto článku, abyste si prohloubili své znalosti.

## [Úkol](lab/README.md)

V úkolu pro tuto lekci budete muset natrénovat model pro rozpoznávání lékařských entit. Můžete začít trénováním modelu LSTM, jak je popsáno v této lekci, a pokračovat použitím modelu transformátoru BERT. Přečtěte si [pokyny](lab/README.md) pro všechny podrobnosti.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.