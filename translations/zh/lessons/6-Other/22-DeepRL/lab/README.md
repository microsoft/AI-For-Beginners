# 训练山地车逃脱

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

你的目标是训练 RL 代理控制 [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) 在 OpenAI 环境中。你将基于截至 2023 年 10 月的数据进行训练。

## 环境

山地车环境由困在山谷中的汽车组成。你的目标是跳出山谷并到达旗帜。你可以执行的动作是向左加速、向右加速或什么都不做。你可以观察汽车在 x 轴上的位置和速度。

## 启动笔记本

通过打开 [MountainCar.ipynb](../../../../../../lessons/6-Other/22-DeepRL/lab/MountainCar.ipynb) 开始实验。

## 收获

你应该在整个实验中了解到，将 RL 算法应用于新环境通常相当简单，因为 OpenAI Gym 为所有环境提供相同的接口，因此算法在很大程度上不依赖于环境的性质。你甚至可以以某种方式重构 Python 代码，以便将任何环境作为参数传递给 RL 算法。

**免责声明**：  
本文件使用机器翻译的AI翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而产生的任何误解或误释不承担责任。