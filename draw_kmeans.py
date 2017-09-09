"""

"""

from kmeans import *
from PIL import Image


class KMeans(KMeansCore):
    def __init__(self):
        super().__init__()
        self.canvas = Image
        self.canvas_size_x = int
        self.canvas_size_y = int
        self.canvas_background_color = (255, 255, 255)
        self.draw_point_size = (5, 5)
        self.point_color_list = [
            (0, 0, 255),  # blue
            (255, 0, 0),  # red
            (0, 255, 0),  # green
            (255, 255, 0),  # yellow
            (0, 255, 255),  # cyan
            (255, 0, 255), ]  # magenta

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
        print(canvas_size, self.canvas_background_color)
        self.canvas = Image.new("RGB", canvas_size, self.canvas_background_color)

    def draw_points(self):
        for i in self.cluster_list:
            color = self.point_color_list[i.id]
            marker = Image.new("RGB", self.draw_point_size, color)

            for j in i.data_list:
                pos = (int(j.pos_x), int(j.pos_y))
                self.canvas.paste(marker, pos)
