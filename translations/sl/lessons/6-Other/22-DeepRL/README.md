<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-25T23:33:25+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "sl"
}
-->
# Globoko okrepitevno učenje

Okrepitevno učenje (RL) velja za enega osnovnih paradigm strojnega učenja, poleg nadzorovanega in nenadzorovanega učenja. Medtem ko se pri nadzorovanem učenju zanašamo na podatkovne nabore z znanimi rezultati, je RL osnovano na **učenju skozi izkušnje**. Na primer, ko prvič vidimo računalniško igro, začnemo igrati, četudi ne poznamo pravil, in kmalu izboljšamo svoje sposobnosti zgolj z igranjem in prilagajanjem svojega vedenja.

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Za izvajanje RL potrebujemo:

* **Okolje** ali **simulator**, ki določa pravila igre. V simulatorju moramo biti sposobni izvajati poskuse in opazovati rezultate.
* **Funkcijo nagrajevanja**, ki kaže, kako uspešen je bil naš poskus. V primeru učenja igranja računalniške igre bi bila nagrada naš končni rezultat.

Na podlagi funkcije nagrajevanja moramo prilagoditi svoje vedenje in izboljšati svoje sposobnosti, da bomo naslednjič igrali bolje. Glavna razlika med drugimi vrstami strojnega učenja in RL je v tem, da pri RL običajno ne vemo, ali smo zmagali ali izgubili, dokler igre ne končamo. Zato ne moremo reči, ali je bila določena poteza sama po sebi dobra ali ne – nagrado prejmemo šele na koncu igre.

Med RL običajno izvedemo veliko poskusov. Pri vsakem poskusu moramo uravnotežiti med sledenjem optimalni strategiji, ki smo jo do sedaj osvojili (**izkoriščanje**), in raziskovanjem novih možnih stanj (**raziskovanje**).

## OpenAI Gym

Odlično orodje za RL je [OpenAI Gym](https://gym.openai.com/) - **simulacijsko okolje**, ki lahko simulira številna različna okolja, od Atari iger do fizike ravnotežja droga. To je eno najbolj priljubljenih simulacijskih okolij za treniranje algoritmov okrepitevnega učenja, ki ga vzdržuje [OpenAI](https://openai.com/).

> **Note**: Vsa okolja, ki jih ponuja OpenAI Gym, si lahko ogledate [tukaj](https://gym.openai.com/envs/#classic_control).

## Uravnoteženje CartPole

Verjetno ste že videli sodobne naprave za ravnotežje, kot so *Segway* ali *Gyroscooterji*. Te naprave se lahko samodejno uravnotežijo z nastavljanjem koles glede na signal iz pospeškomera ali žiroskopa. V tem poglavju se bomo naučili rešiti podoben problem – uravnoteženje droga. To je podobno situaciji, ko cirkuški artist uravnava drog na svoji roki – vendar to uravnoteženje poteka le v eni dimenziji.

Poenostavljena različica uravnoteženja je znana kot problem **CartPole**. V svetu CartPole imamo vodoravno drsno ploščo, ki se lahko premika levo ali desno, cilj pa je uravnotežiti navpični drog na vrhu drsne plošče med njenim premikanjem.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Za ustvarjanje in uporabo tega okolja potrebujemo nekaj vrstic kode v Pythonu:

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

Vsako okolje je dostopno na enak način:
* `env.reset` začne nov poskus
* `env.step` izvede simulacijski korak. Prejme **akcijo** iz **akcijskega prostora** in vrne **opazovanje** (iz opazovalnega prostora), kot tudi nagrado in zastavico za zaključek.

V zgornjem primeru izvajamo naključne akcije pri vsakem koraku, zato je življenjska doba poskusa zelo kratka:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Cilj RL algoritma je trenirati model – tako imenovano **politiko** π – ki bo vrnila akcijo kot odgovor na dano stanje. Politiko lahko obravnavamo tudi kot verjetnostno, npr. za katero koli stanje *s* in akcijo *a* bo vrnila verjetnost π(*a*|*s*), da izvedemo *a* v stanju *s*.

## Algoritem Policy Gradients

Najbolj očiten način za modeliranje politike je ustvarjanje nevronske mreže, ki bo kot vhod prejela stanja in vrnila ustrezne akcije (oziroma verjetnosti vseh akcij). Na nek način je to podobno običajni nalogi klasifikacije, z eno pomembno razliko – vnaprej ne vemo, katere akcije bi morali izvesti v vsakem koraku.

Ideja tukaj je oceniti te verjetnosti. Zgradimo vektor **kumulativnih nagrad**, ki prikazuje našo skupno nagrado v vsakem koraku poskusa. Prav tako uporabimo **diskontiranje nagrad** z množenjem zgodnejših nagrad z nekim koeficientom γ=0.99, da zmanjšamo vpliv zgodnejših nagrad. Nato okrepimo tiste korake na poti poskusa, ki prinašajo večje nagrade.

> Več o algoritmu Policy Gradient in njegovem delovanju si lahko ogledate v [primeru v beležnici](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algoritem Actor-Critic

Izboljšana različica pristopa Policy Gradients se imenuje **Actor-Critic**. Glavna ideja je, da bi nevronska mreža vrnila dve stvari:

* Politiko, ki določa, katero akcijo izvesti. Ta del se imenuje **actor**.
* Oceno skupne nagrade, ki jo lahko pričakujemo v tem stanju – ta del se imenuje **critic**.

Na nek način ta arhitektura spominja na [GAN](../../4-ComputerVision/10-GANs/README.md), kjer imamo dve mreži, ki se trenirata druga proti drugi. V modelu actor-critic actor predlaga akcijo, ki jo moramo izvesti, critic pa poskuša biti kritičen in oceniti rezultat. Naš cilj pa je, da obe mreži treniramo usklajeno.

Ker poznamo tako realne kumulativne nagrade kot rezultate, ki jih med poskusom vrne critic, je relativno enostavno zgraditi funkcijo izgube, ki bo minimizirala razliko med njima. To nam daje **izgubo critica**. **Izgubo actorja** lahko izračunamo z enakim pristopom kot pri algoritmu Policy Gradient.

Po zagonu enega od teh algoritmov lahko pričakujemo, da se bo naš CartPole obnašal takole:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Vaje: Policy Gradients in Actor-Critic RL

Nadaljujte z učenjem v naslednjih beležnicah:

* [RL v TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL v PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Drugi RL nalogi

Okrepitevno učenje je danes hitro rastoče področje raziskav. Nekateri zanimivi primeri uporabe okrepitevnega učenja so:

* Učenje računalnika igranja **Atari iger**. Izziv pri tem problemu je, da nimamo preprostega stanja, predstavljenega kot vektor, temveč posnetek zaslona – in moramo uporabiti CNN za pretvorbo slike zaslona v vektorsko predstavitev ali za pridobivanje informacij o nagradi. Atari igre so na voljo v Gym.
* Učenje računalnika igranja družabnih iger, kot sta šah in go. Nedavno so bili programi, kot je **Alpha Zero**, trenirani od začetka z dvema agentoma, ki igrata drug proti drugemu in se izboljšujeta pri vsakem koraku.
* V industriji se RL uporablja za ustvarjanje sistemov za nadzor iz simulacij. Storitev, imenovana [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste), je posebej zasnovana za to.

## Zaključek

Zdaj smo se naučili, kako trenirati agente, da dosežejo dobre rezultate zgolj z zagotavljanjem funkcije nagrajevanja, ki definira želeno stanje igre, in z omogočanjem inteligentnega raziskovanja iskalnega prostora. Uspešno smo preizkusili dva algoritma in dosegli dober rezultat v relativno kratkem času. Vendar je to šele začetek vaše poti v RL, zato bi morali razmisliti o udeležbi na ločenem tečaju, če želite raziskati to področje bolj poglobljeno.

## 🚀 Izziv

Raziskujte aplikacije, navedene v razdelku 'Drugi RL nalogi', in poskusite implementirati eno!

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Pregled in samostojno učenje

Več o klasičnem okrepitevnem učenju se naučite v našem [učnem načrtu za začetnike strojnega učenja](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Oglejte si [ta odličen video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ki govori o tem, kako se računalnik lahko nauči igrati Super Mario.

## Naloga: [Trenirajte Mountain Car](lab/README.md)

Vaš cilj pri tej nalogi je trenirati drugo Gym okolje – [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.