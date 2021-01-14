from PIL import Image
from collections import deque
import sys


class Node:
    def __init__(self, width, height, parent):
        self.width = width
        self.height = height
        self.parent = parent

    def __repr__(self):
        return str((self.width, self.height))


def load_image(file_path):
    try:
        image = Image.open(file_path)
    except IOError:
        print('Could not load image.')
        sys.exit()
    return image


def display_image(image):
    image.show()


def get_width(image):
    return image.width


def get_height(image):
    return image.height


def image_to_array(width, height, image):
    array = [[0] * width for _ in range(height)]
    for h in range(height):
        for w in range(width):
            if image.getpixel((w, h)) != (0, 0, 0, 255):
                array[h][w] = 1
    return array


def get_start(maze, width):
    for i in range(width):
        if maze[0][i] == 1:
            return i


def get_end(maze, width, height):
    for i in range(width):
        if maze[height - 1][i] == 1:
            return i


def valid(w, h, width, height):
    return (0 <= w < width) and (0 <= h < height)


def shortest_path(maze, width, height, end_w, end_h, WIDTH, HEIGHT):
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    queue = deque()
    node = Node(width, height, None)
    queue.append(node)
    visited = set()
    point = (node.width, node.height)
    visited.add(point)
    while queue:
        current = queue.popleft()
        w = current.width
        h = current.height
        if w == end_w and h == end_h:
            return current
        value = maze[h][w]
        for i in range(4):
            new_w = w + col[i] * value
            new_h = h + row[i] * value
            if valid(new_w, new_h, WIDTH, HEIGHT):
                next_node = Node(new_w, new_h, current)
                point = (next_node.width, next_node.height)
                if point not in visited:
                    queue.append(next_node)
                    visited.add(point)
    return None


def print_path(node):
    if node is None:
        return 0
    length = print_path(node.parent)
    print(node, end=' ')
    return length + 1


def draw_path(image, node):
    while node:
        image.putpixel((node.width, node.height), (255, 0, 0))
        node = node.parent
