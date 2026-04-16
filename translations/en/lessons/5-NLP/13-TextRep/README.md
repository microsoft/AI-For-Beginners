<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbd3f73e4139f030ecb2e20387d70fee",
  "translation_date": "2025-09-23T11:54:14+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "en"
}
-->
# Representing Text as Tensors

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Text Classification

In the first part of this section, we will focus on the task of **text classification**. We'll use the [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Dataset, which contains news articles like the following:

* Category: Sci/Tech
* Title: Ky. Company Wins Grant to Study Peptides (AP)
* Body: AP - A company founded by a chemistry researcher at the University of Louisville won a grant to develop...

Our goal will be to classify the news item into one of the categories based on its text.

## Representing text

To solve Natural Language Processing (NLP) tasks using neural networks, we need a way to represent text as tensors. Computers already represent textual characters as numbers that map to fonts on your screen using encodings like ASCII or UTF-8.

<img alt="Image showing diagram mapping a character to an ASCII and binary representation" src="images/ascii-character-map.png" width="50%"/>

> [Image source](https://www.seobility.net/en/wiki/ASCII)

As humans, we understand what each letter **represents** and how all characters come together to form the words in a sentence. However, computers do not inherently have this understanding, and a neural network must learn the meaning during training.

There are different approaches to representing text:

* **Character-level representation**, where text is represented by treating each character as a number. If we have *C* different characters in our text corpus, the word *Hello* would be represented by a 5x*C* tensor. Each letter corresponds to a tensor column in one-hot encoding.
* **Word-level representation**, where we create a **vocabulary** of all words in our text and represent words using one-hot encoding. This approach is somewhat better because individual letters lack much meaning, and using higher-level semantic concepts—words—simplifies the task for the neural network. However, due to the large dictionary size, we must deal with high-dimensional sparse tensors.

Regardless of the representation, the first step is to convert the text into a sequence of **tokens**, where a token can be a character, a word, or even part of a word. Then, we convert the token into a number, typically using a **vocabulary**, and this number can be fed into a neural network using one-hot encoding.

## N-Grams

In natural language, the precise meaning of words can only be understood in context. For example, the meanings of *neural network* and *fishing network* are entirely different. One way to account for this is to build our model using pairs of words, treating word pairs as separate vocabulary tokens. For instance, the sentence *I like to go fishing* would be represented by the following sequence of tokens: *I like*, *like to*, *to go*, *go fishing*. 

The downside of this approach is that the dictionary size increases significantly, and combinations like *go fishing* and *go shopping* are treated as different tokens, even though they share the same verb and have some semantic similarity.

In some cases, we might use tri-grams—combinations of three words—as well. This approach is often referred to as **n-grams**. It can also be applied to character-level representation, where n-grams roughly correspond to different syllables.

## Bag-of-Words and TF/IDF

For tasks like text classification, we need to represent text as a fixed-size vector that can be used as input to a final dense classifier. One simple way to achieve this is by combining individual word representations, such as adding them together. If we add one-hot encodings of each word, we end up with a vector of frequencies that shows how often each word appears in the text. This representation is called **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Image by the author

A BoW essentially captures which words appear in the text and their quantities, which can be a good indicator of the text's content. For example, a news article about politics might contain words like *president* and *country*, while a scientific publication might include terms like *collider* and *discovered*. Word frequencies can often provide valuable insight into the text's subject matter.

The problem with BoW is that common words like *and* and *is* appear in most texts and have the highest frequencies, overshadowing the words that are truly important. To address this, we can reduce the importance of these common words by considering their frequency across the entire document collection. This is the main idea behind the TF/IDF approach, which is explained in more detail in the notebooks attached to this lesson.

However, neither BoW nor TF/IDF can fully capture the **semantics** of text. To achieve this, we need more advanced neural network models, which we will explore later in this section.

## ✍️ Exercises: Text Representation

Continue your learning with the following notebooks:

* [Text Representation with PyTorch](TextRepresentationPyTorch.ipynb)
* [Text Representation with TensorFlow](TextRepresentationTF.ipynb)

## Conclusion

So far, we've explored techniques that add frequency weight to different words. However, these methods cannot represent meaning or word order. As the renowned linguist J. R. Firth stated in 1935, "The complete meaning of a word is always contextual, and no study of meaning apart from context can be taken seriously." Later in the course, we will learn how to capture contextual information from text using language modeling.

## 🚀 Challenge

Try additional exercises using bag-of-words and other data models. You might find inspiration in this [competition on Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Review & Self Study

Practice your skills with text embeddings and bag-of-words techniques on [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Assignment: Notebooks](assignment.md)

---

