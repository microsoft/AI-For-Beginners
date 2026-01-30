# Deep Reinforcement Learning

Reinforcement learning (RL) wordt gezien als een van de fundamentele machine learning paradigma's, naast supervised learning en unsupervised learning. Terwijl we bij supervised learning vertrouwen op een dataset met bekende uitkomsten, is RL gebaseerd op **leren door te doen**. Bijvoorbeeld, wanneer we voor het eerst een computerspel zien, beginnen we te spelen, zelfs zonder de regels te kennen, en al snel verbeteren we onze vaardigheden simpelweg door te spelen en ons gedrag aan te passen.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Om RL uit te voeren, hebben we nodig:

* Een **omgeving** of **simulator** die de regels van het spel bepaalt. We moeten experimenten kunnen uitvoeren in de simulator en de resultaten kunnen observeren.
* Een **beloningsfunctie**, die aangeeft hoe succesvol ons experiment was. In het geval van leren om een computerspel te spelen, zou de beloning onze eindscore zijn.

Op basis van de beloningsfunctie moeten we ons gedrag kunnen aanpassen en onze vaardigheden verbeteren, zodat we de volgende keer beter spelen. Het belangrijkste verschil tussen andere soorten machine learning en RL is dat we bij RL meestal pas weten of we winnen of verliezen als het spel voorbij is. We kunnen dus niet zeggen of een bepaalde zet op zichzelf goed of slecht is - we ontvangen pas een beloning aan het einde van het spel.

Tijdens RL voeren we meestal veel experimenten uit. Bij elk experiment moeten we een balans vinden tussen het volgen van de optimale strategie die we tot nu toe hebben geleerd (**exploitation**) en het verkennen van nieuwe mogelijke staten (**exploration**).

## OpenAI Gym

Een geweldig hulpmiddel voor RL is de [OpenAI Gym](https://gym.openai.com/) - een **simulatieomgeving** die veel verschillende omgevingen kan simuleren, van Atari-spellen tot de fysica achter het balanceren van een paal. Het is een van de meest populaire simulatieomgevingen voor het trainen van reinforcement learning-algoritmes en wordt onderhouden door [OpenAI](https://openai.com/).

> **Note**: Je kunt alle beschikbare omgevingen van OpenAI Gym [hier](https://gym.openai.com/envs/#classic_control) bekijken.

## CartPole Balanceren

We hebben allemaal moderne balancerende apparaten gezien, zoals de *Segway* of *Gyroscooters*. Ze kunnen automatisch balanceren door hun wielen aan te passen op basis van een signaal van een versnellingsmeter of gyroscoop. In deze sectie leren we hoe we een vergelijkbaar probleem kunnen oplossen: het balanceren van een paal. Dit lijkt op een situatie waarin een circusartiest een paal op zijn hand moet balanceren - maar dit paalbalanceren gebeurt alleen in 1D.

Een vereenvoudigde versie van balanceren staat bekend als het **CartPole**-probleem. In de CartPole-wereld hebben we een horizontale slider die naar links of rechts kan bewegen, en het doel is om een verticale paal bovenop de slider te balanceren terwijl deze beweegt.

<img alt="a cartpole" src="../../../../../translated_images/nl/cartpole.f52a67f27e058170.webp" width="200"/>

Om deze omgeving te creëren en te gebruiken, hebben we een paar regels Python-code nodig:

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

Elke omgeving kan op dezelfde manier worden benaderd:
* `env.reset` start een nieuw experiment
* `env.step` voert een simulatiestap uit. Het ontvangt een **actie** uit de **actie-ruimte** en retourneert een **observatie** (uit de observatieruimte), evenals een beloning en een beëindigingsvlag.

In het bovenstaande voorbeeld voeren we bij elke stap een willekeurige actie uit, waardoor de levensduur van het experiment erg kort is:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Het doel van een RL-algoritme is om een model te trainen - het zogenaamde **beleid** &pi; - dat de actie retourneert in reactie op een gegeven staat. We kunnen beleid ook als probabilistisch beschouwen, bijvoorbeeld voor elke staat *s* en actie *a* retourneert het de waarschijnlijkheid &pi;(*a*|*s*) dat we *a* moeten nemen in staat *s*.

## Policy Gradients Algorithm

De meest voor de hand liggende manier om een beleid te modelleren is door een neuraal netwerk te maken dat staten als input neemt en bijbehorende acties retourneert (of liever de waarschijnlijkheden van alle acties). In zekere zin zou het vergelijkbaar zijn met een normale classificatietaak, met een groot verschil - we weten van tevoren niet welke acties we bij elke stap moeten nemen.

Het idee hier is om die waarschijnlijkheden te schatten. We bouwen een vector van **cumulatieve beloningen** die onze totale beloning bij elke stap van het experiment laat zien. We passen ook **beloningskorting** toe door eerdere beloningen te vermenigvuldigen met een coëfficiënt &gamma;=0.99, om de rol van eerdere beloningen te verminderen. Vervolgens versterken we die stappen langs het experimentpad die grotere beloningen opleveren.

> Leer meer over het Policy Gradient-algoritme en zie het in actie in het [voorbeeldnotebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

Een verbeterde versie van de Policy Gradients-aanpak wordt **Actor-Critic** genoemd. Het belangrijkste idee hierachter is dat het neurale netwerk wordt getraind om twee dingen te retourneren:

* Het beleid, dat bepaalt welke actie moet worden ondernomen. Dit deel wordt **actor** genoemd.
* De schatting van de totale beloning die we kunnen verwachten in deze staat - dit deel wordt **critic** genoemd.

In zekere zin lijkt deze architectuur op een [GAN](../../4-ComputerVision/10-GANs/README.md), waarbij we twee netwerken hebben die tegen elkaar worden getraind. In het actor-critic model stelt de actor de actie voor die we moeten nemen, en probeert de critic kritisch te zijn en het resultaat te schatten. Ons doel is echter om die netwerken in harmonie te trainen.

Omdat we zowel de echte cumulatieve beloningen als de resultaten die door de critic worden geretourneerd tijdens het experiment kennen, is het relatief eenvoudig om een verliesfunctie te bouwen die het verschil tussen hen minimaliseert. Dat zou ons **critic loss** geven. We kunnen **actor loss** berekenen door dezelfde aanpak te gebruiken als in het policy gradient-algoritme.

Na het uitvoeren van een van deze algoritmes kunnen we verwachten dat onze CartPole zich zo gedraagt:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Oefeningen: Policy Gradients en Actor-Critic RL

Ga verder met leren in de volgende notebooks:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Andere RL Taken

Reinforcement Learning is tegenwoordig een snel groeiend onderzoeksgebied. Enkele interessante voorbeelden van reinforcement learning zijn:

* Een computer leren **Atari-spellen** te spelen. Het uitdagende deel van dit probleem is dat we geen eenvoudige staat hebben die wordt weergegeven als een vector, maar eerder een screenshot - en we moeten de CNN gebruiken om dit schermbeeld om te zetten in een featurevector of om beloningsinformatie te extraheren. Atari-spellen zijn beschikbaar in de Gym.
* Een computer leren bordspellen te spelen, zoals Schaken en Go. Onlangs zijn state-of-the-art programma's zoals **Alpha Zero** vanaf nul getraind door twee agenten tegen elkaar te laten spelen en bij elke stap te verbeteren.
* In de industrie wordt RL gebruikt om controlesystemen te creëren vanuit simulatie. Een dienst genaamd [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) is speciaal hiervoor ontworpen.

## Conclusie

We hebben nu geleerd hoe we agenten kunnen trainen om goede resultaten te behalen door hen alleen een beloningsfunctie te geven die de gewenste staat van het spel definieert, en door hen de mogelijkheid te geven om intelligent de zoekruimte te verkennen. We hebben met succes twee algoritmes geprobeerd en een goed resultaat behaald in een relatief korte tijd. Dit is echter slechts het begin van je reis in RL, en je zou zeker moeten overwegen om een aparte cursus te volgen als je dieper wilt graven.

## 🚀 Uitdaging

Verken de toepassingen die worden vermeld in de sectie 'Andere RL Taken' en probeer er een te implementeren!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review & Zelfstudie

Leer meer over klassiek reinforcement learning in ons [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Bekijk [deze geweldige video](https://www.youtube.com/watch?v=qv6UVOQ0F44) waarin wordt uitgelegd hoe een computer kan leren Super Mario te spelen.

## Opdracht: [Train een Mountain Car](lab/README.md)

Je doel tijdens deze opdracht is om een andere Gym-omgeving te trainen - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

