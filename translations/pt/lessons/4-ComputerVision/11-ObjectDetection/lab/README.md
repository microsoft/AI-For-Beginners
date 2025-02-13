# Detecção de Cabeças usando o Conjunto de Dados Hollywood Heads

Tarefa do [Currículo AI para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Contar o número de pessoas em uma transmissão de câmera de vigilância é uma tarefa importante que nos permitirá estimar o número de visitantes em lojas, horários de pico em restaurantes, etc. Para resolver essa tarefa, precisamos ser capazes de detectar cabeças humanas de diferentes ângulos. Para treinar um modelo de detecção de objetos para detectar cabeças humanas, podemos usar o [Conjunto de Dados Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## O Conjunto de Dados

O [Conjunto de Dados Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contém 369.846 cabeças humanas anotadas em 224.740 quadros de filmes de Hollywood. Ele é fornecido no formato [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), onde para cada imagem também há um arquivo de descrição XML que se parece com isto:

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

Neste conjunto de dados, há apenas uma classe de objetos `head`, e para cada cabeça, você obtém as coordenadas da caixa delimitadora. Você pode analisar XML usando bibliotecas Python ou usar [esta biblioteca](https://pypi.org/project/pascal-voc/) para lidar diretamente com o formato PASCAL VOC.

## Treinamento de Detecção de Objetos

Você pode treinar um modelo de detecção de objetos usando uma das seguintes maneiras:

* Usando [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) e sua API Python para treinar programaticamente o modelo na nuvem. A visão personalizada não conseguirá usar mais do que algumas centenas de imagens para treinar o modelo, então você pode precisar limitar o conjunto de dados.
* Usando o exemplo do [tutorial Keras](https://keras.io/examples/vision/retinanet/) para treinar o modelo RetunaNet.
* Usando o módulo embutido [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) na torchvision.

## Conclusão

A detecção de objetos é uma tarefa frequentemente requerida na indústria. Embora existam alguns serviços que podem ser usados para realizar a detecção de objetos (como [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), é importante entender como a detecção de objetos funciona e ser capaz de treinar seus próprios modelos.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.