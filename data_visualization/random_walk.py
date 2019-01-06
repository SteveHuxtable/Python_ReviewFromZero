# 我们今天学写一个一维数轴上的随机漫步模拟

from random import choice
import matplotlib.pyplot as plt
import pygal

class RandomWalk():
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s = 15)
plt.show()
plt.close()

# use pygal to draw a figure
hist = pygal.Bar()
hist.title = "This is a Histogram"
hist.x_labels = ['a', 'b', 'c', 'd', 'e']
hist.x_title = "Char"
hist.y_title = "Not care"

hist.add('Test', [10, 11, 12, 13, 14, 15])
hist.render_to_file('output_fig.svg')
