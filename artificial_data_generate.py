# Author: Teng Fu
# Contact: ggathrun@googlemail.com
# this script aims to produces the moons and circle
# datasets as the example shows in the paper.
# reference for scikit-learn dataset module sample generation.
# http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py
# all generated sample sets are binary based dataset.

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# define the number of samples that is generated.
n_samples = 1000
# a relatively lower noise level, make the result more understandable.
noise_level = 0.1
# set up random state for re-produce
random_state = 100

x_moon, y_moon = datasets.make_moons(n_samples=n_samples,
                                     noise=noise_level,
                                     random_state=random_state)
np.save("x_moon.npy", x_moon)
np.save("y_moon.npy", y_moon)

x_circle, y_circle = datasets.make_circles(noise=noise_level,
                                           factor=0.5,
                                           n_samples=n_samples,
                                           random_state=random_state)
np.save("x_circle.npy", x_circle)
np.save("y_circle.npy", y_circle)

data_sample = [[x_moon, y_moon], [x_circle, y_circle]]
data_title_name_dict = {0: "moon_samples", 1: "circle_samples"}
color_dict = {0: "red", 1: "blue"}


def draw_sample_plot(data_input, plot_title):
    x = data_input[0]
    y = data_input[1]

    reds = y == 0
    blues = y == 1

    plt.figure()
    plt.title(plot_title)
    plt.scatter(x[reds, 0], x[reds, 1], c="red")
    plt.scatter(x[blues, 0], x[blues, 1], c="blue")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    fname = plot_title+str(".png")
    plt.savefig(fname)
    # always call savefig function before show()
    plt.show()
    return


def main(data_input):
    for i in range(2):
        draw_sample_plot(data_input[i], data_title_name_dict[i])
    return


if __name__ == '__main__':
    main(data_sample)
