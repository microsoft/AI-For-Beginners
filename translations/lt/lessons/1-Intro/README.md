<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-31T17:47:24+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "lt"
}
-->
# Įvadas į dirbtinį intelektą

![Dirbtinio intelekto įvado turinio santrauka piešinyje](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.lt.png)

> Piešinys sukurtas [Tomomi Imura](https://twitter.com/girlie_mac)

## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Dirbtinis intelektas** yra įdomi mokslinė disciplina, kuri tiria, kaip galime priversti kompiuterius demonstruoti intelektualų elgesį, pvz., atlikti tuos dalykus, kuriuos žmonės geba daryti geriausiai.

Iš pradžių kompiuterius išrado [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage), kad jie galėtų atlikti skaičiavimus pagal aiškiai apibrėžtą procedūrą – algoritmą. Šiuolaikiniai kompiuteriai, nors ir gerokai pažangesni nei XIX amžiuje pasiūlytas modelis, vis dar remiasi ta pačia kontroliuojamų skaičiavimų idėja. Todėl galima užprogramuoti kompiuterį atlikti tam tikrą užduotį, jei žinome tikslią veiksmų seką, kurią reikia atlikti norint pasiekti tikslą.

![Asmens nuotrauka](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.lt.png)

> Nuotrauka [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Nustatyti žmogaus amžių iš jo nuotraukos yra užduotis, kurios negalima aiškiai užprogramuoti, nes mes nežinome, kaip mūsų galvoje atsiranda skaičius, kai tai darome.

---

Tačiau yra užduočių, kurių mes nežinome, kaip aiškiai išspręsti. Pavyzdžiui, nustatyti žmogaus amžių iš jo nuotraukos. Mes kažkaip išmokstame tai daryti, nes matėme daug įvairaus amžiaus žmonių pavyzdžių, tačiau negalime aiškiai paaiškinti, kaip tai darome, nei užprogramuoti kompiuterio tai atlikti. Būtent tokios užduotys domina **dirbtinį intelektą** (trumpai – DI).

✅ Pagalvokite apie užduotis, kurias galėtumėte perduoti kompiuteriui, kad jos būtų naudingos naudojant DI. Apsvarstykite finansų, medicinos ir meno sritis – kaip šios sritys šiandien naudojasi DI privalumais?

## Silpnas DI ir stiprus DI

Silpnas DI | Stiprus DI
---------------------------------------|-------------------------------------
Silpnas DI reiškia DI sistemas, kurios yra sukurtos ir apmokytos atlikti konkrečią užduotį arba siaurą užduočių rinkinį.|Stiprus DI, arba Dirbtinis Bendrasis Intelektas (AGI), reiškia DI sistemas, turinčias žmogaus lygio intelektą ir supratimą.
Šios DI sistemos nėra bendrai intelektualios; jos puikiai atlieka iš anksto apibrėžtą užduotį, tačiau neturi tikro supratimo ar sąmoningumo.|Šios DI sistemos gali atlikti bet kokią intelektualią užduotį, kurią gali atlikti žmogus, prisitaikyti prie skirtingų sričių ir turėti tam tikrą sąmoningumo ar savimonės formą.
Silpno DI pavyzdžiai yra virtualūs asistentai, tokie kaip Siri ar Alexa, rekomendacijų algoritmai, naudojami srautinio perdavimo paslaugose, ir pokalbių robotai, skirti konkrečioms klientų aptarnavimo užduotims.|Stipraus DI pasiekimas yra ilgalaikis DI tyrimų tikslas ir reikalautų sukurti DI sistemas, kurios galėtų mąstyti, mokytis, suprasti ir prisitaikyti prie įvairių užduočių ir kontekstų.
Silpnas DI yra labai specializuotas ir neturi žmogaus lygio kognityvinių gebėjimų ar bendrų problemų sprendimo galimybių už savo siaurą sritį.|Stiprus DI šiuo metu yra teorinė koncepcija, ir nė viena DI sistema dar nepasiekė šio bendrojo intelekto lygio.

Daugiau informacijos rasite **[Dirbtinis Bendrasis Intelektas](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Intelekto apibrėžimas ir Turingo testas

Viena iš problemų, susijusių su terminu **[Intelektas](https://en.wikipedia.org/wiki/Intelligence)**, yra ta, kad nėra aiškaus šio termino apibrėžimo. Galima teigti, kad intelektas yra susijęs su **abstrakčiu mąstymu** arba **savimone**, tačiau mes negalime jo tinkamai apibrėžti.

![Katės nuotrauka](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.lt.jpg)

> [Nuotrauka](https://unsplash.com/photos/75715CVEJhI) [Amber Kipp](https://unsplash.com/@sadmax) iš Unsplash

Norėdami pamatyti, koks neaiškus yra terminas *intelektas*, pabandykite atsakyti į klausimą: „Ar katė yra intelektuali?“. Skirtingi žmonės linkę pateikti skirtingus atsakymus į šį klausimą, nes nėra visuotinai priimto testo, kuris įrodytų, kad teiginys yra teisingas ar klaidingas. O jei manote, kad toks testas yra – pabandykite atlikti IQ testą savo katei...

✅ Pagalvokite minutę, kaip jūs apibrėžiate intelektą. Ar varna, kuri gali išspręsti labirintą ir pasiekti maistą, yra intelektuali? Ar vaikas yra intelektualus?

---

Kalbant apie AGI, mums reikia būdo nustatyti, ar sukūrėme tikrai intelektualią sistemą. [Alanas Turingas](https://en.wikipedia.org/wiki/Alan_Turing) pasiūlė būdą, vadinamą **[Turingo testu](https://en.wikipedia.org/wiki/Turing_test)**, kuris taip pat veikia kaip intelekto apibrėžimas. Testas lygina tam tikrą sistemą su kažkuo, kas yra iš prigimties intelektualus – tikru žmogumi, ir kadangi bet koks automatinis palyginimas gali būti apeitas kompiuterine programa, naudojamas žmogus tardytojas. Taigi, jei žmogus nesugeba atskirti tikro žmogaus nuo kompiuterinės sistemos tekstiniame dialoge – sistema laikoma intelektualia.

> Pokalbių robotas, vadinamas [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), sukurtas Sankt Peterburge, 2014 m. beveik išlaikė Turingo testą, naudodamas gudrų asmenybės triuką. Jis iš anksto paskelbė, kad yra 13 metų ukrainietis berniukas, kas paaiškintų žinių trūkumą ir tam tikrus neatitikimus tekste. Robotui pavyko įtikinti 30% teisėjų, kad jis yra žmogus po 5 minučių dialogo – metriką, kurią Turingas tikėjo, kad mašina galės pasiekti iki 2000 metų. Tačiau reikia suprasti, kad tai nereiškia, jog sukūrėme intelektualią sistemą ar kad kompiuterinė sistema apgavo žmogų tardytoją – sistema neapgavo žmonių, o veikiau robotų kūrėjai tai padarė!

✅ Ar kada nors buvote apgauti pokalbių roboto, manydami, kad kalbate su žmogumi? Kaip jis jus įtikino?

## Skirtingi DI metodai

Jei norime, kad kompiuteris elgtųsi kaip žmogus, turime kažkaip modeliuoti savo mąstymo būdą kompiuteryje. Todėl turime pabandyti suprasti, kas daro žmogų intelektualų.

> Norėdami užprogramuoti intelektą į mašiną, turime suprasti, kaip veikia mūsų pačių sprendimų priėmimo procesai. Jei šiek tiek pasigilinsite į save, pastebėsite, kad kai kurie procesai vyksta pasąmoningai – pvz., mes galime atskirti katę nuo šuns negalvodami apie tai – o kiti apima samprotavimą.

Yra du galimi požiūriai į šią problemą:

Viršutinis požiūris (Simbolinis samprotavimas) | Apatinis požiūris (Neuroniniai tinklai)
---------------------------------------|-------------------------------------
Viršutinis požiūris modeliuoja, kaip žmogus samprotauja spręsdamas problemą. Tai apima **žinių** išgavimą iš žmogaus ir jų pateikimą kompiuteriui suprantama forma. Taip pat reikia sukurti būdą modeliuoti **samprotavimą** kompiuteryje. | Apatinis požiūris modeliuoja žmogaus smegenų struktūrą, sudarytą iš daugybės paprastų vienetų, vadinamų **neuronais**. Kiekvienas neuronas veikia kaip svertinis savo įėjimų vidurkis, ir mes galime išmokyti neuronų tinklą spręsti naudingas problemas, pateikdami **mokymo duomenis**.

Taip pat yra keletas kitų galimų požiūrių į intelektą:

* **Emergentinis**, **sinerginis** arba **daugiaveiksmis požiūris** remiasi faktu, kad sudėtingas intelektualus elgesys gali atsirasti dėl daugybės paprastų agentų sąveikos. Pagal [evoliucinę kibernetiką](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), intelektas gali *atsirasti* iš paprastesnio, reaktyvaus elgesio *metasistemos perėjimo* procese.

* **Evoliucinis požiūris**, arba **genetinis algoritmas**, yra optimizavimo procesas, pagrįstas evoliucijos principais.

Šiuos požiūrius aptarsime vėliau kurse, tačiau dabar sutelksime dėmesį į dvi pagrindines kryptis: viršutinį ir apatinį požiūrį.

### Viršutinis požiūris

Naudojant **viršutinį požiūrį**, mes bandome modeliuoti savo samprotavimus. Kadangi galime sekti savo mintis, kai samprotaujame, galime pabandyti formalizuoti šį procesą ir užprogramuoti jį kompiuteryje. Tai vadinama **simboliniu samprotavimu**.

Žmonės linkę turėti tam tikras taisykles savo galvoje, kurios vadovauja jų sprendimų priėmimo procesams. Pavyzdžiui, kai gydytojas diagnozuoja pacientą, jis ar ji gali pastebėti, kad žmogus turi karščiavimą, ir todėl gali būti uždegimas organizme. Taikydamas didelį taisyklių rinkinį konkrečiai problemai, gydytojas gali nustatyti galutinę diagnozę.

Šis požiūris labai priklauso nuo **žinių atvaizdavimo** ir **samprotavimo**. Žinių išgavimas iš žmogaus eksperto gali būti sunkiausia dalis, nes gydytojas daugeliu atvejų nežino tiksliai, kodėl jis ar ji pateikia tam tikrą diagnozę. Kartais sprendimas tiesiog atsiranda jo ar jos galvoje be aiškaus mąstymo. Kai kurios užduotys, tokios kaip žmogaus amžiaus nustatymas iš nuotraukos, apskritai negali būti sumažintos iki žinių manipuliavimo.

### Apatinis požiūris

Kita vertus, galime pabandyti modeliuoti paprasčiausius mūsų smegenų elementus – neuroną. Galime sukurti vadinamąjį **dirbtinį neuronų tinklą** kompiuteryje ir tada pabandyti jį išmokyti spręsti problemas, pateikdami jam pavyzdžius. Šis procesas panašus į tai, kaip naujagimis vaikas mokosi apie savo aplinką stebėdamas.

✅ Pasidomėkite, kaip mokosi kūdikiai. Kokie yra pagrindiniai kūdikio smegenų elementai?

> | O kaip ML?         |      |
> |--------------|-----------|
> | Dirbtinio intelekto dalis, pagrįsta kompiuterio mokymusi spręsti problemą remiantis tam tikrais duomenimis, vadinama **mašininiu mokymusi**. Šiame kurse neaptarsime klasikinio mašininio mokymosi – siūlome jums atskirą [Mašininio mokymosi pradedantiesiems](http://aka.ms/ml-beginners) mokymo programą. |   ![ML pradedantiesiems](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.lt.png)    |

## Trumpa DI istorija

Dirbtinis intelektas kaip sritis pradėtas vystyti XX amžiaus viduryje. Iš pradžių simbolinis samprotavimas buvo vyraujantis požiūris, ir jis leido pasiekti nemažai svarbių laimėjimų, tokių kaip ekspertų sistemos – kompiuterinės programos, galinčios veikti kaip ekspertai tam tikrose ribotose problemų srityse. Tačiau netrukus tapo aišku, kad toks požiūris nėra gerai pritaikomas didesniam mastui. Žinių išgavimas iš eksperto, jų pateikimas kompiuteryje ir žinių bazės tikslumo palaikymas pasirodė esąs labai sudėtingas ir daugeliu atvejų per brangus procesas. Tai lėmė vadinamąją [DI žiemą](https://en.wikipedia.org/wiki/AI_winter) 1970-aisiais.

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

Laikui bėgant, kompiuteriniai resursai tapo pigesni, o duomenų kiekis išaugo, todėl neuroninių tinklų metodai pradėjo demonstruoti puikius rezultatus konkuruojant su žmonėmis daugelyje sričių, tokių kaip kompiuterinė rega ar kalbos supratimas. Per pastarąjį dešimtmetį terminas „dirbtinis intelektas“ dažniausiai buvo naudojamas kaip sinonimas neuroniniams tinklams, nes dauguma DI sėkmių, apie kurias girdime, yra pagrįstos jais.

Galime stebėti, kaip keitėsi požiūriai, pavyzdžiui, kuriant šachmatų žaidimo kompiuterinę programą:

* Ankstyvosios šachmatų programos buvo pagrįstos paieška – programa aiškiai bandė įvertinti galimus priešininko ėjimus tam tikram būsimų ėjimų skaičiui ir pasirinkti optimalų ėjimą, remdamasi geriausia pozicija, kurią galima pasiekti per kelis ėjimus. Tai lėmė vadinamojo [alfa-beta genėjimo](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) paieškos algoritmo sukūrimą.
* Paieškos strategijos gerai veikia žaidimo pabaigoje, kai paieškos erdvė yra ribota dėl nedidelio galimų ėjimų skaičiaus. Tačiau žaidimo pradžioje paieškos erdvė yra didžiulė, ir algoritmą galima patobulinti mokantis iš esamų žmonių žaidimų. Vėlesni eksperimentai naudojo vadinamąjį [atvejų pagrįstą samprotavimą](https://en.wikipedia.org/wiki/Case-based_reasoning), kai programa ieškojo atvejų žinių bazėje, labai panašių į dabartinę žaidimo poziciją.
* Šiuolaikinės programos, kurios laimi prieš žmones, yra pagrįstos neuroniniais tinklais ir [stiprinamuoju mokymusi](https://en.wikipedia.org/wiki/Reinforcement_learning), kai programos mokosi žaisti vien tik ilgą laiką žaisdamos prieš save ir mokydamosi iš savo klaidų – labai panašiai kaip žmonės mokosi žaisti šachmatais. Tačiau kompiuterinė programa gali sužaisti daug daugiau žaidimų per daug trumpesnį laiką, todėl gali mokytis daug greičiau.

✅ Pasidomėkite kitais žaidimais, kuriuos žaidė DI.

Panašiai galime matyti, kaip keitėsi požiūris į „kalbančių programų“ (kurios galėtų išlaikyti Turingo testą) kūrimą:

* Ankstyvosios tokio tipo programos, tokios kaip [Eliza](https://en.wikipedia.org/wiki/ELIZA), buvo pagrįstos labai paprastomis gramatikos taisyklėmis ir įvesties sakinio performulavimu į klausimą.
* Šiuolaikiniai asistentai, tokie kaip Cortana, Siri ar Google Assistant, yra hibridinės sistemos, kurios naudoja

> Nuotrauka Dmitry Soshnikov, [nuotrauka](https://unsplash.com/photos/r8LmVbUKgns) Marina Abrosimova, [Unsplash](https://unsplash.com/@abrosimova_marina_foto)

## Naujausi AI tyrimai

Didžiulis pastarųjų metų neuroninių tinklų tyrimų augimas prasidėjo apie 2010 metus, kai pradėjo atsirasti didelės viešos duomenų bazės. Didžiulė vaizdų kolekcija, vadinama [ImageNet](https://en.wikipedia.org/wiki/ImageNet), kurioje yra apie 14 milijonų pažymėtų vaizdų, paskatino [ImageNet didelio masto vizualinio atpažinimo konkursą](https://image-net.org/challenges/LSVRC/).

![ILSVRC Tikslumas](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Nuotrauka [Dmitry Soshnikov](http://soshnikov.com)

2012 metais [Konvoliuciniai neuroniniai tinklai](../4-ComputerVision/07-ConvNets/README.md) pirmą kartą buvo panaudoti vaizdų klasifikavimui, o tai lėmė reikšmingą klasifikavimo klaidų sumažėjimą (nuo beveik 30% iki 16,4%). 2015 metais „ResNet“ architektūra iš „Microsoft Research“ [pasiekė žmogaus lygio tikslumą](https://doi.org/10.1109/ICCV.2015.123).

Nuo to laiko neuroniniai tinklai parodė labai sėkmingą elgesį daugelyje užduočių:

---

Metai | Pasiektas žmogaus lygis
-----|--------
2015 | [Vaizdų klasifikavimas](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Pokalbių kalbos atpažinimas](https://arxiv.org/abs/1610.05256)
2018 | [Automatinis mašininis vertimas](https://arxiv.org/abs/1803.05567) (iš kinų į anglų)
2020 | [Vaizdų aprašymas](https://arxiv.org/abs/2009.13682)

Per pastaruosius kelerius metus mes stebėjome didžiules sėkmes su dideliais kalbos modeliais, tokiais kaip BERT ir GPT-3. Tai daugiausia įvyko dėl to, kad yra daug bendrųjų tekstinių duomenų, leidžiančių mokyti modelius fiksuoti tekstų struktūrą ir prasmę, iš anksto juos treniruoti su bendrosiomis tekstų kolekcijomis, o vėliau specializuoti šiuos modelius konkretesnėms užduotims. Daugiau apie [Natūralios kalbos apdorojimą](../5-NLP/README.md) sužinosime vėliau šiame kurse.

## 🚀 Iššūkis

Pasidomėkite internete, kur, jūsų nuomone, AI yra efektyviausiai naudojamas. Ar tai žemėlapių programėlė, kalbos atpažinimo paslauga ar vaizdo žaidimas? Ištyrinėkite, kaip sistema buvo sukurta.

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Peržiūra ir savarankiškas mokymasis

Peržiūrėkite AI ir ML istoriją, perskaitydami [šią pamoką](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Pasirinkite elementą iš sketchnoto šios ar kitos pamokos pradžioje ir ištyrinėkite jį giliau, kad suprastumėte kultūrinį kontekstą, kuris lėmė jo raidą.

**Užduotis**: [Žaidimų kūrimo konkursas](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.