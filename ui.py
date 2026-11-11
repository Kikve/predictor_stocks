import streamlit as st
from stock_data import stock_search
from pandas import DataFrame
import pandas as pd


def render_stock_search() -> DataFrame:
    search_string = st.text_input("Search company")

    if not search_string:
        return pd.DataFrame()

    data: DataFrame = stock_search(search_string)
    st.dataframe(data)

    return data
