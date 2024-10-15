import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de venta carros')

st.write('Selecciona el tipo de gráfico a realizar')

build_hist=st.checkbox('Construir un histograma')
build_disp=st.checkbox('Construir gráfico de dispersión') 

#Al hacer click en el boton escribe un mensaje
if build_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig=px.histogram(car_data, x='odometer')
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

if build_disp:
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncio de venta de coches')
    
    fig2=px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)