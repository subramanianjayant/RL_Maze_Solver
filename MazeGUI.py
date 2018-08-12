from turtle import *
import Maze_Generator as mazegen
from PIL import Image, ImageDraw

def draw_maze(maze,policy,current_pos):
    rows = maze.shape[0]
    columns = maze.shape[1]
    image = Image.new(mode='RGB',size = (600,600), color=255)
    draw = ImageDraw.Draw(image)
    start = 0
    end = image.height
    x_step = int(end/rows)
    y_step = int(end/columns)

    #draws maze based on array
    for x in range(0,rows):
        for y in range(0,columns):
            if maze[y,x] == 0: #GUI coordinates are transposed
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'white',outline='black')
            if maze[y,x] == 1:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'blue',outline='black')
            if maze[y,x] == 2:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'green',outline='black')
            if maze[y,x] == 5:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'black',outline='black')

    show_path(policy,current_pos,draw,image)
    del draw
    image.show()
    #image.save('maze.jpeg','JPEG')

#shows shortest path from current_pos to end
def show_path(policy,current_pos,draw,image):
    x = current_pos[0]
    y = current_pos[1]
    rows = policy.shape[0]
    columns = policy.shape[1]
    start = 0
    end = image.height
    x_step = int(end/rows)
    y_step = int(end/columns)

    draw.rectangle([y*y_step,x*x_step,(y+1)*y_step,(x+1)*x_step],
    fill = 'yellow',outline='black')
    if policy[x,y] == 1:
        show_path(policy,(x-1,y),draw,image)
    if policy[x,y] == 2:
        show_path(policy,(x+1,y),draw,image)
    if policy[x,y] == 3:
        show_path(policy,(x,y-1),draw,image)
    if policy[x,y] == 4:
        show_path(policy,(x,y+1),draw,image)
