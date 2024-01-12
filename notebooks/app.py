import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Análisis exploratorio de datos sobre autos')