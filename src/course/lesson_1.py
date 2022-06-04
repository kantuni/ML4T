from pathlib import Path

import pandas as pd


def last_five_rows(symbol: str) -> None:
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    print(df.tail(5))


def get_mean_volume(symbol: str) -> float:
    file_path = Path("data/{}.csv".format(symbol))
    df = pd.read_csv(file_path)
    return df["Volume"].mean()


if __name__ == "__main__":
    # Print last 5 rows of the given symbol data
    # last_five_rows("AAPL")

    # Print mean volume of the given symbol data
    for symbol in ["AAPL", "MSFT", "GOOG"]:
        print(symbol, get_mean_volume(symbol))
