<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-31T17:31:00+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "en"
}
-->
# Multi-Agent Systems

One way to achieve intelligence is through the **emergent** (or **synergetic**) approach, which relies on the idea that the combined behavior of many relatively simple agents can lead to more complex (or intelligent) behavior in the system as a whole. This concept is theoretically grounded in principles like [Collective Intelligence](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain), and [Evolutionary Cybernetics](https://en.wikipedia.org/wiki/Global_brain). These principles suggest that higher-level systems gain added value when properly composed of lower-level systems (known as the *principle of metasystem transition*).

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

The field of **Multi-Agent Systems** emerged in AI during the 1990s as a response to the growth of the Internet and distributed systems. One of the classic AI textbooks, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), explores classical AI from the perspective of Multi-Agent Systems.

At the core of the Multi-Agent approach is the concept of an **Agent**—an entity that exists in an **environment**, which it can perceive and act upon. This is a broad definition, and agents can be classified in various ways:

* Based on their reasoning capabilities:
   - **Reactive** agents exhibit simple request-response behavior.
   - **Deliberative** agents use logical reasoning and/or planning capabilities.
* Based on where the agent executes its code:
   - **Static** agents operate on a fixed network node.
   - **Mobile** agents can move their code between network nodes.
* Based on their behavior:
   - **Passive agents** lack specific goals. They can respond to external stimuli but do not initiate actions.
   - **Active agents** pursue specific goals.
   - **Cognitive agents** engage in complex planning and reasoning.

Multi-Agent Systems are now applied in various fields:

* In games, many non-player characters use AI and can be considered intelligent agents.
* In video production, rendering complex 3D scenes with crowds often involves multi-agent simulations.
* In systems modeling, multi-agent approaches simulate the behavior of complex models. For instance, they have been used to predict the global spread of COVID-19. Similar methods can model city traffic and analyze the impact of changes in traffic rules.
* In complex automation systems, each device can act as an independent agent, making the system less monolithic and more robust.

We won’t delve deeply into Multi-Agent Systems but will explore one example of **Multi-Agent Modeling**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) is a multi-agent modeling environment based on a modified version of the [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programming language. Logo was originally developed to teach programming concepts to children, allowing them to control an agent called a **turtle** that moves and leaves a trace behind. This enables the creation of complex geometric figures, providing a visual way to understand agent behavior.

In NetLogo, you can create multiple turtles using the `create-turtles` command. You can then instruct all turtles to perform actions (e.g., move forward by 10 points in the example below):

```
create-turtles 10
ask turtles [
  forward 10
]
```

It becomes more interesting when turtles perform different actions. You can use the `ask` command to target specific groups of turtles, such as those near a certain point. You can also create turtles of different *breeds* using the `breed [cats cat]` command. Here, `cat` is the breed name, and both singular and plural forms are specified for clarity in different commands.

> ✅ We won’t focus on learning the NetLogo language itself—you can explore the excellent [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) if you’re interested in learning more.

You can [download](https://ccl.northwestern.edu/netlogo/download.shtml) and install NetLogo to try it out.

### Models Library

One of NetLogo’s strengths is its library of ready-to-use models. Navigate to **File → Models Library** to explore various categories of models.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Screenshot of the models library by Dmitry Soshnikov

You can open a model, such as **Biology → Flocking**.

### Main Principles

When you open a model, you’ll see the main NetLogo screen. Here’s an example model that simulates the population of wolves and sheep, given finite resources (grass).

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.en.png)

> Screenshot by Dmitry Soshnikov

On this screen, you’ll find:

* The **Interface** section, which includes:
  - The main field where agents live.
  - Various controls like buttons and sliders.
  - Graphs to display simulation parameters.
* The **Code** tab, which contains the editor for writing NetLogo programs.

Typically, the interface includes a **Setup** button to initialize the simulation state and a **Go** button to start execution. These are handled by corresponding code handlers, which look like this:

```
to go [
...
]
```

NetLogo’s world consists of the following objects:

* **Agents** (turtles) that move across the field and perform actions. You can command agents using the `ask turtles [...]` syntax, where the code in brackets runs in *turtle mode*.
* **Patches**, which are square areas of the field where agents reside. You can reference all agents on a patch, change patch properties like color, or use `ask patches` to perform actions.
* **Observer**, a unique agent that controls the world. Button handlers execute in *observer mode*.

> ✅ The beauty of a multi-agent environment is that code running in turtle mode or patch mode executes simultaneously for all agents in parallel. By programming the behavior of individual agents, you can create complex system-wide behavior.

### Flocking

An example of multi-agent behavior is **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**, a pattern resembling how birds fly in flocks. Watching them, you might think they follow a collective algorithm or possess *collective intelligence*. However, this complex behavior arises when each bird observes nearby agents and follows three simple rules:

* **Alignment**: Steer toward the average heading of neighbors.
* **Cohesion**: Move toward the average position of neighbors (*long-range attraction*).
* **Separation**: Move away when too close to others (*short-range repulsion*).

You can run the flocking example and observe the behavior. Adjust parameters like *separation degree* or *viewing range* (how far each bird can see). For instance, reducing the viewing range to 0 makes birds blind, stopping flocking. Reducing separation to 0 causes birds to form a straight line.

> ✅ Switch to the **Code** tab to see how the three flocking rules (alignment, cohesion, and separation) are implemented. Note how only nearby agents are referenced.

### Other Models to Explore

Here are some other interesting models to experiment with:

* **Art → Fireworks**: Simulates fireworks as collective behavior of individual fire streams.
* **Social Science → Traffic Basic** and **Social Science → Traffic Grid**: Models city traffic in 1D and 2D grids, with or without traffic lights. Each car follows rules like:
   - Accelerate if the space ahead is empty (up to a max speed).
   - Brake if an obstacle is visible (adjustable visibility range).
* **Social Science → Party**: Simulates how people group together at a cocktail party. Experiment with parameters to maximize group happiness.

These examples demonstrate how multi-agent simulations help understand complex systems composed of individuals following similar logic. They can also control virtual agents, such as [NPCs](https://en.wikipedia.org/wiki/NPC) in games or agents in 3D animated worlds.

## Deliberative Agents

The agents discussed so far are simple, reacting to environmental changes using algorithms. These are **reactive agents**. However, some agents can reason and plan actions, making them **deliberative**.

For example, a personal agent tasked with booking a vacation tour might interact with other agents online to check flight availability, hotel prices, and negotiate the best deal. Once the plan is confirmed, it proceeds with booking.

To achieve this, agents need to **communicate**. Successful communication requires:

* **Standard languages for knowledge exchange**, such as [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) and [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML), based on [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* **Negotiation protocols**, often based on different **auction types**.
* A **common ontology** to ensure shared understanding of concepts and semantics.
* A way to **discover** agent capabilities, also ontology-based.

Deliberative agents are more complex than reactive ones because they don’t just react—they also *initiate* actions. One proposed architecture for deliberative agents is the Belief-Desire-Intention (BDI) model:

* **Beliefs**: Knowledge about the environment, structured as a knowledge base or rules.
* **Desires**: Goals the agent wants to achieve (e.g., booking a tour or maximizing profit).
* **Intentions**: Specific actions planned to achieve goals, often involving environmental changes or communication.

Platforms like [JADE](https://jade.tilab.com/) support building multi-agent systems. [This paper](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) reviews multi-agent platforms, their history, and usage scenarios.

## Conclusion

Multi-Agent Systems take various forms and are applied in diverse fields. They focus on simple individual agent behavior, achieving complex system-wide behavior through **synergetic effects**.

## 🚀 Challenge

Apply this lesson to real-world scenarios. Conceptualize a multi-agent system to solve a problem. For instance, how could a multi-agent system optimize school bus routes? Or how could it function in a bakery?

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Review & Self Study

Explore how this type of system is used in industry. Choose a domain like manufacturing or video games and investigate how multi-agent systems solve unique challenges.

## [NetLogo Assignment](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.