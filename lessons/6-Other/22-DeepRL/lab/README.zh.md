# 训练Mountain Car逃生

来自[AI初学者的课程实验](https://github.com/microsoft/ai-for-beginners)。

## 任务

你的目标是训练RL代理在OpenAI环境中控制Mountain Car。

<img alt="Mountain Car" src="images/mountaincar.png" width="300"/>

## 环境

Mountain Car 环境是一个小车被困在山谷里。你的目标是跳出山谷并到达旗标。你可以加速向左、向右或不做任何动作。你可以观察小车沿着x轴的位置和速度。

## 开始实验笔记

通过打开 [MountainCar.ipynb](MountainCar.ipynb)开始实验。

## 收获

在整个实验室中，您将了解到将RL算法应用到新环境通常是非常简单的，因为OpenAI Gym对所有环境采用相同的接口，并且算法并不在很大程度上依赖于环境的特性。甚至可以通过重组Python代码的方式将任何环境作为参数传递给RL算法。