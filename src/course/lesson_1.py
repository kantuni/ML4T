from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def last_five_rows(symbol: str) -> None:
    """Print last 5 rows of the given symbol"""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    print(df.tail(5))


def get_mean_volume(symbol: str) -> float:
    """Return mean volume of the given symbol"""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    return df["Volume"].mean()


def plot_high_prices(symbol: str) -> None:
    """Plot high prices of the given symbol"""
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    df["High"].plot(title="High Prices")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()


if __name__ == "__main__":
    # Print last 5 rows of AAPL
    # last_five_rows("AAPL")

    # Print mean volume of AAPL, MSFT, and GOOG
    # for symbol in ["AAPL", "MSFT", "GOOG"]:
    #     print(symbol, get_mean_volume(symbol))

    # Plot high prices of IBM
    plot_high_prices("IBM")
