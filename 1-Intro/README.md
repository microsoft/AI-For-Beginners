# Introduction to AI

**Artificial Intelligence** is an exciting scientific discipline that studies how we can make computers exhibit intelligent behavior, e.g. do those things that human beings are good at doing.

Originally, computers were invented by [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) to operate on numbers following well-defined procedure - an algorithm. Modern computers, even though significantly more advanced than original model proposed in 19th century - still follow the same idea of controlled computations. Thus it is easy to program computer to do something if we know the exact sequence of steps that we need to do in order to achieve the goal.

![Photo of a person](images/dsh_age.png) | Defining an age of a person from his/her photograph is a task that cannot be explicitly programmed, because we do not know how we come up with a number inside our head when we do it.
----|----

There are some tasks, however, that we do not explicitly know how to solve. Consider determining the age of a person from his/her photograph. We somehow learn to do it, because we have seen many examples of people of different age, but we cannot explicitly explain how we do it, nor can we program the computer to do it. This is a exactly the kind of tasks that are of interest to **Artificial Intelligence** (AI for short).

## Weak AI vs. Strong AI

The task of solving a specific human-like problem, such as determining a person's age from a photo, can be called **Weak AI**, because we are creating a system for only one task, and not a system that can solve many tasks, as a human being. Of course, developing a generally intelligent computer system is also extremely interesting from many points of view, including philosophy of consciousness. Such system would be called **Strong AI**, or **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Definition of Intelligence. Turing Test.

One of the problems when dealing with the term **[Intelligence](https://en.wikipedia.org/wiki/Intelligence)** is that there is no clear definition of this term. One can argue that intelligence is connected to **abstract thinking**, or to **self-awareness**, but we cannot properly define it.

![Photo of a Cat](images/photo-cat.jpg) | To see the ambiguity of a term *intelligence*, try answering a question: "Is a cat intelligent?". Different people tend to give different answer to this question, as there is not universally accepted test to prove this true or not. And if you think there is - try running your cat through an IQ test...
----|----

However, when speaking about AGI we need to have some way to tell if we have created a truly intelligent system. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) proposed such a way called **[Turing Test](https://en.wikipedia.org/wiki/Turing_test)**, which also acts like a definition of intelligence. The idea of such a test is that we compare our system to something inherently intelligent - a real human being. And because any automatic comparison can be easily bypassed by a computer program - we use human interrogator. So, if a human being is unable to distinguish between a real person and a computer system in text-based dialogue - the system is considered intelligent. 

> A chat-bot [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), developed in St.Petersburg, came close to passing Turing test in 2014, but using clever personality trick. It announced upfront to be a 13-year old Ukranian boy, which would explain the lack of knowledge and some discrepancies in text. The bot convinced 30% of the judges after 5 minute dialogue, a metric that Turing believed a machines would be able to pass by 2000. However, one should understand that this does not indicate that we have created an intelligent system, or that a computer system has fooled the human interrogator - it was not a computer system, but the bot creators.

## Different Approaches to AI

If we want computer to behave like a human, we need somehow to model inside a computer our way of thinking. Consequently, we need to try to understand what makes a human being intelligent.

There are two possible approaches to this problem:

Top-down Approach (Symbolic Reasoning) | Bottom-up Approach (Neural Networks)
---------------------------------------|-------------------------------------
Modelling the way a person reasons to solve a problem. It involves extracting **knowledge** from a human being, and representing it in a computer-readable form. We also need to develop a way to model **reasoning** inside a computer. | Modelling a structure of a human brain, consisting of huge number of simplest units called **neurons**. Each neuron acts like a simple weighted average of its inputs, and we can train a network of neurons to solve useful problems by providing **training data**.

There are also some other possible approaches to intelligence that we will mention here, but the two above are the main ones.
### Top-Down Approach

In **top-down approach**, we try to model our reasoning. People tend to have some rules in their head, for example, when a doctor is diagnosing a patient, he may realize that a person has a fever, and thus there might be some inflammation going on in his body. By applying a large set of rules to a specific problem a doctor may be able to come up with the final diagnosis. 

This approach relies heavily on **knowledge representation** and **reasoning**. Extracting knowledge from a human expert might be the most difficult part, because a doctor in many cases would not know exactly why he or she is coming up with a particular diagnosis. Sometimes the solution just comes up in his/her head without explicit thinking. Some tasks, such as determining the age of a person from photograph, cannot be at all reduced to manipulating knowledge.

Another  