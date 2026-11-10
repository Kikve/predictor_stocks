
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Search", layout="wide")


def search_stock(search, max_r=10):
    """
    search stocks in yahoo finance
    """
    try:
        results = yf.Search(search, max_results=max_r)
        return pd.DataFrame(results.quotes)

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()


st.title("Register a stock")
search_string = st.text_input("Search company")

df = search_stock(search_string)

if search_string:
    result = search_stock(search_string)
    st.dataframe(result)
    values = (result["symbol"]).tolist()

    ticker_name = st.selectbox("Stock", options=values)
    ticker = yf.Ticker(ticker_name)
    transaction_date = st.date_input("Date", format="YYYY-MM-DD")
    quantity = st.number_input("Quantity", min_value=1)
    st.number_input("price", format="%.2f")
