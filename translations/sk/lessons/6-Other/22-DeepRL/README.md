# Hlboké posilňovacie učenie

Posilňovacie učenie (RL) je považované za jeden zo základných paradigmov strojového učenia, vedľa učenia s učiteľom a učenia bez učiteľa. Zatiaľ čo pri učení s učiteľom sa spoliehame na dataset so známymi výsledkami, RL je založené na **učení sa prostredníctvom skúseností**. Napríklad, keď prvýkrát vidíme počítačovú hru, začneme ju hrať, aj keď nepoznáme pravidlá, a čoskoro dokážeme zlepšiť svoje schopnosti len procesom hrania a prispôsobovania svojho správania.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Na vykonanie RL potrebujeme:

* **Prostredie** alebo **simulátor**, ktorý nastavuje pravidlá hry. Mali by sme byť schopní vykonávať experimenty v simulátore a pozorovať výsledky.
* **Funkciu odmeny**, ktorá naznačuje, ako úspešný bol náš experiment. V prípade učenia sa hrať počítačovú hru by odmenou bolo naše konečné skóre.

Na základe funkcie odmeny by sme mali byť schopní prispôsobiť svoje správanie a zlepšiť svoje schopnosti, aby sme nabudúce hrali lepšie. Hlavný rozdiel medzi inými typmi strojového učenia a RL je, že pri RL zvyčajne nevieme, či vyhráme alebo prehráme, kým nedokončíme hru. Preto nemôžeme povedať, či je určitý krok sám o sebe dobrý alebo nie - odmenu dostaneme až na konci hry.

Počas RL zvyčajne vykonávame mnoho experimentov. Počas každého experimentu musíme vyvážiť medzi nasledovaním optimálnej stratégie, ktorú sme sa doteraz naučili (**exploatácia**), a skúmaním nových možných stavov (**explorácia**).

## OpenAI Gym

Skvelým nástrojom pre RL je [OpenAI Gym](https://gym.openai.com/) - **simulačné prostredie**, ktoré dokáže simulovať mnoho rôznych prostredí, od hier Atari až po fyziku za balansovaním tyče. Je to jedno z najpopulárnejších simulačných prostredí na trénovanie algoritmov posilňovacieho učenia a je udržiavané spoločnosťou [OpenAI](https://openai.com/).

> **Note**: Všetky dostupné prostredia z OpenAI Gym si môžete pozrieť [tu](https://gym.openai.com/envs/#classic_control).

## Balansovanie CartPole

Pravdepodobne ste už videli moderné balansovacie zariadenia, ako napríklad *Segway* alebo *Gyroskútre*. Dokážu automaticky balansovať tým, že upravujú svoje kolesá na základe signálu z akcelerometra alebo gyroskopu. V tejto sekcii sa naučíme, ako vyriešiť podobný problém - balansovanie tyče. Je to podobné situácii, keď cirkusový umelec potrebuje balansovať tyč na svojej ruke - ale toto balansovanie tyče sa odohráva iba v 1D.

Zjednodušená verzia balansovania je známa ako problém **CartPole**. Vo svete CartPole máme horizontálny posúvač, ktorý sa môže pohybovať doľava alebo doprava, a cieľom je balansovať vertikálnu tyč na vrchu posúvača, keď sa pohybuje.

<img alt="cartpole" src="../../../../../translated_images/sk/cartpole.f52a67f27e058170.webp" width="200"/>

Na vytvorenie a použitie tohto prostredia potrebujeme niekoľko riadkov kódu v Pythone:

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

Každé prostredie je možné pristupovať presne rovnakým spôsobom:
* `env.reset` spustí nový experiment
* `env.step` vykoná simulačný krok. Prijíma **akciu** z **akčného priestoru** a vracia **pozorovanie** (z pozorovacieho priestoru), ako aj odmenu a príznak ukončenia.

V príklade vyššie vykonávame náhodnú akciu pri každom kroku, čo je dôvod, prečo je život experimentu veľmi krátky:

![nebalansujúci cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Cieľom RL algoritmu je vytrénovať model - tzv. **politiku** &pi; - ktorá bude vracať akciu v reakcii na daný stav. Politiku môžeme tiež považovať za pravdepodobnostnú, napr. pre akýkoľvek stav *s* a akciu *a* bude vracať pravdepodobnosť &pi;(*a*|*s*), že by sme mali vykonať *a* v stave *s*.

## Algoritmus Policy Gradients

Najzjavnejší spôsob, ako modelovať politiku, je vytvoriť neurónovú sieť, ktorá bude brať stavy ako vstup a vracať zodpovedajúce akcie (alebo skôr pravdepodobnosti všetkých akcií). V istom zmysle by to bolo podobné bežnej klasifikačnej úlohe, s jedným hlavným rozdielom - vopred nevieme, ktoré akcie by sme mali vykonať pri každom kroku.

Myšlienka je tu odhadnúť tieto pravdepodobnosti. Vytvoríme vektor **kumulatívnych odmien**, ktorý ukazuje našu celkovú odmenu pri každom kroku experimentu. Tiež aplikujeme **diskontovanie odmien** násobením skorších odmien určitým koeficientom &gamma;=0.99, aby sme znížili význam skorších odmien. Potom posilníme tie kroky pozdĺž experimentálnej cesty, ktoré prinášajú väčšie odmeny.

> Viac o algoritme Policy Gradient a jeho ukážku nájdete v [príkladovom notebooku](CartPole-RL-TF.ipynb).

## Algoritmus Actor-Critic

Vylepšená verzia prístupu Policy Gradients sa nazýva **Actor-Critic**. Hlavná myšlienka spočíva v tom, že neurónová sieť by bola trénovaná na návrat dvoch vecí:

* Politiku, ktorá určuje, akú akciu vykonať. Táto časť sa nazýva **actor**.
* Odhad celkovej odmeny, ktorú môžeme očakávať v tomto stave - táto časť sa nazýva **critic**.

V istom zmysle táto architektúra pripomína [GAN](../../4-ComputerVision/10-GANs/README.md), kde máme dve siete, ktoré sú trénované proti sebe. V modeli actor-critic navrhuje actor akciu, ktorú potrebujeme vykonať, a critic sa snaží byť kritický a odhadnúť výsledok. Naším cieľom je však trénovať tieto siete v súlade.

Keďže poznáme skutočné kumulatívne odmeny a výsledky vrátené criticom počas experimentu, je relatívne jednoduché vytvoriť funkciu straty, ktorá minimalizuje rozdiel medzi nimi. To nám dáva **critic loss**. **Actor loss** môžeme vypočítať použitím rovnakého prístupu ako v algoritme Policy Gradient.

Po spustení jedného z týchto algoritmov môžeme očakávať, že náš CartPole sa bude správať takto:

![balansujúci cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Cvičenia: Policy Gradients a Actor-Critic RL

Pokračujte vo svojom učení v nasledujúcich notebookoch:

* [RL v TensorFlow](CartPole-RL-TF.ipynb)
* [RL v PyTorch](CartPole-RL-PyTorch.ipynb)

## Ďalšie úlohy RL

Posilňovacie učenie je dnes rýchlo rastúcou oblasťou výskumu. Niektoré zaujímavé príklady posilňovacieho učenia sú:

* Učenie počítača hrať **hry Atari**. Výzvou v tomto probléme je, že nemáme jednoduchý stav reprezentovaný ako vektor, ale skôr snímku obrazovky - a musíme použiť CNN na konverziu tohto obrazového snímku na vektor vlastností alebo na extrakciu informácií o odmene. Hry Atari sú dostupné v Gym.
* Učenie počítača hrať stolové hry, ako šach a Go. Nedávno boli špičkové programy ako **Alpha Zero** trénované od nuly dvoma agentmi, ktorí hrali proti sebe a zlepšovali sa pri každom kroku.
* V priemysle sa RL používa na vytváranie riadiacich systémov zo simulácie. Služba nazývaná [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) je špeciálne navrhnutá na tento účel.

## Záver

Teraz sme sa naučili, ako trénovať agentov na dosiahnutie dobrých výsledkov len poskytnutím funkcie odmeny, ktorá definuje požadovaný stav hry, a umožnením inteligentného skúmania priestoru hľadania. Úspešne sme vyskúšali dva algoritmy a dosiahli dobrý výsledok v relatívne krátkom čase. Toto je však len začiatok vašej cesty do RL, a určite by ste mali zvážiť absolvovanie samostatného kurzu, ak chcete ísť hlbšie.

## 🚀 Výzva

Preskúmajte aplikácie uvedené v sekcii 'Ďalšie úlohy RL' a skúste implementovať jednu z nich!

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Prehľad a samostatné štúdium

Viac o klasickom posilňovacom učení sa dozviete v našom [učebnom pláne Strojového učenia pre začiatočníkov](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Pozrite si [toto skvelé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ktoré hovorí o tom, ako sa počítač môže naučiť hrať Super Mario.

## Zadanie: [Vytrénujte Mountain Car](lab/README.md)

Vaším cieľom počas tohto zadania bude vytrénovať iné prostredie Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

