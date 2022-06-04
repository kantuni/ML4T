from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import pandas as pd


def symbol_to_path(symbol: str) -> Path:
    """Returns CSV file path given ticker symbol."""
    return Path(f"data/{symbol}.csv")


def get_stock_prices(
    symbols: List[str],
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """Returns a dataframe with stock (adjusted close) prices for the given symbols."""
    # Define date range.
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe (with dates as indices).
    df = pd.DataFrame(index=dates)

    # Read SPY data.
    df_spy = pd.read_csv(
        symbol_to_path("SPY"),
        # use the date as index
        index_col="Date",
        # convert the column to datetime
        parse_dates=True,
        # we're only interested in these columns
        usecols=["Date", "Adj Close"],
    )

    # Rename the "Adj Close" column to "SPY" to avoid clashes during joins.
    df_spy = df_spy.rename(columns={"Adj Close": "SPY"})

    # Inner join the dataframes.
    # This operation will remove weekend rows, and
    # will show only trading days form start to end date.
    df = df.join(df_spy, how="inner")

    for symbol in symbols:
        # Read symbol data.
        df_symbol = pd.read_csv(
            symbol_to_path(symbol),
            # use the date as index
            index_col="Date",
            # convert the column to datetime
            parse_dates=True,
            # we're only interested in these columns
            usecols=["Date", "Adj Close"],
        )

        # Rename the "Adj Close" column to symbol to avoid clashes during joins.
        df_symbol = df_symbol.rename(columns={"Adj Close": symbol})

        # Left join the dataframes (because we want to keep all days when SPY traded).
        df = df.join(df_symbol)

    return df


def plot_data(df: pd.DataFrame, title="Stock Prices") -> None:
    """Plots the dataframe."""
    axis = df.plot(title=title)
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    # Show the plot.
    plt.show()


def plot_selected(
    df: pd.DataFrame, symbols: List[str], start_date: str, end_date: str
) -> None:
    """Plots the desired symbols in the given period."""
    plot_data(df.loc[start_date:end_date, symbols])


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normalizes stock prices using the first row of the dataframe."""
    return df / df.iloc[0]


if __name__ == "__main__":
    # Print stock (adjusted close) prices for IBM, GOOG, and GLD from 2010-01-22 to 2010-01-26.
    # df = get_stock_prices(["IBM", "GOOG", "GLD"], "2010-01-22", "2010-01-26")
    # print(df)

    # Get stock (adjusted close) prices for IBM, GOOG, and GLD in 2010.
    df = get_stock_prices(["IBM", "GOOG", "GLD"], "2010-01-01", "2010-12-31")

    # Print SPY and IBM from 2010-03-10 to 2010-03-15 (using slicing).
    # print(df.loc["2010-03-10":"2010-03-15", ["SPY", "IBM"]])

    # Plot stock (adjusted close) prices for IBM, GOOG, and GLD in 2010.
    # plot_data(df)

    # Plot SPY and IBM from 2010-03-10 to 2010-03-15.
    # plot_selected(df, ["SPY", "IBM"], "2010-03-10", "2010-03-15")

    # Plot normalized data.
    plot_data(normalize_data(df))
