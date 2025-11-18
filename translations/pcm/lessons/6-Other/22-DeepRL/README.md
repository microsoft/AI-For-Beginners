<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04395657fc01648f8f70484d0e55ab67",
  "translation_date": "2025-11-18T18:48:28+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "pcm"
}
-->
# Deep Reinforcement Learning

Reinforcement learning (RL) na one of di main machine learning methods, wey dey different from supervised learning and unsupervised learning. For supervised learning, we dey use dataset wey get known answers, but RL na **learning by doing**. For example, when we first see computer game, we go start to play am, even if we no sabi di rules, and soon we go dey improve our skills just by playing di game and changing how we dey behave.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

To do RL, we need:

* **Environment** or **simulator** wey go set di rules of di game. We go fit run experiments for di simulator and see di results.
* **Reward function**, wey go show how successful di experiment be. For example, if we dey learn how to play computer game, di reward go be di final score.

Based on di reward function, we go fit change how we dey behave and improve our skills, so dat next time we go play better. Di main difference between RL and other types of machine learning be say for RL, we no go sabi whether we win or lose until di game finish. So, we no fit talk whether one move alone good or bad - we go only get reward when di game finish.

For RL, we dey do plenty experiments. For each experiment, we need to balance between following di best strategy wey we don learn so far (**exploitation**) and trying new possible moves (**exploration**).

## OpenAI Gym

One better tool for RL na [OpenAI Gym](https://gym.openai.com/) - **simulation environment**, wey fit simulate plenty different environments like Atari games, or di physics behind pole balancing. E be one of di most popular simulation environments for training RL algorithms, and [OpenAI](https://openai.com/) dey maintain am.

> **Note**: You fit see all di environments wey OpenAI Gym get [here](https://gym.openai.com/envs/#classic_control).

## CartPole Balancing

You don see modern balancing devices like *Segway* or *Gyroscooters* before? Dem fit balance by adjusting their wheels based on signal from accelerometer or gyroscope. For dis section, we go learn how to solve similar problem - balancing pole. E be like when circus performer dey balance pole for hand - but dis one na only 1D balancing.

Simplified version of balancing na **CartPole** problem. For CartPole world, we get horizontal slider wey fit move left or right, and di goal na to balance vertical pole on top di slider as e dey move.

<img alt="a cartpole" src="../../../../../translated_images/cartpole.f52a67f27e058170c25efc1bca8375b60906570ea757fe8d7ef04ae8e53df29d.pcm.png" width="200"/>

To create and use dis environment, we need small Python code:

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

Each environment dey work di same way:
* `env.reset` go start new experiment
* `env.step` go do simulation step. E go take **action** from **action space**, and return **observation** (from observation space), reward, and termination flag.

For di example above, we dey do random action for each step, na why di experiment no last long:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Di goal of RL algorithm na to train model - wey dem dey call **policy** &pi; - wey go return action based on di state. We fit also see policy as probabilistic, e.g., for any state *s* and action *a*, e go return di probability &pi;(*a*|*s*) wey show say we suppose take *a* for state *s*.

## Policy Gradients Algorithm

Di easiest way to model policy na to create neural network wey go take states as input, and return di actions (or di probabilities of all actions). E dey similar to normal classification task, but di big difference na say we no sabi beforehand which actions we suppose take for each step.

Di idea na to estimate di probabilities. We go build vector of **cumulative rewards** wey show total reward for each step of di experiment. We go also use **reward discounting** by multiplying earlier rewards by coefficient &gamma;=0.99, to reduce di importance of earlier rewards. Then, we go reinforce di steps wey give bigger rewards.

> Learn more about Policy Gradient algorithm and see am in action for [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

Improved version of Policy Gradients na **Actor-Critic**. Di main idea na say di neural network go dey trained to return two things:

* Di policy, wey go decide which action to take. Dis part dem dey call **actor**.
* Di estimation of total reward we fit get for di state - dis part dem dey call **critic**.

Dis architecture dey resemble [GAN](../../4-ComputerVision/10-GANs/README.md), wey get two networks wey dey train against each other. For actor-critic model, di actor go suggest di action wey we suppose take, and di critic go estimate di result. But di goal na to train di two networks together.

Because we sabi both di real cumulative rewards and di results wey critic return during di experiment, e dey easy to build loss function wey go reduce di difference between dem. Dis one go give us **critic loss**. We fit calculate **actor loss** by using di same method as Policy Gradient algorithm.

After we run one of di algorithms, we fit expect our CartPole to behave like dis:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Exercises: Policy Gradients and Actor-Critic RL

Continue your learning for di following notebooks:

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## Other RL Tasks

Reinforcement Learning na fast growing field for research today. Some interesting examples of RL na:

* Teaching computer to play **Atari Games**. Di challenge for dis problem na say we no get simple state as vector, but na screenshot - and we need CNN to change di screen image to feature vector, or extract reward info. Atari games dey Gym.
* Teaching computer to play board games like Chess and Go. Recently, programs like **Alpha Zero** don dey trained from scratch by two agents wey dey play against each other, and dey improve for each step.
* For industry, RL dey used to create control systems from simulation. Service like [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) dey specially designed for dis.

## Conclusion

We don learn how to train agents to get better results just by giving dem reward function wey define di desired state of di game, and giving dem chance to explore di search space intelligently. We don try two algorithms, and get good result for short time. But dis na just di beginning of your RL journey, and you fit take separate course if you wan learn more.

## 🚀 Challenge

Check di applications wey dey di 'Other RL Tasks' section and try to implement one!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review & Self Study

Learn more about classical reinforcement learning for our [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Watch [dis better video](https://www.youtube.com/watch?v=qv6UVOQ0F44) wey talk about how computer fit learn to play Super Mario.

## Assignment: [Train a Mountain Car](lab/README.md)

Your goal for dis assignment na to train different Gym environment - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg no forget say machine translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important matter, e go better make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->