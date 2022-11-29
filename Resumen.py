import streamlit as st
import pandas as pd



def resumen():
    huesped = pd.read_csv('huespedes.csv')

    col_list = huesped[huesped.columns[0]].values.tolist()


    tupla = tuple(col_list)

    st.selectbox(
        'Ingresa tu Nombre:',
    tupla, key="name")

    if st.checkbox('¡No encuentro mi nombre!'):
        st.text_input("Ingresa tu nombre", key="name1")


    try:
        nombre = st.session_state.name1
    except:
        nombre = st.session_state.name


    
    df = pd.read_csv('huespedes.csv')

    df1 =df.drop(df.index[0])
    df1 = df[df['Nombre'] == nombre]
   


    st.write('''
## Estadia
''')
    st.dataframe(df1)





    df = pd.read_csv('Quinta.csv')

    df1 =df.drop(df.index[0])
    df1 = df[df['Nombre'] == nombre]
    st.write('''
## Gastos
''')
    st.dataframe(df1)