# บทนำสู่ AI เบื้องต้น

![โน้ตสรุปเกี่ยวกับบทนำสู่ AI เบื้องต้น](../sketchnotes/ai-intro.png)

> Sketchnote by [Tomomi Imura](https://twitter.com/girlie_mac)

## [แบบทดสอบก่อนเรียน](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/101)

**ปัญญาประดิษฐ์ (Artificial Intelligence)** เป็นสาขาวิทยาศาสตร์ที่น่าสนใจเพราะเป็นศาสตร์ที่ศึกษาว่าเราสามารถทำให้คอมพิวเตอร์แสดงพฤติกรรมอย่างสิ่งมีชีวิตที่มีปัญญาสูงได้อย่างไร เช่น เลียนแบบพฤติกรรมที่มนุษย์สามารถทำออกมาได้อย่างไม่มีข้อบกพร่อง

ว่ากันว่าตามประวัติศาสตร์แล้ว ผู้ที่คิดค้นประดิษฐ์คอมพิวเตอร์คนแรกคือ ชาร์ล แบบเบจ [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) เขาได้ออกแบบเครื่องคอมพิวเตอร์เพื่อใช้งานด้านการคำนวณตัวเลขและทำงานไปตามอัลกอริทึม ถึงแม่้ว่าคอมพิวเตอร์ในยุคปัจจุบันจะมีสมรรถภาพการทำงานที่สูงกว่าคอมพิวเตอร์ในศตวรรษที่ 19 แต่การทำงานของคอมพิวเตอร์ในยุคนี้ก็ทำงานบนหลักการพื้นฐานของหลักการทำงานของคอมพิวเตอร์ในยุคก่อน ดังนั้นถ้าหากเราวางลำดับขั้นตอนที่เราต้องทำ กำหนดขอบเขตการทำงานที่ชัดเจนเพื่อบรรลุเป้าหมายที่วางไว้ เราสามารถโปรแกรมสั่งให้คอมพิวเตอร์ให้ทำงานสิ่งนั้นให้เราได้

![Photo of a person](images/dsh_age.png)

> Photo by [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ เราไม่สามารถสั่งให้คอมพิวเตอร์กำหนดอายุของบุคคลในภาพถ่ายได้เพราะเราไม่รู้ว่าเราจะกำหนดช่วงอายุอย่างไร

---

แต่ก็ไม่ใช่ว่าเราจะรู้วิธีการหาทางออกสำหรับทุกปัญหา อย่างเช่นการกำหนดอายุของบุคคลจากรูปถ่ายบุคคล ไม่ว่าเราจะเรียนรู้วิธีการต่างๆที่เอามาใช้กำหนดช่วงอายุ แต่เราไม่สามารถอธิบายได้อย่างชัดเจนว่าเราทำได้อย่างไร ทั้งนี้ทั้งนั้นงานแบบนี้แหละที่น่าสนใจสำหรับปัญญาประดิษฐ์ **Artificial Intelligence**  (AI for short)

✅ ลองคิดดูสิว่ามีงานชนิดใดบ้างที่เราสามารถให้ปัญญาประดิษฐ์(AI)ทำแทนได้ ลองพิจารณางานด้านไฟแนนซ์ การแพทย์ ศิลปะ ดูว่าสามารถนำเอาเอไอ(AI) มาใช้งานได้อย่างไร 

## Weak AI vs. Strong AI

ปัญหาในชีวิตประจำวันของคนเรา เช่นการกำหนดอายุของบุคคลจากภาพถ่าย คืองานแบบ **Weak AI** เนื่องจากเราจะสร้างระบบสำหรับงานเพียงอย่างเดียวเท่านั้น ไม่ใช่งานสำหรับแก้ปัญหาหลายๆด้านอย่างที่คนเราทำกัน แน่นอนว่าการพัฒนาระบบคอมพิวเตอร์ที่มีความฉลาดทั่วไปนั้นเป็นเรื่องที่น่าสนใจอย่างมากจากมุมมองหลายๆ ด้าน รวมไปถึงผู้ที่ศึกษาในด้านปรัชญาชานศาสตร์(การรับรู้อารมณ์) ระบบเช่นนี้เรียกว่า **Strong AI**, หรือ **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## คำนิยามของ Intelligence และ the Turing Test

เนื่องจากเราไม่มีคำนิยามที่ตายตัวสำหรับคำว่า **[Intelligence](https://en.wikipedia.org/wiki/Intelligence)** เรื่องนี้ยังถือเป็นข้อกังขาในหลายๆด้าน บางคนอาจจะบอกว่า intelligence เชื่อมโยงกับ **abstract thinking**, หรือ **self-awareness** แต่เราก็ยังไม่สามารถหาคำนิยามดีๆที่ตายตัวมาได้อยู่ดี

![Photo of a Cat](images/photo-cat.jpg)

> [Photo](https://unsplash.com/photos/75715CVEJhI) by [Amber Kipp](https://unsplash.com/@sadmax) from Unsplash

ลองนึกหาคำตอบของคำถามที่ว่า "แมวมีสติปัญญาเฉลียวฉลาดมั้ย" แล้วจะพอนึกออกว่าทำไม *intelligence* ถึงไม่มีความหมายที่แน่นอน เพราะต่างคนก็ให้คำนิยามออกมาต่างกันและเราก็ไม่มีบททดสอบที่ตายตัวเพื่อที่จะชี้วัดคำนิยามเหล่านั้น แต่ถ้าคุณอยากจะลองให้แมวทำแบบทดสอบไอคิวดูละก็...

✅ ลองคิดเล่นๆดูว่าคุณจะสามารถนิยามคำว่า intelligence ได้ยังไง ถ้าหากนกกาสามารถแก้ปัญหาเชาว์ได้และได้อาหารเป็นรางวัลตอบแทน แบบนี้นกกาฉลาดรึเปล่า แล้วเด็กทารกละฉลาดมั้ย  

---

When speaking about AGI we need to have some way to tell if we have created a truly intelligent system. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) proposed a way called a **[Turing Test](https://en.wikipedia.org/wiki/Turing_test)**, which also acts like a definition of intelligence. The test compares a given system to something inherently intelligent - a real human being, and because any automatic comparison can be bypassed by a computer program, we use a human interrogator. So, if a human being is unable to distinguish between a real person and a computer system in text-based dialogue - the system is considered intelligent.

> A chat-bot called [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), developed in St.Petersburg, came close to passing the Turing test in 2014 by using a clever personality trick. It announced up front that it was a 13-year old Ukrainian boy, which would explain the lack of knowledge and some discrepancies in the text. The bot convinced 30% of the judges that it was human after a 5 minute dialogue, a metric that Turing believed a machine would be able to pass by 2000. However, one should understand that this does not indicate that we have created an intelligent system, or that a computer system has fooled the human interrogator - the system didn't fool the humans, but rather the bot creators did!

✅ Have you ever been fooled by a chat bot into thinking that you are speaking to a human? How did it convince you?

## Different Approaches to AI

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
