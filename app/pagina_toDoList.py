import streamlit as st
import pandas as pd

st.title("Confira o treino ideal para o nível da atividade desejada")

previsao = st.session_state.get("previsao")
historico_lesao = st.session_state.get(
    "dados_usuario", {}).get("lesao_encoded")

if previsao is None or historico_lesao is None:
    st.error(
        "❌ Dados do usuário não encontrados. Por favor, preencha o questionário primeiro.")
else:
    st.subheader(
        f"O nível adequado para sua atividade é {str(previsao).upper()}")

    if previsao == "avancado" and historico_lesao == "Não":
        treino = pd.read_csv("AVANÇADO SEM LESÃO.csv")
        st.write(treino)
    elif previsao == "avancado" and historico_lesao == "Sim":
        treino = pd.read_csv("AVANÇADO COM LESÃO.csv")
        st.write(treino)

    elif previsao == "intermediario" and historico_lesao == "Não":
        treino = pd.read_csv("INTERMEDIÁRIO SEM LESÃO.csv")
        st.write(treino)

    elif previsao == "intermediario" and historico_lesao == "Sim":
        treino = pd.read_csv("INTERMEDIÁRIO COM LESÃO.csv")
        st.write(treino)

    elif previsao == "iniciante" and historico_lesao == "Não":
        treino = pd.read_csv("INICIANTE SEM LESÃO.csv")
        st.write(treino)

    elif previsao == "iniciante" and historico_lesao == "Sim":
        treino = pd.read_csv("INICIANTE COM LESÃO.csv")
        st.write(treino)
