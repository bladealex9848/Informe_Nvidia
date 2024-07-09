import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Resultados Financieros NVIDIA - T4 y Año Fiscal 2024", layout="wide")

# Título principal
st.title("Resultados Financieros de NVIDIA - T4 y Año Fiscal 2024")

# Datos
destacados = [
    "Ingresos trimestrales récord de $22.1 mil millones, un aumento del 22% respecto al T3 y del 265% respecto al año anterior",
    "Ingresos trimestrales récord del Centro de Datos de $18.4 mil millones, un aumento del 27% respecto al T3 y del 409% respecto al año anterior",
    "Ingresos anuales récord de $60.9 mil millones, un aumento del 126%",
    "Las ganancias GAAP por acción diluida fueron de $4.93, un aumento del 33% respecto al T3 y del 765% respecto al año anterior",
    "Las ganancias no-GAAP por acción diluida fueron de $5.16, un aumento del 28% respecto al T3 y del 486% respecto al año anterior"
]

datos_trimestrales = pd.DataFrame({
    'Métrica': ['Ingresos', 'Beneficio Bruto', 'Ingreso Operativo', 'Ingreso Neto'],
    'T4 AF2024': [22103, 16791, 13615, 12285],
    'T3 AF2024': [18120, 13400, 10417, 9243],
    'T4 AF2023': [6051, 3833, 1257, 1414]
})

datos_anuales = pd.DataFrame({
    'Métrica': ['Ingresos', 'Beneficio Bruto', 'Ingreso Operativo', 'Ingreso Neto'],
    'AF 2024': [60922, 44301, 32972, 29760],
    'AF 2023': [26974, 15356, 4224, 4368]
})

datos_segmentos = pd.DataFrame({
    'Segmento': ['Centro de Datos', 'Juegos', 'Visualización Profesional', 'Automotriz'],
    'Ingresos': [18400, 2900, 463, 281],
    'Crecimiento': [409, 56, 105, -4]
})

# Funciones para crear gráficos
def crear_grafico_barras(df, titulo):
    fig = go.Figure()
    for columna in df.columns[1:]:
        fig.add_trace(go.Bar(
            x=df['Métrica'],
            y=df[columna],
            name=columna
        ))
    fig.update_layout(
        title=titulo,
        xaxis_title="Métrica",
        yaxis_title="Millones de USD",
        barmode='group'
    )
    return fig

def crear_grafico_segmentos(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Segmento'],
        y=df['Ingresos'],
        name='Ingresos',
        yaxis='y'
    ))
    fig.add_trace(go.Bar(
        x=df['Segmento'],
        y=df['Crecimiento'],
        name='Crecimiento Interanual (%)',
        yaxis='y2'
    ))
    fig.update_layout(
        title="Rendimiento por Segmento - T4 AF2024",
        xaxis_title="Segmento",
        yaxis=dict(title="Ingresos (Millones de USD)"),
        yaxis2=dict(title="Crecimiento Interanual (%)", overlaying='y', side='right'),
        barmode='group'
    )
    return fig

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Destacados", "Resultados Trimestrales", "Resultados Anuales", "Rendimiento por Segmento"])

with tab1:
    st.header("Puntos Destacados")
    for punto in destacados:
        st.markdown(f"- {punto}")

with tab2:
    st.header("Resultados Financieros Trimestrales")
    st.plotly_chart(crear_grafico_barras(datos_trimestrales, "Resultados Financieros Trimestrales (en millones de USD)"), use_container_width=True)

with tab3:
    st.header("Resultados Financieros Anuales")
    st.plotly_chart(crear_grafico_barras(datos_anuales, "Resultados Financieros Anuales (en millones de USD)"), use_container_width=True)

with tab4:
    st.header("Rendimiento por Segmento")
    st.plotly_chart(crear_grafico_segmentos(datos_segmentos), use_container_width=True)

# Nota al pie
st.markdown("---")
st.markdown("Datos proporcionados por NVIDIA Corporation. Todos los valores están en millones de USD, excepto los porcentajes de crecimiento.")