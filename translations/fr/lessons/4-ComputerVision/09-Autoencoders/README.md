# Autoencodeurs

Lors de l'entraînement de CNN, l'un des problèmes est que nous avons besoin de beaucoup de données étiquetées. Dans le cas de la classification d'images, nous devons séparer les images en différentes classes, ce qui nécessite un effort manuel.

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Cependant, nous pourrions vouloir utiliser des données brutes (non étiquetées) pour entraîner des extracteurs de caractéristiques CNN, ce qui s'appelle **l'apprentissage auto-supervisé**. Au lieu d'étiquettes, nous utiliserons les images d'entraînement comme entrée et sortie du réseau. L'idée principale de l'**autoencodeur** est que nous aurons un **réseau encodeur** qui convertit l'image d'entrée en un **espace latent** (normalement, c'est juste un vecteur de taille plus petite), puis le **réseau décodeur**, dont le but serait de reconstruire l'image originale.

> ✅ Un [autoencodeur](https://wikipedia.org/wiki/Autoencoder) est "un type de réseau de neurones artificiels utilisé pour apprendre des codages efficaces de données non étiquetées."

Puisque nous entraînons un autoencodeur pour capturer autant d'informations que possible de l'image originale pour une reconstruction précise, le réseau essaie de trouver le meilleur **embedding** des images d'entrée pour capturer le sens.

![Diagramme AutoEncodeur](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.fr.jpg)

> Image provenant du [blog Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scénarios d'utilisation des Autoencodeurs

Bien que reconstruire des images originales ne semble pas utile en soi, il existe quelques scénarios où les autoencodeurs sont particulièrement utiles :

* **Réduction de la dimension des images pour la visualisation** ou **entraînement des embeddings d'images**. En général, les autoencodeurs donnent de meilleurs résultats que la PCA, car ils prennent en compte la nature spatiale des images et les caractéristiques hiérarchiques.
* **Dénuisage**, c'est-à-dire suppression du bruit de l'image. Comme le bruit contient beaucoup d'informations inutiles, l'autoencodeur ne peut pas tout intégrer dans un espace latent relativement petit, et il capture donc uniquement la partie importante de l'image. Lors de l'entraînement des débruiteurs, nous commençons avec des images originales et utilisons des images avec du bruit ajouté artificiellement comme entrée pour l'autoencodeur.
* **Super-résolution**, augmentation de la résolution de l'image. Nous commençons avec des images haute résolution et utilisons l'image de plus basse résolution comme entrée de l'autoencodeur.
* **Modèles génératifs**. Une fois que nous avons entraîné l'autoencodeur, la partie décodeur peut être utilisée pour créer de nouveaux objets à partir de vecteurs latents aléatoires.

## Autoencodeurs Variationnels (VAE)

Les autoencodeurs traditionnels réduisent d'une certaine manière la dimension des données d'entrée, en identifiant les caractéristiques importantes des images d'entrée. Cependant, les vecteurs latents n'ont souvent pas beaucoup de sens. En d'autres termes, en prenant le jeu de données MNIST comme exemple, il n'est pas facile de déterminer quels chiffres correspondent à différents vecteurs latents, car des vecteurs latents proches ne correspondent pas nécessairement aux mêmes chiffres.

D'autre part, pour entraîner des modèles *génératifs*, il est préférable d'avoir une certaine compréhension de l'espace latent. Cette idée nous conduit à l'**autoencodeur variationnel** (VAE).

Le VAE est l'autoencodeur qui apprend à prédire *la distribution statistique* des paramètres latents, appelée **distribution latente**. Par exemple, nous pouvons vouloir que les vecteurs latents soient distribués normalement avec une certaine moyenne z<sub>mean</sub> et un écart type z<sub>sigma</sub> (la moyenne et l'écart type sont tous deux des vecteurs d'une certaine dimensionnalité d). L'encodeur dans le VAE apprend à prédire ces paramètres, puis le décodeur prend un vecteur aléatoire de cette distribution pour reconstruire l'objet.

Pour résumer :

* À partir du vecteur d'entrée, nous prédisons `z_mean` et `z_log_sigma` (au lieu de prédire l'écart type lui-même, nous prédisons son logarithme)
* Nous échantillonnons un vecteur `sample` à partir de la distribution N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
* Le décodeur essaie de décoder l'image originale en utilisant `sample` comme vecteur d'entrée

<img src="images/vae.png" width="50%">

> Image provenant de [cet article de blog](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) par Isaak Dykeman

Les autoencodeurs variationnels utilisent une fonction de perte complexe qui se compose de deux parties :

* **Perte de reconstruction** est la fonction de perte qui montre à quel point une image reconstruite est proche de la cible (cela peut être l'erreur quadratique moyenne, ou MSE). C'est la même fonction de perte que dans les autoencodeurs normaux.
* **Perte KL**, qui garantit que les distributions des variables latentes restent proches de la distribution normale. Elle est basée sur la notion de [divergence Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - une métrique pour estimer à quel point deux distributions statistiques sont similaires.

Un avantage important des VAE est qu'ils nous permettent de générer de nouvelles images relativement facilement, car nous savons quelle distribution utiliser pour échantillonner les vecteurs latents. Par exemple, si nous entraînons un VAE avec un vecteur latent 2D sur MNIST, nous pouvons ensuite faire varier les composants du vecteur latent pour obtenir différents chiffres :

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Image par [Dmitry Soshnikov](http://soshnikov.com)

Observez comment les images se fondent les unes dans les autres, alors que nous commençons à obtenir des vecteurs latents provenant de différentes portions de l'espace des paramètres latents. Nous pouvons également visualiser cet espace en 2D :

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/>

> Image par [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exercices : Autoencodeurs

Apprenez-en davantage sur les autoencodeurs dans ces carnets correspondants :

* [Autoencodeurs dans TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencodeurs dans PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Propriétés des Autoencodeurs

* **Spécifique aux données** - ils ne fonctionnent bien qu'avec le type d'images sur lequel ils ont été entraînés. Par exemple, si nous entraînons un réseau de super-résolution sur des fleurs, il ne fonctionnera pas bien sur des portraits. Cela est dû au fait que le réseau peut produire une image de plus haute résolution en prenant des détails fins des caractéristiques apprises à partir du jeu de données d'entraînement.
* **Avec perte** - l'image reconstruite n'est pas la même que l'image originale. La nature de la perte est définie par la *fonction de perte* utilisée pendant l'entraînement.
* Fonctionne sur **des données non étiquetées**.

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Conclusion

Dans cette leçon, vous avez appris les différents types d'autoencodeurs disponibles pour le scientifique de l'IA. Vous avez appris à les construire et à les utiliser pour reconstruire des images. Vous avez également appris sur le VAE et comment l'utiliser pour générer de nouvelles images.

## 🚀 Défi

Dans cette leçon, vous avez appris à utiliser des autoencodeurs pour des images. Mais ils peuvent également être utilisés pour la musique ! Découvrez le projet [MusicVAE](https://magenta.tensorflow.org/music-vae) du projet Magenta, qui utilise des autoencodeurs pour apprendre à reconstruire de la musique. Faites quelques [expériences](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) avec cette bibliothèque pour voir ce que vous pouvez créer.

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revue & Auto-apprentissage

Pour référence, lisez-en plus sur les autoencodeurs dans ces ressources :

* [Construire des Autoencodeurs dans Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Article de blog sur NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencodeurs Variationnels Expliqués](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencodeurs Variationnels Conditionnels](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Devoir

À la fin de [ce carnet utilisant TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), vous trouverez une 'tâche' - utilisez ceci comme votre devoir.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des erreurs d'interprétation résultant de l'utilisation de cette traduction.