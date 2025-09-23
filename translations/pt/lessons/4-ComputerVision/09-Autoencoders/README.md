<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-24T08:57:36+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "pt"
}
-->
# Autoencoders

Ao treinar CNNs, um dos problemas é que precisamos de muitos dados rotulados. No caso da classificação de imagens, é necessário separar as imagens em diferentes classes, o que exige um esforço manual.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

No entanto, podemos querer usar dados brutos (não rotulados) para treinar extratores de características de CNN, o que é chamado de **aprendizagem auto-supervisionada**. Em vez de rótulos, usaremos as imagens de treino como entrada e saída da rede. A ideia principal do **autoencoder** é que teremos uma **rede codificadora** que converte a imagem de entrada em algum **espaço latente** (normalmente é apenas um vetor de tamanho reduzido), e uma **rede decodificadora**, cujo objetivo será reconstruir a imagem original.

> ✅ Um [autoencoder](https://wikipedia.org/wiki/Autoencoder) é "um tipo de rede neural artificial usada para aprender codificações eficientes de dados não rotulados."

Como estamos a treinar um autoencoder para capturar o máximo de informação possível da imagem original para uma reconstrução precisa, a rede tenta encontrar a melhor **representação** das imagens de entrada para capturar o seu significado.

![Diagrama do Autoencoder](../../../../../lessons/4-ComputerVision/09-Autoencoders/images/autoencoder_schema.jpg)

> Imagem do [blog Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Cenários para usar Autoencoders

Embora reconstruir imagens originais possa não parecer útil por si só, existem alguns cenários em que os autoencoders são especialmente úteis:

* **Reduzir a dimensão das imagens para visualização** ou **treinar representações de imagens**. Normalmente, os autoencoders oferecem melhores resultados do que PCA, porque levam em consideração a natureza espacial das imagens e as características hierárquicas.
* **Remoção de ruído**, ou seja, eliminar o ruído da imagem. Como o ruído contém muita informação inútil, o autoencoder não consegue encaixar tudo no espaço latente relativamente pequeno e, assim, captura apenas a parte importante da imagem. Ao treinar removedores de ruído, começamos com imagens originais e usamos imagens com ruído artificialmente adicionado como entrada para o autoencoder.
* **Super-resolução**, aumentar a resolução da imagem. Começamos com imagens de alta resolução e usamos a imagem com resolução mais baixa como entrada do autoencoder.
* **Modelos generativos**. Depois de treinar o autoencoder, a parte decodificadora pode ser usada para criar novos objetos a partir de vetores latentes aleatórios.

## Autoencoders Variacionais (VAE)

Os autoencoders tradicionais reduzem a dimensão dos dados de entrada de alguma forma, identificando as características importantes das imagens de entrada. No entanto, os vetores latentes muitas vezes não fazem muito sentido. Por outras palavras, usando o conjunto de dados MNIST como exemplo, identificar quais dígitos correspondem a diferentes vetores latentes não é uma tarefa fácil, porque vetores latentes próximos não correspondem necessariamente aos mesmos dígitos.

Por outro lado, para treinar modelos *generativos*, é melhor ter algum entendimento do espaço latente. Esta ideia leva-nos ao **autoencoder variacional** (VAE).

O VAE é um autoencoder que aprende a prever a *distribuição estatística* dos parâmetros latentes, chamada de **distribuição latente**. Por exemplo, podemos querer que os vetores latentes sejam distribuídos normalmente com uma média z<sub>mean</sub> e desvio padrão z<sub>sigma</sub> (tanto a média quanto o desvio padrão são vetores de alguma dimensionalidade d). O codificador no VAE aprende a prever esses parâmetros, e o decodificador utiliza um vetor aleatório dessa distribuição para reconstruir o objeto.

Resumindo:

 * A partir do vetor de entrada, prevemos `z_mean` e `z_log_sigma` (em vez de prever o desvio padrão diretamente, prevemos o seu logaritmo)
 * Amostramos um vetor `sample` da distribuição N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * O decodificador tenta decodificar a imagem original usando `sample` como vetor de entrada

 <img src="images/vae.png" width="50%">

> Imagem deste [post no blog](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) por Isaak Dykeman

Os autoencoders variacionais utilizam uma função de perda complexa que consiste em duas partes:

* **Perda de reconstrução**, que é a função de perda que mostra quão próxima a imagem reconstruída está do alvo (pode ser o Erro Quadrático Médio, ou MSE). É a mesma função de perda usada em autoencoders normais.
* **Perda KL**, que garante que as distribuições das variáveis latentes permaneçam próximas da distribuição normal. Baseia-se no conceito de [divergência de Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - uma métrica para estimar quão semelhantes são duas distribuições estatísticas.

Uma vantagem importante dos VAEs é que permitem gerar novas imagens de forma relativamente fácil, porque sabemos de qual distribuição amostrar os vetores latentes. Por exemplo, se treinarmos um VAE com vetor latente 2D no MNIST, podemos variar os componentes do vetor latente para obter diferentes dígitos:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Observe como as imagens se misturam umas com as outras, à medida que começamos a obter vetores latentes de diferentes partes do espaço de parâmetros latentes. Também podemos visualizar este espaço em 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exercícios: Autoencoders

Aprenda mais sobre autoencoders nestes notebooks correspondentes:

* [Autoencoders em TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders em PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Propriedades dos Autoencoders

* **Específicos para os dados** - funcionam bem apenas com o tipo de imagens em que foram treinados. Por exemplo, se treinarmos uma rede de super-resolução em flores, ela não funcionará bem em retratos. Isso ocorre porque a rede pode produzir imagens de maior resolução ao usar detalhes finos aprendidos a partir do conjunto de dados de treino.
* **Com perdas** - a imagem reconstruída não é exatamente igual à imagem original. A natureza da perda é definida pela *função de perda* usada durante o treino.
* Funciona com **dados não rotulados**

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Conclusão

Nesta lição, aprendeu sobre os vários tipos de autoencoders disponíveis para o cientista de IA. Aprendeu como construí-los e como usá-los para reconstruir imagens. Também aprendeu sobre o VAE e como usá-lo para gerar novas imagens.

## 🚀 Desafio

Nesta lição, aprendeu a usar autoencoders para imagens. Mas eles também podem ser usados para música! Explore o projeto [MusicVAE](https://magenta.tensorflow.org/music-vae) do Magenta, que utiliza autoencoders para aprender a reconstruir música. Faça alguns [experimentos](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) com esta biblioteca para ver o que consegue criar.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Revisão e Autoestudo

Para referência, leia mais sobre autoencoders nestes recursos:

* [Construindo Autoencoders em Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Post no blog NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencoders Variacionais Explicados](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencoders Variacionais Condicionais](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tarefa

No final deste [notebook usando TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), encontrará uma 'tarefa' - use-a como sua tarefa.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.