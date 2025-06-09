import streamlit as st

# https://docs.streamlit.io/develop/api-reference/execution-flow/st.form
# https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/llm-quickstart

st.title("Questionario para Treino Personalizado")
st.subheader("Preencha suas informações:")

nome = st.text_input(
    "👤 Nome completo",
    placeholder="Digite seu nome aqui",
    help="Insira seu nome completo para identificação."
)

objetivo = st.selectbox(
    "Objetivo do treino",
    ["", "Maratona", "Bem-estar", "Emagrecimento"]
)

tempo = st.number_input(
    "Tempo disponível por treino (minutos)", min_value=20.0, max_value=180.0, step=1.0
)

historico_lesao = st.radio(
    "Possui histórico de lesão?",
    ["Sim", "Não"]
)

peso = st.number_input(
    "Peso (kg)", min_value=50.0, max_value=100.0, step=0.1
)

altura = st.number_input(
    "Altura (cm)", min_value=150.0, max_value=200.0, step=1.0
)

atividades_semana = st.slider(
    "Quantos dias por semana pratica algum tipo de atividade física?",
    min_value=1, max_value=7
)


if st.button("🚀 Gerar Dados"):
    erros = []

    if not nome.strip():
        erros.append("❌ Informe seu Nome.")

    if objetivo == "":
        erros.append("❌ Selecione um objetivo de treino.")

    if erros:
        for erro in erros:
            st.error(erro)
    else:
        dados = {
            "Nome": nome.strip(),
            "Objetivo do treino": objetivo,
            "Tempo (min)": int(tempo),
            "Histórico de lesão": historico_lesao,
            "Peso (kg)": float(peso),
            "Altura (cm)": float(altura),
            "Atividades/semana": int(atividades_semana)
        }

        st.success("✅ Dados coletados com sucesso!")
        st.session_state["dados_usuario"] = dados
