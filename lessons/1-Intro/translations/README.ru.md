# Введение в искусственный интеллект(ИИ)

![Краткое введение в ИИ](../sketchnotes/ai-intro.png)

> Рисунок [Tomomi Imura](https://twitter.com/girlie_mac)

## [Предварительное тестирование](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/101)

**Искусственный интеллект(ИИ)** - научная дисциплина, которая занимается изучением того, как мы можем заставить компьютер 
вести себя разумно т.е как человек.


Изначально компьютер был изобретён [Чарльзом Бэббиджем](https://en.wikipedia.org/wiki/Charles_Babbage) для обработки чисел 
по определённому алгоритму. Современные компьютеры гораздо мощнее, но в их основе лежат те же идеи, что и в 19 веке. 
Мы можем запрограммировать компьютер для выполнения какой-либо задачи если знаем шаги, которые необходимо выполнить для её решения.

![Фото человека](images/dsh_age.png)

> Фото [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Определение возраста человека по фото - задача, которая не может быть явно запрограммирована т.к. мы не может чётко
> описать каким образом наш мозг генерирует предполагаемый возраст.

---

Есть ряд задач, которые не имеют какого-то явного алгоритма решения. Хороший пример такой задачи - определение возраста по фото. Мы можем определить возраст по фото т.к. ранее видели множество людей различных возрастов, но мы не можем запрограммировать то, как мы это делаем.
Это именно тот класс задач на которые ориентированы ИИ.

✅ Подумайте о задачах, которые Вы могли бы передать ИИ. Как применяется ИИ в таких областях как медицина, финансы, искусство?

## Слабый ИИ vs. Сильный ИИ

Слабым ИИ называется ИИ, созданный для решения одной конкретной задачи. Сильным ИИ же называется ИИ, разработанный для решения множества задач.
Разработка ИИ интересна с многих точек зрения, в том числе философии сознания.

## Определение интеллекта и тест Тьюринга

Одной из проблем, связанных с термином **[интеллект](https://en.wikipedia.org/wiki/Intelligence)**, является то, что нет чёткого определения этого термина.
Можно утверждать, что интеллект связан с **абстрактным мышлением** или **самосознанием**, но мы не можем дать им чёткого определения.

![Фото кота](images/photo-cat.jpg)

> [Фото](https://unsplash.com/photos/75715CVEJhI)  [Amber Kipp](https://unsplash.com/@sadmax) с Unsplash

Чтобы понять неоднозначность термина *интеллект*, ответьте на простой вопрос:"Обладает ли кошка интеллектом?". Разные люди дадут разный ответ на этот вопрос.
Нет универсального способа наличие у кошек интеллекта. Если вы считаете иначе, то можете дать кошке пройти IQ тест...

✅ Задумайтесь на минуту о том, что такое интеллект. Обладает ли интеллектом ворона, проходящая лабиринт чтобы получить еду?
Обладает ли интеллектом ребёнок?

---

Когда мы говорим о сильном ИИ, то подразумевает настоящие интеллектуальные системы. [Алан Тьюринг](https://en.wikipedia.org/wiki/Alan_Turing) предложил способ, который сейчас называется **[тестом Тьюринга](https://en.wikipedia.org/wiki/Turing_test)**, 
который может использоваться для определения наличия интеллекта. В данном тесте проводится сравнение с существом, обладающим интеллектом - с человеком. Смысл теста очень прост - если человек, в рамках переписки, не может отличить компьютерную систему от реального человека, то система считается разумной.


> Чат бот [Женя Густман](https://en.wikipedia.org/wiki/Eugene_Goostman), разработанный в Санкт-Петербурге, в 2014 году, был близок к прохождению теста Тьюринга благодаря использованию небольшой уловки - он представлялся 13-летним ребёнком из Украины. Данная уловка позволяла объяснить недостаток знаний и проблемы с сообщениями. Бот, после 5 минут диалога, смог убедить 30% судей. Тьюринг предполагал, что такого результата компьютерные системы достигнут уже в 2000 году. Стоит понимать, что данный случай не доказывает, что мы создали ИИ. В данном случае, разработчики бота просто ввели людей в заблуждение.

✅ Чат бот когда-нибудь заставлял вас думать, что вы общаетесь с человеком? Как ему это удалось?

## Различные подходы к ИИ

If we want a computer to behave like a human, we need somehow to model inside a computer our way of thinking. Consequently, we need to try to understand what makes a human being intelligent.

> To be able to program intelligence into a machine, we need to understand how our own processes of making decisions work. If you do a little self-introspection, you will realize that there are some processes that happen subconsciously – eg. we can distinguish a cat from a dog without thinking about it - while some others involve reasoning.

There are two possible approaches to this problem:

Top-down Approach (Symbolic Reasoning) | Bottom-up Approach (Neural Networks)
---------------------------------------|-------------------------------------
A top-down approach models the way a person reasons to solve a problem. It involves extracting **knowledge** from a human being, and representing it in a computer-readable form. We also need to develop a way to model **reasoning** inside a computer. | A bottom-up approach models the structure of a human brain, consisting of huge number of simple units called **neurons**. Each neuron acts like a weighted average of its inputs, and we can train a network of neurons to solve useful problems by providing **training data**.

There are also some other possible approaches to intelligence:

* An **Emergent**, **Synergetic** or **multi-agent approach** are based on the fact that complex intelligent behaviour can be obtained by an interaction of a large number of simple agents. According to [evolutionary cybernetics](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), intelligence can *emerge* from more simple, reactive behaviour in the process of *metasystem transition*.

* An **Evolutionary approach**, or **genetic algorithm** is an optimization process based on the principles of evolution.

We will consider those approaches later in the course, but right now we will focus on two main directions: top-down and bottom-up.

### The Top-Down Approach

In a **top-down approach**, we try to model our reasoning.  Because we can follow our thoughts when we reason, we can try to formalize this process and program it inside the computer. This is called **symbolic reasoning**.

People tend to have some rules in their head that guide their decision making processes. For example, when a doctor is diagnosing a patient, he or she may realize that a person has a fever, and thus there might be some inflammation going on inside the body. By applying a large set of rules to a specific problem a doctor may be able to come up with the final diagnosis.

This approach relies heavily on **knowledge representation** and **reasoning**. Extracting knowledge from a human expert might be the most difficult part, because a doctor in many cases would not know exactly why he or she is coming up with a particular diagnosis. Sometimes the solution just comes up in his or her head without explicit thinking. Some tasks, such as determining the age of a person from a photograph, cannot be at all reduced to manipulating knowledge.

### Bottom-Up Approach

Alternately, we can try to model the simplest elements inside our brain – a neuron. We can construct a so-called **artificial neural network** inside a computer, and then try to teach it to solve problems by giving it examples. This process is similar to how a newborn child learns about his or her surroundings by making observations.

✅ Do a little research on how babies learn. What are the basic elements of a baby's brain?

> | What about ML?         |      |
> |--------------|-----------|
> | Part of Artificial Intelligence that is based on computer learning to solve a problem based on some data is called **Machine Learning**. We will not consider classical machine learning in this course - we refer you to a separate [Machine Learning for Beginners](http://aka.ms/ml-beginners) curriculum. |   ![ML for Beginners](images/ml-for-beginners.png)    |

## A Brief History of AI

Artificial Intelligence was started as a field in the middle of the twentieth century. Initially, symbolic reasoning was a prevalent approach, and it led to a number of important successes, such as expert systems – computer programs that were able to act as an expert in some limited problem domains. However, it soon became clear that such approach does not scale well. Extracting the knowledge from an expert, representing it in a computer, and keeping that knowledgebase accurate turns out to be a very complex task, and too expensive to be practical in many cases. This led to so-called [AI Winter](https://en.wikipedia.org/wiki/AI_winter) in the 1970s.

<img alt="Brief History of AI" src="images/history-of-ai.png" width="70%"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

As time passed, computing resources became cheaper, and more data has become available, so neural network approaches started demonstrating great performance in competing with human beings in many areas, such as computer vision or speech understanding. In the last decade, the term Artificial Intelligence has been mostly used as a synonym for Neural Networks, because most of the AI successes that we hear about are based on them.

We can observe how the approaches changed, for example, in creating a chess playing computer program:

* Early chess programs were based on search – a program explicitly tried to estimate possible moves of an opponent for a given number of next moves, and selected an optimal move based on the optimal position that can be achieved in a few moves. It led to the development of the so-called [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) search algorithm.
* Search strategies work well toward the end of the game, where the search space is limited by a small number of possible moves. However, at the beginning of the game, the search space is huge, and the algorithm can be improved by learning from existing matches between human players. Subsequent experiments employed so-called [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), where the program looked for cases in the knowledge base very similar to the current position in the game.
* Modern programs that win over human players are based on neural networks and [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), where the programs learn to play solely by playing a long time against themselves and learning from their own mistakes – much like human beings do when learning to play chess. However, a computer program can play many more games in much less time, and thus can learn much faster.

✅ Do a little research on other games that have been played by AI.

Similarly, we can see how the approach towards creating “talking programs” (that might pass the Turing test) changed:

* Early programs of this kind such as [Eliza](https://en.wikipedia.org/wiki/ELIZA), were based on very simple grammatical rules and the re-formulation of the input sentence into a question.
* Modern assistants, such as Cortana, Siri or Google Assistant are all hybrid systems that use Neural networks to convert speech into text and recognize our intent, and then employ some reasoning or explicit algorithms to perform required actions.
* In the future, we may expect a complete neural-based model to handle dialogue by itself. The recent GPT and [Turing-NLG](https://turing.microsoft.com/) family of neural networks show great success in this.

<img alt="the Turing test's evolution" src="images/turing-test-evol.png" width="70%"/>

> Image by Dmitry Soshnikov, [photo](https://unsplash.com/photos/r8LmVbUKgns) by [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Recent AI Research

The huge recent growth in neural network research started around 2010, when large public datasets started to become available. A huge collection of images called [ImageNet](https://en.wikipedia.org/wiki/ImageNet), which contains around 14 million annotated images, gave birth to the [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Accuracy](images/ilsvrc.gif)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

In 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) were first used in image classification, which led to a significant drop in classification errors (from almost 30% to 16.4%). In 2015, ResNet architecture from Microsoft Research [achieved human-level accuracy](https://doi.org/10.1109/ICCV.2015.123).

Since then, Neural Networks demonstrated very successful behaviour in many tasks:

---

Year | Human Parity achieved
-----|--------
2015 | [Image Classification](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Conversational Speech Recognition](https://arxiv.org/abs/1610.05256)
2018 | [Automatic Machine Translation](https://arxiv.org/abs/1803.05567) (Chinese-to-English)
2020 | [Image Captioning](https://arxiv.org/abs/2009.13682)

Over the past few years we have witnessed huge successes with large language models, such as BERT and GPT-3. This happened mostly due to the fact that there is a lot of general text data available that allows us to train models to capture the structure and meaning of texts, pre-train them on general text collections, and then specialize those models for more specific tasks. We will learn more about [Natural Language Processing](../5-NLP/README.md) later in this course.

## 🚀 Challenge

Do a tour of the internet to determine where, in your opinion, AI is most effectively used. Is it in a Mapping app, or some speech-to-text service or a video game? Research how the system was built.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Review & Self Study

Review the history of AI and ML by reading through [this lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Take an element from the sketchnote at the top of that lesson or this one and research it in more depth to understand the cultural context informing its evolution.

**Assignment**: [Game Jam](assignment.md)
