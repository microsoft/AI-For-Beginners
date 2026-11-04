# Trikovi za treniranje dubokog učenja

Kako neuronske mreže postaju dublje, proces njihovog treniranja postaje sve izazovniji. Jedan glavni problem su tzv. [nestajuće gradijente](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ili [eksplodirajuće gradijente](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ovaj post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) pruža dobar uvod u te probleme.

Kako bismo napravili treniranje dubokih mreža učinkovitijim, postoji nekoliko tehnika koje se mogu koristiti.

## Održavanje vrijednosti u razumnom intervalU

Kako bismo učinili numerička računanja stabilnijima, želimo osigurati da su sve vrijednosti unutar naše neuronske mreže unutar razumnog raspona, obično [-1..1] ili [0..1]. To nije stroga zahtjev, ali priroda računanja s pomičnim zarezom je takva da vrijednosti različitih magnituda ne mogu biti točno obrađene zajedno. Na primjer, ako zbrojimo 10<sup>-10</sup> i 10<sup>10</sup>, vjerojatno ćemo dobiti 10<sup>10</sup>, jer će manja vrijednost biti "pretvorena" na isti red veličine kao veća, pa će mantisa biti izgubljena.

Većina funkcija aktivacije ima nelinearnosti oko [-1..1], te stoga ima smisla skalirati sve ulazne podatke na interval [-1..1] ili [0..1].

## Inicijalizacija težina

Idealno, želimo da vrijednosti budu u istom rasponu nakon prolaska kroz slojeve mreže. Stoga je važno inicijalizirati težine na način koji će očuvati distribuciju vrijednosti.

Normalna distribucija **N(0,1)** nije dobra ideja, jer ako imamo *n* ulaza, standardna devijacija izlaza bi bila *&radic;n*, i vrijednosti će vjerojatno iskoračiti iz intervala [0..1].

Sljedeće inicijalizacije se često koriste:

 * Uniformna distribucija -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** jamči da za ulaze s nulom srednje vrijednosti i standardnom devijacijom 1 ista srednja vrijednost/standardna devijacija ostaju
 * **N(0,&radic;2/(n_in+n_out))** -- tzv. **Xavier inicijalizacija** (`glorot`), pomaže zadržati signale u rasponu tijekom i naprijed i povratne propagacije

## Normalizacija batch-eva

Čak i s odgovarajućom inicijalizacijom težina, težine tijekom treniranja mogu postati proizvoljno velike ili male, i izbacivati signale iz ispravnog raspona. Signale možemo vratiti pomoću jedne od tehnika **normalizacije**. Iako ih ima nekoliko (normalizacija težina, normalizacija sloja), najčešće korištena je Batch Normalization.

Ideja **batch normalizacije** je uzeti u obzir sve vrijednosti kroz minibatch i izvesti normalizaciju (tj. oduzeti srednju vrijednost i podijeliti s standardnom devijacijom) na temelju tih vrijednosti. Implementira se kao sloj mreže koji radi ovu normalizaciju nakon primjene težina, ali prije funkcije aktivacije. Kao rezultat, vjerojatno ćemo vidjeti veću konačnu točnost i brže treniranje.

Evo [izvornog rada](https://arxiv.org/pdf/1502.03167.pdf) o batch normalizaciji, [objašnjenja na Wikipediji](https://en.wikipedia.org/wiki/Batch_normalization) i [dobrog uvodnog blog posta](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (kao i [jednog na ruskom](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zanimljiva tehnika koja uklanja određeni postotak slučajnih neurona tijekom treninga. Također se implementira kao sloj s jednim parametrom (postotak neurona za ukloniti, obično 10%-50%), i tijekom treninga slučajno nuluje elemente ulaznog vektora prije prosljeđivanja u sljedeći sloj.

Iako ovo može zvučati kao čudna ideja, možete vidjeti učinak dropouta na treniranje MNIST klasifikatora znamenki u [`Dropout.ipynb`](Dropout.ipynb) bilježnici. To ubrzava treniranje i omogućava postizanje veće točnosti u manje epoha treniranja.

Ovaj se efekt može objasniti na nekoliko načina:

 * Može se smatrati slučajnim šokiranjem modela, što nas izvlači iz lokalnog minimuma optimizacije
 * Može se smatrati *implicitnim prosjekom modela*, jer možemo reći da tijekom dropouta treniramo malo drugačiji model

> *Neki ljudi kažu da kad pijana osoba pokušava nešto naučiti, bolje će to zapamtiti sljedeće jutro u usporedbi s trijeznom osobom, jer mozak s nekim malfunkcionirajućim neuronima pokušava bolje prilagoditi hvatanju značenja. Sami to nismo testirali je li to istina ili ne.*

## Prevencija overfittinga

Jedan vrlo važan aspekt dubokog učenja je moć spriječiti [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Iako može biti primamljivo koristiti vrlo moćan model neuronske mreže, uvijek treba držati broj parametara modela u ravnoteži s brojem uzoraka za treniranje.

> Pobrinite se da razumijete koncept [overfittinga](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) koji smo ranije predstavili!

Postoji nekoliko načina za sprječavanje overfittinga:

 * Rano zaustavljanje -- kontinuirano praćenje pogreške na validacijskom skupu i zaustavljanje treniranja kada validacijska pogreška počne rasti.
 * Izričito umanjenje težina / regularizacija -- dodavanje dodatne kazne funkciji gubitka za visoke apsolutne vrijednosti težina, što sprječava model od dobivanja vrlo nestabilnih rezultata
 * Prosječenje modela -- treniranje nekoliko modela i zatim prosječenje rezultata. Ovo pomaže minimizirati varijancu.
 * Dropout (implicitno prosječenje modela)

## Optimizeri / algoritmi treniranja

Još jedan važan aspekt treniranja je odabrati dobar algoritam treniranja. Dok je klasični **gradijentni spust** razuman izbor, ponekad može biti prespor ili uzrokovati druge probleme.

U dubokom učenju koristimo **Stohastički gradijentni spust** (SGD), koji je gradijentni spust primijenjen na minibatcheve, nasumično odabrane iz skupa za treniranje. Težine se podešavaju pomoću formule:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

U **momentum SGD-u**, zadržavamo dio gradijenta iz prethodnih koraka. To je slično kao kad se nekamo krećemo s inercijom, i dobijemo udarac u drugom smjeru, trag nam se ne mijenja odmah, već zadržava dio prvotnog kretanja. Ovde uvodimo drugi vektor v koji predstavlja *brzinu*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ovdje parametar &gamma; označava do koje mjere uzimamo inerciju u obzir: &gamma;=0 odgovara klasičnom SGD-u; &gamma;=1 je čista jednadžba gibanja.

### Adam, Adagrad, itd.

Budući da u svakom sloju množimo signale matricom W<sub>i</sub>, ovisno o ||W<sub>i</sub>||, gradijent može ili umanjivati i biti blizak 0, ili rasti neograničeno. To je srž problema Exploding/Vanishing Gradienta.

Jedno od rješenja tog problema je koristiti samo smjer gradijenta u jednadžbi, ignorirajući njegovu apsolutnu vrijednost, tj.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), gdje je ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Ovaj algoritam zove se **Adagrad**. Drugi algoritmi koji koriste istu ideju su: **RMSProp**, **Adam**

> **Adam** se smatra vrlo učinkovitim algoritmom za mnoge primjene, pa ako niste sigurni kojeg koristiti - koristite Adam.

### Prigušivanje gradijenta (Gradient clipping)

Prigušivanje gradijenta je proširenje gore navedene ideje. Kada je ||&nabla;&lagran;|| &le; &theta;, smatramo originalni gradijent u optimizaciji težina, a kada je ||&nabla;&lagran;|| > &theta; - dijelimo gradijent njegovom normom. Ovdje je &theta; parametar, u većini slučajeva možemo uzeti &theta;=1 ili &theta;=10.

### Smanjenje brzine učenja

Uspjeh treniranja često ovisi o parametru brzine učenja &eta;. Logično je pretpostaviti da veće vrijednosti &eta; rezultiraju bržim treniranjem, što tipično želimo na početku treniranja, a zatim manje vrijednosti &eta; omogućavaju nam fino podešavanje mreže. Stoga u većini slučajeva želimo smanjiti &eta; tijekom treniranja.

To se može napraviti množenjem &eta; s nekim brojem (npr. 0.98) nakon svake epohe treniranja ili korištenjem složenijeg **rasporeda brzine učenja**.

## Različite arhitekture mreža

Odabir prave arhitekture mreže za vaš problem može biti izazovan. Obično bismo uzeli arhitekturu koja je dokazano učinkovita za naš specifični zadatak (ili sličan). Evo [dobar pregled](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) arhitektura neuronskih mreža za računalni vid.

> Važno je odabrati arhitekturu koja će biti dovoljno moćna za broj trening uzoraka koje imamo. Odabir previše moćnog modela može rezultirati [overfittingom](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Drugi dobar način je koristiti arhitekturu koja će se automatski prilagoditi potrebnoj složenosti. Do neke mjere, **ResNet** arhitektura i **Inception** su samopodešavajuće. [Više o arhitekturama za računalni vid](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->