# Deep Q-Networks (DQN)

In the previous lesson, we explored the Policy Gradients and Actor-Critic algorithms. Now, we will dive into another powerful reinforcement learning algorithm: **Deep Q-Networks (DQN)**. DQN, introduced by DeepMind in 2015, was a major breakthrough in the field of RL, as it was the first algorithm to successfully learn to play a wide range of Atari 2600 games at a superhuman level, directly from raw pixel inputs.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

## Q-Learning and the Bellman Equation

At the core of DQN is **Q-Learning**, a value-based reinforcement learning algorithm. In Q-Learning, we aim to learn a **Q-function**, denoted as Q(s, a), which represents the expected total future reward (or "quality") of taking action 'a' in state 's'. The optimal Q-function, Q*(s, a), follows the **Bellman Equation**:

Q*(s, a) = E[r + γ * max<sub>a'</sub>(Q*(s', a')) | s, a]

This equation states that the optimal Q-value for a given state-action pair is the expected immediate reward 'r' plus the discounted (γ) maximum Q-value of the next state 's''.

## The Challenge of Large State Spaces

In traditional Q-Learning, the Q-function is represented as a table, with states as rows and actions as columns. However, this approach becomes impractical for problems with large state spaces, such as Atari games, where the state is represented by a high-dimensional image. This is where deep learning comes in.

## Deep Q-Networks (DQN)

DQN uses a deep neural network to approximate the Q-function, Q(s, a; θ), where θ represents the network's weights. This allows us to handle large, high-dimensional state spaces.

However, training a neural network to approximate the Q-function can be unstable. DQN introduces two key techniques to address this instability:

1.  **Experience Replay:** Instead of training the network on consecutive samples, which are highly correlated, DQN stores the agent's experiences (state, action, reward, next state) in a **replay buffer**. During training, it samples mini-batches of experiences from this buffer, breaking the temporal correlations and improving training stability.

2.  **Target Network:** DQN uses a separate **target network** to generate the target Q-values for the Bellman Equation. This target network is a copy of the main Q-network, but its weights are updated less frequently. This helps to stabilize the training process by providing a more stable target for the Q-value updates.

## The DQN Algorithm

The DQN algorithm can be summarized as follows:

1.  Initialize the Q-network and the target network with random weights.
2.  Initialize the replay buffer.
3.  For each episode:
    1.  Initialize the environment and get the initial state.
    2.  For each time step:
        1.  Select an action using an epsilon-greedy policy (explore or exploit).
        2.  Execute the action in the environment and observe the reward and the next state.
        3.  Store the experience in the replay buffer.
        4.  Sample a mini-batch of experiences from the replay buffer.
        5.  Calculate the target Q-values using the target network.
        6.  Update the Q-network by minimizing the loss between the predicted Q-values and the target Q-values.
        7.  Periodically update the target network with the weights of the Q-network.

## ✍️ Exercises: Deep Q-Networks

In the accompanying notebook, we will implement a DQN to play the Atari game "Pong". We will use PyTorch to build the Q-network and OpenAI Gym to simulate the game environment.

*   [DQN in PyTorch](DQN-Pong-PyTorch.ipynb)

## Conclusion

DQN is a powerful algorithm that combines the principles of Q-Learning with the representational power of deep neural networks. It has been successfully applied to a wide range of challenging reinforcement learning problems and has laid the foundation for many subsequent advancements in the field.

## 🚀 Challenge

Explore other Atari games in the OpenAI Gym and see if you can train a DQN to play them. You might need to adjust the hyperparameters of the algorithm for different games.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/46)
