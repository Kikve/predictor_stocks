import streamlit as st
from ui import render_transactions_history
from database import get_transactions

st.title("mi titulo")

render_transactions_history(get_transactions())
