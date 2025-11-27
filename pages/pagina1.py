import streamlit as st

import login

# CONFIGURACION DE LA PÁGINA
st.set_page_config(
    page_title="Forecasting", page_icon="F.Duque_DSFB_logo_500px.jpg", layout="wide"
)

archivo = __file__.split("\\")[-1]
login.generarLogin(archivo)
if "usuario" in st.session_state:
    st.header("Pagina:blue[2]")
