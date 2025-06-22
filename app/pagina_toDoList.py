import streamlit as st
import google.generativeai as genai
from fpdf import FPDF


API_KEY = "AIzaSyBUb0tOQMD1mrcAu5DCtaAMEU_zer7nxwE"  
genai.configure(api_key=API_KEY) #metodo do gemini pra configurar. tem como parametro o api key igualando a alguma variavel.

# funcao pra pedir o treino pra o gemini
def gerar_treino_personalizado(entrada_ia, nivel_texto):
    prompt = f"""
    Você é um treinador especialista em corrida.

    Gere um plano de corrida para o seguinte perfil:

    - Nível: {entrada_ia['nivel']}
    - Nome: {entrada_ia['nome']}
    - Peso: {entrada_ia['peso']} kg
    - Altura: {entrada_ia['altura']} cm
    - Tempo médio por treino: {entrada_ia['tempo_medio_treino']} minutos
    - Distância média por treino: {entrada_ia['distancia_media_treino']} km
    - Pace médio: {entrada_ia['pace']} min/km
    - Histórico de lesão: {entrada_ia['lesao']}
    - Dias disponíveis por semana: {entrada_ia['dias_por_semana']}
    - Objetivo: {entrada_ia['objetivo']}
    - Tempo disponível por dia: {entrada_ia['tempo_disponivel_minutos']} minutos
    - Distância alvo: {entrada_ia['distancia_desejada']} km
    - Dias totais de treino: {entrada_ia['dias_de_treino']} dias

    Deixe todo treino organizado de maneira justificada. Liste todas as variáveis na introdução do treino.  Nível, peso, altura, tempo medio, tudo... Divida o plano por dia, seja específico com os tipos de treino (ex: Trote leve 30min, Intervalado, Longão).
    Não use academia nem equipamentos avançados. Acentue corretamente as palavras, mas não use caracteres como asteriscos e traços (hifens), exceto acentos graficos de pontuaçao (não precisa dizer na resposta que não vai usar esses caracteres.)
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

    return pdf.output(dest='S').encode('latin-1')  #retorna o download do pdf


st.title("🏃 Treino Personalizado")

#ia de previsao numerica
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

#conferir dados
campos_necessarios = ["objetivo_encoded", "Distância (km)", "Atividades/semana", "Tempo (min)", "lesao_encoded"]
if all(campo in dados_usuario for campo in campos_necessarios):

    #dados pro prompt
    entrada_ia = {
    "nivel": nivel_texto,
    "nome": st.session_state["dados_usuario"]["Nome"],
    "peso": st.session_state["dados_usuario"]["Peso (kg)"],
    "altura": st.session_state["dados_usuario"]["Altura (cm)"],
    "tempo_medio_treino": st.session_state["dados_usuario"]["Tempo (min)"],
    "distancia_media_treino": st.session_state["dados_usuario"]["Distância (km)"],
    "pace": st.session_state["dados_usuario"]["Pace (min/km)"],
    "lesao": st.session_state["dados_usuario"]["lesao_encoded"],
    "dias_por_semana": st.session_state["dados_usuario"]["Atividades/semana"],
    "objetivo": st.session_state["dados_usuario"]["objetivo_encoded"],
    "tempo_disponivel_minutos": st.session_state["dados_usuario"]["Tempo disponivel"],
    "distancia_desejada": st.session_state["dados_usuario"]["Distância desejada"],
    "dias_de_treino": st.session_state["dados_usuario"]["Dias de treino"]
}

    if st.session_state.get("auto_gerar_pdf"):
        treino_texto = gerar_treino_personalizado(entrada_ia, nivel_texto)

        if treino_texto:
            st.markdown("### ✅ Plano de Treino Gerado pela IA:")
            st.text_area("📋 Treino:", treino_texto, height=400)

            #botao de download do pdf
            pdf_bytes = gerar_pdf(dados_usuario.get("Nome", "Usuário"), treino_texto)

            st.download_button(
                label="📥 Baixar Treino em PDF",
                data=pdf_bytes,
                file_name="treino_personalizado.pdf",
                mime="application/pdf"
            )

else:
    st.warning("⚠️ Dados incompletos. Volte e preencha o questionário primeiro.")
