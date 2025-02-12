# Algoritmos Genéticos

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algoritmos Genéticos** (GA) são baseados em uma **abordagem evolutiva** para IA, na qual métodos da evolução de uma população são usados para obter uma solução ótima para um determinado problema. Eles foram propostos em 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Os Algoritmos Genéticos se baseiam nas seguintes ideias:

* Soluções válidas para o problema podem ser representadas como **genes**
* **Crossover** nos permite combinar duas soluções para obter uma nova solução válida
* **Seleção** é utilizada para selecionar soluções mais ótimas usando alguma **função de aptidão**
* **Mutações** são introduzidas para desestabilizar a otimização e nos tirar do mínimo local

Se você deseja implementar um Algoritmo Genético, precisa do seguinte:

 * Encontrar um método de codificação das soluções do nosso problema usando **genes** g∈Γ
 * No conjunto de genes Γ, precisamos definir a **função de aptidão** fit: Γ→**R**. Valores de função menores correspondem a soluções melhores.
 * Definir um mecanismo de **crossover** para combinar dois genes e obter uma nova solução válida crossover: Γ<sup>2</sub>→Γ.
 * Definir um mecanismo de **mutação** mutate: Γ→Γ.

Em muitos casos, crossover e mutação são algoritmos bastante simples para manipular genes como sequências numéricas ou vetores de bits.

A implementação específica de um algoritmo genético pode variar de caso a caso, mas a estrutura geral é a seguinte:

1. Selecionar uma população inicial G⊂Γ
2. Selecionar aleatoriamente uma das operações que será realizada nesta etapa: crossover ou mutação
3. **Crossover**:
  * Selecionar aleatoriamente dois genes g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Calcular crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Se fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - substituir o gene correspondente na população por g.
4. **Mutação** - selecionar um gene aleatório g∈G e substituí-lo por mutate(g)
5. Repetir a partir do passo 2, até que obtenhamos um valor suficientemente pequeno de fit, ou até que o limite no número de etapas seja alcançado.

## Tarefas Típicas

Tarefas tipicamente resolvidas por Algoritmos Genéticos incluem:

1. Otimização de cronogramas
1. Empacotamento ótimo
1. Corte ótimo
1. Aceleração da busca exaustiva

## ✍️ Exercícios: Algoritmos Genéticos

Continue seu aprendizado nos seguintes cadernos:

Vá para [este caderno](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) para ver dois exemplos de uso de Algoritmos Genéticos:

1. Divisão justa do tesouro
1. Problema das 8 Rainhas

## Conclusão

Os Algoritmos Genéticos são usados para resolver muitos problemas, incluindo problemas de logística e busca. O campo é inspirado por pesquisas que mesclaram tópicos em Psicologia e Ciência da Computação.

## 🚀 Desafio

"Algoritmos genéticos são simples de implementar, mas seu comportamento é difícil de entender." [fonte](https://wikipedia.org/wiki/Genetic_algorithm) Faça algumas pesquisas para encontrar uma implementação de um algoritmo genético, como resolver um quebra-cabeça Sudoku, e explique como funciona em um esboço ou fluxograma.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Revisão e Autoestudo

Assista [a este ótimo vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como computadores podem aprender a jogar Super Mario usando redes neurais treinadas por algoritmos genéticos. Aprenderemos mais sobre o aprendizado de computador para jogar jogos assim [na próxima seção](../22-DeepRL/README.md).

## [Tarefa: Equação Diofantina](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Seu objetivo é resolver a chamada **equação diofantina** - uma equação com raízes inteiras. Por exemplo, considere a equação a+2b+3c+4d=30. Você precisa encontrar as raízes inteiras que satisfazem essa equação.

*Esta tarefa é inspirada [neste post](https://habr.com/post/128704/).*

Dicas:

1. Você pode considerar que as raízes estão no intervalo [0;30]
1. Como gene, considere usar a lista de valores das raízes

Use [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) como ponto de partida.

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.