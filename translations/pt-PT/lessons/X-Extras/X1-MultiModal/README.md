# Redes Multi-Modais

Após o sucesso dos modelos transformadores na resolução de tarefas de PLN, as mesmas ou similares arquiteturas foram aplicadas a tarefas de visão computacional. Há um interesse crescente em construir modelos que *combinem* capacidades de visão e linguagem natural. Uma dessas tentativas foi realizada pela OpenAI, chamada CLIP e DALL.E.

## Treino Contrastivo de Imagens (CLIP)

A ideia principal do CLIP é ser capaz de comparar descrições textuais com uma imagem e determinar o quão bem a imagem corresponde à descrição.

![Arquitetura CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-arch.png)

> *Imagem retirada [deste artigo](https://openai.com/blog/clip/)*

O modelo é treinado com imagens obtidas da Internet e suas legendas. Para cada lote, pegamos N pares de (imagem, texto) e convertemos para representações vetoriais I, ..., I / T, ..., T. Essas representações são então comparadas entre si. A função de perda é definida para maximizar a similaridade cosseno entre os vetores correspondentes a um par (por exemplo, I e T) e minimizar a similaridade cosseno entre todos os outros pares. É por isso que essa abordagem é chamada de **contrastiva**.

O modelo/biblioteca CLIP está disponível no [GitHub da OpenAI](https://github.com/openai/CLIP). A abordagem é descrita [neste artigo](https://openai.com/blog/clip/) e em mais detalhes [neste artigo científico](https://arxiv.org/pdf/2103.00020.pdf).

Uma vez que este modelo é pré-treinado, podemos fornecer um lote de imagens e um lote de descrições textuais, e ele retornará um tensor com probabilidades. O CLIP pode ser usado para várias tarefas:

**Classificação de Imagens**

Suponha que precisamos classificar imagens entre, por exemplo, gatos, cães e humanos. Nesse caso, podemos fornecer ao modelo uma imagem e uma série de descrições textuais: "*uma foto de um gato*", "*uma foto de um cão*", "*uma foto de um humano*". No vetor resultante de 3 probabilidades, basta selecionar o índice com o valor mais alto.

![CLIP para Classificação de Imagens](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-class.png)

> *Imagem retirada [deste artigo](https://openai.com/blog/clip/)*

**Pesquisa de Imagens Baseada em Texto**

Também podemos fazer o oposto. Se tivermos uma coleção de imagens, podemos passar essa coleção para o modelo e uma descrição textual - isso nos dará a imagem mais semelhante à descrição fornecida.

## ✍️ Exemplo: [Usando CLIP para Classificação de Imagens e Pesquisa de Imagens](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Abra o notebook [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) para ver o CLIP em ação.

## Geração de Imagens com VQGAN+CLIP

O CLIP também pode ser usado para **geração de imagens** a partir de uma descrição textual. Para isso, precisamos de um **modelo gerador** que seja capaz de gerar imagens com base em algum vetor de entrada. Um desses modelos é chamado [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

As principais ideias do VQGAN que o diferenciam de um [GAN](../../4-ComputerVision/10-GANs/README.md) tradicional são as seguintes:
* Uso de uma arquitetura transformadora autorregressiva para gerar uma sequência de partes visuais ricas em contexto que compõem a imagem. Essas partes visuais, por sua vez, são aprendidas por uma [CNN](../../4-ComputerVision/07-ConvNets/README.md).
* Uso de um discriminador de sub-imagens que detecta se partes da imagem são "reais" ou "falsas" (diferente da abordagem "tudo ou nada" nos GANs tradicionais).

Saiba mais sobre o VQGAN no site [Taming Transformers](https://compvis.github.io/taming-transformers/).

Uma das diferenças importantes entre o VQGAN e um GAN tradicional é que o último pode produzir uma imagem decente a partir de qualquer vetor de entrada, enquanto o VQGAN provavelmente produzirá uma imagem incoerente. Assim, precisamos orientar ainda mais o processo de criação da imagem, e isso pode ser feito usando o CLIP.

![Arquitetura VQGAN+CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/vqgan.png)

Para gerar uma imagem correspondente a uma descrição textual, começamos com um vetor de codificação aleatório que é passado pelo VQGAN para produzir uma imagem. Em seguida, o CLIP é usado para produzir uma função de perda que mostra o quão bem a imagem corresponde à descrição textual. O objetivo, então, é minimizar essa perda, usando retropropagação para ajustar os parâmetros do vetor de entrada.

Uma excelente biblioteca que implementa o VQGAN+CLIP é a [Pixray](http://github.com/pixray/pixray).

![Imagem gerada pelo Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![Imagem gerada pelo Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![Imagem gerada pelo Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
Imagem gerada a partir da descrição *um retrato em aquarela de perto de um jovem professor de literatura com um livro* | Imagem gerada a partir da descrição *um retrato a óleo de perto de uma jovem professora de ciência da computação com um computador* | Imagem gerada a partir da descrição *um retrato a óleo de perto de um professor idoso de matemática em frente a um quadro-negro*

> Imagens da coleção **Artificial Teachers** por [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E é uma versão do GPT-3 treinada para gerar imagens a partir de descrições textuais. Foi treinado com 12 bilhões de parâmetros.

Ao contrário do CLIP, o DALL-E recebe tanto texto quanto imagem como um único fluxo de tokens para ambos. Assim, a partir de várias descrições, é possível gerar imagens baseadas no texto.

### [DALL-E 2](https://openai.com/dall-e-2)
A principal diferença entre o DALL-E 1 e o 2 é que este último gera imagens e arte mais realistas.

Exemplos de imagens geradas com o DALL-E:
![Imagem gerada pelo DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![Imagem gerada pelo DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![Imagem gerada pelo DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----
Imagem gerada a partir da descrição *um retrato em aquarela de perto de um jovem professor de literatura com um livro* | Imagem gerada a partir da descrição *um retrato a óleo de perto de uma jovem professora de ciência da computação com um computador* | Imagem gerada a partir da descrição *um retrato a óleo de perto de um professor idoso de matemática em frente a um quadro-negro*

## Referências

* Artigo sobre VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Artigo sobre CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.