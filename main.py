from helper import *

FILE_PATH = 'Images/3 by 3 orthogonal maze.png'
image = load_image(FILE_PATH)
WIDTH = get_width(image)
HEIGHT = get_height(image)
binary_maze = image_to_array(WIDTH, HEIGHT, image)
s = get_start(binary_maze, WIDTH)
e = get_end(binary_maze, WIDTH, HEIGHT)
node = shortest_path(binary_maze, s, 0, e, HEIGHT-1, WIDTH, HEIGHT)
draw_path(image, node)
image.show()
