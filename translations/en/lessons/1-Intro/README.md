<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f57e8aa46141fd220b16ffed8f11aec7",
  "translation_date": "2025-11-18T20:28:55+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "en"
}
-->
# Introduction to AI

![Summary of Introduction of AI content in a doodle](../../../../translated_images/en/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.png)

> Sketchnote by [Tomomi Imura](https://twitter.com/girlie_mac)

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Artificial Intelligence** is an exciting scientific field that explores how computers can exhibit intelligent behavior, such as performing tasks that humans excel at.

Originally, computers were invented by [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) to process numbers using a well-defined procedure—an algorithm. Modern computers, while far more advanced than Babbage's 19th-century model, still operate on the same principle of controlled computations. This means we can program a computer to perform a task if we know the exact sequence of steps required to achieve the goal.

![Photo of a person](../../../../translated_images/en/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.png)

> Photo by [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Determining a person's age from their photograph is a task that cannot be explicitly programmed, as we don't fully understand how we arrive at the number in our minds when we do it.

---

Some tasks, however, cannot be explicitly solved. For example, estimating a person's age from their photograph. We learn to do this by observing many examples of people of different ages, but we can't explain the process or program a computer to do it. These types of tasks are the focus of **Artificial Intelligence** (AI).

✅ Think of tasks you could delegate to a computer that would benefit from AI. Consider fields like finance, medicine, and the arts—how are these areas benefiting from AI today?

## Weak AI vs. Strong AI

Weak AI | Strong AI
---------------------------------------|-------------------------------------
Weak AI refers to AI systems designed and trained for specific tasks or a narrow set of tasks.|Strong AI, or Artificial General Intelligence (AGI), refers to AI systems with human-level intelligence and understanding.
These AI systems are not generally intelligent; they excel at performing predefined tasks but lack true understanding or consciousness.|These AI systems can perform any intellectual task a human can, adapt to different domains, and possess a form of consciousness or self-awareness.
Examples of weak AI include virtual assistants like Siri or Alexa, recommendation algorithms used by streaming services, and chatbots designed for specific customer service tasks.|Achieving Strong AI is a long-term goal of AI research and would require developing systems capable of reasoning, learning, understanding, and adapting across diverse tasks and contexts.
Weak AI is highly specialized and lacks human-like cognitive abilities or general problem-solving capabilities beyond its narrow domain.|Strong AI is currently a theoretical concept, and no AI system has reached this level of general intelligence.

For more information, refer to **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## The Definition of Intelligence and the Turing Test

One challenge in discussing **[Intelligence](https://en.wikipedia.org/wiki/Intelligence)** is the lack of a clear definition. Some argue intelligence is linked to **abstract thinking** or **self-awareness**, but it remains difficult to define.

![Photo of a Cat](../../../../translated_images/en/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.jpg)

> [Photo](https://unsplash.com/photos/75715CVEJhI) by [Amber Kipp](https://unsplash.com/@sadmax) from Unsplash

To illustrate the ambiguity of the term *intelligence*, consider the question: "Is a cat intelligent?" People often give different answers, as there is no universally accepted test to prove or disprove the assertion. And if you think there is—try giving your cat an IQ test...

✅ Take a moment to think about how you define intelligence. Is a crow that can solve a maze to access food intelligent? Is a child intelligent?

---

When discussing AGI, we need a way to determine if we've created a truly intelligent system. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) proposed the **[Turing Test](https://en.wikipedia.org/wiki/Turing_test)**, which also serves as a definition of intelligence. The test compares a system to something inherently intelligent—a human being. Since automatic comparisons can be bypassed by computer programs, a human interrogator is used. If the interrogator cannot distinguish between a human and a computer system in a text-based dialogue, the system is considered intelligent.

> A chatbot called [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), developed in St. Petersburg, came close to passing the Turing Test in 2014 by using a clever personality trick. It claimed to be a 13-year-old Ukrainian boy, which explained its lack of knowledge and some inconsistencies in its responses. The bot convinced 30% of the judges it was human after a 5-minute dialogue—a metric Turing predicted machines would achieve by 2000. However, this does not mean we've created an intelligent system or that the computer fooled the human interrogator—the bot creators fooled the humans, not the system itself!

✅ Have you ever been tricked by a chatbot into thinking you were speaking to a human? How did it convince you?

## Different Approaches to AI

To make a computer behave like a human, we need to model human thinking within the computer. This requires understanding what makes humans intelligent.

> To program intelligence into a machine, we need to understand how we make decisions. Through introspection, you'll notice some processes happen subconsciously—e.g., distinguishing a cat from a dog without deliberate thought—while others involve reasoning.

There are two main approaches to this problem:

Top-down Approach (Symbolic Reasoning) | Bottom-up Approach (Neural Networks)
---------------------------------------|-------------------------------------
The top-down approach models how humans reason to solve problems. It involves extracting **knowledge** from humans and representing it in a computer-readable format. It also requires developing methods to model **reasoning** within a computer. | The bottom-up approach models the structure of the human brain, consisting of numerous simple units called **neurons**. Each neuron acts as a weighted average of its inputs, and a network of neurons can be trained to solve problems using **training data**.

Other approaches to intelligence include:

* **Emergent**, **Synergetic**, or **multi-agent approaches** rely on the idea that complex intelligent behavior can arise from the interaction of many simple agents. According to [evolutionary cybernetics](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), intelligence can *emerge* from simpler, reactive behaviors during a process called *metasystem transition*.

* **Evolutionary approaches**, or **genetic algorithms**, are optimization processes based on evolutionary principles.

We will explore these approaches later in the course, but for now, we'll focus on the two main directions: top-down and bottom-up.

### The Top-Down Approach

In the **top-down approach**, we aim to model human reasoning. Since we can follow our thoughts while reasoning, we can formalize this process and program it into a computer. This is known as **symbolic reasoning**.

Humans often use rules to guide their decision-making processes. For instance, a doctor diagnosing a patient might observe that the person has a fever, suggesting inflammation in the body. By applying a large set of rules to a specific problem, the doctor can arrive at a diagnosis.

This approach heavily depends on **knowledge representation** and **reasoning**. Extracting knowledge from human experts can be challenging, as they may not always know why they arrive at a particular conclusion. Sometimes, solutions simply come to mind without explicit reasoning. Certain tasks, like estimating a person's age from a photograph, cannot be reduced to manipulating knowledge.

### Bottom-Up Approach

Alternatively, we can model the simplest elements of the human brain—a neuron. By constructing an **artificial neural network** in a computer, we can teach it to solve problems using examples. This process resembles how a newborn learns about their surroundings through observation.

✅ Research how babies learn. What are the basic elements of a baby's brain?

> | What about ML?         |      |
> |--------------|-----------|
> | Part of Artificial Intelligence that involves computers learning to solve problems using data is called **Machine Learning**. This course does not cover classical machine learning—we recommend the separate [Machine Learning for Beginners](http://aka.ms/ml-beginners) curriculum. |   ![ML for Beginners](../../../../translated_images/en/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.png)    |

## A Brief History of AI

Artificial Intelligence emerged as a field in the mid-20th century. Initially, symbolic reasoning was the dominant approach, leading to significant achievements like expert systems—programs capable of acting as experts in specific domains. However, this approach proved difficult to scale. Extracting knowledge from experts, representing it in a computer, and maintaining an accurate knowledge base became too complex and costly for many applications, leading to the [AI Winter](https://en.wikipedia.org/wiki/AI_winter) in the 1970s.

<img alt="Brief History of AI" src="../../../../translated_images/en/history-of-ai.7e83efa70b537f5a0264357672b0884cf3a220fbafe35c65d70b2c3805f7bf5e.png" width="70%"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

As computing resources became cheaper and more data became available, neural network approaches began to outperform humans in areas like computer vision and speech recognition. Over the last decade, the term Artificial Intelligence has become synonymous with Neural Networks, as most AI successes are based on them.

The evolution of approaches can be seen in chess-playing programs:

* Early chess programs relied on search algorithms, estimating possible moves for a given number of steps and selecting the optimal move based on the best achievable position. This led to the development of the [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) algorithm.
* Search strategies worked well in the endgame, where the search space was limited. However, in the opening, the search space was vast, and the algorithm improved by learning from human matches. Later experiments used [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), where the program searched for similar cases in its knowledge base.
* Modern programs that outperform humans use neural networks and [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), learning to play by competing against themselves and learning from mistakes—similar to how humans learn chess. Computers, however, can play far more games in less time, enabling faster learning.

✅ Research other games played by AI.

Similarly, the evolution of "talking programs" (potentially passing the Turing Test) can be observed:

* Early programs like [Eliza](https://en.wikipedia.org/wiki/ELIZA) used simple grammatical rules and reformulated input sentences into questions.
* Modern assistants like Cortana, Siri, and Google Assistant are hybrid systems, using neural networks to convert speech to text, recognize intent, and employ reasoning or algorithms to perform tasks.
* Future systems may rely entirely on neural models to handle dialogue. Recent neural networks like GPT and [Turing-NLG](https://www.microsoft.com/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft) have shown remarkable progress.

<img alt="the Turing test's evolution" src="../../../../translated_images/en/turing-test-evol.4184696701293ead6de6e6441a659c62f0b119b342456987f531005f43be0b6d.png" width="70%"/>
> Image by Dmitry Soshnikov, [photo](https://unsplash.com/photos/r8LmVbUKgns) by [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Recent AI Research

The significant surge in neural network research began around 2010, when large public datasets became accessible. A massive collection of images called [ImageNet](https://en.wikipedia.org/wiki/ImageNet), containing approximately 14 million annotated images, led to the creation of the [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Accuracy](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

In 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) were first applied to image classification, resulting in a significant reduction in classification errors (from nearly 30% to 16.4%). By 2015, Microsoft's ResNet architecture [achieved human-level accuracy](https://doi.org/10.1109/ICCV.2015.123).

Since then, Neural Networks have shown remarkable success in various tasks:

---

Year | Human Parity Achieved
-----|--------
2015 | [Image Classification](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Conversational Speech Recognition](https://arxiv.org/abs/1610.05256)
2018 | [Automatic Machine Translation](https://arxiv.org/abs/1803.05567) (Chinese-to-English)
2020 | [Image Captioning](https://arxiv.org/abs/2009.13682)

In recent years, we have seen tremendous advancements with large language models like BERT and GPT-3. This progress is largely due to the abundance of general text data, which enables training models to understand the structure and meaning of text. These models are pre-trained on broad text collections and later fine-tuned for specific tasks. We will explore more about [Natural Language Processing](../5-NLP/README.md) later in this course.

## 🚀 Challenge

Explore the internet to identify where, in your opinion, AI is being used most effectively. Is it in a mapping application, a speech-to-text service, or a video game? Investigate how the system was developed.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Review & Self Study

Review the history of AI and ML by going through [this lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Choose an element from the sketchnote at the beginning of that lesson or this one, and research it further to understand the cultural context behind its development.

**Assignment**: [Game Jam](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->