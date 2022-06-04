"""Print last 5 rows of the given symbol data"""

from pathlib import Path

import pandas as pd


def last_five_rows(symbol: str) -> None:
    file_path = Path("data/{}.csv".format(symbol))
    print("file_path", file_path)
    df = pd.read_csv(file_path)
    print(df.tail(5))


if __name__ == "__main__":
    last_five_rows("AAPL")
