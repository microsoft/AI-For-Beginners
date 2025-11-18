<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6522312ff835796ca34136a9462fafb2",
  "translation_date": "2025-11-18T18:40:02+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "pcm"
}
-->
# Named Entity Recognition

So far, we don dey focus mostly on one NLP task - classification. But e get other NLP tasks wey neural networks fit do. One of dem na **[Named Entity Recognition](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), wey dey help to sabi specific entities for text, like places, person names, date-time intervals, chemical formulae and so on.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Example of Using NER

Make we say you wan build natural language chat bot, like Amazon Alexa or Google Assistant. Di way wey smart chat bots dey work na to *understand* wetin di user wan by doing text classification for di sentence wey dem type. Di result of dis classification na wetin dem dey call **intent**, wey go show wetin di chat bot suppose do.

<img alt="Bot NER" src="../../../../../translated_images/bot-ner.4b09235dbb0ad2754ec1f54c8c797f902cbb0b45ac90b0cfc8287343cef8df2f.pcm.png" width="50%"/>

> Image na di author create am

But sometimes, di user fit add some parameters inside di sentence. For example, if dem dey ask about di weather, dem fit talk di location or di date. Di bot suppose sabi dose entities, and use dem fill di parameter slots before e go do di action. Na here NER go help.

> ✅ Another example na [analyzing scientific medical papers](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). One of di main things wey we dey find na specific medical terms, like diseases and medical substances. Even though small diseases fit dey easy to find with substring search, di more complex entities, like chemical compounds and medication names, go need better method.

## NER as Token Classification

NER models na **token classification models**, because for each of di input tokens, we go decide if e belong to one entity or not, and if e belong - which entity class e dey.

Make we look dis paper title:

**Tricuspid valve regurgitation** and **lithium carbonate** **toxicity** in a newborn infant.

Di entities for here na:

* Tricuspid valve regurgitation na disease (`DIS`)
* Lithium carbonate na chemical substance (`CHEM`)
* Toxicity na disease (`DIS`)

You go notice say one entity fit dey spread across plenty tokens. And, like for dis example, we need to sabi di difference between two entities wey dey follow each other. So, e dey common to use two classes for each entity - one wey go show di first token of di entity (dem dey use `B-` prefix, for **b**eginning), and another one for di continuation of di entity (`I-`, for **i**nner token). We go also use `O` as class to show all **o**ther tokens. Dis kind token tagging na wetin dem dey call [BIO tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (or IOB). If we tag di title, e go look like dis:

Token | Tag
------|-----
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Because we need to match tokens and classes one by one, we fit train di **many-to-many** neural network model wey dey show for dis picture:

![Image showing common recurrent neural network patterns.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.pcm.jpg)

> *Image na from [dis blog post](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by [Andrej Karpathy](http://karpathy.github.io/). NER token classification models na di right-most network architecture for dis picture.*

## Training NER models

Since NER model na token classification model, we fit use RNNs wey we don already sabi for dis task. For dis case, each block of di recurrent network go return di token ID. Di example notebook wey dey below go show how to train LSTM for token classification.

## ✍️ Example Notebooks: NER

Continue your learning for di notebook wey dey below:

* [NER with TensorFlow](NER-TF.ipynb)

## Conclusion

NER model na **token classification model**, wey mean say e fit dey used to do token classification. Dis na very common task for NLP, wey dey help to sabi specific entities for text like places, names, dates, and more.

## 🚀 Challenge

Complete di assignment wey dey linked below to train named entity recognition model for medical terms, then try am for another dataset.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Review & Self Study

Read di blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) and follow di Further Reading section for di article to sabi more.

## [Assignment](lab/README.md)

For di assignment for dis lesson, you go train medical entity recognition model. You fit start with training LSTM model as e dey described for dis lesson, then move to use BERT transformer model. Read [di instructions](lab/README.md) to get all di details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->