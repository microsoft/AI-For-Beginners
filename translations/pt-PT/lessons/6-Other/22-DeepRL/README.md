# Aprendizagem por Reforço Profundo

A aprendizagem por reforço (RL) é considerada um dos paradigmas básicos de aprendizagem automática, ao lado da aprendizagem supervisionada e não supervisionada. Enquanto na aprendizagem supervisionada dependemos de um conjunto de dados com resultados conhecidos, a RL baseia-se em **aprender fazendo**. Por exemplo, quando vemos um jogo de computador pela primeira vez, começamos a jogar, mesmo sem conhecer as regras, e rapidamente conseguimos melhorar as nossas habilidades apenas pelo processo de jogar e ajustar o nosso comportamento.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Para realizar RL, precisamos de:

* Um **ambiente** ou **simulador** que define as regras do jogo. Devemos ser capazes de realizar experiências no simulador e observar os resultados.
* Uma **função de recompensa**, que indica o quão bem-sucedida foi a nossa experiência. No caso de aprender a jogar um jogo de computador, a recompensa seria a nossa pontuação final.

Com base na função de recompensa, devemos ser capazes de ajustar o nosso comportamento e melhorar as nossas habilidades, para que na próxima vez joguemos melhor. A principal diferença entre outros tipos de aprendizagem automática e RL é que na RL normalmente não sabemos se ganhamos ou perdemos até terminarmos o jogo. Assim, não podemos dizer se um determinado movimento isolado é bom ou não - só recebemos uma recompensa no final do jogo.

Durante a RL, normalmente realizamos muitas experiências. Em cada experiência, precisamos equilibrar entre seguir a estratégia ótima que aprendemos até agora (**exploração**) e explorar novos estados possíveis (**exploração**).

## OpenAI Gym

Uma ferramenta excelente para RL é o [OpenAI Gym](https://gym.openai.com/) - um **ambiente de simulação**, que pode simular muitos ambientes diferentes, desde jogos Atari até a física por trás do equilíbrio de um poste. É um dos ambientes de simulação mais populares para treinar algoritmos de aprendizagem por reforço e é mantido pela [OpenAI](https://openai.com/).

> **Nota**: Pode ver todos os ambientes disponíveis no OpenAI Gym [aqui](https://gym.openai.com/envs/#classic_control).

## Equilíbrio do CartPole

Provavelmente já viu dispositivos modernos de equilíbrio, como o *Segway* ou *Gyroscooters*. Eles conseguem equilibrar-se automaticamente ajustando as suas rodas em resposta a um sinal de um acelerómetro ou giroscópio. Nesta seção, vamos aprender a resolver um problema semelhante - equilibrar um poste. É semelhante a uma situação em que um artista de circo precisa equilibrar um poste na sua mão - mas este equilíbrio de poste ocorre apenas em 1D.

Uma versão simplificada de equilíbrio é conhecida como o problema **CartPole**. No mundo do CartPole, temos um slider horizontal que pode mover-se para a esquerda ou para a direita, e o objetivo é equilibrar um poste vertical no topo do slider enquanto ele se move.

<img alt="um cartpole" src="../../../../../translated_images/pt-PT/cartpole.f52a67f27e058170.webp" width="200"/>

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

Cada ambiente pode ser acessado exatamente da mesma forma:
* `env.reset` inicia uma nova experiência
* `env.step` realiza um passo de simulação. Recebe uma **ação** do **espaço de ações** e retorna uma **observação** (do espaço de observação), bem como uma recompensa e um sinal de término.

No exemplo acima, realizamos uma ação aleatória em cada passo, razão pela qual a vida da experiência é muito curta:

![cartpole sem equilíbrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

O objetivo de um algoritmo de RL é treinar um modelo - a chamada **política** &pi; - que retornará a ação em resposta a um estado dado. Também podemos considerar a política como probabilística, ou seja, para qualquer estado *s* e ação *a*, ela retornará a probabilidade &pi;(*a*|*s*) de que devemos tomar *a* no estado *s*.

## Algoritmo de Gradientes de Política

A maneira mais óbvia de modelar uma política é criar uma rede neural que receba estados como entrada e retorne ações correspondentes (ou, mais precisamente, as probabilidades de todas as ações). De certa forma, seria semelhante a uma tarefa de classificação normal, com uma grande diferença - não sabemos de antemão quais ações devemos tomar em cada um dos passos.

A ideia aqui é estimar essas probabilidades. Construímos um vetor de **recompensas acumuladas**, que mostra a nossa recompensa total em cada passo da experiência. Também aplicamos **desconto de recompensa** multiplicando recompensas anteriores por algum coeficiente &gamma;=0.99, para diminuir o papel das recompensas anteriores. Em seguida, reforçamos os passos ao longo do caminho da experiência que geram maiores recompensas.

> Saiba mais sobre o algoritmo de Gradientes de Política e veja-o em ação no [notebook de exemplo](CartPole-RL-TF.ipynb).

## Algoritmo Ator-Crítico

Uma versão melhorada da abordagem de Gradientes de Política é chamada de **Ator-Crítico**. A ideia principal por trás disso é que a rede neural seria treinada para retornar duas coisas:

* A política, que determina qual ação tomar. Esta parte é chamada de **ator**.
* A estimativa da recompensa total que podemos esperar obter neste estado - esta parte é chamada de **crítico**.

De certa forma, esta arquitetura assemelha-se a um [GAN](../../4-ComputerVision/10-GANs/README.md), onde temos duas redes que são treinadas uma contra a outra. No modelo ator-crítico, o ator propõe a ação que precisamos tomar, e o crítico tenta ser crítico e estimar o resultado. No entanto, o nosso objetivo é treinar essas redes em conjunto.

Como sabemos tanto as recompensas acumuladas reais quanto os resultados retornados pelo crítico durante a experiência, é relativamente fácil construir uma função de perda que minimize a diferença entre eles. Isso nos daria a **perda do crítico**. Podemos calcular a **perda do ator** usando a mesma abordagem do algoritmo de gradientes de política.

Depois de executar um desses algoritmos, podemos esperar que o nosso CartPole se comporte assim:

![um cartpole equilibrado](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercícios: Gradientes de Política e RL Ator-Crítico

Continue a sua aprendizagem nos seguintes notebooks:

* [RL em TensorFlow](CartPole-RL-TF.ipynb)
* [RL em PyTorch](CartPole-RL-PyTorch.ipynb)

## Outras Tarefas de RL

A aprendizagem por reforço é atualmente um campo de pesquisa em rápido crescimento. Alguns exemplos interessantes de aprendizagem por reforço são:

* Ensinar um computador a jogar **Jogos Atari**. A parte desafiadora deste problema é que não temos um estado simples representado como um vetor, mas sim uma captura de ecrã - e precisamos usar a CNN para converter esta imagem de ecrã num vetor de características ou para extrair informações de recompensa. Os jogos Atari estão disponíveis no Gym.
* Ensinar um computador a jogar jogos de tabuleiro, como Xadrez e Go. Recentemente, programas de última geração como **Alpha Zero** foram treinados do zero por dois agentes jogando um contra o outro e melhorando a cada passo.
* Na indústria, a RL é usada para criar sistemas de controlo a partir de simulação. Um serviço chamado [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) foi especificamente projetado para isso.

## Conclusão

Aprendemos agora como treinar agentes para alcançar bons resultados apenas fornecendo-lhes uma função de recompensa que define o estado desejado do jogo e dando-lhes a oportunidade de explorar inteligentemente o espaço de busca. Experimentámos com sucesso dois algoritmos e alcançámos um bom resultado num período de tempo relativamente curto. No entanto, este é apenas o início da sua jornada na RL, e deve definitivamente considerar fazer um curso separado se quiser aprofundar mais.

## 🚀 Desafio

Explore as aplicações listadas na seção 'Outras Tarefas de RL' e tente implementar uma!

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Revisão e Autoestudo

Saiba mais sobre aprendizagem por reforço clássica no nosso [Currículo de Aprendizagem Automática para Iniciantes](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Assista a [este excelente vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como um computador pode aprender a jogar Super Mario.

## Tarefa: [Treinar um Carro na Montanha](lab/README.md)

O seu objetivo nesta tarefa será treinar um ambiente diferente do Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

