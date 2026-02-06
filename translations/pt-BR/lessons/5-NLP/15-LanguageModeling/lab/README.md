# Treinando o Modelo Skip-Gram

Atividade prática do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, desafiamos você a treinar um modelo Word2Vec usando a técnica Skip-Gram. Treine uma rede com embeddings para prever palavras vizinhas em uma janela Skip-Gram de $N$ tokens de largura. Você pode usar o [código desta lição](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) e modificá-lo levemente.

## O Conjunto de Dados

Você pode usar qualquer livro. Há muitos textos gratuitos disponíveis no [Project Gutenberg](https://www.gutenberg.org/), por exemplo, aqui está um link direto para [Alice no País das Maravilhas](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. Ou, você pode usar as peças de Shakespeare, que podem ser obtidas com o seguinte código:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore!

Se você tiver tempo e quiser se aprofundar no assunto, tente explorar algumas coisas:

* Como o tamanho do embedding afeta os resultados?
* Como diferentes estilos de texto afetam o resultado?
* Pegue vários tipos de palavras muito diferentes e seus sinônimos, obtenha suas representações vetoriais, aplique PCA para reduzir as dimensões para 2 e plote-as em um espaço 2D. Você percebe algum padrão?

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.