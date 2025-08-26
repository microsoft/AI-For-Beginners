<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-25T21:51:51+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "hr"
}
-->
# Predstavljanje teksta kao tenzora

## [Kviz prije predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Klasifikacija teksta

U prvom dijelu ovog poglavlja fokusirat ćemo se na zadatak **klasifikacije teksta**. Koristit ćemo [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) dataset, koji sadrži vijesti poput sljedeće:

* Kategorija: Znanost/Tehnologija  
* Naslov: Ky. tvrtka dobila potporu za proučavanje peptida (AP)  
* Tekst: AP - Tvrtka koju je osnovao istraživač kemije sa Sveučilišta u Louisvilleu dobila je potporu za razvoj...

Naš cilj bit će klasificirati vijest u jednu od kategorija na temelju teksta.

## Predstavljanje teksta

Ako želimo rješavati zadatke obrade prirodnog jezika (NLP) pomoću neuronskih mreža, trebamo način za predstavljanje teksta kao tenzora. Računala već predstavljaju tekstualne znakove kao brojeve koji se mapiraju na fontove na vašem ekranu koristeći kodiranja poput ASCII ili UTF-8.

<img alt="Slika koja prikazuje dijagram mapiranja znaka na ASCII i binarnu reprezentaciju" src="images/ascii-character-map.png" width="50%"/>

> [Izvor slike](https://www.seobility.net/en/wiki/ASCII)

Kao ljudi, razumijemo što svako slovo **predstavlja** i kako se svi znakovi spajaju u riječi rečenice. Međutim, računala sama po sebi nemaju takvo razumijevanje, i neuronska mreža mora naučiti značenje tijekom treniranja.

Stoga možemo koristiti različite pristupe za predstavljanje teksta:

* **Reprezentacija na razini znakova**, gdje tekst predstavljamo tretirajući svaki znak kao broj. Ako imamo *C* različitih znakova u našem tekstualnom korpusu, riječ *Hello* bila bi predstavljena kao 5x*C* tenzor. Svako slovo odgovara stupcu tenzora u one-hot kodiranju.  
* **Reprezentacija na razini riječi**, gdje stvaramo **rječnik** svih riječi u našem tekstu, a zatim predstavljamo riječi koristeći one-hot kodiranje. Ovaj pristup je donekle bolji jer svako slovo samo po sebi nema puno značenja, pa korištenjem semantički viših koncepata - riječi - pojednostavljujemo zadatak za neuronsku mrežu. Međutim, zbog velike veličine rječnika, moramo se nositi s visokodimenzionalnim rijetkim tenzorima.

Bez obzira na način predstavljanja, prvo trebamo pretvoriti tekst u niz **tokena**, pri čemu je jedan token znak, riječ ili ponekad čak dio riječi. Zatim token pretvaramo u broj, obično koristeći **rječnik**, a taj broj može se unijeti u neuronsku mrežu koristeći one-hot kodiranje.

## N-grami

U prirodnom jeziku precizno značenje riječi može se odrediti samo u kontekstu. Na primjer, značenja izraza *neuronska mreža* i *ribička mreža* potpuno su različita. Jedan od načina da to uzmemo u obzir je izgradnja modela na parovima riječi, tretirajući parove riječi kao zasebne tokene u rječniku. Na taj način, rečenica *Volim ići na pecanje* bit će predstavljena sljedećim nizom tokena: *Volim ići*, *ići na*, *na pecanje*. Problem s ovim pristupom je što veličina rječnika značajno raste, a kombinacije poput *na pecanje* i *na kupovinu* predstavljene su različitim tokenima, koji ne dijele nikakvu semantičku sličnost unatoč istom glagolu.

U nekim slučajevima možemo razmotriti korištenje tri-grama -- kombinacija od tri riječi -- također. Ovaj pristup često se naziva **n-grami**. Također, ima smisla koristiti n-grame s reprezentacijom na razini znakova, gdje n-grami otprilike odgovaraju različitim slogovima.

## Bag-of-Words i TF/IDF

Kod rješavanja zadataka poput klasifikacije teksta, trebamo biti u mogućnosti predstaviti tekst jednim vektorom fiksne veličine, koji ćemo koristiti kao ulaz za završni gusti klasifikator. Jedan od najjednostavnijih načina za to je kombiniranje svih pojedinačnih reprezentacija riječi, npr. njihovim zbrajanjem. Ako zbrojimo one-hot kodiranja svake riječi, dobit ćemo vektor frekvencija, koji pokazuje koliko se puta svaka riječ pojavljuje u tekstu. Takva reprezentacija teksta naziva se **bag-of-words** (BoW).

<img src="images/bow.png" width="90%"/>

> Slika autora

BoW u osnovi predstavlja koje se riječi pojavljuju u tekstu i u kojim količinama, što može biti dobar pokazatelj o čemu se tekst radi. Na primjer, članak o politici vjerojatno sadrži riječi poput *predsjednik* i *država*, dok bi znanstvena publikacija imala nešto poput *sudarač*, *otkriveno*, itd. Dakle, frekvencije riječi u mnogim slučajevima mogu biti dobar pokazatelj sadržaja teksta.

Problem s BoW-om je što se određene uobičajene riječi, poput *i*, *je*, itd., pojavljuju u većini tekstova i imaju najviše frekvencije, maskirajući riječi koje su zaista važne. Možemo smanjiti važnost tih riječi uzimajući u obzir učestalost pojavljivanja riječi u cijeloj kolekciji dokumenata. Ovo je glavna ideja iza TF/IDF pristupa, koji je detaljnije obrađen u priloženim bilježnicama ovog poglavlja.

Međutim, nijedan od ovih pristupa ne može u potpunosti uzeti u obzir **semantiku** teksta. Za to su nam potrebni snažniji modeli neuronskih mreža, o kojima ćemo raspravljati kasnije u ovom poglavlju.

## ✍️ Vježbe: Predstavljanje teksta

Nastavite učiti u sljedećim bilježnicama:

* [Predstavljanje teksta s PyTorchom](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Predstavljanje teksta s TensorFlowom](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)  

## Zaključak

Do sada smo proučavali tehnike koje mogu dodati težinu frekvencijama različitih riječi. Međutim, one nisu sposobne predstaviti značenje ili redoslijed. Kao što je poznati lingvist J. R. Firth rekao 1935. godine: "Potpuno značenje riječi uvijek je kontekstualno, i nijedno proučavanje značenja izvan konteksta ne može se smatrati ozbiljnim." Kasnije u tečaju naučit ćemo kako uhvatiti kontekstualne informacije iz teksta koristeći modele jezika.

## 🚀 Izazov

Isprobajte neke druge vježbe koristeći bag-of-words i različite modele podataka. Možete se inspirirati ovim [natjecanjem na Kaggleu](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Kviz nakon predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Pregled i samostalno učenje

Uvježbajte svoje vještine s tehnikama ugrađivanja teksta i bag-of-words na [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Zadatak: Bilježnice](assignment.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.