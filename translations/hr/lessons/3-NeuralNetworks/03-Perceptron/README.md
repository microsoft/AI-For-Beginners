<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:58:43+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže: Perceptron

## [Kviz prije predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Jedan od prvih pokušaja implementacije nečega sličnog modernoj neuronskoj mreži napravio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. Bila je to hardverska implementacija nazvana "Mark-1", dizajnirana za prepoznavanje primitivnih geometrijskih oblika, poput trokuta, kvadrata i krugova.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike [s Wikipedije](https://en.wikipedia.org/wiki/Perceptron)

Ulazna slika predstavljena je nizom fotocelija dimenzija 20x20, tako da je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža sadržavala je jedan neuron, koji se također naziva **jedinica logičkog praga**. Težine neuronske mreže djelovale su poput potenciometara koji su zahtijevali ručno podešavanje tijekom faze treniranja.

> ✅ Potenciometar je uređaj koji omogućuje korisniku podešavanje otpora u strujnom krugu.

> The New York Times je tada pisao o perceptronu: *embrij elektroničkog računala za koje [mornarica] očekuje da će moći hodati, govoriti, vidjeti, pisati, reproducirati se i biti svjesno svog postojanja.*

## Model perceptrona

Pretpostavimo da imamo N značajki u našem modelu, u kojem slučaju bi ulazni vektor bio vektor veličine N. Perceptron je model za **binarnu klasifikaciju**, tj. može razlikovati dvije klase ulaznih podataka. Pretpostavit ćemo da za svaki ulazni vektor x izlaz našeg perceptrona može biti ili +1 ili -1, ovisno o klasi. Izlaz će se izračunati pomoću formule:

y(x) = f(w<sup>T</sup>x)

gdje je f funkcija aktivacije koraka

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Treniranje perceptrona

Za treniranje perceptrona potrebno je pronaći vektor težina w koji klasificira većinu vrijednosti ispravno, tj. rezultira najmanjom **pogreškom**. Ova pogreška E definirana je **kriterijem perceptrona** na sljedeći način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdje:

* zbroj se uzima za one točke skupa za treniranje i koje rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> su ulazni podaci, a t<sub>i</sub> je ili -1 ili +1 za negativne i pozitivne primjere.

Ovaj kriterij se smatra funkcijom težina w, i potrebno ga je minimizirati. Često se koristi metoda nazvana **gradijentni spust**, u kojoj započinjemo s nekim početnim težinama w<sup>(0)</sup>, a zatim u svakom koraku ažuriramo težine prema formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ovdje je η tzv. **stopa učenja**, a ∇E(w) označava **gradijent** funkcije E. Nakon izračuna gradijenta, dobivamo:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritam u Pythonu izgleda ovako:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Zaključak

U ovoj lekciji naučili ste o perceptronu, koji je model za binarnu klasifikaciju, i kako ga trenirati koristeći vektor težina.

## 🚀 Izazov

Ako želite pokušati izraditi vlastiti perceptron, isprobajte [ovu radionicu na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) koja koristi [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kviz nakon predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Pregled i samostalno učenje

Da biste vidjeli kako možemo koristiti perceptron za rješavanje jednostavnih problema, kao i problema iz stvarnog života, i nastavili učiti - pogledajte bilježnicu [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Evo zanimljivog [članka o perceptronima](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Zadatak](lab/README.md)

U ovoj lekciji implementirali smo perceptron za zadatak binarne klasifikacije i koristili ga za klasifikaciju između dvije rukom pisane znamenke. U ovom laboratoriju od vas se traži da riješite problem klasifikacije znamenki u potpunosti, tj. odredite koja znamenka najvjerojatnije odgovara danoj slici.

* [Upute](lab/README.md)
* [Bilježnica](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.