# Djup Förstärkningsinlärning

Förstärkningsinlärning (RL) ses som en av de grundläggande paradigmerna inom maskininlärning, vid sidan av övervakad inlärning och oövervakad inlärning. Medan vi i övervakad inlärning förlitar oss på dataset med kända resultat, bygger RL på **att lära genom att göra**. Till exempel, när vi först ser ett datorspel börjar vi spela, även utan att känna till reglerna, och snart kan vi förbättra våra färdigheter bara genom att spela och justera vårt beteende.

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/43)

För att utföra RL behöver vi:

* En **miljö** eller **simulator** som sätter reglerna för spelet. Vi bör kunna köra experiment i simulatorn och observera resultaten.
* Någon form av **belöningsfunktion**, som indikerar hur framgångsrikt vårt experiment var. När det gäller att lära sig spela ett datorspel skulle belöningen vara vår slutpoäng.

Baserat på belöningsfunktionen bör vi kunna justera vårt beteende och förbättra våra färdigheter, så att vi spelar bättre nästa gång. Den största skillnaden mellan andra typer av maskininlärning och RL är att vi i RL vanligtvis inte vet om vi vinner eller förlorar förrän vi har avslutat spelet. Därför kan vi inte säga om ett visst drag i sig är bra eller inte - vi får bara en belöning i slutet av spelet.

Under RL utför vi vanligtvis många experiment. Under varje experiment behöver vi balansera mellan att följa den optimala strategi vi har lärt oss hittills (**exploatering**) och att utforska nya möjliga tillstånd (**utforskning**).

## OpenAI Gym

Ett utmärkt verktyg för RL är [OpenAI Gym](https://gym.openai.com/) - en **simuleringsmiljö** som kan simulera många olika miljöer, från Atari-spel till fysiken bakom balans med en stång. Det är en av de mest populära simuleringsmiljöerna för att träna förstärkningsinlärningsalgoritmer och underhålls av [OpenAI](https://openai.com/).

> **Note**: Du kan se alla miljöer som finns tillgängliga från OpenAI Gym [här](https://gym.openai.com/envs/#classic_control).

## Balans med CartPole

Ni har förmodligen alla sett moderna balansapparater som *Segway* eller *Gyroscooters*. De kan automatiskt balansera genom att justera sina hjul baserat på signaler från en accelerometer eller gyroskop. I detta avsnitt kommer vi att lära oss att lösa ett liknande problem - att balansera en stång. Det liknar en situation där en cirkusartist behöver balansera en stång på sin hand - men denna balans sker endast i 1D.

En förenklad version av balansproblemet är känt som **CartPole**-problemet. I CartPole-världen har vi en horisontell slider som kan röra sig åt vänster eller höger, och målet är att balansera en vertikal stång ovanpå slidern medan den rör sig.

<img alt="en cartpole" src="../../../../../translated_images/sv/cartpole.f52a67f27e058170.webp" width="200"/>

För att skapa och använda denna miljö behöver vi några rader Python-kod:

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

Varje miljö kan nås på exakt samma sätt:
* `env.reset` startar ett nytt experiment
* `env.step` utför ett simuleringssteg. Det tar emot en **action** från **action space**, och returnerar en **observation** (från observation space), samt en belöning och en flagga för avslutning.

I exemplet ovan utför vi en slumpmässig handling vid varje steg, vilket gör att experimentets livslängd blir mycket kort:

![icke-balanserande cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Målet med en RL-algoritm är att träna en modell - den så kallade **policyn** &pi; - som kommer att returnera handlingen som svar på ett givet tillstånd. Vi kan också betrakta policyn som probabilistisk, t.ex. för varje tillstånd *s* och handling *a* kommer den att returnera sannolikheten &pi;(*a*|*s*) att vi bör ta *a* i tillståndet *s*.

## Policy Gradients-algoritm

Det mest uppenbara sättet att modellera en policy är att skapa ett neuralt nätverk som tar tillstånd som input och returnerar motsvarande handlingar (eller snarare sannolikheterna för alla handlingar). På ett sätt skulle det likna en vanlig klassificeringsuppgift, med en stor skillnad - vi vet inte i förväg vilka handlingar vi bör ta vid varje steg.

Idén här är att uppskatta dessa sannolikheter. Vi bygger en vektor av **kumulativa belöningar** som visar vår totala belöning vid varje steg av experimentet. Vi tillämpar också **belöningsdiskontering** genom att multiplicera tidigare belöningar med en koefficient &gamma;=0.99, för att minska betydelsen av tidigare belöningar. Sedan förstärker vi de steg längs experimentvägen som ger större belöningar.

> Läs mer om Policy Gradients-algoritmen och se den i aktion i [exempelfilen](CartPole-RL-TF.ipynb).

## Actor-Critic-algoritm

En förbättrad version av Policy Gradients-metoden kallas **Actor-Critic**. Huvudidén bakom den är att det neurala nätverket ska tränas för att returnera två saker:

* Policyn, som avgör vilken handling som ska utföras. Denna del kallas **actor**.
* En uppskattning av den totala belöningen vi kan förvänta oss att få i detta tillstånd - denna del kallas **critic**.

På ett sätt liknar denna arkitektur en [GAN](../../4-ComputerVision/10-GANs/README.md), där vi har två nätverk som tränas mot varandra. I Actor-Critic-modellen föreslår aktören den handling vi behöver utföra, och kritikern försöker vara kritisk och uppskatta resultatet. Men vårt mål är att träna dessa nätverk i samspel.

Eftersom vi känner till både de verkliga kumulativa belöningarna och resultaten som kritikern returnerar under experimentet, är det relativt enkelt att bygga en förlustfunktion som minimerar skillnaden mellan dem. Det skulle ge oss **critic loss**. Vi kan beräkna **actor loss** genom att använda samma metod som i Policy Gradients-algoritmen.

Efter att ha kört en av dessa algoritmer kan vi förvänta oss att vår CartPole beter sig så här:

![en balanserande cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Övningar: Policy Gradients och Actor-Critic RL

Fortsätt ditt lärande i följande notebook-filer:

* [RL i TensorFlow](CartPole-RL-TF.ipynb)
* [RL i PyTorch](CartPole-RL-PyTorch.ipynb)

## Andra RL-uppgifter

Förstärkningsinlärning är idag ett snabbt växande forskningsområde. Några intressanta exempel på förstärkningsinlärning är:

* Att lära en dator att spela **Atari-spel**. Den utmanande delen i detta problem är att vi inte har ett enkelt tillstånd representerat som en vektor, utan snarare en skärmdump - och vi behöver använda CNN för att konvertera denna skärmbild till en funktionsvektor eller för att extrahera belöningsinformation. Atari-spel finns tillgängliga i Gym.
* Att lära en dator att spela brädspel, såsom schack och Go. Nyligen har toppmoderna program som **Alpha Zero** tränats från grunden av två agenter som spelar mot varandra och förbättras vid varje steg.
* Inom industrin används RL för att skapa styrsystem från simulering. En tjänst som [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) är specifikt utformad för detta.

## Slutsats

Vi har nu lärt oss hur man tränar agenter att uppnå goda resultat bara genom att ge dem en belöningsfunktion som definierar det önskade tillståndet för spelet och genom att ge dem möjlighet att intelligent utforska sökrymden. Vi har framgångsrikt testat två algoritmer och uppnått ett bra resultat på relativt kort tid. Men detta är bara början på din resa inom RL, och du bör definitivt överväga att ta en separat kurs om du vill fördjupa dig.

## 🚀 Utmaning

Utforska de applikationer som nämns i avsnittet 'Andra RL-uppgifter' och försök implementera en!

## [Quiz efter föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Granskning & Självstudier

Lär dig mer om klassisk förstärkningsinlärning i vår [Maskininlärning för nybörjare-kurs](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Titta på [denna fantastiska video](https://www.youtube.com/watch?v=qv6UVOQ0F44) som handlar om hur en dator kan lära sig spela Super Mario.

## Uppgift: [Träna en Mountain Car](lab/README.md)

Ditt mål under denna uppgift är att träna en annan Gym-miljö - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

