# Algoritmos Genéticos

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algoritmos Genéticos** (GA) baseiam-se numa abordagem **evolutiva** para IA, em que métodos de evolução de uma população são utilizados para obter uma solução ótima para um determinado problema. Foram propostos em 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Os Algoritmos Genéticos baseiam-se nas seguintes ideias:

* Soluções válidas para o problema podem ser representadas como **genes**
* O **Cruzamento** permite combinar duas soluções para obter uma nova solução válida
* A **Seleção** é usada para escolher soluções mais ótimas utilizando uma **função de aptidão**
* **Mutação** é introduzida para desestabilizar a otimização e sair de mínimos locais

Se quiser implementar um Algoritmo Genético, precisa do seguinte:

 * Encontrar um método para codificar as soluções do problema utilizando **genes** g&in;&Gamma;
 * No conjunto de genes &Gamma;, é necessário definir uma **função de aptidão** fit: &Gamma;&rightarrow;**R**. Valores menores da função correspondem a melhores soluções.
 * Definir um mecanismo de **cruzamento** para combinar dois genes e obter uma nova solução válida crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definir um mecanismo de **mutação** mutate: &Gamma;&rightarrow;&Gamma;.

Em muitos casos, os algoritmos de cruzamento e mutação são bastante simples para manipular genes como sequências numéricas ou vetores de bits.

A implementação específica de um algoritmo genético pode variar de caso para caso, mas a estrutura geral é a seguinte:

1. Selecionar uma população inicial G&subset;&Gamma;
2. Selecionar aleatoriamente uma das operações que será realizada neste passo: cruzamento ou mutação
3. **Cruzamento**:
  * Selecionar aleatoriamente dois genes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Calcular o cruzamento g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Se fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - substituir o gene correspondente na população por g.
4. **Mutação** - selecionar um gene aleatório g&in;G e substituí-lo por mutate(g)
5. Repetir a partir do passo 2, até obter um valor suficientemente pequeno de fit, ou até atingir o limite de passos.

## Tarefas Típicas

As tarefas tipicamente resolvidas por Algoritmos Genéticos incluem:

1. Otimização de horários
1. Empacotamento ótimo
1. Corte ótimo
1. Aceleração de busca exaustiva

## ✍️ Exercícios: Algoritmos Genéticos

Continue a sua aprendizagem nos seguintes notebooks:

Aceda a [este notebook](Genetic.ipynb) para ver dois exemplos de utilização de Algoritmos Genéticos:

1. Divisão justa de tesouro
1. Problema das 8 Rainhas

## Conclusão

Os Algoritmos Genéticos são usados para resolver muitos problemas, incluindo logística e problemas de busca. Este campo é inspirado por pesquisas que fundiram tópicos em Psicologia e Ciência da Computação.

## 🚀 Desafio

"Os algoritmos genéticos são simples de implementar, mas o seu comportamento é difícil de entender." [fonte](https://wikipedia.org/wiki/Genetic_algorithm) Faça uma pesquisa para encontrar uma implementação de um algoritmo genético, como resolver um puzzle de Sudoku, e explique como funciona através de um esboço ou fluxograma.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Revisão & Autoestudo

Veja [este excelente vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como um computador pode aprender a jogar Super Mario utilizando redes neurais treinadas por algoritmos genéticos. Vamos aprender mais sobre computadores a jogar jogos como este [na próxima seção](../22-DeepRL/README.md).

## [Tarefa: Equação Diofantina](Diophantine.ipynb)

O seu objetivo é resolver a chamada **equação Diofantina** - uma equação com raízes inteiras. Por exemplo, considere a equação a+2b+3c+4d=30. É necessário encontrar as raízes inteiras que satisfaçam esta equação.

*Esta tarefa é inspirada por [este post](https://habr.com/post/128704/).*

Dicas:

1. Pode considerar raízes no intervalo [0;30]
1. Como gene, considere usar a lista de valores das raízes

Use [Diophantine.ipynb](Diophantine.ipynb) como ponto de partida.

---

