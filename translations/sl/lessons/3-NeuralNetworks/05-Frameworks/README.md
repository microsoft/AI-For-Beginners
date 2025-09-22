<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-25T23:53:25+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "sl"
}
-->
# Okvirji za nevronske mreže

Kot smo že spoznali, za učinkovito učenje nevronskih mrež moramo narediti dve stvari:

* Operirati na tensorjih, npr. množiti, seštevati in izračunavati funkcije, kot sta sigmoid ali softmax
* Izračunati gradient vseh izrazov, da lahko izvedemo optimizacijo z gradientnim spustom

## [Pre-učni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Medtem ko knjižnica `numpy` omogoča prvo nalogo, potrebujemo mehanizem za izračun gradientov. V [našem okviru](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), ki smo ga razvili v prejšnjem razdelku, smo morali ročno programirati vse funkcije za odvode znotraj metode `backward`, ki izvaja povratno propagacijo. Idealno bi bilo, da nam okvir omogoča izračun gradientov *kateregakoli izraza*, ki ga lahko definiramo.

Druga pomembna stvar je možnost izvajanja izračunov na GPU ali drugih specializiranih enotah, kot je [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Učenje globokih nevronskih mrež zahteva *zelo veliko* izračunov, zato je ključnega pomena, da lahko te izračune paraleliziramo na GPU-jih.

> ✅ Izraz 'paralelizirati' pomeni razdeliti izračune med več naprav.

Trenutno sta najbolj priljubljena okvira za nevronske mreže: [TensorFlow](http://TensorFlow.org) in [PyTorch](https://pytorch.org/). Oba ponujata nizkonivojski API za delo s tensorji na CPU in GPU. Poleg nizkonivojskega API-ja obstaja tudi višjenivojski API, imenovan [Keras](https://keras.io/) in [PyTorch Lightning](https://pytorchlightning.ai/).

Nizkonivojski API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
------------------|-------------------------------------|--------------------------------
Višjenivojski API | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Nizkonivojski API-ji** v obeh okvirjih omogočajo gradnjo tako imenovanih **računalniških grafov**. Ta graf definira, kako izračunati rezultat (običajno funkcijo izgube) z danimi vhodnimi parametri, in ga je mogoče prenesti na GPU za izračun, če je na voljo. Obstajajo funkcije za diferenciacijo tega računalniškega grafa in izračun gradientov, ki jih nato lahko uporabimo za optimizacijo parametrov modela.

**Višjenivojski API-ji** obravnavajo nevronske mreže kot **zaporedje slojev** in omogočajo enostavnejšo konstrukcijo večine nevronskih mrež. Učenje modela običajno zahteva pripravo podatkov in nato klic funkcije `fit`, ki opravi delo.

Višjenivojski API omogoča hitro konstrukcijo tipičnih nevronskih mrež brez skrbi za številne podrobnosti. Hkrati pa nizkonivojski API ponuja veliko več nadzora nad procesom učenja, zato se pogosto uporablja v raziskavah, ko se ukvarjamo z novimi arhitekturami nevronskih mrež.

Pomembno je tudi razumeti, da lahko oba API-ja uporabljamo skupaj, npr. lahko razvijemo svojo arhitekturo sloja mreže z nizkonivojskim API-jem in jo nato uporabimo znotraj večje mreže, ki je bila konstruirana in naučena z višjenivojskim API-jem. Lahko pa definiramo mrežo z višjenivojskim API-jem kot zaporedje slojev in nato uporabimo svoj nizkonivojski učni zanki za izvedbo optimizacije. Oba API-ja uporabljata iste osnovne koncepte in sta zasnovana tako, da dobro delujeta skupaj.

## Učenje

V tem tečaju ponujamo večino vsebine tako za PyTorch kot za TensorFlow. Izberete lahko svoj najljubši okvir in se osredotočite le na ustrezne zvezke. Če niste prepričani, kateri okvir izbrati, preberite nekaj razprav na internetu o **PyTorch vs. TensorFlow**. Lahko si tudi ogledate oba okvira, da pridobite boljše razumevanje.

Kjer je mogoče, bomo za enostavnost uporabljali višjenivojske API-je. Vendar pa verjamemo, da je pomembno razumeti, kako nevronske mreže delujejo od temeljev naprej, zato na začetku začnemo z delom z nizkonivojskim API-jem in tensorji. Če pa želite hitro začeti in ne želite porabiti veliko časa za učenje teh podrobnosti, lahko te preskočite in se takoj osredotočite na zvezke z višjenivojskim API-jem.

## ✍️ Naloge: Okvirji

Nadaljujte z učenjem v naslednjih zvezkih:

Nizkonivojski API | [TensorFlow+Keras Zvezek](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
------------------|-------------------------------------|--------------------------------
Višjenivojski API | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Ko obvladate okvirje, si poglejmo koncept prenaučenja.

# Prenaučenje

Prenaučenje je izjemno pomemben koncept v strojnem učenju, zato je zelo pomembno, da ga pravilno razumemo!

Razmislimo o naslednjem problemu približevanja 5 točk (predstavljenih z `x` na spodnjih grafih):

![linearno](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.sl.jpg) | ![prenaučeno](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.sl.jpg)
-------------------------|--------------------------
**Linearen model, 2 parametra** | **Nelinearen model, 7 parametrov**
Napaka pri učenju = 5.3 | Napaka pri učenju = 0
Napaka pri validaciji = 5.1 | Napaka pri validaciji = 20

* Na levi vidimo dobro približanje s premico. Ker je število parametrov ustrezno, model pravilno razume razporeditev točk.
* Na desni je model premočan. Ker imamo le 5 točk in model ima 7 parametrov, se lahko prilagodi tako, da gre skozi vse točke, kar povzroči, da je napaka pri učenju 0. Vendar pa to preprečuje modelu, da bi razumel pravilni vzorec podatkov, zato je napaka pri validaciji zelo visoka.

Zelo pomembno je najti pravo ravnovesje med kompleksnostjo modela (številom parametrov) in številom učnih vzorcev.

## Zakaj pride do prenaučenja

  * Premalo učnih podatkov
  * Preveč zmogljiv model
  * Preveč šuma v vhodnih podatkih

## Kako zaznati prenaučenje

Kot lahko vidite na zgornjem grafu, lahko prenaučenje zaznamo z zelo nizko napako pri učenju in visoko napako pri validaciji. Običajno med učenjem vidimo, da se napake pri učenju in validaciji zmanjšujejo, nato pa se pri neki točki napaka pri validaciji preneha zmanjševati in začne naraščati. To je znak prenaučenja in indikator, da bi morali verjetno prenehati z učenjem (ali vsaj narediti posnetek modela).

![prenaučenje](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.sl.png)

## Kako preprečiti prenaučenje

Če opazite, da pride do prenaučenja, lahko storite naslednje:

 * Povečate količino učnih podatkov
 * Zmanjšate kompleksnost modela
 * Uporabite kakšno [tehniko regularizacije](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), kot je [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), ki jo bomo obravnavali kasneje.

## Prenaučenje in kompromis med pristranskostjo in varianco

Prenaučenje je pravzaprav primer bolj splošnega problema v statistiki, imenovanega [kompromis med pristranskostjo in varianco](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Če razmislimo o možnih virih napak v našem modelu, lahko vidimo dva tipa napak:

* **Napake zaradi pristranskosti** nastanejo, ker naš algoritem ne more pravilno zajeti odnosa med učnimi podatki. To je lahko posledica dejstva, da naš model ni dovolj zmogljiv (**podnaučenje**).
* **Napake zaradi variance**, ki nastanejo, ker model približuje šum v vhodnih podatkih namesto smiselnega odnosa (**prenaučenje**).

Med učenjem se napake zaradi pristranskosti zmanjšujejo (ker se naš model uči približevati podatke), medtem ko se napake zaradi variance povečujejo. Pomembno je, da prenehamo z učenjem - bodisi ročno (ko zaznamo prenaučenje) bodisi samodejno (z uvedbo regularizacije) - da preprečimo prenaučenje.

## Zaključek

V tej lekciji ste spoznali razlike med različnimi API-ji za dva najbolj priljubljena AI okvirja, TensorFlow in PyTorch. Poleg tega ste se naučili o zelo pomembni temi, prenaučenju.

## 🚀 Izziv

V priloženih zvezkih boste našli 'naloge' na dnu; preglejte zvezke in dokončajte naloge.

## [Po-učni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Pregled & Samostojno učenje

Raziskujte naslednje teme:

- TensorFlow
- PyTorch
- Prenaučenje

Vprašajte se naslednja vprašanja:

- Kakšna je razlika med TensorFlow in PyTorch?
- Kakšna je razlika med prenaučenjem in podnaučenjem?

## [Naloga](lab/README.md)

V tej nalogi boste reševali dve klasifikacijski težavi z uporabo enoslojnih in večslojnih popolnoma povezanih mrež z uporabo PyTorch ali TensorFlow.

* [Navodila](lab/README.md)
* [Zvezek](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.