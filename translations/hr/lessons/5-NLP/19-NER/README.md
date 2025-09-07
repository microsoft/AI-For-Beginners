<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-25T22:12:15+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "hr"
}
-->
# Prepoznavanje imenovanih entiteta

Do sada smo se uglavnom fokusirali na jedan NLP zadatak - klasifikaciju. Međutim, postoje i drugi NLP zadaci koji se mogu ostvariti pomoću neuronskih mreža. Jedan od tih zadataka je **[Prepoznavanje imenovanih entiteta](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), koji se bavi prepoznavanjem specifičnih entiteta unutar teksta, poput mjesta, imena osoba, vremenskih intervala, kemijskih formula i slično.

## [Kviz prije predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Primjer korištenja NER-a

Pretpostavimo da želite razviti chatbot za prirodni jezik, sličan Amazon Alexi ili Google Asistentu. Način na koji inteligentni chatbotovi funkcioniraju je da *razumiju* što korisnik želi, radeći klasifikaciju teksta na ulaznoj rečenici. Rezultat te klasifikacije je takozvana **namjera** (intent), koja određuje što chatbot treba učiniti.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Slika autora

Međutim, korisnik može pružiti neke parametre kao dio fraze. Na primjer, kada pita za vremensku prognozu, može navesti lokaciju ili datum. Bot bi trebao razumjeti te entitete i popuniti odgovarajuće parametarske prostore prije nego što izvrši radnju. Upravo tu dolazi NER.

> ✅ Drugi primjer bio bi [analiza znanstvenih medicinskih radova](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Jedna od glavnih stvari koje trebamo tražiti su specifični medicinski termini, poput bolesti i medicinskih supstanci. Dok se mali broj bolesti vjerojatno može izdvojiti pretragom podniza, složeniji entiteti, poput kemijskih spojeva i naziva lijekova, zahtijevaju složeniji pristup.

## NER kao klasifikacija tokena

NER modeli su u suštini **modeli za klasifikaciju tokena**, jer za svaki ulazni token trebamo odlučiti pripada li nekom entitetu ili ne, a ako pripada - kojoj klasi entiteta.

Razmotrimo sljedeći naslov rada:

**Regurgitacija trikuspidnog zaliska** i **litijev karbonat** **toksičnost** kod novorođenčeta.

Entiteti ovdje su:

* Regurgitacija trikuspidnog zaliska je bolest (`DIS`)
* Litijev karbonat je kemijska supstanca (`CHEM`)
* Toksičnost je također bolest (`DIS`)

Primijetite da jedan entitet može obuhvatiti nekoliko tokena. I, kao u ovom slučaju, trebamo razlikovati dva uzastopna entiteta. Stoga je uobičajeno koristiti dvije klase za svaki entitet - jednu koja označava prvi token entiteta (često se koristi prefiks `B-` za **početak**), i drugu za nastavak entiteta (`I-`, za **unutarnji token**). Također koristimo `O` kao klasu za predstavljanje svih **ostalih** tokena. Takvo označavanje tokena naziva se [BIO označavanje](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (ili IOB). Kada se označi, naš naslov izgleda ovako:

Token | Oznaka
------|-------
Trikuspid | B-DIS  
zaliska | I-DIS  
regurgitacija | I-DIS  
i | O  
litijev | B-CHEM  
karbonat | I-CHEM  
toksičnost | B-DIS  
kod | O  
novorođenčeta | O  
. | O  

Budući da trebamo uspostaviti jedno-na-jedan korespondenciju između tokena i klasa, možemo trenirati desni **mnogi-na-mnogi** model neuronske mreže iz ove slike:

![Slika koja prikazuje uobičajene obrasce rekurentnih neuronskih mreža.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.hr.jpg)

> *Slika iz [ovog blog posta](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) autora [Andreja Karpathyja](http://karpathy.github.io/). NER modeli za klasifikaciju tokena odgovaraju desnoj mrežnoj arhitekturi na ovoj slici.*

## Treniranje NER modela

Budući da je NER model u suštini model za klasifikaciju tokena, možemo koristiti RNN-ove s kojima smo već upoznati za ovaj zadatak. U ovom slučaju, svaki blok rekurentne mreže vraća ID tokena. Sljedeća bilježnica s primjerima pokazuje kako trenirati LSTM za klasifikaciju tokena.

## ✍️ Primjeri bilježnica: NER

Nastavite s učenjem u sljedećoj bilježnici:

* [NER s TensorFlowom](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Zaključak

NER model je **model za klasifikaciju tokena**, što znači da se može koristiti za klasifikaciju tokena. Ovo je vrlo čest zadatak u NLP-u, koji pomaže prepoznati specifične entitete unutar teksta, uključujući mjesta, imena, datume i još mnogo toga.

## 🚀 Izazov

Dovršite zadatak povezan ispod kako biste trenirali model za prepoznavanje imenovanih entiteta za medicinske termine, a zatim ga isprobajte na drugom skupu podataka.

## [Kviz nakon predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Pregled i samostalno učenje

Pročitajte blog [Nevjerojatna učinkovitost rekurentnih neuronskih mreža](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) i pratite odjeljak Daljnje čitanje u tom članku kako biste produbili svoje znanje.

## [Zadatak](lab/README.md)

U zadatku za ovu lekciju, morat ćete trenirati model za prepoznavanje medicinskih entiteta. Možete započeti s treniranjem LSTM modela kako je opisano u ovoj lekciji, a zatim nastaviti s korištenjem BERT transformera. Pročitajte [upute](lab/README.md) za sve detalje.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.