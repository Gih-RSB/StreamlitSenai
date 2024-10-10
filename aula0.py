import streamlit as st

st.write("Olá, mundo!")

idade = st.number_input("Digite sua idade:", min_value=14, max_value=120)

if idade >= 18:
    st.write('Olá, mundo! - você é maior de idade.')
else:
    st.write('Olá, mundo! - você é menor de idade.')

# importe o stramlit - baby step -1
# entre com um número  - baby step -2
#verifiques o numero é positivo, negativo ou nulo



