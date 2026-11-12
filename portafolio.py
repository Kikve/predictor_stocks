from pandas import DataFrame


def sumarize_assets(transactions: DataFrame) -> DataFrame:
    return transactions.groupby("company_name")[
        ["quantity", "price"]].sum().reset_index()
