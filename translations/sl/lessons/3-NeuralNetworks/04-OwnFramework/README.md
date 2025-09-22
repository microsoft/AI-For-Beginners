<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:47:26+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže. Večplastni perceptron

V prejšnjem poglavju ste spoznali najpreprostejši model nevronske mreže - enoplastni perceptron, linearen model za klasifikacijo dveh razredov.

V tem poglavju bomo ta model razširili v bolj prilagodljiv okvir, ki nam omogoča:

* izvajanje **klasifikacije več razredov** poleg klasifikacije dveh razredov
* reševanje **regresijskih problemov** poleg klasifikacije
* ločevanje razredov, ki niso linearno ločljivi

Prav tako bomo razvili svoj modularni okvir v Pythonu, ki nam bo omogočil sestavljanje različnih arhitektur nevronskih mrež.

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalizacija strojnega učenja

Začnimo s formalizacijo problema strojnega učenja. Predpostavimo, da imamo učni podatkovni niz **X** z oznakami **Y**, in moramo zgraditi model *f*, ki bo podajal najbolj natančne napovedi. Kakovost napovedi merimo z **funkcijo izgube** ℒ. Pogosto uporabljene funkcije izgube so:

* Pri regresijskih problemih, ko moramo napovedati število, lahko uporabimo **absolutno napako** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| ali **kvadratno napako** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pri klasifikaciji uporabljamo **0-1 izgubo** (ki je v bistvu enaka **natančnosti** modela) ali **logistično izgubo**.

Pri enoplastnem perceptronu je bila funkcija *f* definirana kot linearna funkcija *f(x)=wx+b* (kjer je *w* matrika uteži, *x* vektor vhodnih značilnosti, in *b* vektor pristranskosti). Pri različnih arhitekturah nevronskih mrež lahko ta funkcija prevzame bolj zapleteno obliko.

> Pri klasifikaciji je pogosto zaželeno, da dobimo verjetnosti ustreznih razredov kot izhod mreže. Za pretvorbo poljubnih števil v verjetnosti (npr. za normalizacijo izhoda) pogosto uporabljamo funkcijo **softmax** σ, in funkcija *f* postane *f(x)=σ(wx+b)*.

V zgornji definiciji *f* sta *w* in *b* imenovana **parametra** θ=⟨*w,b*⟩. Glede na podatkovni niz ⟨**X**,**Y**⟩ lahko izračunamo skupno napako na celotnem podatkovnem nizu kot funkcijo parametrov θ.

> ✅ **Cilj učenja nevronske mreže je zmanjšati napako z spreminjanjem parametrov θ**

## Optimizacija z gradientnim spustom

Obstaja dobro poznana metoda optimizacije funkcij, imenovana **gradientni spust**. Ideja je, da lahko izračunamo odvod (v večdimenzionalnem primeru imenovan **gradient**) funkcije izgube glede na parametre in spreminjamo parametre tako, da se napaka zmanjša. To lahko formaliziramo na naslednji način:

* Inicializiramo parametre z naključnimi vrednostmi w<sup>(0)</sup>, b<sup>(0)</sup>
* Večkrat ponovimo naslednji korak:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Med učenjem naj bi se koraki optimizacije izračunavali glede na celoten podatkovni niz (spomnite se, da se izguba izračuna kot vsota skozi vse učne primere). V praksi pa vzamemo majhne dele podatkovnega niza, imenovane **miniserije**, in izračunamo gradient na podlagi podniza podatkov. Ker se podniz vsakič izbere naključno, se takšna metoda imenuje **stohastični gradientni spust** (SGD).

## Večplastni perceptroni in povratno razširjanje

Enoplastna mreža, kot smo videli zgoraj, je sposobna klasificirati linearno ločljive razrede. Za gradnjo bogatejšega modela lahko združimo več plasti mreže. Matematično to pomeni, da bo funkcija *f* imela bolj zapleteno obliko in bo izračunana v več korakih:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tukaj je α **nelinearna aktivacijska funkcija**, σ funkcija softmax, in parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritem gradientnega spusta ostane enak, vendar je izračun gradientov bolj zahteven. Glede na pravilo verižnega diferenciiranja lahko izračunamo odvode kot:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo verižnega diferenciiranja se uporablja za izračun odvoda funkcije izgube glede na parametre.

Opazimo, da je levi del vseh teh izrazov enak, zato lahko učinkovito izračunamo odvode, začenši s funkcijo izgube in gremo "nazaj" skozi računski graf. Zato se metoda učenja večplastnega perceptrona imenuje **povratno razširjanje** ali 'backprop'.

<img alt="računski graf" src="images/ComputeGraphGrad.png"/>

> TODO: navedba vira slike

> ✅ Povratno razširjanje bomo podrobneje obravnavali v našem zvezku z zgledom.

## Zaključek

V tej lekciji smo zgradili svojo knjižnico nevronskih mrež in jo uporabili za preprosto dvodimenzionalno klasifikacijsko nalogo.

## 🚀 Izziv

V priloženem zvezku boste implementirali svoj okvir za gradnjo in učenje večplastnih perceptronov. Podrobno boste lahko videli, kako delujejo sodobne nevronske mreže.

Nadaljujte z zvezkom [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) in ga preučite.

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Pregled in samostojno učenje

Povratno razširjanje je pogost algoritem, ki se uporablja v umetni inteligenci in strojnem učenju, zato je vredno [ga podrobneje preučiti](https://wikipedia.org/wiki/Backpropagation).

## [Naloga](lab/README.md)

V tej laboratorijski nalogi boste uporabili okvir, ki ste ga zgradili v tej lekciji, za reševanje klasifikacije ročno napisanih številk MNIST.

* [Navodila](lab/README.md)
* [Zvezek](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.