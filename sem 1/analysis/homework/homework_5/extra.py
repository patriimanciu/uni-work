import numpy as np
import matplotlib.pyplot as plt


def weierstrass_funtion(x, a, b, n = 100):
    # f(x)=∑ a^n * cos(b^n*πx)
    result = 0
    for k in range(n):
        result += a ** k * np.cos(b ** k * np.pi * x)
    return result

"""
    a and b have to be chosen to satisfy specific conditions for the function to be 
        0 < a < 1
        b = 2k + 1, b > 1
    The function is continuous since it is a sum of continuous functions
    
"""


if __name__ == "__main__":
    a = 0.5
    b = 3

    x = np.linspace(-1, 1, 1000)

    y = weierstrass_funtion(x, a, b)

    plt.plot(x, y)
    plt.title("Weierstrass function")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()