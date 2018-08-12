import numpy as np
import math
import random
import Maze_Generator as mazegen
import MazeGUI

gamma = 0.5
ROWS = 25
COLUMNS = 25
START_POS = (0,random.randint(0,14))

actions = {"up":[-1,0],"down":[1,0],"left":[0,-1],"right":[0,1]}
action_signals = {1:'up',2:'down',3:'left',4:'right'}
maze = mazegen.generate_maze(rows = ROWS, columns = COLUMNS, start_pos = START_POS)
rewards = mazegen.generate_rewards(maze)

def transition(state,action): #can add stochastisity later
    next_state = np.array(state)+np.array(actions[action])
    if next_state[0]<0 or next_state[0]>=ROWS or next_state[1]<0 or next_state[1]>=COLUMNS:
        next_state = state
    return tuple(next_state)

values = np.zeros(shape = rewards.shape)
for iteration in range(0,500):
    values_prime = values.copy()
    for x in range(0,ROWS):
        for y in range(0,COLUMNS):
            next_value = rewards[x,y]
            possible_futures = []
            for action in actions:
                next_state = transition([x,y],action)
                possible_futures.append(gamma*values[next_state])
            max_future = np.array(possible_futures).max()
            values_prime[x,y] = next_value+max_future
    values = values_prime

policy = np.zeros(shape=values.shape)
for x in range(0,ROWS):
    for y in range(0,COLUMNS):
        pot_value = -100000
        for signal in action_signals:
            val = values[transition([x,y],action_signals[signal])]
            if val >pot_value:
                pot_value = val
                policy[x,y]=signal
        if maze[x,y]==5:
            policy[x,y]=np.nan
        if maze[x,y]==2:
            policy[x,y] = 0

print(maze)
print(policy)
MazeGUI.draw_maze(maze,policy,START_POS)
#MazeGUI.show_path(policy,START_POS)
