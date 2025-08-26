<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-25T23:52:59+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "hr"
}
-->
# Okviri za neuronske mreže

Kao što smo već naučili, da bismo učinkovito trenirali neuronske mreže, moramo učiniti dvije stvari:

* Raditi s tenzorima, npr. množiti, zbrajati i izračunavati funkcije poput sigmoid ili softmax
* Izračunati gradijente svih izraza kako bismo mogli provesti optimizaciju gradijentnog spuštanja

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Iako biblioteka `numpy` može obaviti prvi dio, potrebna nam je neka metoda za izračunavanje gradijenata. U [našem okviru](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) koji smo razvili u prethodnom dijelu morali smo ručno programirati sve funkcije derivacija unutar metode `backward`, koja provodi povratnu propagaciju. Idealno, okvir bi nam trebao omogućiti izračunavanje gradijenata *bilo kojeg izraza* koji možemo definirati.

Još jedna važna stvar je mogućnost izvođenja izračuna na GPU-u ili drugim specijaliziranim jedinicama za izračunavanje, poput [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Treniranje dubokih neuronskih mreža zahtijeva *puno* izračuna, a mogućnost paralelizacije tih izračuna na GPU-ima je vrlo važna.

> ✅ Pojam 'paralelizacija' znači raspodjelu izračuna na više uređaja.

Trenutno su dva najpopularnija okvira za neuronske mreže: [TensorFlow](http://TensorFlow.org) i [PyTorch](https://pytorch.org/). Oba pružaju niskorazinski API za rad s tenzorima na CPU-u i GPU-u. Povrh niskorazinskog API-ja, postoji i visokorazinski API, nazvan [Keras](https://keras.io/) i [PyTorch Lightning](https://pytorchlightning.ai/) odgovarajuće.

Niskorazinski API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
------------------|-------------------------------------|--------------------------------
Visokorazinski API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Niskorazinski API-ji** u oba okvira omogućuju izgradnju tzv. **grafova izračuna**. Ovaj graf definira kako izračunati izlaz (obično funkciju gubitka) s obzirom na ulazne parametre i može se poslati na GPU za izračunavanje, ako je dostupan. Postoje funkcije za diferenciranje ovog grafa izračuna i izračunavanje gradijenata, koji se zatim mogu koristiti za optimizaciju parametara modela.

**Visokorazinski API-ji** tretiraju neuronske mreže kao **sekvencu slojeva** i olakšavaju konstrukciju većine neuronskih mreža. Treniranje modela obično zahtijeva pripremu podataka, a zatim pozivanje funkcije `fit` za obavljanje posla.

Visokorazinski API omogućuje brzu konstrukciju tipičnih neuronskih mreža bez brige o mnogim detaljima. Istovremeno, niskorazinski API pruža mnogo više kontrole nad procesom treniranja, pa se često koristi u istraživanju, kada se radi s novim arhitekturama neuronskih mreža.

Također je važno razumjeti da možete koristiti oba API-ja zajedno, npr. možete razviti vlastitu arhitekturu sloja mreže koristeći niskorazinski API, a zatim je koristiti unutar veće mreže konstruirane i trenirane s visokorazinskim API-jem. Ili možete definirati mrežu koristeći visokorazinski API kao sekvencu slojeva, a zatim koristiti vlastitu niskorazinsku petlju treniranja za optimizaciju. Oba API-ja koriste iste osnovne koncepte i dizajnirani su da dobro surađuju.

## Učenje

U ovom tečaju nudimo većinu sadržaja za PyTorch i TensorFlow. Možete odabrati svoj preferirani okvir i proći samo odgovarajuće bilježnice. Ako niste sigurni koji okvir odabrati, pročitajte neke rasprave na internetu o **PyTorch vs. TensorFlow**. Također možete pogledati oba okvira kako biste stekli bolji uvid.

Gdje je moguće, koristit ćemo visokorazinske API-je radi jednostavnosti. Međutim, vjerujemo da je važno razumjeti kako neuronske mreže funkcioniraju od temelja, pa ćemo na početku raditi s niskorazinskim API-jem i tenzorima. Međutim, ako želite brzo krenuti i ne želite trošiti puno vremena na učenje ovih detalja, možete preskočiti te dijelove i odmah prijeći na bilježnice s visokorazinskim API-jem.

## ✍️ Vježbe: Okviri

Nastavite svoje učenje u sljedećim bilježnicama:

Niskorazinski API | [TensorFlow+Keras Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
------------------|-------------------------------------|--------------------------------
Visokorazinski API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Nakon što savladate okvire, ponovimo pojam pretreniranja.

# Pretreniranje

Pretreniranje je iznimno važan koncept u strojnom učenju i vrlo je važno razumjeti ga!

Razmotrimo sljedeći problem aproksimacije 5 točaka (predstavljenih s `x` na grafovima dolje):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.hr.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.hr.jpg)
-------------------------|--------------------------
**Linearni model, 2 parametra** | **Nelinearni model, 7 parametara**
Pogreška na treningu = 5.3 | Pogreška na treningu = 0
Pogreška na validaciji = 5.1 | Pogreška na validaciji = 20

* Na lijevoj strani vidimo dobru aproksimaciju ravnom linijom. Budući da je broj parametara adekvatan, model ispravno razumije raspodjelu točaka.
* Na desnoj strani model je previše moćan. Budući da imamo samo 5 točaka, a model ima 7 parametara, može se prilagoditi tako da prolazi kroz sve točke, čineći pogrešku na treningu 0. Međutim, to sprječava model da razumije ispravan obrazac podataka, pa je pogreška na validaciji vrlo visoka.

Vrlo je važno postići ispravnu ravnotežu između bogatstva modela (broja parametara) i broja uzoraka za trening.

## Zašto dolazi do pretreniranja

  * Nedovoljno podataka za trening
  * Previše moćan model
  * Previše šuma u ulaznim podacima

## Kako otkriti pretreniranje

Kao što možete vidjeti na grafu iznad, pretreniranje se može otkriti vrlo niskom pogreškom na treningu i visokom pogreškom na validaciji. Obično tijekom treninga vidimo kako pogreške na treningu i validaciji počinju opadati, a zatim u nekom trenutku pogreška na validaciji može prestati opadati i početi rasti. To će biti znak pretreniranja i pokazatelj da bismo trebali zaustaviti trening u tom trenutku (ili barem napraviti snimku modela).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.hr.png)

## Kako spriječiti pretreniranje

Ako primijetite da dolazi do pretreniranja, možete učiniti sljedeće:

 * Povećati količinu podataka za trening
 * Smanjiti složenost modela
 * Koristiti neku [tehniku regularizacije](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), poput [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), koju ćemo kasnije razmotriti.

## Pretreniranje i kompromis pristranosti-varijance

Pretreniranje je zapravo slučaj općenitijeg problema u statistici nazvanog [kompromis pristranosti-varijance](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Ako razmotrimo moguće izvore pogreške u našem modelu, možemo vidjeti dvije vrste pogrešaka:

* **Pogreške pristranosti** uzrokovane su time što naš algoritam ne može ispravno uhvatiti odnos između podataka za trening. To može biti rezultat činjenice da naš model nije dovoljno moćan (**nedovoljno treniranje**).
* **Pogreške varijance**, koje su uzrokovane time što model aproksimira šum u ulaznim podacima umjesto značajnog odnosa (**pretreniranje**).

Tijekom treninga, pogreška pristranosti opada (kako naš model uči aproksimirati podatke), a pogreška varijance raste. Važno je zaustaviti trening - bilo ručno (kada otkrijemo pretreniranje) ili automatski (uvođenjem regularizacije) - kako bismo spriječili pretreniranje.

## Zaključak

U ovoj lekciji naučili ste o razlikama između različitih API-ja za dva najpopularnija AI okvira, TensorFlow i PyTorch. Osim toga, naučili ste o vrlo važnoj temi, pretreniranje.

## 🚀 Izazov

U pratećim bilježnicama pronaći ćete 'zadaci' na dnu; prođite kroz bilježnice i dovršite zadatke.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Pregled i samostalno učenje

Provedite istraživanje o sljedećim temama:

- TensorFlow
- PyTorch
- Pretreniranje

Postavite si sljedeća pitanja:

- Koja je razlika između TensorFlow i PyTorch?
- Koja je razlika između pretreniranja i nedovoljnog treniranja?

## [Zadatak](lab/README.md)

U ovom laboratoriju traži se da riješite dva problema klasifikacije koristeći jednostavne i višeslojne potpuno povezane mreže koristeći PyTorch ili TensorFlow.

* [Upute](lab/README.md)
* [Bilježnica](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.