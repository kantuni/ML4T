from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def last_five_rows(symbol: str) -> None:
    """Prints last 5 rows of the given symbol."""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    print(df.tail(5))


def get_mean_volume(symbol: str) -> float:
    """Returns mean volume of the given symbol."""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    return df["Volume"].mean()


def plot_high_prices(symbol: str) -> None:
    """Plots high prices of the given symbol."""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    df["High"].plot(title="High Prices")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()


if __name__ == "__main__":
    print("Last 5 rows of AAPL")
    last_five_rows("AAPL")

    for symbol in ["AAPL", "MSFT", "GOOG"]:
        print(f"Mean volume of {symbol}: {get_mean_volume(symbol)}")

    print("Plotting high prices of AAPL...")
    plot_high_prices("IBM")
