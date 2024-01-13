# Aprendizaje por refuerzo profundo

El aprendizaje por refuerzo (RL) se considera uno de los paradigmas básicos del aprendizaje automático, junto al aprendizaje supervisado y el aprendizaje no supervisado. Mientras que en el aprendizaje supervisado nos basamos en el conjunto de datos con resultados conocidos, RL se basa en **aprender haciendo**. Por ejemplo, cuando vemos por primera vez un juego de computadora, comenzamos a jugar, incluso sin conocer las reglas, y pronto somos capaces de mejorar nuestras habilidades simplemente jugando y ajustando nuestro comportamiento.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Para realizar RL, necesitamos:

* Un **entorno** o **simulador** que marca las reglas del juego. Deberíamos poder ejecutar los experimentos en el simulador y observar los resultados.
* Alguna **Función de recompensa**, que indica el éxito de nuestro experimento. En caso de aprender a jugar a un juego de ordenador, la recompensa sería nuestra puntuación final.

Basándonos en la función de recompensa, deberíamos poder ajustar nuestro comportamiento y mejorar nuestras habilidades, para que la próxima vez juguemos mejor. La principal diferencia entre otros tipos de aprendizaje automático y RL es que en RL normalmente no sabemos si ganamos o perdemos hasta que terminamos el juego. Por lo tanto, no podemos decir si un determinado movimiento por sí solo es bueno o no; solo recibimos una recompensa al final del juego.

Durante RL, normalmente realizamos muchos experimentos. Durante cada experimento, debemos equilibrar entre seguir la estrategia óptima que hemos aprendido hasta ahora (**explotación**) y explorar nuevos estados posibles (**exploración**).

## Gimnasio OpenAI

Una gran herramienta para RL es el [OpenAI Gym](https://gym.openai.com/) - a **simulation environment**, which can simulate many different environments starting from Atari games, to the physics behind pole balancing. It is one of the most popular simulation environments for training reinforcement learning algorithms, and is maintained by [OpenAI](https://openai.com/).

> **Nota**: Puedes ver todos los entornos disponibles en OpenAI Gym [here](https://gym.openai.com/envs/#classic_control).

## Equilibrio de postes de carrito

Probablemente todos habéis visto dispositivos de equilibrio modernos como el *Segway* o los *Gyroscooters*. Pueden equilibrarse automáticamente ajustando sus ruedas en respuesta a una señal de un acelerómetro o giroscopio. En esta sección, aprenderemos cómo resolver un problema similar: equilibrar un poste. Es similar a una situación en la que un artista de circo necesita equilibrar un poste en su mano, pero este equilibrio del poste solo ocurre en 1D.

Una versión simplificada del equilibrio se conoce como problema **CartPole**. En el mundo de los postes, tenemos un control deslizante horizontal que se puede mover hacia la izquierda o hacia la derecha, y el objetivo es equilibrar un poste vertical encima del control deslizante a medida que se mueve.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Para crear y utilizar este entorno, necesitamos un par de líneas de código Python:

```pitón
importar gimnasio
env = gimnasio.make("CartPole-v1")

entorno.reset()
hecho = falso
recompensa_total = 0
mientras no haya terminado:
    entorno.render()
    acción = env.action_space.sample()
    observación, recompensa, hecho, información = env.step(acción)
    recompensa_total += recompensa

print(f"Recompensa total: {recompensa_total}")
```

Se puede acceder a cada entorno exactamente de la misma manera:
* `env.reset` inicia un nuevo experimento
* `env.step` realiza un paso de simulación. Recibe una **acción** del **espacio de acción** y devuelve una **observación** (del espacio de observación), así como una recompensa y un indicador de terminación.

En el ejemplo anterior realizamos una acción aleatoria en cada paso, razón por la cual la duración del experimento es muy corta:

![non-balancing cartpole](images/cartpole-nobalance.gif)

El objetivo de un algoritmo RL es entrenar un modelo: la llamada **política** &pi; - que devolverá la acción en respuesta a un estado determinado. También podemos considerar que la política es probabilística, por ejemplo. para cualquier estado *s* y acción *a* devolverá la probabilidad &pi;(*a*|*s*) de que debamos tomar *a* en el estado *s*.

## Algoritmo de gradientes de políticas

La forma más obvia de modelar una política es crear una red neuronal que tome estados como entrada y devuelva las acciones correspondientes (o más bien las probabilidades de todas las acciones). En cierto sentido, sería similar a una tarea de clasificación normal, con una diferencia importante: no sabemos de antemano qué acciones debemos realizar en cada uno de los pasos.

La idea aquí es estimar esas probabilidades. Creamos un vector de **recompensas acumulativas** que muestra nuestra recompensa total en cada paso del experimento. También aplicamos **descuento de recompensas** multiplicando las recompensas anteriores por algún coeficiente γ=0,99, para disminuir el papel de las recompensas anteriores. Luego, reforzamos aquellos pasos a lo largo del camino del experimento que generan mayores recompensas.

> Obtenga más información sobre el algoritmo de gradiente de políticas y véalo en acción en el [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

An improved version of the Policy Gradients approach is called **Actor-Critic**. The main idea behind it is that the neural network would be trained to return two things:

* The policy, which determines which action to take. This part is called **actor**
* The estimation of the total reward we can expect to get at this state - this part is called **critic**.

In a sense, this architecture resembles a [GAN](../../4-ComputerVision/10-GANs/README.md), donde tenemos dos redes que se entrenan entre sí. En el modelo actor-crítico, el actor propone la acción que debemos realizar y el crítico intenta ser crítico y estimar el resultado. Sin embargo, nuestro objetivo es entrenar esas redes al unísono.

Como conocemos tanto las recompensas acumuladas reales como los resultados arrojados por el crítico durante el experimento, es relativamente fácil construir una función de pérdida que minimice la diferencia entre ellos. Eso nos daría una **pérdida crítica**. Podemos calcular la **pérdida de actor** utilizando el mismo enfoque que en el algoritmo de gradiente de políticas.

Después de ejecutar uno de esos algoritmos, podemos esperar que nuestro CartPole se comporte así:

![a balancing cartpole](images/cartpole-balance.gif)

## ✍️ Ejercicios: gradientes de políticas y RL actor-crítico

Continúa tu aprendizaje en los siguientes cuadernos:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Otras tareas de RL

El aprendizaje por refuerzo es hoy en día un campo de investigación de rápido crecimiento. Algunos de los ejemplos interesantes de aprendizaje por refuerzo son:

* Enseñar a una computadora a jugar **Juegos Atari**. La parte desafiante de este problema es que no tenemos un estado simple representado como un vector, sino más bien una captura de pantalla, y necesitamos usar CNN para convertir esta imagen de pantalla en un vector de características o para extraer información de recompensa. Los juegos de Atari están disponibles en el gimnasio.
* Enseñar a una computadora a jugar juegos de mesa, como Chess and Go. Recientemente, dos agentes entrenaron programas de última generación como **Alpha Zero** desde cero, jugando uno contra el otro y mejorando en cada paso.
* En la industria, RL se utiliza para crear sistemas de control a partir de simulación. un servicio llamado [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) está diseñado específicamente para eso.

* ## Conclusión

Ahora hemos aprendido cómo entrenar agentes para lograr buenos resultados simplemente proporcionándoles una función de recompensa que defina el estado deseado del juego y dándoles la oportunidad de explorar inteligentemente el espacio de búsqueda. Probamos con éxito dos algoritmos y logramos un buen resultado en un período de tiempo relativamente corto. Sin embargo, este es solo el comienzo de su viaje hacia la vida real y definitivamente debería considerar tomar un curso por separado si desea profundizar más.

## 🚀 Desafío

Explore las aplicaciones enumeradas en la sección 'Otras tareas de RL' e intente implementar una.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Revisión y autoestudio

Obtenga más información sobre el aprendizaje por refuerzo clásico en nuestro [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Mirar [this great video](https://www.youtube.com/watch?v=qv6UVOQ0F44) hablando de cómo una computadora puede aprender a jugar Super Mario.

## Asignación: [Train a Mountain Car](lab/README.md)

Su objetivo durante esta tarea sería entrenar en un ambiente de gimnasio diferente -  [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).
