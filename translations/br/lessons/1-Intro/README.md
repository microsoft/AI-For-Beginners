<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-26T09:00:29+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "br"
}
-->
> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Com o passar do tempo, os recursos computacionais se tornaram mais acessíveis, e mais dados passaram a estar disponíveis, permitindo que abordagens baseadas em redes neurais demonstrassem um desempenho impressionante, competindo com seres humanos em diversas áreas, como visão computacional e compreensão de fala. Na última década, o termo Inteligência Artificial tem sido amplamente usado como sinônimo de Redes Neurais, já que a maioria dos sucessos em IA que ouvimos falar são baseados nelas.

Podemos observar como as abordagens mudaram, por exemplo, na criação de um programa de computador para jogar xadrez:

* Os primeiros programas de xadrez eram baseados em busca – o programa tentava explicitamente estimar os possíveis movimentos do oponente para um determinado número de jogadas futuras e selecionava o movimento ideal com base na melhor posição que poderia ser alcançada em algumas jogadas. Isso levou ao desenvolvimento do algoritmo de busca chamado [poda alfa-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Estratégias de busca funcionam bem no final do jogo, onde o espaço de busca é limitado por um número reduzido de movimentos possíveis. No entanto, no início do jogo, o espaço de busca é enorme, e o algoritmo pode ser melhorado aprendendo com partidas existentes entre jogadores humanos. Experimentos subsequentes empregaram o chamado [raciocínio baseado em casos](https://en.wikipedia.org/wiki/Case-based_reasoning), onde o programa buscava casos na base de conhecimento muito semelhantes à posição atual no jogo.
* Programas modernos que vencem jogadores humanos são baseados em redes neurais e [aprendizado por reforço](https://en.wikipedia.org/wiki/Reinforcement_learning), onde os programas aprendem a jogar exclusivamente jogando contra si mesmos por um longo período e aprendendo com seus próprios erros – muito parecido com o que os seres humanos fazem ao aprender a jogar xadrez. No entanto, um programa de computador pode jogar muito mais partidas em muito menos tempo, aprendendo assim de forma muito mais rápida.

✅ Faça uma pequena pesquisa sobre outros jogos que já foram jogados por IA.

De forma semelhante, podemos observar como a abordagem para criar “programas que falam” (que poderiam passar no teste de Turing) mudou:

* Os primeiros programas desse tipo, como [Eliza](https://en.wikipedia.org/wiki/ELIZA), eram baseados em regras gramaticais muito simples e na reformulação da frase de entrada em uma pergunta.
* Assistentes modernos, como Cortana, Siri ou Google Assistant, são todos sistemas híbridos que utilizam redes neurais para converter fala em texto e reconhecer nossa intenção, e depois empregam algum raciocínio ou algoritmos explícitos para realizar as ações necessárias.
* No futuro, podemos esperar um modelo completamente baseado em redes neurais para lidar com diálogos de forma autônoma. As recentes redes neurais da família GPT e [Turing-NLG](https://turing.microsoft.com/) têm mostrado grande sucesso nesse sentido.

> Imagem por Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) por [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Pesquisas Recentes em IA

O enorme crescimento recente na pesquisa de redes neurais começou por volta de 2010, quando grandes conjuntos de dados públicos começaram a se tornar disponíveis. Uma vasta coleção de imagens chamada [ImageNet](https://en.wikipedia.org/wiki/ImageNet), que contém cerca de 14 milhões de imagens anotadas, deu origem ao [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Precisão do ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Em 2012, [Redes Neurais Convolucionais](../4-ComputerVision/07-ConvNets/README.md) foram usadas pela primeira vez na classificação de imagens, o que levou a uma queda significativa nos erros de classificação (de quase 30% para 16,4%). Em 2015, a arquitetura ResNet da Microsoft Research [alcançou precisão em nível humano](https://doi.org/10.1109/ICCV.2015.123).

Desde então, as Redes Neurais demonstraram um desempenho muito bem-sucedido em diversas tarefas:

---

Ano | Paridade com Humanos alcançada
-----|--------
2015 | [Classificação de Imagens](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Reconhecimento de Fala Conversacional](https://arxiv.org/abs/1610.05256)
2018 | [Tradução Automática de Máquinas](https://arxiv.org/abs/1803.05567) (Chinês para Inglês)
2020 | [Geração de Legendas para Imagens](https://arxiv.org/abs/2009.13682)

Nos últimos anos, testemunhamos grandes avanços com modelos de linguagem de grande escala, como BERT e GPT-3. Isso aconteceu principalmente devido ao fato de haver uma grande quantidade de dados textuais gerais disponíveis, permitindo treinar modelos para capturar a estrutura e o significado dos textos, pré-treiná-los em coleções de textos gerais e, em seguida, especializá-los para tarefas mais específicas. Vamos aprender mais sobre [Processamento de Linguagem Natural](../5-NLP/README.md) mais adiante neste curso.

## 🚀 Desafio

Faça uma pesquisa na internet para determinar onde, na sua opinião, a IA é mais eficazmente utilizada. É em um aplicativo de mapeamento, em algum serviço de conversão de fala para texto ou em um videogame? Pesquise como o sistema foi construído.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Revisão e Autoestudo

Revise a história da IA e do aprendizado de máquina lendo [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Escolha um elemento do sketchnote no início dessa lição ou desta e pesquise mais a fundo para entender o contexto cultural que influenciou sua evolução.

**Tarefa**: [Game Jam](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.