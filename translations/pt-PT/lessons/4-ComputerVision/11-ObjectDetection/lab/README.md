# Deteção de Cabeças usando o Hollywood Heads Dataset

Trabalho prático do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Contar o número de pessoas num fluxo de vídeo de uma câmara de vigilância é uma tarefa importante que nos permite estimar o número de visitantes em lojas, as horas de maior movimento num restaurante, etc. Para resolver esta tarefa, precisamos de ser capazes de detetar cabeças humanas a partir de diferentes ângulos. Para treinar um modelo de deteção de objetos para identificar cabeças humanas, podemos usar o [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## O Conjunto de Dados

O [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contém 369.846 cabeças humanas anotadas em 224.740 frames de filmes de Hollywood. É fornecido no formato [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), onde para cada imagem existe também um ficheiro de descrição XML que se parece com isto:

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

Neste conjunto de dados, existe apenas uma classe de objetos, `head`, e para cada cabeça, obtém-se as coordenadas da caixa delimitadora. Pode-se analisar os ficheiros XML usando bibliotecas Python ou usar [esta biblioteca](https://pypi.org/project/pascal-voc/) para lidar diretamente com o formato PASCAL VOC.

## Treinar a Deteção de Objetos

Pode treinar um modelo de deteção de objetos utilizando uma das seguintes abordagens:

* Usar o [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) e a sua API Python para treinar programaticamente o modelo na cloud. O Custom Vision não consegue usar mais do que algumas centenas de imagens para treinar o modelo, por isso pode ser necessário limitar o conjunto de dados.
* Usar o exemplo do [tutorial do Keras](https://keras.io/examples/vision/retinanet/) para treinar o modelo RetunaNet.
* Usar o módulo integrado [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) no torchvision.

## Conclusão

A deteção de objetos é uma tarefa frequentemente necessária na indústria. Embora existam alguns serviços que podem ser usados para realizar a deteção de objetos (como o [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), é importante compreender como funciona a deteção de objetos e ser capaz de treinar os seus próprios modelos.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.