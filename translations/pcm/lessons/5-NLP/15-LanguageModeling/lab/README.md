<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5130f01fdc5ebb83032b23d489027aac",
  "translation_date": "2025-11-18T18:41:32+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/lab/README.md",
  "language_code": "pcm"
}
-->
# Train Skip-Gram Model

Lab Assignment wey come from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

For dis lab, we go challenge you to train Word2Vec model wey dey use Skip-Gram technique. Train one network wey get embedding to fit predict words wey dey near for $N$-tokens-wide Skip-Gram window. You fit use [code wey dey dis lesson](../CBoW-TF.ipynb), and just small modify am.

## The Dataset

You fit use any book wey you like. You fit find plenty free texts for [Project Gutenberg](https://www.gutenberg.org/), like dis direct link to [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) wey Lewis Carroll write. Or, you fit use Shakespeare plays, wey you fit get if you run dis code:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore!

If you get time and wan sabi more for dis topic, try check dis things:

* How embedding size dey affect the results?
* How different text styles dey affect the result?
* Pick some very different types of words and their synonyms, get their vector representations, use PCA to reduce dimensions to 2, and plot them for 2D space. You dey see any pattern?

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make sure say e correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->