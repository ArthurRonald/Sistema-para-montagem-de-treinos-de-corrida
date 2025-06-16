import streamlit as st

st.title("👤 Perfil do Usuário")

if "dados_usuario" in st.session_state:

    dados = st.session_state["dados_usuario"]

    st.subheader(f"Nome: {dados['Nome']}")
    st.write(f"Peso: {dados['Peso (kg)']} kg")
    st.write(f"Altura: {dados['Altura (cm)']} cm")
    st.write(f"Objetivo: {dados['objetivo_encoded']}")
    st.write(f"Tempo disponível: {dados['Tempo (min)']} minutos")
    st.write(f"Histórico de lesão: {dados['lesao_encoded']}")
    st.write(f"Atividades na semana: {dados['Atividades/semana']} dias")
    st.write(f"Distância Média: {dados["Distância (km)"]} km")
    st.write(f"Pace: {dados["Pace (min/km)"]:.2f} (min/km)")

else:
    st.warning("Nenhum dado disponível. Faça o cadastro no questionário primeiro.")
