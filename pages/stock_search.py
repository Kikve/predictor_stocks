
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="titulo", layout="wide")
st.title("mi titulo")

st.title("📈 Dtos del S&P 500 en Pantalla")
st.write("Descargando y mostrando el comportamiento histórico del índice S&P 500 (^GSPC).")



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

if search:
    result = search_stock(search)
    st.dataframe(result)

if st.button("Cargar data"):
    with st.spinner("Conectando con Yahoo Finance..."):
        # 1. Descargar los datos del S&P 500
        df = yf.download(search, start="2023-01-01", end="2026-10-01")

        if df.empty:
            st.error("No se pudieron obtener los datos.")
        else:
            st.success("¡Datos descargados con éxito!")

            # 2. Mostrar gráfico de línea interactivo con el precio de cierre
            st.subheader("Gráfico histórico (Precio de Cierre)")
            st.line_chart(df['Close'])

            # 3. Mostrar la tabla con los últimos registros
            st.subheader("Últimos registros en formato de tabla:")
            st.dataframe(df.tail())



            
