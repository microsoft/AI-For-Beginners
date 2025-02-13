# Entraînement de Mountain Car pour s'échapper

Devoir de [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tâche

Votre objectif est d'entraîner l'agent RL à contrôler [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) dans l'environnement OpenAI. Vous êtes formé sur des données jusqu'en octobre 2023.

## L'environnement

L'environnement Mountain Car se compose de la voiture piégée à l'intérieur d'une vallée. Votre but est de sauter hors de la vallée et d'atteindre le drapeau. Les actions que vous pouvez effectuer sont d'accélérer vers la gauche, vers la droite, ou de ne rien faire. Vous pouvez observer la position de la voiture le long de l'axe x, ainsi que sa vitesse.

## Notebook de démarrage

Commencez le laboratoire en ouvrant [MountainCar.ipynb](../../../../../../lessons/6-Other/22-DeepRL/lab/MountainCar.ipynb)

## Conclusion

Vous devriez apprendre tout au long de ce laboratoire que l'adoption des algorithmes RL dans un nouvel environnement est souvent assez simple, car l'OpenAI Gym a la même interface pour tous les environnements, et les algorithmes ne dépendent donc pas largement de la nature de l'environnement. Vous pouvez même restructurer le code Python de manière à passer n'importe quel environnement à l'algorithme RL en tant que paramètre.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées découlant de l'utilisation de cette traduction.