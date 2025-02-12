# Apprentissage par Renforcement Profond

L'apprentissage par renforcement (RL) est considéré comme l'un des paradigmes fondamentaux de l'apprentissage machine, aux côtés de l'apprentissage supervisé et non supervisé. Alors que dans l'apprentissage supervisé, nous nous appuyons sur un ensemble de données avec des résultats connus, le RL repose sur **l'apprentissage par l'action**. Par exemple, lorsque nous découvrons un nouveau jeu vidéo, nous commençons à jouer, même sans connaître les règles, et rapidement, nous parvenons à améliorer nos compétences simplement en jouant et en ajustant notre comportement.

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Pour effectuer du RL, nous avons besoin de :

* Un **environnement** ou **simulateur** qui définit les règles du jeu. Nous devrions être capables de réaliser des expériences dans le simulateur et d'observer les résultats.
* Une **fonction de récompense**, qui indique à quel point notre expérience a été réussie. Dans le cas de l'apprentissage d'un jeu vidéo, la récompense serait notre score final.

Sur la base de la fonction de récompense, nous devrions être en mesure d'ajuster notre comportement et d'améliorer nos compétences, de sorte qu'à la prochaine partie, nous jouions mieux. La principale différence entre les autres types d'apprentissage machine et le RL est qu'en RL, nous ne savons généralement pas si nous gagnons ou perdons avant d'avoir terminé le jeu. Ainsi, nous ne pouvons pas dire si un mouvement particulier est bon ou non - nous ne recevons une récompense qu'à la fin du jeu.

Lors de l'apprentissage par renforcement, nous réalisons généralement de nombreuses expériences. Au cours de chaque expérience, nous devons équilibrer entre le suivi de la stratégie optimale que nous avons apprise jusqu'à présent (**exploitation**) et l'exploration de nouveaux états possibles (**exploration**).

## OpenAI Gym

Un excellent outil pour le RL est l'[OpenAI Gym](https://gym.openai.com/) - un **environnement de simulation**, capable de simuler de nombreux environnements différents, allant des jeux Atari à la physique derrière l'équilibre d'un poteau. C'est l'un des environnements de simulation les plus populaires pour former des algorithmes d'apprentissage par renforcement, et il est maintenu par [OpenAI](https://openai.com/).

> **Note** : Vous pouvez voir tous les environnements disponibles dans OpenAI Gym [ici](https://gym.openai.com/envs/#classic_control).

## Équilibre CartPole

Vous avez probablement tous vu des dispositifs d'équilibre modernes tels que le *Segway* ou les *Gyroscooters*. Ils parviennent à s'équilibrer automatiquement en ajustant leurs roues en réponse à un signal provenant d'un accéléromètre ou d'un gyroscope. Dans cette section, nous allons apprendre à résoudre un problème similaire - l'équilibre d'un poteau. C'est comparable à une situation où un artiste de cirque doit équilibrer un poteau sur sa main - mais cet équilibre ne se produit que dans une dimension.

Une version simplifiée de l'équilibre est connue sous le nom de problème **CartPole**. Dans le monde du cartpole, nous avons un curseur horizontal qui peut se déplacer à gauche ou à droite, et l'objectif est de maintenir un poteau vertical au sommet du curseur pendant qu'il se déplace.

<img alt="un cartpole" src="images/cartpole.png" width="200"/>

Pour créer et utiliser cet environnement, nous avons besoin de quelques lignes de code Python :

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

Chaque environnement peut être accessible de la même manière :
* `env.reset` starts a new experiment
* `env.step` effectue une étape de simulation. Il reçoit une **action** de l'**espace d'actions** et renvoie une **observation** (de l'espace d'observation), ainsi qu'une récompense et un indicateur de terminaison.

Dans l'exemple ci-dessus, nous effectuons une action aléatoire à chaque étape, ce qui explique pourquoi la durée de vie de l'expérience est très courte :

![cartpole non équilibré](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

L'objectif d'un algorithme de RL est de former un modèle - la soi-disant **politique** π - qui renverra l'action en réponse à un état donné. Nous pouvons également considérer la politique comme étant probabiliste, par exemple, pour tout état *s* et action *a*, elle renverra la probabilité π(*a*|*s*) que nous devrions prendre *a* dans l'état *s*.

## Algorithme des Gradients de Politique

La manière la plus évidente de modéliser une politique est de créer un réseau de neurones qui prendra des états en entrée et renverra les actions correspondantes (ou plutôt les probabilités de toutes les actions). En un sens, cela serait similaire à une tâche de classification normale, avec une différence majeure - nous ne savons pas à l'avance quelles actions nous devrions prendre à chacune des étapes.

L'idée ici est d'estimer ces probabilités. Nous construisons un vecteur de **récompenses cumulées** qui montre notre récompense totale à chaque étape de l'expérience. Nous appliquons également un **escompte de récompense** en multipliant les récompenses antérieures par un coefficient γ=0.99, afin de diminuer le rôle des récompenses antérieures. Ensuite, nous renforçons ces étapes le long du chemin de l'expérience qui produisent des récompenses plus importantes.

> En savoir plus sur l'algorithme de Gradient de Politique et le voir en action dans le [carnet d'exemples](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algorithme Acteur-Critique

Une version améliorée de l'approche des Gradients de Politique est appelée **Acteur-Critique**. L'idée principale est que le réseau de neurones serait entraîné pour renvoyer deux choses :

* La politique, qui détermine quelle action prendre. Cette partie est appelée **acteur**.
* L'estimation de la récompense totale que nous pouvons espérer obtenir dans cet état - cette partie est appelée **critique**.

En un sens, cette architecture ressemble à un [GAN](../../4-ComputerVision/10-GANs/README.md), où nous avons deux réseaux qui sont entraînés l'un contre l'autre. Dans le modèle acteur-critique, l'acteur propose l'action que nous devons prendre, et le critique essaie d'être critique et d'estimer le résultat. Cependant, notre objectif est d'entraîner ces réseaux de manière conjointe.

Comme nous connaissons à la fois les vraies récompenses cumulées et les résultats renvoyés par le critique pendant l'expérience, il est relativement facile de construire une fonction de perte qui minimisera la différence entre elles. Cela nous donnerait la **perte du critique**. Nous pouvons calculer la **perte de l'acteur** en utilisant la même approche que dans l'algorithme de gradient de politique.

Après avoir exécuté l'un de ces algorithmes, nous pouvons nous attendre à ce que notre CartPole se comporte comme ceci :

![un cartpole équilibré](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercices : Gradients de Politique et RL Acteur-Critique

Poursuivez votre apprentissage dans les carnets suivants :

* [RL dans TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL dans PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Autres Tâches de RL

L'apprentissage par renforcement est aujourd'hui un domaine de recherche en pleine expansion. Voici quelques exemples intéressants d'apprentissage par renforcement :

* Apprendre à un ordinateur à jouer à des **jeux Atari**. La difficulté dans ce problème est que nous n'avons pas d'état simple représenté sous forme de vecteur, mais plutôt une capture d'écran - et nous devons utiliser le CNN pour convertir cette image d'écran en un vecteur de caractéristiques, ou pour extraire des informations de récompense. Les jeux Atari sont disponibles dans le Gym.
* Apprendre à un ordinateur à jouer à des jeux de société, tels que les échecs et le Go. Récemment, des programmes à la pointe de la technologie comme **Alpha Zero** ont été entraînés à partir de zéro par deux agents jouant l'un contre l'autre, s'améliorant à chaque étape.
* Dans l'industrie, le RL est utilisé pour créer des systèmes de contrôle à partir de simulations. Un service appelé [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) est spécifiquement conçu pour cela.

## Conclusion

Nous avons maintenant appris comment former des agents pour obtenir de bons résultats simplement en leur fournissant une fonction de récompense qui définit l'état souhaité du jeu, et en leur offrant la possibilité d'explorer intelligemment l'espace de recherche. Nous avons essayé avec succès deux algorithmes et obtenu un bon résultat dans un délai relativement court. Cependant, ce n'est que le début de votre voyage dans le RL, et vous devriez certainement envisager de suivre un cours séparé si vous souhaitez approfondir vos connaissances.

## 🚀 Défi

Explorez les applications énumérées dans la section 'Autres Tâches de RL' et essayez d'en implémenter une !

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Revue et Auto-étude

En savoir plus sur l'apprentissage par renforcement classique dans notre [Curriculum d'Apprentissage Machine pour Débutants](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Regardez [cette excellente vidéo](https://www.youtube.com/watch?v=qv6UVOQ0F44) qui parle de la façon dont un ordinateur peut apprendre à jouer à Super Mario.

## Devoir : [Entraîner une Voiture de Montagne](lab/README.md)

Votre objectif lors de ce devoir serait d'entraîner un environnement Gym différent - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.