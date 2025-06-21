import streamlit as st
import joblib
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.title("Questionário para Treino Personalizado")
st.subheader("Preencha suas informações:")


nome = st.text_input(
    "👤 Nome completo",
    placeholder="Digite seu nome aqui",
    help="Insira seu nome completo para identificação.",
    value=st.session_state.get("dados_usuario", {}).get("Nome", "")
)

peso = st.number_input(
    "Peso (kg)", min_value=40.0, max_value=150.0, step=1.0,
    value=st.session_state.get("dados_usuario", {}).get("Peso (kg)", 40.0)
)

altura = st.number_input(
    "Altura (cm)", min_value=140.0, max_value=210.0, step=1.0,
    value=st.session_state.get("dados_usuario", {}).get("Altura (cm)", 140.0)
)

historico_lesao = st.radio(
    " Possui histórico de lesão?",
    ["Sim", "Não"],
    index=["Sim", "Não"].index(
        st.session_state.get("dados_usuario", {}).get("lesao_encoded", "Sim")
    )
)


objetivo = st.selectbox(
    " Objetivo do treino",
    ["", "Maratona", "Bem-estar", "Emagrecimento"],
    index=["", "Maratona", "Bem-estar", "Emagrecimento"].index(
        st.session_state.get("dados_usuario", {}).get("objetivo_encoded", "")
    )
)


st.text("")

st.markdown("Para entendermos melhor o seu nível atual como corredor, "
            "responda às perguntas abaixo com base nos seus treinos anteriores.\n\n"

            "Indique o tempo médio e a distância média que costuma correr por treino e o seu pace médio "
            "(ritmo, em minutos por quilômetro). **Caso nunca tenha treinado antes, digite 0 nos campos.**")

st.text("")

tempo = st.number_input(
    "⏱ Qual sua média de tempo por treino em minutos?", min_value=0, max_value=180, step=5,
    value=st.session_state.get("dados_usuario", {}).get("Tempo (min)", 0)
)

distancia = st.number_input(
    " Distância média por treino (km)", min_value=0.0, max_value=50.0, step=0.5,
    value=st.session_state.get("dados_usuario", {}).get("Distância (km)", 0.0)
)

pace = st.number_input(
    " Pace médio (min/km)", min_value=0.0, max_value=15.0, step=0.1,
    help="Informe seu ritmo médio de corrida (minutos por quilômetro)",
    value=st.session_state.get("dados_usuario", {}).get("Pace (min/km)", 0.0)
)


atividades_semana = st.slider(
    " Quantos dias por semana você pratica atividade física",
    min_value=0, max_value=7,
    value=st.session_state.get("dados_usuario", {}).get("Atividades/semana", 0)
)


CAMINHO_BASE = os.path.dirname(__file__)

modelo = joblib.load(os.path.join(CAMINHO_BASE, "modelo_utilizar.pkl"))
encoder1 = joblib.load(os.path.join(CAMINHO_BASE, "encoder_objetivo.pkl"))
encoder2 = joblib.load(os.path.join(CAMINHO_BASE, "encoder_lesao.pkl"))

dados_gerados = None

erros = []

if "dados_gerados" not in st.session_state:
    st.session_state["dados_gerados"] = False

if st.button("🚀 Salvar dados"):

    nome_limpo = nome.strip()

    if not nome_limpo:
        erros.append("❌ Informe seu Nome.")
    elif not all(palavra.isalpha() for palavra in nome_limpo.split()):
        erros.append(
            "❌ O nome deve conter apenas letras e espaços. Números ou símbolos não são permitidos.")

    if objetivo == "":
        erros.append("❌ Selecione um objetivo de treino.")

    if erros:
        for erro in erros:
            st.error(erro)
    else:

        dados = {
            "Nome": str(nome_limpo),
            "Peso (kg)": float(peso),
            "Altura (cm)": float(altura),
            "Tempo (min)": int(tempo),
            "Distância (km)": float(distancia),
            "Pace (min/km)": float(pace),
            "lesao_encoded": str(historico_lesao),
            "Atividades/semana": int(atividades_semana),
            "objetivo_encoded": str(objetivo),
        }

        st.session_state["dados_usuario"] = dados
        st.session_state["dados_gerados"] = True
        st.success("✅ Dados coletados com sucesso!")

    if st.session_state.get("dados_gerados", False):
        try:
            dados_modelo = {
                "Tempo (min)": int(tempo),
                "Distância (km)": float(distancia),
                # Sim=1, Não=0
                "lesao_encoded": encoder2.transform([historico_lesao])[0],
                "Pace (min/km)": float(pace),
                "Atividades/semana": int(atividades_semana),
                # Bem-estar=0, Emagrecimento=1, Maratona=2
                "objetivo_encoded": encoder1.transform([objetivo])[0],
            }
            previsao = modelo.predict(pd.DataFrame([dados_modelo]))[0]

            st.session_state["previsao"] = {
                0: "avancado",
                1: "iniciante",
                2: "intermediario"
            }[previsao]

            st.session_state["previsao"] = previsao
            st.session_state["historico_lesao"] = historico_lesao

        except Exception as e:
            st.error("Erro ao processar. Verifique os dados e tente novamente.")


if st.session_state["dados_gerados"]:
    if st.button("Verifique seu Treino"):
        st.switch_page("ia_recomendacao.py")
