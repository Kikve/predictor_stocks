
import streamlit as st
from ui import render_stock_search, render_transaction_form
from pandas import DataFrame

st.set_page_config(page_title="Transaction Register", layout="wide")

st.header("Register a transaction")
searched_stocks_data: DataFrame = render_stock_search()
render_transaction_form(searched_stocks_data)
