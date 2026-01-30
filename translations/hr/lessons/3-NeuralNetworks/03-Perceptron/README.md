# Uvod u neuronske mreže: Perceptron

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Jedan od prvih pokušaja implementacije nečega sličnog modernoj neuronskoj mreži napravio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. To je bila hardverska implementacija nazvana "Mark-1", dizajnirana za prepoznavanje primitivnih geometrijskih oblika, poput trokuta, kvadrata i krugova.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/hr/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/hr/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Slike [s Wikipedije](https://en.wikipedia.org/wiki/Perceptron)

Ulazna slika bila je predstavljena nizom od 20x20 fotoćelija, pa je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža sadržavala je jedan neuron, koji se također naziva **jedinica logičkog praga**. Težine neuronske mreže djelovale su poput potenciometara koji su zahtijevali ručno podešavanje tijekom faze treniranja.

> ✅ Potenciometar je uređaj koji omogućuje korisniku da prilagodi otpor u krugu.

> New York Times je tada pisao o perceptronu: *embrij elektroničkog računala za koje [mornarica] očekuje da će moći hodati, govoriti, vidjeti, pisati, reproducirati se i biti svjestan svog postojanja.*

## Model perceptrona

Pretpostavimo da imamo N značajki u našem modelu, u kojem slučaju ulazni vektor ima veličinu N. Perceptron je model za **binarnu klasifikaciju**, tj. može razlikovati dvije klase ulaznih podataka. Pretpostavit ćemo da za svaki ulazni vektor x izlaz našeg perceptrona može biti ili +1 ili -1, ovisno o klasi. Izlaz se računa pomoću formule:

y(x) = f(w<sup>T</sup>x)

gdje je f funkcija aktivacije koraka

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/hr/activation-func.b4924007c7ce7764.webp"/>

## Treniranje perceptrona

Da bismo trenirali perceptron, trebamo pronaći vektor težina w koji klasificira većinu vrijednosti ispravno, tj. rezultira najmanjom **pogreškom**. Ova pogreška E definirana je **kriterijem perceptrona** na sljedeći način:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdje:

* zbroj se uzima za one točke podataka za treniranje i koje rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> je ulazni podatak, a t<sub>i</sub> je ili -1 ili +1 za negativne i pozitivne primjere.

Ovaj kriterij se smatra funkcijom težina w, i trebamo ga minimizirati. Često se koristi metoda nazvana **gradijentni spust**, u kojoj počinjemo s nekim početnim težinama w<sup>(0)</sup>, a zatim u svakom koraku ažuriramo težine prema formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Ovdje je &eta; tzv. **stopa učenja**, a &nabla;E(w) označava **gradijent** E. Nakon što izračunamo gradijent, dobivamo:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

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

U ovoj lekciji naučili ste o perceptronu, koji je model za binarnu klasifikaciju, i kako ga trenirati pomoću vektora težina.

## 🚀 Izazov

Ako želite pokušati izgraditi vlastiti perceptron, isprobajte [ovu laboratorijsku vježbu na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) koja koristi [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Pregled i samostalno učenje

Da biste vidjeli kako možemo koristiti perceptron za rješavanje jednostavnih problema kao i problema iz stvarnog života, i da biste nastavili učiti - pogledajte bilježnicu [Perceptron](Perceptron.ipynb).

Evo zanimljivog [članka o perceptronima](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Zadatak](lab/README.md)

U ovoj lekciji implementirali smo perceptron za zadatak binarne klasifikacije i koristili ga za klasifikaciju između dvije rukom pisane znamenke. U ovom laboratoriju od vas se traži da riješite problem klasifikacije znamenki u potpunosti, tj. odredite koja znamenka najvjerojatnije odgovara danoj slici.

* [Upute](lab/README.md)
* [Bilježnica](lab/PerceptronMultiClass.ipynb)

---

