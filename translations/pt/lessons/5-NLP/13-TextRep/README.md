# Representando Texto como Tensores

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Classificação de Texto

Na primeira parte desta seção, vamos nos concentrar na tarefa de **classificação de texto**. Usaremos o conjunto de dados [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), que contém artigos de notícias como os seguintes:

* Categoria: Sci/Tech
* Título: Ky. Company Wins Grant to Study Peptides (AP)
* Corpo: AP - Uma empresa fundada por um pesquisador de química na Universidade de Louisville ganhou uma bolsa para desenvolver...

Nosso objetivo será classificar o item de notícia em uma das categorias com base no texto.

## Representando texto

Se quisermos resolver tarefas de Processamento de Linguagem Natural (NLP) com redes neurais, precisamos de alguma forma de representar texto como tensores. Os computadores já representam caracteres textuais como números que mapeiam para fontes na sua tela usando codificações como ASCII ou UTF-8.

<img alt="Imagem mostrando diagrama mapeando um caractere para uma representação ASCII e binária" src="images/ascii-character-map.png" width="50%"/>

> [Fonte da imagem](https://www.seobility.net/en/wiki/ASCII)

Como humanos, entendemos o que cada letra **representa** e como todos os caracteres se juntam para formar as palavras de uma frase. No entanto, os computadores, por si só, não têm essa compreensão, e a rede neural precisa aprender o significado durante o treinamento.

Portanto, podemos usar diferentes abordagens ao representar texto:

* **Representação em nível de caractere**, quando representamos o texto tratando cada caractere como um número. Dado que temos *C* caracteres diferentes em nosso corpus de texto, a palavra *Hello* seria representada por um tensor 5x*C*. Cada letra corresponderia a uma coluna de tensor em codificação one-hot.
* **Representação em nível de palavra**, na qual criamos um **vocabulário** de todas as palavras em nosso texto e, em seguida, representamos as palavras usando codificação one-hot. Essa abordagem é de certa forma melhor, porque cada letra isoladamente não tem muito significado e, assim, ao usar conceitos semânticos de nível superior - palavras - simplificamos a tarefa para a rede neural. No entanto, dado o grande tamanho do dicionário, precisamos lidar com tensores esparsos de alta dimensão.

Independentemente da representação, primeiro precisamos converter o texto em uma sequência de **tokens**, sendo que um token pode ser um caractere, uma palavra ou, às vezes, até mesmo parte de uma palavra. Em seguida, convertemos o token em um número, tipicamente usando **vocabulário**, e esse número pode ser alimentado em uma rede neural usando codificação one-hot.

## N-Gramas

Na linguagem natural, o significado preciso das palavras só pode ser determinado no contexto. Por exemplo, os significados de *rede neural* e *rede de pesca* são completamente diferentes. Uma das maneiras de levar isso em conta é construir nosso modelo com pares de palavras, considerando pares de palavras como tokens de vocabulário separados. Dessa forma, a frase *Eu gosto de pescar* será representada pela seguinte sequência de tokens: *Eu gosto*, *gosto de*, *de pescar*. O problema com essa abordagem é que o tamanho do dicionário cresce significativamente, e combinações como *ir pescar* e *ir às compras* são apresentadas por tokens diferentes, que não compartilham nenhuma semelhança semântica, apesar do mesmo verbo.

Em alguns casos, também podemos considerar o uso de tri-gramas -- combinações de três palavras --. Assim, a abordagem é frequentemente chamada de **n-gramas**. Além disso, faz sentido usar n-gramas com representação em nível de caractere, nesse caso os n-gramas corresponderão aproximadamente a diferentes sílabas.

## Bag-of-Words e TF/IDF

Ao resolver tarefas como a classificação de texto, precisamos ser capazes de representar o texto por um vetor de tamanho fixo, que usaremos como entrada para o classificador denso final. Uma das maneiras mais simples de fazer isso é combinar todas as representações individuais de palavras, por exemplo, somando-as. Se adicionarmos as codificações one-hot de cada palavra, terminaremos com um vetor de frequências, mostrando quantas vezes cada palavra aparece dentro do texto. Essa representação de texto é chamada de **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Imagem do autor

Um BoW representa essencialmente quais palavras aparecem no texto e em quais quantidades, o que pode de fato ser uma boa indicação do que o texto trata. Por exemplo, um artigo de notícias sobre política provavelmente conterá palavras como *presidente* e *país*, enquanto uma publicação científica teria algo como *colisor*, *descoberto*, etc. Assim, as frequências das palavras podem, em muitos casos, ser um bom indicador do conteúdo do texto.

O problema com o BoW é que certas palavras comuns, como *e*, *é*, etc., aparecem na maioria dos textos e têm as maiores frequências, ofuscando as palavras que são realmente importantes. Podemos diminuir a importância dessas palavras levando em conta a frequência com que as palavras ocorrem em toda a coleção de documentos. Essa é a ideia principal por trás da abordagem TF/IDF, que é abordada com mais detalhes nos notebooks anexados a esta lição.

No entanto, nenhuma dessas abordagens pode levar plenamente em conta a **semântica** do texto. Precisamos de modelos de redes neurais mais poderosos para fazer isso, que discutiremos mais adiante nesta seção.

## ✍️ Exercícios: Representação de Texto

Continue seu aprendizado nos seguintes notebooks:

* [Representação de Texto com PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Representação de Texto com TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Conclusão

Até agora, estudamos técnicas que podem adicionar peso de frequência a diferentes palavras. No entanto, elas não conseguem representar significado ou ordem. Como disse o famoso linguista J. R. Firth em 1935: "O significado completo de uma palavra é sempre contextual, e nenhum estudo de significado separado do contexto pode ser levado a sério." Aprenderemos mais tarde no curso como capturar informações contextuais do texto usando modelagem de linguagem.

## 🚀 Desafio

Tente alguns outros exercícios usando bag-of-words e diferentes modelos de dados. Você pode se inspirar nesta [competição no Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Revisão & Autoestudo

Pratique suas habilidades com embeddings de texto e técnicas de bag-of-words em [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Tarefa: Notebooks](assignment.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.