class Point:
    def __init__(self):
        self.pos_x = float
        self.pos_y = float
        self.belong_cluster = int


class Cluster:
    def __init__(self):
        self.id = int
        self.data_number = 0
        self.data_list = []
        self.centroid_x = float
        self.centroid_y = float
