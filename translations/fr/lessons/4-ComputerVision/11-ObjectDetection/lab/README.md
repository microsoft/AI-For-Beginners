# Détection de têtes utilisant le jeu de données Hollywood Heads

Devoir de [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tâche

Compter le nombre de personnes sur le flux de caméra de surveillance vidéo est une tâche importante qui nous permettra d'estimer le nombre de visiteurs dans des magasins, les heures d'affluence dans un restaurant, etc. Pour résoudre cette tâche, nous devons être capables de détecter des têtes humaines sous différents angles. Pour entraîner un modèle de détection d'objets à détecter des têtes humaines, nous pouvons utiliser le [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Le Jeu de Données

Le [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contient 369 846 têtes humaines annotées dans 224 740 images de films hollywoodiens. Il est fourni au format [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), où pour chaque image, il y a également un fichier de description XML qui ressemble à ceci :

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

Dans ce jeu de données, il n'y a qu'une seule classe d'objets `head`, et pour chaque tête, vous obtenez les coordonnées de la boîte englobante. Vous pouvez analyser le XML en utilisant des bibliothèques Python, ou utiliser [cette bibliothèque](https://pypi.org/project/pascal-voc/) pour traiter directement le format PASCAL VOC.

## Entraînement de la Détection d'Objets

Vous pouvez entraîner un modèle de détection d'objets en utilisant l'une des méthodes suivantes :

* Utiliser [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) et son API Python pour entraîner le modèle de manière programmatique dans le cloud. La vision personnalisée ne pourra pas utiliser plus de quelques centaines d'images pour entraîner le modèle, vous devrez donc peut-être limiter le jeu de données.
* Utiliser l'exemple du [tutoriel Keras](https://keras.io/examples/vision/retinanet/) pour entraîner le modèle RetunaNet.
* Utiliser le module intégré [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) dans torchvision.

## Conclusion

La détection d'objets est une tâche fréquemment requise dans l'industrie. Bien qu'il existe des services qui peuvent être utilisés pour effectuer la détection d'objets (comme [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), il est important de comprendre comment fonctionne la détection d'objets et d'être capable d'entraîner vos propres modèles.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des erreurs d'interprétation résultant de l'utilisation de cette traduction.