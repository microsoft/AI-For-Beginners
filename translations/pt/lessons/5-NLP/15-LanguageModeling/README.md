# Modelagem de Linguagem

Embutimentos semânticos, como Word2Vec e GloVe, são na verdade um primeiro passo em direção à **modelagem de linguagem** - criar modelos que de alguma forma *entendem* (ou *representam*) a natureza da linguagem.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

A ideia principal por trás da modelagem de linguagem é treiná-los em conjuntos de dados não rotulados de maneira não supervisionada. Isso é importante porque temos grandes quantidades de texto não rotulado disponíveis, enquanto a quantidade de texto rotulado sempre seria limitada pela quantidade de esforço que podemos gastar na rotulagem. Na maioria das vezes, podemos construir modelos de linguagem que podem **prever palavras ausentes** no texto, porque é fácil mascarar uma palavra aleatória no texto e usá-la como uma amostra de treinamento.

## Treinamento de Embutimentos

Em nossos exemplos anteriores, usamos embutimentos semânticos pré-treinados, mas é interessante ver como esses embutimentos podem ser treinados. Existem várias ideias possíveis que podem ser usadas:

* Modelagem de linguagem **N-Gram**, quando prevemos um token olhando para N tokens anteriores (N-gram)
* **Continuous Bag-of-Words** (CBoW), quando prevemos o token do meio $W_0$ em uma sequência de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, onde prevemos um conjunto de tokens vizinhos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partir do token do meio $W_0$.

![imagem do artigo sobre conversão de palavras em vetores](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.pt.png)

> Imagem do [este artigo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks de Exemplo: Treinando o modelo CBoW

Continue seu aprendizado nos seguintes notebooks:

* [Treinando CBoW Word2Vec com TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Treinando CBoW Word2Vec com PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusão

Na lição anterior, vimos que os embutimentos de palavras funcionam como mágica! Agora sabemos que treinar embutimentos de palavras não é uma tarefa muito complexa, e devemos ser capazes de treinar nossos próprios embutimentos de palavras para texto específico de domínio, se necessário.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Revisão & Estudo Autônomo

* [Tutorial oficial do PyTorch sobre Modelagem de Linguagem](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial do TensorFlow sobre treinamento de modelo Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Usar o framework **gensim** para treinar os embutimentos mais comumente usados em algumas linhas de código é descrito [nesta documentação](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tarefa: Treinar Modelo Skip-Gram](lab/README.md)

No laboratório, desafiamos você a modificar o código desta lição para treinar o modelo skip-gram em vez do CBoW. [Leia os detalhes](lab/README.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.