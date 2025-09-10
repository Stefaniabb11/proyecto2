import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

data = pd.read_csv('municipios.csv')

st.title("Recaudo Municipal ")

st.set_page_config(
    page_title="Recaudo Municipal | Agua Azul, Barrancas y Barrancabermeja",
    page_icon="💰",
    layout="wide"
)

municipios= data['entidad'].unique(). tolist() #guardamos en una lista las entidades unicas 
mun = st.selectbox("seleccione un municipio:", municipios)

filtro = data[data['entidad'] == mun] 

gen = (filtro.groupby('clas_gen')['total_recaudo'].sum()) 
total_gen = gen.sum()

# Filtro de año
anios = sorted(data['anio'].unique().tolist())
anio = st.radio(" Selecciona el año", anios, horizontal=True)
#agregar filtro

#st.dataframe(filtro) #dataframe original pero filtrado por municipio

gen = (filtro.groupby('clas_gen')['total_recaudo'].sum()) 
total_gen = gen.sum()

gen = (gen / total_gen).round(2) #proporciones para hacer el grafico de torta

det = (filtro.groupby('clasificacion_ofpuj')['total_recaudo'].sum())
total_det = det.sum()

det = (det/total_det).round(3) #proporciones para hacer el grafico de torta
#el codigo groupby separa las clasificaciones 

#st.dataframe(gen) #clasificacion general 
#st.dataframe(det) #clasificacion detallada 

fig_line = px.line(
    filtro,
    x="anio",
    y="total_recaudo",
    color="entidad",
    markers=True,
    title="Evolución del recaudo por entidad"
)

colores = {
    "Ingresos propios": "#1f77b4",   # azul
    "Transferencias": "#ff7f0e",     # naranja
    "Regalías": "#2ca02c"            # verde
}

# Gráfico de barras
fig_bar = px.bar(
    filtro,
    x="entidad",
    y="total_recaudo",
    color="clas_gen",
    barmode="group",
    facet_col="anio",   # separa por año
    color_discrete_map=colores,
    title="📊 Recaudo Fiscal por Entidad y Año"
)

# Mostrar en Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

#gropuby agrupaaaaa
fin = (filtro.groupby(['clas_gen', 'clasificacion_ofpuj'])['total_recaudo'].sum().reset_index())
#st.dataframe(fin)

fig = px.treemap(fin, path = [px.Constant("Total"),'clas_gen' , 'clasificacion_ofpuj'], values= 'total_recaudo')
st.plotly_chart(fig)