# Redes Adversárias Generativas

Na secção anterior, aprendemos sobre **modelos generativos**: modelos que podem gerar novas imagens semelhantes às do conjunto de dados de treino. O VAE foi um bom exemplo de modelo generativo.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/19)

No entanto, se tentarmos gerar algo realmente significativo, como uma pintura com resolução razoável, usando o VAE, veremos que o treino não converge bem. Para este caso, devemos aprender sobre outra arquitetura especificamente direcionada para modelos generativos - **Redes Adversárias Generativas**, ou GANs.

A ideia principal de uma GAN é ter duas redes neuronais que serão treinadas uma contra a outra:

<img src="../../../../../translated_images/pt-PT/gan_architecture.8f3a5ab62b8d5d69.webp" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Um pouco de vocabulário:
> * **Gerador** é uma rede que recebe um vetor aleatório e produz uma imagem como resultado.
> * **Discriminador** é uma rede que recebe uma imagem e deve dizer se é uma imagem real (do conjunto de dados de treino) ou se foi gerada por um gerador. Essencialmente, é um classificador de imagens.

### Discriminador

A arquitetura do discriminador não difere de uma rede de classificação de imagens comum. No caso mais simples, pode ser um classificador totalmente conectado, mas provavelmente será uma [rede convolucional](../07-ConvNets/README.md).

> ✅ Uma GAN baseada em redes convolucionais é chamada de [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Um discriminador CNN consiste nas seguintes camadas: várias convoluções+poolings (com tamanho espacial decrescente) e uma ou mais camadas totalmente conectadas para obter o "vetor de características", classificador binário final.

> ✅ Um 'pooling' neste contexto é uma técnica que reduz o tamanho da imagem. "As camadas de pooling reduzem as dimensões dos dados ao combinar os resultados de clusters de neurónios numa camada em um único neurónio na próxima camada." - [fonte](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Gerador

Um Gerador é um pouco mais complicado. Pode ser considerado como um discriminador invertido. Começando por um vetor latente (em vez de um vetor de características), tem uma camada totalmente conectada para convertê-lo no tamanho/forma necessária, seguida por deconvoluções+ampliação. Isto é semelhante à parte de *decodificador* de um [autoencoder](../09-Autoencoders/README.md).

> ✅ Como a camada de convolução é implementada como um filtro linear que percorre a imagem, a deconvolução é essencialmente semelhante à convolução e pode ser implementada usando a mesma lógica de camada.

<img src="../../../../../translated_images/pt-PT/gan_arch_detail.46b95fd366f8e543.webp" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

### Treino da GAN

As GANs são chamadas de **adversárias** porque há uma competição constante entre o gerador e o discriminador. Durante esta competição, tanto o gerador quanto o discriminador melhoram, e assim a rede aprende a produzir imagens cada vez melhores.

O treino ocorre em duas etapas:

* **Treino do discriminador**. Esta tarefa é bastante direta: geramos um lote de imagens com o gerador, rotulando-as como 0, que representa imagem falsa, e pegamos um lote de imagens do conjunto de dados de entrada (com rótulo 1, imagem real). Obtemos uma *perda do discriminador* e realizamos o backprop.
* **Treino do gerador**. Isto é um pouco mais complicado, porque não sabemos diretamente o resultado esperado para o gerador. Pegamos toda a rede GAN, consistindo de um gerador seguido por um discriminador, alimentamo-la com alguns vetores aleatórios e esperamos que o resultado seja 1 (correspondente a imagens reais). Em seguida, congelamos os parâmetros do discriminador (não queremos que ele seja treinado nesta etapa) e realizamos o backprop.

Durante este processo, as perdas do gerador e do discriminador não diminuem significativamente. Na situação ideal, elas devem oscilar, correspondendo a ambos os modelos a melhorar o desempenho.

## ✍️ Exercícios: GANs

* [Notebook GAN em TensorFlow/Keras](GANTF.ipynb)
* [Notebook GAN em PyTorch](GANPyTorch.ipynb)

### Problemas no treino de GANs

As GANs são conhecidas por serem especialmente difíceis de treinar. Aqui estão alguns problemas:

* **Colapso de modo**. Este termo refere-se ao fato de o gerador aprender a produzir uma única imagem bem-sucedida que engana o discriminador, em vez de uma variedade de imagens diferentes.
* **Sensibilidade aos hiperparâmetros**. Muitas vezes, pode-se observar que uma GAN não converge de forma alguma, e então, de repente, uma diminuição na taxa de aprendizagem leva à convergência.
* Manter um **equilíbrio** entre o gerador e o discriminador. Em muitos casos, a perda do discriminador pode cair para zero relativamente rápido, o que resulta no gerador incapaz de continuar o treino. Para superar isso, podemos tentar definir taxas de aprendizagem diferentes para o gerador e o discriminador ou ignorar o treino do discriminador se a perda já for muito baixa.
* Treino para **alta resolução**. Refletindo o mesmo problema dos autoencoders, este problema é desencadeado porque reconstruir muitas camadas de uma rede convolucional leva a artefactos. Este problema é geralmente resolvido com o chamado **crescimento progressivo**, onde primeiro algumas camadas são treinadas em imagens de baixa resolução e, em seguida, as camadas são "desbloqueadas" ou adicionadas. Outra solução seria adicionar conexões extras entre camadas e treinar várias resoluções ao mesmo tempo - veja este artigo [Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) para mais detalhes.

## Transferência de Estilo

As GANs são uma ótima maneira de gerar imagens artísticas. Outra técnica interessante é a chamada **transferência de estilo**, que pega uma **imagem de conteúdo** e redesenha-a num estilo diferente, aplicando filtros de uma **imagem de estilo**.

O funcionamento é o seguinte:
* Começamos com uma imagem de ruído aleatório (ou com uma imagem de conteúdo, mas para fins de compreensão é mais fácil começar com ruído aleatório).
* O nosso objetivo será criar uma imagem que seja próxima tanto da imagem de conteúdo quanto da imagem de estilo. Isto será determinado por duas funções de perda:
   - **Perda de conteúdo** é calculada com base nas características extraídas pela CNN em algumas camadas da imagem atual e da imagem de conteúdo.
   - **Perda de estilo** é calculada entre a imagem atual e a imagem de estilo de uma forma inteligente usando matrizes de Gram (mais detalhes no [notebook de exemplo](StyleTransfer.ipynb)).
* Para tornar a imagem mais suave e remover o ruído, também introduzimos a **Perda de variação**, que calcula a distância média entre pixels vizinhos.
* O principal ciclo de otimização ajusta a imagem atual usando descida de gradiente (ou algum outro algoritmo de otimização) para minimizar a perda total, que é uma soma ponderada de todas as três perdas.

## ✍️ Exemplo: [Transferência de Estilo](StyleTransfer.ipynb)

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Conclusão

Nesta lição, aprendeste sobre GANs e como treiná-las. Também aprendeste sobre os desafios especiais que este tipo de rede neuronal pode enfrentar e algumas estratégias para superá-los.

## 🚀 Desafio

Experimenta o [notebook de Transferência de Estilo](StyleTransfer.ipynb) usando as tuas próprias imagens.

## Revisão e Autoestudo

Para referência, lê mais sobre GANs nestes recursos:

* Marco Pasini, [10 Lições que Aprendi ao Treinar GANs por um Ano](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), uma arquitetura GAN *de facto* a considerar
* [Criando Arte Generativa usando GANs no Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tarefa

Revisita um dos dois notebooks associados a esta lição e treina novamente a GAN com as tuas próprias imagens. O que consegues criar?

---

