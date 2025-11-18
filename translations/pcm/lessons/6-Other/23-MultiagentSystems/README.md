<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "38a1185ae3d54b180378bbd71ae3ef16",
  "translation_date": "2025-11-18T18:46:50+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "pcm"
}
-->
# Multi-Agent Systems

One way wey people fit take achieve intelligence na wetin dem dey call **emergent** (or **synergetic**) approach. Dis one dey base on di fact say di combined behavior of plenty simple agents fit result for di overall more complex (or intelligent) behavior of di system as one whole. For theory, e dey base on di principles of [Collective Intelligence](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain) and [Evolutionary Cybernetics](https://en.wikipedia.org/wiki/Global_brain), wey talk say higher-level systems dey gain extra value if dem combine well from lower-level systems (wetin dem dey call *principle of metasystem transition*).

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

Di idea of **Multi-Agent Systems** start for AI for di 1990s as response to di growth of Internet and distributed systems. One of di classical AI textbooks, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), dey focus on di view of classical AI from di angle of Multi-agent systems.

Di main thing for Multi-agent approach na di idea of **Agent** - one entity wey dey live for one **environment**, wey e fit perceive and act upon. Dis definition dey broad well, and e get plenty different types and classifications of agents:

* By di way dem fit reason:
   - **Reactive** agents dey usually get simple request-response type of behavior
   - **Deliberative** agents dey use some kind logical reasoning and/or planning skills
* By di place wey agent dey run e code:
   - **Static** agents dey work for one fixed network node
   - **Mobile** agents fit move dia code between network nodes
* By dia behavior:
   - **Passive agents** no get specific goals. Dis kind agents fit react to external things, but dem no go start any action by demself.
   - **Active agents** get some goals wey dem dey pursue
   - **Cognitive agents** dey involve complex planning and reasoning

Multi-agent systems dey used today for plenty applications:

* For games, many non-player characters dey use some kind AI, and dem fit be considered as intelligent agents
* For video production, to render complex 3D scenes wey involve crowds, dem dey use multi-agent simulation
* For systems modeling, multi-agent approach dey help simulate di behavior of one complex model. For example, multi-agent approach don dey used to predict how COVID-19 disease go spread worldwide. Di same approach fit dey used to model traffic for city, and see how e go react to changes for traffic rules.
* For complex automation systems, each device fit act as independent agent, wey go make di whole system less monolith and more strong.

We no go spend plenty time to go deep into multi-agent systems, but we go look one example of **Multi-Agent Modeling**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) na multi-agent modeling environment wey dey base on one modified version of di [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programming language. Dis language dey developed to teach programming concepts to children, and e dey allow you control one agent wey dem dey call **turtle**, wey fit move and leave trace behind. Dis one dey allow people create complex geometric figures, wey be very visual way to understand di behavior of one agent.

For NetLogo, we fit create plenty turtles by using di `create-turtles` command. We fit then command all di turtles to do some actions (for di example below - move 10 point forward):

```
create-turtles 10
ask turtles [
  forward 10
]
```

E no dey interesting if all di turtles dey do di same thing, so we fit `ask` groups of turtles, like di ones wey dey near one certain point. We fit also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` na di name of di breed, and we need to specify both singular and plural word, because different commands dey use different forms for clarity.

> ✅ We no go learn di NetLogo language itself - you fit visit di brilliant [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) resource if you wan learn more.

You fit [download](https://ccl.northwestern.edu/netlogo/download.shtml) and install NetLogo to try am.

### Models Library

One good thing about NetLogo na say e get one library of working models wey you fit try. Go **File &rightarrow; Models Library**, and you go see plenty categories of models to choose from.

<img alt="NetLogo Models Library" src="../../../../../translated_images/NetLogo-ModelLib.efe023afb4763c059704a8ac0e2cd5e51889b117e8eac02aaa5334cfe1c52c13.pcm.png" width="60%"/>

> Screenshot of di models library by Dmitry Soshnikov

You fit open one of di models, like **Biology &rightarrow; Flocking**.

### Main Principles

After you open di model, you go see di main NetLogo screen. Here na sample model wey dey describe di population of wolves and sheep, wey dey depend on finite resources (grass).

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.pcm.png)

> Screenshot by Dmitry Soshnikov

For dis screen, you go see:

* Di **Interface** section wey get:
  - Di main field, where all di agents dey live
  - Different controls: buttons, sliders, etc.
  - Graphs wey you fit use to display di simulation parameters
* Di **Code** tab wey get di editor, where you fit type NetLogo program

Most times, di interface go get **Setup** button, wey dey initialize di simulation state, and **Go** button wey dey start di execution. Dem dey handled by di handlers for di code wey look like dis:

```
to go [
...
]
```

NetLogo world dey consist of di following objects:

* **Agents** (turtles) wey fit move across di field and do something. You fit command agents by using `ask turtles [...]` syntax, and di code for di brackets go dey executed by all agents for *turtle mode*.
* **Patches** na square areas for di field, where agents dey live. You fit refer to all agents for di same patch, or you fit change patch colors and some other properties. You fit also `ask patches` to do something.
* **Observer** na one unique agent wey dey control di world. All button handlers dey run for *observer mode*.

> ✅ Di beauty of multi-agent environment na say di code wey dey run for turtle mode or patch mode dey run at di same time by all agents for parallel. So, by writing small code and programming di behavior of individual agent, you fit create complex behavior for di simulation system as one whole.

### Flocking

As example of multi-agent behavior, make we look **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking na complex pattern wey dey similar to how flocks of birds dey fly. If you dey watch dem fly, you fit think say dem dey follow one kind collective algorithm, or say dem get some kind *collective intelligence*. But dis complex behavior dey happen when each individual agent (for dis case, one *bird*) dey observe some other agents wey dey close to am, and dey follow three simple rules:

* **Alignment** - e dey move towards di average heading of di agents wey dey near am
* **Cohesion** - e dey try move towards di average position of di agents wey dey near am (*long range attraction*)
* **Separation** - if e dey too close to other birds, e dey try move away (*short range repulsion*)

You fit run di flocking example and observe di behavior. You fit also adjust di parameters, like *degree of separation*, or di *viewing range*, wey dey define how far each bird fit see. If you reduce di viewing range to 0, all di birds go blind, and flocking go stop. If you reduce separation to 0, all di birds go gather for straight line.

> ✅ Switch to di **Code** tab and see where di three rules of flocking (alignment, cohesion and separation) dey implemented for code. Note how we dey refer only to di agents wey dey sight.

### Other Models to see

E get some other interesting models wey you fit experiment with:

* **Art &rightarrow; Fireworks** dey show how firework fit be collective behavior of individual fire streams
* **Social Science &rightarrow; Traffic Basic** and **Social Science &rightarrow; Traffic Grid** dey show di model of city traffic for 1D and 2D Grid with or without traffic lights. Each car for di simulation dey follow di following rules:
   - If di space for front dey empty - accelerate (up to one certain max speed)
   - If e see obstacle for front - brake (and you fit adjust how far di driver fit see)
* **Social Science &rightarrow; Party** dey show how people dey group together during cocktail party. You fit find di combination of parameters wey go lead to di fastest increase of happiness for di group.

As you fit see from dis examples, multi-agent simulations fit dey very useful to understand di behavior of one complex system wey dey consist of individuals wey dey follow di same or similar logic. E fit also dey used to control virtual agents, like [NPCs](https://en.wikipedia.org/wiki/NPC) for computer games, or agents for 3D animated worlds.

## Deliberative Agents

Di agents wey we don describe so far dey very simple, dem dey react to changes for environment using some kind algorithm. As such, dem be **reactive agents**. But sometimes agents fit reason and plan dia action, and for dis case dem dey called **deliberative**.

One example fit be personal agent wey dey receive instruction from human to book vacation tour. Suppose say e get plenty agents wey dey live for internet wey fit help am. E go need contact other agents to check which flights dey available, wetin be di hotel prices for different dates, and try negotiate di best price. When di vacation plan don complete and di owner don confirm am, e fit proceed with booking.

To do dis, agents need to **communicate**. For successful communication dem need:

* Some **standard languages to exchange knowledge**, like [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) and [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Dis languages dey designed based on [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* Di languages suppose also get some **protocols for negotiations**, based on different **auction types**.
* One **common ontology** to use, so say dem go dey refer to di same concepts knowing dia meaning
* One way to **discover** wetin different agents fit do, also based on some kind ontology

Deliberative agents dey more complex pass reactive ones, because dem no dey only react to changes for environment, dem suppose fit *start* actions. One proposed architecture for deliberative agents na di so-called Belief-Desire-Intention (BDI) agent:

* **Beliefs** dey form one set of knowledge about di agent environment. E fit dey structured as knowledge base or set of rules wey agent fit apply to one specific situation for di environment.
* **Desires** dey define wetin di agent wan do, i.e. e goals. For example, di goal of di personal assistant agent wey we talk about na to book tour, and di goal of hotel agent na to maximize profit.
* **Intentions** na specific actions wey di agent dey plan to achieve e goals. Actions dey usually change di environment and cause communication with other agents.

E get some platforms wey dey available to build multi-agent systems, like [JADE](https://jade.tilab.com/). [Dis paper](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) dey review multi-agent platforms, together with brief history of multi-agent systems and dia different usage scenarios.

## Conclusion

Multi-Agent systems fit take plenty different forms and dey used for many different applications. 
Dem dey focus on di simpler behavior of individual agent, and achieve more complex behavior of di overall system because of **synergetic effect**.

## 🚀 Challenge

Carry dis lesson enter real world and try conceptualize one multi-agent system wey fit solve one problem. Wetin, for example, multi-agent system go need do to optimize school bus route? How e fit work for bakery?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Review & Self Study

Review how dis type of system dey used for industry. Pick one domain like manufacturing or di video game industry and discover how multi-agent systems fit dey used to solve unique problems.

## [NetLogo Assignment](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say transleshion wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make professional human transleshion dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->