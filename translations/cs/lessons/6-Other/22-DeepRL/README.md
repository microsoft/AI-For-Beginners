# Hluboké posilované učení

Posilované učení (RL) je považováno za jeden ze základních paradigmat strojového učení, vedle učení s učitelem a učení bez učitele. Zatímco u učení s učitelem se spoléháme na dataset s předem známými výsledky, RL je založeno na **učení skrze zkušenost**. Například, když poprvé vidíme počítačovou hru, začneme ji hrát, i když neznáme pravidla, a brzy dokážeme zlepšit své dovednosti jen díky procesu hraní a přizpůsobování svého chování.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Pro provádění RL potřebujeme:

* **Prostředí** nebo **simulátor**, který nastaví pravidla hry. Měli bychom být schopni provádět experimenty v simulátoru a pozorovat výsledky.
* Nějakou **funkci odměny**, která ukazuje, jak úspěšný byl náš experiment. V případě učení se hrát počítačovou hru by odměnou bylo naše konečné skóre.

Na základě funkce odměny bychom měli být schopni přizpůsobit své chování a zlepšit své dovednosti, aby příště naše hra byla lepší. Hlavní rozdíl mezi jinými typy strojového učení a RL je ten, že v RL obvykle nevíme, zda vyhrajeme nebo prohrajeme, dokud nedokončíme hru. Nemůžeme tedy říci, zda je určitý tah sám o sobě dobrý nebo ne - odměnu dostaneme až na konci hry.

Během RL obvykle provádíme mnoho experimentů. Během každého experimentu musíme vyvážit mezi sledováním optimální strategie, kterou jsme se dosud naučili (**exploatace**), a zkoumáním nových možných stavů (**explorace**).

## OpenAI Gym

Skvělým nástrojem pro RL je [OpenAI Gym](https://gym.openai.com/) - **simulační prostředí**, které dokáže simulovat mnoho různých prostředí, od her Atari až po fyziku za balancováním tyče. Je to jedno z nejpopulárnějších simulačních prostředí pro trénování algoritmů posilovaného učení a je spravováno společností [OpenAI](https://openai.com/).

> **Note**: Všechna dostupná prostředí z OpenAI Gym si můžete prohlédnout [zde](https://gym.openai.com/envs/#classic_control).

## Balancování CartPole

Pravděpodobně jste všichni viděli moderní balancovací zařízení, jako je *Segway* nebo *Gyroskútry*. Jsou schopny automaticky balancovat tím, že upravují své kolečka na základě signálu z akcelerometru nebo gyroskopu. V této sekci se naučíme, jak vyřešit podobný problém - balancování tyče. Je to podobné situaci, kdy cirkusový umělec potřebuje balancovat tyč na své ruce - ale toto balancování tyče probíhá pouze v 1D.

Zjednodušená verze balancování je známá jako problém **CartPole**. Ve světě CartPole máme horizontální posuvník, který se může pohybovat doleva nebo doprava, a cílem je balancovat vertikální tyč na vrcholu posuvníku, zatímco se pohybuje.

<img alt="cartpole" src="../../../../../translated_images/cs/cartpole.f52a67f27e058170.webp" width="200"/>

Pro vytvoření a použití tohoto prostředí potřebujeme několik řádků kódu v Pythonu:

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

Každé prostředí lze přistupovat stejným způsobem:
* `env.reset` zahájí nový experiment
* `env.step` provede simulační krok. Přijímá **akci** z **akčního prostoru** a vrací **pozorování** (z pozorovacího prostoru), stejně jako odměnu a příznak ukončení.

V příkladu výše provádíme náhodnou akci při každém kroku, což je důvod, proč je životnost experimentu velmi krátká:

![nebalancující cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Cílem algoritmu RL je vytrénovat model - tzv. **politiku** &pi; - která vrátí akci v reakci na daný stav. Politiku můžeme také považovat za pravděpodobnostní, tj. pro jakýkoli stav *s* a akci *a* vrátí pravděpodobnost &pi;(*a*|*s*), že bychom měli provést *a* ve stavu *s*.

## Algoritmus Policy Gradients

Nejzřejmější způsob, jak modelovat politiku, je vytvořit neuronovou síť, která bude přijímat stavy jako vstup a vracet odpovídající akce (nebo spíše pravděpodobnosti všech akcí). V jistém smyslu by to bylo podobné běžnému klasifikačnímu úkolu, s hlavním rozdílem - předem nevíme, které akce bychom měli provést v každém kroku.

Myšlenkou zde je odhadnout tyto pravděpodobnosti. Vytvoříme vektor **kumulativních odměn**, který ukazuje naši celkovou odměnu v každém kroku experimentu. Také aplikujeme **diskontování odměn** tím, že násobíme dřívější odměny nějakým koeficientem &gamma;=0.99, abychom snížili význam dřívějších odměn. Poté posilujeme ty kroky podél experimentální cesty, které přinášejí větší odměny.

> Více o algoritmu Policy Gradient a jeho použití najdete v [příkladovém notebooku](CartPole-RL-TF.ipynb).

## Algoritmus Actor-Critic

Vylepšená verze přístupu Policy Gradients se nazývá **Actor-Critic**. Hlavní myšlenkou je, že neuronová síť bude trénována tak, aby vracela dvě věci:

* Politiku, která určuje, jakou akci provést. Tato část se nazývá **actor**.
* Odhad celkové odměny, kterou můžeme očekávat v tomto stavu - tato část se nazývá **critic**.

V jistém smyslu tato architektura připomíná [GAN](../../4-ComputerVision/10-GANs/README.md), kde máme dvě sítě, které se trénují proti sobě. V modelu actor-critic navrhuje actor akci, kterou bychom měli provést, a critic se snaží být kritický a odhadnout výsledek. Naším cílem je však trénovat tyto sítě společně.

Protože známe jak skutečné kumulativní odměny, tak výsledky vrácené criticem během experimentu, je relativně snadné vytvořit ztrátovou funkci, která minimalizuje rozdíl mezi nimi. To nám poskytne **critic loss**. **Actor loss** můžeme vypočítat stejným přístupem jako v algoritmu Policy Gradient.

Po spuštění jednoho z těchto algoritmů můžeme očekávat, že naše CartPole bude vypadat takto:

![balancující cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Cvičení: Policy Gradients a Actor-Critic RL

Pokračujte ve svém učení v následujících noteboocích:

* [RL v TensorFlow](CartPole-RL-TF.ipynb)
* [RL v PyTorch](CartPole-RL-PyTorch.ipynb)

## Další úkoly RL

Posilované učení je dnes rychle rostoucí oblastí výzkumu. Některé zajímavé příklady posilovaného učení jsou:

* Učení počítače hrát **hry Atari**. Výzvou v tomto problému je, že nemáme jednoduchý stav reprezentovaný jako vektor, ale spíše snímek obrazovky - a musíme použít CNN k převodu tohoto obrazového snímku na vektor vlastností nebo k extrakci informací o odměně. Hry Atari jsou dostupné v Gym.
* Učení počítače hrát deskové hry, jako je šachy a Go. Nedávno byly špičkové programy jako **Alpha Zero** trénovány od nuly dvěma agenty, kteří hráli proti sobě a zlepšovali se při každém kroku.
* V průmyslu se RL používá k vytváření řídicích systémů ze simulace. Služba [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) je speciálně navržena pro tento účel.

## Závěr

Nyní jsme se naučili, jak trénovat agenty, aby dosáhli dobrých výsledků pouze tím, že jim poskytneme funkci odměny, která definuje požadovaný stav hry, a dáme jim příležitost inteligentně prozkoumat prostor hledání. Úspěšně jsme vyzkoušeli dva algoritmy a dosáhli dobrého výsledku v relativně krátkém čase. Toto je však pouze začátek vaší cesty do RL, a měli byste určitě zvážit absolvování samostatného kurzu, pokud chcete jít hlouběji.

## 🚀 Výzva

Prozkoumejte aplikace uvedené v sekci 'Další úkoly RL' a zkuste jednu implementovat!

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Přehled & Samostudium

Více o klasickém posilovaném učení se dozvíte v našem [kurikulu Strojového učení pro začátečníky](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Podívejte se na [toto skvělé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), které ukazuje, jak se počítač může naučit hrát Super Mario.

## Úkol: [Vytrénujte Mountain Car](lab/README.md)

Vaším cílem během tohoto úkolu bude vytrénovat jiné prostředí Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

