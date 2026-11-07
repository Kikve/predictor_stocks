import streamlit as st
import yfinance as yf

st.set_page_config(page_title="titulo", layout="wide")
st.title("mi titulo")

st.title("📈 Dtos del S&P 500 en Pantalla")
st.write("Descargando y mostrando el comportamiento histórico del índice S&P 500 (^GSPC).")

# Botón para cargar los datos
if st.button("Cargar datos del S&P 500"):
    with st.spinner("Conectando con Yahoo Finance..."):
        # 1. Descargar los datos del S&P 500
        df = yf.download("^GSPC", start="2023-01-01", end="2026-01-01")

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
