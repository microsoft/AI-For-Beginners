# Aprendizado por Reforço Profundo

O aprendizado por reforço (RL) é visto como um dos paradigmas básicos de aprendizado de máquina, ao lado do aprendizado supervisionado e do aprendizado não supervisionado. Enquanto no aprendizado supervisionado confiamos em um conjunto de dados com resultados conhecidos, o RL é baseado em **aprender fazendo**. Por exemplo, quando vemos um jogo de computador pela primeira vez, começamos a jogar, mesmo sem conhecer as regras, e logo conseguimos melhorar nossas habilidades apenas pelo processo de jogar e ajustar nosso comportamento.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Para realizar RL, precisamos de:

* Um **ambiente** ou **simulador** que estabelece as regras do jogo. Devemos ser capazes de executar os experimentos no simulador e observar os resultados.
* Alguma **função de recompensa**, que indica quão bem-sucedido foi nosso experimento. No caso de aprender a jogar um jogo de computador, a recompensa seria nossa pontuação final.

Com base na função de recompensa, devemos ser capazes de ajustar nosso comportamento e melhorar nossas habilidades, para que na próxima vez joguemos melhor. A principal diferença entre outros tipos de aprendizado de máquina e RL é que, no RL, normalmente não sabemos se ganhamos ou perdemos até terminarmos o jogo. Assim, não podemos dizer se um determinado movimento é bom ou não - recebemos uma recompensa apenas ao final do jogo.

Durante o RL, normalmente realizamos muitos experimentos. Durante cada experimento, precisamos equilibrar entre seguir a estratégia ótima que aprendemos até agora (**exploração**) e explorar novos estados possíveis (**exploração**).

## OpenAI Gym

Uma ótima ferramenta para RL é o [OpenAI Gym](https://gym.openai.com/) - um **ambiente de simulação**, que pode simular muitos ambientes diferentes, desde jogos Atari até a física por trás do equilíbrio de um poste. É um dos ambientes de simulação mais populares para treinar algoritmos de aprendizado por reforço, e é mantido pela [OpenAI](https://openai.com/).

> **Nota**: Você pode ver todos os ambientes disponíveis no OpenAI Gym [aqui](https://gym.openai.com/envs/#classic_control).

## Equilíbrio do CartPole

Você provavelmente já viu dispositivos modernos de equilíbrio, como o *Segway* ou *Gyroscooters*. Eles conseguem se equilibrar automaticamente ajustando suas rodas em resposta a um sinal de um acelerômetro ou giroscópio. Nesta seção, aprenderemos como resolver um problema semelhante - equilibrar um poste. É semelhante a uma situação em que um artista de circo precisa equilibrar um poste em sua mão - mas esse equilíbrio de poste ocorre apenas em 1D.

Uma versão simplificada do equilíbrio é conhecida como o problema **CartPole**. No mundo do cartpole, temos um deslizante horizontal que pode se mover para a esquerda ou para a direita, e o objetivo é equilibrar um poste vertical em cima do deslizante enquanto ele se move.

<img alt="um cartpole" src="images/cartpole.png" width="200"/>

Para criar e usar esse ambiente, precisamos de algumas linhas de código Python:

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
* `env.reset` starts a new experiment
* `env.step` realiza um passo de simulação. Ele recebe uma **ação** do **espaço de ações** e retorna uma **observação** (do espaço de observação), bem como uma recompensa e um sinal de terminação.

No exemplo acima, realizamos uma ação aleatória a cada passo, razão pela qual a vida do experimento é muito curta:

![cartpole sem equilíbrio](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

O objetivo de um algoritmo de RL é treinar um modelo - a chamada **política** π - que retornará a ação em resposta a um determinado estado. Também podemos considerar a política como probabilística, ou seja, para qualquer estado *s* e ação *a*, ela retornará a probabilidade π(*a*|*s*) de que devemos tomar *a* no estado *s*.

## Algoritmo de Gradientes de Política

A maneira mais óbvia de modelar uma política é criando uma rede neural que receberá estados como entrada e retornará as ações correspondentes (ou melhor, as probabilidades de todas as ações). De certa forma, seria semelhante a uma tarefa de classificação normal, com uma grande diferença - não sabemos de antemão quais ações devemos tomar em cada um dos passos.

A ideia aqui é estimar essas probabilidades. Construímos um vetor de **recompensas cumulativas** que mostra nossa recompensa total em cada passo do experimento. Também aplicamos **desconto de recompensa** multiplicando recompensas anteriores por algum coeficiente γ=0.99, a fim de diminuir o papel das recompensas anteriores. Em seguida, reforçamos aqueles passos ao longo do caminho do experimento que geram recompensas maiores.

> Aprenda mais sobre o algoritmo de Gradiente de Política e veja-o em ação no [notebook de exemplo](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algoritmo Ator-Crítico

Uma versão aprimorada da abordagem de Gradientes de Política é chamada de **Ator-Crítico**. A ideia principal por trás disso é que a rede neural seria treinada para retornar duas coisas:

* A política, que determina qual ação tomar. Esta parte é chamada de **ator**.
* A estimativa da recompensa total que podemos esperar obter neste estado - esta parte é chamada de **crítico**.

De certa forma, essa arquitetura se assemelha a um [GAN](../../4-ComputerVision/10-GANs/README.md), onde temos duas redes que são treinadas uma contra a outra. No modelo ator-crítico, o ator propõe a ação que precisamos tomar, e o crítico tenta ser crítico e estimar o resultado. No entanto, nosso objetivo é treinar essas redes em uníssono.

Como sabemos tanto as recompensas cumulativas reais quanto os resultados retornados pelo crítico durante o experimento, é relativamente fácil construir uma função de perda que minimize a diferença entre elas. Isso nos dará a **perda do crítico**. Podemos calcular a **perda do ator** usando a mesma abordagem que no algoritmo de gradiente de política.

Depois de executar um desses algoritmos, podemos esperar que nosso CartPole se comporte assim:

![um cartpole equilibrado](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercícios: Gradientes de Política e RL Ator-Crítico

Continue seu aprendizado nos seguintes notebooks:

* [RL em TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL em PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Outras Tarefas de RL

O Aprendizado por Reforço atualmente é um campo de pesquisa em rápido crescimento. Alguns exemplos interessantes de aprendizado por reforço são:

* Ensinar um computador a jogar **Jogos Atari**. A parte desafiadora desse problema é que não temos um estado simples representado como um vetor, mas sim uma captura de tela - e precisamos usar a CNN para converter essa imagem de tela em um vetor de características, ou para extrair informações de recompensa. Jogos Atari estão disponíveis no Gym.
* Ensinar um computador a jogar jogos de tabuleiro, como Xadrez e Go. Recentemente, programas de ponta como **Alpha Zero** foram treinados do zero por dois agentes jogando um contra o outro e melhorando a cada passo.
* Na indústria, o RL é usado para criar sistemas de controle a partir de simulação. Um serviço chamado [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) é especificamente projetado para isso.

## Conclusão

Agora aprendemos como treinar agentes para alcançar bons resultados apenas fornecendo uma função de recompensa que define o estado desejado do jogo e dando a eles a oportunidade de explorar inteligentemente o espaço de busca. Tentamos com sucesso dois algoritmos e alcançamos um bom resultado em um período relativamente curto de tempo. No entanto, isso é apenas o começo de sua jornada no RL, e você definitivamente deve considerar fazer um curso separado se quiser se aprofundar mais.

## 🚀 Desafio

Explore as aplicações listadas na seção 'Outras Tarefas de RL' e tente implementar uma!

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Revisão e Estudo Autônomo

Aprenda mais sobre aprendizado por reforço clássico em nosso [Currículo de Aprendizado de Máquina para Iniciantes](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Assista a [este ótimo vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como um computador pode aprender a jogar Super Mario.

## Tarefa: [Treine um Carro de Montanha](lab/README.md)

Seu objetivo durante esta tarefa será treinar um ambiente diferente do Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.