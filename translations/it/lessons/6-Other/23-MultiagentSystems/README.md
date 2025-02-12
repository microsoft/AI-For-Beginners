# Systèmes Multi-Agents

L'une des manières possibles d'atteindre l'intelligence est l'approche dite **émergente** (ou **synergétique**), qui repose sur le fait que le comportement combiné de nombreux agents relativement simples peut donner lieu à un comportement global plus complexe (ou intelligent) du système dans son ensemble. Théoriquement, cela repose sur les principes de [l'Intelligence Collective](https://en.wikipedia.org/wiki/Collective_intelligence), de [l'Émergentisme](https://en.wikipedia.org/wiki/Global_brain) et de [la Cybernétique Évolutionnaire](https://en.wikipedia.org/wiki/Global_brain), qui affirment que les systèmes de niveau supérieur obtiennent une sorte de valeur ajoutée lorsqu'ils sont correctement combinés à partir de systèmes de niveau inférieur (le soi-disant *principe de transition de méta-système*).

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

Le domaine des **Systèmes Multi-Agents** a émergé dans l'IA dans les années 1990 en réponse à la croissance d'Internet et des systèmes distribués. L'un des manuels classiques de l'IA, [Intelligence Artificielle : Une Approche Moderne](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), se concentre sur la vision de l'IA classique du point de vue des systèmes multi-agents.

Au cœur de l'approche multi-agents se trouve la notion d'**Agent** - une entité qui évolue dans un **environnement**, qu'elle peut percevoir et sur lequel elle peut agir. C'est une définition très large, et il peut y avoir de nombreux types et classifications d'agents :

* Par leur capacité à raisonner :
   - Les agents **Réactifs** ont généralement un comportement simple de type demande-réponse
   - Les agents **Délibératifs** utilisent une sorte de raisonnement logique et/ou de capacités de planification
* Par l'endroit où l'agent exécute son code :
   - Les agents **Statiques** fonctionnent sur un nœud de réseau dédié
   - Les agents **Mobiles** peuvent déplacer leur code entre les nœuds de réseau
* Par leur comportement :
   - Les **agents passifs** n'ont pas d'objectifs spécifiques. Ces agents peuvent réagir à des stimuli externes, mais n'initieront aucune action eux-mêmes. 
   - Les **agents actifs** ont des objectifs qu'ils poursuivent
   - Les **agents cognitifs** impliquent une planification et un raisonnement complexes

Les systèmes multi-agents sont aujourd'hui utilisés dans un certain nombre d'applications :

* Dans les jeux, de nombreux personnages non-joueurs utilisent une forme d'IA et peuvent être considérés comme des agents intelligents
* Dans la production vidéo, le rendu de scènes 3D complexes impliquant des foules est généralement réalisé à l'aide de simulations multi-agents
* Dans la modélisation de systèmes, l'approche multi-agents est utilisée pour simuler le comportement d'un modèle complexe. Par exemple, cette approche a été utilisée avec succès pour prédire la propagation de la maladie COVID-19 dans le monde entier. Une approche similaire peut être utilisée pour modéliser le trafic dans la ville et observer comment il réagit aux changements des règles de circulation.
* Dans les systèmes d'automatisation complexes, chaque appareil peut agir comme un agent indépendant, ce qui rend l'ensemble du système moins monolithique et plus robuste.

Nous ne passerons pas beaucoup de temps à approfondir les systèmes multi-agents, mais considérons un exemple de **Modélisation Multi-Agent**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) est un environnement de modélisation multi-agent basé sur une version modifiée du langage de programmation [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Ce langage a été développé pour enseigner les concepts de programmation aux enfants, et il vous permet de contrôler un agent appelé **tortue**, qui peut se déplacer en laissant une trace derrière elle. Cela permet de créer des figures géométriques complexes, ce qui est une manière très visuelle de comprendre le comportement d'un agent.

Dans NetLogo, nous pouvons créer de nombreuses tortues en utilisant la commande `create-turtles`. Nous pouvons ensuite ordonner à toutes les tortues d'effectuer certaines actions (dans l'exemple ci-dessous - avancer de 10 points) :

```
create-turtles 10
ask turtles [
  forward 10
]
```

Bien sûr, il n'est pas intéressant que toutes les tortues fassent la même chose, donc nous pouvons `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` est le nom d'une race, et nous devons spécifier à la fois le mot au singulier et au pluriel, car différentes commandes utilisent différentes formes pour plus de clarté.

> ✅ Nous n'allons pas approfondir l'apprentissage du langage NetLogo lui-même - vous pouvez visiter le brillant [Dictionnaire Interactif pour Débutants de NetLogo](https://ccl.northwestern.edu/netlogo/bind/) si vous souhaitez en savoir plus.

Vous pouvez [télécharger](https://ccl.northwestern.edu/netlogo/download.shtml) et installer NetLogo pour l'essayer.

### Bibliothèque de Modèles

Une grande chose à propos de NetLogo est qu'il contient une bibliothèque de modèles fonctionnels que vous pouvez essayer. Allez dans **Fichier → Bibliothèque de Modèles**, et vous aurez de nombreuses catégories de modèles parmi lesquelles choisir.

<img alt="Bibliothèque de Modèles NetLogo" src="images/NetLogo-ModelLib.png" width="60%"/>

> Une capture d'écran de la bibliothèque de modèles par Dmitry Soshnikov

Vous pouvez ouvrir l'un des modèles, par exemple **Biologie → Flocking**.

### Principes Principaux

Après avoir ouvert le modèle, vous êtes dirigé vers l'écran principal de NetLogo. Voici un modèle d'exemple qui décrit la population de loups et de moutons, compte tenu des ressources finies (herbe).

![Écran Principal de NetLogo](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.it.png)

> Capture d'écran par Dmitry Soshnikov

Sur cet écran, vous pouvez voir :

* La section **Interface** qui contient :
  - Le champ principal, où vivent tous les agents
  - Différents contrôles : boutons, curseurs, etc.
  - Des graphiques que vous pouvez utiliser pour afficher les paramètres de la simulation
* L'onglet **Code** qui contient l'éditeur, où vous pouvez taper le programme NetLogo

Dans la plupart des cas, l'interface aura un bouton **Setup**, qui initialise l'état de la simulation, et un bouton **Go** qui démarre l'exécution. Ceux-ci sont gérés par les gestionnaires correspondants dans le code qui ressemblent à ceci :

```
to go [
...
]
```

Le monde de NetLogo se compose des objets suivants :

* **Agents** (tortues) qui peuvent se déplacer sur le champ et faire quelque chose. Vous commandez les agents en utilisant `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` pour faire quelque chose.
* **Observer** est un agent unique qui contrôle le monde. Tous les gestionnaires de boutons sont exécutés en *mode observateur*.

> ✅ La beauté d'un environnement multi-agent est que le code qui s'exécute en mode tortue ou en mode patch est exécuté en même temps par tous les agents en parallèle. Ainsi, en écrivant un peu de code et en programmant le comportement d'un agent individuel, vous pouvez créer un comportement complexe du système de simulation dans son ensemble.

### Flocking

Comme exemple de comportement multi-agent, considérons le **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Le flocking est un modèle complexe qui ressemble beaucoup à la façon dont les volées d'oiseaux volent. En les observant voler, vous pourriez penser qu'ils suivent une sorte d'algorithme collectif, ou qu'ils possèdent une forme d'*intelligence collective*. Cependant, ce comportement complexe émerge lorsque chaque agent individuel (dans ce cas, un *oiseau*) n'observe que quelques autres agents à une courte distance de lui, et suit trois règles simples :

* **Alignement** - il s'oriente vers la direction moyenne des agents voisins
* **Cohésion** - il essaie de s'orienter vers la position moyenne des voisins (*attraction à long terme*)
* **Séparation** - lorsqu'il s'approche trop des autres oiseaux, il essaie de s'éloigner (*répulsion à courte portée*)

Vous pouvez exécuter l'exemple de flocking et observer le comportement. Vous pouvez également ajuster des paramètres, tels que le *degré de séparation* ou le *champ de vision*, qui définit jusqu'où chaque oiseau peut voir. Notez que si vous réduisez le champ de vision à 0, tous les oiseaux deviennent aveugles et le flocking s'arrête. Si vous réduisez la séparation à 0, tous les oiseaux se regroupent en une ligne droite.

> ✅ Passez à l'onglet **Code** et voyez où les trois règles du flocking (alignement, cohésion et séparation) sont mises en œuvre dans le code. Notez comment nous ne faisons référence qu'aux agents qui sont en vue.

### Autres Modèles à Explorer

Il y a quelques modèles intéressants supplémentaires avec lesquels vous pouvez expérimenter :

* **Art → Feux d'Artifice** montre comment un feu d'artifice peut être considéré comme un comportement collectif de flux de feu individuels
* **Sciences Sociales → Trafic de Base** et **Sciences Sociales → Grille de Trafic** montrent le modèle du trafic urbain en 1D et en 2D avec ou sans feux de circulation. Chaque voiture dans la simulation suit les règles suivantes :
   - Si l'espace devant elle est vide - accélérer (jusqu'à une certaine vitesse maximale)
   - Si elle voit un obstacle devant - freiner (et vous pouvez ajuster jusqu'où un conducteur peut voir)
* **Sciences Sociales → Fête** montre comment les gens se regroupent lors d'une fête. Vous pouvez trouver la combinaison de paramètres qui conduit à la plus rapide augmentation du bonheur du groupe.

Comme vous pouvez le constater à partir de ces exemples, les simulations multi-agents peuvent être un moyen très utile de comprendre le comportement d'un système complexe composé d'individus qui suivent la même logique ou une logique similaire. Cela peut également être utilisé pour contrôler des agents virtuels, tels que les [PNJ](https://en.wikipedia.org/wiki/NPC) dans les jeux vidéo, ou des agents dans des mondes animés en 3D.

## Agents Délibératifs

Les agents décrits ci-dessus sont très simples, réagissant aux changements dans l'environnement à l'aide d'un certain type d'algorithme. En tant que tels, ils sont des **agents réactifs**. Cependant, parfois, les agents peuvent raisonner et planifier leurs actions, auquel cas on les appelle **délibératifs**.

Un exemple typique serait un agent personnel qui reçoit une instruction d'un humain pour réserver un voyage. Supposons qu'il existe de nombreux agents qui vivent sur Internet, qui peuvent l'aider. Il devrait alors contacter d'autres agents pour voir quels vols sont disponibles, quels sont les prix des hôtels pour différentes dates, et essayer de négocier le meilleur prix. Lorsque le plan de vacances est complet et confirmé par le propriétaire, il peut procéder à la réservation.

Pour cela, les agents doivent **communiquer**. Pour une communication réussie, ils ont besoin de :

* De **langages standard pour échanger des connaissances**, tels que le [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) et le [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Ces langages sont conçus sur la base de la [théorie des actes de langage](https://en.wikipedia.org/wiki/Speech_act).
* Ces langages devraient également inclure certains **protocoles de négociation**, basés sur différents **types d'enchères**.
* Une **ontologie commune** à utiliser, afin qu'ils fassent référence aux mêmes concepts en connaissant leur sémantique
* Un moyen de **découvrir** ce que différents agents peuvent faire, également basé sur une sorte d'ontologie

Les agents délibératifs sont beaucoup plus complexes que les réactifs, car ils ne réagissent pas seulement aux changements dans l'environnement, mais doivent également être capables d'*initier* des actions. L'une des architectures proposées pour les agents délibératifs est celle des agents de type Croyance-Désir-Intention (BDI) :

* Les **Croyances** forment un ensemble de connaissances sur l'environnement d'un agent. Cela peut être structuré sous la forme d'une base de connaissances ou d'un ensemble de règles qu'un agent peut appliquer à une situation spécifique dans l'environnement.
* Les **Désirs** définissent ce qu'un agent souhaite faire, c'est-à-dire ses objectifs. Par exemple, l'objectif de l'agent assistant personnel ci-dessus est de réserver un voyage, et l'objectif d'un agent hôtelier est de maximiser le profit.
* Les **Intentions** sont des actions spécifiques qu'un agent prévoit d'accomplir pour atteindre ses objectifs. Les actions modifient généralement l'environnement et entraînent une communication avec d'autres agents.

Il existe des plateformes disponibles pour construire des systèmes multi-agents, telles que [JADE](https://jade.tilab.com/). [Cet article](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) contient une revue des plateformes multi-agents, ainsi qu'une brève histoire des systèmes multi-agents et de leurs différents scénarios d'utilisation.

## Conclusion

Les systèmes multi-agents peuvent prendre des formes très différentes et être utilisés dans de nombreuses applications variées. Ils ont tous tendance à se concentrer sur le comportement plus simple d'un agent individuel, et à atteindre un comportement plus complexe de l'ensemble du système grâce à l'effet **synergétique**.

## 🚀 Défi

Prenez cette leçon dans le monde réel et essayez de conceptualiser un système multi-agent capable de résoudre un problème. Que devrait faire un système multi-agent pour optimiser un itinéraire de bus scolaire, par exemple ? Comment cela pourrait-il fonctionner dans une boulangerie ?

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Revue et Auto-Étude

Examinez l'utilisation de ce type de système dans l'industrie. Choisissez un domaine tel que la fabrication ou l'industrie du jeu vidéo et découvrez comment les systèmes multi-agents peuvent être utilisés pour résoudre des problèmes uniques.

## [Devoir NetLogo](assignment.md)

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.