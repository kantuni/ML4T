import math
from typing import List

import pandas as pd

from lesson_2 import get_stock_prices, normalize_prices
from lesson_4 import compute_daily_returns


def compute_portfolio_value(
    budget: float,
    symbols: List[str],
    allocations: List[float],
    start_date: str,
    end_date: str,
) -> pd.Series:
    """Computes the value of a portfolio."""
    prices = get_stock_prices(symbols, start_date, end_date)
    normalized = normalize_prices(prices)
    allocated = normalized * allocations
    position_values = allocated * budget
    portfolio_value = position_values.sum(axis=1)
    return portfolio_value


def compute_portfolio_daily_returns(portfolio_value: pd.DataFrame) -> pd.Series:
    """Computes the daily returns of a portfolio given the portfolio value.

    NOTE: Drop the first row (as we ignored it in the portfolio value computation)
    for correct measurements.
    """
    daily_returns = compute_daily_returns(portfolio_value)
    return daily_returns[1:]


def compute_portfolio_cumulative_return(portfolio_value: pd.DataFrame) -> float:
    """Computes the cumulative return of a portfolio given the portfolio value."""
    return portfolio_value.iloc[-1] / portfolio_value.iloc[0] - 1


def compute_portfolio_average_daily_return(portfolio_daily_returns: pd.Series) -> float:
    """Computes the average daily return of a portfolio given the portfolio daily returns."""
    return portfolio_daily_returns.mean()


def compute_portfolio_risk(portfolio_daily_returns: pd.Series) -> float:
    """Computes the risk of a portfolio given the portfolio daily returns."""
    return portfolio_daily_returns.std()


def compute_sharpe_ratio(
    portfolio_daily_returns: pd.Series, risk_free_rate: float = 0.01
) -> float:
    """Computes the Sharpe ratio of a portfolio given the portfolio daily returns.

    The Sharpe ratio is the ratio of the portfolio's average daily return to its
    volatility.

    NOTE: Risk free rate of return is usually about 1% per year.
    That means, that if we were to take our money out of the market and
    put it into a savings account, we will gain about 1% per year.
    """
    # Sharpe ratio is defined for annualized returns.
    # To calculate sharpe ratio for daily returns, we need to multiply by k,
    # where k = sqrt(# of samples per year) = sqrt(frequency of data).
    # For daily data, k = sqrt(252)
    # For weekly data, k = sqrt(52)
    # For monthly data, k = sqrt(12)
    k = math.sqrt(252)
    average_daily_return = compute_portfolio_average_daily_return(
        portfolio_daily_returns
    )
    risk = compute_portfolio_risk(portfolio_daily_returns)
    return k * (average_daily_return - risk_free_rate) / risk


if __name__ == "__main__":
    budget = 1_000_000
    symbols = ["SPY", "XOM", "GOOG", "GLD"]
    allocations = [0.4, 0.4, 0.1, 0.1]
    start_date = "2009-01-01"
    end_date = "2011-12-31"

    # Calculate daily portfolio value
    portfolio_value = compute_portfolio_value(
        budget, symbols, allocations, start_date, end_date
    )
    print("Portfolio value")
    print(portfolio_value)

    # Calculate daily returns of the portfolio
    portfolio_daily_returns = compute_portfolio_daily_returns(portfolio_value)
    print("Portfolio daily returns")
    print(portfolio_daily_returns)

    cumulative_return = compute_portfolio_cumulative_return(portfolio_value)
    print("Cumulative return:", cumulative_return)

    average_daily_return = compute_portfolio_average_daily_return(
        portfolio_daily_returns
    )
    print("Average daily return:", average_daily_return)

    # Standard deviation of daily return is risk.
    risk = compute_portfolio_risk(portfolio_daily_returns)
    print("Risk:", risk)

    # Calculate sharpe ratio
    sharpe_ratio = compute_sharpe_ratio(portfolio_daily_returns)
    print("Sharpe ratio:", sharpe_ratio)
