# RL_Maze_Solver

Generates and solves mazes in the shortest path using simple MDP solving techniques like Value Iteration. All algorithms are coded from scratch.

(Policy Iteration, Q-learning, potentially MCTS to be added later)

### Running the code

Simply download the files and run the code of the algorithm you want to use to solve the maze:
```
/Users/subra/Desktop/git/RL_Maze_Solver$ Value_Iteration.py
```
The output in the terminal should be the maze and the policy in ndarray format:
```
[[5. 5. 5. 5. 0. 0. 0. 5. 0. 0. 5. 1. 5. 5. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 5. 5. 0. 5. 5. 5. 0. 5. 5. 0. 0. 5. 5.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 5. 0. 0. 5. 5. 5. 5. 5. 5. 5. 0. 0. 5. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 0. 5. 5. 0. 5. 5. 0. 5. 0. 5. 5. 0. 5. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 0. 0. 5. 5. 5. 5. 0. 5. 5. 5. 5. 5. 5. 5.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 5. 5. 5. 5. 5. 0. 5. 5. 5. 5. 5. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 5. 0. 5. 0. 0. 5. 5. 5. 5. 5. 5. 0. 5. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 5. 5. 5. 5. 2. 0. 5. 5. 5. 5. 5. 0. 0. 5.]]
[[nan nan nan nan  2.  2.  2. nan  2.  2. nan  2. nan nan  2.]
 [ 2.  2.  3.  4.  2.  3.  3.  3.  2.  4.  4.  2.  2.  3.  3.]
 [ 2.  2. nan nan  2. nan nan nan  2. nan nan  2.  2. nan nan]
 [ 2.  3.  2.  2.  3.  3.  3.  3.  4.  4.  4.  2.  2.  3.  2.]
 [ 2. nan  2.  2. nan nan nan nan nan nan nan  2.  2. nan  2.]
 [ 4.  2.  3.  4.  2.  4.  4.  2.  3.  2.  3.  3.  2.  3.  2.]
 [nan  2. nan nan  2. nan nan  2. nan  2. nan nan  2. nan  2.]
 [ 4.  2.  2.  3.  4.  4.  4.  2.  3.  3.  3.  3.  3.  3.  3.]
 [nan  2.  2. nan nan nan nan  2. nan nan nan nan nan nan nan]
 [ 4.  4.  4.  4.  4.  4.  2.  3.  3.  3.  3.  3.  2.  2.  2.]
 [nan nan nan nan nan nan  2. nan nan nan nan nan  2.  2.  2.]
 [ 4.  4.  2.  4.  2.  2.  3.  3.  3.  3.  3.  3.  2.  3.  2.]
 [nan nan  2. nan  2.  2. nan nan nan nan nan nan  2. nan  2.]
 [ 4.  4.  4.  4.  4.  2.  2.  3.  3.  3.  3.  3.  3.  3.  3.]
 [nan nan nan nan nan  0.  3. nan nan nan nan nan  1.  1. nan]]
 ```
 An image of the maze with the shortest path from start to finish should also display 
 with the path highlighed in yellow:
 
 
