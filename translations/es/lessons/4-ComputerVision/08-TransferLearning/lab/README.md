# Clasificación de Mascotas de Oxford usando Aprendizaje por Transferencia

Asignación de laboratorio del [Currículo de AI para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Imagina que necesitas desarrollar una aplicación para una guardería de mascotas para catalogar a todas las mascotas. Una de las grandes características de dicha aplicación sería identificar automáticamente la raza a partir de una fotografía. En esta asignación, utilizaremos aprendizaje por transferencia para clasificar imágenes reales de mascotas del conjunto de datos de [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## El Conjunto de Datos

Usaremos el conjunto de datos original de [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), que contiene 35 razas diferentes de perros y gatos.

Para descargar el conjunto de datos, utiliza este fragmento de código:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Iniciando el Cuaderno

Comienza el laboratorio abriendo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusión

El aprendizaje por transferencia y las redes preentrenadas nos permiten resolver problemas reales de clasificación de imágenes de manera relativamente sencilla. Sin embargo, las redes preentrenadas funcionan bien con imágenes de un tipo similar, y si comenzamos a clasificar imágenes muy diferentes (por ejemplo, imágenes médicas), es probable que obtengamos resultados mucho peores.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.