# Aprendizado por Reforço Profundo

O aprendizado por reforço (RL) é considerado um dos paradigmas básicos de aprendizado de máquina, ao lado do aprendizado supervisionado e não supervisionado. Enquanto no aprendizado supervisionado dependemos de um conjunto de dados com resultados conhecidos, o RL é baseado no **aprender fazendo**. Por exemplo, quando jogamos um jogo de computador pela primeira vez, começamos a jogar mesmo sem conhecer as regras, e logo conseguimos melhorar nossas habilidades apenas pelo processo de jogar e ajustar nosso comportamento.

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Para realizar RL, precisamos de:

* Um **ambiente** ou **simulador** que define as regras do jogo. Devemos ser capazes de executar experimentos no simulador e observar os resultados.
* Alguma **função de recompensa**, que indica quão bem-sucedido foi nosso experimento. No caso de aprender a jogar um jogo de computador, a recompensa seria nossa pontuação final.

Com base na função de recompensa, devemos ser capazes de ajustar nosso comportamento e melhorar nossas habilidades, para que na próxima vez joguemos melhor. A principal diferença entre outros tipos de aprendizado de máquina e RL é que no RL geralmente não sabemos se ganhamos ou perdemos até terminarmos o jogo. Assim, não podemos dizer se um movimento específico é bom ou não - só recebemos uma recompensa no final do jogo.

Durante o RL, normalmente realizamos muitos experimentos. Em cada experimento, precisamos equilibrar entre seguir a estratégia ideal que aprendemos até agora (**exploração**) e explorar novos estados possíveis (**exploração**).

## OpenAI Gym

Uma ferramenta excelente para RL é o [OpenAI Gym](https://gym.openai.com/) - um **ambiente de simulação**, que pode simular muitos ambientes diferentes, desde jogos de Atari até a física por trás do equilíbrio de um pêndulo. É um dos ambientes de simulação mais populares para treinar algoritmos de aprendizado por reforço e é mantido pela [OpenAI](https://openai.com/).

> **Note**: Você pode ver todos os ambientes disponíveis no OpenAI Gym [aqui](https://gym.openai.com/envs/#classic_control).

## Equilíbrio do CartPole

Provavelmente todos já viram dispositivos modernos de equilíbrio, como o *Segway* ou *Gyroscooters*. Eles conseguem se equilibrar automaticamente ajustando suas rodas em resposta a um sinal de um acelerômetro ou giroscópio. Nesta seção, aprenderemos como resolver um problema semelhante - equilibrar um pêndulo. É similar à situação em que um artista de circo precisa equilibrar um pêndulo na mão - mas este equilíbrio ocorre apenas em 1D.

Uma versão simplificada do equilíbrio é conhecida como problema **CartPole**. No mundo do CartPole, temos um deslizante horizontal que pode se mover para a esquerda ou para a direita, e o objetivo é equilibrar um pêndulo vertical no topo do deslizante enquanto ele se move.

<img alt="um cartpole" src="../../../../../translated_images/pt-BR/cartpole.f52a67f27e058170.webp" width="200"/>

Para criar e usar este ambiente, precisamos de algumas linhas de código Python:

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

Cada ambiente pode ser acessado exatamente da mesma maneira:
* `env.reset` inicia um novo experimento
* `env.step` realiza um passo de simulação. Ele recebe uma **ação** do **espaço de ações** e retorna uma **observação** (do espaço de observação), bem como uma recompensa e um sinal de término.

No exemplo acima, realizamos uma ação aleatória em cada passo, o que faz com que a vida do experimento seja muito curta:

![cartpole sem equilíbrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

O objetivo de um algoritmo de RL é treinar um modelo - a chamada **política** &pi; - que retornará a ação em resposta a um estado dado. Também podemos considerar a política como probabilística, por exemplo, para qualquer estado *s* e ação *a*, ela retornará a probabilidade &pi;(*a*|*s*) de que devemos tomar *a* no estado *s*.

## Algoritmo de Gradientes de Política

A maneira mais óbvia de modelar uma política é criando uma rede neural que receba estados como entrada e retorne ações correspondentes (ou melhor, as probabilidades de todas as ações). Em certo sentido, seria semelhante a uma tarefa de classificação normal, com uma grande diferença - não sabemos de antemão quais ações devemos tomar em cada um dos passos.

A ideia aqui é estimar essas probabilidades. Construímos um vetor de **recompensas acumuladas**, que mostra nossa recompensa total em cada passo do experimento. Também aplicamos **desconto de recompensa** multiplicando recompensas anteriores por algum coeficiente &gamma;=0.99, para diminuir o papel das recompensas anteriores. Em seguida, reforçamos aqueles passos ao longo do caminho do experimento que geram maiores recompensas.

> Saiba mais sobre o algoritmo de Gradientes de Política e veja-o em ação no [notebook de exemplo](CartPole-RL-TF.ipynb).

## Algoritmo Ator-Crítico

Uma versão aprimorada da abordagem de Gradientes de Política é chamada de **Ator-Crítico**. A ideia principal por trás disso é que a rede neural seria treinada para retornar duas coisas:

* A política, que determina qual ação tomar. Esta parte é chamada de **ator**
* A estimativa da recompensa total que podemos esperar obter neste estado - esta parte é chamada de **crítico**.

Em certo sentido, esta arquitetura se assemelha a um [GAN](../../4-ComputerVision/10-GANs/README.md), onde temos duas redes que são treinadas uma contra a outra. No modelo ator-crítico, o ator propõe a ação que precisamos tomar, e o crítico tenta ser crítico e estimar o resultado. No entanto, nosso objetivo é treinar essas redes em conjunto.

Como sabemos tanto as recompensas acumuladas reais quanto os resultados retornados pelo crítico durante o experimento, é relativamente fácil construir uma função de perda que minimize a diferença entre eles. Isso nos daria a **perda do crítico**. Podemos calcular a **perda do ator** usando a mesma abordagem do algoritmo de gradientes de política.

Depois de executar um desses algoritmos, podemos esperar que nosso CartPole se comporte assim:

![um cartpole equilibrado](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercícios: Gradientes de Política e RL Ator-Crítico

Continue seu aprendizado nos seguintes notebooks:

* [RL em TensorFlow](CartPole-RL-TF.ipynb)
* [RL em PyTorch](CartPole-RL-PyTorch.ipynb)

## Outras Tarefas de RL

O Aprendizado por Reforço atualmente é um campo de pesquisa em rápido crescimento. Alguns exemplos interessantes de aprendizado por reforço são:

* Ensinar um computador a jogar **jogos de Atari**. A parte desafiadora deste problema é que não temos um estado simples representado como um vetor, mas sim uma captura de tela - e precisamos usar a CNN para converter esta imagem de tela em um vetor de características ou para extrair informações de recompensa. Jogos de Atari estão disponíveis no Gym.
* Ensinar um computador a jogar jogos de tabuleiro, como Xadrez e Go. Recentemente, programas de última geração como **Alpha Zero** foram treinados do zero por dois agentes jogando um contra o outro e melhorando a cada passo.
* Na indústria, o RL é usado para criar sistemas de controle a partir de simulação. Um serviço chamado [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) é especificamente projetado para isso.

## Conclusão

Agora aprendemos como treinar agentes para alcançar bons resultados apenas fornecendo-lhes uma função de recompensa que define o estado desejado do jogo e dando-lhes a oportunidade de explorar inteligentemente o espaço de busca. Experimentamos com sucesso dois algoritmos e alcançamos um bom resultado em um período relativamente curto de tempo. No entanto, este é apenas o começo de sua jornada no RL, e você definitivamente deve considerar fazer um curso separado se quiser se aprofundar.

## 🚀 Desafio

Explore as aplicações listadas na seção 'Outras Tarefas de RL' e tente implementar uma delas!

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Revisão e Autoestudo

Saiba mais sobre aprendizado por reforço clássico em nosso [Currículo de Aprendizado de Máquina para Iniciantes](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Assista a [este ótimo vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como um computador pode aprender a jogar Super Mario.

## Tarefa: [Treine um Mountain Car](lab/README.md)

Seu objetivo durante esta tarefa será treinar um ambiente diferente do Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

