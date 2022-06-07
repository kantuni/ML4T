import matplotlib.pyplot as plt
import numpy as np

from lesson_4 import compute_daily_returns, get_stock_prices, plot_data

if __name__ == "__main__":
    print("Plotting SPY stock prices from 2009 to 2012...")
    df = get_stock_prices(["SPY"], "2009-01-01", "2012-12-31")
    plot_data(df)

    print("Plotting SPY daily returns from 2009 to 2012...")
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="SPY daily returns", ylabel="Daily returns")

    print("Plotting SPY daily returns as a histogram with 20 bins, mean and std...")
    plt.hist(daily_returns, bins=20)

    mean = daily_returns["SPY"].mean()
    print("Mean:", mean)

    std = daily_returns["SPY"].std()
    print("Standard deviation:", std)

    # Kurtosis is a measure of whether the data are heavy-tailed or
    # light-tailed relative to a normal distribution.
    # That is, data sets with high kurtosis tend to have heavy tails, or outliers.
    # Data sets with low kurtosis tend to have light tails, or lack of outliers.
    kurtosis = daily_returns["SPY"].kurtosis()
    print("Kurtosis:", kurtosis)

    plt.axvline(mean, color="white", linestyle="dashed", linewidth=2)
    plt.axvline(std, color="red", linestyle="dashed", linewidth=2)
    plt.axvline(-std, color="red", linestyle="dashed", linewidth=2)
    plt.show()

    print("Plotting SPY and XOM daily returns as a histogram with 20 bins...")
    df = get_stock_prices(["SPY", "XOM"], "2009-01-01", "2012-12-31")
    daily_returns = compute_daily_returns(df)

    plt.hist(daily_returns["SPY"], bins=20, label="SPY")
    plt.hist(daily_returns["XOM"], bins=20, label="XOM")
    plt.legend(loc="upper left")
    plt.title("SPY vs XOM daily returns")
    plt.show()

    df = get_stock_prices(["SPY", "XOM", "GLD"], "2009-01-01", "2012-12-31")
    daily_returns = compute_daily_returns(df)

    plt.scatter(daily_returns["SPY"], daily_returns["XOM"])
    beta_xom, alpha_xom = np.polyfit(daily_returns["SPY"], daily_returns["XOM"], 1)
    print("Beta XOM:", beta_xom)
    print("Alpha XOM:", alpha_xom)
    plt.plot(
        daily_returns["SPY"],
        beta_xom * daily_returns["SPY"] + alpha_xom,
        color="red",
        linewidth=2,
    )
    plt.title("SPY vs XOM daily returns")
    plt.show()

    plt.scatter(daily_returns["SPY"], daily_returns["GLD"])
    beta_gld, alpha_gld = np.polyfit(daily_returns["SPY"], daily_returns["GLD"], 1)
    print("Beta GLD:", beta_gld)
    print("Alpha GLD:", alpha_gld)
    plt.plot(
        daily_returns["SPY"],
        beta_gld * daily_returns["SPY"] + alpha_gld,
        color="red",
        linewidth=2,
    )
    plt.title("SPY vs GLD daily returns")
    plt.show()

    print("Correlation coefficient")
    print(daily_returns.corr(method="pearson"))
