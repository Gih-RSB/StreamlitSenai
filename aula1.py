import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS 🛒")

url = "https://labdados.com/produtos?regiao=norte&ano=2022"
response = requests.get(url)

if response.status_code == 200:
    df = pd.DataFrame.from_dict(response.json())
    st.dataframe(df)

    if st.button("todos"):
        st.balloons()
        st.metric('Receita', df['Preço'].sum())
        st.metric('Quantidade de vendas (linhas)', df.shape[0])
        st.metric('Quantidade de variáveis (colunas)', df.shape[1])
        st.dataframe(df)
        st.snow()
    else:
        st.write("Clique no botão 'todos' para visualizar os dados.")
else:
    st.error("Erro ao carregar os dados. Tente novamente mais tarde.")
