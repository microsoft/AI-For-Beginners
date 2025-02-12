# Clasificación de Caras de Mascotas

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Imagina que necesitas desarrollar una aplicación para una guardería de mascotas para catalogar todas las mascotas. Una de las grandes características de tal aplicación sería descubrir automáticamente la raza a partir de una fotografía. Esto se puede hacer con éxito utilizando redes neuronales.

Necesitas entrenar una red neuronal convolucional para clasificar diferentes razas de gatos y perros utilizando el conjunto de datos **Caras de Mascotas**.

## El Conjunto de Datos

Usaremos el conjunto de datos **Caras de Mascotas**, derivado del conjunto de datos de mascotas [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Contiene 35 razas diferentes de perros y gatos.

![Conjunto de datos con el que trabajaremos](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.es.png)

Para descargar el conjunto de datos, usa este fragmento de código:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Iniciando el Notebook

Comienza el laboratorio abriendo [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Conclusión

¡Has resuelto un problema relativamente complejo de clasificación de imágenes desde cero! Hubo muchas clases, ¡y aún así lograste obtener una precisión razonable! También tiene sentido medir la precisión top-k, porque es fácil confundir algunas de las clases que no son claramente diferentes incluso para los seres humanos.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.