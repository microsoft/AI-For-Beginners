<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-25T22:10:08+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "hu"
}
-->
# Névjegy Felismerés

Eddig főként egy NLP feladatra, a klasszifikációra koncentráltunk. Azonban léteznek más NLP feladatok is, amelyeket neurális hálózatokkal meg lehet oldani. Az egyik ilyen feladat a **[Névjegy Felismerés](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), amely a szövegben található konkrét entitások, például helyek, személynevek, dátum-idő intervallumok, kémiai képletek stb. felismerésével foglalkozik.

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Példa a NER használatára

Tegyük fel, hogy egy természetes nyelvi chatbotot szeretnél fejleszteni, hasonlóan az Amazon Alexa vagy a Google Assistant megoldásaihoz. Az intelligens chatbotok úgy működnek, hogy *megértik*, mit szeretne a felhasználó, azáltal hogy szövegklasszifikációt végeznek a bemeneti mondaton. Ennek a klasszifikációnak az eredménye az úgynevezett **szándék**, amely meghatározza, mit kell tennie a chatbotnak.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Kép a szerzőtől

Azonban a felhasználó megadhat bizonyos paramétereket a mondat részeként. Például, ha az időjárásról kérdez, megadhat egy helyszínt vagy dátumot. A chatbotnak képesnek kell lennie felismerni ezeket az entitásokat, és kitölteni a paraméterhelyeket, mielőtt végrehajtja a műveletet. Pontosan itt jön képbe a NER.

> ✅ Egy másik példa lehet [tudományos orvosi cikkek elemzése](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Az egyik fő dolog, amit keresnünk kell, az a konkrét orvosi kifejezések, például betegségek és orvosi anyagok. Míg egy kis számú betegséget valószínűleg ki lehet nyerni szövegrészlet-kereséssel, összetettebb entitások, mint például kémiai vegyületek és gyógyszernevek, bonyolultabb megközelítést igényelnek.

## NER mint Token Klasszifikáció

A NER modellek lényegében **token klasszifikációs modellek**, mivel minden bemeneti tokenről el kell döntenünk, hogy egy entitáshoz tartozik-e vagy sem, és ha igen, melyik entitásosztályhoz.

Vegyük például az alábbi cikkcímet:

**Tricuspidalis billentyű regurgitáció** és **lítium-karbonát** **toxicitás** egy újszülött csecsemőben.

Az entitások itt a következők:

* A Tricuspidalis billentyű regurgitáció egy betegség (`DIS`)
* A Lítium-karbonát egy kémiai anyag (`CHEM`)
* A Toxicitás szintén egy betegség (`DIS`)

Figyeld meg, hogy egy entitás több tokenből is állhat. És, ahogy ebben az esetben, meg kell különböztetnünk két egymást követő entitást. Ezért gyakori, hogy két osztályt használunk minden entitáshoz - az egyik az entitás első tokenjét jelöli (gyakran a `B-` előtagot használjuk, a **b**eginning, azaz kezdés jelölésére), a másik pedig az entitás folytatását (`I-`, azaz **i**nner token). Az összes **o**ther, azaz egyéb tokenek jelölésére az `O` osztályt használjuk. Az ilyen token címkézést [BIO címkézésnek](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (vagy IOB) nevezzük. Ha címkézzük, a címünk így fog kinézni:

Token | Címke
------|-----
Tricuspidalis | B-DIS
billentyű | I-DIS
regurgitáció | I-DIS
és | O
lítium | B-CHEM
karbonát | I-CHEM
toxicitás | B-DIS
egy | O
újszülött | O
csecsemőben | O
. | O

Mivel egy-egy megfeleltetést kell létrehoznunk a tokenek és osztályok között, egy **sok-az-egyhez** neurális hálózati modellt tudunk tanítani ebből a képből:

![Kép, amely a gyakori rekurzív neurális hálózati mintákat mutatja.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.hu.jpg)

> *Kép [ebből a blogbejegyzésből](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) [Andrej Karpathy](http://karpathy.github.io/) tollából. A NER token klasszifikációs modellek megfelelnek a jobb szélső hálózati architektúrának ezen a képen.*

## NER modellek tanítása

Mivel a NER modell lényegében egy token klasszifikációs modell, az általunk már ismert RNN-eket használhatjuk erre a feladatra. Ebben az esetben minden rekurzív hálózati blokk visszaadja a token ID-t. Az alábbi példajegyzet bemutatja, hogyan lehet LSTM-et tanítani token klasszifikációra.

## ✍️ Példajegyzetek: NER

Folytasd a tanulást az alábbi jegyzetben:

* [NER TensorFlow-val](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Összegzés

A NER modell egy **token klasszifikációs modell**, ami azt jelenti, hogy token klasszifikációt tud végezni. Ez egy nagyon gyakori feladat az NLP-ben, amely segít felismerni konkrét entitásokat a szövegben, például helyeket, neveket, dátumokat és még sok mást.

## 🚀 Kihívás

Teljesítsd az alábbi feladathoz kapcsolódó kihívást, amelyben egy orvosi kifejezéseket felismerő modellt kell tanítanod, majd próbáld ki egy másik adathalmazon.

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Áttekintés és önálló tanulás

Olvasd el a blogot [A rekurzív neurális hálózatok ésszerűtlen hatékonysága](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) címmel, és kövesd az ott található További Olvasmányok szekciót, hogy elmélyítsd tudásodat.

## [Feladat](lab/README.md)

Az ehhez a leckéhez tartozó feladatban egy orvosi entitás felismerő modellt kell tanítanod. Kezdheted az LSTM modell tanításával, ahogy ebben a leckében leírtuk, majd folytathatod a BERT transformer modell használatával. Olvasd el [az utasításokat](lab/README.md), hogy minden részletet megtudj.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.