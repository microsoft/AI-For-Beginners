# Mecanismos de Atenção e Transformers

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Um dos problemas mais importantes no domínio do PLN é **tradução automática**, uma tarefa essencial que fundamenta ferramentas como o Google Translate. Nesta seção, focaremos na tradução automática ou, de forma mais geral, em qualquer tarefa *sequência-para-sequência* (que também é chamada de **transdução de sentenças**).

Com RNNs, a sequência-para-sequência é implementada por duas redes recorrentes, onde uma rede, o **codificador**, colapsa uma sequência de entrada em um estado oculto, enquanto outra rede, o **decodificador**, desdobra esse estado oculto em um resultado traduzido. Existem alguns problemas com essa abordagem:

* O estado final da rede codificadora tem dificuldade em lembrar o início de uma sentença, causando assim uma qualidade ruim do modelo para sentenças longas.
* Todas as palavras em uma sequência têm o mesmo impacto no resultado. Na realidade, no entanto, palavras específicas na sequência de entrada frequentemente têm mais impacto nas saídas sequenciais do que outras.

**Mecanismos de Atenção** fornecem um meio de ponderar o impacto contextual de cada vetor de entrada em cada previsão de saída da RNN. A forma como é implementado é criando atalhos entre estados intermediários da RNN de entrada e da RNN de saída. Dessa maneira, ao gerar o símbolo de saída y<sub>t</sub>, levaremos em conta todos os estados ocultos de entrada h<sub>i</sub>, com diferentes coeficientes de peso α<sub>t,i</sub>.

![Imagem mostrando um modelo codificador/decodificador com uma camada de atenção aditiva](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.pt.png)

> O modelo codificador-decodificador com mecanismo de atenção aditiva em [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), citado a partir [deste post de blog](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

A matriz de atenção {α<sub>i,j</sub>} representaria o grau em que certas palavras de entrada desempenham na geração de uma palavra específica na sequência de saída. Abaixo está um exemplo de tal matriz:

![Imagem mostrando um alinhamento de exemplo encontrado por RNNsearch-50, tirada de Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.pt.png)

> Figura de [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Os mecanismos de atenção são responsáveis por grande parte do estado da arte atual ou quase atual em PLN. No entanto, adicionar atenção aumenta significativamente o número de parâmetros do modelo, o que levou a problemas de escalabilidade com RNNs. Uma restrição chave da escalabilidade das RNNs é que a natureza recorrente dos modelos torna desafiador agrupar e paralelizar o treinamento. Em uma RNN, cada elemento de uma sequência precisa ser processado em ordem sequencial, o que significa que não pode ser facilmente paralelizado.

![Codificador Decodificador com Atenção](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figura do [Blog do Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

A adoção de mecanismos de atenção combinada com essa restrição levou à criação dos agora modelos Transformer de Estado da Arte que conhecemos e usamos hoje, como BERT e Open-GPT3.

## Modelos Transformer

Uma das principais ideias por trás dos transformers é evitar a natureza sequencial das RNNs e criar um modelo que seja paralelizável durante o treinamento. Isso é alcançado implementando duas ideias:

* codificação posicional
* uso de mecanismo de autoatenção para capturar padrões em vez de RNNs (ou CNNs) (é por isso que o artigo que introduz os transformers é chamado *[Atenção é tudo o que você precisa](https://arxiv.org/abs/1706.03762)*)

### Codificação/Embutimento Posicional

A ideia da codificação posicional é a seguinte. 
1. Ao usar RNNs, a posição relativa dos tokens é representada pelo número de etapas e, portanto, não precisa ser explicitamente representada. 
2. No entanto, uma vez que mudamos para atenção, precisamos saber as posições relativas dos tokens dentro de uma sequência. 
3. Para obter a codificação posicional, aumentamos nossa sequência de tokens com uma sequência de posições de tokens na sequência (ou seja, uma sequência de números 0, 1, ...).
4. Em seguida, misturamos a posição do token com um vetor de embutimento de token. Para transformar a posição (inteiro) em um vetor, podemos usar diferentes abordagens:

* Embutimento treinável, semelhante ao embutimento de token. Esta é a abordagem que consideramos aqui. Aplicamos camadas de embutimento tanto em tokens quanto em suas posições, resultando em vetores de embutimento das mesmas dimensões, que então somamos.
* Função de codificação de posição fixa, conforme proposto no artigo original.

<img src="images/pos-embedding.png" width="50%"/>

> Imagem do autor

O resultado que obtemos com o embutimento posicional incorpora tanto o token original quanto sua posição dentro de uma sequência.

### Autoatenção Multi-Cabeça

Em seguida, precisamos capturar alguns padrões dentro da nossa sequência. Para fazer isso, os transformers usam um mecanismo de **autoatenção**, que é essencialmente atenção aplicada à mesma sequência como entrada e saída. A aplicação de autoatenção nos permite levar em conta o **contexto** dentro da sentença e ver quais palavras estão inter-relacionadas. Por exemplo, isso nos permite ver quais palavras são referidas por co-referências, como *isso*, e também levar o contexto em consideração:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.pt.png)

> Imagem do [Blog do Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Nos transformers, usamos **Atenção Multi-Cabeça** para dar ao modelo o poder de capturar vários tipos diferentes de dependências, por exemplo, relações de palavras de longo prazo versus curto prazo, co-referência versus algo mais, etc.

[Notebook TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) contém mais detalhes sobre a implementação das camadas de transformer.

### Atenção Codificador-Decodificador

Nos transformers, a atenção é usada em dois lugares:

* Para capturar padrões dentro do texto de entrada usando autoatenção
* Para realizar tradução de sequência - é a camada de atenção entre codificador e decodificador.

A atenção codificador-decodificador é muito semelhante ao mecanismo de atenção usado em RNNs, como descrito no início desta seção. Este diagrama animado explica o papel da atenção codificador-decodificador.

![GIF animado mostrando como as avaliações são realizadas em modelos transformer.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Como cada posição de entrada é mapeada independentemente para cada posição de saída, os transformers podem ser paralelizados melhor do que as RNNs, o que permite modelos de linguagem muito maiores e mais expressivos. Cada cabeça de atenção pode ser usada para aprender diferentes relações entre palavras que melhoram as tarefas de Processamento de Linguagem Natural a jusante.

## BERT

**BERT** (Representações de Codificador Bidirecional de Transformers) é uma rede transformer multilayer muito grande com 12 camadas para *BERT-base* e 24 para *BERT-large*. O modelo é primeiro pré-treinado em um grande corpus de dados textuais (WikiPedia + livros) usando treinamento não supervisionado (previsão de palavras mascaradas em uma sentença). Durante o pré-treinamento, o modelo absorve níveis significativos de compreensão da linguagem, que podem ser aproveitados com outros conjuntos de dados usando ajuste fino. Este processo é chamado de **aprendizado por transferência**.

![imagem de http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.pt.png)

> Imagem [fonte](http://jalammar.github.io/illustrated-bert/)

## ✍️ Exercícios: Transformers

Continue seu aprendizado nos seguintes notebooks:

* [Transformers em PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformers em TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Conclusão

Nesta lição, você aprendeu sobre Transformers e Mecanismos de Atenção, todas ferramentas essenciais no conjunto de ferramentas de PLN. Existem muitas variações das arquiteturas Transformer, incluindo BERT, DistilBERT, BigBird, OpenGPT3 e mais, que podem ser ajustadas. O [pacote HuggingFace](https://github.com/huggingface/) fornece um repositório para treinar muitas dessas arquiteturas com PyTorch e TensorFlow.

## 🚀 Desafio

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Revisão & Autoestudo

* [Post de blog](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), explicando o clássico artigo [Atenção é tudo o que você precisa](https://arxiv.org/abs/1706.03762) sobre transformers.
* [Uma série de posts de blog](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) sobre transformers, explicando a arquitetura em detalhes.

## [Tarefa](assignment.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas que possam surgir do uso desta tradução.