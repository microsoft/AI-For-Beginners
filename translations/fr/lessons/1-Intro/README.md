> Image par [Dmitry Soshnikov](http://soshnikov.com)

Au fil du temps, les ressources informatiques sont devenues moins chères et davantage de données sont devenues disponibles, ce qui a permis aux approches par réseaux de neurones de montrer d'excellentes performances en concurrence avec les êtres humains dans de nombreux domaines, tels que la vision par ordinateur ou la compréhension de la parole. Au cours de la dernière décennie, le terme Intelligence Artificielle a été principalement utilisé comme synonyme de Réseaux de Neurones, car la plupart des succès de l'IA dont nous entendons parler en dépendent.

Nous pouvons observer comment les approches ont évolué, par exemple, dans la création d'un programme d'échecs :

* Les premiers programmes d'échecs étaient basés sur la recherche – un programme essayait explicitement d'estimer les coups possibles d'un adversaire pour un certain nombre de coups suivants et sélectionnait un coup optimal basé sur la position optimale qui pouvait être atteinte en quelques coups. Cela a conduit au développement de l'algorithme de recherche dit [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Les stratégies de recherche fonctionnent bien vers la fin de la partie, où l'espace de recherche est limité par un petit nombre de coups possibles. Cependant, au début de la partie, l'espace de recherche est énorme, et l'algorithme peut être amélioré en apprenant des parties existantes entre joueurs humains. Les expériences ultérieures ont utilisé le raisonnement basé sur les cas, où le programme cherchait des cas dans la base de connaissances très similaires à la position actuelle dans le jeu.
* Les programmes modernes qui gagnent contre des joueurs humains sont basés sur des réseaux de neurones et sur l'[apprentissage par renforcement](https://en.wikipedia.org/wiki/Reinforcement_learning), où les programmes apprennent à jouer uniquement en jouant longtemps contre eux-mêmes et en apprenant de leurs propres erreurs – tout comme le font les êtres humains en apprenant à jouer aux échecs. Cependant, un programme informatique peut jouer beaucoup plus de parties en beaucoup moins de temps, et peut donc apprendre beaucoup plus rapidement.

✅ Faites un peu de recherche sur d'autres jeux auxquels l'IA a joué.

De même, nous pouvons voir comment l'approche pour créer des "programmes parlants" (qui pourraient passer le test de Turing) a évolué :

* Les premiers programmes de ce type, tels que [Eliza](https://en.wikipedia.org/wiki/ELIZA), étaient basés sur des règles grammaticales très simples et la reformulation de la phrase d'entrée en une question.
* Les assistants modernes, tels que Cortana, Siri ou Google Assistant, sont tous des systèmes hybrides qui utilisent des réseaux de neurones pour convertir la parole en texte et reconnaître notre intention, puis emploient un raisonnement ou des algorithmes explicites pour effectuer les actions requises.
* À l'avenir, nous pouvons nous attendre à un modèle entièrement basé sur des neurones capable de gérer le dialogue par lui-même. Les récents réseaux de neurones GPT et [Turing-NLG](https://turing.microsoft.com/) montrent un grand succès à cet égard.

> Image par Dmitry Soshnikov, [photo](https://unsplash.com/photos/r8LmVbUKgns) par [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Recherche récente en IA

L'énorme croissance récente de la recherche sur les réseaux de neurones a commencé vers 2010, lorsque de grands ensembles de données publics ont commencé à devenir disponibles. Une vaste collection d'images appelée [ImageNet](https://en.wikipedia.org/wiki/ImageNet), qui contient environ 14 millions d'images annotées, a donné naissance au [Défi de Reconnaissance Visuelle à Grande Échelle ImageNet](https://image-net.org/challenges/LSVRC/).

![Précision ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Image par [Dmitry Soshnikov](http://soshnikov.com)
En 2012, les [réseaux de neurones convolutionnels](../4-ComputerVision/07-ConvNets/README.md) ont été utilisés pour la première fois dans la classification d'images, ce qui a entraîné une réduction significative des erreurs de classification (passant de presque 30 % à 16,4 %). En 2015, l'architecture ResNet de Microsoft Research a [atteint une précision au niveau humain](https://doi.org/10.1109/ICCV.2015.123).

Depuis lors, les réseaux de neurones ont démontré un comportement très réussi dans de nombreuses tâches :

---

Année | Parité humaine atteinte
-----|--------
2015 | [Classification d'images](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Reconnaissance vocale conversationnelle](https://arxiv.org/abs/1610.05256)
2018 | [Traduction automatique](https://arxiv.org/abs/1803.05567) (Chinois vers Anglais)
2020 | [Légendes d'images](https://arxiv.org/abs/2009.13682)

Au cours des dernières années, nous avons été témoins de grands succès avec de grands modèles de langage, tels que BERT et GPT-3. Cela est principalement dû au fait qu'il existe beaucoup de données textuelles générales disponibles qui nous permettent de former des modèles pour capturer la structure et le sens des textes, de les préformer sur des collections de textes générales, puis de spécialiser ces modèles pour des tâches plus spécifiques. Nous en apprendrons davantage sur le [traitement du langage naturel](../5-NLP/README.md) plus tard dans ce cours.

## 🚀 Défi

Faites un tour d'internet pour déterminer où, selon vous, l'IA est utilisée de manière la plus efficace. Est-ce dans une application de cartographie, un service de reconnaissance vocale ou un jeu vidéo ? Renseignez-vous sur la manière dont le système a été construit.

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Revue et auto-apprentissage

Revoyez l'histoire de l'IA et du ML en lisant [cette leçon](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Prenez un élément du sketchnote en haut de cette leçon ou de celle-ci et recherchez-le plus en profondeur pour comprendre le contexte culturel qui informe son évolution.

**Devoir** : [Game Jam](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées découlant de l'utilisation de cette traduction.