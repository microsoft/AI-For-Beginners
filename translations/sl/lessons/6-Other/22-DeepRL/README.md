# Globoko okrepljeno učenje

Okrepljeno učenje (RL) velja za enega osnovnih paradigm strojnega učenja, poleg nadzorovanega in nenadzorovanega učenja. Medtem ko se pri nadzorovanem učenju zanašamo na podatkovne nabore z znanimi rezultati, je RL osnovano na **učenju skozi izkušnje**. Na primer, ko prvič vidimo računalniško igro, začnemo igrati, čeprav ne poznamo pravil, in kmalu izboljšamo svoje spretnosti zgolj z igranjem in prilagajanjem svojega vedenja.

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Za izvajanje RL potrebujemo:

* **Okolje** ali **simulator**, ki določa pravila igre. V simulatorju moramo biti sposobni izvajati poskuse in opazovati rezultate.
* Nekakšno **funkcijo nagrajevanja**, ki kaže, kako uspešen je bil naš poskus. Pri učenju igranja računalniške igre bi bila nagrada naš končni rezultat.

Na podlagi funkcije nagrajevanja moramo prilagoditi svoje vedenje in izboljšati svoje spretnosti, da bomo naslednjič igrali bolje. Glavna razlika med drugimi vrstami strojnega učenja in RL je, da pri RL običajno ne vemo, ali smo zmagali ali izgubili, dokler igre ne končamo. Zato ne moremo reči, ali je določena poteza sama po sebi dobra ali ne - nagrado prejmemo šele na koncu igre.

Med RL običajno izvedemo veliko poskusov. Pri vsakem poskusu moramo uravnotežiti med sledenjem optimalni strategiji, ki smo jo doslej osvojili (**izkoriščanje**), in raziskovanjem novih možnih stanj (**raziskovanje**).

## OpenAI Gym

Odlično orodje za RL je [OpenAI Gym](https://gym.openai.com/) - **simulacijsko okolje**, ki lahko simulira številna različna okolja, od Atari iger do fizike ravnotežja droga. To je eno najbolj priljubljenih simulacijskih okolij za treniranje algoritmov okrepljenega učenja, ki ga vzdržuje [OpenAI](https://openai.com/).

> **Note**: Vsa okolja, ki jih ponuja OpenAI Gym, si lahko ogledate [tukaj](https://gym.openai.com/envs/#classic_control).

## Uravnoteženje CartPole

Verjetno ste že videli sodobne naprave za uravnoteženje, kot so *Segway* ali *Gyroscooterji*. Te naprave se samodejno uravnotežijo z nastavljanjem svojih koles glede na signal iz pospeškomera ali žiroskopa. V tem razdelku se bomo naučili rešiti podoben problem - uravnoteženje droga. To je podobno situaciji, ko cirkusant uravnava drog na svoji roki - vendar se to uravnoteženje droga zgodi le v 1D.

Poenostavljena različica uravnoteženja je znana kot problem **CartPole**. V svetu CartPole imamo horizontalni drsnik, ki se lahko premika levo ali desno, cilj pa je uravnotežiti navpični drog na vrhu drsnika med njegovim premikanjem.

<img alt="cartpole" src="../../../../../translated_images/sl/cartpole.f52a67f27e058170.webp" width="200"/>

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

![neuravnotežen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Cilj algoritma RL je trenirati model - tako imenovano **politiko** &pi; - ki bo vrnil akcijo kot odgovor na dano stanje. Politiko lahko obravnavamo tudi kot verjetnostno, npr. za katero koli stanje *s* in akcijo *a* bo vrnila verjetnost &pi;(*a*|*s*), da bi morali izvesti *a* v stanju *s*.

## Algoritem Policy Gradients

Najbolj očiten način za modeliranje politike je ustvarjanje nevronske mreže, ki bo kot vhod prejela stanja in vrnila ustrezne akcije (ali bolje rečeno verjetnosti vseh akcij). Na nek način bi bilo to podobno običajni nalogi klasifikacije, z eno veliko razliko - vnaprej ne vemo, katere akcije bi morali izvesti pri vsakem koraku.

Ideja tukaj je oceniti te verjetnosti. Zgradimo vektor **kumulativnih nagrad**, ki prikazuje našo skupno nagrado pri vsakem koraku poskusa. Prav tako uporabimo **diskontiranje nagrad** z množenjem zgodnejših nagrad z nekim koeficientom &gamma;=0.99, da zmanjšamo vlogo zgodnejših nagrad. Nato okrepimo tiste korake vzdolž poti poskusa, ki prinašajo večje nagrade.

> Več o algoritmu Policy Gradient in njegovem delovanju si oglejte v [primeru zvezka](CartPole-RL-TF.ipynb).

## Algoritem Actor-Critic

Izboljšana različica pristopa Policy Gradients se imenuje **Actor-Critic**. Glavna ideja je, da bi nevronska mreža vrnila dve stvari:

* Politiko, ki določa, katero akcijo izvesti. Ta del se imenuje **actor**.
* Oceno skupne nagrade, ki jo lahko pričakujemo v tem stanju - ta del se imenuje **critic**.

Na nek način ta arhitektura spominja na [GAN](../../4-ComputerVision/10-GANs/README.md), kjer imamo dve mreži, ki se trenirata ena proti drugi. V modelu actor-critic actor predlaga akcijo, ki jo moramo izvesti, critic pa poskuša biti kritičen in oceniti rezultat. Vendar je naš cilj trenirati ti mreži v harmoniji.

Ker poznamo tako resnične kumulativne nagrade kot rezultate, ki jih med poskusom vrne critic, je razmeroma enostavno zgraditi funkcijo izgube, ki bo minimizirala razliko med njima. To nam daje **critic loss**. **Actor loss** lahko izračunamo z uporabo istega pristopa kot pri algoritmu Policy Gradient.

Po izvedbi enega od teh algoritmov lahko pričakujemo, da se bo naš CartPole obnašal takole:

![uravnotežen cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Vaje: Policy Gradients in Actor-Critic RL

Nadaljujte z učenjem v naslednjih zvezkih:

* [RL v TensorFlow](CartPole-RL-TF.ipynb)
* [RL v PyTorch](CartPole-RL-PyTorch.ipynb)

## Drugi RL nalogi

Okrepljeno učenje je danes hitro rastoče področje raziskav. Nekateri zanimivi primeri okrepljenega učenja so:

* Učenje računalnika igranja **Atari iger**. Izziv pri tem problemu je, da nimamo preprostega stanja, predstavljenega kot vektor, temveč posnetek zaslona - in moramo uporabiti CNN za pretvorbo slike zaslona v vektorsko značilnost ali za pridobivanje informacij o nagradi. Atari igre so na voljo v Gym.
* Učenje računalnika igranja namiznih iger, kot sta šah in Go. Nedavno so vrhunski programi, kot je **Alpha Zero**, trenirani od začetka z dvema agentoma, ki igrata drug proti drugemu in se izboljšujeta pri vsakem koraku.
* V industriji se RL uporablja za ustvarjanje sistemov za nadzor iz simulacij. Storitev, imenovana [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste), je posebej zasnovana za to.

## Zaključek

Sedaj smo se naučili, kako trenirati agente, da dosežejo dobre rezultate zgolj z zagotavljanjem funkcije nagrajevanja, ki definira želeno stanje igre, in z omogočanjem inteligentnega raziskovanja iskalnega prostora. Uspešno smo preizkusili dva algoritma in dosegli dober rezultat v razmeroma kratkem času. Vendar je to šele začetek vaše poti v RL, zato bi morali razmisliti o ločenem tečaju, če želite raziskati globlje.

## 🚀 Izziv

Raziskujte aplikacije, navedene v razdelku 'Drugi RL nalogi', in poskusite implementirati eno!

## [Naknadni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Pregled in samostojno učenje

Več o klasičnem okrepljenem učenju si preberite v našem [učnem načrtu za začetnike strojnega učenja](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Oglejte si [odličen video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ki govori o tem, kako se računalnik lahko nauči igrati Super Mario.

## Naloga: [Trenirajte Mountain Car](lab/README.md)

Vaš cilj pri tej nalogi bo trenirati drugo Gym okolje - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

