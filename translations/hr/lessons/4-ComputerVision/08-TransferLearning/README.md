<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-25T23:08:57+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "hr"
}
-->
# Predtrenirane mreže i prijenos učenja

Treniranje CNN-a može zahtijevati puno vremena i veliku količinu podataka. Međutim, većina vremena troši se na učenje najboljih niskorazinskih filtera koje mreža može koristiti za izdvajanje uzoraka iz slika. Postavlja se prirodno pitanje - možemo li koristiti neuronsku mrežu treniranu na jednom skupu podataka i prilagoditi je za klasifikaciju različitih slika bez potrebe za potpunim procesom treniranja?

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Ovaj pristup naziva se **prijenos učenja**, jer prenosimo dio znanja iz jednog modela neuronske mreže u drugi. Kod prijenosa učenja obično počinjemo s predtreniranim modelom, koji je treniran na nekom velikom skupu slika, poput **ImageNet**. Ti modeli već dobro obavljaju posao izdvajanja različitih značajki iz generičkih slika, a u mnogim slučajevima samo izgradnja klasifikatora na temelju tih izdvojenih značajki može dati dobre rezultate.

> ✅ Prijenos učenja je pojam koji se koristi i u drugim akademskim područjima, poput obrazovanja. Odnosi se na proces primjene znanja iz jedne domene u drugu.

## Predtrenirani modeli kao ekstraktori značajki

Konvolucijske mreže o kojima smo govorili u prethodnom dijelu sadržavale su niz slojeva, od kojih je svaki trebao izdvojiti određene značajke iz slike, počevši od niskorazinskih kombinacija piksela (poput horizontalnih/vertikalnih linija ili poteza), pa sve do višerazinskih kombinacija značajki koje odgovaraju stvarima poput oka ili plamena. Ako treniramo CNN na dovoljno velikom skupu generičkih i raznolikih slika, mreža bi trebala naučiti izdvajati te zajedničke značajke.

I Keras i PyTorch sadrže funkcije za jednostavno učitavanje predtrenirane težine neuronske mreže za neke uobičajene arhitekture, od kojih je većina trenirana na slikama iz ImageNet-a. Najčešće korištene opisane su na stranici [CNN Architectures](../07-ConvNets/CNN_Architectures.md) iz prethodne lekcije. Konkretno, možete razmotriti korištenje jedne od sljedećih:

* **VGG-16/VGG-19** su relativno jednostavni modeli koji i dalje daju dobru točnost. Često je korištenje VGG-a kao prvog pokušaja dobar izbor za provjeru kako prijenos učenja funkcionira.
* **ResNet** je obitelj modela koju je predložio Microsoft Research 2015. godine. Imaju više slojeva i stoga zahtijevaju više resursa.
* **MobileNet** je obitelj modela smanjene veličine, prikladna za mobilne uređaje. Koristite ih ako imate ograničene resurse i možete žrtvovati malo točnosti.

Evo primjera značajki izdvojenih iz slike mačke pomoću VGG-16 mreže:

![Značajke izdvojene pomoću VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.hr.png)

## Skup podataka Mačke vs. Psi

U ovom primjeru koristit ćemo skup podataka [Mačke i Psi](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), koji je vrlo blizak stvarnom scenariju klasifikacije slika.

## ✍️ Vježba: Prijenos učenja

Pogledajmo prijenos učenja u praksi u pripadajućim bilježnicama:

* [Prijenos učenja - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Prijenos učenja - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Vizualizacija idealne mačke

Predtrenirana neuronska mreža sadrži različite uzorke unutar svog *mozga*, uključujući pojmove **idealne mačke** (kao i idealnog psa, idealne zebre itd.). Bilo bi zanimljivo nekako **vizualizirati ovu sliku**. Međutim, to nije jednostavno, jer su uzorci raspoređeni po težinama mreže i organizirani u hijerarhijsku strukturu.

Jedan pristup koji možemo koristiti je započeti s nasumičnom slikom, a zatim pokušati koristiti tehniku **optimizacije gradijentnog spuštanja** kako bismo prilagodili tu sliku na način da mreža počne misliti da je to mačka.

![Petlja optimizacije slike](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.hr.png)

Međutim, ako to učinimo, dobit ćemo nešto vrlo slično nasumičnom šumu. To je zato što *postoji mnogo načina da mreža pomisli da je ulazna slika mačka*, uključujući neke koji vizualno nemaju smisla. Iako te slike sadrže mnogo uzoraka tipičnih za mačku, ništa ih ne ograničava da budu vizualno prepoznatljive.

Kako bismo poboljšali rezultat, možemo dodati još jedan član u funkciju gubitka, koji se naziva **gubitak varijacije**. To je metrika koja pokazuje koliko su slični susjedni pikseli slike. Minimiziranje gubitka varijacije čini sliku glađom i uklanja šum - otkrivajući tako vizualno privlačnije uzorke. Evo primjera takvih "idealnih" slika koje se klasificiraju kao mačka i zebra s velikom vjerojatnošću:

![Idealna mačka](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.hr.png) | ![Idealna zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.hr.png)
-----|-----
*Idealna mačka* | *Idealna zebra*

Sličan pristup može se koristiti za provođenje takozvanih **adversarijalnih napada** na neuronsku mrežu. Pretpostavimo da želimo zavarati neuronsku mrežu i učiniti da pas izgleda kao mačka. Ako uzmemo sliku psa, koju mreža prepoznaje kao psa, možemo je malo prilagoditi pomoću optimizacije gradijentnog spuštanja dok mreža ne počne klasificirati sliku kao mačku:

![Slika psa](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.hr.png) | ![Slika psa klasificirana kao mačka](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.hr.png)
-----|-----
*Izvorna slika psa* | *Slika psa klasificirana kao mačka*

Pogledajte kod za reprodukciju gore navedenih rezultata u sljedećoj bilježnici:

* [Idealna i adversarijalna mačka - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Zaključak

Koristeći prijenos učenja, možete brzo sastaviti klasifikator za zadatak klasifikacije prilagođenih objekata i postići visoku točnost. Možete vidjeti da složeniji zadaci koje sada rješavamo zahtijevaju veću računalnu snagu i ne mogu se lako riješiti na CPU-u. U sljedećoj jedinici pokušat ćemo koristiti lakšu implementaciju za treniranje istog modela koristeći manje računalne resurse, što rezultira samo malo nižom točnošću.

## 🚀 Izazov

U pripadajućim bilježnicama postoje bilješke na dnu o tome kako prijenos znanja najbolje funkcionira s donekle sličnim podacima za treniranje (možda nova vrsta životinje). Eksperimentirajte s potpuno novim vrstama slika kako biste vidjeli koliko dobro ili loše vaši modeli prijenosa znanja funkcioniraju.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Pregled i samostalno učenje

Pročitajte [TrainingTricks.md](TrainingTricks.md) kako biste produbili svoje znanje o nekim drugim načinima treniranja modela.

## [Zadatak](lab/README.md)

U ovom laboratoriju koristit ćemo stvarni [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) skup podataka o kućnim ljubimcima s 35 pasmina mačaka i pasa te ćemo izgraditi klasifikator prijenosa učenja.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.