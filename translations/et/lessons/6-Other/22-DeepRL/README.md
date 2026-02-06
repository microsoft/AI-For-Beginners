# Sügav Tugevdusõpe

Tugevdusõpe (RL) on üks põhilisi masinõppe paradigmasid, kõrvuti juhendatud ja juhendamata õppega. Kui juhendatud õppes tugineb õpe teadaolevate tulemustega andmekogule, siis RL põhineb **õppimisel läbi tegutsemise**. Näiteks, kui me esimest korda näeme arvutimängu, hakkame seda mängima, isegi kui me reegleid ei tea, ja peagi suudame oma oskusi parandada lihtsalt mängimise ja käitumise kohandamise kaudu.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/43)

RL-i teostamiseks on vaja:

* **Keskkonda** või **simulaatorit**, mis määrab mängu reeglid. Me peaksime saama simulaatoris katseid läbi viia ja tulemusi jälgida.
* **Tasu funktsiooni**, mis näitab, kui edukas meie katse oli. Arvutimängu mängimise õppimise puhul oleks tasu meie lõplik punktisumma.

Tasu funktsiooni põhjal peaksime suutma oma käitumist kohandada ja oskusi parandada, et järgmisel korral paremini mängida. Peamine erinevus teiste masinõppe tüüpide ja RL-i vahel on see, et RL-is me tavaliselt ei tea, kas võidame või kaotame enne, kui mäng on lõppenud. Seega ei saa me öelda, kas teatud käik iseenesest on hea või mitte - tasu saame alles mängu lõpus.

RL-i käigus teeme tavaliselt palju katseid. Iga katse ajal peame tasakaalustama seni õpitud optimaalse strateegia järgimise (**kasutamine**) ja uute võimalike seisundite uurimise (**uurimine**).

## OpenAI Gym

Suurepärane tööriist RL-i jaoks on [OpenAI Gym](https://gym.openai.com/) - **simulatsioonikeskkond**, mis suudab simuleerida mitmesuguseid keskkondi, alates Atari mängudest kuni füüsikani, mis on seotud posti tasakaalustamisega. See on üks populaarsemaid simulatsioonikeskkondi tugevdusõppe algoritmide treenimiseks ja seda haldab [OpenAI](https://openai.com/).

> **Note**: Kõiki OpenAI Gym-i keskkondi saab vaadata [siin](https://gym.openai.com/envs/#classic_control).

## CartPole tasakaalustamine

Tõenäoliselt olete näinud kaasaegseid tasakaalustusseadmeid, nagu *Segway* või *güroskootrid*. Need suudavad automaatselt tasakaalu hoida, kohandades oma rattaid vastavalt signaalile, mis tuleb kiirendusmõõturilt või güroskoobilt. Selles jaotises õpime lahendama sarnast probleemi - posti tasakaalustamist. See on sarnane olukorrale, kus tsirkuseartist peab tasakaalustama posti oma käel - kuid see tasakaalustamine toimub ainult ühes dimensioonis.

Lihtsustatud versioon tasakaalustamisest on tuntud kui **CartPole** probleem. CartPole maailmas on meil horisontaalne liugur, mis saab liikuda vasakule või paremale, ja eesmärk on tasakaalustada vertikaalne post liuguri peal, kui see liigub.

<img alt="cartpole" src="../../../../../translated_images/et/cartpole.f52a67f27e058170.webp" width="200"/>

Selle keskkonna loomiseks ja kasutamiseks on vaja paar rida Python koodi:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Iga keskkonda saab kasutada täpselt samamoodi:
* `env.reset` alustab uut katset
* `env.step` teostab simulatsiooni sammu. See võtab vastu **tegevuse** **tegevusruumist** ja tagastab **vaatluse** (vaatluste ruumist), samuti tasu ja lõpetamise lipu.

Ülaltoodud näites teeme igal sammul juhusliku tegevuse, mistõttu katse eluiga on väga lühike:

![tasakaalustamata cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

RL algoritmi eesmärk on treenida mudelit - nn **poliitikat** &pi; -, mis tagastab tegevuse vastuseks antud seisundile. Samuti võime pidada poliitikat tõenäosuslikuks, st iga seisundi *s* ja tegevuse *a* puhul tagastab see tõenäosuse &pi;(*a*|*s*), et peaksime seisundis *s* tegema tegevuse *a*.

## Poliitika gradientide algoritm

Kõige ilmsem viis poliitika modelleerimiseks on luua närvivõrk, mis võtab sisendiks seisundid ja tagastab vastavad tegevused (või pigem kõigi tegevuste tõenäosused). Teatud mõttes oleks see sarnane tavalise klassifikatsiooniprobleemiga, kuid peamine erinevus seisneb selles, et me ei tea ette, milliseid tegevusi peaksime igal sammul tegema.

Idee seisneb siin tõenäosuste hindamises. Loome **kumulatiivsete tasude** vektori, mis näitab meie kogutasu igal katse sammul. Samuti rakendame **tasu diskonteerimist**, korrutades varasemad tasud koefitsiendiga &gamma;=0.99, et vähendada varasemate tasude rolli. Seejärel tugevdame neid samme katse teekonnal, mis annavad suuremaid tasusid.

> Lisateavet poliitika gradientide algoritmi kohta ja selle rakendust näete [näidispäevikus](CartPole-RL-TF.ipynb).

## Näitleja-kriitik algoritm

Poliitika gradientide lähenemise täiustatud versiooni nimetatakse **näitleja-kriitikuks**. Selle peamine idee seisneb selles, et närvivõrk treenitakse tagastama kahte asja:

* Poliitika, mis määrab, millist tegevust teha. Seda osa nimetatakse **näitlejaks**.
* Hinnang kogutasule, mida me võime selles seisundis saada - seda osa nimetatakse **kriitikuks**.

Teatud mõttes sarnaneb see arhitektuur [GAN-iga](../../4-ComputerVision/10-GANs/README.md), kus meil on kaks võrku, mis treenitakse üksteise vastu. Näitleja-kriitiku mudelis pakub näitleja välja tegevuse, mida peame tegema, ja kriitik püüab olla kriitiline ning hinnata tulemust. Kuid meie eesmärk on treenida neid võrke ühtselt.

Kuna me teame nii tegelikke kumulatiivseid tasusid kui ka kriitiku poolt katse ajal tagastatud tulemusi, on suhteliselt lihtne luua kaotuse funktsioon, mis minimeerib nendevahelist erinevust. See annaks meile **kriitiku kaotuse**. **Näitleja kaotuse** saame arvutada, kasutades sama lähenemist nagu poliitika gradientide algoritmis.

Pärast ühe neist algoritmidest käivitamist võime oodata, et meie CartPole käitub järgmiselt:

![tasakaalustav cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Harjutused: Poliitika gradientid ja näitleja-kriitik RL

Jätka õppimist järgmistes päevikutes:

* [RL TensorFlow-s](CartPole-RL-TF.ipynb)
* [RL PyTorch-is](CartPole-RL-PyTorch.ipynb)

## Muud RL ülesanded

Tugevdusõpe on tänapäeval kiiresti kasvav uurimisvaldkond. Mõned huvitavad tugevdusõppe näited on:

* Arvuti õpetamine mängima **Atari mänge**. Selle probleemi keeruline osa on see, et meil ei ole lihtsat seisundit, mis oleks esitatud vektorina, vaid pigem ekraanipilt - ja peame kasutama CNN-i, et muuta see ekraanipilt tunnuste vektoriks või eraldada tasu teave. Atari mängud on saadaval Gym-is.
* Arvuti õpetamine mängima lauamänge, nagu male ja Go. Hiljuti treeniti tipptasemel programme, nagu **Alpha Zero**, nullist, kus kaks agenti mängisid üksteise vastu ja parandasid end igal sammul.
* Tööstuses kasutatakse RL-i juhtimissüsteemide loomiseks simulatsioonist. Teenus nimega [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) on spetsiaalselt selleks loodud.

## Kokkuvõte

Oleme nüüd õppinud, kuidas treenida agente saavutama häid tulemusi lihtsalt tasu funktsiooni pakkumisega, mis määratleb mängu soovitud seisundi, ja andes neile võimaluse intelligentselt otsinguruumi uurida. Oleme edukalt proovinud kahte algoritmi ja saavutanud hea tulemuse suhteliselt lühikese aja jooksul. Kuid see on alles teie RL-i teekonna algus ja peaksite kindlasti kaaluma eraldi kursuse võtmist, kui soovite sügavamale minna.

## 🚀 Väljakutse

Uurige rakendusi, mis on loetletud jaotises "Muud RL ülesanded", ja proovige ühte neist rakendada!

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Ülevaade ja iseseisev õppimine

Lisateavet klassikalise tugevdusõppe kohta leiate meie [Masinõppe algajatele õppekavast](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Vaadake [seda suurepärast videot](https://www.youtube.com/watch?v=qv6UVOQ0F44), mis räägib, kuidas arvuti saab õppida mängima Super Mariot.

## Ülesanne: [Treeni Mountain Car](lab/README.md)

Teie eesmärk selle ülesande käigus oleks treenida teistsugust Gym keskkonda - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.