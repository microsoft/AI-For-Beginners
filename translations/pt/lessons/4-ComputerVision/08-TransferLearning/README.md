# Redes Neurais Pré-treinadas e Aprendizado por Transferência

Treinar CNNs pode levar muito tempo, e uma grande quantidade de dados é necessária para essa tarefa. No entanto, muito do tempo é gasto aprendendo os melhores filtros de baixo nível que uma rede pode usar para extrair padrões de imagens. Surge uma pergunta natural - podemos usar uma rede neural treinada em um conjunto de dados e adaptá-la para classificar diferentes imagens sem precisar de um processo de treinamento completo?

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Essa abordagem é chamada de **aprendizado por transferência**, porque transferimos algum conhecimento de um modelo de rede neural para outro. No aprendizado por transferência, normalmente começamos com um modelo pré-treinado, que foi treinado em algum grande conjunto de dados de imagens, como **ImageNet**. Esses modelos já podem fazer um bom trabalho extraindo diferentes características de imagens genéricas, e em muitos casos, apenas construir um classificador em cima dessas características extraídas pode resultar em um bom resultado.

> ✅ Aprendizado por Transferência é um termo que você encontra em outros campos acadêmicos, como Educação. Refere-se ao processo de levar conhecimento de um domínio e aplicá-lo a outro.

## Modelos Pré-Treinados como Extratores de Características

As redes convolucionais que discutimos na seção anterior continham uma série de camadas, cada uma das quais deve extrair algumas características da imagem, começando por combinações de pixels de baixo nível (como linha horizontal/vertical ou traço), até combinações de características de nível mais alto, correspondendo a coisas como o olho de uma chama. Se treinarmos uma CNN em um conjunto de dados suficientemente grande de imagens genéricas e diversas, a rede deve aprender a extrair essas características comuns.

Tanto Keras quanto PyTorch contêm funções para carregar facilmente pesos de redes neurais pré-treinadas para algumas arquiteturas comuns, a maioria das quais foi treinada em imagens do ImageNet. As mais frequentemente usadas estão descritas na página de [Arquiteturas CNN](../07-ConvNets/CNN_Architectures.md) da lição anterior. Em particular, você pode considerar usar uma das seguintes:

* **VGG-16/VGG-19**, que são modelos relativamente simples que ainda oferecem boa precisão. Muitas vezes, usar VGG como uma primeira tentativa é uma boa escolha para ver como o aprendizado por transferência funciona.
* **ResNet** é uma família de modelos proposta pela Microsoft Research em 2015. Eles têm mais camadas e, portanto, consomem mais recursos.
* **MobileNet** é uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Use-os se você estiver com recursos limitados e puder sacrificar um pouco de precisão.

Aqui estão amostras de características extraídas de uma imagem de um gato pela rede VGG-16:

![Características extraídas pela VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.pt.png)

## Conjunto de Dados de Gatos vs. Cachorros

Neste exemplo, usaremos um conjunto de dados de [Gatos e Cachorros](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), que é muito próximo de um cenário real de classificação de imagens.

## ✍️ Exercício: Aprendizado por Transferência

Vamos ver o aprendizado por transferência em ação nos cadernos correspondentes:

* [Aprendizado por Transferência - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Aprendizado por Transferência - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualizando o Gato Adversarial

A rede neural pré-treinada contém diferentes padrões dentro de seu *cérebro*, incluindo noções de **gato ideal** (assim como cachorro ideal, zebra ideal, etc.). Seria interessante de alguma forma **visualizar essa imagem**. No entanto, não é simples, porque os padrões estão espalhados por todo o peso da rede e também organizados em uma estrutura hierárquica.

Uma abordagem que podemos adotar é começar com uma imagem aleatória e, em seguida, tentar usar a técnica de **otimização por descida de gradiente** para ajustar essa imagem de tal forma que a rede comece a pensar que é um gato.

![Loop de Otimização de Imagem](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.pt.png)

No entanto, se fizermos isso, receberemos algo muito semelhante a um ruído aleatório. Isso ocorre porque *existem muitas maneiras de fazer a rede pensar que a imagem de entrada é um gato*, incluindo algumas que não fazem sentido visualmente. Embora essas imagens contenham muitos padrões típicos de um gato, não há nada que as restrinja a serem visualmente distintas.

Para melhorar o resultado, podemos adicionar outro termo à função de perda, que é chamado de **perda de variação**. É uma métrica que mostra quão semelhantes são os pixels vizinhos da imagem. Minimizar a perda de variação torna a imagem mais suave e elimina o ruído - revelando assim padrões visualmente mais agradáveis. Aqui está um exemplo de tais imagens "ideais", que são classificadas como gato e como zebra com alta probabilidade:

![Gato Ideal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.pt.png) | ![Zebra Ideal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.pt.png)
-----|-----
 *Gato Ideal* | *Zebra Ideal*

Uma abordagem semelhante pode ser usada para realizar os chamados **ataques adversariais** em uma rede neural. Suponha que queiramos enganar uma rede neural e fazer um cachorro parecer um gato. Se pegarmos a imagem de um cachorro, que é reconhecida pela rede como um cachorro, podemos então ajustá-la um pouco usando otimização por descida de gradiente, até que a rede comece a classificá-la como um gato:

![Imagem de um Cachorro](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.pt.png) | ![Imagem de um cachorro classificada como gato](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.pt.png)
-----|-----
*Imagem original de um cachorro* | *Imagem de um cachorro classificada como gato*

Veja o código para reproduzir os resultados acima no seguinte caderno:

* [Gato Ideal e Adversarial - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Conclusão

Usando aprendizado por transferência, você pode rapidamente montar um classificador para uma tarefa de classificação de objetos personalizada e alcançar alta precisão. Você pode ver que tarefas mais complexas que estamos resolvendo agora requerem maior poder computacional e não podem ser facilmente resolvidas na CPU. Na próxima unidade, tentaremos usar uma implementação mais leve para treinar o mesmo modelo usando recursos computacionais menores, o que resulta em uma precisão apenas ligeiramente inferior.

## 🚀 Desafio

Nos cadernos acompanhantes, há notas na parte inferior sobre como o conhecimento de transferência funciona melhor com dados de treinamento um tanto semelhantes (um novo tipo de animal, talvez). Faça algumas experimentações com tipos de imagens completamente novos para ver quão bem ou mal seus modelos de conhecimento de transferência se saem.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisão & Autoestudo

Leia [TrainingTricks.md](TrainingTricks.md) para aprofundar seu conhecimento sobre algumas outras maneiras de treinar seus modelos.

## [Tarefa](lab/README.md)

Neste laboratório, usaremos um conjunto de dados de animais de estimação da vida real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) com 35 raças de gatos e cachorros, e construiremos um classificador de aprendizado por transferência.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.