<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbd3f73e4139f030ecb2e20387d70fee",
  "translation_date": "2025-11-18T18:38:48+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "pcm"
}
-->
# Representing Text as Tensors

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Text Classification

For dis first part of dis section, we go focus on **text classification** task. We go use [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Dataset, wey get news articles like dis one:

* Category: Sci/Tech
* Title: Ky. Company Wins Grant to Study Peptides (AP)
* Body: AP - One company wey one chemistry researcher for University of Louisville start don win grant to develop...

Our goal na to classify di news item into one of di categories based on di text.

## Representing text

If we wan solve Natural Language Processing (NLP) tasks wit neural networks, we need way to represent text as tensors. Computers dey already represent text characters as numbers wey dey map to fonts for your screen using encodings like ASCII or UTF-8.

<img alt="Image wey show diagram wey dey map one character to ASCII and binary representation" src="../../../../../translated_images/ascii-character-map.18ed6aa7f3b0a7ffeb29db95be05a245b6a20712bb2c3a9963c1ec7e9df70358.pcm.png" width="50%"/>

> [Image source](https://www.seobility.net/en/wiki/ASCII)

As humans, we sabi wetin each letter **mean**, and how all di characters dey join together to form di words for one sentence. But computers no get dis kain understanding by demself, and neural network go need learn di meaning during training.

So, we fit use different ways to represent text:

* **Character-level representation**, wey mean we go represent text by treating each character as one number. If we get *C* different characters for our text corpus, di word *Hello* go dey represented by 5x*C* tensor. Each letter go correspond to one tensor column for one-hot encoding.
* **Word-level representation**, wey mean we go create one **vocabulary** of all di words for our text, then represent di words using one-hot encoding. Dis approach better small, because each letter no get plenty meaning by itself, so if we use higher-level semantic concepts - words - we go make di task easier for di neural network. But, because di dictionary size big, we go need deal wit high-dimensional sparse tensors.

No matter di representation, we first need convert di text into one sequence of **tokens**, one token fit be character, word, or even part of word. Then, we go convert di token into one number, usually using **vocabulary**, and dis number fit enter neural network using one-hot encoding.

## N-Grams

For natural language, di exact meaning of words fit only show for context. For example, di meaning of *neural network* and *fishing network* dey totally different. One way to handle dis na to build our model on pairs of words, and treat word pairs as separate vocabulary tokens. Like dis, di sentence *I like to go fishing* go dey represented by dis sequence of tokens: *I like*, *like to*, *to go*, *go fishing*. Di problem wit dis approach na say di dictionary size go grow well well, and combinations like *go fishing* and *go shopping* go dey represented by different tokens, wey no get any semantic similarity even though di same verb dey.

Sometimes, we fit use tri-grams -- combinations of three words -- too. Dis approach dey called **n-grams**. E also make sense to use n-grams wit character-level representation, wey go mean n-grams go roughly correspond to different syllables.

## Bag-of-Words and TF/IDF

If we dey solve tasks like text classification, we need way to represent text as one fixed-size vector, wey we go use as input to di final dense classifier. One simple way na to combine all di individual word representations, like adding dem. If we add one-hot encodings of each word, we go get one vector of frequencies, wey go show how many times each word appear for di text. Dis representation of text na **bag of words** (BoW).

<img src="../../../../../translated_images/bow.3811869cff59368d951c7a765ed20ebeaf7d10680eb602ea7c5312fb22f7b7ad.pcm.png" width="90%"/>

> Image by di author

BoW dey show which words dey appear for text and how many times dem appear, wey fit be good clue of wetin di text dey talk about. For example, news article about politics fit get words like *president* and *country*, while scientific publication fit get words like *collider*, *discovered*, etc. So, word frequencies fit be good clue of di text content.

Di problem wit BoW na say some common words, like *and*, *is*, etc. dey appear for most texts, and dem dey get di highest frequencies, wey fit cover di words wey really important. We fit reduce di importance of those words by considering di frequency wey words dey appear for di whole document collection. Dis na di main idea behind TF/IDF approach, wey dey explained more for di notebooks wey dey attached to dis lesson.

But, none of dis approaches fit fully capture di **semantics** of text. We need stronger neural network models to do dis, wey we go discuss later for dis section.

## ✍️ Exercises: Text Representation

Continue your learning for di following notebooks:

* [Text Representation with PyTorch](TextRepresentationPyTorch.ipynb)
* [Text Representation with TensorFlow](TextRepresentationTF.ipynb)

## Conclusion

So far, we don study techniques wey fit add frequency weight to different words. But dem no fit represent meaning or order. As di famous linguist J. R. Firth talk for 1935, "Di complete meaning of one word dey always contextual, and no study of meaning wey no consider context fit dey serious." We go learn later for di course how to capture contextual information from text using language modeling.

## 🚀 Challenge

Try some other exercises using bag-of-words and different data models. You fit get inspiration from dis [competition on Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Review & Self Study

Practice your skills wit text embeddings and bag-of-words techniques for [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Assignment: Notebooks](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->