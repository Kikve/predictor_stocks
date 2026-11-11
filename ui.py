import streamlit as st
from stock_data import stock_search
from pandas import DataFrame
import pandas as pd
from datetime import date
from database import create_transaction


def render_stock_search() -> DataFrame:
    search_string = st.text_input("Search company")

    if not search_string:
        return pd.DataFrame()

    data: DataFrame = stock_search(search_string)
    st.dataframe(data)

    return data


def render_transaction_form(data: DataFrame) -> None:

    # values = (result["symbol"]).tolist()
    stock_options = (data["longname"] + " (" + data["symbol"] + ")").tolist()

    with st.form("Register a transaction"):
        stock_selected: str = st.selectbox("Stock", options=stock_options)
        index_selected: int = stock_options.index(stock_selected)
        transaction_date: date = st.date_input("Date", format="YYYY-MM-DD")
        quantity: int = st.number_input("Quantity", min_value=1)
        price: float = st.number_input("price", format="%.2f")

        submitted = st.form_submit_button("Submit")
    if submitted:
        line_selected = data.iloc[index_selected]

        transaction = {
            line_selected["longname"],
            line_selected["symbol"],
            transaction_date,
            quantity,
            price
        }

        create_transaction(transaction)
        display_transaction_summary(transaction)

        st.success("Registered")


def display_transaction_summary(
    stock_name: str,
    symbol: str,
    transaction_date: date,
    quantity: int,
    price: float


) -> None:
    col1, col2 = st.columns(2)
    col1.subheader(f"{stock_name} ({symbol})")
    st.text(transaction_date)
    col2.metric("Total", price * quantity)
