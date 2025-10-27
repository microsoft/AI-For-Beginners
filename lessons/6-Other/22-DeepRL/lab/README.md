# Training Mountain Car to Escape

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Your goal is to train the RL agent to control [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) in OpenAI Environment.

<img alt="Mountain Car" src="images/mountaincar.png" width="300"/>

## The Environment

Mountain Car environment consists of the car trapped inside a valley. Your goal is to jump out of the valley and reach the flag. The actions you can perform are to accelerate to the left, to the right, or do nothing. You can observe position of the car along x-axis, and velocity.

## Starting Notebook

Start the lab by opening [MountainCar-Lab.ipynb](MountainCar-Lab.ipynb). This notebook provides starter code for the Policy Gradient algorithm and guides you through the process of training the agent.

## Takeaway

You should learn throughout this lab that adopting RL algorithms to a new environment is often quite straightforward, because the OpenAI Gym has the same interface for all environments, and algorithms as such do not largely depend on the nature of the environment. You can even restructure the Python code in such a way as to pass any environment to RL algorithm as a parameter.
