# Etinis ir atsakingas dirbtinis intelektas

Jūs beveik baigėte šį kursą, ir tikiuosi, kad dabar aiškiai matote, jog dirbtinis intelektas (DI) yra pagrįstas daugybe formalių matematinių metodų, leidžiančių mums rasti ryšius duomenyse ir mokyti modelius atkartoti tam tikrus žmogaus elgesio aspektus. Šiuo istorijos momentu DI laikomas labai galingu įrankiu, padedančiu išgauti duomenų šablonus ir pritaikyti juos naujų problemų sprendimui.

## [Prieš paskaitą vykdomas testas](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Tačiau mokslinėje fantastikoje dažnai matome istorijas, kuriose DI kelia pavojų žmonijai. Paprastai tokios istorijos sukasi apie tam tikrą DI maištą, kai DI nusprendžia priešintis žmonėms. Tai reiškia, kad DI turi tam tikras emocijas arba gali priimti sprendimus, kurių kūrėjai nenumatė.

DI, apie kurį mokėmės šiame kurse, yra ne kas kita, kaip didelė matricų aritmetika. Tai labai galingas įrankis, padedantis mums spręsti problemas, ir kaip bet kuris kitas galingas įrankis – jis gali būti naudojamas tiek geriems, tiek blogiems tikslams. Svarbu paminėti, kad jis gali būti *netinkamai naudojamas*.

## Atsakingo DI principai

Siekiant išvengti atsitiktinio ar tyčinio DI netinkamo naudojimo, „Microsoft“ nurodo svarbius [Atsakingo DI principus](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Šiuos principus grindžia šios sąvokos:

* **Teisingumas** susijęs su svarbia *modelių šališkumo* problema, kuri gali atsirasti naudojant šališkus duomenis mokymui. Pavyzdžiui, kai bandome prognozuoti tikimybę, kad asmuo gaus programinės įrangos kūrėjo darbą, modelis greičiausiai teiks pirmenybę vyrams – tiesiog todėl, kad mokymo duomenų rinkinys greičiausiai buvo šališkas vyrų auditorijos atžvilgiu. Turime kruopščiai subalansuoti mokymo duomenis ir tirti modelį, kad išvengtume šališkumo ir užtikrintume, jog modelis atsižvelgia į svarbesnes savybes.
* **Patikimumas ir saugumas**. Dėl savo prigimties DI modeliai gali daryti klaidas. Neuroninis tinklas grąžina tikimybes, ir mes turime tai įvertinti priimdami sprendimus. Kiekvienas modelis turi tam tikrą tikslumą ir atpažinimo rodiklį, ir mes turime tai suprasti, kad išvengtume žalos, kurią gali sukelti neteisingi patarimai.
* **Privatumas ir saugumas** turi tam tikras DI specifines implikacijas. Pavyzdžiui, kai naudojame tam tikrus duomenis modelio mokymui, šie duomenys tam tikru būdu tampa „integruoti“ į modelį. Viena vertus, tai padidina saugumą ir privatumą, kita vertus – turime prisiminti, kokiais duomenimis modelis buvo mokytas.
* **Įtrauktis** reiškia, kad mes nekuriame DI tam, kad pakeistume žmones, o tam, kad papildytume žmones ir padarytume mūsų darbą kūrybiškesnį. Tai taip pat susiję su teisingumu, nes dirbant su nepakankamai atstovaujamomis bendruomenėmis, dauguma mūsų surinktų duomenų rinkinių greičiausiai bus šališki, ir mes turime užtikrinti, kad šios bendruomenės būtų įtrauktos ir tinkamai apdorotos DI.
* **Skaidrumas**. Tai apima užtikrinimą, kad visada aiškiai nurodytume, jog naudojamas DI. Be to, kur tik įmanoma, norime naudoti DI sistemas, kurios yra *interpretuojamos*.
* **Atsakomybė**. Kai DI modeliai priima tam tikrus sprendimus, ne visada aišku, kas yra atsakingas už tuos sprendimus. Turime užtikrinti, kad suprastume, kur slypi DI sprendimų atsakomybė. Daugeliu atvejų norėtume įtraukti žmones į svarbių sprendimų priėmimo procesą, kad faktiniai žmonės būtų atsakingi.

## Atsakingo DI įrankiai

„Microsoft“ sukūrė [Atsakingo DI įrankių rinkinį](https://github.com/microsoft/responsible-ai-toolbox), kuriame yra šie įrankiai:

* Interpretacijos prietaisų skydelis (InterpretML)
* Teisingumo prietaisų skydelis (FairLearn)
* Klaidų analizės prietaisų skydelis
* Atsakingo DI prietaisų skydelis, kuris apima:

   - EconML – priežastinės analizės įrankis, orientuotas į „kas būtų, jeigu“ klausimus
   - DiCE – kontrafaktinės analizės įrankis, leidžiantis pamatyti, kokias savybes reikia pakeisti, kad būtų paveiktas modelio sprendimas

Daugiau informacijos apie DI etiką rasite [šiame pamokoje](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) apie mašininio mokymosi mokymo programą, kurioje yra užduočių.

## Apžvalga ir savarankiškas mokymasis

Pasinaudokite šiuo [mokymosi keliu](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), kad sužinotumėte daugiau apie atsakingą DI.

## [Po paskaitos vykdomas testas](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.