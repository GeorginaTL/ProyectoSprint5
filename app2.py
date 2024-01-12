import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Análisis exploratorio de datos sobre autos')

hist_button = st.button('Construir histograma') # crear un botón
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    #fig.show() # dibujar histograma
scatter_button = st.button('Construir gráfico de dispersión') # crear un botón
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    #fig.show() # dibujar gráfico de dispersión 