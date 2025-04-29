import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análisis de los vehículos", layout="wide")

st.header("Análisis de datos de vehículos en venta")

car_data = pd.read_csv('vehicles_us.csv')

st.subheader("Distribución de kilometraje")
hist_button = st.button('Mostrar histograma de kilometraje')

if hist_button:
    st.write("""
    ### Histograma del Odómetro
    Este gráfico muestra la distribución de el kilometraje de los vehículos
    """)
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        labels={'odometer': 'Kilometraje'},
        color_discrete_sequence=['#636EFA']
    )
    fig_hist.update_layout(
        title_text='Distribución de Kilometraje',
        xaxis_title="Kilometraje",
        yaxis_title="Cantidad de Vehículos"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.subheader("Relación entre precio y kilometraje")
scatter_button = st.button('mostrar gráfico de dispersión')

if scatter_button:
    st.write("""
    ### Relación Precio vs. Kilometraje
    Este gráfico muestra cómo varían los precios en función del kilometraje de los vehículos.
    """)
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="type",
        hover_name="model",
        labels={
            'odometer': 'Kilometraje',
            'price': 'Precio (USD)',
            'type': 'Tipo de Vehículo'
        }
    )
    fig_scatter.update_layout(
        title_text='Precio vs. Kilometraje por Tipo de Vehículo',
        xaxis_title="Kilometraje",
        yaxis_title="Precio (USD)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
