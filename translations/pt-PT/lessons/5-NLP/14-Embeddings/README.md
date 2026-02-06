# Embeddings

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Ao treinar classificadores baseados em BoW ou TF/IDF, trabalhávamos com vetores de bag-of-words de alta dimensão com comprimento `vocab_size`, e estávamos a converter explicitamente de vetores de representação posicional de baixa dimensão para uma representação esparsa de one-hot. No entanto, esta representação one-hot não é eficiente em termos de memória. Além disso, cada palavra é tratada de forma independente, ou seja, os vetores codificados em one-hot não expressam qualquer semelhança semântica entre palavras.

A ideia de **embedding** é representar palavras por vetores densos de menor dimensão, que de alguma forma refletem o significado semântico de uma palavra. Mais tarde, discutiremos como construir embeddings de palavras significativos, mas por agora vamos apenas pensar nos embeddings como uma forma de reduzir a dimensionalidade de um vetor de palavras.

Assim, a camada de embedding receberia uma palavra como entrada e produziria um vetor de saída com o tamanho especificado `embedding_size`. De certa forma, é muito semelhante a uma camada `Linear`, mas em vez de receber um vetor codificado em one-hot, será capaz de receber um número de palavra como entrada, permitindo-nos evitar a criação de grandes vetores codificados em one-hot.

Ao usar uma camada de embedding como a primeira camada na nossa rede de classificação, podemos mudar de um modelo de bag-of-words para um modelo de **embedding bag**, onde primeiro convertemos cada palavra no nosso texto no embedding correspondente e, em seguida, calculamos alguma função agregada sobre todos esses embeddings, como `sum`, `average` ou `max`.  

![Imagem mostrando um classificador de embedding para cinco palavras de sequência.](../../../../../translated_images/pt-PT/embedding-classifier-example.b77f021a7ee67eee.webp)

> Imagem do autor

## ✍️ Exercícios: Embeddings

Continue a sua aprendizagem nos seguintes notebooks:
* [Embeddings com PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings com TensorFlow](EmbeddingsTF.ipynb)

## Embeddings Semânticos: Word2Vec

Embora a camada de embedding tenha aprendido a mapear palavras para representações vetoriais, essa representação não necessariamente possui muito significado semântico. Seria interessante aprender uma representação vetorial tal que palavras semelhantes ou sinónimos correspondam a vetores próximos entre si em termos de alguma distância vetorial (por exemplo, distância Euclidiana).

Para isso, precisamos de pré-treinar o nosso modelo de embedding numa grande coleção de texto de uma forma específica. Uma maneira de treinar embeddings semânticos é chamada [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Baseia-se em duas arquiteturas principais que são usadas para produzir uma representação distribuída de palavras:

 - **Continuous bag-of-words** (CBoW) — nesta arquitetura, treinamos o modelo para prever uma palavra a partir do contexto circundante. Dado o ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, o objetivo do modelo é prever $W_0$ a partir de $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** é o oposto do CBoW. O modelo usa uma janela de palavras de contexto circundantes para prever a palavra atual.

CBoW é mais rápido, enquanto skip-gram é mais lento, mas faz um trabalho melhor ao representar palavras menos frequentes.

![Imagem mostrando os algoritmos CBoW e Skip-Gram para converter palavras em vetores.](../../../../../translated_images/pt-PT/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Imagem retirada [deste artigo](https://arxiv.org/pdf/1301.3781.pdf)

Os embeddings pré-treinados do Word2Vec (bem como outros modelos semelhantes, como GloVe) também podem ser usados no lugar da camada de embedding em redes neurais. No entanto, precisamos de lidar com vocabulários, porque o vocabulário usado para pré-treinar o Word2Vec/GloVe provavelmente será diferente do vocabulário no nosso corpus de texto. Consulte os notebooks acima para ver como este problema pode ser resolvido.

## Embeddings Contextuais

Uma limitação importante das representações tradicionais de embeddings pré-treinados, como Word2Vec, é o problema da desambiguação de sentidos das palavras. Embora os embeddings pré-treinados possam capturar algum significado das palavras no contexto, todos os possíveis significados de uma palavra são codificados no mesmo embedding. Isso pode causar problemas em modelos posteriores, já que muitas palavras, como a palavra 'play', têm significados diferentes dependendo do contexto em que são usadas.

Por exemplo, a palavra 'play' nas duas frases abaixo tem significados bastante diferentes:

- Fui a uma **peça** no teatro.
- O João quer **brincar** com os amigos.

Os embeddings pré-treinados acima representam ambos os significados da palavra 'play' no mesmo embedding. Para superar esta limitação, precisamos de construir embeddings baseados no **modelo de linguagem**, que é treinado num grande corpus de texto e *sabe* como as palavras podem ser combinadas em diferentes contextos. Discutir embeddings contextuais está fora do âmbito deste tutorial, mas voltaremos a eles quando falarmos sobre modelos de linguagem mais adiante no curso.

## Conclusão

Nesta lição, descobriu como construir e usar camadas de embedding no TensorFlow e PyTorch para refletir melhor os significados semânticos das palavras.

## 🚀 Desafio

O Word2Vec tem sido usado em algumas aplicações interessantes, incluindo a geração de letras de músicas e poesia. Veja [este artigo](https://www.politetype.com/blog/word2vec-color-poems), que explica como o autor usou o Word2Vec para gerar poesia. Assista também a [este vídeo de Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) para descobrir uma explicação diferente desta técnica. Depois, tente aplicar estas técnicas ao seu próprio corpus de texto, talvez obtido no Kaggle.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Revisão & Autoestudo

Leia este artigo sobre Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Assignment: Notebooks](assignment.md)

---

