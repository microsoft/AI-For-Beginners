# Treinamento do Modelo Skip-Gram

Tarefa do [Currículo AI para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, desafiamos você a treinar um modelo Word2Vec usando a técnica Skip-Gram. Treine uma rede com incorporação para prever palavras vizinhas em uma janela Skip-Gram de $N$-tokens de largura. Você pode usar o [código desta lição](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) e modificá-lo ligeiramente.

## O Conjunto de Dados

Sinta-se à vontade para usar qualquer livro. Você pode encontrar muitos textos gratuitos no [Project Gutenberg](https://www.gutenberg.org/); por exemplo, aqui está um link direto para [As Aventuras de Alice no País das Maravilhas](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. Ou, você pode usar as peças de Shakespeare, que você pode obter usando o seguinte código:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore!

Se você tiver tempo e quiser se aprofundar no assunto, tente explorar várias coisas:

* Como o tamanho da incorporação afeta os resultados?
* Como diferentes estilos de texto afetam o resultado?
* Pegue vários tipos de palavras muito diferentes e seus sinônimos, obtenha suas representações vetoriais, aplique PCA para reduzir as dimensões para 2 e plote-os em um espaço 2D. Você vê algum padrão?

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.