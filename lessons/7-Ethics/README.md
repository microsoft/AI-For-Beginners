# Ethical and Responsible AI

You have almost finished this course, and I hope that by now you clearly see that AI is based on a number of formal mathematical methods that allow us to find relationships in data and train models to replicate the human behavior in some areas. At this point in history, we consider AI to be a very powerful tool to extract patterns from data, and to apply those patterns to solve new problems.

However, in science fiction we often see stories where AI presents a danger to the humankind. Usually those stories are centered around some sort of AI rebellion, when AI decides to confront human beings. This implies that AI has some sort of emotions, or can take decisions unforeseen by its developers.

The kind of AI that we have learnt about in this course is nothing more than large matrix arithmetics. It is a very powerful tool to help us solve our problems, and as any other powerful tool - it can be used for good and for bad purposes. What's also important, it can be *misused*.

## Principles of Responsible AI

To avoid this accidental misuse of AI, Microsoft states important [Principles of Responsible AI](https://www.microsoft.com/ai/responsible-ai).

* **Fairness** is related to the important problem of *model biases*, which can be caused by using biased data for training. For example, when we try to predict the probability of getting a software developer job for a person, the model is likely to give higher preference to males - just because the training dataset was likely biased towards male audience. We need to carefully balance training data and investigate the model to avoid biases, and make sure that the model takes into account more relevant features.
* **Reliability and Safety**. By their nature, AI models can make mistakes. A neural network returns probabilities, and we need to take it into account when making decisions. Every model has some precision and recall, and we need to understand that to prevent harm that a wrong advice can cause.
* **Privacy and Security** have some AI-specific flavour. For example, when we use some data for training a model, this data becomes somehow "integrated" into the model. On one hand, that increases security and privacy, on the other - we need to remember which data the model was trained on.
* **Inclusiveness** means that we are not building AI to replace people, but rather to augment people and make our work more creative. It is also related to fairness, because when dealing with underrepresented communities, most of the datasets we collect are likely to be biased, and we need to make sure that those communities are included and correctly handled by AI. 
* **Transparency**. This includes making sure that we are always clear about AI being used. Also, wherever possible, we want to use AI systems that are *interpretable*. 
* **Accountability**. When AI models come up with some decisions, it is not always clear who is responsible for those decisions. We need to make sure that we understand the responsibility of AI decisions. In most of the cases we would want to include human being into the loop of taking important decisions, and people are made accountable. 

## Tools for Responsible AI

At Microsoft, we have developed [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), which contains a set of tools:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard that includes
   - EconML - tool for Causal Analysis, which focuses on what-if questions
   - DiCE - tool for Counterfactual Analysis allows you to see which features need to be changed to affect the decision of the model

## Model Interpretability

* Glass box models
* Black box models

## Model Fairness

