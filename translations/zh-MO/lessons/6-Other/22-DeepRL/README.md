# 深度強化學習

強化學習（RL）被視為機器學習的基本範式之一，與監督學習和非監督學習並列。在監督學習中，我們依賴已知結果的數據集，而強化學習則基於**透過行動來學習**。例如，當我們第一次看到一個電腦遊戲時，即使不知道規則，我們也會開始玩，並且很快就能透過遊玩和調整行為來提升技能。

## [課前測驗](https://ff-quizzes.netlify.app/en/ai/quiz/43)

要進行強化學習，我們需要：

* 一個**環境**或**模擬器**，用來設定遊戲規則。我們應該能夠在模擬器中運行實驗並觀察結果。
* 一些**獎勵函數**，用來指示實驗的成功程度。以學習玩電腦遊戲為例，獎勵可以是我們的最終得分。

基於獎勵函數，我們應該能夠調整行為並提升技能，以便下次表現更好。強化學習與其他類型的機器學習的主要區別在於，強化學習通常直到遊戲結束才知道是否贏或輸。因此，我們無法判斷某個單獨的動作是否是好的——只有在遊戲結束時才會收到獎勵。

在強化學習過程中，我們通常會進行許多實驗。在每次實驗中，我們需要在遵循目前學到的最佳策略（**利用**）和探索新的可能狀態（**探索**）之間取得平衡。

## OpenAI Gym

一個非常棒的強化學習工具是 [OpenAI Gym](https://gym.openai.com/)——一個**模擬環境**，可以模擬許多不同的環境，從 Atari 遊戲到物理學中的平衡問題。它是訓練強化學習算法最受歡迎的模擬環境之一，由 [OpenAI](https://openai.com/) 維護。

> **注意**：你可以在 [這裡](https://gym.openai.com/envs/#classic_control) 查看 OpenAI Gym 提供的所有環境。

## CartPole 平衡

你可能都見過現代的平衡裝置，例如 *Segway* 或 *Gyroscooters*。它們能夠透過加速計或陀螺儀的信號自動調整輪子來保持平衡。在本節中，我們將學習如何解決類似的問題——平衡一根桿子。這類似於馬戲團表演者需要在手上平衡桿子的情況——但這裡的桿子平衡僅發生在一維空間。

一個簡化版的平衡問題被稱為 **CartPole** 問題。在 CartPole 世界中，我們有一個可以左右移動的水平滑塊，目標是讓滑塊上的垂直桿子保持平衡。

<img alt="a cartpole" src="../../../../../translated_images/zh-MO/cartpole.f52a67f27e058170.webp" width="200"/>

要創建並使用這個環境，我們只需要幾行 Python 代碼：

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

每個環境都可以以相同的方式訪問：
* `env.reset` 開始一個新的實驗
* `env.step` 執行一個模擬步驟。它接收來自**動作空間**的**動作**，並返回**觀察值**（來自觀察空間）、獎勵以及終止標誌。

在上面的例子中，我們在每一步執行隨機動作，因此實驗的生命週期非常短：

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

強化學習算法的目標是訓練一個模型——所謂的**策略** &pi;——它能根據給定的狀態返回相應的動作。我們也可以將策略視為概率性的，例如對於任意狀態 *s* 和動作 *a*，它會返回 &pi;(*a*|*s*) 的概率，表示在狀態 *s* 下應該採取動作 *a*。

## 策略梯度算法

建模策略的最明顯方法是創建一個神經網絡，該網絡以狀態作為輸入，並返回相應的動作（或所有動作的概率）。在某種意義上，它類似於普通的分類任務，但有一個主要區別——我們事先並不知道每一步應該採取哪些動作。

這裡的想法是估算這些概率。我們構建一個**累積獎勵**向量，顯示實驗中每一步的總獎勵。我們還通過乘以某個係數 &gamma;=0.99 來應用**獎勵折扣**，以減少早期獎勵的影響。然後，我們加強那些在實驗路徑中產生較大獎勵的步驟。

> 了解更多關於策略梯度算法的內容，並在[示例筆記本](CartPole-RL-TF.ipynb)中查看其實際應用。

## Actor-Critic 算法

策略梯度方法的一個改進版本被稱為 **Actor-Critic**。其主要思想是神經網絡將被訓練來返回兩個結果：

* 策略，決定應採取的動作。這部分被稱為 **actor**。
* 對當前狀態下可期望獲得的總獎勵的估算——這部分被稱為 **critic**。

在某種意義上，這種架構類似於 [GAN](../../4-ComputerVision/10-GANs/README.md)，其中有兩個網絡相互對抗訓練。在 Actor-Critic 模型中，actor 提出需要採取的動作，而 critic 則進行批判並估算結果。然而，我們的目標是讓這些網絡協同訓練。

由於我們在實驗中同時知道真實的累積獎勵和 critic 返回的結果，因此構建一個損失函數來最小化它們之間的差異相對容易。這將給我們**critic 損失**。我們可以使用與策略梯度算法相同的方法來計算**actor 損失**。

運行其中一個算法後，我們可以期望 CartPole 的表現如下：

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ 練習：策略梯度和 Actor-Critic 強化學習

在以下筆記本中繼續學習：

* [TensorFlow 中的強化學習](CartPole-RL-TF.ipynb)
* [PyTorch 中的強化學習](CartPole-RL-PyTorch.ipynb)

## 其他強化學習任務

如今，強化學習是一個快速增長的研究領域。一些有趣的強化學習例子包括：

* 教電腦玩 **Atari 遊戲**。這個問題的挑戰在於我們沒有簡單的狀態向量，而是截圖——我們需要使用 CNN 將屏幕圖像轉換為特徵向量或提取獎勵信息。Atari 遊戲可在 Gym 中使用。
* 教電腦玩棋盤遊戲，例如象棋和圍棋。最近，像 **Alpha Zero** 這樣的最先進程序是通過兩個代理相互對弈並逐步改進來從零開始訓練的。
* 在工業中，強化學習被用於從模擬中創建控制系統。一項名為 [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) 的服務專門為此設計。

## 結論

我們現在已經學會如何僅通過提供定義遊戲期望狀態的獎勵函數，並給代理智能探索搜索空間的機會來訓練代理以取得良好結果。我們成功嘗試了兩種算法，並在相對較短的時間內取得了良好的結果。然而，這只是你進入強化學習旅程的開始，如果你想深入研究，應該考慮參加專門的課程。

## 🚀 挑戰

探索「其他強化學習任務」部分列出的應用，並嘗試實現其中一個！

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## 回顧與自學

在我們的[初學者機器學習課程](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md)中了解更多關於經典強化學習的內容。

觀看[這段精彩影片](https://www.youtube.com/watch?v=qv6UVOQ0F44)，了解電腦如何學習玩超級瑪利歐。

## 作業：[訓練一個山地車](lab/README.md)

在這次作業中，你的目標是訓練一個不同的 Gym 環境——[山地車](https://www.gymlibrary.ml/environments/classic_control/mountain_car/)。

---

