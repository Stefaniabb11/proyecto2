import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go 

data = pd.read_csv('municipios.csv')

st.title("Recaudo Municipal ")

st.set_page_config(
    page_title="Recaudo municipal",
    page_icon="💰",
    layout="wide")


munis = data ['entidad'].unique().tolist()
mun=st.selectbox ("Seleccione un municipio y un año.",
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
    tabla = filtro.groupby(["anio", "clas_gen"])["total_recaudo"].sum().reset_index()
    tabla = tabla.sort_values(by=["anio", "total_recaudo"], ascending=[True, False])
    fig_lolli = go.Figure()
    for categoria in tabla["clas_gen"].unique():
     df_cat = tabla[tabla["clas_gen"] == categoria]
     fig_lolli.add_trace(go.Scatter(
        x = df_cat["anio"],
        y = df_cat["total_recaudo"],
        mode = 'markers',
        name = categoria,
        marker=dict(size=10)  # tamaño del punto en la punta
     ))
    fig_lolli.add_trace(go.Scatter(
        x = df_cat["anio"],
        y = [0]*len(df_cat["anio"]),  # base en cero
        mode = 'lines',
        name = categoria + "_line",
        line=dict(width=2),
        showlegend=False  # para que las líneas no sean legend separadas
     ))
     # Otra forma más precisa:
    for _, row in df_cat.iterrows():
        fig_lolli.add_shape(dict(
            type="line",
            x0=row["anio"], y0=0,
            x1=row["anio"], y1=row["total_recaudo"],
            line=dict(color="dimgray", width=2)
        ))
    fig_lolli.update_layout(
    title=f"Gráfico tipo Lollipop de ingresos en {"mun"}",
    xaxis_title="Año",
    yaxis_title="Total de recaudo",
    template="plotly_white",
    hovermode="x unified"
    )
    st.plotly_chart(fig_lolli, use_container_width=True)

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

tabla_pie = filtro.groupby("clas_gen")["total_recaudo"].sum().reset_index()

# Colores personalizados
colores = {
    "Ingresos propios": "#877d5e",  
    "Transferencias": "#bdce8a",     
    "Recursos de capital": "#eecf8e"
}

# Gráfico de torta
fig_pie = px.pie(
    tabla_pie,
    names="clas_gen",
    values="total_recaudo",
    color="clas_gen",
    color_discrete_map=colores,
    title="📊 Distribución del recaudo fiscal por categoría"
)
fig_pie.update_layout(
    width=800,
    height=600,
    title_font_size=20,
    legend=dict(
        font=dict(size=25)  # tamaño de la letra de la leyenda
    )
)
# Mostrar en Streamlit
st.plotly_chart(fig_pie, use_container_width=True)

