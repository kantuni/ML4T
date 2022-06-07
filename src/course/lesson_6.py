import matplotlib.pyplot as plt

from lesson_4 import compute_daily_returns, get_stock_prices, plot_data

if __name__ == "__main__":
    print("Plotting SPY stock prices from 2009 to 2012...")
    df = get_stock_prices(["SPY"], "2009-01-01", "2012-12-31")
    plot_data(df)

    print("Plotting SPY daily returns from 2009 to 2012...")
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="SPY daily returns", ylabel="Daily returns")

    print("Plotting SPY daily returns as a histogram with 20 bins...")
    daily_returns.hist(bins=20)
    plt.show()
