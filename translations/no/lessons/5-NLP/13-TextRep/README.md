<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-28T16:03:09+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "no"
}
-->
# Representere tekst som tensorer

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Tekstklassifisering

I den første delen av denne seksjonen vil vi fokusere på oppgaven **tekstklassifisering**. Vi skal bruke [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset)-datasettet, som inneholder nyhetsartikler som følgende:

* Kategori: Vitenskap/Teknologi  
* Tittel: Ky. Selskap vinner stipend for å studere peptider (AP)  
* Brødtekst: AP - Et selskap grunnlagt av en kjemiforsker ved University of Louisville vant et stipend for å utvikle...

Målet vårt vil være å klassifisere nyhetsartikkelen i en av kategoriene basert på teksten.

## Representere tekst

Hvis vi ønsker å løse oppgaver innen naturlig språkprosessering (NLP) med nevrale nettverk, trenger vi en måte å representere tekst som tensorer på. Datamaskiner representerer allerede teksttegn som tall som tilsvarer fonter på skjermen ved hjelp av kodinger som ASCII eller UTF-8.

<img alt="Bilde som viser et diagram som kartlegger et tegn til en ASCII- og binær representasjon" src="images/ascii-character-map.png" width="50%"/>

> [Bildekilde](https://www.seobility.net/en/wiki/ASCII)

Som mennesker forstår vi hva hver bokstav **representerer**, og hvordan alle tegnene sammen danner ordene i en setning. Datamaskiner har imidlertid ikke en slik forståelse, og et nevralt nettverk må lære betydningen under trening.

Derfor kan vi bruke ulike tilnærminger for å representere tekst:

* **Tegn-nivå representasjon**, der vi representerer tekst ved å behandle hvert tegn som et tall. Gitt at vi har *C* forskjellige tegn i tekstkorpuset vårt, vil ordet *Hello* bli representert som en 5x*C* tensor. Hver bokstav tilsvarer en tensor-kolonne i en one-hot-koding.  
* **Ord-nivå representasjon**, der vi lager et **ordforråd** av alle ordene i teksten vår, og deretter representerer ordene ved hjelp av one-hot-koding. Denne tilnærmingen er på noen måter bedre, fordi hver bokstav i seg selv ikke har mye mening. Ved å bruke høyere semantiske konsepter - ord - forenkler vi oppgaven for det nevrale nettverket. Men gitt den store ordbokstørrelsen, må vi håndtere høy-dimensjonale, sparsomme tensorer.

Uansett representasjon må vi først konvertere teksten til en sekvens av **tokens**, der en token kan være et tegn, et ord, eller noen ganger til og med en del av et ord. Deretter konverterer vi tokenet til et tall, vanligvis ved hjelp av et **ordforråd**, og dette tallet kan mates inn i et nevralt nettverk ved hjelp av one-hot-koding.

## N-Grammer

I naturlig språk kan den presise betydningen av ord bare bestemmes i kontekst. For eksempel har *nevralt nettverk* og *fiskegarn* helt forskjellige betydninger. En måte å ta dette i betraktning på er å bygge modellen vår på par av ord og betrakte ordpar som separate tokens i ordforrådet. På denne måten vil setningen *Jeg liker å fiske* bli representert av følgende sekvens av tokens: *Jeg liker*, *liker å*, *å fiske*. Problemet med denne tilnærmingen er at ordbokstørrelsen øker betydelig, og kombinasjoner som *å fiske* og *å handle* representeres av forskjellige tokens, som ikke deler noen semantisk likhet til tross for samme verb.

I noen tilfeller kan vi vurdere å bruke tri-grammer – kombinasjoner av tre ord – også. Dermed kalles denne tilnærmingen ofte **n-grammer**. Det gir også mening å bruke n-grammer med tegn-nivå representasjon, der n-grammer grovt sett tilsvarer forskjellige stavelser.

## Bag-of-Words og TF/IDF

Når vi løser oppgaver som tekstklassifisering, må vi kunne representere tekst som en fast-størrelse vektor, som vi vil bruke som input til den endelige tette klassifisatoren. En av de enkleste måtene å gjøre dette på er å kombinere alle individuelle ordrepresentasjoner, for eksempel ved å legge dem sammen. Hvis vi legger sammen one-hot-kodingene av hvert ord, ender vi opp med en frekvensvektor som viser hvor mange ganger hvert ord vises i teksten. En slik representasjon av tekst kalles **bag-of-words** (BoW).

<img src="images/bow.png" width="90%"/>

> Bilde av forfatteren

En BoW representerer i hovedsak hvilke ord som vises i teksten og i hvilke mengder, noe som kan være en god indikasjon på hva teksten handler om. For eksempel er det sannsynlig at en nyhetsartikkel om politikk inneholder ord som *president* og *land*, mens en vitenskapelig publikasjon kan inneholde ord som *kollider*, *oppdaget*, osv. Dermed kan ordfrekvenser i mange tilfeller være en god indikator på tekstinnhold.

Problemet med BoW er at visse vanlige ord, som *og*, *er*, osv., vises i de fleste tekster og har de høyeste frekvensene, noe som maskerer ordene som virkelig er viktige. Vi kan redusere viktigheten av disse ordene ved å ta hensyn til frekvensen ordene forekommer i hele dokumentkolleksjonen. Dette er hovedideen bak TF/IDF-tilnærmingen, som dekkes mer detaljert i notatbøkene som er vedlagt denne leksjonen.

Ingen av disse tilnærmingene kan imidlertid fullt ut ta hensyn til tekstens **semantikk**. Vi trenger kraftigere modeller for nevrale nettverk for å gjøre dette, noe vi vil diskutere senere i denne seksjonen.

## ✍️ Øvelser: Tekstrepresentasjon

Fortsett læringen i følgende notatbøker:

* [Tekstrepresentasjon med PyTorch](TextRepresentationPyTorch.ipynb)  
* [Tekstrepresentasjon med TensorFlow](TextRepresentationTF.ipynb)  

## Konklusjon

Så langt har vi studert teknikker som kan legge frekvensvekt på forskjellige ord. De er imidlertid ikke i stand til å representere mening eller rekkefølge. Som den berømte lingvisten J. R. Firth sa i 1935: "Den fullstendige betydningen av et ord er alltid kontekstuelt, og ingen studie av betydning utenfor kontekst kan tas seriøst." Vi vil senere i kurset lære hvordan vi kan fange opp kontekstuell informasjon fra tekst ved hjelp av språkmodellering.

## 🚀 Utfordring

Prøv noen andre øvelser ved å bruke bag-of-words og forskjellige datamodeller. Du kan finne inspirasjon i denne [konkurransen på Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Gjennomgang og selvstudium

Øv på ferdighetene dine med tekstembedding og bag-of-words-teknikker på [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Oppgave: Notatbøker](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.