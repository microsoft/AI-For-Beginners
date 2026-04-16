# Trikovi za treniranje dubokog učenja

Kako neuronske mreže postaju dublje, proces njihovog treniranja postaje sve izazovniji. Jedan od glavnih problema su takozvani [nestajući gradijenti](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ili [eksplodirajući gradijenti](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ovaj članak](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) pruža dobar uvod u te probleme.

Kako bismo učinili treniranje dubokih mreža učinkovitijim, postoji nekoliko tehnika koje možemo koristiti.

## Održavanje vrijednosti u razumnom intervalu

Kako bi numerički proračuni bili stabilniji, želimo osigurati da sve vrijednosti unutar naše neuronske mreže budu u razumnom rasponu, obično [-1..1] ili [0..1]. To nije strogi zahtjev, ali priroda proračuna s pomičnim zarezom je takva da se vrijednosti različitih veličina ne mogu precizno manipulirati zajedno. Na primjer, ako zbrojimo 10<sup>-10</sup> i 10<sup>10</sup>, vjerojatno ćemo dobiti 10<sup>10</sup>, jer će manja vrijednost biti "pretvorena" u isti red veličine kao veća, čime će se mantisa izgubiti.

Većina funkcija aktivacije ima nelinearnosti oko [-1..1], pa ima smisla skalirati sve ulazne podatke na interval [-1..1] ili [0..1].

## Inicijalizacija težina

Idealno, želimo da vrijednosti ostanu u istom rasponu nakon prolaska kroz slojeve mreže. Stoga je važno inicijalizirati težine na način koji očuva distribuciju vrijednosti.

Normalna distribucija **N(0,1)** nije dobra ideja, jer ako imamo *n* ulaza, standardna devijacija izlaza bila bi *n*, a vrijednosti bi vjerojatno izašle iz intervala [0..1].

Sljedeće inicijalizacije često se koriste:

 * Uniformna distribucija -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** jamči da za ulaze sa srednjom vrijednošću nula i standardnom devijacijom 1 ista srednja vrijednost/standardna devijacija ostaje
 * **N(0,√2/(n_in+n_out))** -- takozvana **Xavier inicijalizacija** (`glorot`), pomaže održati signale u rasponu tijekom propagacije naprijed i unatrag

## Normalizacija po batchu

Čak i uz pravilnu inicijalizaciju težina, težine tijekom treniranja mogu postati proizvoljno velike ili male, čime signali izlaze iz odgovarajućeg raspona. Signale možemo vratiti u raspon korištenjem jedne od tehnika **normalizacije**. Iako ih postoji nekoliko (normalizacija težina, normalizacija sloja), najčešće se koristi normalizacija po batchu.

Ideja **normalizacije po batchu** je uzeti u obzir sve vrijednosti unutar minibatcha i provesti normalizaciju (tj. oduzeti srednju vrijednost i podijeliti sa standardnom devijacijom) na temelju tih vrijednosti. Implementira se kao sloj mreže koji provodi ovu normalizaciju nakon primjene težina, ali prije funkcije aktivacije. Kao rezultat, vjerojatno ćemo postići veću konačnu točnost i brže treniranje.

Evo [originalnog rada](https://arxiv.org/pdf/1502.03167.pdf) o normalizaciji po batchu, [objašnjenja na Wikipediji](https://en.wikipedia.org/wiki/Batch_normalization), i [dobrog uvodnog blog posta](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (i jednog [na ruskom](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zanimljiva tehnika koja uklanja određeni postotak slučajnih neurona tijekom treniranja. Također se implementira kao sloj s jednim parametrom (postotak neurona koji se uklanjaju, obično 10%-50%), a tijekom treniranja poništava slučajne elemente ulaznog vektora prije nego što ih proslijedi sljedećem sloju.

Iako ovo može zvučati kao čudna ideja, možete vidjeti učinak dropouta na treniranje klasifikatora MNIST znamenki u bilježnici [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Ubrzava treniranje i omogućuje postizanje veće točnosti u manje epoha treniranja.

Ovaj učinak može se objasniti na nekoliko načina:

 * Može se smatrati slučajnim šok faktorom za model, koji ga izvlači iz lokalnog minimuma
 * Može se smatrati *implicitnim prosjekom modela*, jer možemo reći da tijekom dropouta treniramo malo drugačiji model

> *Neki ljudi kažu da kada pijana osoba pokušava nešto naučiti, bolje će to zapamtiti sljedećeg jutra u usporedbi s trijeznom osobom, jer mozak s nekim nefunkcionalnim neuronima pokušava bolje prilagoditi kako bi shvatio značenje. Nikada nismo testirali je li to istina ili ne.*

## Sprječavanje overfittinga

Jedan od vrlo važnih aspekata dubokog učenja je sposobnost sprječavanja [overfittinga](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Iako može biti primamljivo koristiti vrlo moćan model neuronske mreže, uvijek bismo trebali balansirati broj parametara modela s brojem uzoraka za treniranje.

> Pobrinite se da razumijete koncept [overfittinga](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) koji smo ranije objasnili!

Postoji nekoliko načina za sprječavanje overfittinga:

 * Rano zaustavljanje -- kontinuirano praćenje pogreške na validacijskom skupu i zaustavljanje treniranja kada pogreška validacije počne rasti.
 * Eksplicitno smanjenje težina / Regularizacija -- dodavanje dodatne kazne funkciji gubitka za visoke apsolutne vrijednosti težina, što sprječava model da daje vrlo nestabilne rezultate
 * Prosjek modela -- treniranje nekoliko modela i zatim prosječno izračunavanje rezultata. Ovo pomaže minimizirati varijancu.
 * Dropout (Implicitni prosjek modela)

## Optimizatori / Algoritmi treniranja

Još jedan važan aspekt treniranja je odabir dobrog algoritma treniranja. Iako je klasični **gradijentni spust** razumna opcija, ponekad može biti prespor ili rezultirati drugim problemima.

U dubokom učenju koristimo **Stohastički gradijentni spust** (SGD), koji je gradijentni spust primijenjen na minibatcheve, nasumično odabrane iz skupa za treniranje. Težine se prilagođavaju pomoću ove formule:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

U **momentum SGD-u**, zadržavamo dio gradijenta iz prethodnih koraka. To je slično kao kada se krećemo negdje s inercijom, a primimo udarac u drugom smjeru, naša putanja se ne mijenja odmah, već zadržava dio originalnog kretanja. Ovdje uvodimo još jedan vektor v koji predstavlja *brzinu*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ovdje parametar γ označava u kojoj mjeri uzimamo inerciju u obzir: γ=0 odgovara klasičnom SGD-u; γ=1 je čista jednadžba kretanja.

### Adam, Adagrad, itd.

Budući da u svakom sloju množimo signale s nekom matricom W<sub>i</sub>, ovisno o ||W<sub>i</sub>||, gradijent može ili nestati i biti blizu 0, ili rasti neograničeno. To je suština problema eksplodirajućih/nestajućih gradijenata.

Jedno od rješenja ovog problema je koristiti samo smjer gradijenta u jednadžbi i ignorirati apsolutnu vrijednost, tj.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), gdje ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Ovaj algoritam se zove **Adagrad**. Ostali algoritmi koji koriste istu ideju: **RMSProp**, **Adam**

> **Adam** se smatra vrlo učinkovitim algoritmom za mnoge primjene, pa ako niste sigurni koji koristiti - koristite Adam.

### Rezanje gradijenta

Rezanje gradijenta je proširenje gore navedene ideje. Kada je ||∇ℒ|| ≤ θ, uzimamo originalni gradijent u optimizaciji težina, a kada je ||∇ℒ|| > θ - dijelimo gradijent njegovom normom. Ovdje je θ parametar, u većini slučajeva možemo uzeti θ=1 ili θ=10.

### Smanjenje stope učenja

Uspjeh treniranja često ovisi o parametru stope učenja η. Logično je pretpostaviti da veće vrijednosti η rezultiraju bržim treniranjem, što je nešto što obično želimo na početku treniranja, a zatim manje vrijednosti η omogućuju fino podešavanje mreže. Stoga, u većini slučajeva želimo smanjiti η tijekom procesa treniranja.

To se može učiniti množenjem η s nekim brojem (npr. 0.98) nakon svake epohe treniranja, ili korištenjem složenijeg **rasporeda stope učenja**.

## Različite arhitekture mreža

Odabir prave arhitekture mreže za vaš problem može biti izazovan. Obično bismo odabrali arhitekturu koja se pokazala učinkovitom za naš specifični zadatak (ili sličan). Evo [dobrog pregleda](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) arhitektura neuronskih mreža za računalni vid.

> Važno je odabrati arhitekturu koja će biti dovoljno moćna za broj uzoraka za treniranje koje imamo. Odabir previše moćnog modela može rezultirati [overfittingom](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Drugi dobar način bio bi korištenje arhitekture koja će se automatski prilagoditi potrebnoj složenosti. Do određene mjere, **ResNet** arhitektura i **Inception** su samoprilagodljive. [Više o arhitekturama za računalni vid](../07-ConvNets/CNN_Architectures.md).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.