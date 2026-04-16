<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "38a1185ae3d54b180378bbd71ae3ef16",
  "translation_date": "2025-09-23T11:43:13+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "en"
}
-->
# Multi-Agent Systems

One possible way to achieve intelligence is through the **emergent** (or **synergetic**) approach, which is based on the idea that the combined behavior of many relatively simple agents can result in a more complex (or intelligent) behavior of the system as a whole. Theoretically, this is grounded in the principles of [Collective Intelligence](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain), and [Evolutionary Cybernetics](https://en.wikipedia.org/wiki/Global_brain), which suggest that higher-level systems gain added value when properly composed of lower-level systems (the so-called *principle of metasystem transition*).

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

The field of **Multi-Agent Systems** emerged in AI during the 1990s as a response to the growth of the Internet and distributed systems. One of the classical AI textbooks, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), explores classical AI from the perspective of Multi-Agent Systems.

At the core of the Multi-Agent approach is the concept of an **Agent**—an entity that exists in an **environment**, which it can perceive and act upon. This is a broad definition, and there are many types and classifications of agents:

* Based on their reasoning ability:
   - **Reactive** agents typically exhibit simple request-response behavior.
   - **Deliberative** agents use some form of logical reasoning and/or planning.
* Based on where the agent executes its code:
   - **Static** agents operate on a dedicated network node.
   - **Mobile** agents can move their code between network nodes.
* Based on their behavior:
   - **Passive agents** lack specific goals. They can react to external stimuli but do not initiate actions on their own.
   - **Active agents** pursue specific goals.
   - **Cognitive agents** involve complex planning and reasoning.

Multi-Agent Systems are now used in a variety of applications:

* In games, many non-player characters use some form of AI and can be considered intelligent agents.
* In video production, rendering complex 3D scenes involving crowds is often done using multi-agent simulations.
* In systems modeling, the multi-agent approach is used to simulate the behavior of complex models. For instance, it has been successfully applied to predict the global spread of COVID-19. A similar approach can model city traffic and analyze the impact of changes in traffic rules.
* In complex automation systems, each device can act as an independent agent, making the entire system less monolithic and more robust.

We won’t delve deeply into multi-agent systems but will explore one example of **Multi-Agent Modeling**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) is a multi-agent modeling environment based on a modified version of the [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programming language. Logo was originally developed to teach programming concepts to children and allows you to control an agent called a **turtle**, which can move and leave a trail behind. This makes it possible to create complex geometric figures, providing a visual way to understand agent behavior.

In NetLogo, you can create multiple turtles using the `create-turtles` command. You can then instruct all turtles to perform actions (e.g., move forward by 10 steps in the example below):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Of course, it’s not very interesting if all turtles do the same thing, so you can use `ask` to command specific groups of turtles, such as those near a certain point. You can also create turtles of different *breeds* using the `breed [cats cat]` command. Here, `cat` is the name of the breed, and both singular and plural forms are specified for clarity in different commands.

> ✅ We won’t focus on learning the NetLogo language itself—you can explore the excellent [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) if you’re interested in learning more.

You can [download](https://ccl.northwestern.edu/netlogo/download.shtml) and install NetLogo to try it out.

### Models Library

One of the great features of NetLogo is its library of working models that you can experiment with. Go to **File &rightarrow; Models Library**, and you’ll find many categories of models to explore.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Screenshot of the models library by Dmitry Soshnikov

You can open one of the models, such as **Biology &rightarrow; Flocking**.

### Main Principles

After opening a model, you’ll see the main NetLogo screen. Here’s an example model that simulates the population of wolves and sheep, given finite resources (grass).

![NetLogo Main Screen](../../../../../translated_images/en/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.png)

> Screenshot by Dmitry Soshnikov

On this screen, you’ll find:

* The **Interface** section, which includes:
  - The main field where all agents live.
  - Various controls: buttons, sliders, etc.
  - Graphs to display simulation parameters.
* The **Code** tab, which contains the editor where you can write NetLogo programs.

Most interfaces include a **Setup** button to initialize the simulation state and a **Go** button to start execution. These are handled by corresponding handlers in the code, which look like this:

```
to go [
...
]
```

NetLogo’s world consists of the following objects:

* **Agents** (turtles) that move across the field and perform actions. You can command agents using the `ask turtles [...]` syntax, where the code in brackets is executed by all agents in *turtle mode*.
* **Patches**, which are square areas of the field where agents live. You can refer to all agents on a patch, change patch colors, and modify other properties. You can also `ask patches` to perform actions.
* **Observer**, a unique agent that controls the world. All button handlers are executed in *observer mode*.

> ✅ The beauty of a multi-agent environment is that code running in turtle mode or patch mode is executed simultaneously by all agents in parallel. By writing a small amount of code to define individual agent behavior, you can create complex system-wide behavior.

### Flocking

As an example of multi-agent behavior, let’s look at **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking is a complex pattern resembling how flocks of birds fly. Watching them, you might think they follow a collective algorithm or possess some form of *collective intelligence*. However, this complex behavior arises when each individual agent (a *bird* in this case) observes nearby agents and follows three simple rules:

* **Alignment** - Steer toward the average heading of neighboring agents.
* **Cohesion** - Steer toward the average position of neighbors (*long-range attraction*).
* **Separation** - Move away when too close to other birds (*short-range repulsion*).

You can run the flocking example and observe the behavior. Adjust parameters like *degree of separation* or *viewing range*, which defines how far each bird can see. Note that if you reduce the viewing range to 0, all birds become blind, and flocking stops. If you reduce separation to 0, all birds cluster into a straight line.

> ✅ Switch to the **Code** tab to see where the three flocking rules (alignment, cohesion, and separation) are implemented. Notice how the code refers only to agents within sight.

### Other Models to Explore

Here are a few more interesting models to experiment with:

* **Art &rightarrow; Fireworks** demonstrates how fireworks can be seen as the collective behavior of individual fire streams.
* **Social Science &rightarrow; Traffic Basic** and **Social Science &rightarrow; Traffic Grid** simulate city traffic in 1D and 2D grids, with or without traffic lights. Each car in the simulation follows these rules:
   - Accelerate if the space ahead is clear (up to a maximum speed).
   - Brake if an obstacle is detected ahead (adjustable based on how far the driver can see).
* **Social Science &rightarrow; Party** models how people group together at a cocktail party. Experiment with parameters to find the combination that maximizes group happiness.

These examples show how multi-agent simulations can help us understand the behavior of complex systems made up of individuals following similar logic. They can also be used to control virtual agents, such as [NPCs](https://en.wikipedia.org/wiki/NPC) in video games or agents in 3D animated worlds.

## Deliberative Agents

The agents described above are simple and react to environmental changes using algorithms. These are **reactive agents**. However, some agents can reason and plan their actions, making them **deliberative**.

A common example is a personal agent tasked with booking a vacation. Suppose there are many agents on the internet that can assist. The agent would contact others to check flight availability, hotel prices for different dates, and negotiate the best deal. Once the plan is finalized and approved by the user, it proceeds with booking.

For this, agents need to **communicate**. Successful communication requires:

* **Standard languages for knowledge exchange**, such as [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) and [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML), which are based on [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* **Negotiation protocols**, often based on different **auction types**.
* A **common ontology** to ensure shared understanding of concepts and their semantics.
* A way to **discover** the capabilities of other agents, also based on ontology.

Deliberative agents are more complex than reactive ones because they don’t just react to environmental changes—they can also *initiate* actions. One proposed architecture for deliberative agents is the Belief-Desire-Intention (BDI) model:

* **Beliefs** represent the agent’s knowledge about its environment, structured as a knowledge base or a set of rules.
* **Desires** define the agent’s goals. For example, a personal assistant agent’s goal might be to book a tour, while a hotel agent’s goal might be to maximize profit.
* **Intentions** are specific actions the agent plans to take to achieve its goals. These actions typically alter the environment and involve communication with other agents.

Platforms like [JADE](https://jade.tilab.com/) are available for building multi-agent systems. [This paper](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) provides a review of multi-agent platforms, along with a brief history and various use cases.

## Conclusion

Multi-Agent Systems can take many forms and serve a wide range of applications. They focus on the simpler behavior of individual agents, achieving complex system-wide behavior through **synergetic effects**.

## 🚀 Challenge

Apply this lesson to the real world by conceptualizing a multi-agent system to solve a problem. For example, how could a multi-agent system optimize a school bus route? How might it work in a bakery?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Review & Self Study

Explore how this type of system is used in industry. Choose a domain, such as manufacturing or video games, and investigate how multi-agent systems solve unique problems.

## [NetLogo Assignment](assignment.md)

---

