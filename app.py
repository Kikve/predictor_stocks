import streamlit as st

pages = [
    st.Page("pages/stock_search.py", title="Stock Search"),
    st.Page("pages/historical_data.py", title="Historical Data"),
    st.Page("pages/predictions.py", title="Predictions"),
]

pg = st.navigation(pages, position="sidebar")

pg.run()
