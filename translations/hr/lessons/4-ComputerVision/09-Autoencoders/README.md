<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:31:34+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "hr"
}
-->
# Autoenkoderi

Prilikom treniranja CNN-ova, jedan od problema je što nam treba puno označenih podataka. U slučaju klasifikacije slika, moramo razdvojiti slike u različite klase, što zahtijeva ručni rad.

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Međutim, možda bismo željeli koristiti sirove (neoznačene) podatke za treniranje CNN ekstraktora značajki, što se naziva **samostalno učenje**. Umjesto oznaka, koristit ćemo slike za treniranje kao ulaz i izlaz mreže. Glavna ideja **autoenkodera** je da imamo **enkodersku mrežu** koja pretvara ulaznu sliku u neki **latentni prostor** (obično je to vektor manje dimenzije), a zatim **dekodersku mrežu**, čiji je cilj rekonstruirati izvornu sliku.

> ✅ [Autoenkoder](https://wikipedia.org/wiki/Autoencoder) je "vrsta umjetne neuronske mreže koja se koristi za učenje učinkovitih kodiranja neoznačenih podataka."

Budući da treniramo autoenkoder kako bi uhvatio što više informacija iz izvorne slike za točnu rekonstrukciju, mreža pokušava pronaći najbolju **ugradnju** ulaznih slika kako bi uhvatila njihovo značenje.

![Dijagram Autoenkodera](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.hr.jpg)

> Slika s [Keras bloga](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenariji za korištenje autoenkodera

Iako rekonstrukcija izvornih slika sama po sebi možda ne izgleda korisna, postoje neki scenariji u kojima su autoenkoderi posebno korisni:

* **Smanjenje dimenzije slika za vizualizaciju** ili **treniranje ugrađivanja slika**. Autoenkoderi obično daju bolje rezultate od PCA jer uzimaju u obzir prostornu prirodu slika i hijerarhijske značajke.
* **Uklanjanje šuma**, tj. uklanjanje šuma sa slike. Budući da šum nosi puno beskorisnih informacija, autoenkoder ne može sve to uklopiti u relativno mali latentni prostor, pa hvata samo važne dijelove slike. Prilikom treniranja za uklanjanje šuma, počinjemo s izvornim slikama i koristimo slike s umjetno dodanim šumom kao ulaz za autoenkoder.
* **Super-rezolucija**, povećanje rezolucije slike. Počinjemo s visokorezolucijskim slikama i koristimo slike niže rezolucije kao ulaz za autoenkoder.
* **Generativni modeli**. Nakon što istreniramo autoenkoder, dekoderski dio može se koristiti za stvaranje novih objekata počevši od slučajnih latentnih vektora.

## Varijacijski autoenkoderi (VAE)

Tradicionalni autoenkoderi na neki način smanjuju dimenziju ulaznih podataka, otkrivajući važne značajke ulaznih slika. Međutim, latentni vektori često nemaju puno smisla. Drugim riječima, uzimajući MNIST dataset kao primjer, nije lako odrediti koji brojevi odgovaraju različitim latentnim vektorima, jer bliski latentni vektori ne moraju nužno odgovarati istim brojevima.

S druge strane, za treniranje *generativnih* modela bolje je imati neko razumijevanje latentnog prostora. Ova ideja vodi nas do **varijacijskog autoenkodera** (VAE).

VAE je autoenkoder koji uči predvidjeti *statističku distribuciju* latentnih parametara, tzv. **latentnu distribuciju**. Na primjer, možemo željeti da latentni vektori budu normalno distribuirani s nekom sredinom z<sub>mean</sub> i standardnom devijacijom z<sub>sigma</sub> (i sredina i standardna devijacija su vektori neke dimenzije d). Enkoder u VAE-u uči predvidjeti te parametre, a zatim dekoder uzima slučajni vektor iz te distribucije za rekonstrukciju objekta.

Ukratko:

 * Iz ulaznog vektora predviđamo `z_mean` i `z_log_sigma` (umjesto da predviđamo standardnu devijaciju, predviđamo njezin logaritam)
 * Uzorkujemo vektor `sample` iz distribucije N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Dekoder pokušava dekodirati izvornu sliku koristeći `sample` kao ulazni vektor

 <img src="images/vae.png" width="50%">

> Slika iz [ovog blog posta](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) autora Isaaka Dykemana

Varijacijski autoenkoderi koriste složenu funkciju gubitka koja se sastoji od dva dijela:

* **Gubitak rekonstrukcije** je funkcija gubitka koja pokazuje koliko je rekonstruirana slika bliska ciljanoj slici (može biti srednja kvadratna pogreška, ili MSE). To je ista funkcija gubitka kao kod običnih autoenkodera.
* **KL gubitak**, koji osigurava da distribucija latentnih varijabli ostane bliska normalnoj distribuciji. Temelji se na konceptu [Kullback-Leiblerove divergencije](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metričke mjere sličnosti između dvije statističke distribucije.

Jedna važna prednost VAE-a je što omogućuju relativno jednostavno generiranje novih slika, jer znamo iz koje distribucije uzorkovati latentne vektore. Na primjer, ako treniramo VAE s 2D latentnim vektorom na MNIST-u, možemo zatim mijenjati komponente latentnog vektora kako bismo dobili različite brojeve:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Slika autora [Dmitryja Soshnikova](http://soshnikov.com)

Primijetite kako se slike stapaju jedna u drugu dok počinjemo dobivati latentne vektore iz različitih dijelova latentnog prostora parametara. Također možemo vizualizirati ovaj prostor u 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Slika autora [Dmitryja Soshnikova](http://soshnikov.com)

## ✍️ Vježbe: Autoenkoderi

Saznajte više o autoenkoderima u ovim odgovarajućim bilježnicama:

* [Autoenkoderi u TensorFlowu](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoenkoderi u PyTorchu](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Svojstva autoenkodera

* **Specifični za podatke** - dobro rade samo s vrstom slika na kojima su trenirani. Na primjer, ako treniramo mrežu za super-rezoluciju na cvijeću, neće dobro raditi na portretima. To je zato što mreža može proizvesti sliku više rezolucije koristeći fine detalje iz značajki naučenih iz skupa podataka za treniranje.
* **Gubitak informacija** - rekonstruirana slika nije ista kao izvorna slika. Priroda gubitka definirana je *funkcijom gubitka* korištenom tijekom treniranja.
* Radi na **neoznačenim podacima**

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Zaključak

U ovoj lekciji naučili ste o različitim vrstama autoenkodera dostupnih AI znanstvenicima. Naučili ste kako ih izgraditi i kako ih koristiti za rekonstrukciju slika. Također ste naučili o VAE-u i kako ga koristiti za generiranje novih slika.

## 🚀 Izazov

U ovoj lekciji naučili ste o korištenju autoenkodera za slike. Ali oni se također mogu koristiti za glazbu! Pogledajte projekt Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), koji koristi autoenkodere za učenje rekonstrukcije glazbe. Napravite nekoliko [eksperimenata](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) s ovom bibliotekom kako biste vidjeli što možete stvoriti.

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Pregled i samostalno učenje

Za referencu, pročitajte više o autoenkoderima u ovim resursima:

* [Izgradnja autoenkodera u Kerasu](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post na NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Objašnjenje varijacijskih autoenkodera](https://kvfrans.com/variational-autoencoders-explained/)
* [Uvjetni varijacijski autoenkoderi](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Zadatak

Na kraju [ove bilježnice koristeći TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), pronaći ćete 'zadatak' - koristite ga kao svoj zadatak.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.