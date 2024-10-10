# 1. Crie o número secreto
# 2. Coloque o Título na aplicação
# 3. Dê uma mensagem de boas-vindas
# 4. Receba o chute do usuário
# 5. Verifique o chute com o número secreto

import streamlit as st
import random

def iniciar_jogo():
    st.session_state.numero_secreto = random.randint(1, 10)
    st.session_state.acertou = False

if 'numero_secreto' not in st.session_state:
    iniciar_jogo()

st.title("Adivinhe o Número Secreto!")

st.write("Bem-vindo ao jogo! Tente adivinhar o número secreto entre 1 e 10.")

chute = st.number_input("Digite seu palpite:", min_value=1, max_value=10)

if st.button("Chutar"):
    if chute < st.session_state.numero_secreto:
        st.write("Seu palpite é muito baixo. Tente novamente!")
    elif chute > st.session_state.numero_secreto:
        st.write("Seu palpite é muito alto. Tente novamente!")
    else:
        st.write("Parabéns! Você adivinhou o número secreto!")
        st.session_state.acertou = True

if st.button("Jogar Novamente"):
    iniciar_jogo()

if st.session_state.acertou:
    st.write("Você pode jogar novamente clicando no botão abaixo!")
