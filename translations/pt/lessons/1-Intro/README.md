> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Com o passar do tempo, os recursos computacionais se tornaram mais baratos e mais dados se tornaram disponíveis, então as abordagens de redes neurais começaram a demonstrar um ótimo desempenho em competir com seres humanos em várias áreas, como visão computacional ou compreensão de fala. Na última década, o termo Inteligência Artificial tem sido usado principalmente como sinônimo de Redes Neurais, pois a maioria dos sucessos em IA que ouvimos falar se baseia nelas.

Podemos observar como as abordagens mudaram, por exemplo, na criação de um programa de computador para jogar xadrez:

* Os primeiros programas de xadrez eram baseados em busca – um programa tentava explicitamente estimar os possíveis movimentos de um oponente para um determinado número de jogadas futuras e selecionava um movimento ótimo com base na posição ideal que poderia ser alcançada em algumas jogadas. Isso levou ao desenvolvimento do algoritmo de busca conhecido como [corte alfa-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* As estratégias de busca funcionam bem no final do jogo, onde o espaço de busca é limitado por um pequeno número de possíveis movimentos. No entanto, no início do jogo, o espaço de busca é enorme, e o algoritmo pode ser aprimorado aprendendo com partidas existentes entre jogadores humanos. Experimentos subsequentes empregaram o chamado [raciocínio baseado em casos](https://en.wikipedia.org/wiki/Case-based_reasoning), onde o programa procurava por casos na base de conhecimento muito semelhantes à posição atual no jogo.
* Programas modernos que vencem jogadores humanos são baseados em redes neurais e [aprendizado por reforço](https://en.wikipedia.org/wiki/Reinforcement_learning), onde os programas aprendem a jogar apenas jogando por muito tempo contra si mesmos e aprendendo com seus próprios erros – muito parecido com o que os seres humanos fazem ao aprender a jogar xadrez. No entanto, um programa de computador pode jogar muitas mais partidas em muito menos tempo, e assim pode aprender muito mais rápido.

✅ Faça uma pequena pesquisa sobre outros jogos que foram jogados por IA.

Da mesma forma, podemos ver como a abordagem para criar “programas falantes” (que poderiam passar no teste de Turing) mudou:

* Os primeiros programas desse tipo, como [Eliza](https://en.wikipedia.org/wiki/ELIZA), eram baseados em regras gramaticais muito simples e na reformulação da frase de entrada em uma pergunta.
* Assistentes modernos, como Cortana, Siri ou Google Assistant, são todos sistemas híbridos que usam Redes Neurais para converter fala em texto e reconhecer nossa intenção, e então empregam algum raciocínio ou algoritmos explícitos para realizar as ações necessárias.
* No futuro, podemos esperar um modelo completamente baseado em redes neurais para lidar com diálogos por conta própria. As recentes redes neurais da família GPT e [Turing-NLG](https://turing.microsoft.com/) mostram grande sucesso nisso.

> Imagem por Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) por [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Pesquisa Recente em IA

O enorme crescimento recente na pesquisa de redes neurais começou por volta de 2010, quando grandes conjuntos de dados públicos começaram a se tornar disponíveis. Uma enorme coleção de imagens chamada [ImageNet](https://en.wikipedia.org/wiki/ImageNet), que contém cerca de 14 milhões de imagens anotadas, deu origem ao [Desafio de Reconhecimento Visual em Grande Escala do ImageNet](https://image-net.org/challenges/LSVRC/).

![Precisão do ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)
Em 2012, [Redes Neurais Convolucionais](../4-ComputerVision/07-ConvNets/README.md) foram utilizadas pela primeira vez na classificação de imagens, o que resultou em uma queda significativa nos erros de classificação (de quase 30% para 16,4%). Em 2015, a arquitetura ResNet da Microsoft Research [alcançou precisão em nível humano](https://doi.org/10.1109/ICCV.2015.123).

Desde então, as Redes Neurais demonstraram um comportamento muito bem-sucedido em muitas tarefas:

---

Ano | Paridade Humana alcançada
-----|--------
2015 | [Classificação de Imagens](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Reconhecimento de Fala Conversacional](https://arxiv.org/abs/1610.05256)
2018 | [Tradução Automática de Máquinas](https://arxiv.org/abs/1803.05567) (Chinês para Inglês)
2020 | [Legenda de Imagens](https://arxiv.org/abs/2009.13682)

Nos últimos anos, testemunhamos grandes sucessos com grandes modelos de linguagem, como BERT e GPT-3. Isso ocorreu principalmente devido ao fato de que há uma grande quantidade de dados textuais gerais disponíveis que nos permite treinar modelos para capturar a estrutura e o significado dos textos, pré-treiná-los em coleções de textos gerais e, em seguida, especializar esses modelos para tarefas mais específicas. Aprenderemos mais sobre [Processamento de Linguagem Natural](../5-NLP/README.md) mais adiante neste curso.

## 🚀 Desafio

Faça um tour pela internet para determinar onde, na sua opinião, a IA é utilizada de forma mais eficaz. É em um aplicativo de mapeamento, ou em algum serviço de conversão de fala para texto ou em um videogame? Pesquise como o sistema foi construído.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Revisão & Estudo Autônomo

Revise a história da IA e do ML lendo [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Escolha um elemento do sketchnote no topo dessa lição ou desta e pesquise mais a fundo para entender o contexto cultural que informa sua evolução.

**Tarefa**: [Game Jam](assignment.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.