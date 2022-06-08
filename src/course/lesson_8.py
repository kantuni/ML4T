import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(x):
    return (x - 1.5) ** 2 + 0.5


if __name__ == "__main__":
    x_guess = 2.0
    minimum = spo.minimize(f, x_guess, method="SLSQP", options={"disp": True})
    print("Minima found at x = ", minimum.x, ", f(x) = ", minimum.fun)

    # Plot function and mark minimum
    xs = np.linspace(0.5, 2.5)
    ys = f(xs)
    plt.plot(xs, ys)
    # NOTE: ro = red circle
    plt.plot(minimum.x, minimum.fun, "ro")
    plt.title("f(x) = (x - 1.5)^2 + 0.5")
    plt.show()
