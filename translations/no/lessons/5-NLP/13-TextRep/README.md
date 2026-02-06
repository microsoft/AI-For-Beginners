# Representere tekst som tensorer

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Tekstklassifisering

I den første delen av denne seksjonen vil vi fokusere på oppgaven **tekstklassifisering**. Vi skal bruke [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset)-datasettet, som inneholder nyhetsartikler som følgende:

* Kategori: Sci/Tech
* Tittel: Ky. Company Wins Grant to Study Peptides (AP)
* Kropp: AP - Et selskap grunnlagt av en kjemiforsker ved University of Louisville vant et stipend for å utvikle...

Målet vårt vil være å klassifisere nyhetsartikkelen i en av kategoriene basert på teksten.

## Representere tekst

Hvis vi ønsker å løse oppgaver innen Natural Language Processing (NLP) med nevrale nettverk, trenger vi en måte å representere tekst som tensorer. Datamaskiner representerer allerede teksttegn som tall som kartlegger til fonter på skjermen din ved hjelp av kodinger som ASCII eller UTF-8.

<img alt="Bilde som viser diagram som kartlegger et tegn til ASCII- og binærrepresentasjon" src="../../../../../translated_images/no/ascii-character-map.18ed6aa7f3b0a7ff.webp" width="50%"/>

> [Bildekilde](https://www.seobility.net/en/wiki/ASCII)

Som mennesker forstår vi hva hver bokstav **representerer**, og hvordan alle tegnene kommer sammen for å danne ordene i en setning. Datamaskiner har imidlertid ikke en slik forståelse av seg selv, og det nevrale nettverket må lære betydningen under trening.

Derfor kan vi bruke forskjellige tilnærminger når vi representerer tekst:

* **Tegn-nivå representasjon**, der vi representerer tekst ved å behandle hvert tegn som et tall. Gitt at vi har *C* forskjellige tegn i tekstkorpuset vårt, vil ordet *Hello* bli representert av en 5x*C* tensor. Hver bokstav vil tilsvare en tensor-kolonne i en one-hot encoding.
* **Ord-nivå representasjon**, der vi lager et **vokabular** av alle ord i teksten vår, og deretter representerer ord ved hjelp av one-hot encoding. Denne tilnærmingen er på en måte bedre, fordi hver bokstav i seg selv ikke har mye mening, og ved å bruke høyere nivå semantiske konsepter - ord - forenkler vi oppgaven for det nevrale nettverket. Men gitt den store ordbokstørrelsen, må vi håndtere høy-dimensjonale sparsomme tensorer.

Uansett representasjon, må vi først konvertere teksten til en sekvens av **tokens**, der én token er enten et tegn, et ord, eller noen ganger til og med en del av et ord. Deretter konverterer vi tokenet til et tall, vanligvis ved hjelp av **vokabular**, og dette tallet kan mates inn i et nevralt nettverk ved hjelp av one-hot encoding.

## N-Grams

I naturlig språk kan den presise betydningen av ord bare bestemmes i kontekst. For eksempel er betydningene av *nevralt nettverk* og *fiskegarn* helt forskjellige. En av måtene å ta dette i betraktning på er å bygge modellen vår på par av ord, og betrakte ordpar som separate vokabular-tokens. På denne måten vil setningen *I like to go fishing* bli representert av følgende sekvens av tokens: *I like*, *like to*, *to go*, *go fishing*. Problemet med denne tilnærmingen er at ordbokstørrelsen øker betydelig, og kombinasjoner som *go fishing* og *go shopping* presenteres av forskjellige tokens, som ikke deler noen semantisk likhet til tross for samme verb.

I noen tilfeller kan vi vurdere å bruke tri-grams -- kombinasjoner av tre ord -- også. Dermed kalles denne tilnærmingen ofte **n-grams**. Det gir også mening å bruke n-grams med tegn-nivå representasjon, der n-grams grovt sett vil tilsvare forskjellige stavelser.

## Bag-of-Words og TF/IDF

Når vi løser oppgaver som tekstklassifisering, må vi kunne representere tekst med én vektor av fast størrelse, som vi vil bruke som input til den endelige tette klassifisereren. En av de enkleste måtene å gjøre dette på er å kombinere alle individuelle ordrepresentasjoner, f.eks. ved å legge dem sammen. Hvis vi legger sammen one-hot encodingene av hvert ord, ender vi opp med en frekvensvektor som viser hvor mange ganger hvert ord vises i teksten. En slik representasjon av tekst kalles **bag of words** (BoW).

<img src="../../../../../translated_images/no/bow.3811869cff59368d.webp" width="90%"/>

> Bilde av forfatteren

En BoW representerer i hovedsak hvilke ord som vises i teksten og i hvilke mengder, noe som faktisk kan være en god indikasjon på hva teksten handler om. For eksempel vil en nyhetsartikkel om politikk sannsynligvis inneholde ord som *president* og *land*, mens en vitenskapelig publikasjon vil ha noe som *kollider*, *oppdaget*, osv. Dermed kan ordfrekvenser i mange tilfeller være en god indikator på tekstinnhold.

Problemet med BoW er at visse vanlige ord, som *og*, *er*, osv. vises i de fleste tekster, og de har høyest frekvenser, noe som maskerer ut ordene som virkelig er viktige. Vi kan redusere viktigheten av disse ordene ved å ta hensyn til frekvensen som ord forekommer med i hele dokumentkolleksjonen. Dette er hovedideen bak TF/IDF-tilnærmingen, som er dekket mer detaljert i notatbøkene som er vedlagt denne leksjonen.

Ingen av disse tilnærmingene kan imidlertid fullt ut ta hensyn til **semantikken** i teksten. Vi trenger mer kraftige nevrale nettverksmodeller for å gjøre dette, som vi vil diskutere senere i denne seksjonen.

## ✍️ Øvelser: Tekstrepresentasjon

Fortsett læringen din i følgende notatbøker:

* [Tekstrepresentasjon med PyTorch](TextRepresentationPyTorch.ipynb)
* [Tekstrepresentasjon med TensorFlow](TextRepresentationTF.ipynb)

## Konklusjon

Så langt har vi studert teknikker som kan legge frekvensvekt til forskjellige ord. De er imidlertid ikke i stand til å representere mening eller rekkefølge. Som den berømte lingvisten J. R. Firth sa i 1935, "Den fullstendige betydningen av et ord er alltid kontekstuelt, og ingen studie av mening utenfor kontekst kan tas seriøst." Senere i kurset vil vi lære hvordan vi kan fange kontekstuell informasjon fra tekst ved hjelp av språkmodellering.

## 🚀 Utfordring

Prøv noen andre øvelser ved hjelp av bag-of-words og forskjellige datamodeller. Du kan bli inspirert av denne [konkurransen på Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Gjennomgang og selvstudium

Øv på ferdighetene dine med tekstinnbygging og bag-of-words-teknikker på [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Oppgave: Notatbøker](assignment.md)

---

