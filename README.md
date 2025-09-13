🧾 Nota Metodológica

Elección de municipios

- La selección de Aguazul, Barrancas y Barrancabermeja se realizó considerando:
- Diferencias en la composición de su recaudo fiscal (dependencia de transferencias, ingresos propios o recursos de capital).
- Ubicación geográfica diversa, con el fin de representar distintas regiones del país y permitir un análisis más comparativo.

Variables y transformaciones

La base de datos utilizada contiene variables como código y nombre de departamento, año e información fiscal. Durante el proceso de preparación de los datos fue necesario realizar algunas transformaciones: se ajustó el tipo de variable de año a valores enteros y del total de recaudo a numéricos, se renombraron ciertas columnas para facilitar su manipulación y se filtraron únicamente los años 2023 y 2024, de acuerdo con el alcance del ejercicio. Asimismo, se seleccionaron los municipios mencionados como unidades de análisis y se agruparon sus valores de recaudo según la clasificación de ingresos.

Limitaciones de los datos

En primer lugar, el periodo de análisis es corto, lo cual restringe la posibilidad de identificar tendencias de largo plazo en el comportamiento fiscal de los municipios. En segundo lugar, la disponibilidad de datos desagregados es limitada, esto conlleva a omitir variables relevantes, lo cual limita el buen análisis y entendimiento del sistema fiscal de los municipios (gasto público, deuda).

Descripción de la aplicación

La aplicación desarrollada ofrece un flujo sencillo para el usuario. En la primera parte, se incluye un filtro para seleccionar el municipio de interés. Posteriormente, mediante botones, es posible elegir el año de análisis entre 2023 y 2024. Una vez definidos estos criterios, se generan diferentes visualizaciones con gráficos elaborados en Plotly. Entre ellos se encuentran un gráfico de barras agrupadas que permite observar el comportamiento de las tres fuentes de ingresos principales (ingresos propios, transferencias y recursos de capital) por entidad; un gráfico tipo lollipop que facilita identificar la magnitud y evolución de los ingresos en cada año; un treemap que muestra la composición interna de las fuentes de recaudo; y un gráfico de pastel que resume la distribución del recaudo fiscal por categoría.

🖥️ Link de la App -> https://proyec-2.streamlit.app/
