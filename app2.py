import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

data = pd.read_csv('municipios.csv')

st.title("Recaudo Municipal ")

st.set_page_config(
    page_title="Recaudo municipal",
    page_icon="💰",
    layout="wide")


munis = data ['entidad'].unique().tolist()
mun=st.selectbox ("Seleccione un municipio:",
             munis)
filtro = data[data['entidad'] == mun]
             
#st.dataframe(filtro)

gen=( filtro.groupby ('clas_gen')['total_recaudo']
    .sum())
total_gen = gen.sum()
gen = (gen/ total_gen).round(2)

det= (filtro
      .groupby ('clasificacion_ofpuj') ['total_recaudo']
      .sum())
total_det = det.sum()
det= (det/ total_det).round(3)
#st.dataframe(gen) #clasificacion general

# st.dataframe(det) # clasificacion detallada
# st.pyplot(fig)

#st.pyplot(fig)

anio = None

if st.button("📆 2023"):
    anio = 2023
if st.button("📆 2024"):
    anio=2024


col1, col2 = st.columns(2)

with col1:
    if anio:
        # Filtrar datos por año
        filtro_anio = filtro[filtro["anio"] == anio]
        colores = {
            "Ingresos propios": "#877d5e",  
            "Transferencias": "#bdce8a",     
            "Recursos de capital": "#eecf8e"
        }

        # Gráfico de barras (solo año seleccionado)
        fig_bar = px.bar(
            filtro_anio,
            x="entidad",
            y="total_recaudo",
            color="clas_gen",
            barmode="group",
            color_discrete_map=colores,
            title=f"📊 Recaudo Fiscal por Entidad - {anio}"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    tabla_heat = filtro.groupby(["anio", "clas_gen"])["total_recaudo"].sum().reset_index()
    fig_heat = px.density_heatmap(
        tabla_heat,
        x="anio",
        y="clas_gen",
        z="total_recaudo",
        color_continuous_scale=["#877d5e", "#bdce8a", "#eecf8e"],
        title=f"Mapa de calor de ingresos en {mun}"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

#treemap
fin= (filtro
     .groupby(['clas_gen','clasificacion_ofpuj'])['total_recaudo']
     .sum()
     .reset_index())
# st.dataframe(fin)

fig= px.treemap(fin ,path =[px.Constant("Total"),
                            'clas_gen',
                            'clasificacion_ofpuj'],
                            values= 'total_recaudo',color_discrete_sequence=["#877d5e", "#bdce8a", "#eecf8e"])
st.plotly_chart(fig)



# Gráfico de línea (evolución completa)
colores_verdes = {
    "Aguazul": "#877d5e",
    "Barrancas": "#bdce8a",
    "Barrancabermeja": "#eecf8e"
}

fig_line = px.line(
    filtro,
    x="anio",
    y="total_recaudo",
    color="entidad",
    markers=True,
    color_discrete_map=colores_verdes,
    title="Evolución del recaudo por entidad"
)
st.plotly_chart(fig_line, use_container_width=True)