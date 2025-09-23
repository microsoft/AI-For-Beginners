<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-24T09:01:46+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "pt"
}
-->
# Algoritmos Genéticos

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algoritmos Genéticos** (AG) baseiam-se numa abordagem **evolutiva** para a IA, em que métodos de evolução de uma população são utilizados para obter uma solução ótima para um determinado problema. Foram propostos em 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Os Algoritmos Genéticos baseiam-se nas seguintes ideias:

* Soluções válidas para o problema podem ser representadas como **genes**
* O **crossover** permite combinar duas soluções para obter uma nova solução válida
* A **seleção** é usada para escolher soluções mais otimizadas utilizando uma **função de aptidão**
* **Mutações** são introduzidas para desestabilizar a otimização e evitar mínimos locais

Se quiser implementar um Algoritmo Genético, precisará do seguinte:

 * Encontrar um método para codificar as soluções do problema utilizando **genes** g∈Γ
 * No conjunto de genes Γ, é necessário definir uma **função de aptidão** fit: Γ→**R**. Valores menores da função correspondem a melhores soluções.
 * Definir um mecanismo de **crossover** para combinar dois genes e obter uma nova solução válida crossover: Γ<sup>2</sub>→Γ.
 * Definir um mecanismo de **mutação** mutate: Γ→Γ.

Em muitos casos, os algoritmos de crossover e mutação são bastante simples, manipulando genes como sequências numéricas ou vetores de bits.

A implementação específica de um algoritmo genético pode variar de caso para caso, mas a estrutura geral é a seguinte:

1. Selecionar uma população inicial G⊂Γ
2. Selecionar aleatoriamente uma das operações a ser realizada neste passo: crossover ou mutação
3. **Crossover**:
  * Selecionar aleatoriamente dois genes g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Calcular o crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Se fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - substituir o gene correspondente na população por g.
4. **Mutação** - selecionar um gene aleatório g∈G e substituí-lo por mutate(g)
5. Repetir a partir do passo 2, até obtermos um valor suficientemente pequeno de fit, ou até atingir o limite de passos.

## Tarefas Típicas

As tarefas tipicamente resolvidas por Algoritmos Genéticos incluem:

1. Otimização de horários
1. Empacotamento ótimo
1. Corte ótimo
1. Aceleração de buscas exaustivas

## ✍️ Exercícios: Algoritmos Genéticos

Continue a sua aprendizagem nos seguintes notebooks:

Aceda a [este notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) para ver dois exemplos de utilização de Algoritmos Genéticos:

1. Divisão justa de um tesouro
1. Problema das 8 Rainhas

## Conclusão

Os Algoritmos Genéticos são usados para resolver muitos problemas, incluindo problemas de logística e de busca. Este campo é inspirado por pesquisas que combinam tópicos de Psicologia e Ciência da Computação.

## 🚀 Desafio

"Os algoritmos genéticos são simples de implementar, mas o seu comportamento é difícil de compreender." [fonte](https://wikipedia.org/wiki/Genetic_algorithm) Faça uma pesquisa para encontrar uma implementação de um algoritmo genético, como a resolução de um puzzle de Sudoku, e explique como funciona através de um esboço ou fluxograma.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Revisão e Autoestudo

Veja [este excelente vídeo](https://www.youtube.com/watch?v=qv6UVOQ0F44) que fala sobre como um computador pode aprender a jogar Super Mario utilizando redes neurais treinadas por algoritmos genéticos. Vamos aprender mais sobre computadores a jogar jogos como este [na próxima secção](../22-DeepRL/README.md).

## [Tarefa: Equação Diofantina](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

O seu objetivo é resolver a chamada **equação diofantina** - uma equação com raízes inteiras. Por exemplo, considere a equação a+2b+3c+4d=30. É necessário encontrar as raízes inteiras que satisfaçam esta equação.

*Esta tarefa é inspirada por [este post](https://habr.com/post/128704/).*

Dicas:

1. Pode considerar as raízes no intervalo [0;30]
1. Como gene, considere usar a lista de valores das raízes

Use [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) como ponto de partida.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.