"""

"""

from data import *
import random
import math


class KMeansCore:
    """
    set_cluster_number
    add_data
    run

    """
    def __init__(self):
        self.cluster_list = []
        self.data_list = []
        self.cluster_number = 0
        self.data_number = 0

    def set_cluster_number(self, number):
        self.cluster_number = number
        self.cluster_list = []  # delete exists
        for i in range(number):
            cluster = Cluster()
            cluster.id = i
            self.cluster_list.append(cluster)

    def add_data(self, position: tuple):
        if str(type(self.cluster_number)) != "<class 'int'>" or self.cluster_number < 0:
            raise Exception

        data = Point()
        data.pos_x = float(position[0])
        data.pos_y = float(position[1])
        data.belong_cluster = random.randint(0, self.cluster_number - 1)
        self.data_list.append(data)
        self.cluster_list[data.belong_cluster].data_list.append(data)
        self.data_number += 1
        self.cluster_list[data.belong_cluster].data_number += 1

    def run(self):
        self.calc_center()
        self.reassign_data()

    def calc_center(self):
        for i in self.cluster_list:
            sum_x = 0
            sum_y = 0
            for j in i.data_list:
                sum_x += j.pos_x
                sum_y += j.pos_y
            i.centroid_x = sum_x / i.data_number
            i.centroid_y = sum_y / i.data_number

    def reassign_data(self):
        for i in self.cluster_list:
            i.data_list = []  # reset list
            i.data_number = 0
        for i in self.data_list:
            self.find_closest(i)
            self.cluster_list[i.belong_cluster].data_list.append(i)
            self.cluster_list[i.belong_cluster].data_number += 1

    def find_closest(self, data: Point):
        closest = float("inf")
        for i in self.cluster_list:
            a = math.pow(data.pos_x - i.centroid_x, 2)
            b = math.pow(data.pos_y - i.centroid_y, 2)
            distance = math.sqrt(a + b)
            if distance < closest:
                closest = distance
                data.belong_cluster = i.id
