<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-24T08:58:33+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "pt"
}
-->
# Redes Generativas Adversárias

Na seção anterior, aprendemos sobre **modelos generativos**: modelos que podem gerar novas imagens semelhantes às do conjunto de dados de treino. O VAE foi um bom exemplo de modelo generativo.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

No entanto, se tentarmos gerar algo realmente significativo, como uma pintura com resolução razoável, usando o VAE, veremos que o treino não converge bem. Para este caso, devemos aprender sobre outra arquitetura especificamente voltada para modelos generativos - **Redes Generativas Adversárias**, ou GANs.

A ideia principal de uma GAN é ter duas redes neurais que serão treinadas uma contra a outra:

<img src="images/gan_architecture.png" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Um pouco de vocabulário:
> * **Gerador** é uma rede que recebe um vetor aleatório e produz uma imagem como resultado.
> * **Discriminador** é uma rede que recebe uma imagem e deve dizer se é uma imagem real (do conjunto de dados de treino) ou se foi gerada por um gerador. Essencialmente, é um classificador de imagens.

### Discriminador

A arquitetura do discriminador não difere de uma rede de classificação de imagens comum. No caso mais simples, pode ser um classificador totalmente conectado, mas, muito provavelmente, será uma [rede convolucional](../07-ConvNets/README.md).

> ✅ Uma GAN baseada em redes convolucionais é chamada de [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Um discriminador CNN consiste nas seguintes camadas: várias convoluções+poolings (com tamanho espacial decrescente) e uma ou mais camadas totalmente conectadas para obter o "vetor de características", seguido de um classificador binário final.

> ✅ Um 'pooling' neste contexto é uma técnica que reduz o tamanho da imagem. "As camadas de pooling reduzem as dimensões dos dados combinando as saídas de clusters de neurónios em uma camada em um único neurónio na próxima camada." - [fonte](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Gerador

Um Gerador é um pouco mais complicado. Pode ser considerado como um discriminador invertido. Começando por um vetor latente (no lugar de um vetor de características), ele possui uma camada totalmente conectada para convertê-lo no tamanho/forma desejados, seguida por deconvoluções+ampliação. Isso é semelhante à parte de *decodificador* de um [autoencoder](../09-Autoencoders/README.md).

> ✅ Como a camada de convolução é implementada como um filtro linear que percorre a imagem, a deconvolução é essencialmente semelhante à convolução e pode ser implementada usando a mesma lógica de camada.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

### Treinando a GAN

As GANs são chamadas de **adversárias** porque há uma competição constante entre o gerador e o discriminador. Durante essa competição, tanto o gerador quanto o discriminador melhoram, fazendo com que a rede aprenda a produzir imagens cada vez melhores.

O treino ocorre em duas etapas:

* **Treinando o discriminador**. Esta tarefa é bastante direta: geramos um lote de imagens com o gerador, rotulando-as como 0, que representa imagem falsa, e pegamos um lote de imagens do conjunto de dados de entrada (com rótulo 1, imagem real). Obtemos uma *perda do discriminador* e realizamos o backpropagation.
* **Treinando o gerador**. Isto é um pouco mais complicado, porque não sabemos diretamente o resultado esperado para o gerador. Pegamos toda a rede GAN, composta por um gerador seguido de um discriminador, alimentamos com alguns vetores aleatórios e esperamos que o resultado seja 1 (correspondente a imagens reais). Em seguida, congelamos os parâmetros do discriminador (não queremos que ele seja treinado nesta etapa) e realizamos o backpropagation.

Durante este processo, as perdas do gerador e do discriminador não diminuem significativamente. Na situação ideal, elas devem oscilar, correspondendo à melhoria de desempenho de ambas as redes.

## ✍️ Exercícios: GANs

* [Notebook GAN em TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook GAN em PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problemas no treino de GANs

As GANs são conhecidas por serem especialmente difíceis de treinar. Aqui estão alguns problemas:

* **Colapso de modo**. Este termo refere-se ao fato de que o gerador aprende a produzir uma única imagem bem-sucedida que engana o discriminador, em vez de uma variedade de imagens diferentes.
* **Sensibilidade aos hiperparâmetros**. Muitas vezes, pode-se observar que uma GAN não converge de forma alguma e, de repente, uma redução na taxa de aprendizagem leva à convergência.
* Manter um **equilíbrio** entre o gerador e o discriminador. Em muitos casos, a perda do discriminador pode cair para zero relativamente rápido, o que resulta no gerador sendo incapaz de continuar o treino. Para superar isso, podemos tentar definir taxas de aprendizagem diferentes para o gerador e o discriminador ou pular o treino do discriminador se a perda já estiver muito baixa.
* Treino para **alta resolução**. Refletindo o mesmo problema dos autoencoders, este problema ocorre porque reconstruir muitas camadas de uma rede convolucional leva a artefatos. Este problema é geralmente resolvido com o chamado **crescimento progressivo**, onde primeiro algumas camadas são treinadas em imagens de baixa resolução e, em seguida, as camadas são "desbloqueadas" ou adicionadas. Outra solução seria adicionar conexões extras entre camadas e treinar várias resoluções ao mesmo tempo - veja este [artigo sobre Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) para mais detalhes.

## Transferência de Estilo

As GANs são uma ótima maneira de gerar imagens artísticas. Outra técnica interessante é a chamada **transferência de estilo**, que pega uma **imagem de conteúdo** e a redesenha em um estilo diferente, aplicando filtros de uma **imagem de estilo**.

O funcionamento é o seguinte:
* Começamos com uma imagem de ruído aleatório (ou com uma imagem de conteúdo, mas para fins de compreensão é mais fácil começar com ruído aleatório).
* Nosso objetivo será criar uma imagem que seja próxima tanto da imagem de conteúdo quanto da imagem de estilo. Isso será determinado por duas funções de perda:
   - **Perda de conteúdo** é calculada com base nas características extraídas pela CNN em algumas camadas da imagem atual e da imagem de conteúdo.
   - **Perda de estilo** é calculada entre a imagem atual e a imagem de estilo de uma maneira inteligente usando matrizes de Gram (mais detalhes no [notebook de exemplo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Para tornar a imagem mais suave e remover ruídos, também introduzimos a **Perda de variação**, que calcula a distância média entre pixels vizinhos.
* O principal loop de otimização ajusta a imagem atual usando descida de gradiente (ou algum outro algoritmo de otimização) para minimizar a perda total, que é uma soma ponderada de todas as três perdas.

## ✍️ Exemplo: [Transferência de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Conclusão

Nesta lição, você aprendeu sobre GANs e como treiná-las. Também aprendeu sobre os desafios especiais que este tipo de rede neural pode enfrentar e algumas estratégias para superá-los.

## 🚀 Desafio

Execute o [notebook de Transferência de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) usando suas próprias imagens.

## Revisão e Estudo Individual

Para referência, leia mais sobre GANs nestes recursos:

* Marco Pasini, [10 Lições que Aprendi Treinando GANs por um Ano](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), uma arquitetura GAN *de facto* a considerar.
* [Criando Arte Generativa usando GANs no Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tarefa

Revise um dos dois notebooks associados a esta lição e treine novamente a GAN com suas próprias imagens. O que você consegue criar?

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.