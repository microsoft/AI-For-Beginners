# Modelagem de Linguagem

Embeddings semânticos, como Word2Vec e GloVe, são, na verdade, um primeiro passo em direção à **modelagem de linguagem** - criando modelos que de alguma forma *entendem* (ou *representam*) a natureza da linguagem.

## [Pré-quiz da aula](https://ff-quizzes.netlify.app/en/ai/quiz/29)

A ideia principal por trás da modelagem de linguagem é treiná-los em conjuntos de dados não rotulados de forma não supervisionada. Isso é importante porque temos uma enorme quantidade de texto não rotulado disponível, enquanto a quantidade de texto rotulado sempre será limitada pelo esforço que podemos dedicar à rotulagem. Na maioria das vezes, podemos construir modelos de linguagem que conseguem **prever palavras ausentes** no texto, porque é fácil mascarar uma palavra aleatória no texto e usá-la como um exemplo de treinamento.

## Treinando Embeddings

Nos nossos exemplos anteriores, usamos embeddings semânticos pré-treinados, mas é interessante ver como esses embeddings podem ser treinados. Existem várias ideias possíveis que podem ser utilizadas:

* **Modelagem de linguagem N-Gram**, onde prevemos um token olhando para os N tokens anteriores (N-grama).
* **Continuous Bag-of-Words** (CBoW), onde prevemos o token do meio $W_0$ em uma sequência de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, onde prevemos um conjunto de tokens vizinhos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partir do token do meio $W_0$.

![imagem do artigo sobre conversão de palavras em vetores](../../../../../translated_images/pt-BR/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Imagem retirada [deste artigo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Exemplos de Notebooks: Treinando o modelo CBoW

Continue seu aprendizado nos seguintes notebooks:

* [Treinando CBoW Word2Vec com TensorFlow](CBoW-TF.ipynb)
* [Treinando CBoW Word2Vec com PyTorch](CBoW-PyTorch.ipynb)

## Conclusão

Na lição anterior, vimos que embeddings de palavras funcionam como mágica! Agora sabemos que treinar embeddings de palavras não é uma tarefa muito complexa, e devemos ser capazes de treinar nossos próprios embeddings para textos específicos de domínio, se necessário.

## [Pós-quiz da aula](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Revisão e Autoestudo

* [Tutorial oficial do PyTorch sobre Modelagem de Linguagem](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial do TensorFlow sobre treinamento do modelo Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* O uso do framework **gensim** para treinar os embeddings mais comumente usados em poucas linhas de código é descrito [nesta documentação](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tarefa: Treinar Modelo Skip-Gram](lab/README.md)

No laboratório, desafiamos você a modificar o código desta lição para treinar um modelo skip-gram em vez de CBoW. [Leia os detalhes](lab/README.md)

---

