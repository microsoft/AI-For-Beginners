# Introduksjon til nevrale nettverk: Perceptron

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/5)

En av de første forsøkene på å implementere noe som ligner på et moderne nevralt nettverk ble gjort av Frank Rosenblatt fra Cornell Aeronautical Laboratory i 1957. Det var en maskinvareimplementasjon kalt "Mark-1", designet for å gjenkjenne primitive geometriske figurer, som trekanter, firkanter og sirkler.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/no/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/no/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Bilder [fra Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Et inputbilde ble representert av et 20x20 fotocelle-array, så det nevrale nettverket hadde 400 innganger og én binær utgang. Et enkelt nettverk inneholdt én nevron, også kalt en **terskellogikkenhet**. Vektene i det nevrale nettverket fungerte som potensiometre som krevde manuell justering under treningsfasen.

> ✅ Et potensiometer er en enhet som lar brukeren justere motstanden i en krets.

> The New York Times skrev om perceptron på den tiden: *embryoet til en elektronisk datamaskin som [marinen] forventer vil kunne gå, snakke, se, skrive, reprodusere seg selv og være bevisst sin egen eksistens.*

## Perceptron-modell

Anta at vi har N funksjoner i modellen vår, i så fall vil inputvektoren være en vektor av størrelse N. En perceptron er en **binær klassifiseringsmodell**, det vil si at den kan skille mellom to klasser av inputdata. Vi antar at for hver inputvektor x vil utgangen fra vår perceptron være enten +1 eller -1, avhengig av klassen. Utgangen beregnes ved hjelp av formelen:

y(x) = f(w<sup>T</sup>x)

hvor f er en stegaktiveringsfunksjon

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/no/activation-func.b4924007c7ce7764.webp"/>

## Trening av perceptron

For å trene en perceptron må vi finne en vektvektor w som klassifiserer flest mulig verdier korrekt, det vil si som resulterer i den minste **feilen**. Denne feilen E er definert av **perceptron-kriteriet** på følgende måte:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

hvor:

* summen tas over de treningsdatapunktene i som resulterer i feil klassifisering
* x<sub>i</sub> er inputdata, og t<sub>i</sub> er enten -1 eller +1 for henholdsvis negative og positive eksempler.

Dette kriteriet betraktes som en funksjon av vektene w, og vi må minimere det. Ofte brukes en metode kalt **gradient descent**, der vi starter med noen initiale vekter w<sup>(0)</sup>, og deretter oppdaterer vektene ved hver steg i henhold til formelen:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Her er &eta; den såkalte **læringsraten**, og &nabla;E(w) betegner **gradienten** av E. Etter å ha beregnet gradienten, ender vi opp med

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser slik ut:

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

## Konklusjon

I denne leksjonen lærte du om en perceptron, som er en binær klassifiseringsmodell, og hvordan du trener den ved hjelp av en vektvektor.

## 🚀 Utfordring

Hvis du vil prøve å bygge din egen perceptron, kan du prøve [dette laboratoriet på Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) som bruker [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Gjennomgang & Selvstudium

For å se hvordan vi kan bruke perceptron til å løse et lekeproblem så vel som virkelige problemer, og for å fortsette læringen - gå til [Perceptron](Perceptron.ipynb)-notatboken.

Her er en interessant [artikkel om perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) også.

## [Oppgave](lab/README.md)

I denne leksjonen har vi implementert en perceptron for en binær klassifiseringsoppgave, og vi har brukt den til å klassifisere mellom to håndskrevne sifre. I dette laboratoriet blir du bedt om å løse problemet med sifferklassifisering helt, det vil si å bestemme hvilket siffer som mest sannsynlig tilsvarer et gitt bilde.

* [Instruksjoner](lab/README.md)
* [Notatbok](lab/PerceptronMultiClass.ipynb)

---

