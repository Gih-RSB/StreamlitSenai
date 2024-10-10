import streamlit as st

st.write("Olá, mundo!")

numero = st.number_input("Digite um número:", format="%d")

if numero > 0:
    st.write('O número é positivo.')
elif numero < 0:
    st.write('O número é negativo.')
else:
    st.write('O número é nulo (zero).')
