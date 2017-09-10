"""

"""
from draw_kmeans import KMeans
import random
import numpy as np

class Settings:
    def __init__(self):
        self.canvas_size = (2000, 2000)  # x, y
        self.canvas_margin = 30
        self.cluster_number = 5
        # self.cluster_color = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]
        self.data_number = 30000
        self.max_square_spread = 200


def add(x, y, spread):
    x += random.randint(-spread, spread)
    y += random.randint(-spread, spread)
    return x, y

def random_point():
    for i in range(st.data_number):
        pos_x = random.uniform(st.canvas_margin, st.canvas_size[0] - st.canvas_margin)
        pos_y = random.uniform(st.canvas_margin, st.canvas_size[1] - st.canvas_margin)
        pos = (pos_x, pos_y)
        cv.add_data(pos)

def add_square():
    for i in range(st.cluster_number+1):
        x = random.randint(st.canvas_margin, st.canvas_size[0] - st.canvas_margin)
        y = random.randint(st.canvas_margin, st.canvas_size[1] - st.canvas_margin)  # center position
        d_x = np.minimum(np.abs(x-st.canvas_margin), st.canvas_size[0]-st.canvas_margin)
        d_y = np.minimum(np.abs(y-st.canvas_margin), st.canvas_size[1]-st.canvas_margin)
        spread = np.minimum(d_x, d_y)
        spread = np.minimum(spread, st.max_square_spread)
        for j in range(st.data_number // st.cluster_number):
            pos = add(x, y, spread)
            cv.add_data(pos)


if __name__ == "__main__":
    st = Settings()
    cv = KMeans()
    cv.set_cluster_number(st.cluster_number)

    #random_point()
    add_square()

    cv.set_canvas_size(st.canvas_size[0], st.canvas_size[1])
    cv.set_canvas_background_color((255, 255, 255))

while True:
    cv.draw()
    cv.canvas.save("km00.png")
    count = 0
    while cv.last_move_count != 0:
        count += 1
        cv.run()
        cv.draw()
        cv.canvas.save("km{0:02d}.png".format(count))
        print("run:", cv.run_count, "  moved: ", cv.last_move_count)


    try:
        print("enter new cluster number or string to end")
        new_cluster_number = int(input())
    except:
        print("end")
        break

    cv.reset(new_cluster_number)




