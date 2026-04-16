# Deep Reinforcement Learning

Forstærkningslæring (RL) betragtes som en af de grundlæggende paradigmer inden for maskinlæring, ved siden af superviseret læring og usuperviseret læring. Mens vi i superviseret læring baserer os på datasæt med kendte resultater, er RL baseret på **at lære ved at gøre**. For eksempel, når vi ser et computerspil for første gang, begynder vi at spille, selv uden at kende reglerne, og snart bliver vi bedre, blot ved at spille og justere vores adfærd.

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/43)

For at udføre RL har vi brug for:

* Et **miljø** eller en **simulator**, der fastsætter reglerne for spillet. Vi skal kunne udføre eksperimenter i simulatoren og observere resultaterne.
* En **belønningsfunktion**, der angiver, hvor succesfuldt vores eksperiment var. Når vi lærer at spille et computerspil, ville belønningen være vores endelige score.

Baseret på belønningsfunktionen skal vi kunne justere vores adfærd og forbedre vores færdigheder, så vi spiller bedre næste gang. Den største forskel mellem andre typer maskinlæring og RL er, at vi i RL typisk ikke ved, om vi vinder eller taber, før spillet er slut. Derfor kan vi ikke sige, om et bestemt træk alene er godt eller ej - vi modtager kun en belønning ved slutningen af spillet.

Under RL udfører vi typisk mange eksperimenter. Under hvert eksperiment skal vi balancere mellem at følge den optimale strategi, vi har lært indtil videre (**udnyttelse**), og at udforske nye mulige tilstande (**udforskning**).

## OpenAI Gym

Et fantastisk værktøj til RL er [OpenAI Gym](https://gym.openai.com/) - et **simuleringsmiljø**, der kan simulere mange forskellige miljøer, lige fra Atari-spil til fysikken bag stangbalancering. Det er et af de mest populære simuleringsmiljøer til træning af forstærkningslæringsalgoritmer og vedligeholdes af [OpenAI](https://openai.com/).

> **Note**: Du kan se alle de miljøer, der er tilgængelige fra OpenAI Gym [her](https://gym.openai.com/envs/#classic_control).

## CartPole Balancering

I har sikkert alle set moderne balanceringsenheder som *Segway* eller *Gyroscooters*. De kan automatisk balancere ved at justere deres hjul som reaktion på signaler fra en accelerometer eller gyroskop. I denne sektion vil vi lære at løse et lignende problem - at balancere en stang. Det minder om en situation, hvor en cirkusartist skal balancere en stang på sin hånd - men denne stangbalancering foregår kun i 1D.

En forenklet version af balancering er kendt som **CartPole**-problemet. I CartPole-verdenen har vi en horisontal slider, der kan bevæge sig til venstre eller højre, og målet er at balancere en vertikal stang oven på slideren, mens den bevæger sig.

<img alt="en cartpole" src="../../../../../translated_images/da/cartpole.f52a67f27e058170.webp" width="200"/>

For at oprette og bruge dette miljø har vi brug for et par linjer Python-kode:

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

Hvert miljø kan tilgås på præcis samme måde:
* `env.reset` starter et nyt eksperiment
* `env.step` udfører et simuleringsskridt. Det modtager en **handling** fra **handlingsrummet** og returnerer en **observation** (fra observationsrummet), samt en belønning og en afslutningsflag.

I eksemplet ovenfor udfører vi en tilfældig handling ved hvert skridt, hvilket er grunden til, at eksperimentets levetid er meget kort:

![ikke-balancerende cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Målet med en RL-algoritme er at træne en model - den såkaldte **policy** &pi; - som vil returnere handlingen som svar på en given tilstand. Vi kan også betragte policy som probabilistisk, dvs. for enhver tilstand *s* og handling *a* vil den returnere sandsynligheden &pi;(*a*|*s*) for, at vi bør tage *a* i tilstand *s*.

## Policy Gradients Algoritme

Den mest oplagte måde at modellere en policy på er ved at oprette et neuralt netværk, der tager tilstande som input og returnerer tilsvarende handlinger (eller rettere sandsynlighederne for alle handlinger). På en måde ville det ligne en normal klassifikationsopgave, med en væsentlig forskel - vi ved ikke på forhånd, hvilke handlinger vi skal tage ved hvert skridt.

Ideen her er at estimere disse sandsynligheder. Vi bygger en vektor af **kumulative belønninger**, der viser vores samlede belønning ved hvert skridt i eksperimentet. Vi anvender også **belønningsdiskontering** ved at multiplicere tidligere belønninger med en koefficient &gamma;=0.99 for at mindske betydningen af tidligere belønninger. Derefter forstærker vi de skridt langs eksperimentets sti, der giver større belønninger.

> Lær mere om Policy Gradient-algoritmen og se den i aktion i [eksempelsnotebooken](CartPole-RL-TF.ipynb).

## Actor-Critic Algoritme

En forbedret version af Policy Gradients-tilgangen kaldes **Actor-Critic**. Hovedideen bag den er, at det neurale netværk skal trænes til at returnere to ting:

* Policy, der bestemmer, hvilken handling der skal tages. Denne del kaldes **actor**.
* Estimeringen af den samlede belønning, vi kan forvente at få i denne tilstand - denne del kaldes **critic**.

På en måde minder denne arkitektur om en [GAN](../../4-ComputerVision/10-GANs/README.md), hvor vi har to netværk, der trænes mod hinanden. I actor-critic-modellen foreslår actor den handling, vi skal tage, og critic forsøger at være kritisk og estimere resultatet. Vores mål er dog at træne disse netværk i fællesskab.

Fordi vi kender både de reelle kumulative belønninger og de resultater, der returneres af critic under eksperimentet, er det relativt nemt at opbygge en tab-funktion, der minimerer forskellen mellem dem. Det giver os **critic loss**. Vi kan beregne **actor loss** ved at bruge samme tilgang som i policy gradient-algoritmen.

Efter at have kørt en af disse algoritmer kan vi forvente, at vores CartPole opfører sig sådan her:

![en balancerende cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Øvelser: Policy Gradients og Actor-Critic RL

Fortsæt din læring i følgende notebooks:

* [RL i TensorFlow](CartPole-RL-TF.ipynb)
* [RL i PyTorch](CartPole-RL-PyTorch.ipynb)

## Andre RL-opgaver

Forstærkningslæring er i dag et hurtigt voksende forskningsområde. Nogle interessante eksempler på forstærkningslæring er:

* At lære en computer at spille **Atari-spil**. Den udfordrende del af dette problem er, at vi ikke har en simpel tilstand repræsenteret som en vektor, men snarere et skærmbillede - og vi skal bruge CNN til at konvertere dette skærmbillede til en feature-vektor eller til at udtrække belønningsinformation. Atari-spil er tilgængelige i Gym.
* At lære en computer at spille brætspil som skak og Go. For nylig blev avancerede programmer som **Alpha Zero** trænet fra bunden af to agenter, der spillede mod hinanden og forbedrede sig ved hvert skridt.
* I industrien bruges RL til at skabe kontrolsystemer fra simulering. En tjeneste kaldet [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) er specifikt designet til dette.

## Konklusion

Vi har nu lært, hvordan man træner agenter til at opnå gode resultater blot ved at give dem en belønningsfunktion, der definerer den ønskede tilstand af spillet, og ved at give dem mulighed for intelligent at udforske søgeområdet. Vi har med succes prøvet to algoritmer og opnået et godt resultat på relativt kort tid. Dette er dog kun begyndelsen på din rejse ind i RL, og du bør bestemt overveje at tage et separat kursus, hvis du vil dykke dybere.

## 🚀 Udfordring

Udforsk de applikationer, der er nævnt i afsnittet 'Andre RL-opgaver', og prøv at implementere en af dem!

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Gennemgang & Selvstudie

Lær mere om klassisk forstærkningslæring i vores [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Se [denne fantastiske video](https://www.youtube.com/watch?v=qv6UVOQ0F44), der taler om, hvordan en computer kan lære at spille Super Mario.

## Opgave: [Træn en Mountain Car](lab/README.md)

Dit mål under denne opgave vil være at træne et andet Gym-miljø - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

