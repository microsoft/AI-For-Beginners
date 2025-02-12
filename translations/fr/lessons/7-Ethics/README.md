# IA Éthique et Responsable

Vous avez presque terminé ce cours, et j'espère qu'à ce stade, vous comprenez clairement que l'IA repose sur un certain nombre de méthodes mathématiques formelles qui nous permettent de trouver des relations dans les données et d'entraîner des modèles pour reproduire certains aspects du comportement humain. À ce moment de l'histoire, nous considérons l'IA comme un outil très puissant pour extraire des modèles à partir des données et appliquer ces modèles pour résoudre de nouveaux problèmes.

## [Quiz pré-conférence](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Cependant, dans la science-fiction, nous voyons souvent des histoires où l'IA représente un danger pour l'humanité. En général, ces histoires tournent autour d'une sorte de rébellion de l'IA, lorsque l'IA décide de confronter les êtres humains. Cela implique que l'IA a une sorte d'émotion ou peut prendre des décisions imprévues par ses développeurs.

Le type d'IA que nous avons appris dans ce cours n'est rien d'autre qu'une arithmétique de grandes matrices. C'est un outil très puissant pour nous aider à résoudre nos problèmes, et comme tout autre outil puissant - il peut être utilisé à des fins bonnes ou mauvaises. Il est important de noter qu'il peut être *mal utilisé*.

## Principes de l'IA Responsable

Pour éviter cet usage accidentel ou intentionnel de l'IA, Microsoft énonce les importants [Principes de l'IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Les concepts suivants sous-tendent ces principes :

* **Équité** est liée au problème important des *biais de modèle*, qui peuvent être causés par l'utilisation de données biaisées pour l'entraînement. Par exemple, lorsque nous essayons de prédire la probabilité d'obtenir un emploi de développeur de logiciels pour une personne, le modèle est susceptible de donner une préférence plus élevée aux hommes - simplement parce que le jeu de données d'entraînement était probablement biaisé vers un public masculin. Nous devons équilibrer soigneusement les données d'entraînement et examiner le modèle pour éviter les biais, et nous assurer que le modèle prend en compte des caractéristiques plus pertinentes.
* **Fiabilité et Sécurité**. Par nature, les modèles d'IA peuvent faire des erreurs. Un réseau de neurones retourne des probabilités, et nous devons en tenir compte lors de la prise de décisions. Chaque modèle a une certaine précision et un certain rappel, et nous devons comprendre cela pour prévenir les dommages que de mauvais conseils peuvent causer.
* **Confidentialité et Sécurité** ont des implications spécifiques à l'IA. Par exemple, lorsque nous utilisons certaines données pour entraîner un modèle, ces données deviennent d'une certaine manière "intégrées" dans le modèle. D'une part, cela augmente la sécurité et la confidentialité, d'autre part - nous devons nous rappeler sur quelles données le modèle a été entraîné.
* **Inclusivité** signifie que nous ne construisons pas l'IA pour remplacer les gens, mais plutôt pour augmenter les capacités humaines et rendre notre travail plus créatif. Cela est également lié à l'équité, car lorsqu'il s'agit de communautés sous-représentées, la plupart des ensembles de données que nous collectons sont susceptibles d'être biaisés, et nous devons nous assurer que ces communautés sont incluses et correctement prises en charge par l'IA.
* **Transparence**. Cela inclut de s'assurer que nous sommes toujours clairs sur l'utilisation de l'IA. De plus, dans la mesure du possible, nous voulons utiliser des systèmes d'IA qui sont *interprétables*.
* **Responsabilité**. Lorsque les modèles d'IA prennent certaines décisions, il n'est pas toujours clair qui est responsable de ces décisions. Nous devons nous assurer que nous comprenons où se situe la responsabilité des décisions de l'IA. Dans la plupart des cas, nous voudrions inclure des êtres humains dans le processus de prise de décisions importantes, afin que des personnes réelles soient tenues responsables.

## Outils pour une IA Responsable

Microsoft a développé la [Boîte à outils pour une IA Responsable](https://github.com/microsoft/responsible-ai-toolbox) qui contient un ensemble d'outils :

* Tableau de bord d'interprétabilité (InterpretML)
* Tableau de bord d'équité (FairLearn)
* Tableau de bord d'analyse des erreurs
* Tableau de bord d'IA Responsable qui inclut

   - EconML - outil d'analyse causale, qui se concentre sur les questions de type "et si"
   - DiCE - outil d'analyse contrefactuelle qui vous permet de voir quelles caractéristiques doivent être modifiées pour affecter la décision du modèle

Pour plus d'informations sur l'éthique de l'IA, veuillez visiter [cette leçon](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) sur le programme d'apprentissage automatique qui inclut des exercices.

## Révision & Auto-apprentissage

Suivez ce [Parcours d'apprentissage](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) pour en savoir plus sur l'IA responsable.

## [Quiz post-conférence](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.