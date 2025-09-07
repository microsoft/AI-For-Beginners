<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-26T09:45:40+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "br"
}
-->
# Redes Pré-treinadas e Aprendizado por Transferência

Treinar redes neurais convolucionais (CNNs) pode levar muito tempo e requer uma grande quantidade de dados. No entanto, grande parte do tempo é gasto aprendendo os melhores filtros de baixo nível que uma rede pode usar para extrair padrões de imagens. Surge então uma pergunta natural: podemos usar uma rede neural treinada em um conjunto de dados e adaptá-la para classificar imagens diferentes sem precisar de um processo completo de treinamento?

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Essa abordagem é chamada de **aprendizado por transferência**, porque transferimos algum conhecimento de um modelo de rede neural para outro. No aprendizado por transferência, geralmente começamos com um modelo pré-treinado, que foi treinado em um grande conjunto de dados de imagens, como o **ImageNet**. Esses modelos já conseguem extrair diferentes características de imagens genéricas, e em muitos casos, apenas construir um classificador em cima dessas características extraídas pode gerar bons resultados.

> ✅ Aprendizado por Transferência é um termo encontrado em outras áreas acadêmicas, como Educação. Ele se refere ao processo de transferir conhecimento de um domínio e aplicá-lo em outro.

## Modelos Pré-treinados como Extratores de Características

As redes convolucionais que discutimos na seção anterior contêm várias camadas, cada uma responsável por extrair características da imagem, começando com combinações de pixels de baixo nível (como linhas horizontais/verticais ou traços), até combinações de características de nível mais alto, correspondendo a coisas como o olho de uma chama. Se treinarmos uma CNN em um conjunto de dados suficientemente grande e diverso, a rede deve aprender a extrair essas características comuns.

Tanto o Keras quanto o PyTorch possuem funções para carregar facilmente pesos de redes neurais pré-treinadas para algumas arquiteturas comuns, a maioria das quais foi treinada em imagens do ImageNet. As mais utilizadas são descritas na página [Arquiteturas de CNN](../07-ConvNets/CNN_Architectures.md) da lição anterior. Em particular, você pode considerar usar uma das seguintes:

* **VGG-16/VGG-19**, que são modelos relativamente simples, mas ainda oferecem boa precisão. Usar o VGG como uma primeira tentativa é uma boa escolha para ver como o aprendizado por transferência funciona.
* **ResNet**, uma família de modelos proposta pela Microsoft Research em 2015. Eles possuem mais camadas e, portanto, exigem mais recursos.
* **MobileNet**, uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Use-os se você tiver poucos recursos e puder sacrificar um pouco de precisão.

Aqui estão exemplos de características extraídas de uma imagem de um gato pela rede VGG-16:

![Características extraídas pela VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.br.png)

## Conjunto de Dados de Gatos vs. Cachorros

Neste exemplo, usaremos um conjunto de dados de [Gatos e Cachorros](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), que é muito próximo de um cenário real de classificação de imagens.

## ✍️ Exercício: Aprendizado por Transferência

Vamos ver o aprendizado por transferência em ação nos notebooks correspondentes:

* [Aprendizado por Transferência - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Aprendizado por Transferência - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualizando o Gato Adversarial

Uma rede neural pré-treinada contém diferentes padrões em seu *cérebro*, incluindo noções de um **gato ideal** (assim como um cachorro ideal, uma zebra ideal, etc.). Seria interessante de alguma forma **visualizar essa imagem**. No entanto, isso não é simples, porque os padrões estão espalhados pelos pesos da rede e organizados em uma estrutura hierárquica.

Uma abordagem que podemos adotar é começar com uma imagem aleatória e, em seguida, tentar usar a técnica de **otimização por descida de gradiente** para ajustar essa imagem de forma que a rede comece a pensar que é um gato.

![Loop de Otimização de Imagem](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.br.png)

No entanto, se fizermos isso, obteremos algo muito semelhante a um ruído aleatório. Isso ocorre porque *existem muitas maneiras de fazer a rede pensar que a imagem de entrada é um gato*, incluindo algumas que não fazem sentido visualmente. Embora essas imagens contenham muitos padrões típicos de um gato, não há nada que as restrinja a serem visualmente distintas.

Para melhorar o resultado, podemos adicionar outro termo à função de perda, chamado de **perda de variação**. É uma métrica que mostra o quão semelhantes são os pixels vizinhos da imagem. Minimizar a perda de variação torna a imagem mais suave e elimina o ruído, revelando assim padrões visualmente mais atraentes. Aqui está um exemplo de tais imagens "ideais", classificadas como gato e zebra com alta probabilidade:

![Gato Ideal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.br.png) | ![Zebra Ideal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.br.png)
-----|-----
*Gato Ideal* | *Zebra Ideal*

Uma abordagem semelhante pode ser usada para realizar os chamados **ataques adversariais** em uma rede neural. Suponha que queremos enganar uma rede neural e fazer um cachorro parecer um gato. Se pegarmos a imagem de um cachorro, que é reconhecida pela rede como um cachorro, podemos ajustá-la um pouco usando a otimização por descida de gradiente, até que a rede comece a classificá-la como um gato:

![Imagem de um Cachorro](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.br.png) | ![Imagem de um cachorro classificada como um gato](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.br.png)
-----|-----
*Imagem original de um cachorro* | *Imagem de um cachorro classificada como um gato*

Veja o código para reproduzir os resultados acima no seguinte notebook:

* [Gato Ideal e Adversarial - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Conclusão

Usando o aprendizado por transferência, você pode rapidamente montar um classificador para uma tarefa personalizada de classificação de objetos e alcançar alta precisão. Você pode perceber que tarefas mais complexas que estamos resolvendo agora exigem maior poder computacional e não podem ser facilmente resolvidas em uma CPU. Na próxima unidade, tentaremos usar uma implementação mais leve para treinar o mesmo modelo usando menos recursos computacionais, resultando em uma precisão ligeiramente menor.

## 🚀 Desafio

Nos notebooks que acompanham, há notas no final sobre como o aprendizado por transferência funciona melhor com dados de treinamento um pouco semelhantes (talvez um novo tipo de animal). Faça alguns experimentos com tipos completamente novos de imagens para ver quão bem ou mal seus modelos de aprendizado por transferência se saem.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisão e Autoestudo

Leia o arquivo [TrainingTricks.md](TrainingTricks.md) para aprofundar seu conhecimento sobre outras formas de treinar seus modelos.

## [Tarefa](lab/README.md)

Neste laboratório, usaremos o conjunto de dados real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) de animais de estimação, com 35 raças de gatos e cachorros, e construiremos um classificador usando aprendizado por transferência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.