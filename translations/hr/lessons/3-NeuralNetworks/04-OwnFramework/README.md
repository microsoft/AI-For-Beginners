<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:47:04+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže. Višeslojni perceptron

U prethodnom dijelu naučili ste o najjednostavnijem modelu neuronske mreže - jednoslojnom perceptronu, linearnom modelu za klasifikaciju s dvije klase.

U ovom dijelu proširit ćemo ovaj model u fleksibilniji okvir koji nam omogućuje:

* izvođenje **višeklasne klasifikacije** uz klasifikaciju s dvije klase
* rješavanje **regresijskih problema** uz klasifikaciju
* razdvajanje klasa koje nisu linearno razdvojive

Također ćemo razviti vlastiti modularni okvir u Pythonu koji će nam omogućiti konstrukciju različitih arhitektura neuronskih mreža.

## [Kviz prije predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalizacija strojnog učenja

Počnimo s formalizacijom problema strojnog učenja. Pretpostavimo da imamo skup podataka za treniranje **X** s oznakama **Y**, i trebamo izgraditi model *f* koji će davati najtočnija predviđanja. Kvaliteta predviđanja mjeri se pomoću **funkcije gubitka** ℒ. Sljedeće funkcije gubitka često se koriste:

* Za regresijske probleme, kada trebamo predvidjeti broj, možemo koristiti **apsolutnu pogrešku** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| ili **kvadratnu pogrešku** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikaciju koristimo **0-1 gubitak** (što je u suštini isto kao i **točnost** modela) ili **logistički gubitak**.

Za jednoslojni perceptron, funkcija *f* definirana je kao linearna funkcija *f(x)=wx+b* (gdje je *w* matrica težina, *x* vektor ulaznih značajki, a *b* vektor pomaka). Za različite arhitekture neuronskih mreža, ova funkcija može poprimiti složeniji oblik.

> U slučaju klasifikacije, često je poželjno dobiti vjerojatnosti odgovarajućih klasa kao izlaz mreže. Kako bismo proizvoljne brojeve pretvorili u vjerojatnosti (npr. normalizirali izlaz), često koristimo funkciju **softmax** σ, pa funkcija *f* postaje *f(x)=σ(wx+b)*.

U gore navedenoj definiciji *f*, *w* i *b* nazivaju se **parametri** θ=⟨*w,b*⟩. S obzirom na skup podataka ⟨**X**,**Y**⟩, možemo izračunati ukupnu pogrešku na cijelom skupu podataka kao funkciju parametara θ.

> ✅ **Cilj treniranja neuronske mreže je minimizirati pogrešku mijenjanjem parametara θ**

## Optimizacija gradijentnim spuštanjem

Postoji dobro poznata metoda optimizacije funkcija nazvana **gradijentno spuštanje**. Ideja je da možemo izračunati derivaciju (u višedimenzionalnom slučaju nazvanu **gradijent**) funkcije gubitka u odnosu na parametre i mijenjati parametre na način da se pogreška smanji. Ovo se može formalizirati na sljedeći način:

* Inicijalizirajte parametre nekim slučajnim vrijednostima w<sup>(0)</sup>, b<sup>(0)</sup>
* Ponavljajte sljedeći korak više puta:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijekom treniranja, koraci optimizacije trebali bi se računati uzimajući u obzir cijeli skup podataka (sjetite se da se gubitak računa kao zbroj kroz sve uzorke za treniranje). Međutim, u stvarnosti uzimamo male dijelove skupa podataka nazvane **minibatch-evi** i računamo gradijente na temelju podskupa podataka. Budući da se podskup uzima slučajno svaki put, takva metoda naziva se **stohastičko gradijentno spuštanje** (SGD).

## Višeslojni perceptroni i povratna propagacija

Jednoslojna mreža, kao što smo vidjeli, može klasificirati linearno razdvojive klase. Kako bismo izgradili bogatiji model, možemo kombinirati nekoliko slojeva mreže. Matematički, to bi značilo da funkcija *f* ima složeniji oblik i računa se u nekoliko koraka:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ovdje je α **nelinearna aktivacijska funkcija**, σ je softmax funkcija, a parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritam gradijentnog spuštanja ostaje isti, ali postaje složenije izračunati gradijente. Prema pravilu lančane derivacije, možemo izračunati derivacije kao:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo lančane derivacije koristi se za izračunavanje derivacija funkcije gubitka u odnosu na parametre.

Primijetite da je lijevi dio svih tih izraza isti, pa možemo učinkovito izračunavati derivacije počevši od funkcije gubitka i idući "unatrag" kroz računski graf. Stoga se metoda treniranja višeslojnog perceptrona naziva **povratna propagacija**, ili 'backprop'.

<img alt="računski graf" src="images/ComputeGraphGrad.png"/>

> TODO: citiranje slike

> ✅ Povratnu propagaciju obradit ćemo detaljnije u našem primjeru u bilježnici.  

## Zaključak

U ovoj lekciji izgradili smo vlastitu biblioteku za neuronske mreže i koristili je za jednostavan zadatak klasifikacije u dvodimenzionalnom prostoru.

## 🚀 Izazov

U pratećoj bilježnici implementirat ćete vlastiti okvir za izgradnju i treniranje višeslojnih perceptrona. Moći ćete detaljno vidjeti kako moderne neuronske mreže funkcioniraju.

Prijeđite na bilježnicu [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) i prođite kroz nju.

## [Kviz nakon predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Pregled i samostalno učenje

Povratna propagacija je uobičajeni algoritam koji se koristi u umjetnoj inteligenciji i strojnome učenju, vrijedan detaljnijeg proučavanja [ovdje](https://wikipedia.org/wiki/Backpropagation).

## [Zadatak](lab/README.md)

U ovom laboratoriju traži se da koristite okvir koji ste izgradili u ovoj lekciji za rješavanje klasifikacije rukom pisanih znamenki iz skupa podataka MNIST.

* [Upute](lab/README.md)
* [Bilježnica](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.