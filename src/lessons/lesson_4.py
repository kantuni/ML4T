from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd

from lesson_2 import get_stock_prices, plot_data


def get_rolling_mean(values: pd.Series, window: int) -> pd.Series:
    """Returns a rolling mean of the values."""
    return values.rolling(window=window).mean()


def get_rolling_std(values: pd.Series, window: int) -> pd.Series:
    """Returns a rolling standard deviation of the values."""
    return values.rolling(window=window).std()


def get_bollinger_bands(rm: pd.Series, rstd: pd.Series) -> Tuple[pd.Series, pd.Series]:
    """Returns upper and lower Bollinger Bands."""
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


def compute_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Returns the daily return values.

    Let's say the price today is $110, and yesterday it was $100.
    Then the daily return is (110 - 100) / 100 = 110 / 100 - 1 = 0.1 = 10%
    Thus, for day d the formula is: prices[d] / prices[d - 1] - 1

    NOTE: As the first day values will not have previous values,
    they will become NaN. We then replace them with 0.
    """
    return (df / df.shift(1) - 1).fillna(0)


def compute_cumulative_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Returns the cumulative return values.

    Let's say the price today is $110, and on the first day it was $100.
    Then the cumulative return is (110 - 100) / 100 = 110 / 100 - 1 = 0.1 = 10%
    Thus, for day d the formula is: prices[d] / prices[0] - 1
    """
    return df / df.iloc[0] - 1


if __name__ == "__main__":
    print("Plotting stock prices for SPY, XOM, GOOG, and GLD from 2010 to 2012...")
    df = get_stock_prices(["SPY", "XOM", "GOOG", "GLD"], "2010-01-01", "2012-12-31")
    plot_data(df)

    print("Mean")
    print(df.mean())

    print("Median")
    print(df.median())

    print("Standard deviation")
    print(df.std())

    print("Plotting stock prices and rolling mean for SPY in 2012...")
    df = get_stock_prices(["SPY"], "2012-01-01", "2012-12-31")
    axis = df["SPY"].plot(label="SPY")
    rolling_mean = get_rolling_mean(df["SPY"], 20)
    rolling_mean.plot(label="Rolling Mean", ax=axis)
    axis.set_title("Stock Prices and Rolling Mean for SPY in 2012")
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.legend(loc="upper left")
    plt.show()

    print("Plotting rolling mean and Bollinger bands for SPY in 2012...")
    df = get_stock_prices(["SPY"], "2012-01-01", "2012-12-31")
    rm = get_rolling_mean(df["SPY"], 20)
    rstd = get_rolling_std(df["SPY"], 20)
    upper_band, lower_band = get_bollinger_bands(rm, rstd)
    axis = df["SPY"].plot(label="SPY")
    rm.plot(label="Rolling Mean", ax=axis)
    upper_band.plot(label="Upper Band", ax=axis, color="black")
    lower_band.plot(label="Lower Band", ax=axis, color="black")
    axis.set_title("Rolling mean and Bollinger bands for SPY in 2012")
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.legend(loc="upper left")
    plt.show()

    print("Plotting SPY and XOM daily returns from 2012-07-01 to 2012-07-31...")
    df = get_stock_prices(["SPY", "XOM"], "2012-07-01", "2012-07-31")
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="SPY and XOM daily returns", ylabel="Daily returns")

    year = 2010
    print(f"Plotting SPY cumulative returns in {year}...")
    df = get_stock_prices(["SPY"], f"{year}-01-01", f"{year}-12-31")
    cumulative_returns = compute_cumulative_returns(df)
    plot_data(
        cumulative_returns, title="SPY cumulative returns", ylabel="Cumulative returns"
    )
    yearly_cumulative_return = df["SPY"].iloc[-1] / df["SPY"].iloc[0] - 1
    print(
        f"Yearly cumulative return in {year}:",
        "{:.2f}%".format(yearly_cumulative_return * 100),
    )
