<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-31T18:01:52+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "en"
}
-->
# Representing Text as Tensors

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Text Classification

In the first part of this section, we will focus on the task of **text classification**. We will use the [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Dataset, which contains news articles like the following:

* Category: Sci/Tech
* Title: Ky. Company Wins Grant to Study Peptides (AP)
* Body: AP - A company founded by a chemistry researcher at the University of Louisville won a grant to develop...

Our goal will be to classify the news item into one of the categories based on the text.

## Representing text

To solve Natural Language Processing (NLP) tasks with neural networks, we need a way to represent text as tensors. Computers already represent textual characters as numbers that map to fonts on your screen using encodings like ASCII or UTF-8.

<img alt="Image showing diagram mapping a character to an ASCII and binary representation" src="images/ascii-character-map.png" width="50%"/>

> [Image source](https://www.seobility.net/en/wiki/ASCII)

As humans, we understand what each letter **represents**, and how all characters come together to form the words of a sentence. However, computers do not have this understanding inherently, and a neural network must learn the meaning during training.

Thus, we can use different approaches to represent text:

* **Character-level representation**, where we represent text by treating each character as a number. If we have *C* different characters in our text corpus, the word *Hello* would be represented by a 5x*C* tensor. Each letter corresponds to a tensor column in one-hot encoding.
* **Word-level representation**, where we create a **vocabulary** of all words in our text and represent words using one-hot encoding. This approach is somewhat better because individual letters have little meaning, and using higher-level semantic concepts—words—simplifies the task for the neural network. However, due to the large dictionary size, we must deal with high-dimensional sparse tensors.

Regardless of the representation, we first need to convert the text into a sequence of **tokens**, where a token can be a character, a word, or even part of a word. Then, we convert the token into a number, typically using a **vocabulary**, and this number can be fed into a neural network using one-hot encoding.

## N-Grams

In natural language, the precise meaning of words can only be understood in context. For example, the meanings of *neural network* and *fishing network* are completely different. One way to account for this is to build our model using pairs of words, treating word pairs as separate vocabulary tokens. For instance, the sentence *I like to go fishing* would be represented by the following sequence of tokens: *I like*, *like to*, *to go*, *go fishing*. 

The downside of this approach is that the dictionary size grows significantly, and combinations like *go fishing* and *go shopping* are treated as different tokens, even though they share the same verb and have some semantic similarity.

In some cases, we might use tri-grams—combinations of three words—as well. This approach is generally referred to as **n-grams**. It can also be applied to character-level representation, where n-grams roughly correspond to different syllables.

## Bag-of-Words and TF/IDF

When solving tasks like text classification, we need to represent text as a fixed-size vector, which can be used as input to a final dense classifier. One simple way to do this is to combine all individual word representations, for example, by adding them. If we add one-hot encodings of each word, we end up with a vector of frequencies, showing how many times each word appears in the text. This representation is called **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Image by the author

A BoW essentially shows which words appear in the text and how often, which can be a good indicator of the text's content. For example, a news article about politics is likely to contain words like *president* and *country*, while a scientific publication might include words like *collider* and *discovered*. Thus, word frequencies can often provide a good indication of the text's subject.

The problem with BoW is that common words like *and* and *is* appear in most texts and have the highest frequencies, overshadowing the words that are truly important. To address this, we can reduce the importance of these common words by considering how frequently they occur across the entire document collection. This is the main idea behind the TF/IDF approach, which is covered in more detail in the notebooks attached to this lesson.

However, neither of these approaches can fully capture the **semantics** of text. To achieve this, we need more powerful neural network models, which we will discuss later in this section.

## ✍️ Exercises: Text Representation

Continue your learning in the following notebooks:

* [Text Representation with PyTorch](TextRepresentationPyTorch.ipynb)
* [Text Representation with TensorFlow](TextRepresentationTF.ipynb)

## Conclusion

So far, we have explored techniques that add frequency weight to different words. However, these methods cannot represent meaning or word order. As the famous linguist J. R. Firth said in 1935, "The complete meaning of a word is always contextual, and no study of meaning apart from context can be taken seriously." Later in the course, we will learn how to capture contextual information from text using language modeling.

## 🚀 Challenge

Try some other exercises using bag-of-words and different data models. You might find inspiration in this [competition on Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Review & Self Study

Practice your skills with text embeddings and bag-of-words techniques on [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Assignment: Notebooks](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.