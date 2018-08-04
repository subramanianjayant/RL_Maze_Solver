from turtle import *
import Maze_Generator as mazegen
from PIL import Image, ImageDraw

def draw_maze(maze):
    rows = maze.shape[0]
    columns = maze.shape[1]
    image = Image.new(mode='RGB',size = (600,600), color=255)
    draw = ImageDraw.Draw(image)
    start = 0
    end = image.height
    x_step = int(end/rows)
    y_step = int(end/columns)

    for x in range(0,rows):
        for y in range(0,columns):
            if maze[x,y] == 0:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'white',outline='black')
            if maze[x,y] == 1:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'blue',outline='black')
            if maze[x,y] == 2:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'green',outline='black')
            if maze[x,y] == 5:
                draw.rectangle([x*x_step,y*y_step,(x+1)*x_step,(y+1)*y_step],
                fill = 'black',outline='black')
    del draw
    image.rotate(270).show()

if __name__=='__main__':
    maze = mazegen.generate_maze(10,10)
    draw_maze(maze)
