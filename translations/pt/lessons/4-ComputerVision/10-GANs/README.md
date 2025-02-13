# Redes Adversariais Generativas

Na seção anterior, aprendemos sobre **modelos geradores**: modelos que podem gerar novas imagens semelhantes às do conjunto de dados de treinamento. O VAE foi um bom exemplo de um modelo gerador.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

No entanto, se tentarmos gerar algo realmente significativo, como uma pintura em uma resolução razoável, com o VAE, veremos que o treinamento não converge bem. Para esse caso de uso, devemos aprender sobre outra arquitetura especificamente direcionada a modelos geradores - **Redes Adversariais Generativas**, ou GANs.

A ideia principal de uma GAN é ter duas redes neurais que serão treinadas uma contra a outra:

<img src="images/gan_architecture.png" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Um pequeno vocabulário:
> * **Gerador** é uma rede que recebe um vetor aleatório e produz a imagem como resultado.
> * **Discriminador** é uma rede que recebe uma imagem e deve dizer se é uma imagem real (do conjunto de dados de treinamento) ou se foi gerada por um gerador. É essencialmente um classificador de imagens.

### Discriminador

A arquitetura do discriminador não difere de uma rede de classificação de imagens comum. No caso mais simples, pode ser um classificador totalmente conectado, mas provavelmente será uma [rede convolucional](../07-ConvNets/README.md).

> ✅ Uma GAN baseada em redes convolucionais é chamada de [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Um discriminador CNN consiste nas seguintes camadas: várias convoluções + pooling (com tamanho espacial decrescente) e uma ou mais camadas totalmente conectadas para obter o "vetor de características", classificador binário final.

> ✅ Um 'pooling' neste contexto é uma técnica que reduz o tamanho da imagem. "Camadas de pooling reduzem as dimensões dos dados combinando as saídas de grupos de neurônios em uma camada em um único neurônio na próxima camada." - [fonte](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Gerador

Um Gerador é um pouco mais complicado. Você pode considerá-lo como um discriminador invertido. Começando de um vetor latente (no lugar de um vetor de características), ele tem uma camada totalmente conectada para convertê-lo no tamanho/formato necessário, seguida de deconvoluções + aumento de escala. Isso é semelhante à parte *decodificadora* de um [autoencoder](../09-Autoencoders/README.md).

> ✅ Como a camada de convolução é implementada como um filtro linear que percorre a imagem, a deconvolução é essencialmente semelhante à convolução e pode ser implementada usando a mesma lógica de camada.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

### Treinando a GAN

As GANs são chamadas de **adversariais** porque há uma competição constante entre o gerador e o discriminador. Durante essa competição, tanto o gerador quanto o discriminador melhoram, assim a rede aprende a produzir imagens cada vez melhores.

O treinamento acontece em duas etapas:

* **Treinando o discriminador**. Esta tarefa é bastante direta: geramos um lote de imagens pelo gerador, rotulando-as como 0, que representa imagem falsa, e pegamos um lote de imagens do conjunto de dados de entrada (com rótulo 1, imagem real). Obtemos uma *perda do discriminador* e realizamos a retropropagação.
* **Treinando o gerador**. Isso é um pouco mais complicado, porque não sabemos a saída esperada para o gerador diretamente. Pegamos toda a rede GAN, consistindo de um gerador seguido de um discriminador, alimentamos com alguns vetores aleatórios e esperamos que o resultado seja 1 (correspondente a imagens reais). Em seguida, congelamos os parâmetros do discriminador (não queremos que ele seja treinado nesta etapa) e realizamos a retropropagação.

Durante esse processo, as perdas do gerador e do discriminador não estão diminuindo significativamente. Na situação ideal, elas devem oscilar, correspondendo a ambas as redes melhorando seu desempenho.

## ✍️ Exercícios: GANs

* [Notebook GAN em TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook GAN em PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problemas com o treinamento de GAN

As GANs são conhecidas por serem especialmente difíceis de treinar. Aqui estão alguns problemas:

* **Colapso de Modo**. Por esse termo, queremos dizer que o gerador aprende a produzir uma imagem bem-sucedida que engana o discriminador, e não uma variedade de imagens diferentes.
* **Sensibilidade a hiperparâmetros**. Muitas vezes você pode ver que uma GAN não converge de forma alguma e, em seguida, de repente diminui na taxa de aprendizado levando à convergência.
* Manter um **equilíbrio** entre o gerador e o discriminador. Em muitos casos, a perda do discriminador pode cair para zero relativamente rápido, o que resulta na incapacidade do gerador de treinar mais. Para superar isso, podemos tentar definir diferentes taxas de aprendizado para o gerador e o discriminador, ou pular o treinamento do discriminador se a perda já estiver muito baixa.
* Treinamento para **alta resolução**. Refletindo o mesmo problema que com autoencoders, esse problema é desencadeado porque reconstruir muitas camadas de uma rede convolucional leva a artefatos. Esse problema é tipicamente resolvido com o chamado **crescimento progressivo**, quando primeiro algumas camadas são treinadas em imagens de baixa resolução e, em seguida, as camadas são "desbloqueadas" ou adicionadas. Outra solução seria adicionar conexões extras entre camadas e treinar várias resoluções ao mesmo tempo - veja este [artigo sobre GANs de Gradiente Multi-Escala](https://arxiv.org/abs/1903.06048) para detalhes.

## Transferência de Estilo

As GANs são uma ótima maneira de gerar imagens artísticas. Outra técnica interessante é a chamada **transferência de estilo**, que pega uma **imagem de conteúdo** e a redesenha em um estilo diferente, aplicando filtros da **imagem de estilo**.

A maneira como isso funciona é a seguinte:
* Começamos com uma imagem de ruído aleatório (ou com uma imagem de conteúdo, mas para fins de compreensão é mais fácil começar a partir do ruído aleatório).
* Nosso objetivo seria criar uma imagem que estivesse próxima tanto da imagem de conteúdo quanto da imagem de estilo. Isso seria determinado por duas funções de perda:
   - **Perda de conteúdo** é calculada com base nas características extraídas pela CNN em algumas camadas da imagem atual e da imagem de conteúdo.
   - **Perda de estilo** é calculada entre a imagem atual e a imagem de estilo de uma maneira inteligente usando matrizes de Gram (mais detalhes no [notebook de exemplo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Para tornar a imagem mais suave e remover o ruído, também introduzimos a **Perda de Variedade**, que calcula a distância média entre pixels vizinhos.
* O loop principal de otimização ajusta a imagem atual usando descida de gradiente (ou algum outro algoritmo de otimização) para minimizar a perda total, que é uma soma ponderada de todas as três perdas.

## ✍️ Exemplo: [Transferência de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusão

Nesta lição, você aprendeu sobre GANs e como treiná-las. Você também aprendeu sobre os desafios especiais que esse tipo de Rede Neural pode enfrentar e algumas estratégias sobre como superá-los.

## 🚀 Desafio

Execute o [notebook de Transferência de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) usando suas próprias imagens.

## Revisão & Estudo Autônomo

Para referência, leia mais sobre GANs nestes recursos:

* Marco Pasini, [10 Lições que Aprendi Treinando GANs por um Ano](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), uma arquitetura GAN *de fato* a considerar
* [Criando Arte Generativa usando GANs no Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tarefa

Revisite um dos dois notebooks associados a esta lição e re-treine a GAN com suas próprias imagens. O que você pode criar?

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.