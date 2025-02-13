# Autoencoders

Ao treinar CNNs, um dos problemas é que precisamos de muitos dados rotulados. No caso da classificação de imagens, precisamos separar as imagens em diferentes classes, o que é um esforço manual.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

No entanto, podemos querer usar dados brutos (não rotulados) para treinar extratores de características CNN, o que é chamado de **aprendizado auto-supervisionado**. Em vez de rótulos, usaremos imagens de treinamento como entrada e saída da rede. A ideia principal do **autoencoder** é que teremos uma **rede de codificação** que converte a imagem de entrada em algum **espaço latente** (normalmente é apenas um vetor de um tamanho menor), e então a **rede de decodificação**, cujo objetivo seria reconstruir a imagem original.

> ✅ Um [autoencoder](https://wikipedia.org/wiki/Autoencoder) é "um tipo de rede neural artificial usada para aprender codificações eficientes de dados não rotulados."

Como estamos treinando um autoencoder para capturar o máximo de informações da imagem original possível para uma reconstrução precisa, a rede tenta encontrar a melhor **incorporação** das imagens de entrada para capturar o significado.

![Diagrama do AutoEncoder](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.pt.jpg)

> Imagem do [blog Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Cenários para usar Autoencoders

Embora reconstruir imagens originais não pareça útil por si só, existem alguns cenários onde os autoencoders são especialmente úteis:

* **Redução da dimensão das imagens para visualização** ou **treinamento de incorporações de imagem**. Normalmente, os autoencoders apresentam resultados melhores do que PCA, pois levam em consideração a natureza espacial das imagens e características hierárquicas.
* **Remoção de ruído**, ou seja, eliminar ruído da imagem. Como o ruído carrega muitas informações inúteis, o autoencoder não consegue ajustá-lo todo em um espaço latente relativamente pequeno e, assim, captura apenas a parte importante da imagem. Ao treinar denoisers, começamos com imagens originais e usamos imagens com ruído adicionado artificialmente como entrada para o autoencoder.
* **Super-resolução**, aumentando a resolução da imagem. Começamos com imagens de alta resolução e usamos a imagem de baixa resolução como entrada do autoencoder.
* **Modelos generativos**. Uma vez que treinamos o autoencoder, a parte do decodificador pode ser usada para criar novos objetos a partir de vetores latentes aleatórios.

## Autoencoders Variacionais (VAE)

Autoencoders tradicionais reduzem a dimensão dos dados de entrada de alguma forma, identificando as características importantes das imagens de entrada. No entanto, vetores latentes muitas vezes não fazem muito sentido. Em outras palavras, tomando o conjunto de dados MNIST como exemplo, descobrir quais dígitos correspondem a diferentes vetores latentes não é uma tarefa fácil, porque vetores latentes próximos não necessariamente correspondem aos mesmos dígitos.

Por outro lado, para treinar modelos *generativos*, é melhor ter algum entendimento do espaço latente. Essa ideia nos leva ao **autoencoder variacional** (VAE).

VAE é o autoencoder que aprende a prever a *distribuição estatística* dos parâmetros latentes, chamada de **distribuição latente**. Por exemplo, podemos querer que os vetores latentes sejam distribuídos normalmente com uma média z<sub>mean</sub> e desvio padrão z<sub>sigma</sub> (tanto a média quanto o desvio padrão são vetores de alguma dimensionalidade d). O codificador no VAE aprende a prever esses parâmetros, e então o decodificador pega um vetor aleatório dessa distribuição para reconstruir o objeto.

Para resumir:

 * A partir do vetor de entrada, prevemos `z_mean` e `z_log_sigma` (em vez de prever o desvio padrão em si, prevemos seu logaritmo)
 * Amostramos um vetor `sample` da distribuição N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * O decodificador tenta decodificar a imagem original usando `sample` como vetor de entrada

 <img src="images/vae.png" width="50%">

> Imagem do [este post no blog](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) de Isaak Dykeman

Autoencoders variacionais usam uma função de perda complexa que consiste em duas partes:

* **Perda de reconstrução** é a função de perda que mostra quão próxima uma imagem reconstruída está do alvo (pode ser o Erro Quadrático Médio, ou MSE). É a mesma função de perda que em autoencoders normais.
* **Perda KL**, que garante que as distribuições das variáveis latentes permaneçam próximas à distribuição normal. É baseada na noção de [divergência de Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - uma métrica para estimar quão semelhantes são duas distribuições estatísticas.

Uma vantagem importante dos VAEs é que eles nos permitem gerar novas imagens relativamente facilmente, porque sabemos de qual distribuição amostrar vetores latentes. Por exemplo, se treinarmos um VAE com vetor latente 2D no MNIST, podemos então variar os componentes do vetor latente para obter diferentes dígitos:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imagem de [Dmitry Soshnikov](http://soshnikov.com)

Observe como as imagens se misturam umas às outras, à medida que começamos a obter vetores latentes de diferentes porções do espaço de parâmetros latentes. Também podemos visualizar esse espaço em 2D:

<img alt="cluster vaemnist" src="images/vaemnist-diag.png" width="50%"/> 

> Imagem de [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exercícios: Autoencoders

Saiba mais sobre autoencoders nestes cadernos correspondentes:

* [Autoencoders em TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders em PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Propriedades dos Autoencoders

* **Específico para dados** - eles funcionam bem apenas com o tipo de imagens para as quais foram treinados. Por exemplo, se treinarmos uma rede de super-resolução em flores, ela não funcionará bem em retratos. Isso ocorre porque a rede pode produzir uma imagem de maior resolução ao captar detalhes finos das características aprendidas a partir do conjunto de dados de treinamento.
* **Com perdas** - a imagem reconstruída não é a mesma que a imagem original. A natureza da perda é definida pela *função de perda* usada durante o treinamento.
* Funciona com **dados não rotulados**.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Conclusão

Nesta lição, você aprendeu sobre os vários tipos de autoencoders disponíveis para o cientista de IA. Você aprendeu como construí-los e como usá-los para reconstruir imagens. Você também aprendeu sobre o VAE e como usá-lo para gerar novas imagens.

## 🚀 Desafio

Nesta lição, você aprendeu sobre o uso de autoencoders para imagens. Mas eles também podem ser usados para música! Confira o projeto [MusicVAE](https://magenta.tensorflow.org/music-vae) do projeto Magenta, que usa autoencoders para aprender a reconstruir música. Faça alguns [experimentos](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) com esta biblioteca para ver o que você pode criar.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisão & Autoestudo

Para referência, leia mais sobre autoencoders nestes recursos:

* [Construindo Autoencoders em Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Post no blog sobre NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencoders Variacionais Explicados](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencoders Variacionais Condicionais](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tarefa

No final de [este caderno usando TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), você encontrará uma 'tarefa' - use isso como sua tarefa.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.