from pathlib import Path
from typing import List, Tuple

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

    # Read SPY data. It would act as a reference stock.
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
        # Skip SPY as we already have it.
        if symbol == "SPY":
            continue

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


def plot_data(
    df: pd.DataFrame,
    title: str = "Stock Prices",
    xlabel: str = "Date",
    ylabel: str = "Price",
) -> None:
    """Plots the dataframe."""
    axis = df.plot(title=title)
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    # Show the plot.
    plt.show()


def fill_missing_values(df: pd.DataFrame) -> None:
    """Fills missing values inplace.
    We first fill forward to prevent peaking into the future.
    Then we fill backward to fill the starting values.
    """
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)


if __name__ == "__main__":
    print("Plotting SPY and JAVA stock prices...")
    df = get_stock_prices(["JAVA"], "2000-01-01", "2010-12-31")
    plot_data(df)

    print("Plotting SPY and JAVA stock prices with missing values filled...")
    fill_missing_values(df)
    plot_data(df)
