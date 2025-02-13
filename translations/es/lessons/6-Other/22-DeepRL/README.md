# Aprendizaje Profundo por Refuerzo

El aprendizaje por refuerzo (RL) se considera uno de los paradigmas básicos del aprendizaje automático, junto al aprendizaje supervisado y no supervisado. Mientras que en el aprendizaje supervisado nos basamos en un conjunto de datos con resultados conocidos, el RL se basa en **aprender haciendo**. Por ejemplo, cuando vemos un videojuego por primera vez, comenzamos a jugar, incluso sin conocer las reglas, y pronto somos capaces de mejorar nuestras habilidades simplemente a través del proceso de jugar y ajustar nuestro comportamiento.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Para realizar RL, necesitamos:

* Un **entorno** o **simulador** que establezca las reglas del juego. Debemos poder ejecutar experimentos en el simulador y observar los resultados.
* Una **función de recompensa**, que indique cuán exitoso fue nuestro experimento. En el caso de aprender a jugar un videojuego, la recompensa sería nuestra puntuación final.

Basándonos en la función de recompensa, deberíamos poder ajustar nuestro comportamiento y mejorar nuestras habilidades, de modo que la próxima vez juguemos mejor. La principal diferencia entre otros tipos de aprendizaje automático y el RL es que en el RL típicamente no sabemos si ganamos o perdemos hasta que terminamos el juego. Por lo tanto, no podemos decir si un determinado movimiento por sí solo es bueno o no; solo recibimos una recompensa al final del juego.

Durante el RL, normalmente realizamos muchos experimentos. Durante cada experimento, necesitamos equilibrar entre seguir la estrategia óptima que hemos aprendido hasta ahora (**explotación**) y explorar nuevos estados posibles (**exploración**).

## OpenAI Gym

Una gran herramienta para RL es el [OpenAI Gym](https://gym.openai.com/) - un **entorno de simulación**, que puede simular muchos entornos diferentes, desde juegos de Atari hasta la física detrás del equilibrio de un palo. Es uno de los entornos de simulación más populares para entrenar algoritmos de aprendizaje por refuerzo, y es mantenido por [OpenAI](https://openai.com/).

> **Nota**: Puedes ver todos los entornos disponibles en OpenAI Gym [aquí](https://gym.openai.com/envs/#classic_control).

## Equilibrio de CartPole

Probablemente todos hayan visto dispositivos de equilibrio modernos como el *Segway* o *Gyroscooters*. Son capaces de equilibrarse automáticamente ajustando sus ruedas en respuesta a una señal de un acelerómetro o giroscopio. En esta sección, aprenderemos cómo resolver un problema similar: equilibrar un palo. Es similar a una situación en la que un artista de circo necesita equilibrar un palo en su mano, pero este equilibrio de palo solo ocurre en 1D.

Una versión simplificada del equilibrio se conoce como el problema de **CartPole**. En el mundo de cartpole, tenemos un deslizador horizontal que puede moverse hacia la izquierda o hacia la derecha, y el objetivo es equilibrar un palo vertical en la parte superior del deslizador mientras se mueve.

<img alt="un cartpole" src="images/cartpole.png" width="200"/>

Para crear y usar este entorno, necesitamos un par de líneas de código en Python:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Cada entorno se puede acceder exactamente de la misma manera:
* `env.reset` starts a new experiment
* `env.step` realiza un paso de simulación. Recibe una **acción** del **espacio de acciones**, y devuelve una **observación** (del espacio de observaciones), así como una recompensa y una bandera de terminación.

En el ejemplo anterior, realizamos una acción aleatoria en cada paso, por lo que la vida del experimento es muy corta:

![cartpole sin equilibrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

El objetivo de un algoritmo de RL es entrenar un modelo - la llamada **política** π - que devolverá la acción en respuesta a un estado dado. También podemos considerar la política como probabilística, es decir, para cualquier estado *s* y acción *a* devolverá la probabilidad π(*a*|*s*) de que debamos tomar *a* en el estado *s*.

## Algoritmo de Gradientes de Política

La forma más obvia de modelar una política es creando una red neuronal que tome estados como entrada y devuelva acciones correspondientes (o más bien las probabilidades de todas las acciones). En cierto sentido, sería similar a una tarea de clasificación normal, con una gran diferencia: no sabemos de antemano qué acciones debemos tomar en cada uno de los pasos.

La idea aquí es estimar esas probabilidades. Construimos un vector de **recompensas acumulativas** que muestra nuestra recompensa total en cada paso del experimento. También aplicamos **descuento de recompensa** multiplicando las recompensas anteriores por algún coeficiente γ=0.99, con el fin de disminuir el papel de las recompensas anteriores. Luego, reforzamos esos pasos a lo largo del camino del experimento que generan mayores recompensas.

> Aprende más sobre el algoritmo de Gradiente de Política y míralo en acción en el [cuaderno de ejemplo](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algoritmo Actor-Critic

Una versión mejorada del enfoque de Gradientes de Política se llama **Actor-Critic**. La idea principal detrás de esto es que la red neuronal se entrenaría para devolver dos cosas:

* La política, que determina qué acción tomar. Esta parte se llama **actor**.
* La estimación de la recompensa total que podemos esperar obtener en este estado - esta parte se llama **crítico**.

En cierto sentido, esta arquitectura se asemeja a un [GAN](../../4-ComputerVision/10-GANs/README.md), donde tenemos dos redes que se entrenan entre sí. En el modelo actor-crítico, el actor propone la acción que necesitamos tomar, y el crítico intenta ser crítico y estimar el resultado. Sin embargo, nuestro objetivo es entrenar esas redes de manera conjunta.

Dado que conocemos tanto las recompensas acumulativas reales como los resultados devueltos por el crítico durante el experimento, es relativamente fácil construir una función de pérdida que minimice la diferencia entre ellas. Eso nos daría la **pérdida del crítico**. Podemos calcular la **pérdida del actor** utilizando el mismo enfoque que en el algoritmo de gradiente de política.

Después de ejecutar uno de estos algoritmos, podemos esperar que nuestro CartPole se comporte así:

![un cartpole en equilibrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Ejercicios: Gradientes de Política y RL Actor-Critic

Continúa tu aprendizaje en los siguientes cuadernos:

* [RL en TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL en PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Otras Tareas de RL

El Aprendizaje por Refuerzo hoy en día es un campo de investigación de rápido crecimiento. Algunos de los ejemplos interesantes de aprendizaje por refuerzo son:

* Enseñar a una computadora a jugar **Juegos de Atari**. La parte desafiante de este problema es que no tenemos un estado simple representado como un vector, sino más bien una captura de pantalla, y necesitamos usar la CNN para convertir esta imagen de pantalla en un vector de características, o extraer información de recompensa. Los juegos de Atari están disponibles en el Gym.
* Enseñar a una computadora a jugar juegos de mesa, como Ajedrez y Go. Recientemente, programas de vanguardia como **Alpha Zero** fueron entrenados desde cero por dos agentes jugando entre sí y mejorando en cada paso.
* En la industria, el RL se utiliza para crear sistemas de control a partir de simulaciones. Un servicio llamado [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) está diseñado específicamente para eso.

## Conclusión

Ahora hemos aprendido cómo entrenar agentes para lograr buenos resultados simplemente proporcionándoles una función de recompensa que define el estado deseado del juego y dándoles la oportunidad de explorar inteligentemente el espacio de búsqueda. Hemos probado con éxito dos algoritmos y logrado un buen resultado en un período de tiempo relativamente corto. Sin embargo, este es solo el comienzo de tu viaje en RL, y definitivamente deberías considerar tomar un curso separado si deseas profundizar más.

## 🚀 Desafío

Explora las aplicaciones enumeradas en la sección 'Otras Tareas de RL' y trata de implementar una.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Revisión y Autoestudio

Aprende más sobre el aprendizaje por refuerzo clásico en nuestro [Currículo de Aprendizaje Automático para Principiantes](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Mira [este gran video](https://www.youtube.com/watch?v=qv6UVOQ0F44) que habla sobre cómo una computadora puede aprender a jugar Super Mario.

## Tarea: [Entrenar un Mountain Car](lab/README.md)

Tu objetivo durante esta tarea sería entrenar un entorno diferente de Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.