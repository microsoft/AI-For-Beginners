<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-31T17:32:28+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "en"
}
-->
# Deep Reinforcement Learning

Reinforcement learning (RL) is considered one of the fundamental machine learning paradigms, alongside supervised learning and unsupervised learning. While supervised learning relies on datasets with known outcomes, RL is based on **learning through experience**. For instance, when we first encounter a computer game, we start playing without knowing the rules, and over time, we improve our skills simply by playing and adjusting our actions.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

To perform RL, we need:

* An **environment** or **simulator** that defines the rules of the game. It should allow us to run experiments and observe the results.
* A **reward function** that indicates how successful our experiment was. For example, in learning to play a computer game, the reward could be the final score.

Using the reward function, we can adjust our actions and improve our skills to perform better in subsequent attempts. The key difference between RL and other types of machine learning is that in RL, we often don't know whether we are succeeding or failing until the game ends. This means we can't evaluate individual moves in isolation; the reward is only received at the end of the game.

In RL, we typically conduct numerous experiments. During each experiment, we must balance between following the best strategy we've learned so far (**exploitation**) and exploring new possibilities (**exploration**).

## OpenAI Gym

A powerful tool for RL is the [OpenAI Gym](https://gym.openai.com/) - a **simulation environment** capable of simulating various scenarios, from Atari games to physics-based problems like pole balancing. It is one of the most widely used environments for training RL algorithms and is maintained by [OpenAI](https://openai.com/).

> **Note**: You can explore all the environments available in OpenAI Gym [here](https://gym.openai.com/envs/#classic_control).

## CartPole Balancing

You may be familiar with modern balancing devices like *Segways* or *Gyroscooters*. These devices automatically balance by adjusting their wheels based on signals from accelerometers or gyroscopes. In this section, we'll tackle a similar problem: balancing a pole. This is akin to a circus performer balancing a pole on their hand, but here the balancing occurs in one dimension.

A simplified version of this problem is known as the **CartPole** problem. In the CartPole scenario, there is a horizontal slider that can move left or right, and the goal is to balance a vertical pole on top of the slider as it moves.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

To create and use this environment, we need just a few lines of Python code:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Each environment can be interacted with in the same way:
* `env.reset` initializes a new experiment.
* `env.step` performs a simulation step. It takes an **action** from the **action space** and returns an **observation** (from the observation space), along with a reward and a termination flag.

In the example above, we perform random actions at each step, which results in a very short experiment:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

The goal of an RL algorithm is to train a model, known as a **policy** π, which determines the action to take in response to a given state. The policy can also be probabilistic, meaning for any state *s* and action *a*, it returns the probability π(*a*|*s*) of taking action *a* in state *s*.

## Policy Gradients Algorithm

The most straightforward way to model a policy is by using a neural network that takes states as input and outputs corresponding actions (or the probabilities of all actions). This is similar to a standard classification task, with one major difference: we don't know in advance which actions to take at each step.

The idea is to estimate these probabilities. We construct a vector of **cumulative rewards** that represents the total reward at each step of the experiment. We also apply **reward discounting** by multiplying earlier rewards by a coefficient γ=0.99, reducing the influence of earlier rewards. Then, we reinforce the steps in the experiment that yield higher rewards.

> Learn more about the Policy Gradient algorithm and see it in action in the [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

An enhanced version of the Policy Gradients approach is called **Actor-Critic**. The key idea is to train a neural network to output two things:

* The policy, which decides the action to take. This part is called the **actor**.
* An estimate of the total reward expected from the current state. This part is called the **critic**.

This architecture is somewhat similar to a [GAN](../../4-ComputerVision/10-GANs/README.md), where two networks are trained in tandem. In the actor-critic model, the actor suggests the action to take, while the critic evaluates the expected outcome. The goal is to train both networks collaboratively.

Since we know both the actual cumulative rewards and the critic's predictions during the experiment, we can easily create a loss function to minimize the difference between them, resulting in **critic loss**. **Actor loss** can be computed using the same approach as in the policy gradient algorithm.

After training with one of these algorithms, we can expect the CartPole to behave like this:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercises: Policy Gradients and Actor-Critic RL

Continue your learning with the following notebooks:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Other RL Tasks

Reinforcement Learning is a rapidly evolving field of research. Some fascinating applications include:

* Teaching a computer to play **Atari Games**. The challenge here is that the state isn't a simple vector but rather a screenshot. A CNN is used to convert the screen image into a feature vector or extract reward information. Atari games are available in the Gym.
* Training a computer to play board games like Chess and Go. Recent programs like **Alpha Zero** were trained from scratch by having two agents play against each other, improving with each step.
* In industry, RL is used to develop control systems through simulation. A service called [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) is specifically designed for this purpose.

## Conclusion

We have learned how to train agents to achieve good results by providing them with a reward function that defines the desired state of the game and allowing them to intelligently explore the search space. We successfully applied two algorithms and achieved promising results in a relatively short time. However, this is just the beginning of your RL journey, and you should consider taking a dedicated course if you want to dive deeper.

## 🚀 Challenge

Explore the applications mentioned in the 'Other RL Tasks' section and try implementing one!

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Review & Self Study

Learn more about classical reinforcement learning in our [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Watch [this great video](https://www.youtube.com/watch?v=qv6UVOQ0F44) to see how a computer learns to play Super Mario.

## Assignment: [Train a Mountain Car](lab/README.md)

Your task in this assignment is to train a different Gym environment: [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.