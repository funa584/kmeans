"""

"""

from kmeans import *
from PIL import Image
import numpy as np


class KMeans(KMeansCore):
    def __init__(self):
        super().__init__()
        self.canvas = Image
        self.canvas_size_x = int
        self.canvas_size_y = int
        self.canvas_background_color = (255, 255, 255)
        self.draw_point_size = 8
        self.point_color_list = [
            (0, 0, 255),  # blue
            (255, 0, 0),  # red
            (0, 255, 0),  # green
            (255, 255, 0),  # yellow
            (0, 255, 255),  # cyan
            (255, 0, 255),  # magenta
            (128, 0, 0),
            (0, 128, 0),
            (0, 0, 128),
            (128, 128, 0),
            (128, 0, 128),
            (0, 128, 128),
            (64, 0, 0),
            (0, 64, 0),
            (0, 0, 64),
            (64, 64, 0),
            (64, 0, 64),
            (0, 64, 64),
            (64, 64, 64)
        ]
        self.marker_border_color = (0, 0, 0)

    def set_canvas_size(self, size_x: int, size_y: int):
        self.canvas_size_x = size_x
        self.canvas_size_y = size_y

    def set_canvas_background_color(self, color: tuple):
        self.canvas_background_color = color

    def set_point_color(self, color_list: list):
        self.point_color_list = color_list

    def draw(self):
        self.new_canvas()
        self.draw_points()

    def new_canvas(self):
        canvas_size = (self.canvas_size_x, self.canvas_size_y)
        self.canvas = Image.new("RGB", canvas_size, self.canvas_background_color)

    def draw_points(self):
        for i in self.cluster_list:
            color = self.point_color_list[i.id]
            marker = self.create_marker(color)

            for j in i.data_list:
                pos = (int(j.pos_x), int(j.pos_y))
                self.canvas.paste(marker, pos)

    def create_marker(self, color):
        # square
        marker = Image.new("RGB", (self.draw_point_size, self.draw_point_size), color)
        arr = np.array(marker)
        for i in range(self.draw_point_size):  # draw border
            arr[0][i] = self.marker_border_color  # left
            arr[self.draw_point_size-1][i] = self.marker_border_color  # right
            arr[i][0] = self.marker_border_color  # top
            arr[i][self.draw_point_size-1] = self.marker_border_color  # bottom

        return Image.fromarray(arr)
