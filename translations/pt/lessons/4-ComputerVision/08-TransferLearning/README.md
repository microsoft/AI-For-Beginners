<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-24T09:00:55+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "pt"
}
-->
# Redes Pré-treinadas e Aprendizagem por Transferência

Treinar CNNs pode levar muito tempo e requer uma grande quantidade de dados. No entanto, grande parte do tempo é gasto aprendendo os melhores filtros de baixo nível que uma rede pode usar para extrair padrões de imagens. Surge uma questão natural: podemos usar uma rede neural treinada em um conjunto de dados e adaptá-la para classificar imagens diferentes sem precisar de um processo completo de treino?

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Essa abordagem é chamada de **aprendizagem por transferência**, porque transferimos algum conhecimento de um modelo de rede neural para outro. Na aprendizagem por transferência, normalmente começamos com um modelo pré-treinado, que foi treinado em um grande conjunto de dados de imagens, como o **ImageNet**. Esses modelos já conseguem extrair diferentes características de imagens genéricas, e, em muitos casos, apenas construir um classificador em cima dessas características extraídas pode gerar bons resultados.

> ✅ Aprendizagem por Transferência é um termo que também aparece em outros campos acadêmicos, como Educação. Refere-se ao processo de aplicar conhecimento de um domínio a outro.

## Modelos Pré-treinados como Extratores de Características

As redes convolucionais que discutimos na seção anterior contêm várias camadas, cada uma delas destinada a extrair características da imagem, começando por combinações de pixels de baixo nível (como linhas horizontais/verticais ou traços), até combinações de características de nível mais alto, correspondendo a coisas como o olho de uma chama. Se treinarmos uma CNN em um conjunto de dados suficientemente grande e diversificado, a rede deve aprender a extrair essas características comuns.

Tanto o Keras quanto o PyTorch possuem funções para carregar facilmente pesos de redes neurais pré-treinadas para algumas arquiteturas comuns, a maioria das quais foi treinada em imagens do ImageNet. As mais utilizadas estão descritas na página [Arquiteturas de CNN](../07-ConvNets/CNN_Architectures.md) da lição anterior. Em particular, pode ser interessante considerar uma das seguintes:

* **VGG-16/VGG-19**, que são modelos relativamente simples, mas ainda assim oferecem boa precisão. Usar o VGG como uma primeira tentativa é uma boa escolha para ver como a aprendizagem por transferência funciona.
* **ResNet**, uma família de modelos proposta pela Microsoft Research em 2015. Eles possuem mais camadas e, portanto, exigem mais recursos.
* **MobileNet**, uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Use-os se estiver com poucos recursos e puder sacrificar um pouco de precisão.

Aqui estão exemplos de características extraídas de uma imagem de um gato pela rede VGG-16:

![Características extraídas pela VGG-16](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/features.png)

## Conjunto de Dados de Gatos vs. Cães

Neste exemplo, usaremos um conjunto de dados de [Gatos e Cães](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), que é muito próximo de um cenário real de classificação de imagens.

## ✍️ Exercício: Aprendizagem por Transferência

Vamos ver a aprendizagem por transferência em ação nos notebooks correspondentes:

* [Transfer Learning - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualizando o Gato Adversarial

Uma rede neural pré-treinada contém diferentes padrões dentro do seu *cérebro*, incluindo noções de **gato ideal** (assim como cão ideal, zebra ideal, etc.). Seria interessante **visualizar essa imagem** de alguma forma. No entanto, isso não é simples, porque os padrões estão espalhados pelos pesos da rede e organizados em uma estrutura hierárquica.

Uma abordagem que podemos adotar é começar com uma imagem aleatória e, em seguida, usar a técnica de **otimização por descida de gradiente** para ajustar essa imagem de forma que a rede comece a pensar que é um gato.

![Loop de Otimização de Imagem](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat-loop.png)

No entanto, se fizermos isso, obteremos algo muito semelhante a um ruído aleatório. Isso ocorre porque *existem muitas maneiras de fazer a rede pensar que a imagem de entrada é um gato*, incluindo algumas que não fazem sentido visualmente. Embora essas imagens contenham muitos padrões típicos de um gato, não há nada que as restrinja a serem visualmente distintas.

Para melhorar o resultado, podemos adicionar outro termo à função de perda, chamado **perda de variação**. É uma métrica que mostra quão semelhantes são os pixels vizinhos da imagem. Minimizar a perda de variação torna a imagem mais suave e elimina o ruído, revelando padrões mais visualmente atraentes. Aqui está um exemplo de imagens "ideais", classificadas como gato e zebra com alta probabilidade:

![Gato Ideal](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat.png) | ![Zebra Ideal](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-zebra.png)
-----|-----
 *Gato Ideal* | *Zebra Ideal*

Uma abordagem semelhante pode ser usada para realizar os chamados **ataques adversariais** em uma rede neural. Suponha que queremos enganar uma rede neural e fazer um cão parecer um gato. Se pegarmos a imagem de um cão, que é reconhecida pela rede como um cão, podemos ajustá-la um pouco usando otimização por descida de gradiente até que a rede comece a classificá-la como um gato:

![Imagem de um Cão](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/original-dog.png) | ![Imagem de um cão classificada como gato](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/adversarial-dog.png)
-----|-----
*Imagem original de um cão* | *Imagem de um cão classificada como gato*

Veja o código para reproduzir os resultados acima no seguinte notebook:

* [Ideal e Adversarial Cat - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Conclusão

Usando a aprendizagem por transferência, é possível montar rapidamente um classificador para uma tarefa de classificação de objetos personalizada e alcançar alta precisão. É possível perceber que tarefas mais complexas que estamos resolvendo agora exigem maior poder computacional e não podem ser facilmente resolvidas no CPU. Na próxima unidade, tentaremos usar uma implementação mais leve para treinar o mesmo modelo usando menos recursos computacionais, o que resulta em uma precisão ligeiramente menor.

## 🚀 Desafio

Nos notebooks que acompanham, há notas no final sobre como o conhecimento transferido funciona melhor com dados de treino relativamente semelhantes (um novo tipo de animal, talvez). Faça algumas experiências com tipos completamente novos de imagens para ver como os modelos de conhecimento transferido funcionam bem ou mal.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisão e Estudo Individual

Leia o documento [TrainingTricks.md](TrainingTricks.md) para aprofundar seu conhecimento sobre outras formas de treinar seus modelos.

## [Tarefa](lab/README.md)

Neste laboratório, usaremos o conjunto de dados real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) de animais de estimação, com 35 raças de gatos e cães, e construiremos um classificador de aprendizagem por transferência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.