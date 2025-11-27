import streamlit as st

from login import*

# CONFIGURACION DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio DSFB",
    page_icon="F.Duque_DSFB_logo_500px.jpg",
    layout="centered",
)

st.header("Productos de Datos :orange[Machine Learning]")

archivo = __file__.split("\\")[-1]
login.generarLogin(archivo)
if "usuario" in st.session_state:
    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.markdown("""
                    ¿Sabías que tu empresa tiene mucha información que no utiliza?

                    Los datos disponibles no se aprovechan para mejorar las ventas ni las operaciones.
                    Esto es común en la mayoría de las empresas locales.  


                    :orange[Las empresas necesitan servicios profesionales  que les apoyen en el procesamiento 
                    de la información que recopilan en sus operaciones diarias, cruzarla con otras 
                    fuentes, analizarla, encontrar oportunidades y construir productos de datos que permitan definir acciones 
                    basadas en datos, para  aumentar los ingresos o reducir los costos.]
                    
                    """)
    with col2:
        st.subheader(":blue[Modelos de Machine Learning ML]")
        st.markdown(""":gray[
                    Son un tipo de productos de datos que permiten construir modelos
                    personalizados ajustados a los procesos de la empresa y con la información 
                    generada, modelos utilizados en diferentes ámbitos.]

    Como ejemplos se pueden citar:  
    * Segmentación de clientes
    * Retención - fidelización clientes
    * Forecasting de ventas 
      (por tienda y producto)
    * Lead scoring para evaluar el 
      valor de un cliente potencial
    * Detección de fraude
    * Análisis de riesgo crediticio
    * etcetera        
                    """)
    # st.markdown("""
    #           El aprendizaje automático o aprendizaje automatizado o aprendizaje de
    #            máquinas (del inglés, machine learning) es el subcampo de las ciencias de la
    #            computación y una rama de la inteligencia artificial, cuyo objetivo es desarrollar
    #            técnicas que permitan que las computadoras aprendan (Wikipedia)
    #            """)

