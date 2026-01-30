# Învățare prin Recompensă Profundă

Învățarea prin recompensă (RL) este considerată unul dintre paradigmele de bază ale învățării automate, alături de învățarea supravegheată și nesupravegheată. În timp ce în învățarea supravegheată ne bazăm pe un set de date cu rezultate cunoscute, RL se bazează pe **învățarea prin acțiune**. De exemplu, când vedem pentru prima dată un joc pe calculator, începem să jucăm, chiar dacă nu cunoaștem regulile, și în scurt timp ne putem îmbunătăți abilitățile doar prin procesul de joc și ajustarea comportamentului.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Pentru a realiza RL, avem nevoie de:

* Un **mediu** sau **simulator** care stabilește regulile jocului. Trebuie să putem rula experimente în simulator și să observăm rezultatele.
* O **funcție de recompensă**, care indică cât de reușit a fost experimentul nostru. În cazul învățării să jucăm un joc pe calculator, recompensa ar fi scorul final.

Pe baza funcției de recompensă, ar trebui să putem ajusta comportamentul nostru și să ne îmbunătățim abilitățile, astfel încât data viitoare să jucăm mai bine. Principala diferență între alte tipuri de învățare automată și RL este că în RL, de obicei, nu știm dacă câștigăm sau pierdem până nu terminăm jocul. Astfel, nu putem spune dacă o anumită mișcare este bună sau nu - primim recompensa doar la sfârșitul jocului.

În timpul RL, de obicei realizăm multe experimente. În fiecare experiment, trebuie să echilibrăm între urmarea strategiei optime pe care am învățat-o până acum (**exploatare**) și explorarea unor stări noi posibile (**explorare**).

## OpenAI Gym

Un instrument excelent pentru RL este [OpenAI Gym](https://gym.openai.com/) - un **mediu de simulare**, care poate simula multe medii diferite, de la jocuri Atari până la fizica din spatele echilibrării unui stâlp. Este unul dintre cele mai populare medii de simulare pentru antrenarea algoritmilor de învățare prin recompensă și este întreținut de [OpenAI](https://openai.com/).

> **Notă**: Puteți vedea toate mediile disponibile în OpenAI Gym [aici](https://gym.openai.com/envs/#classic_control).

## Echilibrarea CartPole

Probabil ați văzut cu toții dispozitive moderne de echilibrare, cum ar fi *Segway* sau *Gyroscooters*. Acestea sunt capabile să se echilibreze automat ajustându-și roțile ca răspuns la un semnal de la un accelerometru sau giroscop. În această secțiune, vom învăța cum să rezolvăm o problemă similară - echilibrarea unui stâlp. Este similar cu situația în care un artist de circ trebuie să echilibreze un stâlp pe mâna sa - dar această echilibrare a stâlpului are loc doar în 1D.

O versiune simplificată a echilibrării este cunoscută sub numele de problema **CartPole**. În lumea CartPole, avem un slider orizontal care se poate mișca la stânga sau la dreapta, iar scopul este să echilibrăm un stâlp vertical deasupra sliderului în timp ce acesta se mișcă.

<img alt="un cartpole" src="../../../../../translated_images/ro/cartpole.f52a67f27e058170.webp" width="200"/>

Pentru a crea și utiliza acest mediu, avem nevoie de câteva linii de cod Python:

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

Fiecare mediu poate fi accesat exact în același mod:
* `env.reset` începe un nou experiment
* `env.step` efectuează un pas de simulare. Primește o **acțiune** din **spațiul de acțiuni** și returnează o **observație** (din spațiul de observații), precum și o recompensă și un indicator de terminare.

În exemplul de mai sus, efectuăm o acțiune aleatorie la fiecare pas, motiv pentru care durata experimentului este foarte scurtă:

![cartpole fără echilibrare](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Scopul unui algoritm RL este să antreneze un model - așa-numita **politică** &pi; - care va returna acțiunea ca răspuns la o stare dată. De asemenea, putem considera politica ca fiind probabilistică, de exemplu, pentru orice stare *s* și acțiune *a*, va returna probabilitatea &pi;(*a*|*s*) că ar trebui să luăm *a* în starea *s*.

## Algoritmul Policy Gradients

Cel mai evident mod de a modela o politică este prin crearea unei rețele neuronale care va lua stările ca intrare și va returna acțiunile corespunzătoare (sau mai degrabă probabilitățile tuturor acțiunilor). Într-un sens, ar fi similar cu o sarcină normală de clasificare, cu o diferență majoră - nu știm în avans ce acțiuni ar trebui să luăm la fiecare pas.

Ideea aici este să estimăm aceste probabilități. Construim un vector de **recompense cumulative** care arată recompensa totală la fiecare pas al experimentului. De asemenea, aplicăm **discounting-ul recompenselor** prin multiplicarea recompenselor anterioare cu un coeficient &gamma;=0.99, pentru a diminua rolul recompenselor anterioare. Apoi, întărim acei pași de-a lungul traseului experimentului care generează recompense mai mari.

> Aflați mai multe despre algoritmul Policy Gradient și vedeți-l în acțiune în [notebook-ul de exemplu](CartPole-RL-TF.ipynb).

## Algoritmul Actor-Critic

O versiune îmbunătățită a abordării Policy Gradients se numește **Actor-Critic**. Ideea principală din spatele acestuia este că rețeaua neuronală ar fi antrenată să returneze două lucruri:

* Politica, care determină ce acțiune să luăm. Această parte se numește **actor**.
* Estimarea recompensei totale pe care ne putem aștepta să o obținem în această stare - această parte se numește **critic**.

Într-un sens, această arhitectură seamănă cu un [GAN](../../4-ComputerVision/10-GANs/README.md), unde avem două rețele care sunt antrenate una împotriva celeilalte. În modelul actor-critic, actorul propune acțiunea pe care trebuie să o luăm, iar criticul încearcă să fie critic și să estimeze rezultatul. Totuși, scopul nostru este să antrenăm aceste rețele în armonie.

Pentru că știm atât recompensele cumulative reale, cât și rezultatele returnate de critic în timpul experimentului, este relativ ușor să construim o funcție de pierdere care va minimiza diferența dintre ele. Aceasta ne-ar oferi **critic loss**. Putem calcula **actor loss** folosind aceeași abordare ca în algoritmul Policy Gradient.

După rularea unuia dintre aceste algoritme, ne putem aștepta ca CartPole-ul nostru să se comporte astfel:

![cartpole echilibrat](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exerciții: Policy Gradients și Actor-Critic RL

Continuați învățarea în următoarele notebook-uri:

* [RL în TensorFlow](CartPole-RL-TF.ipynb)
* [RL în PyTorch](CartPole-RL-PyTorch.ipynb)

## Alte Sarcini RL

Învățarea prin recompensă este în prezent un domeniu de cercetare în plină expansiune. Unele exemple interesante de învățare prin recompensă sunt:

* Învățarea unui computer să joace **jocuri Atari**. Partea provocatoare în această problemă este că nu avem o stare simplă reprezentată ca un vector, ci mai degrabă un screenshot - și trebuie să folosim CNN pentru a converti această imagine într-un vector de caracteristici sau pentru a extrage informații despre recompensă. Jocurile Atari sunt disponibile în Gym.
* Învățarea unui computer să joace jocuri de masă, cum ar fi Șah și Go. Recent, programe de ultimă generație precum **Alpha Zero** au fost antrenate de la zero prin doi agenți care joacă unul împotriva celuilalt și se îmbunătățesc la fiecare pas.
* În industrie, RL este utilizat pentru a crea sisteme de control din simulare. Un serviciu numit [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) este special conceput pentru acest lucru.

## Concluzie

Am învățat acum cum să antrenăm agenți pentru a obține rezultate bune doar oferindu-le o funcție de recompensă care definește starea dorită a jocului și oferindu-le oportunitatea de a explora inteligent spațiul de căutare. Am încercat cu succes două algoritmi și am obținut un rezultat bun într-o perioadă relativ scurtă de timp. Totuși, acesta este doar începutul călătoriei voastre în RL, și ar trebui să luați în considerare un curs separat dacă doriți să aprofundați.

## 🚀 Provocare

Explorați aplicațiile enumerate în secțiunea 'Alte Sarcini RL' și încercați să implementați una!

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Recapitulare & Studiu Individual

Aflați mai multe despre învățarea prin recompensă clasică în [Curriculum-ul nostru de Învățare Automată pentru Începători](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Urmăriți [acest video excelent](https://www.youtube.com/watch?v=qv6UVOQ0F44) despre cum un computer poate învăța să joace Super Mario.

## Temă: [Antrenează o Mașină de Munte](lab/README.md)

Scopul vostru în această temă va fi să antrenați un mediu diferit din Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

