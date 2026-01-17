<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T11:46:54+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "en"
}
-->
# Knowledge Representation and Expert Systems

![Summary of Symbolic AI content](../../../../translated_images/en/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.png)

> Sketchnote by [Tomomi Imura](https://twitter.com/girlie_mac)

The pursuit of artificial intelligence revolves around understanding the world in a way similar to humans. But how can this be achieved?

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/3)

In the early days of AI, the top-down approach to building intelligent systems (discussed in the previous lesson) was widely used. The idea was to extract knowledge from humans into a machine-readable format and use it to solve problems automatically. This approach was based on two key concepts:

* Knowledge Representation
* Reasoning

## Knowledge Representation

One of the central ideas in Symbolic AI is **knowledge**. It’s important to distinguish knowledge from *information* or *data*. For instance, people often say books contain knowledge because studying them can make someone an expert. However, books actually contain *data*, and by reading and integrating this data into our understanding of the world, we transform it into knowledge.

> ✅ **Knowledge** is what resides in our minds and reflects our understanding of the world. It is acquired through an active **learning** process, where pieces of information are integrated into our mental model of the world.

Typically, knowledge isn’t strictly defined but is aligned with related concepts using the [DIKW Pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid). This pyramid includes:

* **Data**: Represented in physical forms like written text or spoken words. Data exists independently of humans and can be shared.
* **Information**: How we interpret data mentally. For example, hearing the word *computer* evokes an understanding of what it is.
* **Knowledge**: Information integrated into our mental model of the world. For instance, once we learn what a computer is, we develop ideas about its functionality, cost, and uses. This interconnected network of concepts forms our knowledge.
* **Wisdom**: A higher level of understanding, representing *meta-knowledge*, such as knowing how and when to apply knowledge.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Image [from Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

The challenge of **knowledge representation** is finding an effective way to encode knowledge in a computer as data, making it usable automatically. This can be visualized as a spectrum:

![Knowledge representation spectrum](../../../../translated_images/en/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.png)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

* On the left, simple types of knowledge representations are highly usable by computers. The simplest form is algorithmic, where knowledge is encoded as a computer program. However, this approach lacks flexibility, as human knowledge is often non-algorithmic.
* On the right, representations like natural text are powerful but cannot be used for automatic reasoning.

> ✅ Take a moment to think about how you represent knowledge in your mind and translate it into notes. Is there a specific format that helps you retain information better?

## Classifying Computer Knowledge Representations

Different methods of computer-based knowledge representation can be categorized as follows:

* **Network representations**: These mimic the interconnected concepts in our minds by creating a graph-like structure in a computer, known as a **semantic network**.

1. **Object-Attribute-Value triplets** or **attribute-value pairs**: A semantic network can be represented as a list of triplets containing objects, attributes, and values. For example, we can describe programming languages using the following triplets:

Object | Attribute | Value
-------|-----------|------
Python | is | Untyped-Language
Python | invented-by | Guido van Rossum
Python | block-syntax | indentation
Untyped-Language | doesn't have | type definitions

> ✅ Think about how triplets could be used to represent other types of knowledge.

2. **Hierarchical representations**: These emphasize the way we often organize objects into hierarchies in our minds. For example, we know a canary is a bird, and all birds have wings. We also associate specific attributes like a canary’s color or flight speed.

   - **Frame representation**: Represents each object or class of objects as a **frame** containing **slots**. Slots may have default values, restrictions, or procedures to retrieve values. Frames form a hierarchy similar to object hierarchies in object-oriented programming.
   - **Scenarios**: Special types of frames that represent complex situations unfolding over time.

**Python**

Slot | Value | Default value | Interval |
-----|-------|---------------|----------|
Name | Python | | |
Is-A | Untyped-Language | | |
Variable Case | | CamelCase | |
Program Length | | | 5-5000 lines |
Block Syntax | Indent | | |

3. **Procedural representations**: Represent knowledge as a sequence of actions triggered by specific conditions.
   - Production rules: If-then statements used to draw conclusions. For example, a doctor might use the rule: **IF** a patient has a high fever **OR** elevated C-reactive protein levels **THEN** they have inflammation. Encountering one of these conditions allows the doctor to infer inflammation and use it for further reasoning.
   - Algorithms: Another form of procedural representation, though rarely used directly in knowledge-based systems.

4. **Logic**: Originally proposed by Aristotle as a method to represent universal human knowledge.
   - Predicate Logic: A mathematical theory that is too complex for computation, so subsets like Horn clauses (used in Prolog) are typically employed.
   - Descriptive Logic: Logical systems used to represent and reason about hierarchies of objects in distributed knowledge representations like the *semantic web*.

## Expert Systems

One of the early achievements of symbolic AI was the development of **expert systems**—computer systems designed to act as experts in specific problem domains. These systems relied on a **knowledge base** extracted from human experts and an **inference engine** to perform reasoning.

![Human Architecture](../../../../translated_images/en/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.png) | ![Knowledge-Based System](../../../../translated_images/en/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.png)
---------------------------------------------|------------------------------------------------
Simplified structure of a human neural system | Architecture of a knowledge-based system

Expert systems are modeled after human reasoning, which involves **short-term memory** and **long-term memory**. Similarly, knowledge-based systems consist of:

* **Problem memory**: Stores knowledge about the current problem being solved, such as a patient’s temperature or blood pressure. This is called **static knowledge**, representing a snapshot of the problem state.
* **Knowledge base**: Contains long-term knowledge about the problem domain, extracted from human experts. It remains unchanged across consultations and is referred to as **dynamic knowledge** because it helps navigate between problem states.
* **Inference engine**: Manages the reasoning process, asking questions when needed and applying rules to the problem state.

For example, consider an expert system designed to identify animals based on physical characteristics:

![AND-OR Tree](../../../../translated_images/en/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.png)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

This diagram, called an **AND-OR tree**, visually represents a set of production rules. While useful for extracting knowledge from experts, rules are more convenient for computer representation:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Notice that each condition on the left-hand side of the rule and the action are essentially object-attribute-value (OAV) triplets. The **working memory** contains OAV triplets related to the current problem. A **rules engine** identifies applicable rules and adds new triplets to the working memory.

> ✅ Create your own AND-OR tree on a topic of your choice!

### Forward vs. Backward Inference

The process described above is known as **forward inference**, which starts with initial data in the working memory and follows these steps:

1. If the target attribute is already in the working memory, stop and provide the result.
2. Identify rules whose conditions are satisfied, forming a **conflict set**.
3. Resolve the conflict by selecting one rule to execute. Strategies include:
   - Choosing the first applicable rule.
   - Selecting a random rule.
   - Picking the *most specific* rule, i.e., the one with the most conditions on the left-hand side (LHS).
4. Apply the selected rule and update the problem state.
5. Repeat from step 1.

In some cases, we start with no knowledge about the problem and ask questions to reach a conclusion. For instance, in medical diagnosis, tests are performed only when needed for decision-making.

This approach is modeled using **backward inference**, driven by the **goal**—the attribute value we aim to find:

1. Identify rules that can provide the goal value (i.e., rules with the goal on the RHS).
2. If no rules exist for the attribute or a rule suggests asking the user, do so. Otherwise:
3. Use a conflict resolution strategy to select a rule as a *hypothesis* to prove.
4. Recursively repeat the process for all attributes in the LHS of the rule, treating them as sub-goals.
5. If the process fails at any point, try another rule from step 3.

> ✅ When is forward inference more suitable? What about backward inference?

### Implementing Expert Systems

Expert systems can be implemented using various methods:

* Direct programming in a high-level language. This is not ideal, as the separation of knowledge from inference allows domain experts to write rules without understanding the inference process.
* Using an **expert systems shell**, a specialized system designed for knowledge representation and inference.

## ✍️ Exercise: Animal Inference

Refer to [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) for an example of implementing forward and backward inference in an expert system.

> **Note**: This example is simple and provides a basic understanding of expert systems. As you develop such systems, they exhibit *intelligent* behavior only after reaching a certain number of rules, typically around 200+. At this point, the rules become too complex to manage mentally, and you may wonder why the system makes certain decisions. However, a key feature of knowledge-based systems is their ability to *explain* the reasoning behind any decision.

## Ontologies and the Semantic Web

At the end of the 20th century, an initiative aimed to use knowledge representation to annotate Internet resources, enabling highly specific queries. This effort, called the **Semantic Web**, relied on several concepts:

- A specialized knowledge representation based on **[description logics](https://en.wikipedia.org/wiki/Description_logic)** (DL). Similar to frame-based representation, it organizes objects hierarchically with properties but includes formal logical semantics and inference. Various DLs balance expressiveness with computational complexity.
- Distributed knowledge representation, where all concepts are identified by global URIs, allowing the creation of knowledge hierarchies spanning the internet.
- A family of XML-based languages for knowledge representation: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

A key concept in the Semantic Web is **Ontology**. It refers to the explicit specification of a problem domain using formal knowledge representation. The simplest ontology might just be a hierarchy of objects within a problem domain, but more complex ontologies include rules that enable inference.

In the Semantic Web, all representations are based on triplets. Each object and each relation are uniquely identified by a URI. For example, if we want to state that this AI Curriculum was developed by Dmitry Soshnikov on January 1st, 2022, here are the triplets we can use:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Here `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` are well-known and widely accepted URIs to express the concepts of *creator* and *creation date*.

In a more complex scenario, if we want to define a list of creators, we can use certain data structures defined in RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagrams above by [Dmitry Soshnikov](http://soshnikov.com)

The development of the Semantic Web has been somewhat slowed by the success of search engines and natural language processing techniques, which can extract structured data from text. However, in certain areas, significant efforts are still being made to maintain ontologies and knowledge bases. A few noteworthy projects include:

* [WikiData](https://wikidata.org/) is a collection of machine-readable knowledge bases linked to Wikipedia. Much of the data is extracted from Wikipedia *InfoBoxes*, which are structured content sections within Wikipedia pages. You can [query](https://query.wikidata.org/) WikiData using SPARQL, a specialized query language for the Semantic Web. Here’s an example query that displays the most common eye colors among humans:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) is another initiative similar to WikiData.

> ✅ If you want to experiment with building your own ontologies or exploring existing ones, there’s a great visual ontology editor called [Protégé](https://protege.stanford.edu/). You can download it or use it online.

<img src="images/protege.png" width="70%"/>

*Web Protégé editor open with the Romanov Family ontology. Screenshot by Dmitry Soshnikov*

## ✍️ Exercise: A Family Ontology

Refer to [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) for an example of using Semantic Web techniques to analyze family relationships. We will take a family tree represented in the common GEDCOM format and an ontology of family relationships to construct a graph of all family connections for a given set of individuals.

## Microsoft Concept Graph

In most cases, ontologies are meticulously crafted by hand. However, it is also possible to **extract** ontologies from unstructured data, such as natural language text.

One such effort was undertaken by Microsoft Research, resulting in the [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

This is a large collection of entities grouped using the `is-a` inheritance relationship. It can answer questions like "What is Microsoft?"—with responses such as "a company with probability 0.87, and a brand with probability 0.75."

The graph is accessible either via a REST API or as a downloadable text file listing all entity pairs.

## ✍️ Exercise: A Concept Graph

Explore the [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) notebook to see how Microsoft Concept Graph can be used to categorize news articles into different groups.

## Conclusion

Today, AI is often equated with *Machine Learning* or *Neural Networks*. However, humans also exhibit explicit reasoning, which is something neural networks currently do not handle. In real-world projects, explicit reasoning is still employed for tasks requiring explanations or the ability to modify system behavior in a controlled manner.

## 🚀 Challenge

In the Family Ontology notebook associated with this lesson, experiment with other family relationships. Try to uncover new connections between individuals in the family tree.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Review & Self Study

Research online to find examples where humans have attempted to quantify and codify knowledge. Look into Bloom's Taxonomy, and delve into history to understand how humans have tried to make sense of their world. Study Linnaeus's work on creating a taxonomy of organisms, and examine how Dmitri Mendeleev developed a system for describing and grouping chemical elements. What other fascinating examples can you discover?

**Assignment**: [Build an Ontology](assignment.md)

---

