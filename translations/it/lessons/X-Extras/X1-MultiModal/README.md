# Réseaux Multi-Modal

Après le succès des modèles transformer pour résoudre des tâches de traitement du langage naturel, des architectures similaires ont été appliquées aux tâches de vision par ordinateur. Il y a un intérêt croissant à construire des modèles qui *combinent* les capacités de vision et de langage naturel. L'une de ces tentatives a été réalisée par OpenAI, et elle s'appelle CLIP et DALL.E.

## Pré-Formation d'Image Contrastive (CLIP)

L'idée principale de CLIP est de pouvoir comparer des invites textuelles avec une image et de déterminer à quel point l'image correspond à l'invite.

![Architecture CLIP](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.it.png)

> *Image provenant de [cet article de blog](https://openai.com/blog/clip/)*

Le modèle est entraîné sur des images obtenues sur Internet et leurs légendes. Pour chaque lot, nous prenons N paires de (image, texte) et les convertissons en certaines représentations vectorielles I et T. Ces représentations sont ensuite appariées. La fonction de perte est définie pour maximiser la similarité cosinus entre les vecteurs correspondant à une paire (par exemple, I et T), et minimiser la similarité cosinus entre toutes les autres paires. C'est la raison pour laquelle cette approche est appelée **contrastive**.

Le modèle/bibliothèque CLIP est disponible sur [OpenAI GitHub](https://github.com/openai/CLIP). L'approche est décrite dans [cet article de blog](https://openai.com/blog/clip/), et plus en détail dans [ce document](https://arxiv.org/pdf/2103.00020.pdf).

Une fois que ce modèle est pré-entraîné, nous pouvons lui donner un lot d'images et un lot d'invites textuelles, et il retournera un tenseur avec des probabilités. CLIP peut être utilisé pour plusieurs tâches :

**Classification d'Image**

Supposons que nous devions classer des images entre, disons, des chats, des chiens et des humains. Dans ce cas, nous pouvons donner au modèle une image et une série d'invites textuelles : "*une image d'un chat*", "*une image d'un chien*", "*une image d'un humain*". Dans le vecteur résultant de 3 probabilités, nous devons simplement sélectionner l'index avec la valeur la plus élevée.

![CLIP pour la Classification d'Image](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.it.png)

> *Image provenant de [cet article de blog](https://openai.com/blog/clip/)*

**Recherche d'Image Basée sur du Texte**

Nous pouvons également faire l'inverse. Si nous avons une collection d'images, nous pouvons passer cette collection au modèle, et une invite textuelle - cela nous donnera l'image qui est la plus similaire à l'invite donnée.

## ✍️ Exemple : [Utilisation de CLIP pour la Classification d'Image et la Recherche d'Image](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Ouvrez le notebook [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) pour voir CLIP en action.

## Génération d'Image avec VQGAN+ CLIP

CLIP peut également être utilisé pour la **génération d'images** à partir d'une invite textuelle. Pour ce faire, nous avons besoin d'un **modèle générateur** qui sera capable de générer des images basées sur une certaine entrée vectorielle. L'un de ces modèles s'appelle [VQGAN](https://compvis.github.io/taming-transformers/) (GAN à Quantification Vectorielle).

Les principales idées de VQGAN qui le différencient d'un GAN ordinaire sont les suivantes :
* Utiliser une architecture transformer autoregressive pour générer une séquence de parties visuelles riches en contexte qui composent l'image. Ces parties visuelles sont à leur tour apprises par un [CNN](../../4-ComputerVision/07-ConvNets/README.md).
* Utiliser un discriminateur de sous-image qui détecte si des parties de l'image sont "réelles" ou "fausses" (contrairement à l'approche "tout ou rien" dans un GAN traditionnel).

En savoir plus sur VQGAN sur le site [Taming Transformers](https://compvis.github.io/taming-transformers/).

Une des différences importantes entre VQGAN et un GAN traditionnel est que ce dernier peut produire une image décente à partir de n'importe quel vecteur d'entrée, tandis que VQGAN est susceptible de produire une image qui ne serait pas cohérente. Ainsi, nous devons guider davantage le processus de création d'image, et cela peut être fait en utilisant CLIP.

![Architecture VQGAN+CLIP](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.it.png)

Pour générer une image correspondant à une invite textuelle, nous commençons avec un vecteur d'encodage aléatoire qui est passé à travers VQGAN pour produire une image. Ensuite, CLIP est utilisé pour produire une fonction de perte qui montre à quel point l'image correspond à l'invite textuelle. L'objectif est alors de minimiser cette perte, en utilisant la rétropropagation pour ajuster les paramètres du vecteur d'entrée.

Une excellente bibliothèque qui implémente VQGAN+CLIP est [Pixray](http://github.com/pixray/pixray).

![Image produite par Pixray](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.it.png) |  ![Image produite par pixray](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.it.png) | ![Image produite par Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.it.png)
----|----|----
Image générée à partir de l'invite *un gros plan d'un portrait aquarelle d'un jeune enseignant de littérature avec un livre* | Image générée à partir de l'invite *un gros plan d'un portrait à l'huile d'une jeune enseignante de sciences informatiques avec un ordinateur* | Image générée à partir de l'invite *un gros plan d'un portrait à l'huile d'un vieux professeur de mathématiques devant un tableau noir*

> Images de la collection **Enseignants Artificiels** par [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E est une version de GPT-3 entraînée pour générer des images à partir d'invites. Il a été entraîné avec 12 milliards de paramètres.

Contrairement à CLIP, DALL-E reçoit à la fois le texte et l'image comme un seul flux de jetons pour les images et le texte. Par conséquent, à partir de plusieurs invites, vous pouvez générer des images basées sur le texte.

### [DALL-E 2](https://openai.com/dall-e-2)
La principale différence entre DALL-E 1 et 2 est qu'il génère des images et des œuvres d'art plus réalistes.

Exemples de générations d'images avec DALL-E :
![Image produite par Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.it.png) |  ![Image produite par pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.it.png) | ![Image produite par Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.it.png)
----|----|----
Image générée à partir de l'invite *un gros plan d'un portrait aquarelle d'un jeune enseignant de littérature avec un livre* | Image générée à partir de l'invite *un gros plan d'un portrait à l'huile d'une jeune enseignante de sciences informatiques avec un ordinateur* | Image générée à partir de l'invite *un gros plan d'un portrait à l'huile d'un vieux professeur de mathématiques devant un tableau noir*

## Références

* Document VQGAN : [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Document CLIP : [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.