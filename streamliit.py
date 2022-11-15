import streamlit as st
import pandas as pd
import Gestion as gd
import csv

st.write('''
## `Gestión Kurt Dic 22`
''')

huesped = pd.read_csv('huespedes.csv')

col_list = huesped[huesped.columns[0]].values.tolist()


tupla = tuple(col_list)

option = st.selectbox(
    'Ingresa tu Nombre:',
   tupla, key="name")

if st.checkbox('¡No encuentro mi nombre!'):
    st.text_input("Ingresa tu nombre", key="name1")
    nombre1 = st.session_state.name1
    
    


   



# You can access the value at any point with:





try:
    nombre = st.session_state.name1
except:
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
    
        precioconvert = int(precio)
        if nombre == "":
            st.write('¡Seleccione su Nombre!')
            pass
        else:
            if nombre == "Seleccione un nombre":
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
                            
                            p = gd.Person(nombre, descripcion, precioconvert)
                            p.say_hi()


            

        

    except ValueError:
        st.write('El precio debe ser un numero entero')


