import streamlit as st

st.title("👤 Perfil do Usuário")

if "dados_usuario" in st.session_state:

    dados = st.session_state["dados_usuario"]

    st.subheader("Dados Pessoais")
    st.write(f"Nome: {dados['Nome']}")
    st.write(f"Peso: {dados['Peso (kg)']} kg")
    st.write(f"Altura: {dados['Altura (cm)']} cm")

    st.subheader("Dados Para Personalização de Treino")
    st.write(f"Tempo disponível: {dados['Tempo disponivel']} minutos")
    st.write(f"Distância Desejada: {dados["Distância desejada"]}Km")
    st.write(f"Plano de Treino: {dados["Dias de treino"]} dias")

    st.subheader("Dados Para Medição de Nível")
    st.write(f"Objetivo: {dados['objetivo_encoded']}")
    st.write(f"Histórico de lesão: {dados['lesao_encoded']}")
    st.write(f"Atividades na semana: {dados['Atividades/semana']} dias")
    st.write(f"Distância Média: {dados["Distância (km)"]} km")
    st.write(f"Pace: {dados["Pace (min/km)"]:.2f} (min/km)")
    st.write(f"Tempo médio: {dados["Tempo (min)"]} min")

else:
    st.warning("Nenhum dado disponível. Faça o cadastro no questionário primeiro.")
