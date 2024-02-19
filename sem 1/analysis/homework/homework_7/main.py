import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x ** 2)


# ∫f(x)dx ≈ [(b - a) / n] * ( 1/2 f(a) + ∑{1}{n - 1} f(x_k) + 1/2 f(b)
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    return S


def plot(a, b, n):
    """
    plots the function f(x) between a and b
    """
    x_values = np.linspace(a, b, n)
    y_values = f(x_values)

    plt.figure(figsize=(15, 10))
    plt.plot(x_values, y_values, label=r'$e^{-x^2}$', )

    for i in range(len(x_values) - 1):
        plt.fill_between(x_values[i:i + 3], y_values[i:i + 3], step="mid")

    plt.xlabel('x')
    plt.title('Plot of $e^{-x^2}$')
    plt.grid(True)
    plt.ylabel(r'$e^{-x^2}$')
    plt.show()


a = -5
b = 5
n = 500

plot(a, b, n)

# we know that the area should be √π
sqrt_pi = np.sqrt(np.pi)
trapezoidal_result = trapezoidal_rule(a, b, n)

print(
    f"For a = {a}, b = {b} and n = {n} the trapezoidal rule gives us {trapezoidal_result} and the actual result is √π = {sqrt_pi}")


def trapezoidal_aprox():
    n_trapezoids = 1000

    f_values = np.arange(1, 8, 0.1)

    approximation_values = [trapezoidal_rule(-f, f, n_trapezoids) for f in f_values]

    plt.plot(f_values, approximation_values, label='Trapezoidal Rule Approximation')
    plt.axhline(np.sqrt(np.pi), color='red', linestyle='dotted', label=r'$\sqrt{\pi}$')
    plt.title('Trapezoidal Rule Approximation vs. sqrt(pi)')
    plt.xlabel('Value of f')
    plt.ylabel('Approximation')
    plt.legend()
    plt.show()


trapezoidal_aprox()
