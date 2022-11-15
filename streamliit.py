import streamlit as st
import numpy as np
import pandas as pd
import Gestion as gd



st.markdown('Gestión Kurt **_Diciembre_ 2022**.')

st.text_input("Ingresa tu Nombre", key="name")

# You can access the value at any point with:

nombre = st.session_state.name

st.text_input("Descripcion", key="descripcion")

# You can access the value at any point with:

descripcion = st.session_state.descripcion

st.text_input("Precio", key="precio")

# You can access the value at any point with:

precio = st.session_state.precio






dataframe = pd.read_csv('Quinta.csv')



st.dataframe(dataframe)

if st.checkbox('Actualizar Tabla'):
   pass




if st.button('Guardar'):
    
    try:
        #nombreconvert= str()
        #descripcovert=
        precioconvert = int(precio)
        if nombre == "":
            st.write('¡Seleccione su Nombre!')
            pass
        else:
            if descripcion == "":
                st.write('¡Seleccione el tipo de Gasto!')
                pass
            else:
                if precio == "":
                    st.write('¡Ingrese el precio del gasto!')
                    pass
                else:
                        print(nombre)
                        p = gd.Person(nombre, descripcion, precioconvert)
                        p.say_hi()


        

        

    except ValueError:
        st.write('El precio debe ser un numero entero')
