<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T08:54:47+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "pt"
}
-->
# Modelação de Linguagem

Embeddings semânticos, como Word2Vec e GloVe, são, na verdade, um primeiro passo em direção à **modelação de linguagem** - criar modelos que de alguma forma *compreendem* (ou *representam*) a natureza da linguagem.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

A ideia principal por trás da modelação de linguagem é treiná-los em conjuntos de dados não rotulados de forma não supervisionada. Isto é importante porque temos grandes quantidades de texto não rotulado disponível, enquanto a quantidade de texto rotulado estará sempre limitada pelo esforço necessário para rotulá-lo. Na maioria das vezes, podemos construir modelos de linguagem que conseguem **prever palavras em falta** no texto, porque é fácil ocultar uma palavra aleatória no texto e usá-la como amostra de treino.

## Treinar Embeddings

Nos nossos exemplos anteriores, utilizámos embeddings semânticos pré-treinados, mas é interessante ver como esses embeddings podem ser treinados. Existem várias ideias possíveis que podem ser utilizadas:

* **Modelação de linguagem N-Gram**, onde prevemos um token olhando para os N tokens anteriores (N-grama).
* **Continuous Bag-of-Words** (CBoW), onde prevemos o token central $W_0$ numa sequência de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, onde prevemos um conjunto de tokens vizinhos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partir do token central $W_0$.

![imagem do artigo sobre conversão de palavras em vetores](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Imagem retirada [deste artigo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks de Exemplo: Treinar modelo CBoW

Continue a sua aprendizagem nos seguintes notebooks:

* [Treinar CBoW Word2Vec com TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Treinar CBoW Word2Vec com PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusão

Na lição anterior vimos que os embeddings de palavras funcionam como magia! Agora sabemos que treinar embeddings de palavras não é uma tarefa muito complexa, e devemos ser capazes de treinar os nossos próprios embeddings para texto específico de domínio, se necessário.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Revisão & Estudo Autónomo

* [Tutorial oficial do PyTorch sobre Modelação de Linguagem](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial do TensorFlow sobre treino de modelo Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Utilizar o framework **gensim** para treinar os embeddings mais comuns em poucas linhas de código é descrito [nesta documentação](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tarefa: Treinar Modelo Skip-Gram](lab/README.md)

No laboratório, desafiamos-lhe a modificar o código desta lição para treinar um modelo skip-gram em vez de CBoW. [Leia os detalhes](lab/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.