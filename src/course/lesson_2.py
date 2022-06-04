from pathlib import Path
from typing import List

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
        # Use the date as index
        index_col="Date",
        # Convert the column to datetime
        parse_dates=True,
        # We're only interested in these columns
        usecols=["Date", "Adj Close"],
    )

    # Rename the "Adj Close" column to "SPY" to avoid clashes after joining.
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

        # Rename the "Adj Close" column to symbol to avoid clashes after joining.
        df_symbol = df_symbol.rename(columns={"Adj Close": symbol})

        # Left join the dataframes (because we want to keep all days when SPY traded).
        df = df.join(df_symbol)

    return df


if __name__ == "__main__":
    # Print stock (adjusted close) prices for IBM, GOOG, and GLD from 2010-01-22 to 2010-01-26
    print(get_stock_prices(["IBM", "GOOG", "GLD"], "2010-01-22", "2010-01-26"))
