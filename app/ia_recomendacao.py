import streamlit as st
import google.generativeai as genai
from fpdf import FPDF


API_KEY = "AIzaSyBUb0tOQMD1mrcAu5DCtaAMEU_zer7nxwE"  # Substitua pela sua key Gemini
genai.configure(api_key=API_KEY)


def gerar_treino_personalizado(dados_usuario, nivel):
    prompt = f"""
    Você é um treinador especialista em corrida.

    Gere um plano de corrida para o seguinte perfil:

    - Nível: {nivel}
    - Objetivo: {dados_usuario['objetivo']}
    - Distância desejada: {dados_usuario['distancia']} km
    - Dias por semana: {dados_usuario['dias_por_semana']}
    - Minutos por dia: {dados_usuario['minutos_por_dia']}
    - Histórico de lesão: {dados_usuario['lesao']}
    - Prazo total: {dados_usuario['dias_total']} dias

    Divida o plano por dia, seja específico com os tipos de treino (ex: Trote leve 30min, Intervalado, Longão).
    Não use academia nem equipamentos avançados. NÃO USE CARACTERES UNICODE, exceto acentos graficos de pontuaçao (não precisa dizer na resposta que não vai usar esses caracteres.)
    """

    model = genai.GenerativeModel('gemini-2.5-flash')

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Erro ao gerar o treino: {e}")
        return "❌ Não foi possível gerar o treino no momento."


def gerar_pdf(nome, treino_texto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Plano de Treino Personalizado para {nome}", ln=True, align='C')
    
    pdf.set_font("Arial", "", 12)
    for linha in treino_texto.split('\n'):
        pdf.multi_cell(0, 10, linha)

    return pdf.output(dest='S').encode('latin-1')  # Retorna o PDF como bytes para download no Streamlit



st.title("🏃 Treino Personalizado")

# Dados da sessão
previsao_numerica = st.session_state.get("previsao")
nivel_texto = ""

if previsao_numerica == 0:
    nivel_texto = "Avançado"
elif previsao_numerica == 1:
    nivel_texto = "Iniciante"
elif previsao_numerica == 2:
    nivel_texto = "Intermediário"
else:
    st.error("Nível não reconhecido. Por favor, refaça o questionário.")

dados_usuario = st.session_state.get("dados_usuario", {})

# Conferindo se os dados necessários estão disponíveis
campos_necessarios = ["objetivo_encoded", "Distância (km)", "Atividades/semana", "Tempo (min)", "lesao_encoded"]
if all(campo in dados_usuario for campo in campos_necessarios):

    # Montando os dados para o prompt
    entrada_ia = {
        "objetivo": dados_usuario["objetivo_encoded"],
        "distancia": dados_usuario["Distância (km)"],
        "dias_por_semana": dados_usuario["Atividades/semana"],
        "minutos_por_dia": dados_usuario["Tempo (min)"],
        "lesao": dados_usuario["lesao_encoded"],
        "dias_total": 30  # Pode ajustar esse valor se quiser
    }

    if st.button("🚀 Gerar Treino"):
        treino_texto = gerar_treino_personalizado(entrada_ia, nivel_texto)

        if treino_texto:
            st.markdown("### ✅ Plano de Treino Gerado pela IA:")
            st.text_area("📋 Treino:", treino_texto, height=400)

            # Botão de Download do PDF
            pdf_bytes = gerar_pdf(dados_usuario.get("Nome", "Usuário"), treino_texto)

            st.download_button(
                label="📥 Baixar Treino em PDF",
                data=pdf_bytes,
                file_name="treino_personalizado.pdf",
                mime="application/pdf"
            )

else:
    st.warning("⚠️ Dados incompletos. Volte e preencha o questionário primeiro.")
