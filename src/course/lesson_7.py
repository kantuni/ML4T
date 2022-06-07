from lesson_2 import get_stock_prices, normalize_prices
from lesson_4 import compute_daily_returns

if __name__ == "__main__":
    start_value = 1_000_000
    start_date = "2009-01-01"
    end_date = "2011-12-31"
    symbols = ["SPY", "XOM", "GOOG", "GLD"]
    allocations = [0.4, 0.4, 0.1, 0.1]

    # Calculate daily portfolio value
    df = get_stock_prices(symbols, start_date, end_date)
    normalized = normalize_prices(df)
    allocated = normalized * allocations
    position_values = allocated * start_value
    portfolio_value = position_values.sum(axis=1)
    print("Daily portfolio value")
    print(portfolio_value)

    # Calculate daily returns of the portfolio
    daily_returns = compute_daily_returns(portfolio_value)
    # Drop the first row (as we ignored it in the computation) for correct measurements
    daily_returns = daily_returns[1:]

    cumulative_return = portfolio_value[-1] / portfolio_value[0] - 1
    print("Cumulative return:", cumulative_return)

    average_daily_return = daily_returns.mean()
    print("Average daily return:", average_daily_return)

    std_daily_return = daily_returns.std()
    print("Standard deviation of the daily return:", std_daily_return)
