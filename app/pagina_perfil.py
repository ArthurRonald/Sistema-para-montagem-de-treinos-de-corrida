import streamlit as st

st.title("👤 Perfil do Usuário")

if "dados_usuario" in st.session_state:

    dados = st.session_state["dados_usuario"]

    st.subheader(f"Nome: {dados['Nome']}")
    st.write(f"Objetivo: {dados['Objetivo do treino']}")
    st.write(f"Tempo disponível: {dados['Tempo (min)']} minutos")
    st.write(f"Histórico de lesão: {dados['Histórico de lesão']}")
    st.write(f"Peso: {dados['Peso (kg)']} kg")
    st.write(f"Altura: {dados['Altura (cm)']} cm")
    st.write(f"Atividades na semana: {dados['Atividades/semana']} dias")

else:
    st.warning("Nenhum dado disponível. Faça o cadastro no questionário primeiro.")
