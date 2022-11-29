import streamlit as st
import pandas as pd
import Gestion as gd


def contabilidad():
    st.text_input("Ingrese Contraseña", key="contraseña", type='password')
    contraseña = st.session_state.contraseña
    if contraseña != 'yamimaxi':
                        st.write('Contraseña Incorrecta')
                        pass
    else:
            huesped = pd.read_csv('huespedes.csv')

            col_list = huesped[huesped.columns[0]].values.tolist()


            tupla = tuple(col_list)

            st.selectbox(
                'Ingresa tu Nombre:',
            tupla, key="name")

            if st.checkbox('¡No encuentro mi nombre!'):
                st.text_input("Ingresa tu nombre", key="name1")
                
            