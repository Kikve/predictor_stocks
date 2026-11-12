import streamlit as st
from ui import render_transactions_history
from database import get_transactions
from portafolio import sumarize_assets

st.title("mi titulo")

render_transactions_history(get_transactions())
st.dataframe(sumarize_assets(get_transactions()))
