# Détection de têtes avec le dataset Hollywood Heads

Travail pratique issu du [Curriculum AI pour les débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

Compter le nombre de personnes sur un flux vidéo de caméra de surveillance est une tâche importante qui permet d'estimer le nombre de visiteurs dans les magasins, les heures de pointe dans un restaurant, etc. Pour résoudre cette tâche, nous devons être capables de détecter les têtes humaines sous différents angles. Pour entraîner un modèle de détection d'objets à identifier les têtes humaines, nous pouvons utiliser le [dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Le Dataset

Le [dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contient 369 846 têtes humaines annotées dans 224 740 images extraites de films hollywoodiens. Il est fourni au format [PASCAL VOC](https://host.robots.ox.ac.uk/pascal/VOC/), où chaque image est accompagnée d'un fichier XML descriptif ressemblant à ceci :

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

Dans ce dataset, il n'y a qu'une seule classe d'objets `head`, et pour chaque tête, vous obtenez les coordonnées de la boîte englobante. Vous pouvez analyser les fichiers XML en utilisant des bibliothèques Python, ou utiliser [cette bibliothèque](https://pypi.org/project/pascal-voc/) pour travailler directement avec le format PASCAL VOC.

## Entraînement de la détection d'objets

Vous pouvez entraîner un modèle de détection d'objets en utilisant l'une des méthodes suivantes :

* Utiliser [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) et son API Python pour entraîner le modèle dans le cloud de manière programmatique. Custom Vision ne pourra pas utiliser plus de quelques centaines d'images pour entraîner le modèle, vous devrez donc limiter le dataset.
* Utiliser l'exemple du [tutoriel Keras](https://keras.io/examples/vision/retinanet/) pour entraîner un modèle RetinaNet.
* Utiliser le module intégré [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) dans torchvision.

## Conclusion

La détection d'objets est une tâche fréquemment requise dans l'industrie. Bien qu'il existe des services permettant de réaliser la détection d'objets (comme [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), il est important de comprendre comment fonctionne la détection d'objets et de savoir entraîner vos propres modèles.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.