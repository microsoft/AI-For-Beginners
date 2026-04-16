# Algoritmos Genéticos

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algoritmos Genéticos** (AG) são baseados em uma **abordagem evolucionária** para IA, na qual métodos de evolução de uma população são usados para obter uma solução ótima para um problema específico. Eles foram propostos em 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Os Algoritmos Genéticos são baseados nas seguintes ideias:

* Soluções válidas para o problema podem ser representadas como **genes**
* O **Crossover** permite combinar duas soluções para obter uma nova solução válida
* A **Seleção** é usada para escolher as soluções mais ótimas utilizando alguma **função de aptidão**
* **Mutações** são introduzidas para desestabilizar a otimização e nos tirar de mínimos locais

Se você quiser implementar um Algoritmo Genético, precisará do seguinte:

 * Encontrar um método para codificar as soluções do problema usando **genes** g&in;&Gamma;
 * No conjunto de genes &Gamma;, é necessário definir uma **função de aptidão** fit: &Gamma;&rightarrow;**R**. Valores menores da função correspondem a melhores soluções.
 * Definir um mecanismo de **crossover** para combinar dois genes e obter uma nova solução válida crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definir um mecanismo de **mutação** mutate: &Gamma;&rightarrow;&Gamma;.

Em muitos casos, os algoritmos de crossover e mutação são bastante simples para manipular genes como sequências numéricas ou vetores de bits.

A implementação específica de um algoritmo genético pode variar de caso para caso, mas a estrutura geral é a seguinte:

1. Selecionar uma população inicial G&subset;&Gamma;
2. Selecionar aleatoriamente uma das operações que será realizada nesta etapa: crossover ou mutação
3. **Crossover**:
  * Selecionar aleatoriamente dois genes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Calcular o crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Se fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - substituir o gene correspondente na população por g.
4. **Mutação** - selecionar um gene aleatório g&in;G e substituí-lo por mutate(g)
5. Repetir a partir do passo 2, até obtermos um valor suficientemente pequeno de fit, ou até que o limite de número de etapas seja alcançado.

## Tarefas Típicas

As tarefas tipicamente resolvidas por Algoritmos Genéticos incluem:

1. Otimização de cronogramas
1. Empacotamento ótimo
1. Corte ótimo
1. Aceleração de busca exaustiva

## ✍️ Exercícios: Algoritmos Genéticos

Continue seu aprendizado nos seguintes notebooks:

Acesse [este notebook](Genetic.ipynb) para ver dois exemplos de uso de Algoritmos Genéticos:

1. Divisão justa de tesouro
1. Problema das 8 Rainhas

## Conclusão

Os Algoritmos Genéticos são usados para resolver muitos problemas, incluindo logística e problemas de busca. O campo é inspirado por pesquisas que uniram tópicos de Psicologia e Ciência da Computação.

## 🚀 Desafio

"Algoritmos genéticos são simples de implementar, mas seu comportamento é difícil de entender." [fonte](https://wikipedia.org/wiki/Genetic_algorithm) Faça uma pesquisa para encontrar uma implementação de um algoritmo genético, como resolver um quebra-cabeça de Sudoku, e explique como ele funciona em forma de esboço ou fluxograma.

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Revisão & Autoestudo

Assista a [este ótimo vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como computadores podem aprender a jogar Super Mario usando redes neurais treinadas por algoritmos genéticos. Aprenderemos mais sobre computadores aprendendo a jogar jogos como esse [na próxima seção](../22-DeepRL/README.md).

## [Tarefa: Equação Diofantina](Diophantine.ipynb)

Seu objetivo é resolver a chamada **equação diofantina** - uma equação com raízes inteiras. Por exemplo, considere a equação a+2b+3c+4d=30. Você precisa encontrar as raízes inteiras que satisfazem essa equação.

*Esta tarefa é inspirada por [este post](https://habr.com/post/128704/).*

Dicas:

1. Você pode considerar raízes no intervalo [0;30]
1. Como gene, considere usar a lista de valores das raízes

Use [Diophantine.ipynb](Diophantine.ipynb) como ponto de partida.

---

