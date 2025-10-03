<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T09:18:20+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "es"
}
-->
# Clasificación de Caras de Mascotas

Asignación de laboratorio del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Imagina que necesitas desarrollar una aplicación para una guardería de mascotas para catalogar a todas las mascotas. Una de las grandes características de dicha aplicación sería descubrir automáticamente la raza a partir de una fotografía. Esto se puede lograr con éxito utilizando redes neuronales.

Necesitas entrenar una red neuronal convolucional para clasificar diferentes razas de gatos y perros utilizando el conjunto de datos **Pet Faces**.

## El Conjunto de Datos

Usaremos el conjunto de datos **Pet Faces**, derivado del conjunto de datos de mascotas [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Contiene 35 razas diferentes de perros y gatos.

![Conjunto de datos con el que trabajaremos](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/images/data.png)

Para descargar el conjunto de datos, utiliza este fragmento de código:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Cuaderno Inicial

Comienza el laboratorio abriendo [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Conclusión

¡Has resuelto un problema relativamente complejo de clasificación de imágenes desde cero! Había bastantes clases, y aun así lograste obtener una precisión razonable. También tiene sentido medir la precisión top-k, porque es fácil confundir algunas de las clases que no son claramente diferentes, incluso para los seres humanos.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.