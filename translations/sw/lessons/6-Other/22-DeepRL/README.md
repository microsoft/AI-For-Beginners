# Djup Förstärkningsinlärning

Förstärkningsinlärning (RL) ses som en av de grundläggande paradigmerna inom maskininlärning, bredvid övervakad inlärning och oövervakad inlärning. Medan vi i övervakad inlärning förlitar oss på dataset med kända utfall, bygger RL på **att lära sig genom att göra**. Till exempel, när vi först ser ett datorspel börjar vi spela, även utan att känna till reglerna, och snart kan vi förbättra våra färdigheter bara genom att spela och justera vårt beteende.

## [För- föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

För att utföra RL behöver vi:

* En **miljö** eller **simulator** som sätter reglerna för spelet. Vi ska kunna köra experimenten i simulatorn och observera resultaten.
* En **Belöningsfunktion**, som indikerar hur framgångsrikt vårt experiment var. I fallet med att lära sig spela ett datorspel skulle belöningen vara vår slutpoäng.

Baserat på belöningsfunktionen ska vi kunna justera vårt beteende och förbättra våra färdigheter, så att vi nästa gång spelar bättre. Den största skillnaden mellan andra typer av maskininlärning och RL är att vi i RL vanligtvis inte vet om vi vinner eller förlorar förrän vi har avslutat spelet. Därför kan vi inte säga om ett visst drag ensam är bra eller inte - vi får bara en belöning i slutet av spelet.

Under RL utför vi vanligtvis många experiment. Under varje experiment behöver vi balansera mellan att följa den optimala strategin som vi har lärt oss hittills (**utnyttjande**) och att utforska nya möjliga tillstånd (**utforskning**).

## OpenAI Gym

Ett utmärkt verktyg för RL är [OpenAI Gym](https://gym.openai.com/) - en **simuleringsmiljö**, som kan simulera många olika miljöer, från Atari-spel till fysiken bakom polbalansering. Det är en av de mest populära simuleringsmiljöerna för träning av förstärkningsinlärningsalgoritmer och underhålls av [OpenAI](https://openai.com/).

> **Notera**: Du kan se alla miljöer som finns tillgängliga från OpenAI Gym [här](https://gym.openai.com/envs/#classic_control).

## CartPole Balansering

Du har förmodligen sett moderna balanseringsanordningar som *Segway* eller *Gyroscooters*. De kan automatiskt balansera genom att justera sina hjul som svar på en signal från en accelerometer eller gyroskop. I den här sektionen kommer vi att lära oss hur man löser ett liknande problem - att balansera en stång. Det liknar en situation när en cirkusartist behöver balansera en stång på sin hand - men denna stångbalansering sker endast i 1D.

En förenklad version av balansering är känd som **CartPole**-problemet. I cartpole-världen har vi en horisontell glidare som kan röra sig åt vänster eller höger, och målet är att balansera en vertikal stång ovanpå glidaren medan den rör sig.

<img alt="en cartpole" src="images/cartpole.png" width="200"/>

För att skapa och använda denna miljö behöver vi ett par rader Python-kod:

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
* `env.reset` starts a new experiment
* `env.step` utför ett simuleringssteg. Den tar emot en **åtgärd** från **åtgärdsutrymmet** och returnerar en **observation** (från observationsutrymmet), samt en belöning och en avslutningsflagga.

I exemplet ovan utför vi en slumpmässig åtgärd vid varje steg, vilket är anledningen till att experimentets livslängd är mycket kort:

![icke-balanserande cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Målet med en RL-algoritm är att träna en modell - den så kallade **policyn** π - som kommer att returnera åtgärden som svar på ett givet tillstånd. Vi kan också betrakta policyn som probabilistisk, t.ex. för något tillstånd *s* och åtgärd *a* kommer den att returnera sannolikheten π(*a*|*s*) att vi bör ta *a* i tillstånd *s*.

## Policy Gradient Algoritm

Det mest uppenbara sättet att modellera en policy är att skapa ett neuralt nätverk som tar tillstånd som indata och returnerar motsvarande åtgärder (eller snarare sannolikheterna för alla åtgärder). På ett sätt skulle det likna en normal klassificeringsuppgift, med en stor skillnad - vi vet inte i förväg vilka åtgärder vi ska ta vid varje steg.

Idén här är att uppskatta dessa sannolikheter. Vi bygger en vektor av **kumulativa belöningar** som visar vår totala belöning vid varje steg av experimentet. Vi tillämpar också **belöningsdiskontering** genom att multiplicera tidigare belöningar med en koefficient γ=0.99, för att minska betydelsen av tidigare belöningar. Sedan förstärker vi de steg längs experimentets väg som ger större belöningar.

> Lär dig mer om Policy Gradient-algoritmen och se den i aktion i [exempelnotebooken](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Actor-Critic Algoritm

En förbättrad version av Policy Gradients-metoden kallas **Actor-Critic**. Huvudidén bakom den är att det neurala nätverket skulle tränas för att returnera två saker:

* Policyn, som avgör vilken åtgärd som ska vidtas. Denna del kallas **aktör**
* Uppskattningen av den totala belöningen vi kan förvänta oss att få i detta tillstånd - denna del kallas **kritiker**.

På ett sätt liknar denna arkitektur en [GAN](../../4-ComputerVision/10-GANs/README.md), där vi har två nätverk som tränas mot varandra. I actor-critic-modellen föreslår aktören den åtgärd vi behöver vidta, och kritikern försöker vara kritisk och uppskatta resultatet. Men vårt mål är att träna dessa nätverk i enhet.

Eftersom vi känner till både de verkliga kumulativa belöningarna och de resultat som returnerats av kritikern under experimentet, är det relativt enkelt att bygga en förlustfunktion som minimerar skillnaden mellan dem. Det skulle ge oss **kritikerförlust**. Vi kan beräkna **aktörförlust** genom att använda samma metod som i policy gradient-algoritmen.

Efter att ha kört en av dessa algoritmer kan vi förvänta oss att vår CartPole beter sig så här:

![en balanserande cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Övningar: Policy Gradients och Actor-Critic RL

Fortsätt din inlärning i följande notebooks:

* [RL i TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL i PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Andra RL-uppgifter

Förstärkningsinlärning är idag ett snabbt växande forskningsområde. Några intressanta exempel på förstärkningsinlärning är:

* Att lära en dator att spela **Atari-spel**. Den utmanande delen av detta problem är att vi inte har ett enkelt tillstånd representerat som en vektor, utan snarare en skärmdump - och vi behöver använda CNN för att konvertera denna skärmbild till en funktionsvektor, eller för att extrahera belöningsinformation. Atari-spel finns tillgängliga i Gym.
* Att lära en dator att spela brädspel, såsom Schack och Go. Nyligen har toppmoderna program som **Alpha Zero** tränats från grunden av två agenter som spelar mot varandra och förbättras vid varje steg.
* Inom industrin används RL för att skapa kontrollsystem från simulering. En tjänst som heter [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) är speciellt utformad för det.

## Slutsats

Vi har nu lärt oss hur man tränar agenter för att uppnå bra resultat genom att bara ge dem en belöningsfunktion som definierar det önskade tillståndet för spelet, och genom att ge dem möjlighet att intelligent utforska sökområdet. Vi har framgångsrikt prövat två algoritmer och uppnått ett bra resultat på en relativt kort tid. Men detta är bara början på din resa in i RL, och du bör definitivt överväga att ta en separat kurs om du vill gräva djupare.

## 🚀 Utmaning

Utforska de tillämpningar som listas i avsnittet "Andra RL-uppgifter" och försök att implementera en!

## [Efter-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Granskning & Självstudie

Lär dig mer om klassisk förstärkningsinlärning i vår [Maskininlärning för Nybörjare Läroplan](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Titta på [denna fantastiska video](https://www.youtube.com/watch?v=qv6UVOQ0F44) som handlar om hur en dator kan lära sig att spela Super Mario.

## Uppgift: [Träna en Mountain Car](lab/README.md)

Ditt mål under denna uppgift skulle vara att träna en annan Gym-miljö - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.