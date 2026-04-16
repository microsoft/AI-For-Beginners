# Deep Reinforcement Learning

Reinforcement Learning (RL) wird als eines der grundlegenden Paradigmen des maschinellen Lernens angesehen, neben überwachten und unüberwachten Lernen. Während wir beim überwachten Lernen auf Datensätze mit bekannten Ergebnissen angewiesen sind, basiert RL auf dem Prinzip des **Lernens durch Handeln**. Zum Beispiel: Wenn wir ein Computerspiel zum ersten Mal sehen, beginnen wir zu spielen, auch ohne die Regeln zu kennen, und verbessern unsere Fähigkeiten allein durch das Spielen und Anpassen unseres Verhaltens.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Um RL durchzuführen, benötigen wir:

* Eine **Umgebung** oder einen **Simulator**, der die Regeln des Spiels festlegt. Wir sollten in der Lage sein, Experimente im Simulator durchzuführen und die Ergebnisse zu beobachten.
* Eine **Belohnungsfunktion**, die anzeigt, wie erfolgreich unser Experiment war. Im Fall des Lernens, ein Computerspiel zu spielen, wäre die Belohnung unsere Endpunktzahl.

Basierend auf der Belohnungsfunktion sollten wir unser Verhalten anpassen und unsere Fähigkeiten verbessern, sodass wir beim nächsten Mal besser spielen. Der Hauptunterschied zwischen anderen Arten des maschinellen Lernens und RL besteht darin, dass wir bei RL normalerweise erst am Ende des Spiels wissen, ob wir gewonnen oder verloren haben. Daher können wir nicht sagen, ob ein bestimmter Zug allein gut oder schlecht ist – wir erhalten die Belohnung erst am Ende des Spiels.

Während des RL führen wir typischerweise viele Experimente durch. Bei jedem Experiment müssen wir zwischen der Anwendung der optimalen Strategie, die wir bisher gelernt haben (**Exploitation**), und der Erkundung neuer möglicher Zustände (**Exploration**) abwägen.

## OpenAI Gym

Ein großartiges Werkzeug für RL ist das [OpenAI Gym](https://gym.openai.com/) – eine **Simulationsumgebung**, die viele verschiedene Umgebungen simulieren kann, von Atari-Spielen bis hin zur Physik des Stangenbalancierens. Es ist eine der beliebtesten Simulationsumgebungen für das Training von Reinforcement-Learning-Algorithmen und wird von [OpenAI](https://openai.com/) gepflegt.

> **Note**: Alle verfügbaren Umgebungen von OpenAI Gym können [hier](https://gym.openai.com/envs/#classic_control) eingesehen werden.

## CartPole Balancing

Ihr habt wahrscheinlich alle moderne Balanciergeräte wie den *Segway* oder *Gyroscooter* gesehen. Sie können sich automatisch ausbalancieren, indem sie ihre Räder entsprechend einem Signal von einem Beschleunigungsmesser oder Gyroskop anpassen. In diesem Abschnitt lernen wir, ein ähnliches Problem zu lösen – das Balancieren einer Stange. Es ist vergleichbar mit der Situation, in der ein Zirkuskünstler eine Stange auf seiner Hand balancieren muss – aber dieses Balancieren erfolgt nur in einer Dimension.

Eine vereinfachte Version des Balancierens ist als **CartPole**-Problem bekannt. In der CartPole-Welt haben wir einen horizontalen Schlitten, der sich nach links oder rechts bewegen kann, und das Ziel ist es, eine vertikale Stange oben auf dem Schlitten zu balancieren, während er sich bewegt.

<img alt="a cartpole" src="../../../../../translated_images/de/cartpole.f52a67f27e058170.webp" width="200"/>

Um diese Umgebung zu erstellen und zu nutzen, benötigen wir ein paar Zeilen Python-Code:

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

Jede Umgebung kann auf die gleiche Weise angesprochen werden:
* `env.reset` startet ein neues Experiment
* `env.step` führt einen Simulationsschritt aus. Es erhält eine **Aktion** aus dem **Aktionsraum** und gibt eine **Beobachtung** (aus dem Beobachtungsraum) sowie eine Belohnung und ein Abbruchflag zurück.

Im obigen Beispiel führen wir bei jedem Schritt eine zufällige Aktion aus, weshalb die Lebensdauer des Experiments sehr kurz ist:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Das Ziel eines RL-Algorithmus ist es, ein Modell zu trainieren – die sogenannte **Policy** &pi; –, die die Aktion als Antwort auf einen gegebenen Zustand zurückgibt. Wir können die Policy auch als probabilistisch betrachten, z. B. für jeden Zustand *s* und jede Aktion *a* gibt sie die Wahrscheinlichkeit &pi;(*a*|*s*) zurück, dass wir *a* im Zustand *s* ausführen sollten.

## Policy-Gradient-Algorithmus

Die offensichtlichste Möglichkeit, eine Policy zu modellieren, besteht darin, ein neuronales Netzwerk zu erstellen, das Zustände als Eingabe nimmt und entsprechende Aktionen (oder vielmehr die Wahrscheinlichkeiten aller Aktionen) zurückgibt. In gewisser Weise wäre es ähnlich wie eine normale Klassifikationsaufgabe, mit einem wesentlichen Unterschied – wir wissen im Voraus nicht, welche Aktionen wir bei jedem Schritt ausführen sollten.

Die Idee ist hier, diese Wahrscheinlichkeiten zu schätzen. Wir erstellen einen Vektor von **kumulierten Belohnungen**, der unsere Gesamtbelohnung bei jedem Schritt des Experiments zeigt. Wir wenden auch **Belohnungsdiskontierung** an, indem wir frühere Belohnungen mit einem Koeffizienten &gamma;=0.99 multiplizieren, um die Rolle früherer Belohnungen zu verringern. Dann verstärken wir die Schritte entlang des Experimentpfads, die größere Belohnungen bringen.

> Erfahren Sie mehr über den Policy-Gradient-Algorithmus und sehen Sie ihn in Aktion im [Beispiel-Notebook](CartPole-RL-TF.ipynb).

## Actor-Critic-Algorithmus

Eine verbesserte Version des Policy-Gradient-Ansatzes wird **Actor-Critic** genannt. Die Hauptidee dahinter ist, dass das neuronale Netzwerk so trainiert wird, dass es zwei Dinge zurückgibt:

* Die Policy, die bestimmt, welche Aktion ausgeführt werden soll. Dieser Teil wird **Actor** genannt.
* Die Schätzung der Gesamtbelohnung, die wir in diesem Zustand erwarten können – dieser Teil wird **Critic** genannt.

In gewisser Weise ähnelt diese Architektur einem [GAN](../../4-ComputerVision/10-GANs/README.md), bei dem wir zwei Netzwerke haben, die gegeneinander trainiert werden. Im Actor-Critic-Modell schlägt der Actor die Aktion vor, die wir ausführen müssen, und der Critic versucht kritisch zu sein und das Ergebnis zu schätzen. Unser Ziel ist jedoch, diese Netzwerke im Einklang zu trainieren.

Da wir sowohl die tatsächlichen kumulierten Belohnungen als auch die vom Critic während des Experiments zurückgegebenen Ergebnisse kennen, ist es relativ einfach, eine Verlustfunktion zu erstellen, die die Differenz zwischen ihnen minimiert. Das ergibt den **Critic-Loss**. Den **Actor-Loss** können wir mit dem gleichen Ansatz wie beim Policy-Gradient-Algorithmus berechnen.

Nach dem Ausführen eines dieser Algorithmen können wir erwarten, dass unser CartPole sich so verhält:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Übungen: Policy-Gradient und Actor-Critic RL

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Andere RL-Aufgaben

Reinforcement Learning ist heutzutage ein schnell wachsendes Forschungsfeld. Einige interessante Beispiele für Reinforcement Learning sind:

* Das Lehren eines Computers, **Atari-Spiele** zu spielen. Die Herausforderung bei diesem Problem besteht darin, dass wir keinen einfachen Zustand als Vektor haben, sondern einen Screenshot – und wir müssen CNNs verwenden, um dieses Bildschirmbild in einen Feature-Vektor umzuwandeln oder Belohnungsinformationen zu extrahieren. Atari-Spiele sind im Gym verfügbar.
* Das Lehren eines Computers, Brettspiele wie Schach und Go zu spielen. Kürzlich wurden Programme wie **Alpha Zero** von Grund auf trainiert, indem zwei Agenten gegeneinander spielten und sich bei jedem Schritt verbesserten.
* In der Industrie wird RL verwendet, um Steuerungssysteme aus Simulationen zu erstellen. Ein Dienst namens [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) ist speziell dafür konzipiert.

## Fazit

Wir haben nun gelernt, wie man Agenten trainiert, um gute Ergebnisse zu erzielen, indem man ihnen lediglich eine Belohnungsfunktion gibt, die den gewünschten Zustand des Spiels definiert, und ihnen die Möglichkeit gibt, den Suchraum intelligent zu erkunden. Wir haben erfolgreich zwei Algorithmen ausprobiert und in relativ kurzer Zeit ein gutes Ergebnis erzielt. Dies ist jedoch nur der Anfang Ihrer Reise in RL, und Sie sollten definitiv einen separaten Kurs in Betracht ziehen, wenn Sie tiefer eintauchen möchten.

## 🚀 Herausforderung

Erkunden Sie die Anwendungen, die im Abschnitt "Andere RL-Aufgaben" aufgeführt sind, und versuchen Sie, eine davon umzusetzen!

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Überprüfung & Selbststudium

Erfahren Sie mehr über klassisches Reinforcement Learning in unserem [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Sehen Sie sich [dieses großartige Video](https://www.youtube.com/watch?v=qv6UVOQ0F44) an, das zeigt, wie ein Computer lernen kann, Super Mario zu spielen.

## Aufgabe: [Trainieren Sie ein Mountain Car](lab/README.md)

Ihr Ziel bei dieser Aufgabe ist es, eine andere Gym-Umgebung zu trainieren – [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

