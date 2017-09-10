"""

"""
from draw_kmeans import KMeans
import random
import numpy as np

class Settings:
    def __init__(self):
        self.canvas_size = (1000, 1000)  # x, y
        self.canvas_margin = 30
        self.cluster_number = 5
        self.cluster_color = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]
        self.data_number = 1000


def add(x, y, spread):
    x += random.randint(-spread, spread)
    y += random.randint(-spread, spread)
    return x, y

if __name__ == "__main__":
    st = Settings()
    cv = KMeans()
    cv.set_cluster_number(st.cluster_number)
    """
    for i in range(st.data_number):
        pos_x = random.uniform(st.canvas_margin, st.canvas_size[0] - st.canvas_margin)
        pos_y = random.uniform(st.canvas_margin, st.canvas_size[1] - st.canvas_margin)
        pos = (pos_x, pos_y)
        cv.add_data(pos)
    """
    for i in range(20):
        x = random.randint(st.canvas_margin, st.canvas_size[0] - st.canvas_margin)
        y = random.randint(st.canvas_margin, st.canvas_size[1] - st.canvas_margin)  # center position
        d_x = np.minimum(np.abs(x-st.canvas_margin), st.canvas_size[0]-st.canvas_margin)
        d_y = np.minimum(np.abs(y-st.canvas_margin), st.canvas_size[1]-st.canvas_margin)
        spread = np.minimum(d_x, d_y)
        for j in range(30):
            pos = add(x, y, spread)
            cv.add_data(pos)

    cv.set_canvas_size(st.canvas_size[0], st.canvas_size[1])
    cv.set_canvas_background_color((230, 230, 230))

    cv.draw()
    cv.canvas.save("km00.png")
for i in range(1, 20):
    cv.run()
    cv.draw()
    # cv.canvas.show()
    cv.canvas.save("km{0:02d}.png".format(i))
