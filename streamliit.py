import streamlit as st
from streamlit_option_menu import option_menu
import Gastos as gd
import Estadia as es
import Resumen as re
import Contabilidad as co

st.write('''
## `Gestión Kurt Dic 22`
''')
st.markdown("<h4 style='text-align: justify;'>Carga de Compras, en el 2do la estadia de cada uno, el 3ro veras si debes poner o recibir plata y el 4to es solo para el dto. contable donde imputa el precio de lo consumido en el dia.</h1>", unsafe_allow_html=True)


selected = option_menu(None, ["Gastos", "Estadia", "Resumen", 'Dto. Contable'],
icons=['cash', 'cloud-upload', "list-task", 'gear'],
menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Gastos":
    gd.gastos()
    
if selected == "Estadia":
    es.estadia()
   
if selected == "Resumen":
    re.resumen()

if selected == "Dto. Contable":
    co.contabilidad()
