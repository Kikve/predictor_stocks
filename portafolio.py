from pandas import DataFrame
from stock_data import current_price


def sumarize_assets(transactions: DataFrame) -> DataFrame:
    summary = transactions.groupby(["company_name", "ticker"])[
        ["quantity", "price"]].sum().reset_index()

    tickers: list = summary["ticker"].tolist()
    prices: list = list(map(current_price, tickers))

    summary["current_price"] = prices
    return summary
