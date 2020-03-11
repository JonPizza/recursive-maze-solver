from PIL import Image
from time import sleep
import sys


def open_img(img, dim):
    img = Image.open(img)
    px_map = []
    for x in range(dim):
        px_row = []
        for y in range(dim):
            px_row.append('b' if img.load()[y, x] == (0, 0, 0, 255) else 'w')
        px_map.append(px_row)
    return px_map


def show_image(img_list):
    print('\n\n')
    for i in img_list:
        p = ''
        for x in i:
            if x == 'r':
                p += '\033[41m  \033[0m'
            elif x == 'b':
                p += '\033[40m  \033[0m'
            elif x == 'w':
                p += '\033[47m  \033[0m'
        print(p)


def solve(maze):
    path = [(0, maze[0].index('w'))]
    win = [len(maze), maze[-1].index('w')]
    try: 
        recurse_solve(maze, win, path)
    except:
        return 'Done!'

def recurse_solve(maze, win, path):
    if win in path:
        return 'SOLVED!!!'
    if maze[path[-1][0]][path[-1][1]] == 'b' or maze[path[-1][0]][path[-1][1]] == 'r' or path[-1] in path[:-1]:
        return []
    maze[path[-1][0]][path[-1][1]] = 'r'
    show_image(maze)
    sleep(0.03)

    r1 = recurse_solve(maze, win, path+[(path[-1][0]+1, path[-1][1])])
    r2 = recurse_solve(maze, win, path+[(path[-1][0], path[-1][1]+1)])
    r3 = recurse_solve(maze, win, path+[(path[-1][0]-1, path[-1][1])])
    r4 = recurse_solve(maze, win, path+[(path[-1][0], path[-1][1]-1)])
    arrs = [len(r1), len(r2), len(r3), len(r4)]
    if arrs.index(max(arrs)) == 0:
        return r1 
    elif arrs.index(max(arrs)) == 1:
        return r2
    elif arrs.index(max(arrs)) == 2:
        return r3 
    else:
        return r4


maze = open_img(input('da maze 2 solve: '), 32)
solve(maze)
