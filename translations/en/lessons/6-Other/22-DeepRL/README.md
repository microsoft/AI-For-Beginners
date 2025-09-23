<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04395657fc01648f8f70484d0e55ab67",
  "translation_date": "2025-09-23T11:43:49+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "en"
}
-->
# Deep Reinforcement Learning

Reinforcement learning (RL) is considered one of the fundamental paradigms of machine learning, alongside supervised learning and unsupervised learning. While supervised learning relies on datasets with known outcomes, RL is based on **learning through experience**. For instance, when we play a computer game for the first time, we start playing without knowing the rules, and over time, we improve our skills simply by playing and adjusting our behavior.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

To perform RL, we need:

* An **environment** or **simulator** that defines the rules of the game. This allows us to run experiments and observe the results.
* A **reward function**, which indicates how successful our experiment was. For example, in the context of learning to play a computer game, the reward could be the final score.

Using the reward function, we adjust our behavior to improve our performance, so that we do better the next time. The key difference between RL and other types of machine learning is that in RL, we typically don’t know whether we’ve succeeded or failed until the end of the game. This means we can’t evaluate whether a specific move is good or bad in isolation—we only receive feedback (the reward) at the end.

In RL, we usually perform many experiments. During each experiment, we must balance between following the best strategy we’ve learned so far (**exploitation**) and trying out new possibilities (**exploration**).

## OpenAI Gym

A fantastic tool for RL is the [OpenAI Gym](https://gym.openai.com/)—a **simulation environment** that can simulate a variety of scenarios, from Atari games to physics-based problems like pole balancing. It is one of the most widely used environments for training reinforcement learning algorithms and is maintained by [OpenAI](https://openai.com/).

> **Note**: You can explore all the environments available in OpenAI Gym [here](https://gym.openai.com/envs/#classic_control).

## CartPole Balancing

You’ve probably seen modern balancing devices like *Segways* or *gyroscooters*. These devices balance automatically by adjusting their wheels based on signals from accelerometers or gyroscopes. In this section, we’ll learn how to solve a similar problem—balancing a pole. This is akin to a circus performer balancing a pole on their hand, but in our case, the balancing happens in 1D.

A simplified version of this problem is called the **CartPole** problem. In the CartPole scenario, there’s a horizontal slider that can move left or right, and the goal is to balance a vertical pole on top of the slider as it moves.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

To create and use this environment, we only need a few lines of Python code:

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

In the example above, we perform random actions at each step, which is why the experiment ends quickly:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

The goal of an RL algorithm is to train a model—called a **policy** &pi;—that determines the action to take in response to a given state. The policy can also be probabilistic, meaning that for any state *s* and action *a*, it returns the probability &pi;(*a*|*s*) of taking action *a* in state *s*.

## Policy Gradients Algorithm

The most straightforward way to model a policy is by using a neural network that takes states as input and outputs corresponding actions (or the probabilities of all actions). This is somewhat similar to a classification task, with one major difference—we don’t know in advance which actions to take at each step.

The idea is to estimate these probabilities. We construct a vector of **cumulative rewards**, which represents the total reward at each step of the experiment. We also apply **reward discounting** by multiplying earlier rewards by a coefficient &gamma;=0.99, reducing the influence of earlier rewards. Then, we reinforce the steps in the experiment that yield higher rewards.

> Learn more about the Policy Gradient algorithm and see it in action in the [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

An improved version of the Policy Gradients approach is the **Actor-Critic** algorithm. The main idea is to train a neural network to output two things:

* The policy, which determines the action to take. This part is called the **actor**.
* An estimate of the total reward expected from the current state. This part is called the **critic**.

This architecture is somewhat similar to a [GAN](../../4-ComputerVision/10-GANs/README.md), where two networks are trained together. In the Actor-Critic model, the actor suggests the action to take, while the critic evaluates the expected outcome. However, the goal is to train both networks collaboratively.

Since we know both the actual cumulative rewards and the critic’s predictions during the experiment, we can easily create a loss function to minimize the difference between them, resulting in the **critic loss**. The **actor loss** can be computed using the same approach as in the Policy Gradient algorithm.

After training with one of these algorithms, we can expect our CartPole to behave like this:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercises: Policy Gradients and Actor-Critic RL

Continue your learning with the following notebooks:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Other RL Tasks

Reinforcement Learning is a rapidly growing field of research. Some interesting applications include:

* Teaching a computer to play **Atari games**. The challenge here is that the state isn’t a simple vector but rather a screenshot. A convolutional neural network (CNN) is used to convert the screen image into a feature vector or extract reward information. Atari games are available in the Gym.
* Teaching a computer to play board games like Chess and Go. Recent state-of-the-art programs like **AlphaZero** were trained from scratch by having two agents play against each other, improving with each iteration.
* In industry, RL is used to create control systems from simulations. A service like [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) is specifically designed for this purpose.

## Conclusion

We’ve learned how to train agents to achieve good results by providing them with a reward function that defines the desired outcome and allowing them to intelligently explore the search space. We’ve successfully tried two algorithms and achieved good results in a relatively short time. However, this is just the beginning of your RL journey, and you should consider taking a dedicated course if you want to dive deeper.

## 🚀 Challenge

Explore the applications listed in the 'Other RL Tasks' section and try implementing one!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review & Self Study

Learn more about classical reinforcement learning in our [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Watch [this great video](https://www.youtube.com/watch?v=qv6UVOQ0F44) about how a computer can learn to play Super Mario.

## Assignment: [Train a Mountain Car](lab/README.md)

Your goal for this assignment is to train a different Gym environment—[Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

