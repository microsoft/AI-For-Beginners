# Treinar Modelo Skip-Gram

Trabalho prático do [Currículo AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, desafiamos-te a treinar um modelo Word2Vec utilizando a técnica Skip-Gram. Treina uma rede com embeddings para prever palavras vizinhas numa janela Skip-Gram de $N$ tokens de largura. Podes usar o [código desta lição](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) e modificá-lo ligeiramente.

## O Conjunto de Dados

Podes usar qualquer livro. Podes encontrar muitos textos gratuitos no [Project Gutenberg](https://www.gutenberg.org/), por exemplo, aqui está um link direto para [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. Ou, podes usar as peças de Shakespeare, que podes obter utilizando o seguinte código:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explora!

Se tiveres tempo e quiseres aprofundar o tema, tenta explorar várias questões:

* Como o tamanho do embedding afeta os resultados?
* Como diferentes estilos de texto afetam o resultado?
* Escolhe vários tipos de palavras muito diferentes e os seus sinónimos, obtém as suas representações vetoriais, aplica PCA para reduzir as dimensões para 2 e representa-as num espaço 2D. Consegues identificar algum padrão?

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.