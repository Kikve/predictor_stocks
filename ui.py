import streamlit as st
from stock_data import stock_search
from pandas import DataFrame
import pandas as pd
from datetime import date
from database import create_transaction


def render_stock_search() -> DataFrame:
    """
        render a component which allows to search an stock
        returns Dataframe with searched data
    """
    search_string = st.text_input("Search company")

    if not search_string:
        return pd.DataFrame()

    data: DataFrame = stock_search(search_string)
    st.dataframe(data)

    return data


def render_transaction_form(
    data: DataFrame,
    name="longname",
    identifier="symbol"
) -> None:
    """
    render an form which allows to register an stock transaction

    [data] -> Dataframe with stocks available to choose
    name column name which is identified name of the stock
    identifier column name of symbol of the stock
    """
    if data.empty:
        st.info("Search for a company")
        return None

    stock_options = [
        f"{n} ({i})"
        for n, i in zip(data[name], data[identifier])
    ]

    with st.form("Register a transaction"):
        stock_selected: str = st.selectbox("Stock", options=stock_options)
        index_selected: int = stock_options.index(stock_selected)
        transaction_date: date = st.date_input("Date", format="YYYY-MM-DD")
        quantity: int = st.number_input("Quantity", min_value=1)
        price: float = st.number_input("price", format="%.2f")

        submitted = st.form_submit_button("Submit")
    if submitted:
        line_selected = data.iloc[index_selected]

        transaction = [
            line_selected[name],
            line_selected[identifier],
            transaction_date,
            quantity,
            price
        ]

        create_transaction(*transaction)
        display_transaction_summary(*transaction)

        st.success("Registered")


def display_transaction_summary(
    stock_name: str,
    symbol: str,
    transaction_date: date,
    quantity: int,
    price: float


) -> None:

    with st.container(border=True):

        st.subheader("Transaction Summary")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.caption("Stock")
            st.write(f"{stock_name} ({symbol})")

        with col2:
            st.caption("Total amount")
            st.subheader(f"${price * quantity:,.2f}")

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.caption("Transaction date")
            st.write(transaction_date.strftime("%b %d, %Y"))

        with col2:
            st.caption("Quantity")
            st.write(f"{quantity:,}")

        with col3:
            st.caption("Price per share")
            st.write(f"${price:,.2f}")
