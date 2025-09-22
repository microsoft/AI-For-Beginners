<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-28T15:24:32+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "no"
}
-->
# Autoenkodere

Når vi trener CNN-er, er en av utfordringene at vi trenger mye merket data. Når det gjelder bildeklassifisering, må vi dele bilder inn i forskjellige klasser, noe som krever manuelt arbeid.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Vi kan imidlertid ønske å bruke rå (umerket) data for å trene CNN-funksjonsekstraktorer, noe som kalles **selv-supervisert læring**. I stedet for etiketter bruker vi treningsbilder både som nettverksinput og output. Hovedideen med **autoenkoder** er at vi har et **enkodernettverk** som konverterer inputbildet til et **latent rom** (vanligvis bare en vektor av mindre størrelse), og deretter et **dekodernettverk**, som har som mål å rekonstruere det originale bildet.

> ✅ En [autoenkoder](https://wikipedia.org/wiki/Autoencoder) er "en type kunstig nevralt nettverk som brukes til å lære effektive kodinger av umerket data."

Siden vi trener en autoenkoder til å fange så mye informasjon som mulig fra det originale bildet for nøyaktig rekonstruksjon, prøver nettverket å finne den beste **innkapslingen** av inputbilder for å fange meningen.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.no.jpg)

> Bilde fra [Keras-bloggen](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenarier for bruk av autoenkodere

Selv om det å rekonstruere originale bilder ikke virker nyttig i seg selv, finnes det noen scenarier der autoenkodere er spesielt nyttige:

* **Redusere dimensjonen på bilder for visualisering** eller **trene bildeinnkapslinger**. Vanligvis gir autoenkodere bedre resultater enn PCA, fordi de tar hensyn til bildenes romlige natur og hierarkiske funksjoner.
* **Fjerne støy**, altså fjerne støy fra bildet. Fordi støy inneholder mye unyttig informasjon, kan ikke autoenkoderen få plass til alt i det relativt lille latente rommet, og dermed fanger den bare den viktige delen av bildet. Når vi trener støyfjernere, starter vi med originale bilder og bruker bilder med kunstig lagt til støy som input for autoenkoderen.
* **Superoppløsning**, øke bildekvaliteten. Vi starter med bilder med høy oppløsning og bruker bildet med lavere oppløsning som input for autoenkoderen.
* **Generative modeller**. Når vi har trent autoenkoderen, kan dekoderdelen brukes til å lage nye objekter basert på tilfeldige latente vektorer.

## Variasjonelle autoenkodere (VAE)

Tradisjonelle autoenkodere reduserer dimensjonen på inputdata på en eller annen måte, og finner de viktige funksjonene i inputbildene. Latente vektorer gir imidlertid ofte ikke mye mening. Med andre ord, hvis vi tar MNIST-datasettet som et eksempel, er det ikke lett å finne ut hvilke sifre som tilsvarer forskjellige latente vektorer, fordi nærliggende latente vektorer ikke nødvendigvis tilsvarer de samme sifrene.

På den annen side, for å trene *generative* modeller er det bedre å ha en viss forståelse av det latente rommet. Denne ideen leder oss til **variabel autoenkoder** (VAE).

VAE er en autoenkoder som lærer å forutsi *statistisk fordeling* av de latente parameterne, den såkalte **latente fordelingen**. For eksempel kan vi ønske at latente vektorer skal være normalt fordelt med en viss gjennomsnitt z<sub>mean</sub> og standardavvik z<sub>sigma</sub> (både gjennomsnitt og standardavvik er vektorer med en viss dimensjonalitet d). Enkoder i VAE lærer å forutsi disse parameterne, og deretter tar dekoderen en tilfeldig vektor fra denne fordelingen for å rekonstruere objektet.

For å oppsummere:

 * Fra inputvektoren forutsier vi `z_mean` og `z_log_sigma` (i stedet for å forutsi standardavviket direkte, forutsier vi logaritmen av det)
 * Vi tar en prøvevektor `sample` fra fordelingen N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Dekoderen prøver å dekode det originale bildet ved å bruke `sample` som inputvektor

 <img src="images/vae.png" width="50%">

> Bilde fra [denne bloggposten](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) av Isaak Dykeman

Variasjonelle autoenkodere bruker en kompleks tapsfunksjon som består av to deler:

* **Rekonstruksjonstap** er tapsfunksjonen som viser hvor nært et rekonstruert bilde er målet (det kan være Mean Squared Error, eller MSE). Det er den samme tapsfunksjonen som i vanlige autoenkodere.
* **KL-tap**, som sikrer at den latente variabelens fordeling holder seg nær normalfordelingen. Det er basert på begrepet [Kullback-Leibler-divergens](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - en metrikk for å estimere hvor like to statistiske fordelinger er.

En viktig fordel med VAE-er er at de lar oss generere nye bilder relativt enkelt, fordi vi vet hvilken fordeling vi skal ta latente vektorer fra. For eksempel, hvis vi trener VAE med en 2D latent vektor på MNIST, kan vi deretter variere komponentene i den latente vektoren for å få forskjellige sifre:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Bilde av [Dmitry Soshnikov](http://soshnikov.com)

Legg merke til hvordan bildene glir over i hverandre, ettersom vi begynner å ta latente vektorer fra forskjellige deler av det latente parameterrommet. Vi kan også visualisere dette rommet i 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Bilde av [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Øvelser: Autoenkodere

Lær mer om autoenkodere i disse tilhørende notatbøkene:

* [Autoenkodere i TensorFlow](AutoencodersTF.ipynb)
* [Autoenkodere i PyTorch](AutoEncodersPyTorch.ipynb)

## Egenskaper ved autoenkodere

* **Dataspesifikke** - de fungerer bare godt med den typen bilder de er trent på. For eksempel, hvis vi trener et superoppløsningsnettverk på blomster, vil det ikke fungere godt på portretter. Dette er fordi nettverket kan produsere bilder med høyere oppløsning ved å ta fine detaljer fra funksjoner lært fra treningsdatasettet.
* **Tapsbaserte** - det rekonstruerte bildet er ikke det samme som det originale bildet. Tapets natur er definert av *tapsfunksjonen* som brukes under trening.
* Fungerer på **umerket data**

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Konklusjon

I denne leksjonen lærte du om de forskjellige typene autoenkodere som er tilgjengelige for AI-forskeren. Du lærte hvordan du bygger dem, og hvordan du bruker dem til å rekonstruere bilder. Du lærte også om VAE og hvordan du bruker det til å generere nye bilder.

## 🚀 Utfordring

I denne leksjonen lærte du om bruk av autoenkodere for bilder. Men de kan også brukes for musikk! Sjekk ut Magenta-prosjektets [MusicVAE](https://magenta.tensorflow.org/music-vae)-prosjekt, som bruker autoenkodere for å lære å rekonstruere musikk. Gjør noen [eksperimenter](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) med dette biblioteket for å se hva du kan skape.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Gjennomgang & Selvstudium

For referanse, les mer om autoenkodere i disse ressursene:

* [Bygge autoenkodere i Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Bloggpost på NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variasjonelle autoenkodere forklart](https://kvfrans.com/variational-autoencoders-explained/)
* [Betingede variasjonelle autoenkodere](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Oppgave

På slutten av [denne notatboken med TensorFlow](AutoencodersTF.ipynb), finner du en 'oppgave' - bruk denne som din oppgave.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.