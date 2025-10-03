<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06ca1b0138e65b964481ae83275b270e",
  "translation_date": "2025-10-03T09:09:37+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "lt"
}
-->
# Įvadas į dirbtinį intelektą

![Santrauka apie dirbtinio intelekto įvadą piešinyje](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.lt.png)

> Piešinys sukurtas [Tomomi Imura](https://twitter.com/girlie_mac)

## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Dirbtinis intelektas** yra įdomi mokslinė disciplina, kuri tiria, kaip galime priversti kompiuterius demonstruoti intelektualų elgesį, pvz., atlikti tuos dalykus, kuriuos žmonės geba daryti geriausiai.

Iš pradžių kompiuterius išrado [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage), kad jie galėtų dirbti su skaičiais, vykdydami aiškiai apibrėžtą procedūrą – algoritmą. Šiuolaikiniai kompiuteriai, nors ir gerokai pažangesni nei originalus modelis, pasiūlytas XIX amžiuje, vis dar remiasi ta pačia kontroliuojamų skaičiavimų idėja. Todėl galima užprogramuoti kompiuterį atlikti tam tikrą užduotį, jei žinome tikslų veiksmų seką, kurią reikia atlikti norint pasiekti tikslą.

![Asmens nuotrauka](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.lt.png)

> Nuotrauka sukūrė [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Asmens amžiaus nustatymas iš jo nuotraukos yra užduotis, kurios negalima aiškiai užprogramuoti, nes mes nežinome, kaip galvoje sugalvojame skaičių, kai tai darome.

---

Tačiau yra užduočių, kurių mes aiškiai nežinome, kaip išspręsti. Pavyzdžiui, apsvarstykite asmens amžiaus nustatymą iš jo nuotraukos. Mes kažkaip išmokstame tai daryti, nes matėme daugybę skirtingo amžiaus žmonių pavyzdžių, tačiau negalime aiškiai paaiškinti, kaip tai darome, nei užprogramuoti kompiuterio tai atlikti. Būtent tokios užduotys yra įdomios **dirbtiniam intelektui** (DI).

✅ Pagalvokite apie užduotis, kurias galėtumėte perduoti kompiuteriui, kad jos būtų naudingos DI. Apsvarstykite finansų, medicinos ir meno sritis – kaip šios sritys šiandien pasinaudoja DI?

## Silpnas DI vs. Stiprus DI

Silpnas DI | Stiprus DI
---------------------------------------|-------------------------------------
Silpnas DI reiškia DI sistemas, kurios yra sukurtos ir apmokytos atlikti konkrečią užduotį arba siaurą užduočių rinkinį.|Stiprus DI, arba Dirbtinis Bendrasis Intelektas (AGI), reiškia DI sistemas, turinčias žmogaus lygio intelektą ir supratimą.
Šios DI sistemos nėra universaliai protingos; jos puikiai atlieka iš anksto apibrėžtą užduotį, tačiau neturi tikro supratimo ar sąmoningumo.|Šios DI sistemos gali atlikti bet kokią intelektualią užduotį, kurią gali atlikti žmogus, prisitaikyti prie skirtingų sričių ir turėti tam tikrą sąmoningumo ar savimonės formą.
Silpno DI pavyzdžiai yra virtualūs asistentai, tokie kaip Siri ar Alexa, rekomendacijų algoritmai, naudojami srautinio perdavimo paslaugose, ir pokalbių robotai, skirti konkrečioms klientų aptarnavimo užduotims.|Stipraus DI pasiekimas yra ilgalaikis DI tyrimų tikslas, kuris reikalautų DI sistemų, galinčių mąstyti, mokytis, suprasti ir prisitaikyti įvairiose užduotyse ir kontekstuose, kūrimo.
Silpnas DI yra labai specializuotas ir neturi žmogaus lygio kognityvinių gebėjimų ar bendro problemų sprendimo gebėjimų už savo siaurą sritį.|Stiprus DI šiuo metu yra teorinė koncepcija, ir nė viena DI sistema dar nepasiekė tokio bendro intelekto lygio.

Daugiau informacijos rasite **[Dirbtinis Bendrasis Intelektas](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Intelekto apibrėžimas ir Tiuringo testas

Viena iš problemų, susijusių su terminu **[Intelektas](https://en.wikipedia.org/wiki/Intelligence)**, yra ta, kad nėra aiškaus šio termino apibrėžimo. Galima teigti, kad intelektas yra susijęs su **abstrakčiu mąstymu** arba **savimone**, tačiau mes negalime tinkamai jo apibrėžti.

![Katės nuotrauka](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.lt.jpg)

> [Nuotrauka](https://unsplash.com/photos/75715CVEJhI) sukūrė [Amber Kipp](https://unsplash.com/@sadmax) iš Unsplash

Norėdami pamatyti termino *intelektas* dviprasmiškumą, pabandykite atsakyti į klausimą: „Ar katė yra protinga?“. Skirtingi žmonės linkę pateikti skirtingus atsakymus į šį klausimą, nes nėra visuotinai priimto testo, kuris įrodytų, kad teiginys yra teisingas arba ne. O jei manote, kad toks testas yra – pabandykite atlikti IQ testą savo katei...

✅ Pagalvokite minutę, kaip apibrėžiate intelektą. Ar varna, kuri gali išspręsti labirintą ir pasiekti maistą, yra protinga? Ar vaikas yra protingas?

---

Kalbant apie AGI, mums reikia turėti būdą, kaip nustatyti, ar sukūrėme tikrai protingą sistemą. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) pasiūlė būdą, vadinamą **[Tiuringo testu](https://en.wikipedia.org/wiki/Turing_test)**, kuris taip pat veikia kaip intelekto apibrėžimas. Testas lygina tam tikrą sistemą su kažkuo, kas yra iš esmės protinga – tikru žmogumi, ir kadangi bet kokį automatinį palyginimą galima apeiti kompiuterine programa, naudojamas žmogus tardytojas. Taigi, jei žmogus nesugeba atskirti tikro žmogaus nuo kompiuterinės sistemos tekstiniame dialoge – sistema laikoma protinga.

> Pokalbių robotas, vadinamas [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), sukurtas Sankt Peterburge, 2014 m. beveik išlaikė Tiuringo testą, naudodamas gudrų asmenybės triuką. Jis iš anksto paskelbė, kad yra 13 metų ukrainiečių berniukas, kas paaiškintų žinių trūkumą ir kai kuriuos teksto neatitikimus. Robotas įtikino 30% teisėjų, kad jis yra žmogus po 5 minučių dialogo – metriką, kurią Tiuringas tikėjo, kad mašina galės pasiekti iki 2000 m. Tačiau reikia suprasti, kad tai nereiškia, jog sukūrėme protingą sistemą arba kad kompiuterinė sistema apgavo žmogų tardytoją – sistema neapgavo žmonių, o robotų kūrėjai tai padarė!

✅ Ar kada nors buvote apgautas pokalbių roboto, manydamas, kad kalbate su žmogumi? Kaip jis jus įtikino?

## Skirtingi DI metodai

Jei norime, kad kompiuteris elgtųsi kaip žmogus, turime kažkaip modeliuoti mūsų mąstymo būdą kompiuteryje. Todėl turime pabandyti suprasti, kas daro žmogų protingą.

> Kad galėtume užprogramuoti intelektą į mašiną, turime suprasti, kaip veikia mūsų pačių sprendimų priėmimo procesai. Jei šiek tiek pasigilinsite į save, pastebėsite, kad kai kurie procesai vyksta nesąmoningai – pvz., mes galime atskirti katę nuo šuns, apie tai negalvodami – o kiti apima samprotavimą.

Yra du galimi požiūriai į šią problemą:

Viršutinis požiūris (Simbolinis samprotavimas) | Apatinis požiūris (Neuroniniai tinklai)
---------------------------------------|-------------------------------------
Viršutinis požiūris modeliuoja, kaip žmogus samprotauja spręsdamas problemą. Tai apima **žinių** išgavimą iš žmogaus ir jų pateikimą kompiuteriui suprantama forma. Taip pat reikia sukurti būdą modeliuoti **samprotavimą** kompiuteryje. | Apatinis požiūris modeliuoja žmogaus smegenų struktūrą, sudarytą iš daugybės paprastų vienetų, vadinamų **neuronais**. Kiekvienas neuronas veikia kaip svertinis vidurkis savo įėjimų, ir mes galime išmokyti neuronų tinklą spręsti naudingas problemas, pateikdami **mokymo duomenis**.

Taip pat yra keletas kitų galimų intelekto metodų:

* **Emergentinis**, **sinerginis** arba **daugiagentinis požiūris** remiasi faktu, kad sudėtingas intelektualus elgesys gali atsirasti dėl daugybės paprastų agentų sąveikos. Pagal [evoliucinę kibernetiką](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), intelektas gali *atsirasti* iš paprastesnio, reaktyvaus elgesio *metasistemos perėjimo* procese.

* **Evoliucinis požiūris**, arba **genetinis algoritmas**, yra optimizavimo procesas, pagrįstas evoliucijos principais.

Šiuos metodus nagrinėsime vėliau kurse, tačiau dabar sutelksime dėmesį į dvi pagrindines kryptis: viršutinį ir apatinį požiūrius.

### Viršutinis požiūris

Naudojant **viršutinį požiūrį**, mes bandome modeliuoti savo samprotavimą. Kadangi galime sekti savo mintis, kai samprotaujame, galime pabandyti formalizuoti šį procesą ir užprogramuoti jį kompiuteryje. Tai vadinama **simboliniu samprotavimu**.

Žmonės linkę turėti tam tikras taisykles savo galvoje, kurios vadovauja jų sprendimų priėmimo procesams. Pavyzdžiui, kai gydytojas diagnozuoja pacientą, jis arba ji gali pastebėti, kad žmogus turi karščiavimą, todėl organizme gali būti uždegimas. Taikydamas didelį taisyklių rinkinį konkrečiai problemai, gydytojas gali suformuluoti galutinę diagnozę.

Šis metodas labai priklauso nuo **žinių reprezentavimo** ir **samprotavimo**. Žinių išgavimas iš žmogaus eksperto gali būti sunkiausia dalis, nes gydytojas daugeliu atvejų nežino, kodėl jis arba ji pateikia tam tikrą diagnozę. Kartais sprendimas tiesiog atsiranda galvoje be aiškaus mąstymo. Kai kurios užduotys, pvz., asmens amžiaus nustatymas iš nuotraukos, visiškai negali būti sumažintos iki žinių manipuliavimo.

### Apatinis požiūris

Alternatyviai, galime pabandyti modeliuoti paprasčiausius elementus mūsų smegenyse – neuroną. Galime sukurti vadinamąjį **dirbtinį neuronų tinklą** kompiuteryje ir tada pabandyti išmokyti jį spręsti problemas, pateikdami pavyzdžius. Šis procesas panašus į tai, kaip naujagimis vaikas mokosi apie savo aplinką stebėdamas.

✅ Šiek tiek pasidomėkite, kaip kūdikiai mokosi. Kokie yra pagrindiniai kūdikio smegenų elementai?

> | O kaip ML?         |      |
> |--------------|-----------|
> | Dirbtinio intelekto dalis, pagrįsta kompiuterio mokymusi spręsti problemą remiantis tam tikrais duomenimis, vadinama **Mašininiu mokymusi**. Šiame kurse neaptarsime klasikinio mašininio mokymosi – nukreipiame jus į atskirą [Mašininio mokymosi pradedantiesiems](http://aka.ms/ml-beginners) mokymo programą. |   ![ML pradedantiesiems](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.lt.png)    |

## Trumpa DI istorija

Dirbtinis intelektas kaip sritis prasidėjo XX amžiaus viduryje. Iš pradžių simbolinis samprotavimas buvo vyraujantis metodas, ir jis pasiekė nemažai svarbių laimėjimų, tokių kaip ekspertų sistemos – kompiuterinės programos, galinčios veikti kaip ekspertas tam tikrose ribotose problemų srityse. Tačiau netrukus paaiškėjo, kad toks metodas nėra gerai pritaikomas. Žinių išgavimas iš eksperto, jų pateikimas kompiuteryje ir žinių bazės tikslumo palaikymas pasirodė esąs labai sudėtingas uždavinys ir per brangus daugeliu atvejų. Tai lėmė vadinamąją [DI žiemą](https://en.wikipedia.org/wiki/AI_winter) 1970-aisiais.

<img alt="Trumpa DI istorija" src="../../../../translated_images/history-of-ai.7e83efa70b537f5a0264357672b0884cf3a220fbafe35c65d70b2c3805f7bf5e.lt.png" width="70%"/>

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

Laikui bėgant, kompiuteriniai ištekliai tapo pigesni, o duomenų daugiau, todėl neuronų tinklų metodai pradėjo demonstruoti puikų našumą konkuruojant su žmonėmis daugelyje sričių, tokių kaip kompiuterinis matymas ar kalbos supratimas. Per pastarąjį dešimtmetį terminas Dirbtinis intelektas dažniausiai buvo naudojamas kaip sinonimas neuronų tinklams, nes dauguma DI sėkmių, apie kurias girdime, yra pagrįstos jais.

Galime stebėti, kaip metodai keitėsi, pavyzdžiui, kuriant šachmatų žaidimo kompiuterinę programą:

* Ankstyvos šachmatų programos buvo pagrįstos paieška – programa aiškiai bandė įvertinti galimus priešininko ėjimus tam tikram skaičiui būsimų ėjimų ir pasirinkti optimalų ėjimą, remdamasi optimaliu pozicijos, kurią galima pasiekti per kelis ėjimus, vertinimu. Tai lėmė vadinamojo [alfa-beta genėjimo](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) paieškos algoritmo kūrimą.
* Paieškos strategijos gerai veikia žaidimo pabaigoje, kai paieškos erdvė yra ribota dėl nedidelio galimų ėjimų skaičiaus. Tačiau žaidimo pradžioje paieškos erdvė yra didžiulė, ir algoritmas gali būti patobulintas mokantis iš esamų rungtynių tarp žmonių žaidėjų. Vėlesni eksperimentai naudojo vadinamąjį [atvejų pagrįstą samprotavimą](https://en.wikipedia.org/wiki/Case-based_reasoning), kai programa ieškojo atvejų žinių bazėje, labai panašių į dabartinę žaidimo poziciją.
* Šiuolaikinės programos, kurios laimi prieš žmonių žaidėjus, yra pagrįstos neuronų tinklais ir [stiprinamuoju mokymusi](https://en.wikipedia.org/wiki/Reinforcement_learning), kur programos mokosi žaisti vien tik žaisdamos ilgą laiką prieš save ir mokydamosi iš savo klaidų – panašiai kaip žmonės mokosi žaisti šachmatus. Tačiau kompiuterinė programa gali žaisti daug daugiau žaidimų per daug mažiau laiko, todėl gali mokytis daug greičiau.

✅ Šiek tiek pasidomėkite kitais žaidimais, kuriuos žaidė DI.

Panašiai galime matyti, kaip keitėsi požiūris į „kalbančių programų“ (kurios galėtų išlaikyti Tiuringo testą) kūrimą:

* Ankstyvos tokio tipo programos, tokios kaip [Eliza](https://en.wikipedia.org/wiki/ELIZA), buvo pagrįstos labai paprastomis gramatikos taisyklėmis ir įvesties sakinio performulavimu į klausimą.
* Šiuolaikiniai asistentai, tokie kaip Cortana, Siri ar Google Assistant, yra hibridinės sistemos, kurios naudoja neuronų
> Vaizdas Dmitry Soshnikov, [nuotrauka](https://unsplash.com/photos/r8LmVbUKgns) Marina Abrosimova, [Unsplash](https://unsplash.com/@abrosimova_marina_foto)

## Naujausi AI tyrimai

Didžiulis pastarųjų metų neuroninių tinklų tyrimų augimas prasidėjo apie 2010 metus, kai viešai prieinami dideli duomenų rinkiniai tapo pasiekiami. Didžiulė vaizdų kolekcija, vadinama [ImageNet](https://en.wikipedia.org/wiki/ImageNet), kurioje yra apie 14 milijonų anotuotų vaizdų, paskatino [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Tikslumas](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Vaizdas [Dmitry Soshnikov](http://soshnikov.com)

2012 metais [Konvoliuciniai neuroniniai tinklai](../4-ComputerVision/07-ConvNets/README.md) pirmą kartą buvo panaudoti vaizdų klasifikavimui, o tai ženkliai sumažino klasifikavimo klaidų skaičių (nuo beveik 30% iki 16,4%). 2015 metais „ResNet“ architektūra iš Microsoft Research [pasiekė žmogaus lygio tikslumą](https://doi.org/10.1109/ICCV.2015.123).

Nuo tada neuroniniai tinklai parodė labai sėkmingą veikimą daugelyje užduočių:

---

Metai | Pasiektas žmogaus lygis
-----|--------
2015 | [Vaizdų klasifikavimas](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Pokalbių kalbos atpažinimas](https://arxiv.org/abs/1610.05256)
2018 | [Automatinis mašininis vertimas](https://arxiv.org/abs/1803.05567) (iš kinų į anglų)
2020 | [Vaizdų antraščių generavimas](https://arxiv.org/abs/2009.13682)

Pastaraisiais metais matėme didžiulius pasiekimus su dideliais kalbos modeliais, tokiais kaip BERT ir GPT-3. Tai daugiausia įvyko dėl to, kad yra daug bendrų tekstinių duomenų, leidžiančių treniruoti modelius, kurie supranta tekstų struktūrą ir prasmę, iš anksto juos apmokyti bendruose tekstų rinkiniuose, o vėliau specializuoti šiuos modelius konkretesnėms užduotims. Daugiau apie [Natūralios kalbos apdorojimą](../5-NLP/README.md) sužinosime vėliau šiame kurse.

## 🚀 Iššūkis

Pasidairykite internete ir nustatykite, jūsų nuomone, kur AI naudojamas efektyviausiai. Ar tai žemėlapių programėlė, kalbos į tekstą paslauga, ar galbūt vaizdo žaidimas? Ištirkite, kaip sistema buvo sukurta.

## [Testas po paskaitos](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Apžvalga ir savarankiškas mokymasis

Peržiūrėkite AI ir ML istoriją, perskaitydami [šią pamoką](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Pasirinkite elementą iš sketchnoto, esančio šios pamokos viršuje arba šioje pamokoje, ir išsamiau ištirkite, kad suprastumėte kultūrinį kontekstą, kuris informavo jo evoliuciją.

**Užduotis**: [Žaidimų kūrimo maratonas](assignment.md)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.