import streamlit as st
from app.ia_recomendacao import gerar_treino_personalizado
from app.gerar_pdf_treino import gerar_pdf

# Inputs do usuário (os dados vão tá repetidos sim, é mais pra ver se o código funciona)
nivel = st.selectbox("Nível do atleta:", ["Iniciante", "Intermediário", "Avançado"])
objetivo = st.selectbox("Objetivo:", ["Maratona", "Emagrecimento", "Bem-estar"])
distancia = st.number_input("Distância alvo (em km):", min_value=1, max_value=100)
dias_por_semana = st.slider("Dias por semana disponíveis para treino:", 1, 7)
minutos_por_dia = st.slider("Minutos disponíveis por dia:", 10, 180)
lesao = st.radio("Histórico de lesão?", ["Sim", "Não"])
dias_total = st.selectbox("Prazo total do plano:", [10, 15, 20, 30])

# Empacotamento dos dados do usuário 
dados_usuario = {
    "nivel": nivel,
    "objetivo": objetivo,
    "distancia": distancia,
    "dias_por_semana": dias_por_semana,
    "minutos_por_dia": minutos_por_dia,
    "lesao": lesao,
    "dias_total": dias_total
}

# Botão para gerar recomendação 
if st.button("Recomendação Inteligente"):
    st.info("Gerando plano personalizado com IA...")
    plano = gerar_treino_personalizado(dados_usuario)
    caminho_pdf = gerar_pdf(plano)
    st.success("Plano gerado com sucesso!")
    
    with open(caminho_pdf, "rb") as file:
        st.download_button("📥 Baixar Plano de Treino", file, file_name="treino_personalizado.pdf")
