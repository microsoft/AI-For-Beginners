# Représentation des connaissances et systèmes experts

![Résumé du contenu de l'IA symbolique](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.it.png)

> Schéma par [Tomomi Imura](https://twitter.com/girlie_mac)

La quête de l'intelligence artificielle repose sur la recherche de connaissances, pour donner un sens au monde de manière similaire à celle des humains. Mais comment procéder ?

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Au début de l'IA, l'approche descendante pour créer des systèmes intelligents (discutée dans la leçon précédente) était populaire. L'idée était d'extraire les connaissances des personnes dans une forme lisible par machine, puis de les utiliser pour résoudre automatiquement des problèmes. Cette approche reposait sur deux grandes idées :

* Représentation des connaissances
* Raisonnement

## Représentation des connaissances

L'un des concepts importants de l'IA symbolique est la **connaissance**. Il est essentiel de différencier la connaissance de *l'information* ou *des données*. Par exemple, on peut dire que les livres contiennent des connaissances, car on peut les étudier et devenir un expert. Cependant, ce que contiennent les livres est en réalité appelé *données*, et en lisant ces livres et en intégrant ces données dans notre modèle du monde, nous convertissons ces données en connaissances.

> ✅ **La connaissance** est quelque chose qui est contenu dans notre esprit et représente notre compréhension du monde. Elle est obtenue par un processus d'**apprentissage** actif, qui intègre des morceaux d'information que nous recevons dans notre modèle actif du monde.

Le plus souvent, nous ne définissons pas strictement la connaissance, mais nous l'alignons avec d'autres concepts connexes en utilisant la [Pyramide DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Elle contient les concepts suivants :

* **Données** : quelque chose représenté sur un support physique, tel qu'un texte écrit ou des mots prononcés. Les données existent indépendamment des êtres humains et peuvent être transmises entre les personnes.
* **Information** : c'est ainsi que nous interprétons les données dans notre esprit. Par exemple, lorsque nous entendons le mot *ordinateur*, nous avons une certaine compréhension de ce que c'est.
* **Connaissance** : c'est l'information intégrée dans notre modèle du monde. Par exemple, une fois que nous apprenons ce qu'est un ordinateur, nous commençons à avoir des idées sur son fonctionnement, son coût et ses utilisations possibles. Ce réseau de concepts interconnectés forme notre connaissance.
* **Sagesse** : c'est encore un niveau supplémentaire de notre compréhension du monde, et cela représente *la méta-connaissance*, c'est-à-dire une notion sur comment et quand la connaissance doit être utilisée.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Image [de Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), par Longlivetheux - Travail personnel, CC BY-SA 4.0*

Ainsi, le problème de la **représentation des connaissances** est de trouver un moyen efficace de représenter les connaissances à l'intérieur d'un ordinateur sous forme de données, afin de les rendre automatiquement utilisables. Cela peut être vu comme un spectre :

![Spectre de la représentation des connaissances](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.it.png)

> Image par [Dmitry Soshnikov](http://soshnikov.com)

* À gauche, il y a des types très simples de représentations des connaissances qui peuvent être efficacement utilisés par les ordinateurs. Le plus simple est algorithmique, lorsque la connaissance est représentée par un programme informatique. Cependant, ce n'est pas la meilleure façon de représenter la connaissance, car elle n'est pas flexible. La connaissance dans notre esprit est souvent non-algorithmique.
* À droite, il y a des représentations telles que le texte naturel. C'est la plus puissante, mais elle ne peut pas être utilisée pour le raisonnement automatique.

> ✅ Pensez un instant à la façon dont vous représentez la connaissance dans votre esprit et la convertissez en notes. Existe-t-il un format particulier qui fonctionne bien pour vous afin d'aider à la rétention ?

## Classification des représentations des connaissances informatiques

Nous pouvons classer différentes méthodes de représentation des connaissances informatiques dans les catégories suivantes :

* **Représentations en réseau** : basées sur le fait que nous avons un réseau de concepts interconnectés dans notre esprit. Nous pouvons essayer de reproduire ces mêmes réseaux sous forme de graphique à l'intérieur d'un ordinateur - un soi-disant **réseau sémantique**.

1. **Triplets Objet-Attribut-Valeur** ou **paires attribut-valeur**. Étant donné qu'un graphique peut être représenté à l'intérieur d'un ordinateur sous forme de liste de nœuds et d'arêtes, nous pouvons représenter un réseau sémantique par une liste de triplets, contenant des objets, des attributs et des valeurs. Par exemple, nous construisons les triplets suivants sur les langages de programmation :

Objet | Attribut | Valeur
-------|-----------|------
Python | est | Langage-Non-Typé
Python | inventé-par | Guido van Rossum
Python | syntaxe-bloc | indentation
Langage-Non-Typé | n'a pas | définitions de type

> ✅ Réfléchissez à la manière dont les triplets peuvent être utilisés pour représenter d'autres types de connaissances.

2. **Représentations hiérarchiques** : mettent en avant le fait que nous créons souvent une hiérarchie d'objets dans notre esprit. Par exemple, nous savons que le canari est un oiseau, et que tous les oiseaux ont des ailes. Nous avons également une idée de la couleur qu'un canari a généralement et de sa vitesse de vol.

   - **Représentation par cadre** : basée sur la représentation de chaque objet ou classe d'objets sous forme de **cadre** qui contient des **emplacements**. Les emplacements ont des valeurs par défaut possibles, des restrictions de valeur ou des procédures stockées qui peuvent être appelées pour obtenir la valeur d'un emplacement. Tous les cadres forment une hiérarchie similaire à une hiérarchie d'objets dans les langages de programmation orientés objet.
   - **Scénarios** : sont une sorte spéciale de cadres qui représentent des situations complexes pouvant se dérouler dans le temps.

**Python**

Emplacement | Valeur | Valeur par défaut | Intervalle |
-----|-------|---------------|----------|
Nom | Python | | |
Est-Un | Langage-Non-Typé | | |
Cas de Variable | | CamelCase | |
Longueur du Programme | | | 5-5000 lignes |
Syntaxe de Bloc | Indentation | | |

3. **Représentations procédurales** : basées sur la représentation de la connaissance par une liste d'actions pouvant être exécutées lorsqu'une certaine condition se produit.
   - Les règles de production sont des déclarations si-alors qui nous permettent de tirer des conclusions. Par exemple, un médecin peut avoir une règle disant que **SI** un patient a une forte fièvre **OU** un taux élevé de protéine C-réactive dans un test sanguin **ALORS** il a une inflammation. Une fois que nous rencontrons l'une des conditions, nous pouvons tirer une conclusion sur l'inflammation, puis l'utiliser dans un raisonnement ultérieur.
   - Les algorithmes peuvent être considérés comme une autre forme de représentation procédurale, bien qu'ils ne soient presque jamais utilisés directement dans les systèmes basés sur la connaissance.

4. **Logique** : a été initialement proposée par Aristote comme un moyen de représenter la connaissance humaine universelle.
   - La logique des prédicats, en tant que théorie mathématique, est trop riche pour être calculable, donc un sous-ensemble est normalement utilisé, comme les clauses Horn utilisées dans Prolog.
   - La logique descriptive est une famille de systèmes logiques utilisés pour représenter et raisonner sur des hiérarchies d'objets et des représentations de connaissances distribuées telles que le *web sémantique*.

## Systèmes experts

L'un des premiers succès de l'IA symbolique a été les soi-disant **systèmes experts** - des systèmes informatiques conçus pour agir en tant qu'expert dans un domaine de problème limité. Ils étaient basés sur une **base de connaissances** extraite d'un ou plusieurs experts humains, et contenaient un **moteur d'inférence** qui effectuait un raisonnement sur cette base.

![Architecture humaine](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.it.png) | ![Système basé sur la connaissance](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.it.png)
---------------------------------------------|------------------------------------------------
Structure simplifiée d'un système nerveux humain | Architecture d'un système basé sur la connaissance

Les systèmes experts sont construits comme le système de raisonnement humain, qui contient de la **mémoire à court terme** et de la **mémoire à long terme**. De même, dans les systèmes basés sur la connaissance, nous distinguons les composants suivants :

* **Mémoire de problème** : contient les connaissances sur le problème actuellement résolu, c'est-à-dire la température ou la pression artérielle d'un patient, s'il a une inflammation ou non, etc. Cette connaissance est également appelée **connaissance statique**, car elle contient un instantané de ce que nous savons actuellement sur le problème - l'état du *problème*.
* **Base de connaissances** : représente la connaissance à long terme sur un domaine de problème. Elle est extraite manuellement d'experts humains et ne change pas d'une consultation à l'autre. Parce qu'elle nous permet de naviguer d'un état de problème à un autre, elle est également appelée **connaissance dynamique**.
* **Moteur d'inférence** : orchestre tout le processus de recherche dans l'espace des états de problème, posant des questions à l'utilisateur lorsque cela est nécessaire. Il est également responsable de la recherche des bonnes règles à appliquer à chaque état.

Prenons comme exemple le système expert suivant pour déterminer un animal en fonction de ses caractéristiques physiques :

![Arbre AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.it.png)

> Image par [Dmitry Soshnikov](http://soshnikov.com)

Ce diagramme est appelé un **arbre AND-OR**, et c'est une représentation graphique d'un ensemble de règles de production. Dessiner un arbre est utile au début de l'extraction de connaissances de l'expert. Pour représenter les connaissances à l'intérieur de l'ordinateur, il est plus pratique d'utiliser des règles :

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Vous pouvez remarquer que chaque condition du côté gauche de la règle et l'action sont essentiellement des triplets objet-attribut-valeur (OAV). La **mémoire de travail** contient l'ensemble des triplets OAV qui correspondent au problème actuellement résolu. Un **moteur de règles** recherche les règles pour lesquelles une condition est satisfaite et les applique, ajoutant un autre triplet à la mémoire de travail.

> ✅ Écrivez votre propre arbre AND-OR sur un sujet qui vous plaît !

### Inférence avant vs. Inférence arrière

Le processus décrit ci-dessus est appelé **inférence avant**. Il commence avec certaines données initiales sur le problème disponibles dans la mémoire de travail, puis exécute la boucle de raisonnement suivante :

1. Si l'attribut cible est présent dans la mémoire de travail - arrêtez et donnez le résultat
2. Recherchez toutes les règles dont la condition est actuellement satisfaite - obtenez l'**ensemble de conflits** des règles.
3. Effectuez la **résolution de conflits** - sélectionnez une règle qui sera exécutée à cette étape. Il pourrait y avoir différentes stratégies de résolution de conflits :
   - Sélectionnez la première règle applicable dans la base de connaissances
   - Sélectionnez une règle aléatoire
   - Sélectionnez une règle *plus spécifique*, c'est-à-dire celle qui répond à la plupart des conditions dans le "côté gauche" (LHS)
4. Appliquez la règle sélectionnée et insérez un nouveau morceau de connaissance dans l'état du problème
5. Répétez à partir de l'étape 1.

Cependant, dans certains cas, nous pourrions vouloir commencer avec une connaissance vide du problème et poser des questions qui nous aideront à arriver à la conclusion. Par exemple, lors d'un diagnostic médical, nous ne réalisons généralement pas toutes les analyses médicales à l'avance avant de commencer à diagnostiquer le patient. Nous préférons plutôt effectuer des analyses lorsqu'une décision doit être prise.

Ce processus peut être modélisé en utilisant l'**inférence arrière**. Il est dirigé par le **but** - la valeur d'attribut que nous cherchons à trouver :

1. Sélectionnez toutes les règles qui peuvent nous donner la valeur d'un but (c'est-à-dire avec le but sur le RHS ("côté droit")) - un ensemble de conflits
2. S'il n'y a pas de règles pour cet attribut, ou s'il y a une règle disant que nous devons demander la valeur à l'utilisateur - demandez-la, sinon :
3. Utilisez la stratégie de résolution de conflits pour sélectionner une règle que nous utiliserons comme *hypothèse* - nous allons essayer de la prouver
4. Répétez de manière récurrente le processus pour tous les attributs dans le LHS de la règle, essayant de les prouver comme des buts
5. Si à un moment donné le processus échoue - utilisez une autre règle à l'étape 3.

> ✅ Dans quelles situations l'inférence avant est-elle plus appropriée ? Et l'inférence arrière ?

### Mise en œuvre des systèmes experts

Les systèmes experts peuvent être mis en œuvre à l'aide de différents outils :

* En les programmant directement dans un langage de programmation de haut niveau. Ce n'est pas la meilleure idée, car le principal avantage d'un système basé sur la connaissance est que la connaissance est séparée de l'inférence, et potentiellement un expert du domaine du problème devrait être capable d'écrire des règles sans comprendre les détails du processus d'inférence.
* En utilisant une **coquille de systèmes experts**, c'est-à-dire un système spécifiquement conçu pour être peuplé de connaissances à l'aide d'un certain langage de représentation des connaissances.

## ✍️ Exercice : Inférence animale

Voir [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) pour un exemple de mise en œuvre d'un système expert d'inférence avant et arrière.

> **Remarque** : Cet exemple est assez simple et ne donne qu'une idée de ce à quoi ressemble un système expert. Une fois que vous commencez à créer un tel système, vous remarquerez un comportement *intelligent* de sa part seulement lorsque vous atteindrez un certain nombre de règles, autour de 200+. À un moment donné, les règles deviennent trop complexes pour garder toutes en tête, et à ce stade, vous pourriez commencer à vous demander pourquoi un système prend certaines décisions. Cependant, la caractéristique importante des systèmes basés sur la connaissance est que vous pouvez toujours *expliquer* exactement comment l'une des décisions a été prise.

## Ontologies et Web Sémantique

À la fin du 20ème siècle, il y a eu une initiative visant à utiliser la représentation des connaissances pour annoter les ressources Internet, afin qu'il soit possible de trouver des ressources correspondant à des requêtes très spécifiques. Ce mouvement a été appelé **Web Sémantique**, et il reposait sur plusieurs concepts :

- Une représentation de connaissance spéciale basée sur les **[logiques de description](https://en.wikipedia.org/wiki/Description_logic)** (DL). Elle est similaire à la représentation de connaissance par cadre, car elle construit une hiérarchie d'objets avec des propriétés, mais elle a une sémantique logique formelle et une inférence. Il existe toute une famille de DL qui équilibre expressivité et complexité algorithmique de l'inférence.
- Représentation de connaissance distribuée, où tous les concepts sont représentés par un identifiant URI global, ce qui permet de créer des hiérarchies de connaissances qui s'étendent sur Internet.
- Une famille de langages basés sur XML pour la description des connaissances : RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Un concept central du Web Sémantique est le concept d'**Ontologie**. Cela fait référence à une spécification explicite d'un domaine de problème utilisant une certaine représentation formelle des connaissances. La plus simple des ontologies peut être juste une hiérarchie d'objets dans un domaine de problème, mais des ontologies plus complexes incluront des règles qui peuvent être utilisées pour l'inférence.

Dans le web sémantique, toutes les représentations sont basées sur des triplets. Chaque objet et chaque relation sont identifiés de manière unique par l'URI. Par exemple, si nous voulons affirmer le fait que ce curriculum IA a été développé par Dmitry Soshnikov le 1er janvier 2022 - voici les triplets que nous pouvons utiliser :

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Ici `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` sont des URI bien connues et universellement acceptées pour exprimer les concepts de *créateur* et de *date de création*.

Dans un cas plus complexe, si nous voulons définir une liste de créateurs, nous pouvons utiliser certaines structures de données définies dans RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagrammes ci-dessus par [Dmitry Soshnikov](http://soshnikov.com)

Les progrès réalisés dans la construction du Web Sémantique ont été quelque peu ralentis par le succès des moteurs de recherche et des techniques de traitement du langage naturel, qui permettent d'extraire des données structurées à partir de texte. Cependant, dans certains domaines, il y a encore des efforts significatifs pour maintenir des ontologies et des bases de connaissances. Quelques projets à noter :

* [WikiData](https://wikidata.org/) est une collection de bases de connaissances lisibles par machine associées à Wikipedia. La plupart des données sont extraites des *InfoBoxes* de Wikipedia, des morceaux de contenu structuré à l'intérieur des pages Wikipedia. Vous pouvez [interroger](https://query.wikidata.org/) wikidata en SPARQL, un langage de requête spécial pour le Web Sémantique. Voici un exemple de requête qui affiche les couleurs d'yeux les plus populaires chez les humains :

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) est un autre effort similaire à WikiData.

> ✅ Si vous souhaitez expérimenter la construction de vos propres ontologies, ou ouvrir des ontologies existantes, il existe un excellent éditeur d'ontologies visuel appelé [Protégé](https://protege.stanford.edu/

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.