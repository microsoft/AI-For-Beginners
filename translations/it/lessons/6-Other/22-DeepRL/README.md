<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-26T07:06:48+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "it"
}
-->
# Apprendimento per Rinforzo Profondo

L'apprendimento per rinforzo (RL) è considerato uno dei paradigmi fondamentali del machine learning, accanto all'apprendimento supervisionato e non supervisionato. Mentre nell'apprendimento supervisionato ci basiamo su un dataset con risultati noti, l'RL si basa sull'**imparare facendo**. Ad esempio, quando vediamo per la prima volta un videogioco, iniziamo a giocare anche senza conoscere le regole, e presto miglioriamo le nostre abilità semplicemente giocando e adattando il nostro comportamento.

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Per eseguire l'RL, abbiamo bisogno di:

* Un **ambiente** o **simulatore** che definisca le regole del gioco. Dovremmo essere in grado di eseguire esperimenti nel simulatore e osservare i risultati.
* Una **funzione di ricompensa**, che indichi quanto è stato efficace il nostro esperimento. Nel caso di apprendimento per giocare a un videogioco, la ricompensa potrebbe essere il nostro punteggio finale.

Basandoci sulla funzione di ricompensa, dovremmo essere in grado di adattare il nostro comportamento e migliorare le nostre abilità, così da giocare meglio la volta successiva. La principale differenza tra l'RL e altri tipi di machine learning è che nell'RL tipicamente non sappiamo se abbiamo vinto o perso fino alla fine del gioco. Pertanto, non possiamo dire se una singola mossa sia buona o meno - riceviamo una ricompensa solo alla fine del gioco.

Durante l'RL, eseguiamo tipicamente molti esperimenti. In ciascun esperimento, dobbiamo bilanciare tra il seguire la strategia ottimale appresa fino a quel momento (**sfruttamento**) e l'esplorazione di nuovi stati possibili (**esplorazione**).

## OpenAI Gym

Uno strumento eccellente per l'RL è [OpenAI Gym](https://gym.openai.com/) - un **ambiente di simulazione**, che può simulare molti ambienti diversi, dai giochi Atari alla fisica dietro l'equilibrio di un'asta. È uno degli ambienti di simulazione più popolari per l'addestramento di algoritmi di apprendimento per rinforzo, ed è mantenuto da [OpenAI](https://openai.com/).

> **Nota**: Puoi vedere tutti gli ambienti disponibili in OpenAI Gym [qui](https://gym.openai.com/envs/#classic_control).

## Equilibrio del CartPole

Avrete probabilmente visto dispositivi moderni di bilanciamento come il *Segway* o i *Gyroscooter*. Sono in grado di bilanciarsi automaticamente regolando le ruote in risposta a un segnale proveniente da un accelerometro o giroscopio. In questa sezione, impareremo a risolvere un problema simile: bilanciare un'asta. È simile alla situazione in cui un artista circense deve bilanciare un'asta sulla mano - ma in questo caso il bilanciamento avviene solo in 1D.

Una versione semplificata del bilanciamento è nota come problema del **CartPole**. Nel mondo del CartPole, abbiamo uno slider orizzontale che può muoversi a sinistra o a destra, e l'obiettivo è bilanciare un'asta verticale sopra lo slider mentre si muove.

<img alt="un cartpole" src="images/cartpole.png" width="200"/>

Per creare e utilizzare questo ambiente, servono poche righe di codice Python:

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

Ogni ambiente può essere utilizzato esattamente nello stesso modo:
* `env.reset` avvia un nuovo esperimento
* `env.step` esegue un passo di simulazione. Riceve un'**azione** dallo **spazio delle azioni** e restituisce un'**osservazione** (dallo spazio delle osservazioni), oltre a una ricompensa e un flag di terminazione.

Nell'esempio sopra, eseguiamo un'azione casuale a ogni passo, motivo per cui la durata dell'esperimento è molto breve:

![cartpole senza bilanciamento](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

L'obiettivo di un algoritmo di RL è addestrare un modello - la cosiddetta **policy** π - che restituisca l'azione in risposta a uno stato dato. Possiamo anche considerare la policy come probabilistica, ad esempio per ogni stato *s* e azione *a* restituirà la probabilità π(*a*|*s*) che dovremmo eseguire *a* nello stato *s*.

## Algoritmo dei Gradienti di Policy

Il modo più ovvio per modellare una policy è creare una rete neurale che prenda gli stati come input e restituisca le azioni corrispondenti (o piuttosto le probabilità di tutte le azioni). In un certo senso, sarebbe simile a un normale compito di classificazione, con una differenza fondamentale: non sappiamo in anticipo quali azioni dovremmo eseguire a ciascun passo.

L'idea qui è stimare quelle probabilità. Costruiamo un vettore di **ricompense cumulative** che mostra la nostra ricompensa totale a ciascun passo dell'esperimento. Applichiamo anche uno **sconto sulle ricompense** moltiplicando le ricompense precedenti per un coefficiente γ=0.99, al fine di ridurre l'importanza delle ricompense più lontane nel tempo. Successivamente, rafforziamo quei passi lungo il percorso dell'esperimento che producono ricompense maggiori.

> Scopri di più sull'algoritmo dei Gradienti di Policy e guardalo in azione nel [notebook di esempio](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algoritmo Actor-Critic

Una versione migliorata dell'approccio dei Gradienti di Policy è chiamata **Actor-Critic**. L'idea principale è che la rete neurale venga addestrata per restituire due cose:

* La policy, che determina quale azione intraprendere. Questa parte è chiamata **actor**.
* La stima della ricompensa totale che possiamo aspettarci di ottenere in questo stato - questa parte è chiamata **critic**.

In un certo senso, questa architettura ricorda un [GAN](../../4-ComputerVision/10-GANs/README.md), dove abbiamo due reti che vengono addestrate l'una contro l'altra. Nel modello actor-critic, l'actor propone l'azione da intraprendere, e il critic cerca di essere critico e stimare il risultato. Tuttavia, il nostro obiettivo è addestrare queste reti in sincronia.

Poiché conosciamo sia le ricompense cumulative reali sia i risultati restituiti dal critic durante l'esperimento, è relativamente facile costruire una funzione di perdita che minimizzi la differenza tra di essi. Questo ci darà la **perdita del critic**. Possiamo calcolare la **perdita dell'actor** utilizzando lo stesso approccio dell'algoritmo dei gradienti di policy.

Dopo aver eseguito uno di questi algoritmi, possiamo aspettarci che il nostro CartPole si comporti così:

![cartpole in equilibrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Esercizi: Gradienti di Policy e Actor-Critic RL

Continua il tuo apprendimento nei seguenti notebook:

* [RL in TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL in PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Altri Compiti di RL

L'apprendimento per rinforzo è oggi un campo di ricerca in rapida crescita. Alcuni esempi interessanti di apprendimento per rinforzo sono:

* Insegnare a un computer a giocare ai **giochi Atari**. La parte impegnativa di questo problema è che non abbiamo uno stato semplice rappresentato come un vettore, ma piuttosto uno screenshot - e dobbiamo usare una CNN per convertire questa immagine dello schermo in un vettore di caratteristiche o per estrarre informazioni sulla ricompensa. I giochi Atari sono disponibili in Gym.
* Insegnare a un computer a giocare a giochi da tavolo, come gli scacchi e il Go. Recentemente, programmi all'avanguardia come **Alpha Zero** sono stati addestrati da zero facendo giocare due agenti l'uno contro l'altro, migliorando a ogni passo.
* Nell'industria, l'RL viene utilizzato per creare sistemi di controllo a partire da simulazioni. Un servizio chiamato [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) è specificamente progettato per questo.

## Conclusione

Abbiamo ora imparato come addestrare agenti per ottenere buoni risultati semplicemente fornendo loro una funzione di ricompensa che definisce lo stato desiderato del gioco e dando loro l'opportunità di esplorare intelligentemente lo spazio di ricerca. Abbiamo provato con successo due algoritmi e ottenuto un buon risultato in un periodo di tempo relativamente breve. Tuttavia, questo è solo l'inizio del tuo viaggio nell'RL, e dovresti sicuramente considerare di seguire un corso specifico se vuoi approfondire.

## 🚀 Sfida

Esplora le applicazioni elencate nella sezione "Altri Compiti di RL" e prova a implementarne una!

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Revisione e Studio Autonomo

Scopri di più sull'apprendimento per rinforzo classico nel nostro [Curriculum di Machine Learning per Principianti](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Guarda [questo fantastico video](https://www.youtube.com/watch?v=qv6UVOQ0F44) che spiega come un computer può imparare a giocare a Super Mario.

## Compito: [Addestra una Mountain Car](lab/README.md)

Il tuo obiettivo durante questo compito sarà addestrare un ambiente Gym diverso - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.