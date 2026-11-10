
import streamlit as st
import yfinance as yf
import pandas as pd
from database import get_connection


# main()
# │
# ├── render_stock_search()
# │   └── search_stock()
# │
# └── render_transaction_form()
#     │
#     ├── get_stock_information()
#     │
#     └── register_transaction()
#         │
#         ├── get_or_create_asset()
#         │
#         └── save_transaction()
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

    with st.form("regiyrr"):
        ticker_name = st.selectbox("Stock", options=values)
        ticker = yf.Ticker(ticker_name)
        transaction_date = st.date_input("Date", format="YYYY-MM-DD")
        quantity = st.number_input("Quantity", min_value=1)
        price = st.number_input("price", format="%.2f")

        submitted = st.form_submit_button("register")
        if submitted:
            st.success("Registered")
            filtered = result[result["symbol"] == ticker_name]
            col1, col2 = st.columns(2)
            col1.subheader(filtered["shortname"].iloc[0] +
                           " (" + filtered["symbol"].iloc[0] + ")")
            col2.metric("Total", price * quantity)

            # ----------------------------------------------
            # change to something more specific functions for work with db
            with get_connection() as conn:
                conn.execute("""
                        INSERT OR IGNORE INTO assets (ticker, company_name)
                        VALUES (?, ?)
                        """, (ticker_name, filtered["longname"].iloc[0])
                             )

                asset_id = conn.execute(
                    """SELECT id FROM assets WHERE ticker = ?""", (
                        ticker_name,)
                ).fetchone()[0]

                conn.execute("""
                    INSERT INTO transactions (
                    asset_id,
                    transaction_date,
                    quantity,
                    price
                    )
                    VALUES (?,?,?,?)
                    """,  (asset_id, transaction_date, quantity, price)
                )
