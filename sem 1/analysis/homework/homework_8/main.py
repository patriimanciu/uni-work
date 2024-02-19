import numpy as np
import matplotlib.pyplot as plt


def in_unit_ball(x, y, p):
    return (np.abs(x) ** p + np.abs(y) ** p) ** (1 / p) < 1


x_vals = np.linspace(-1, 1, 400)
y_vals = np.linspace(-1, 1, 400)

np.random.seed(60)
x_samples = np.random.uniform(-1.25, 1.25, 10000)
y_samples = np.random.uniform(-1.25, 1.25, 10000)


for p in [0.5, 0.75, 1.25, 1.5, 3, 8]:
    inside_ball = in_unit_ball(x_samples, y_samples, p)

    plt.figure(figsize=(10, 10))
    plt.scatter(x_samples[inside_ball], y_samples[inside_ball], color='teal', label='Inside Ball', alpha=0.2)
    plt.scatter(x_samples[~inside_ball], y_samples[~inside_ball], color='red', label='Outside Ball', alpha=0.05)

    plt.title(f'Unit Ball in R for $p = {p}$-norm')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
