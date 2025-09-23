<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T08:56:33+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "pt"
}
-->
# Introdução à IA

![Resumo do conteúdo de Introdução à IA em um desenho](../../../../lessons/sketchnotes/ai-intro.png)

> Sketchnote por [Tomomi Imura](https://twitter.com/girlie_mac)

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Inteligência Artificial** é uma disciplina científica fascinante que estuda como podemos fazer os computadores exibirem comportamentos inteligentes, ou seja, realizarem tarefas nas quais os seres humanos são bons.

Originalmente, os computadores foram inventados por [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) para operar com números seguindo um procedimento bem definido - um algoritmo. Os computadores modernos, embora significativamente mais avançados do que o modelo original proposto no século XIX, ainda seguem a mesma ideia de cálculos controlados. Assim, é possível programar um computador para realizar algo se soubermos a sequência exata de passos necessários para atingir o objetivo.

![Foto de uma pessoa](../../../../lessons/1-Intro/images/dsh_age.png)

> Foto por [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Definir a idade de uma pessoa a partir de sua fotografia é uma tarefa que não pode ser programada explicitamente, porque não sabemos como chegamos a um número em nossa mente ao fazê-lo.

---

No entanto, existem algumas tarefas para as quais não sabemos resolver explicitamente. Considere determinar a idade de uma pessoa a partir de sua fotografia. De alguma forma, aprendemos a fazer isso porque vimos muitos exemplos de pessoas de diferentes idades, mas não conseguimos explicar explicitamente como fazemos isso, nem programar um computador para fazê-lo. Este é exatamente o tipo de tarefa que interessa à **Inteligência Artificial** (IA).

✅ Pense em algumas tarefas que você poderia delegar a um computador e que se beneficiariam da IA. Considere os campos das finanças, medicina e artes - como esses campos estão a beneficiar-se hoje da IA?

## IA Fraca vs. IA Forte

IA Fraca | IA Forte
---------------------------------------|-------------------------------------
IA Fraca refere-se a sistemas de IA projetados e treinados para uma tarefa específica ou um conjunto restrito de tarefas.|IA Forte, ou Inteligência Artificial Geral (AGI), refere-se a sistemas de IA com inteligência e compreensão ao nível humano.
Esses sistemas de IA não são geralmente inteligentes; eles se destacam em realizar uma tarefa predefinida, mas não possuem verdadeira compreensão ou consciência.|Esses sistemas de IA têm a capacidade de realizar qualquer tarefa intelectual que um ser humano possa fazer, adaptar-se a diferentes domínios e possuir uma forma de consciência ou autoconsciência.
Exemplos de IA Fraca incluem assistentes virtuais como Siri ou Alexa, algoritmos de recomendação usados por serviços de streaming e chatbots projetados para tarefas específicas de atendimento ao cliente.|Alcançar a IA Forte é um objetivo de longo prazo da pesquisa em IA e exigiria o desenvolvimento de sistemas de IA que possam raciocinar, aprender, compreender e adaptar-se a uma ampla gama de tarefas e contextos.
A IA Fraca é altamente especializada e não possui habilidades cognitivas semelhantes às humanas ou capacidades gerais de resolução de problemas além do seu domínio restrito.|A IA Forte é atualmente um conceito teórico, e nenhum sistema de IA atingiu esse nível de inteligência geral.

Para mais informações, consulte **[Inteligência Artificial Geral](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## A Definição de Inteligência e o Teste de Turing

Um dos problemas ao lidar com o termo **[Inteligência](https://en.wikipedia.org/wiki/Intelligence)** é que não há uma definição clara para ele. Pode-se argumentar que a inteligência está ligada ao **pensamento abstrato** ou à **autoconsciência**, mas não conseguimos defini-la adequadamente.

![Foto de um gato](../../../../lessons/1-Intro/images/photo-cat.jpg)

> [Foto](https://unsplash.com/photos/75715CVEJhI) por [Amber Kipp](https://unsplash.com/@sadmax) do Unsplash

Para perceber a ambiguidade do termo *inteligência*, tente responder à pergunta: "Um gato é inteligente?". Diferentes pessoas tendem a dar respostas diferentes a esta pergunta, pois não há um teste universalmente aceito para provar se a afirmação é verdadeira ou não. E se acha que há - tente submeter o seu gato a um teste de QI...

✅ Pense por um minuto sobre como você define inteligência. Um corvo que consegue resolver um labirinto para obter comida é inteligente? E uma criança, é inteligente?

---

Ao falar sobre AGI, precisamos de alguma forma de determinar se criámos um sistema verdadeiramente inteligente. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) propôs uma maneira chamada **[Teste de Turing](https://en.wikipedia.org/wiki/Turing_test)**, que também funciona como uma definição de inteligência. O teste compara um sistema dado com algo inerentemente inteligente - um ser humano real, e porque qualquer comparação automática pode ser contornada por um programa de computador, usamos um interrogador humano. Assim, se um ser humano não conseguir distinguir entre uma pessoa real e um sistema de computador em um diálogo baseado em texto - o sistema é considerado inteligente.

> Um chatbot chamado [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), desenvolvido em São Petersburgo, chegou perto de passar no Teste de Turing em 2014 usando um truque de personalidade inteligente. Ele anunciou desde o início que era um menino ucraniano de 13 anos, o que explicaria a falta de conhecimento e algumas discrepâncias no texto. O bot convenceu 30% dos juízes de que era humano após um diálogo de 5 minutos, uma métrica que Turing acreditava que uma máquina seria capaz de passar até 2000. No entanto, deve-se entender que isso não indica que criámos um sistema inteligente, ou que um sistema de computador enganou o interrogador humano - o sistema não enganou os humanos, mas sim os criadores do bot!

✅ Alguma vez foi enganado por um chatbot ao pensar que estava a falar com um humano? Como ele o convenceu?

## Diferentes Abordagens à IA

Se quisermos que um computador se comporte como um humano, precisamos de alguma forma modelar dentro do computador a nossa maneira de pensar. Consequentemente, precisamos tentar entender o que torna um ser humano inteligente.

> Para programar inteligência numa máquina, precisamos entender como funcionam os nossos próprios processos de tomada de decisão. Se fizer uma pequena introspeção, perceberá que existem alguns processos que acontecem subconscientemente – por exemplo, conseguimos distinguir um gato de um cão sem pensar muito nisso – enquanto outros envolvem raciocínio.

Existem duas abordagens possíveis para este problema:

Abordagem de Cima para Baixo (Raciocínio Simbólico) | Abordagem de Baixo para Cima (Redes Neurais)
---------------------------------------|-------------------------------------
Uma abordagem de cima para baixo modela a maneira como uma pessoa raciocina para resolver um problema. Envolve extrair **conhecimento** de um ser humano e representá-lo numa forma legível por computador. Também precisamos desenvolver uma maneira de modelar o **raciocínio** dentro de um computador. | Uma abordagem de baixo para cima modela a estrutura do cérebro humano, que consiste num grande número de unidades simples chamadas **neurónios**. Cada neurónio atua como uma média ponderada das suas entradas, e podemos treinar uma rede de neurónios para resolver problemas úteis fornecendo **dados de treino**.

Existem também outras abordagens possíveis para a inteligência:

* Uma abordagem **Emergente**, **Sinergética** ou de **múltiplos agentes** baseia-se no facto de que comportamentos inteligentes complexos podem ser obtidos pela interação de um grande número de agentes simples. De acordo com a [cibernética evolutiva](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), a inteligência pode *emergir* de comportamentos mais simples e reativos no processo de *transição de metassistema*.

* Uma abordagem **Evolutiva**, ou **algoritmo genético**, é um processo de otimização baseado nos princípios da evolução.

Vamos considerar essas abordagens mais tarde no curso, mas por agora vamos focar-nos em duas direções principais: de cima para baixo e de baixo para cima.

### A Abordagem de Cima para Baixo

Numa **abordagem de cima para baixo**, tentamos modelar o nosso raciocínio. Como conseguimos seguir os nossos pensamentos ao raciocinar, podemos tentar formalizar esse processo e programá-lo no computador. Isso é chamado de **raciocínio simbólico**.

As pessoas tendem a ter algumas regras na cabeça que orientam os seus processos de tomada de decisão. Por exemplo, quando um médico está a diagnosticar um paciente, ele ou ela pode perceber que a pessoa tem febre e, portanto, pode haver alguma inflamação no corpo. Ao aplicar um grande conjunto de regras a um problema específico, um médico pode ser capaz de chegar ao diagnóstico final.

Esta abordagem depende muito da **representação do conhecimento** e do **raciocínio**. Extrair conhecimento de um especialista humano pode ser a parte mais difícil, porque um médico, em muitos casos, não saberá exatamente por que está a chegar a um diagnóstico específico. Às vezes, a solução simplesmente surge na sua mente sem um pensamento explícito. Algumas tarefas, como determinar a idade de uma pessoa a partir de uma fotografia, não podem ser de forma alguma reduzidas à manipulação de conhecimento.

### Abordagem de Baixo para Cima

Alternativamente, podemos tentar modelar os elementos mais simples dentro do nosso cérebro – um neurónio. Podemos construir uma chamada **rede neural artificial** dentro de um computador e, em seguida, tentar ensiná-la a resolver problemas fornecendo-lhe exemplos. Este processo é semelhante à forma como um recém-nascido aprende sobre o seu ambiente ao fazer observações.

✅ Faça uma pequena pesquisa sobre como os bebés aprendem. Quais são os elementos básicos do cérebro de um bebé?

> | E o ML?         |      |
> |--------------|-----------|
> | Parte da Inteligência Artificial que se baseia no computador aprender a resolver um problema com base em alguns dados é chamada de **Machine Learning**. Não vamos considerar o aprendizado de máquina clássico neste curso - recomendamos o currículo separado [Machine Learning para Iniciantes](http://aka.ms/ml-beginners). |   ![ML para Iniciantes](../../../../lessons/1-Intro/images/ml-for-beginners.png)    |

## Um Breve Histórico da IA

A Inteligência Artificial começou como um campo no meio do século XX. Inicialmente, o raciocínio simbólico era a abordagem predominante, e isso levou a uma série de sucessos importantes, como sistemas especialistas – programas de computador capazes de atuar como especialistas em alguns domínios de problemas limitados. No entanto, logo ficou claro que essa abordagem não escala bem. Extrair o conhecimento de um especialista, representá-lo num computador e manter essa base de conhecimento precisa revelou-se uma tarefa muito complexa e cara demais para ser prática em muitos casos. Isso levou ao chamado [Inverno da IA](https://en.wikipedia.org/wiki/AI_winter) na década de 1970.

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Com o passar do tempo, os recursos computacionais tornaram-se mais baratos e mais dados ficaram disponíveis, então as abordagens baseadas em redes neurais começaram a demonstrar um ótimo desempenho ao competir com seres humanos em muitas áreas, como visão computacional ou compreensão da fala. Na última década, o termo Inteligência Artificial tem sido usado principalmente como sinônimo de Redes Neurais, porque a maioria dos sucessos da IA que ouvimos falar baseiam-se nelas.

Podemos observar como as abordagens mudaram, por exemplo, na criação de um programa de computador para jogar xadrez:

* Os primeiros programas de xadrez baseavam-se em pesquisa – um programa tentava estimar explicitamente os possíveis movimentos de um oponente para um determinado número de movimentos seguintes e selecionava um movimento ótimo com base na posição ideal que poderia ser alcançada em alguns movimentos. Isso levou ao desenvolvimento do chamado algoritmo de pesquisa [poda alfa-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Estratégias de pesquisa funcionam bem no final do jogo, onde o espaço de pesquisa é limitado por um pequeno número de movimentos possíveis. No entanto, no início do jogo, o espaço de pesquisa é enorme, e o algoritmo pode ser melhorado aprendendo com partidas existentes entre jogadores humanos. Experimentos subsequentes empregaram o chamado [raciocínio baseado em casos](https://en.wikipedia.org/wiki/Case-based_reasoning), onde o programa procurava casos na base de conhecimento muito semelhantes à posição atual no jogo.
* Programas modernos que vencem jogadores humanos baseiam-se em redes neurais e [aprendizado por reforço](https://en.wikipedia.org/wiki/Reinforcement_learning), onde os programas aprendem a jogar jogando contra si mesmos por muito tempo e aprendendo com os próprios erros – muito parecido com o que os seres humanos fazem ao aprender a jogar xadrez. No entanto, um programa de computador pode jogar muito mais jogos em muito menos tempo e, assim, aprender muito mais rápido.

✅ Faça uma pequena pesquisa sobre outros jogos que foram jogados por IA.

Da mesma forma, podemos ver como a abordagem para criar “programas que falam” (que poderiam passar no Teste de Turing) mudou:

* Os primeiros programas desse tipo, como [Eliza](https://en.wikipedia.org/wiki/ELIZA), baseavam-se em regras gramaticais muito simples e na reformulação da frase de entrada numa pergunta.
* Assistentes modernos, como Cortana, Siri ou Google Assistant, são todos sistemas híbridos que usam redes neurais para converter fala em texto e reconhecer nossa intenção, e depois empregam algum raciocínio ou algoritmos explícitos para realizar as ações necessárias.
* No futuro, podemos esperar um modelo completamente baseado em redes neurais para lidar com o diálogo por conta própria. As recentes famílias de redes neurais GPT e [Turing-NLG](https://turing.microsoft.com/) mostram grande sucesso nisso.

> Imagem de Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) de [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Investigação Recente em IA

O enorme crescimento recente na investigação sobre redes neuronais começou por volta de 2010, quando grandes conjuntos de dados públicos começaram a estar disponíveis. Uma vasta coleção de imagens chamada [ImageNet](https://en.wikipedia.org/wiki/ImageNet), que contém cerca de 14 milhões de imagens anotadas, deu origem ao [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Precisão do ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Imagem de [Dmitry Soshnikov](http://soshnikov.com)

Em 2012, as [Redes Neuronais Convolucionais](../4-ComputerVision/07-ConvNets/README.md) foram usadas pela primeira vez na classificação de imagens, o que levou a uma redução significativa nos erros de classificação (de quase 30% para 16,4%). Em 2015, a arquitetura ResNet da Microsoft Research [atingiu precisão ao nível humano](https://doi.org/10.1109/ICCV.2015.123).

Desde então, as Redes Neuronais demonstraram um desempenho muito bem-sucedido em muitas tarefas:

---

Ano | Paridade Humana alcançada
-----|--------
2015 | [Classificação de Imagens](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Reconhecimento de Fala Conversacional](https://arxiv.org/abs/1610.05256)
2018 | [Tradução Automática de Máquinas](https://arxiv.org/abs/1803.05567) (Chinês para Inglês)
2020 | [Legenda Automática de Imagens](https://arxiv.org/abs/2009.13682)

Nos últimos anos, assistimos a enormes sucessos com modelos de linguagem de grande escala, como o BERT e o GPT-3. Isto aconteceu principalmente devido ao facto de haver uma grande quantidade de dados textuais gerais disponíveis, o que permite treinar modelos para capturar a estrutura e o significado dos textos, pré-treiná-los em coleções de textos gerais e, em seguida, especializar esses modelos para tarefas mais específicas. Vamos aprender mais sobre [Processamento de Linguagem Natural](../5-NLP/README.md) mais adiante neste curso.

## 🚀 Desafio

Faça uma pesquisa na internet para determinar onde, na sua opinião, a IA é mais eficazmente utilizada. Será numa aplicação de mapas, num serviço de conversão de fala para texto ou num videojogo? Investigue como o sistema foi construído.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Revisão e Estudo Autónomo

Revise a história da IA e do ML lendo [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Escolha um elemento do sketchnote no início dessa lição ou desta e investigue-o mais a fundo para compreender o contexto cultural que influenciou a sua evolução.

**Tarefa**: [Game Jam](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.