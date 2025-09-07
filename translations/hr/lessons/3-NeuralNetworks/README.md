<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:37:08+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže

![Sažetak sadržaja o uvodu u neuronske mreže u obliku crteža](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.hr.png)

Kao što smo raspravili u uvodu, jedan od načina za postizanje inteligencije je treniranje **računalnog modela** ili **umjetnog mozga**. Od sredine 20. stoljeća, istraživači su isprobavali različite matematičke modele, sve dok se u posljednjim godinama ovaj smjer nije pokazao iznimno uspješnim. Takvi matematički modeli mozga nazivaju se **neuronske mreže**.

> Ponekad se neuronske mreže nazivaju *Umjetne neuronske mreže* (Artificial Neural Networks, ANNs) kako bi se naglasilo da govorimo o modelima, a ne o stvarnim mrežama neurona.

## Strojno učenje

Neuronske mreže dio su šire discipline zvane **Strojno učenje**, čiji je cilj koristiti podatke za treniranje računalnih modela koji mogu rješavati probleme. Strojno učenje čini velik dio umjetne inteligencije, no klasično strojno učenje ne pokrivamo u ovom kurikulumu.

> Posjetite naš zasebni kurikulum **[Strojno učenje za početnike](http://github.com/microsoft/ml-for-beginners)** kako biste saznali više o klasičnom strojnome učenju.

U strojnome učenju pretpostavljamo da imamo neki skup podataka primjera **X** i odgovarajuće izlazne vrijednosti **Y**. Primjeri su često N-dimenzionalni vektori koji se sastoje od **značajki**, a izlazi se nazivaju **oznake**.

Razmotrit ćemo dva najčešća problema strojnog učenja:

* **Klasifikacija**, gdje trebamo klasificirati ulazni objekt u dvije ili više klasa.
* **Regresija**, gdje trebamo predvidjeti numeričku vrijednost za svaki od ulaznih uzoraka.

> Kada predstavljamo ulaze i izlaze kao tenzore, ulazni skup podataka je matrica veličine M×N, gdje je M broj uzoraka, a N broj značajki. Izlazne oznake Y su vektor veličine M.

U ovom kurikulumu fokusirat ćemo se samo na modele neuronskih mreža.

## Model neurona

Iz biologije znamo da naš mozak sastoji se od neuronskih stanica, od kojih svaka ima više "ulaza" (aksona) i jedan izlaz (dendrit). Aksoni i dendriti mogu provoditi električne signale, a veze između aksona i dendrita mogu pokazivati različite stupnjeve provodljivosti (kontrolirane neurotransmiterima).

![Model neurona](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.hr.jpg) | ![Model neurona](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.hr.png)
----|----
Stvarni neuron *([Slika](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) s Wikipedije)* | Umjetni neuron *(Slika autora)*

Dakle, najjednostavniji matematički model neurona sadrži nekoliko ulaza X<sub>1</sub>, ..., X<sub>N</sub> i jedan izlaz Y, te niz težinskih vrijednosti W<sub>1</sub>, ..., W<sub>N</sub>. Izlaz se računa kao:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

gdje je f neka nelinearna **funkcija aktivacije**.

> Rani modeli neurona opisani su u klasičnom radu [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) Warrena McCullocka i Waltera Pittsa iz 1943. godine. Donald Hebb u svojoj knjizi "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" predložio je način na koji se te mreže mogu trenirati.

## U ovom odjeljku

U ovom odjeljku naučit ćemo o:
* [Perceptronu](03-Perceptron/README.md), jednom od najranijih modela neuronskih mreža za klasifikaciju s dvije klase
* [Višeslojnim mrežama](04-OwnFramework/README.md) uz prateću bilježnicu [kako izgraditi vlastiti okvir](04-OwnFramework/OwnFramework.ipynb)
* [Okvirima za neuronske mreže](05-Frameworks/README.md), uz ove bilježnice: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) i [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Prenaučavanju](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva pogrešna tumačenja ili nesporazume koji proizlaze iz korištenja ovog prijevoda.