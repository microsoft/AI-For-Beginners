# Apprentissage par renforcement profond

L'apprentissage par renforcement (RL) est considéré comme l'un des paradigmes fondamentaux de l'apprentissage automatique, aux côtés de l'apprentissage supervisé et non supervisé. Alors que l'apprentissage supervisé repose sur un ensemble de données avec des résultats connus, le RL est basé sur **l'apprentissage par l'expérience**. Par exemple, lorsque nous découvrons un jeu vidéo pour la première fois, nous commençons à jouer, même sans connaître les règles, et nous améliorons rapidement nos compétences simplement en jouant et en ajustant notre comportement.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Pour effectuer du RL, nous avons besoin de :

* Un **environnement** ou **simulateur** qui définit les règles du jeu. Nous devons pouvoir exécuter des expériences dans le simulateur et observer les résultats.
* Une **fonction de récompense**, qui indique à quel point notre expérience a été réussie. Dans le cas de l'apprentissage d'un jeu vidéo, la récompense serait notre score final.

En fonction de la fonction de récompense, nous devrions être capables d'ajuster notre comportement et d'améliorer nos compétences, afin de mieux jouer la prochaine fois. La principale différence entre les autres types d'apprentissage automatique et le RL est qu'en RL, nous ne savons généralement pas si nous gagnons ou perdons avant la fin du jeu. Ainsi, nous ne pouvons pas dire si un mouvement particulier est bon ou non - nous ne recevons une récompense qu'à la fin du jeu.

Pendant le RL, nous effectuons généralement de nombreuses expériences. Lors de chaque expérience, nous devons trouver un équilibre entre suivre la stratégie optimale que nous avons apprise jusqu'à présent (**exploitation**) et explorer de nouveaux états possibles (**exploration**).

## OpenAI Gym

Un excellent outil pour le RL est le [OpenAI Gym](https://gym.openai.com/) - un **environnement de simulation**, capable de simuler de nombreux environnements différents, allant des jeux Atari à la physique derrière l'équilibre d'un poteau. C'est l'un des environnements de simulation les plus populaires pour entraîner des algorithmes d'apprentissage par renforcement, et il est maintenu par [OpenAI](https://openai.com/).

> **Note** : Vous pouvez voir tous les environnements disponibles dans OpenAI Gym [ici](https://gym.openai.com/envs/#classic_control).

## Équilibrage du CartPole

Vous avez probablement déjà vu des dispositifs modernes d'équilibrage tels que le *Segway* ou les *gyroscooters*. Ils sont capables de s'équilibrer automatiquement en ajustant leurs roues en réponse à un signal provenant d'un accéléromètre ou d'un gyroscope. Dans cette section, nous allons apprendre à résoudre un problème similaire : équilibrer un poteau. Cela ressemble à la situation où un artiste de cirque doit équilibrer un poteau sur sa main - mais cet équilibrage ne se produit qu'en 1D.

Une version simplifiée de l'équilibrage est connue sous le nom de problème **CartPole**. Dans le monde du CartPole, nous avons un curseur horizontal qui peut se déplacer à gauche ou à droite, et l'objectif est d'équilibrer un poteau vertical au-dessus du curseur pendant qu'il se déplace.

<img alt="un CartPole" src="../../../../../translated_images/fr/cartpole.f52a67f27e058170.webp" width="200"/>

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

Chaque environnement peut être utilisé de la même manière :
* `env.reset` démarre une nouvelle expérience
* `env.step` effectue une étape de simulation. Il reçoit une **action** de l'**espace d'action**, et retourne une **observation** (de l'espace d'observation), ainsi qu'une récompense et un indicateur de fin.

Dans l'exemple ci-dessus, nous effectuons une action aléatoire à chaque étape, ce qui explique pourquoi la durée de vie de l'expérience est très courte :

![CartPole sans équilibre](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

L'objectif d'un algorithme de RL est d'entraîner un modèle - la **politique** &pi; - qui retournera l'action en réponse à un état donné. Nous pouvons également considérer la politique comme probabiliste, c'est-à-dire que pour tout état *s* et action *a*, elle retournera la probabilité &pi;(*a*|*s*) que nous devrions prendre *a* dans l'état *s*.

## Algorithme des gradients de politique

La manière la plus évidente de modéliser une politique est de créer un réseau neuronal qui prendra les états en entrée et retournera les actions correspondantes (ou plutôt les probabilités de toutes les actions). En un sens, cela serait similaire à une tâche de classification normale, avec une différence majeure : nous ne savons pas à l'avance quelles actions nous devrions prendre à chaque étape.

L'idée ici est d'estimer ces probabilités. Nous construisons un vecteur de **récompenses cumulées** qui montre notre récompense totale à chaque étape de l'expérience. Nous appliquons également un **rabais sur les récompenses** en multipliant les récompenses antérieures par un coefficient &gamma;=0.99, afin de diminuer l'importance des récompenses antérieures. Ensuite, nous renforçons les étapes de l'expérience qui génèrent des récompenses plus importantes.

> Apprenez-en davantage sur l'algorithme des gradients de politique et voyez-le en action dans le [notebook d'exemple](CartPole-RL-TF.ipynb).

## Algorithme Actor-Critic

Une version améliorée de l'approche des gradients de politique est appelée **Actor-Critic**. L'idée principale est que le réseau neuronal serait entraîné pour retourner deux choses :

* La politique, qui détermine quelle action entreprendre. Cette partie est appelée **acteur**.
* L'estimation de la récompense totale que nous pouvons espérer obtenir dans cet état - cette partie est appelée **critique**.

En un sens, cette architecture ressemble à un [GAN](../../4-ComputerVision/10-GANs/README.md), où nous avons deux réseaux qui s'entraînent l'un contre l'autre. Dans le modèle Actor-Critic, l'acteur propose l'action à entreprendre, et le critique essaie d'être critique et d'estimer le résultat. Cependant, notre objectif est d'entraîner ces réseaux en harmonie.

Parce que nous connaissons à la fois les récompenses cumulées réelles et les résultats retournés par le critique pendant l'expérience, il est relativement facile de construire une fonction de perte qui minimisera la différence entre eux. Cela nous donnerait la **perte du critique**. Nous pouvons calculer la **perte de l'acteur** en utilisant la même approche que dans l'algorithme des gradients de politique.

Après avoir exécuté l'un de ces algorithmes, nous pouvons nous attendre à ce que notre CartPole se comporte comme ceci :

![CartPole équilibré](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercices : Gradients de politique et RL Actor-Critic

Poursuivez votre apprentissage dans les notebooks suivants :

* [RL avec TensorFlow](CartPole-RL-TF.ipynb)
* [RL avec PyTorch](CartPole-RL-PyTorch.ipynb)

## Autres tâches de RL

L'apprentissage par renforcement est aujourd'hui un domaine de recherche en pleine croissance. Voici quelques exemples intéressants d'apprentissage par renforcement :

* Apprendre à un ordinateur à jouer à des **jeux Atari**. La difficulté de ce problème réside dans le fait que nous n'avons pas un état simple représenté sous forme de vecteur, mais plutôt une capture d'écran - et nous devons utiliser un CNN pour convertir cette image en vecteur de caractéristiques ou pour extraire des informations de récompense. Les jeux Atari sont disponibles dans le Gym.
* Apprendre à un ordinateur à jouer à des jeux de plateau, comme les échecs et le Go. Récemment, des programmes de pointe comme **Alpha Zero** ont été entraînés à partir de zéro par deux agents jouant l'un contre l'autre et s'améliorant à chaque étape.
* Dans l'industrie, le RL est utilisé pour créer des systèmes de contrôle à partir de simulations. Un service appelé [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) est spécialement conçu pour cela.

## Conclusion

Nous avons maintenant appris à entraîner des agents pour obtenir de bons résultats simplement en leur fournissant une fonction de récompense qui définit l'état souhaité du jeu, et en leur donnant l'opportunité d'explorer intelligemment l'espace de recherche. Nous avons essayé avec succès deux algorithmes et obtenu de bons résultats en relativement peu de temps. Cependant, ce n'est que le début de votre voyage dans le RL, et vous devriez envisager de suivre un cours dédié si vous souhaitez approfondir vos connaissances.

## 🚀 Défi

Explorez les applications listées dans la section "Autres tâches de RL" et essayez d'en implémenter une !

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Révision et auto-apprentissage

Apprenez-en davantage sur l'apprentissage par renforcement classique dans notre [programme d'apprentissage automatique pour débutants](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Regardez [cette excellente vidéo](https://www.youtube.com/watch?v=qv6UVOQ0F44) qui explique comment un ordinateur peut apprendre à jouer à Super Mario.

## Devoir : [Entraîner une voiture de montagne](lab/README.md)

Votre objectif pour ce devoir sera d'entraîner un environnement Gym différent - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

