import pandas as pd

from lesson_2 import get_stock_prices, plot_data


def fill_missing_values(df: pd.DataFrame) -> None:
    """Fills missing values inplace.

    NOTE: We first fill forward to prevent peaking into the future.
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
