import pandas as pd
import streamlit as st
previsao = st.session_state.get("previsao", None)
historico_lesao = st.session_state.get("historico_lesao", None)
st.title("Confira o treino ideal para o nível da atividade desejada")
st.subheader(f'O nível adequado para sua atividade é **{previsao}**')

if previsao== "avancado" and historico_lesao == "Não":
    treino1= pd.read_csv("AVANÇADO SEM LESÃO.csv")
    print(treino1)

elif previsao== "avancado" and historico_lesao == "Sim":
    treino2= pd.read_csv("AVANÇADO COM LESÃO.csv")
    print(treino2)
elif previsao== "intermediario" and historico_lesao == "Não":
    treino3= pd.read_csv("INTERMEDIÁRIO SEM LESÃO.csv")
    print(treino3)
elif previsao== "intermediario" and historico_lesao == "Sim":
    treino4= pd.read_csv("INTERMEDIÁRIO COM LESÃO.csv")
    print(treino4)
elif previsao== "iniciante" and historico_lesao == "Não":
    treino5= pd.read_csv("INICIANTE SEM LESÃO.csv")
    print(treino5)
elif previsao== "iniciante" and historico_lesao == "Sim":
    treino6= pd.read_csv("INICIANTE COM LESÃO.csv")    
