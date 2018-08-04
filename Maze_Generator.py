import numpy as np
import math
import numpy.random as random
#maybe instantiate Maze object, include a class

def generate_maze(rows=10, columns=10, start_pos = (0,0)):
    maze = np.zeros(shape=(rows,columns))
    maze[start_pos] = 1 #starting point
    maze[rows-1,columns-1] = 2 #goal
    #put in actual maze generation algorithm later
    for x in range(0,rows,2):
        for y in range(0,columns):
            if random.random()<0.8:
                if maze[x,y]!=2 and maze[x,y]!=1:
                    maze[x,y] = 5 #walls
    return maze

def generate_rewards(maze):
    rewards_dict = {0:-1,1:-1,2:10000,5:-10000}
    rewards = np.zeros(shape = maze.shape)
    for x in range(0,rewards.shape[0]):
        for y in range(0,rewards.shape[1]):
            type = maze[x,y]
            rewards[x,y] = rewards_dict[type]
    return rewards

def generate_init_policy(maze): #possible policy iteration
    action_signals = {1:'up',2:'down',3:'left',4:'right'}
    rows = maze.shape[0]
    columns = maze.shape[1]
    policy = np.zeros(maze.shape)
    for x in range(0,rows):
        for y in range(0,columns):
            if random.random()>0.5:
                policy[x,y] = 2
            else:
                policy[x,y] = 4
    return policy

if __name__ == '__main__':
    maze = generate_maze()
    rewards = generate_rewards(maze)
    policy = generate_init_policy(maze)
    print(policy)
