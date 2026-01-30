# Ejemplos de IA para Principiantes

¡Bienvenido! Este directorio contiene ejemplos simples e independientes para ayudarte a comenzar con la inteligencia artificial y el aprendizaje automático. Cada ejemplo está diseñado para ser accesible para principiantes, con comentarios detallados y explicaciones paso a paso.

## 📚 Resumen de Ejemplos

| Ejemplo | Descripción | Dificultad | Requisitos Previos |
|---------|-------------|------------|--------------------|
| [Hola Mundo de IA](../../../examples/01-hello-ai-world.py) | Tu primer programa de IA: reconocimiento de patrones simple | ⭐ Principiante | Conceptos básicos de Python |
| [Red Neuronal Simple](../../../examples/02-simple-neural-network.py) | Construye una red neuronal desde cero | ⭐⭐ Principiante+ | Python, matemáticas básicas |
| [Clasificador de Imágenes](./03-image-classifier.ipynb) | Clasifica imágenes con un modelo preentrenado | ⭐⭐ Principiante+ | Python, numpy |
| [Análisis de Sentimientos de Texto](../../../examples/04-text-sentiment.py) | Analiza el sentimiento de un texto (positivo/negativo) | ⭐⭐ Principiante+ | Python |

## 🚀 Comenzando

### Requisitos Previos

Asegúrate de tener Python instalado (se recomienda la versión 3.8 o superior). Instala los paquetes necesarios:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

O utiliza el entorno conda del currículo principal:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Ejecutando los Ejemplos

**Para scripts de Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Para notebooks de Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Ruta de Aprendizaje

Recomendamos seguir los ejemplos en el siguiente orden:

1. **Comienza con "Hola Mundo de IA"** - Aprende los conceptos básicos del reconocimiento de patrones
2. **Construye una Red Neuronal Simple** - Entiende cómo funcionan las redes neuronales
3. **Prueba el Clasificador de Imágenes** - Observa la IA en acción con imágenes reales
4. **Analiza el Sentimiento de Texto** - Explora el procesamiento del lenguaje natural

## 💡 Consejos para Principiantes

- **Lee cuidadosamente los comentarios del código** - Explican qué hace cada línea
- **¡Experimenta!** - Prueba cambiar valores y observa qué sucede
- **No te preocupes por entender todo** - Aprender lleva tiempo
- **Haz preguntas** - Usa el [foro de discusión](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Próximos Pasos

Después de completar estos ejemplos, explora el currículo completo:
- [Introducción a la IA](../lessons/1-Intro/README.md)
- [Redes Neuronales](../lessons/3-NeuralNetworks/README.md)
- [Visión por Computadora](../lessons/4-ComputerVision/README.md)
- [Procesamiento del Lenguaje Natural](../lessons/5-NLP/README.md)

## 🤝 Contribuir

¿Encontraste útiles estos ejemplos? Ayúdanos a mejorarlos:
- Reporta problemas o sugiere mejoras
- Agrega más ejemplos para principiantes
- Mejora la documentación y los comentarios

---

*Recuerda: Todo experto alguna vez fue principiante. ¡Feliz aprendizaje! 🎓*

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.