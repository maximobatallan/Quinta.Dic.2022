import streamlit as st
from streamlit_option_menu import option_menu
import Gastos as gd
import Estadia as es
import Resumen as re
import Contabilidad as co

st.write('''
## `Gestión Kurt Dic 22`
''')


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
