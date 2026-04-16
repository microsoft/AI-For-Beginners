# Dyp Forsterkningslæring

Forsterkningslæring (RL) regnes som en av de grunnleggende paradigmer innen maskinlæring, ved siden av veiledet læring og uveiledet læring. Mens vi i veiledet læring baserer oss på datasett med kjente utfall, er RL basert på **læring gjennom handling**. For eksempel, når vi ser et dataspill for første gang, begynner vi å spille, selv uten å kjenne reglene, og snart blir vi bedre bare ved å spille og justere oppførselen vår.

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/43)

For å utføre RL trenger vi:

* Et **miljø** eller en **simulator** som setter reglene for spillet. Vi må kunne kjøre eksperimenter i simulatoren og observere resultatene.
* En **belønningsfunksjon**, som indikerer hvor vellykket eksperimentet vårt var. Når vi lærer å spille et dataspill, vil belønningen være vår endelige poengsum.

Basert på belønningsfunksjonen bør vi kunne justere oppførselen vår og forbedre ferdighetene våre, slik at vi spiller bedre neste gang. Den største forskjellen mellom RL og andre typer maskinlæring er at vi i RL vanligvis ikke vet om vi vinner eller taper før spillet er ferdig. Dermed kan vi ikke si om en enkelt handling er god eller dårlig – vi mottar belønningen først ved slutten av spillet.

Under RL utfører vi typisk mange eksperimenter. I hvert eksperiment må vi balansere mellom å følge den optimale strategien vi har lært så langt (**utnyttelse**) og utforske nye mulige tilstander (**utforskning**).

## OpenAI Gym

Et fantastisk verktøy for RL er [OpenAI Gym](https://gym.openai.com/) – et **simuleringsmiljø** som kan simulere mange forskjellige miljøer, fra Atari-spill til fysikken bak stangbalansering. Det er et av de mest populære simuleringsmiljøene for trening av forsterkningslæringsalgoritmer, og vedlikeholdes av [OpenAI](https://openai.com/).

> **Note**: Du kan se alle miljøene som er tilgjengelige fra OpenAI Gym [her](https://gym.openai.com/envs/#classic_control).

## CartPole-balansering

Dere har sikkert sett moderne balanseringsenheter som *Segway* eller *Gyroscooters*. De kan automatisk balansere ved å justere hjulene sine basert på signaler fra et akselerometer eller gyroskop. I denne delen skal vi lære å løse et lignende problem – å balansere en stang. Det ligner på en situasjon der en sirkusartist må balansere en stang på hånden – men denne stangbalanseringen skjer kun i én dimensjon.

En forenklet versjon av balansering er kjent som **CartPole**-problemet. I CartPole-verdenen har vi en horisontal skyver som kan bevege seg til venstre eller høyre, og målet er å balansere en vertikal stang på toppen av skyveren mens den beveger seg.

<img alt="en cartpole" src="../../../../../translated_images/no/cartpole.f52a67f27e058170.webp" width="200"/>

For å opprette og bruke dette miljøet trenger vi noen få linjer med Python-kode:

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

Hvert miljø kan nås på nøyaktig samme måte:
* `env.reset` starter et nytt eksperiment
* `env.step` utfører et simuleringssteg. Det mottar en **handling** fra **handlingsrommet**, og returnerer en **observasjon** (fra observasjonsrommet), samt en belønning og en avslutningsflagg.

I eksemplet ovenfor utfører vi en tilfeldig handling ved hvert steg, noe som gjør at eksperimentets levetid er veldig kort:

![ikke-balanserende cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Målet med en RL-algoritme er å trene en modell – den såkalte **policy** &pi; – som vil returnere handlingen som svar på en gitt tilstand. Vi kan også betrakte policy som probabilistisk, dvs. for enhver tilstand *s* og handling *a* vil den returnere sannsynligheten &pi;(*a*|*s*) for at vi bør ta *a* i tilstand *s*.

## Policy Gradients-algoritme

Den mest åpenbare måten å modellere en policy på er ved å opprette et nevralt nettverk som tar tilstander som input og returnerer tilsvarende handlinger (eller snarere sannsynlighetene for alle handlinger). På en måte vil det være lik en vanlig klassifiseringsoppgave, med en stor forskjell – vi vet ikke på forhånd hvilke handlinger vi bør ta ved hvert steg.

Ideen her er å estimere disse sannsynlighetene. Vi bygger en vektor av **kumulative belønninger** som viser vår totale belønning ved hvert steg av eksperimentet. Vi bruker også **belønningsdiskontering** ved å multiplisere tidligere belønninger med en koeffisient &gamma;=0.99, for å redusere betydningen av tidligere belønninger. Deretter forsterker vi de stegene langs eksperimentbanen som gir større belønninger.

> Lær mer om Policy Gradient-algoritmen og se den i aksjon i [eksempelfilen](CartPole-RL-TF.ipynb).

## Actor-Critic-algoritme

En forbedret versjon av Policy Gradients-tilnærmingen kalles **Actor-Critic**. Hovedideen bak denne er at det nevrale nettverket skal trenes til å returnere to ting:

* Policy, som bestemmer hvilken handling som skal tas. Denne delen kalles **actor**.
* Estimeringen av den totale belønningen vi kan forvente å få i denne tilstanden – denne delen kalles **critic**.

På en måte ligner denne arkitekturen en [GAN](../../4-ComputerVision/10-GANs/README.md), der vi har to nettverk som trenes mot hverandre. I Actor-Critic-modellen foreslår actor handlingen vi må ta, og critic prøver å være kritisk og estimere resultatet. Målet vårt er imidlertid å trene disse nettverkene i harmoni.

Fordi vi kjenner både de reelle kumulative belønningene og resultatene returnert av critic under eksperimentet, er det relativt enkelt å bygge en tapsfunksjon som minimerer forskjellen mellom dem. Dette gir oss **critic loss**. Vi kan beregne **actor loss** ved å bruke samme tilnærming som i Policy Gradient-algoritmen.

Etter å ha kjørt en av disse algoritmene, kan vi forvente at vår CartPole oppfører seg slik:

![en balanserende cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Øvelser: Policy Gradients og Actor-Critic RL

Fortsett læringen i følgende notatbøker:

* [RL i TensorFlow](CartPole-RL-TF.ipynb)
* [RL i PyTorch](CartPole-RL-PyTorch.ipynb)

## Andre RL-oppgaver

Forsterkningslæring er i dag et raskt voksende forskningsfelt. Noen interessante eksempler på forsterkningslæring er:

* Å lære en datamaskin å spille **Atari-spill**. Den utfordrende delen av dette problemet er at vi ikke har en enkel tilstand representert som en vektor, men snarere et skjermbilde – og vi må bruke CNN for å konvertere dette skjermbildet til en funksjonsvektor eller for å trekke ut belønningsinformasjon. Atari-spill er tilgjengelige i Gym.
* Å lære en datamaskin å spille brettspill, som sjakk og Go. Nylig ble toppmoderne programmer som **Alpha Zero** trent fra bunnen av ved at to agenter spilte mot hverandre og forbedret seg ved hvert steg.
* I industrien brukes RL til å lage kontrollsystemer fra simulering. En tjeneste kalt [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) er spesielt designet for dette.

## Konklusjon

Vi har nå lært hvordan vi kan trene agenter til å oppnå gode resultater bare ved å gi dem en belønningsfunksjon som definerer ønsket tilstand for spillet, og ved å gi dem muligheten til intelligent å utforske søkeområdet. Vi har prøvd to algoritmer med suksess og oppnådd gode resultater på relativt kort tid. Dette er imidlertid bare begynnelsen på din reise inn i RL, og du bør definitivt vurdere å ta et eget kurs hvis du vil fordype deg.

## 🚀 Utfordring

Utforsk applikasjonene som er oppført i delen 'Andre RL-oppgaver' og prøv å implementere en!

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Gjennomgang og selvstudium

Lær mer om klassisk forsterkningslæring i vårt [Maskinlæring for nybegynnere-kurs](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Se [denne flotte videoen](https://www.youtube.com/watch?v=qv6UVOQ0F44) som forklarer hvordan en datamaskin kan lære å spille Super Mario.

## Oppgave: [Tren en Mountain Car](lab/README.md)

Målet ditt under denne oppgaven vil være å trene et annet Gym-miljø – [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

