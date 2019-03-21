# Maze_Solver_Reinforcement_Learning

A Q-Learning agent which finds the optimum escape route.

![Maze_image](https://user-images.githubusercontent.com/36446402/54755746-a26ece00-4c0c-11e9-8d36-22fddc15f4a8.PNG)

In a nutshell, there’s an agent in an environment which performs certain actions as a result of which, it’s state changes. Ultimately, the agent learns a policy which tells it which action to take under certain circumstances. Executing an action in a specific state provides the agent with a numerical score called a reward. The main target of the agent is to maximize this reward.

Let’s imagine a dumb virtual agent which is trapped inside a house. The aim of this innocent agent is to just get out of the house. So in this case, each room of the house is a state and the agent’s movement from one room to another is an action.

This is similar to teaching a dog to fetch a ball. For instance, when you throw the ball for the first time, the dog might just be staring at you. Next time it might maybe go in the right direction. If it does, you give it a piece of biscuit as it’s reward. Next time when you throw the ball, it will remember that it has to go in the direction of the ball because of the reward. After a few more throws, it might try to grab the ball using its teeth. So you again give him a piece of biscuit as a reward. Each throw of the ball in this case is a new iteration. Over time, the dog starts to understand that if it goes in the right direction, grabs the ball using its teeth and returns, it’ll receive a piece of biscuit. So after a couple of throws, your dog should be able to fetch a ball. The biscuits are an incentive for doing the right action in the right scenario. With more throws (iterations), it gets more trained to fetch balls. Over time, perfection!
You can view the maze that I've used in my code by opening the Maze.PNG file. Feel free to run the code and play around.
