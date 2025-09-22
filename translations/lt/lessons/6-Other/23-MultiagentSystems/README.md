<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-31T17:31:23+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "lt"
}
-->
# Daugiaveiksmės sistemos

Vienas iš galimų būdų pasiekti intelektą yra vadinamasis **emergentinis** (arba **sinerginis**) požiūris, kuris remiasi faktu, kad daugelio palyginti paprastų agentų bendras elgesys gali sukurti sudėtingesnį (arba protingesnį) visos sistemos elgesį. Teoriškai tai grindžiama [Kolektyvinio intelekto](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentizmo](https://en.wikipedia.org/wiki/Global_brain) ir [Evoliucinės kibernetikos](https://en.wikipedia.org/wiki/Global_brain) principais, kurie teigia, kad aukštesnio lygio sistemos įgyja tam tikrą pridėtinę vertę, kai tinkamai sujungiamos iš žemesnio lygio sistemų (vadinamasis *metasistemos perėjimo principas*).

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ai/quiz/45)

**Daugiaveiksmių sistemų** kryptis dirbtinio intelekto srityje atsirado 1990-aisiais kaip atsakas į interneto ir paskirstytų sistemų augimą. Viena iš klasikinių dirbtinio intelekto vadovėlių, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), nagrinėja klasikinio dirbtinio intelekto požiūrį iš daugiaveiksmių sistemų perspektyvos.

Pagrindinė daugiaveiksmių sistemų sąvoka yra **agentas** – subjektas, kuris egzistuoja tam tikroje **aplinkoje**, kurią jis gali suvokti ir veikti joje. Tai labai plati apibrėžtis, todėl gali būti daug skirtingų agentų tipų ir klasifikacijų:

* Pagal gebėjimą mąstyti:
   - **Reaktyvūs** agentai paprastai turi paprastą užklausos-atsako tipo elgesį
   - **Apgalvoti** agentai naudoja tam tikrą loginį mąstymą ir/arba planavimo gebėjimus
* Pagal vietą, kurioje vykdomas agento kodas:
   - **Stacionarūs** agentai veikia tam tikrame tinklo mazge
   - **Mobilūs** agentai gali perkelti savo kodą tarp tinklo mazgų
* Pagal elgesį:
   - **Pasyvūs agentai** neturi konkrečių tikslų. Tokie agentai gali reaguoti į išorinius dirgiklius, bet patys neveiks
   - **Aktyvūs agentai** turi tam tikrus tikslus, kurių siekia
   - **Kognityviniai agentai** apima sudėtingą planavimą ir mąstymą

Daugiaveiksmės sistemos šiuo metu naudojamos įvairiose srityse:

* Žaidimuose daugelis ne žaidėjo valdomų veikėjų naudoja tam tikrą dirbtinį intelektą ir gali būti laikomi protingais agentais
* Vaizdo gamyboje sudėtingų 3D scenų, kuriose dalyvauja minios, atvaizdavimas paprastai atliekamas naudojant daugiaveiksmių sistemų modeliavimą
* Sistemų modeliavime daugiaveiksmių sistemų metodas naudojamas sudėtingų modelių elgesiui imituoti. Pavyzdžiui, daugiaveiksmių sistemų metodas buvo sėkmingai naudojamas prognozuojant COVID-19 ligos plitimą visame pasaulyje. Panašus metodas gali būti naudojamas miesto eismui modeliuoti ir stebėti, kaip jis reaguoja į eismo taisyklių pokyčius.
* Sudėtingose automatizavimo sistemose kiekvienas įrenginys gali veikti kaip nepriklausomas agentas, todėl visa sistema tampa mažiau monolitinė ir atsparesnė.

Mes nesigilinsime į daugiaveiksmių sistemų detales, bet apsvarstysime vieną **daugiaveiksmių modelių** pavyzdį.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) yra daugiaveiksmių modelių kūrimo aplinka, paremta modifikuota [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programavimo kalbos versija. Ši kalba buvo sukurta mokyti vaikus programavimo pagrindų, ir ji leidžia valdyti agentą, vadinamą **vėžliu**, kuris gali judėti, palikdamas pėdsaką. Tai leidžia kurti sudėtingas geometrines figūras, kurios yra labai vizualus būdas suprasti agento elgesį.

NetLogo aplinkoje galime sukurti daug vėžlių naudodami komandą `create-turtles`. Tada galime nurodyti visiems vėžliams atlikti tam tikrus veiksmus (pvz., žemiau esančiame pavyzdyje – judėti 10 taškų į priekį):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Žinoma, nėra įdomu, kai visi vėžliai daro tą patį, todėl galime `ask` tam tikras vėžlių grupes, pvz., esančias tam tikro taško aplinkoje. Taip pat galime sukurti skirtingų *veislių* vėžlius naudodami komandą `breed [cats cat]`. Čia `cat` yra veislės pavadinimas, ir reikia nurodyti tiek vienaskaitos, tiek daugiskaitos formą, nes skirtingos komandos naudoja skirtingas formas aiškumo dėlei.

> ✅ Mes nesimokysime NetLogo kalbos detaliai – jei norite sužinoti daugiau, galite apsilankyti puikiame [Pradedančiųjų interaktyviame NetLogo žodyne](https://ccl.northwestern.edu/netlogo/bind/).

Galite [atsisiųsti](https://ccl.northwestern.edu/netlogo/download.shtml) ir įdiegti NetLogo, kad išbandytumėte.

### Modelių biblioteka

Vienas iš puikių NetLogo privalumų yra tai, kad ji turi veikiančių modelių biblioteką, kurią galite išbandyti. Eikite į **File → Models Library**, ir turėsite daugybę modelių kategorijų, iš kurių galite rinktis.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Dmitry Soshnikov modelių bibliotekos ekrano nuotrauka

Galite atidaryti vieną iš modelių, pavyzdžiui, **Biology → Flocking**.

### Pagrindiniai principai

Atidarę modelį, pateksite į pagrindinį NetLogo ekraną. Čia yra pavyzdinis modelis, kuris aprašo vilkų ir avių populiaciją, turint ribotus išteklius (žolę).

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.lt.png)

> Dmitry Soshnikov ekrano nuotrauka

Šiame ekrane galite matyti:

* **Sąsajos** skyrių, kuriame yra:
  - Pagrindinis laukas, kuriame gyvena visi agentai
  - Įvairūs valdikliai: mygtukai, slankikliai ir kt.
  - Grafikai, kuriuos galite naudoti simuliacijos parametrams rodyti
* **Kodo** skirtuką, kuriame yra redaktorius, kuriame galite rašyti NetLogo programą

Daugeliu atvejų sąsajoje bus **Setup** mygtukas, kuris inicijuoja simuliacijos būseną, ir **Go** mygtukas, kuris pradeda vykdymą. Šie mygtukai valdomi atitinkamais kodų apdorojimo blokais, kurie atrodo taip:

```
to go [
...
]
```

NetLogo pasaulį sudaro šie objektai:

* **Agentai** (vėžliai), kurie gali judėti po lauką ir atlikti veiksmus. Agentus valdote naudodami `ask turtles [...]` sintaksę, o skliausteliuose esantis kodas vykdomas visų agentų *vėžlio režimu*.
* **Lopai** yra kvadratinės lauko sritys, kuriose gyvena agentai. Galite kreiptis į visus agentus, esančius tame pačiame lape, arba galite keisti lopų spalvas ir kitas savybes. Taip pat galite `ask patches` atlikti veiksmus.
* **Stebėtojas** yra unikalus agentas, kuris valdo pasaulį. Visi mygtukų apdorojimo blokai vykdomi *stebėtojo režimu*.

> ✅ Daugiaveiksmių aplinkos grožis yra tas, kad kodas, vykdomas vėžlio arba lopų režimu, vykdomas vienu metu visų agentų lygiagrečiai. Taigi, parašę nedaug kodo ir suprogramavę individualaus agento elgesį, galite sukurti sudėtingą visos simuliacijos sistemos elgesį.

### Grupavimasis

Kaip daugiaveiksmių sistemų elgesio pavyzdį, apsvarstykime **[grupavimąsi](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Grupavimasis yra sudėtingas modelis, labai panašus į tai, kaip paukščių pulkai skraido. Stebėdami juos galite pagalvoti, kad jie laikosi tam tikro kolektyvinio algoritmo arba turi tam tikrą *kolektyvinį intelektą*. Tačiau šis sudėtingas elgesys atsiranda, kai kiekvienas individualus agentas (šiuo atveju – *paukštis*) stebi tik kitus agentus, esančius netoliese, ir laikosi trijų paprastų taisyklių:

* **Lygiavimas** – jis orientuojasi į vidutinę kaimyninių agentų kryptį
* **Sanglauda** – jis stengiasi orientuotis į vidutinę kaimynų poziciją (*tolimojo veikimo trauka*)
* **Atsiskyrimas** – kai per daug priartėja prie kitų paukščių, jis stengiasi atsitraukti (*trumpojo veikimo atstūmimas*)

Galite paleisti grupavimosi pavyzdį ir stebėti elgesį. Taip pat galite reguliuoti parametrus, pvz., *atsiskyrimo laipsnį* arba *matymo diapazoną*, kuris apibrėžia, kaip toli kiekvienas paukštis gali matyti. Atkreipkite dėmesį, kad jei sumažinsite matymo diapazoną iki 0, visi paukščiai taps akli, ir grupavimasis sustos. Jei sumažinsite atsiskyrimą iki 0, visi paukščiai susiburs į tiesią liniją.

> ✅ Pereikite į **Kodo** skirtuką ir pažiūrėkite, kur kode įgyvendintos trys grupavimosi taisyklės (lygiavimas, sanglauda ir atsiskyrimas). Atkreipkite dėmesį, kaip kreipiamasi tik į tuos agentus, kurie yra matymo lauke.

### Kiti modeliai, kuriuos verta pamatyti

Yra dar keletas įdomių modelių, kuriuos galite išbandyti:

* **Art → Fireworks** rodo, kaip fejerverkas gali būti laikomas individualių ugnies srautų kolektyviniu elgesiu
* **Social Science → Traffic Basic** ir **Social Science → Traffic Grid** rodo miesto eismo modelį 1D ir 2D tinkle su arba be šviesoforų. Kiekvienas automobilis simuliacijoje laikosi šių taisyklių:
   - Jei erdvė priešais jį tuščia – pagreitėja (iki tam tikro maksimalaus greičio)
   - Jei mato kliūtį priešais – stabdo (ir galite reguliuoti, kaip toli vairuotojas gali matyti)
* **Social Science → Party** rodo, kaip žmonės grupuojasi per kokteilių vakarėlį. Galite rasti parametrų derinį, kuris greičiausiai padidina grupės laimės lygį.

Kaip matote iš šių pavyzdžių, daugiaveiksmių sistemų modeliavimas gali būti labai naudingas būdas suprasti sudėtingos sistemos, sudarytos iš individų, kurie laikosi tos pačios ar panašios logikos, elgesį. Jis taip pat gali būti naudojamas valdyti virtualius agentus, tokius kaip [NPC](https://en.wikipedia.org/wiki/NPC) kompiuteriniuose žaidimuose arba agentus 3D animuotose pasauliuose.

## Apgalvoti agentai

Aukščiau aprašyti agentai yra labai paprasti, reaguojantys į aplinkos pokyčius naudodami tam tikrą algoritmą. Tokie agentai vadinami **reaktyviais agentais**. Tačiau kartais agentai gali mąstyti ir planuoti savo veiksmus, tokiu atveju jie vadinami **apgalvotais**.

Tipinis pavyzdys būtų asmeninis agentas, kuris gauna iš žmogaus nurodymą užsakyti atostogų kelionę. Tarkime, kad internete yra daug agentų, kurie gali jam padėti. Jis turėtų susisiekti su kitais agentais, kad sužinotų, kokie skrydžiai yra prieinami, kokios yra viešbučių kainos skirtingomis datomis, ir bandyti derėtis dėl geriausios kainos. Kai atostogų planas bus parengtas ir patvirtintas savininko, jis galės tęsti užsakymą.

Tam, kad tai atliktų, agentai turi **bendrauti**. Sėkmingam bendravimui jiems reikia:

* Tam tikrų **standartinių kalbų žinių mainams**, tokių kaip [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) ir [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Šios kalbos sukurtos remiantis [Kalbos aktų teorija](https://en.wikipedia.org/wiki/Speech_act).
* Šios kalbos taip pat turėtų apimti tam tikrus **derybų protokolus**, pagrįstus skirtingais **aukcionų tipais**.
* **Bendros ontologijos**, kad agentai galėtų remtis tais pačiais konceptais, žinodami jų semantiką
* Būdo **atrasti**, ką gali atlikti skirtingi agentai, taip pat remiantis tam tikra ontologija

Apgalvoti agentai yra daug sudėtingesni nei reaktyvūs, nes jie ne tik reaguoja į aplinkos pokyčius, bet ir turi gebėti *inicijuoti* veiksmus. Viena iš siūlomų apgalvotų agentų architektūrų yra vadinamoji Tikėjimo-Noro-Ketinimo (BDI) agento architektūra:

* **Tikėjimai** sudaro žinių rinkinį apie agento aplinką. Tai gali būti struktūrizuota kaip žinių bazė arba taisyklių rinkinys, kurį agentas gali taikyti konkrečioje situacijoje aplinkoje.
* **Norai** apibrėžia, ką agentas nori atlikti, t. y. jo tikslus. Pavyzdžiui, aukščiau minėto asmeninio asistento agento tikslas yra užsakyti kelionę, o viešbučio agento tikslas – maksimaliai padidinti pelną.
* **Ketinimai** yra konkretūs veiksmai, kuriuos agentas planuoja atlikti, kad pasiektų savo tikslus. Veiksmai paprastai keičia aplinką ir sukelia bendravimą su kitais agentais.

Yra keletas platformų, skirtų daugiaveiksmių sistemų kūrimui, tokių kaip [JADE](https://jade.tilab.com/). [Šiame straipsnyje](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) pateikiama daugiaveiksmių platformų apžvalga kartu su trumpa daugiaveiksmių sistemų istorija ir jų naudojimo scenarijais.

## Išvada

Daugiaveiksmės sistemos gali būti labai įvairios formos ir naudojamos daugelyje skirtingų sričių. 
Jos visos linkusios sutelkti dėmesį į paprastesnį individualaus agento elgesį, o sudėtingesnis visos sistemos elgesys pasiekiamas dėl **sinerginio efekto**.

## 🚀 Iššūkis

Pritaikykite šią pamoką realiame pasaulyje ir pabandykite sukurti daugiaveiksmės sistemos koncepciją, kuri galėtų išspręsti problemą. Ką, pavyzdžiui, turėtų atlikti daugiaveiksmė sistema, kad optimizuotų mokyklinio autobuso maršrutą? Kaip ji galėtų veikti kepykloje?

## [Po paskaitos: testas](https://red-field

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.