import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis exploratorio de datos sobre autos")

st.write("\n",car_data.sample(10),"\n")

# casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma: frecuencia para los valores de la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    st.write('La mayoría de los autos a la venta han recorrido 1000 Millas, segun el odómetro')

    # casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión: odómetro vs precio del auto')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    st.write('Los autos que se venden a precios mas altos son los mas nuevos (con odómetro 0). A partir de 2000 Millas, su precio empieza a bajar')

#hist_button = st.button('Construir histograma') # crear un botón
#if hist_button:
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
#    fig = px.histogram(car_data, x="odometer")
#    st.plotly_chart(fig, use_container_width=True)
#    st.write('La mayoría de los autos a la venta han recorrido 1000 Millas, segun el odómetro')


#scatter_button = st.button('Construir gráfico de dispersión') # crear un botón
#if scatter_button:
#    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
#    fig = px.scatter(car_data, x="odometer", y="price")
#    st.plotly_chart(fig, use_container_width=True)
#    st.write('Los autos que se venden a precios mas altos son los mas nuevos (con odómetro 0). A partir de 2000 Millas, su precio empieza a bajar')
  