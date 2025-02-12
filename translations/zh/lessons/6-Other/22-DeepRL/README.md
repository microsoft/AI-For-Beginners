# 深度强化学习

强化学习（RL）被视为基本的机器学习范式之一，和监督学习、无监督学习并列。在监督学习中，我们依赖于具有已知结果的数据集，而强化学习则基于**实践学习**。例如，当我们第一次看到一款电脑游戏时，我们开始玩耍，即使不知道规则，经过一段时间的游戏，我们能够通过玩耍和调整行为来提高我们的技能。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

要进行强化学习，我们需要：

* 一个**环境**或**模拟器**，它设定了游戏的规则。我们应该能够在模拟器中运行实验并观察结果。
* 一些**奖励函数**，指示我们的实验成功程度。在学习玩电脑游戏的情况下，奖励将是我们的最终得分。

基于奖励函数，我们应该能够调整我们的行为并提高我们的技能，以便下次能玩得更好。强化学习与其他类型的机器学习的主要区别在于，在强化学习中，我们通常不知道在游戏结束之前我们是赢还是输。因此，我们不能仅仅说某个动作是好是坏——我们只在游戏结束时获得奖励。

在强化学习过程中，我们通常会进行许多实验。在每个实验中，我们需要在遵循迄今为止学习到的最佳策略（**利用**）和探索新的可能状态（**探索**）之间进行平衡。

## OpenAI Gym

一个很好的强化学习工具是 [OpenAI Gym](https://gym.openai.com/) - 一个**模拟环境**，可以模拟许多不同的环境，从Atari游戏到杆平衡的物理原理。它是训练强化学习算法的最受欢迎的模拟环境之一，由 [OpenAI](https://openai.com/) 维护。

> **注意**：您可以在 [这里](https://gym.openai.com/envs/#classic_control) 查看 OpenAI Gym 中可用的所有环境。

## CartPole 平衡

您可能都见过现代的平衡设备，如 *Segway* 或 *Gyroscooters*。它们能够通过根据加速度计或陀螺仪的信号自动调整轮子来实现平衡。在本节中，我们将学习如何解决一个类似的问题——平衡一个杆。这个问题类似于一个马戏团表演者需要在手上平衡一个杆的情况——但这个杆的平衡仅发生在一维。

平衡的简化版本被称为**CartPole**问题。在cartpole世界中，我们有一个可以左右移动的水平滑块，目标是在滑块上方平衡一个垂直杆。

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

要创建和使用这个环境，我们需要几行Python代码：

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

每个环境的访问方式完全相同：
* `env.reset` starts a new experiment
* `env.step` 执行一个模拟步骤。它从**动作空间**接收一个**动作**，并返回一个**观察**（来自观察空间），以及一个奖励和一个终止标志。

在上面的例子中，我们在每个步骤执行一个随机动作，这就是实验生命周期很短的原因：

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

强化学习算法的目标是训练一个模型——所谓的**策略** π——它将根据给定的状态返回动作。我们也可以将策略视为概率性的，例如，对于任何状态 *s* 和动作 *a*，它将返回在状态 *s* 采取 *a* 的概率 π(*a*|*s*)。

## 策略梯度算法

建模策略最明显的方法是创建一个神经网络，该网络将状态作为输入，并返回相应的动作（或者说是所有动作的概率）。从某种意义上说，这类似于普通的分类任务，但有一个主要区别——我们事先不知道在每一步应该采取哪些动作。

这里的想法是估计这些概率。我们构建一个**累积奖励**的向量，显示我们在实验每一步的总奖励。我们还通过将早期奖励乘以某个系数 γ=0.99 来应用**奖励折扣**，以减小早期奖励的作用。然后，我们强化在实验路径上产生更大奖励的步骤。

> 了解更多关于策略梯度算法的信息，并在 [示例笔记本](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb) 中查看其实际应用。

## Actor-Critic 算法

策略梯度方法的改进版本称为**Actor-Critic**。其主要思想是神经网络将被训练以返回两样东西：

* 策略，决定采取哪个动作。这部分称为**actor**
* 我们可以在该状态下预期获得的总奖励的估计——这部分称为**critic**。

从某种意义上说，这种架构类似于 [GAN](../../4-ComputerVision/10-GANs/README.md)，其中有两个网络相互对抗训练。在actor-critic模型中，actor提出我们需要采取的动作，而critic则尝试进行评估并估计结果。然而，我们的目标是共同训练这些网络。

因为我们知道实验过程中真实的累积奖励和critic返回的结果，所以构建一个损失函数以最小化它们之间的差异相对容易。这将给我们**critic损失**。我们可以通过使用与策略梯度算法相同的方法来计算**actor损失**。

运行这些算法之一后，我们可以期待我们的CartPole表现如下：

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ 练习：策略梯度和Actor-Critic RL

在以下笔记本中继续学习：

* [TensorFlow中的RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [PyTorch中的RL](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## 其他RL任务

如今，强化学习是一个快速发展的研究领域。一些有趣的强化学习示例包括：

* 教会计算机玩**Atari游戏**。这个问题的挑战在于，我们没有简单的状态以向量表示，而是一个屏幕截图——我们需要使用CNN将这个屏幕图像转换为特征向量，或提取奖励信息。Atari游戏在Gym中可用。
* 教会计算机玩棋类游戏，如国际象棋和围棋。最近，像**Alpha Zero**这样的先进程序是通过两个代理相互对弈，从零开始训练的，并在每一步中不断提高。
* 在工业中，强化学习被用来从模拟中创建控制系统。一个名为 [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) 的服务专门为此设计。

## 结论

我们现在已经学习了如何通过提供定义游戏所需状态的奖励函数，并给予智能探索搜索空间的机会，来训练代理以获得良好的结果。我们成功尝试了两种算法，并在相对较短的时间内取得了良好的结果。然而，这只是您进入强化学习旅程的开始，如果您想深入了解，绝对应该考虑参加一个单独的课程。

## 🚀 挑战

探索“其他RL任务”部分列出的应用，并尝试实现其中一个！

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## 复习与自学

在我们的 [初学者机器学习课程](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) 中了解更多关于经典强化学习的信息。

观看 [这段精彩视频](https://www.youtube.com/watch?v=qv6UVOQ0F44)，讲述计算机如何学习玩超级马里奥。

## 作业：[训练山地车](lab/README.md)

在这个作业中，您的目标是训练一个不同的Gym环境——[Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/)。

**免责声明**：  
本文件是使用基于机器的人工智能翻译服务翻译的。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议进行专业人工翻译。我们对因使用本翻译而导致的任何误解或误读不承担责任。