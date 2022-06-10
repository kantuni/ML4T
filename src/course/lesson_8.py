from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(x: float) -> float:
    return (x - 1.5) ** 2 + 0.5


def error_line(line: np.ndarray, data: np.ndarray) -> float:
    """Computes error between the given line model and the original data."""
    c0, c1 = line
    x, y = data[:, 0], data[:, 1]
    return np.sum((y - (c0 * x + c1)) ** 2)


def fit_line(data: np.ndarray, error_fn: Callable) -> np.ndarray:
    """Fits a line to the given data, minimizing the error."""
    # Generate initial guess (x = 0, y = mean of ys)
    line_guess = np.array([0, np.mean(data[:, 1])])
    print("line guess", line_guess)
    c0_guess, c1_guess = line_guess
    x_guess = np.linspace(0, 10, 20)
    y_guess = c0_guess * x_guess + c1_guess
    # NOTE: m-- = magenta dashed line
    plt.plot(x_guess, y_guess, "m--", linewidth=2, label="Initial guess")

    # Use SciPy to minimize the error function
    result = spo.minimize(
        error_fn, line_guess, args=(data,), method="SLSQP", options={"disp": True}
    )
    return result.x


def error_poly(coeffs: np.ndarray, data: np.ndarray) -> float:
    """Computes error between the given polynomial model and the original data."""
    x, y = data[:, 0], data[:, 1]
    return np.sum((y - np.polyval(coeffs, x)) ** 2)


def fit_poly(data: np.ndarray, error_fn: Callable, degree=3) -> np.poly1d:
    """Fits a polynomial to the given data, minimizing the error."""
    # Generate initial guess (coeffs = [1, 1, 1, ...])
    poly_guess = np.poly1d(np.ones(degree + 1, dtype=np.float32))
    x_guess = np.linspace(-100, 100, 50)
    y_guess = np.polyval(poly_guess, x_guess)
    # NOTE: m-- = magenta dashed line
    plt.plot(x_guess, y_guess, "m--", linewidth=2, label="Initial guess")

    # Use SciPy to minimize the error function
    result = spo.minimize(
        error_fn, poly_guess, args=(data,), method="Nelder-Mead", options={"disp": True}
    )
    return np.poly1d(result.x)


if __name__ == "__main__":
    # x_guess = 2.0
    # minimum = spo.minimize(f, x_guess, method="SLSQP", options={"disp": True})
    # print("Minima found at x = ", minimum.x, ", f(x) = ", minimum.fun)

    # # Plot function and mark minimum
    # xs = np.linspace(0.5, 2.5)
    # ys = f(xs)
    # plt.plot(xs, ys)
    # # NOTE: ro = red circle
    # plt.plot(minimum.x, minimum.fun, "ro")
    # plt.title("f(x) = (x - 1.5)^2 + 0.5")
    # plt.show()

    # # Define original line
    # line_original = np.array([4, 2])
    # c0_original, c1_original = line_original
    # x_original = np.linspace(0, 10, 20)
    # y_original = c0_original * x_original + c1_original
    # # NOTE: b-- = blue dashed line
    # plt.plot(x_original, y_original, "b--", linewidth=2, label="Original line")

    # # Generate noisy data points
    # noise_sigma = 3.0
    # noise = np.random.normal(0, noise_sigma, size=x_original.shape)
    # data = np.asarray([x_original, y_original + noise]).T
    # xs, ys = data[:, 0], data[:, 1]
    # # NOTE: go = green circle
    # plt.plot(xs, ys, "go", label="Data points")

    # # Fit line to data points
    # line_fitted = fit_line(data, error_line)
    # c0_fitted, c1_fitted = line_fitted
    # x_fitted = np.linspace(0, 10, 20)
    # y_fitted = c0_fitted * x_fitted + c1_fitted
    # # NOTE: r-- = red dashed line
    # plt.plot(x_fitted, y_fitted, "r--", linewidth=2, label="Fitted line")

    # plt.title("Fitting a line to data points")
    # plt.legend(loc="upper left")
    # plt.show()

    # Define original polynomial
    poly_original = np.poly1d([1.5, 10, 5, 60, 50])
    print("Original polynomial")
    print(poly_original)
    x_original = np.linspace(-100, 100, 50)
    y_original = np.polyval(poly_original, x_original)
    plt.plot(x_original, y_original, "b--", linewidth=2, label="Original polynomial")

    # Generate noisy data points
    noise_sigma = 5_000_000.0
    noise = np.random.normal(0, noise_sigma, size=x_original.shape)
    data = np.asarray([x_original, y_original + noise]).T
    xs, ys = data[:, 0], data[:, 1]
    # NOTE: go = green circle
    plt.plot(xs, ys, "go", label="Data points")

    # Fit polynomial to data points
    poly_fitted = fit_poly(data, error_poly, degree=4)
    print("Fitted polynomial")
    print(poly_fitted)
    x_fitted = np.linspace(-100, 100, 50)
    y_fitted = np.polyval(poly_fitted, x_fitted)
    # NOTE: r-- = red dashed line
    plt.plot(x_fitted, y_fitted, "r--", linewidth=2, label="Fitted polynomial")

    plt.title("Fitting a polynomial to data points")
    plt.legend(loc="upper left")
    plt.show()
