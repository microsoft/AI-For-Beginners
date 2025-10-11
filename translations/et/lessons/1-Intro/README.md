<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06ca1b0138e65b964481ae83275b270e",
  "translation_date": "2025-10-11T11:49:41+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "et"
}
-->
# Sissejuhatus tehisintellekti

![Sissejuhatuse kokkuvõte tehisintellekti teemal doodlina](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.et.png)

> Sketchnote autor: [Tomomi Imura](https://twitter.com/girlie_mac)

## [Loengu-eelne viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Tehisintellekt** on põnev teadusvaldkond, mis uurib, kuidas panna arvutid käituma intelligentselt, näiteks tegema asju, milles inimesed on osavad.

Algselt leiutas [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) arvutid, et need töötleksid numbreid kindla protseduuri ehk algoritmi järgi. Kaasaegsed arvutid, kuigi palju arenenumad kui 19. sajandil välja pakutud mudel, järgivad endiselt sama ideed kontrollitud arvutustest. Seega on võimalik programmeerida arvutit midagi tegema, kui me teame täpset sammude jada, mida eesmärgi saavutamiseks vaja on.

![Foto inimesest](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.et.png)

> Foto autor: [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Inimese vanuse määramine tema foto põhjal on ülesanne, mida ei saa selgesõnaliselt programmeerida, sest me ei tea täpselt, kuidas me seda oma peas teeme.

---

Siiski on ülesandeid, mille lahendamise viisi me ei tea täpselt. Näiteks inimese vanuse määramine tema foto põhjal. Me õpime seda kuidagi tegema, kuna oleme näinud palju erinevas vanuses inimesi, kuid me ei oska täpselt selgitada, kuidas me seda teeme, ega saa ka arvutit seda tegema programmeerida. Just sellised ülesanded on **tehisintellekti** (lühendatult AI) huviobjektiks.

✅ Mõtle mõnele ülesandele, mida saaksid arvutile delegeerida ja mis võiks AI-st kasu saada. Mõtle valdkondadele nagu rahandus, meditsiin ja kunst – kuidas need valdkonnad täna AI-st kasu saavad?

## Nõrk AI vs. Tugev AI

Nõrk AI | Tugev AI
---------------------------------------|-------------------------------------
Nõrk AI viitab tehisintellekti süsteemidele, mis on loodud ja treenitud täitma konkreetset ülesannet või kitsast ülesannete komplekti. | Tugev AI ehk üldine tehisintellekt (AGI) viitab tehisintellekti süsteemidele, millel on inimtasemel intelligentsus ja arusaamine.
Need tehisintellekti süsteemid ei ole üldiselt intelligentsed; nad on suurepärased konkreetse ülesande täitmisel, kuid neil puudub tõeline arusaamine või teadvus. | Need tehisintellekti süsteemid suudavad täita kõiki intellektuaalseid ülesandeid, mida inimene suudab, kohaneda erinevate valdkondadega ning omada teatud teadvust või eneseteadvust.
Näited nõrgast AI-st on virtuaalsed assistendid nagu Siri või Alexa, voogedastusteenuste soovitusalgoritmid ja klienditeeninduseks mõeldud vestlusrobotid. | Tugeva AI saavutamine on tehisintellekti uurimise pikaajaline eesmärk ja see nõuaks AI-süsteemide arendamist, mis suudavad mõelda, õppida, mõista ja kohaneda laia valiku ülesannete ja kontekstidega.
Nõrk AI on väga spetsialiseerunud ja tal puuduvad inimlikud kognitiivsed võimed või üldised probleemide lahendamise oskused väljaspool oma kitsast valdkonda. | Tugev AI on praegu teoreetiline kontseptsioon ja ükski AI-süsteem pole veel sellise üldise intelligentsuse tasemeni jõudnud.

Lisateabe saamiseks vaata **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Intelligentsuse definitsioon ja Turingi test

Üks probleeme terminiga **[intelligentsus](https://en.wikipedia.org/wiki/Intelligence)** on see, et sellel puudub selge definitsioon. Võib väita, et intelligentsus on seotud **abstraktse mõtlemise** või **eneseteadvusega**, kuid me ei suuda seda täpselt määratleda.

![Kassi foto](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.et.jpg)

> [Foto](https://unsplash.com/photos/75715CVEJhI) autor: [Amber Kipp](https://unsplash.com/@sadmax) Unsplashist

Et näha, kui mitmetähenduslik on termin *intelligentsus*, proovi vastata küsimusele: "Kas kass on intelligentne?" Erinevad inimesed annavad sellele küsimusele erinevaid vastuseid, kuna puudub universaalselt aktsepteeritud test, mis tõestaks väite tõesust või väärust. Ja kui sa arvad, et selline test on olemas – proovi oma kassi läbi viia IQ testist...

✅ Mõtle hetkeks, kuidas sa defineerid intelligentsust. Kas vares, kes suudab lahendada labürindi ja saada toitu, on intelligentne? Kas laps on intelligentne?

---

Kui räägime AGI-st, peame leidma viisi, kuidas kindlaks teha, kas oleme loonud tõeliselt intelligentse süsteemi. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) pakkus välja meetodi, mida nimetatakse **[Turingi testiks](https://en.wikipedia.org/wiki/Turing_test)**, mis toimib ka intelligentsuse definitsioonina. Test võrdleb antud süsteemi millegi loomupäraselt intelligentsega – reaalse inimesega, ja kuna igasugust automaatset võrdlust saab arvutiprogrammiga mööda hiilida, kasutame inimküsitlejat. Kui inimene ei suuda tekstipõhises dialoogis eristada reaalset inimest ja arvutisüsteemi, loetakse süsteem intelligentseks.

> Vestlusrobot nimega [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), mis arendati Peterburis, jõudis 2014. aastal Turingi testi läbimisele lähedale, kasutades nutikat isiksuse trikki. See teatas kohe alguses, et on 13-aastane Ukraina poiss, mis selgitas teadmiste puudumist ja mõningaid tekstilisi vastuolusid. Robot veenis 30% kohtunikest, et see on inimene pärast 5-minutilist dialoogi – see on mõõdik, mille Turing uskus, et masin suudab saavutada aastaks 2000. Siiski tuleb mõista, et see ei tähenda, et oleme loonud intelligentse süsteemi või et arvutisüsteem on inimese küsitlejat petnud – tegelikult petsid robotiloojad inimesi, mitte süsteem ise!

✅ Kas sind on kunagi vestlusrobot petnud arvama, et räägid inimesega? Kuidas see sind veenis?

## Erinevad lähenemised tehisintellektile

Kui tahame, et arvuti käituks nagu inimene, peame kuidagi modelleerima arvutis meie mõtlemisviisi. Seega peame püüdma mõista, mis teeb inimese intelligentseks.

> Selleks, et programmeerida intelligentsust masinasse, peame mõistma, kuidas meie enda otsustusprotsessid toimivad. Kui teed natuke eneseanalüüsi, mõistad, et mõned protsessid toimuvad alateadlikult – näiteks suudame eristada kassi koerast ilma sellele mõtlemata – samas kui teised protsessid hõlmavad arutlemist.

Selle probleemi lahendamiseks on kaks võimalikku lähenemist:

Ülalt-alla lähenemine (sümboolne arutlemine) | Alt-üles lähenemine (närvivõrgud)
---------------------------------------|-------------------------------------
Ülalt-alla lähenemine modelleerib viisi, kuidas inimene arutleb probleemi lahendamiseks. See hõlmab **teadmiste** hankimist inimeselt ja nende esitamist arvutile loetaval kujul. Samuti peame välja töötama viisi, kuidas modelleerida **arutlemist** arvutis. | Alt-üles lähenemine modelleerib inimese aju struktuuri, mis koosneb suurest hulgast lihtsatest üksustest, mida nimetatakse **neuroniteks**. Iga neuron toimib oma sisendite kaalutud keskmisena ja me saame treenida neuronivõrku kasulike probleemide lahendamiseks, pakkudes **treeningandmeid**.

On ka teisi võimalikke lähenemisi intelligentsusele:

* **Emergentne**, **sünergeetiline** või **multiagendi lähenemine** põhineb tõsiasjal, et keeruline intelligentne käitumine võib tekkida suure hulga lihtsate agentide vastastikmõjust. Vastavalt [evolutsioonilisele küberneetikale](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics) võib intelligentsus *tõusta* lihtsamast, reaktiivsest käitumisest *metasüsteemi ülemineku* käigus.

* **Evolutsiooniline lähenemine** või **geneetiline algoritm** on optimeerimisprotsess, mis põhineb evolutsiooni põhimõtetel.

Me käsitleme neid lähenemisi hiljem kursuse jooksul, kuid praegu keskendume kahele peamisele suunale: ülalt-alla ja alt-üles.

### Ülalt-alla lähenemine

**Ülalt-alla lähenemises** püüame modelleerida oma arutlemist. Kuna me suudame jälgida oma mõtteid, kui me arutleme, saame proovida seda protsessi formaliseerida ja programmeerida see arvutisse. Seda nimetatakse **sümboolseks arutlemiseks**.

Inimestel on tavaliselt peas mingid reeglid, mis juhivad nende otsustusprotsesse. Näiteks kui arst diagnoosib patsienti, võib ta märgata, et inimesel on palavik, ja järeldada, et kehas võib olla põletik. Rakendades suurt hulka reegleid konkreetsele probleemile, võib arst jõuda lõpliku diagnoosini.

See lähenemine tugineb suuresti **teadmiste esitusviisile** ja **arutlemisele**. Teadmiste hankimine inimspetsialistilt võib olla kõige raskem osa, sest arst ei pruugi paljudel juhtudel täpselt teada, miks ta jõuab konkreetse diagnoosini. Mõnikord tekib lahendus lihtsalt tema peas ilma selgesõnalise mõtlemiseta. Mõningaid ülesandeid, näiteks inimese vanuse määramist fotolt, ei saa üldse taandada teadmiste manipuleerimisele.

### Alt-üles lähenemine

Teise võimalusena võime proovida modelleerida meie aju kõige lihtsamaid elemente – neuroneid. Me saame arvutis luua nn **tehisnärvivõrgu** ja seejärel proovida õpetada seda probleeme lahendama, andes sellele näiteid. See protsess sarnaneb sellega, kuidas vastsündinud laps õpib oma ümbrust tundma, tehes tähelepanekuid.

✅ Tee natuke uurimistööd selle kohta, kuidas beebid õpivad. Millised on beebi aju põhielemendid?

> | Mis on ML?         |      |
> |--------------|-----------|
> | Tehisintellekti osa, mis põhineb arvuti õppimisel probleemi lahendamiseks andmete põhjal, nimetatakse **masinõppeks**. Me ei käsitle selles kursuses klassikalist masinõpet – soovitame tutvuda eraldi [Masinõppe algajatele](http://aka.ms/ml-beginners) õppekavaga. |   ![ML algajatele](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.et.png)    |

## Lühike ülevaade tehisintellekti ajaloost

Tehisintellekt sai alguse valdkonnana 20. sajandi keskel. Alguses oli sümboolne arutlemine valdav lähenemine ja see tõi kaasa mitmeid olulisi edusamme, näiteks ekspertsüsteemid – arvutiprogrammid, mis suutsid tegutseda eksperdina mõnes piiratud probleemivaldkonnas. Kuid peagi sai selgeks, et selline lähenemine ei ole hästi skaleeritav. Teadmiste hankimine eksperdilt, nende esitamine arvutis ja teadmistebaasi täpsuse säilitamine osutus väga keeruliseks ja paljudel juhtudel liiga kulukaks. See viis nn [tehisintellekti talveni](https://en.wikipedia.org/wiki/AI_winter) 1970. aastatel.

<img alt="Tehisintellekti ajaloo ülevaade" src="../../../../translated_images/history-of-ai.7e83efa70b537f5a0264357672b0884cf3a220fbafe35c65d70b2c3805f7bf5e.et.png" width="70%"/>

> Pilt autorilt [Dmitry Soshnikov](http://soshnikov.com)

Aja jooksul muutusid arvutusressursid odavamaks ja rohkem andmeid sai kättesaadavaks, mistõttu närvivõrkudel põhinevad lähenemised hakkasid näitama suurepärast jõudlust, konkureerides inimestega paljudes valdkondades, nagu arvutinägemine või kõne mõistmine. Viimase kümnendi jooksul on terminit tehisintellekt peamiselt kasutatud sünonüümina närvivõrkudele, sest enamik AI edusamme, millest me kuuleme, põhinevad neil.

Me võime jälgida, kuidas lähenemised muutusid, näiteks malemängu arvutiprogrammi loomisel:

* Varased maleprogrammid põhinesid otsingul – programm püüdis selgesõnaliselt hinnata vastase võimalikke käike teatud arvu järgnevate käikude ulatuses ja valis optimaalse käigu, lähtudes parimast positsioonist, mis mõne käiguga saavutada saab. See viis nn [alfa-beeta kärpimise](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) otsingualgoritmi väljatöötamiseni.
* Otsingustrateegiad toimivad hästi mängu lõpus, kus otsinguruum on piiratud väikese arvu võimalike käikudega. Kuid mängu alguses on otsinguruum tohutu ja algoritmi saab täiustada, õppides olemasolevatest inimeste vahel peetud mängudest. Järgnevad eksperimendid kasutasid nn [juhtumipõhist arutlemist](https://en.wikipedia.org/wiki/Case-based_reasoning), kus programm otsis teadmistebaasist juhtumeid, mis on mängu praeguse olukorraga väga sarnased.
* Kaasaegsed programmid, mis võidavad inimmängijaid, põhinevad närvivõrkudel ja [tugevdamisõppel](https://en.wikipedia.org/wiki/Reinforcement_learning), kus programmid õpivad mängima, mängides pikka aega iseenda vastu ja õppides oma vigadest – sarnaselt inimestega, kes õpivad malet mängima. Kuid arvutiprogramm suudab mängida palju rohkem mänge palju lühema ajaga ja seega õppida palju kiiremini.

✅ Tee natuke uurimistööd teiste mängude kohta, mida AI on mänginud.

Samamoodi võime näha, kuidas lähenemine “rääkivate programmide” (mis võiksid läbida Turingi testi) loomisele on muutunud:

* Sellised varased programmid nagu [Eliza](https://en.wikipedia.org/wiki/ELIZA) põhinesid väga lihtsatel grammatilistel reeglitel ja sisendlause ümberkujundamisel küsimuseks.
* Kaasaegsed assistendid, nagu Cortana, Siri või Google Assistant, on kõik hübriidsüsteemid, mis kasutavad närvivõrke kõne tekstiks teisendamiseks ja meie kavatsuste tuvastamiseks ning seejärel rakendavad mõningaid arutlusi või selgesõnalisi algoritme vajalike toimingute tegemiseks.
* Tulevikus võime oodata täielikult närvivõrkudel põhinevat mudelit, mis suudab dialoogi iseseisvalt hallata. Hiljutised GPT ja [Turing-NLG](https://www.microsoft.com/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft) närvivõrkude perekonnad näitavad selles osas suurt edu.

<img alt="Turingi testi areng" src="../../../../translated_images/turing-test-evol.4184696701293ead6de6e6441a659c62f0b119b342456987f531005f43be0b6d.et.png" width="70%"/>
> Pilt Dmitry Soshnikovilt, [foto](https://unsplash.com/photos/r8LmVbUKgns) autoriks [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Viimased AI-uuringud

Neuraalvõrkude uurimise tohutu kasv algas umbes 2010. aastal, kui avalikud suured andmekogumid muutusid kättesaadavaks. Suur pildikogu nimega [ImageNet](https://en.wikipedia.org/wiki/ImageNet), mis sisaldab umbes 14 miljonit märgistatud pilti, andis alguse [ImageNeti suuremahulise visuaalse äratundmise väljakutsele](https://image-net.org/challenges/LSVRC/).

![ILSVRC Täpsus](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Pilt autorilt [Dmitry Soshnikov](http://soshnikov.com)

2012. aastal kasutati esmakordselt [konvolutsioonilisi neuraalvõrke](../4-ComputerVision/07-ConvNets/README.md) pildiklassifikatsioonis, mis viis klassifikatsioonivigade olulise vähenemiseni (peaaegu 30%-lt 16,4%-ni). 2015. aastal saavutas Microsoft Researchi ResNet arhitektuur [inimtasemel täpsuse](https://doi.org/10.1109/ICCV.2015.123).

Sellest ajast alates on neuraalvõrgud näidanud väga edukat käitumist paljudes ülesannetes:

---

Aasta | Inimtasemel täpsus saavutatud
-----|--------
2015 | [Pildiklassifikatsioon](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Vestlusliku kõne äratundmine](https://arxiv.org/abs/1610.05256)
2018 | [Automaatne masintõlge](https://arxiv.org/abs/1803.05567) (hiina keelest inglise keelde)
2020 | [Pildiallkirjade genereerimine](https://arxiv.org/abs/2009.13682)

Viimastel aastatel oleme näinud suuri edusamme suurte keelemudelitega, nagu BERT ja GPT-3. See on peamiselt tingitud asjaolust, et üldise tekstiga andmeid on palju, mis võimaldab treenida mudeleid tekstide struktuuri ja tähenduse tabamiseks, neid üldiste tekstikogumite põhjal eeltreenida ja seejärel spetsialiseerida konkreetsemate ülesannete jaoks. Me õpime rohkem [loomuliku keele töötlemisest](../5-NLP/README.md) hiljem selles kursuses.

## 🚀 Väljakutse

Tehke internetis ringkäik, et määrata, kus teie arvates kasutatakse AI-d kõige tõhusamalt. Kas see on kaardirakenduses, kõnest tekstiks teenuses või videomängus? Uurige, kuidas süsteem on üles ehitatud.

## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Ülevaade ja iseseisev õppimine

Vaadake AI ja ML ajalugu, lugedes läbi [selle õppetunni](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Valige element selle õppetunni või käesoleva õppetunni sketšimärkmetest ja uurige seda sügavamalt, et mõista kultuurilist konteksti, mis on mõjutanud selle arengut.

**Ülesanne**: [Mängu Jam](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.