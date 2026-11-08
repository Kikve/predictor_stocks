
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Search", layout="wide")
st.title("Stock Search")




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




search = st.text_input("Buscar stock")

df = search_stock(search)


if search:
    result = search_stock(search)
    st.dataframe(result)

