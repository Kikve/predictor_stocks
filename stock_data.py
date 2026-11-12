import yfinance as yf
import pandas as pd
from pandas import DataFrame


def stock_search(search_str: str, max_results=10) -> DataFrame:
    """
    search stocks in yahoo finance
    """
    try:
        results = yf.Search(
            search_str, max_results=max_results, enable_fuzzy_query=True)
        return pd.DataFrame(results.quotes)

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()


def current_price(symbol: str) -> float:
    """
    returns the current prince of the stock
    """
    return yf.Ticker(symbol).fast_info["lastPrice"]
