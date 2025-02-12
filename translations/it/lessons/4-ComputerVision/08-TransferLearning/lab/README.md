# Clasificación de Mascotas de Oxford utilizando Aprendizaje por Transferencia

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Imagina que necesitas desarrollar una aplicación para una guardería de mascotas para catalogar todos los animales. Una de las grandes características de dicha aplicación sería descubrir automáticamente la raza a partir de una fotografía. En esta tarea, utilizaremos el aprendizaje por transferencia para clasificar imágenes de mascotas de la vida real del conjunto de datos de mascotas [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## El Conjunto de Datos

Usaremos el conjunto de datos original de mascotas [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), que contiene 35 razas diferentes de perros y gatos.

Para descargar el conjunto de datos, utiliza este fragmento de código:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Iniciando el Notebook

Comienza el laboratorio abriendo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusión

El aprendizaje por transferencia y las redes preentrenadas nos permiten resolver problemas de clasificación de imágenes del mundo real de manera relativamente sencilla. Sin embargo, las redes preentrenadas funcionan bien con imágenes de un tipo similar, y si comenzamos a clasificar imágenes muy diferentes (por ejemplo, imágenes médicas), es probable que obtengamos resultados mucho peores.

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.