# Deep Reinforcement Learning

Reinforcement Learning (RL) wird als eines der grundlegenden Paradigmen des maschinellen Lernens angesehen, neben dem überwachten und unüberwachten Lernen. Während wir im überwachten Lernen auf Datensätze mit bekannten Ergebnissen angewiesen sind, basiert RL auf **Lernen durch Handeln**. Zum Beispiel, wenn wir ein Computer-Spiel zum ersten Mal sehen, fangen wir an zu spielen, selbst ohne die Regeln zu kennen, und bald sind wir in der Lage, unsere Fähigkeiten allein durch das Spielen und Anpassen unseres Verhaltens zu verbessern.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Um RL durchzuführen, benötigen wir:

* Eine **Umgebung** oder **Simulation**, die die Regeln des Spiels festlegt. Wir sollten in der Lage sein, die Experimente in der Simulation durchzuführen und die Ergebnisse zu beobachten.
* Eine **Belohnungsfunktion**, die angibt, wie erfolgreich unser Experiment war. Im Fall des Lernens, ein Computerspiel zu spielen, wäre die Belohnung unser Endpunktestand.

Basierend auf der Belohnungsfunktion sollten wir in der Lage sein, unser Verhalten anzupassen und unsere Fähigkeiten zu verbessern, damit wir beim nächsten Mal besser spielen. Der Hauptunterschied zwischen anderen Arten des maschinellen Lernens und RL besteht darin, dass wir im RL typischerweise nicht wissen, ob wir gewinnen oder verlieren, bis wir das Spiel beenden. Daher können wir nicht sagen, ob ein bestimmter Zug allein gut oder schlecht ist - wir erhalten die Belohnung erst am Ende des Spiels.

Während des RL führen wir typischerweise viele Experimente durch. Während jedes Experiments müssen wir ein Gleichgewicht finden zwischen der Verfolgung der optimalen Strategie, die wir bisher gelernt haben (**Exploitation**), und der Erkundung neuer möglicher Zustände (**Exploration**).

## OpenAI Gym

Ein großartiges Werkzeug für RL ist das [OpenAI Gym](https://gym.openai.com/) - eine **Simulationsumgebung**, die viele verschiedene Umgebungen simulieren kann, von Atari-Spielen bis hin zur Physik hinter dem Balancieren eines Mastes. Es ist eine der beliebtesten Simulationsumgebungen zur Schulung von Reinforcement-Learning-Algorithmen und wird von [OpenAI](https://openai.com/) gepflegt.

> **Hinweis**: Sie können alle verfügbaren Umgebungen von OpenAI Gym [hier](https://gym.openai.com/envs/#classic_control) einsehen.

## CartPole Balancing

Sie haben wahrscheinlich alle moderne Balanciergeräte wie den *Segway* oder *Gyroscooter* gesehen. Diese sind in der Lage, automatisch zu balancieren, indem sie ihre Räder als Reaktion auf ein Signal von einem Beschleunigungsmesser oder Gyroskop anpassen. In diesem Abschnitt werden wir lernen, wie man ein ähnliches Problem löst - das Balancieren eines Mastes. Es ist vergleichbar mit einer Situation, in der ein Zirkuskünstler einen Mast auf seiner Hand balancieren muss - jedoch findet dieses Balancieren nur in 1D statt.

Eine vereinfachte Version des Balancierens ist als **CartPole**-Problem bekannt. In der CartPole-Welt haben wir einen horizontalen Schieber, der sich nach links oder rechts bewegen kann, und das Ziel ist es, einen vertikalen Mast oben auf dem Schieber auszubalancieren, während er sich bewegt.

<img alt="ein cartpole" src="images/cartpole.png" width="200"/>

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

Jede Umgebung kann auf genau die gleiche Weise aufgerufen werden:
* `env.reset` starts a new experiment
* `env.step` führt einen Simulationsschritt durch. Es erhält eine **Aktion** aus dem **Aktionsraum** und gibt eine **Beobachtung** (aus dem Beobachtungsraum) sowie eine Belohnung und ein Beendigungsflag zurück.

Im obigen Beispiel führen wir bei jedem Schritt eine zufällige Aktion aus, weshalb die Lebensdauer des Experiments sehr kurz ist:

![nicht balancierendes cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Das Ziel eines RL-Algorithmus ist es, ein Modell - die sogenannte **Politik** π - zu trainieren, das die Aktion als Antwort auf einen gegebenen Zustand zurückgibt. Wir können die Politik auch als probabilistisch betrachten, d.h. für jeden Zustand *s* und jede Aktion *a* gibt sie die Wahrscheinlichkeit π(*a*|*s*) zurück, dass wir *a* im Zustand *s* wählen sollten.

## Policy Gradients Algorithmus

Der offensichtlichste Weg, eine Politik zu modellieren, besteht darin, ein neuronales Netzwerk zu erstellen, das Zustände als Eingabe nimmt und die entsprechenden Aktionen (oder besser gesagt die Wahrscheinlichkeiten aller Aktionen) zurückgibt. In gewissem Sinne wäre es ähnlich wie bei einer normalen Klassifikationsaufgabe, mit einem wesentlichen Unterschied - wir wissen im Voraus nicht, welche Aktionen wir in jedem Schritt ausführen sollten.

Die Idee hier ist, diese Wahrscheinlichkeiten zu schätzen. Wir erstellen einen Vektor von **kumulierten Belohnungen**, der unsere Gesamtbelohnung in jedem Schritt des Experiments zeigt. Wir wenden auch **Belohnungsdiskontierung** an, indem wir frühere Belohnungen mit einem Koeffizienten γ=0.99 multiplizieren, um die Rolle der früheren Belohnungen zu verringern. Dann verstärken wir die Schritte entlang des Experimentpfades, die größere Belohnungen erzielen.

> Erfahren Sie mehr über den Policy-Gradient-Algorithmus und sehen Sie ihn in Aktion im [Beispiel-Notebook](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Actor-Critic Algorithmus

Eine verbesserte Version des Policy-Gradients-Ansatzes wird als **Actor-Critic** bezeichnet. Die Hauptidee dahinter ist, dass das neuronale Netzwerk trainiert wird, um zwei Dinge zurückzugeben:

* Die Politik, die bestimmt, welche Aktion zu ergreifen ist. Dieser Teil wird **Actor** genannt.
* Die Schätzung der Gesamtbelohnung, die wir in diesem Zustand erwarten können - dieser Teil wird **Critic** genannt.

In gewissem Sinne ähnelt diese Architektur einem [GAN](../../4-ComputerVision/10-GANs/README.md), bei dem wir zwei Netzwerke haben, die gegeneinander trainiert werden. Im Actor-Critic-Modell schlägt der Actor die Aktion vor, die wir ausführen müssen, und der Critic versucht, kritisch zu sein und das Ergebnis zu schätzen. Unser Ziel ist es jedoch, diese Netzwerke gemeinsam zu trainieren.

Da wir sowohl die tatsächlichen kumulierten Belohnungen als auch die Ergebnisse, die der Critic während des Experiments zurückgibt, kennen, ist es relativ einfach, eine Verlustfunktion zu erstellen, die den Unterschied zwischen ihnen minimiert. Das würde uns **Critic-Verlust** geben. Wir können **Actor-Verlust** berechnen, indem wir denselben Ansatz wie im Policy-Gradient-Algorithmus verwenden.

Nach dem Ausführen eines dieser Algorithmen können wir erwarten, dass unser CartPole so aussieht:

![ein balancierendes cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Übungen: Policy Gradients und Actor-Critic RL

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [RL in TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL in PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Weitere RL-Aufgaben

Reinforcement Learning ist heutzutage ein schnell wachsendes Forschungsfeld. Einige interessante Beispiele für Reinforcement Learning sind:

* Einem Computer beibringen, **Atari-Spiele** zu spielen. Der herausfordernde Teil dieses Problems besteht darin, dass wir keinen einfachen Zustand in Form eines Vektors haben, sondern eher einen Screenshot - und wir müssen das CNN verwenden, um dieses Bildschirmbild in einen Merkmalsvektor zu konvertieren oder Belohnungsinformationen zu extrahieren. Atari-Spiele sind im Gym verfügbar.
* Einem Computer beibringen, Brettspiele wie Schach und Go zu spielen. Kürzlich wurden hochmoderne Programme wie **Alpha Zero** von zwei Agenten, die gegeneinander spielten und sich mit jedem Schritt verbesserten, von Grund auf trainiert.
* In der Industrie wird RL verwendet, um Steuerungssysteme aus Simulationen zu erstellen. Ein Dienst namens [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) wurde speziell dafür entwickelt.

## Fazit

Wir haben nun gelernt, wie man Agenten trainiert, um gute Ergebnisse zu erzielen, indem wir ihnen eine Belohnungsfunktion bereitstellen, die den gewünschten Zustand des Spiels definiert, und ihnen die Möglichkeit geben, den Suchraum intelligent zu erkunden. Wir haben erfolgreich zwei Algorithmen ausprobiert und in relativ kurzer Zeit ein gutes Ergebnis erzielt. Dies ist jedoch nur der Anfang Ihrer Reise in das RL, und Sie sollten auf jeden Fall in Betracht ziehen, einen separaten Kurs zu belegen, wenn Sie tiefer eintauchen möchten.

## 🚀 Herausforderung

Erforschen Sie die in der Rubrik 'Weitere RL-Aufgaben' aufgeführten Anwendungen und versuchen Sie, eine zu implementieren!

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Überprüfung & Selbststudium

Erfahren Sie mehr über klassisches Reinforcement Learning in unserem [Maschinenlernen für Anfänger Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Sehen Sie sich [dieses großartige Video](https://www.youtube.com/watch?v=qv6UVOQ0F44) an, das darüber spricht, wie ein Computer lernen kann, Super Mario zu spielen.

## Aufgabe: [Trainiere ein Mountain Car](lab/README.md)

Ihr Ziel während dieser Aufgabe wäre es, eine andere Gym-Umgebung zu trainieren - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Haftungsausschluss**:  
Dieses Dokument wurde mit Hilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.