"""

"""
from draw_kmeans import KMeans
import random


class Settings:
    def __init__(self):
        self.canvas_size = (1000, 1000)  # x, y
        self.canvas_margin = 30
        self.cluster_number = 5
        self.cluster_color = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]
        self.data_number = 1000


if __name__ == "__main__":
    st = Settings()
    cv = KMeans()
    cv.set_cluster_number(st.cluster_number)
    for i in range(st.data_number):
        pos_x = random.uniform(st.canvas_margin, st.canvas_size[0] - st.canvas_margin)
        pos_y = random.uniform(st.canvas_margin, st.canvas_size[1] - st.canvas_margin)
        pos = (pos_x, pos_y)
        cv.add_data(pos)

    for i in cv.data_list:
        pass
        # print(i.pos_x, i.pos_y)

    cv.set_canvas_size(st.canvas_size[0], st.canvas_size[1])
    cv.set_canvas_background_color((230, 230, 230))
    cv.draw()

    cv.canvas.show()


for i in range(10):
    cv.run()
    cv.draw()
    # cv.canvas.show()
    cv.canvas.save("km{0:02d}.png".format(i))
