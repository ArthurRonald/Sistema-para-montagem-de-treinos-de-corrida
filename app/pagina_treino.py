import streamlit as st
import google.generativeai as genai
from fpdf import FPDF


API_KEY = "AIzaSyBUb0tOQMD1mrcAu5DCtaAMEU_zer7nxwE"
# metodo do gemini pra configurar. tem como parametro o api key igualando a alguma variavel.
genai.configure(api_key=API_KEY)

# funcao pra pedir o treino pra o gemini
#prompt é o que a ia irá receber como pedido
def gerar_treino_personalizado(entrada_ia):
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
    - Dias que pratica atividade física: {entrada_ia['dias_por_semana']}
    - Objetivo: {entrada_ia['objetivo']}
    - Tempo disponível por dia: {entrada_ia['tempo_disponivel_minutos']} minutos
    - Distância alvo: {entrada_ia['distancia_desejada']} km
    - Dias totais de treino: {entrada_ia['dias_de_treino']} dias

    Deixe todo treino organizado de maneira justificada. Liste todas as variáveis na introdução do treino.  Nível, peso, altura, tempo medio, tudo... Divida o plano por dia, seja específico com os tipos de treino (ex: Trote leve 30min, Intervalado, Longão).
    Não use academia nem equipamentos avançados. Não use negrito em nenhuma palavra. Acentue corretamente as palavras, mas não use caracteres como emojis, asteriscos nem traços (hifens), exceto acentos graficos de pontuaçao (não precisa dizer na resposta que não vai usar esses caracteres.) Para separar as linhas, nao use nenhum caractere especial.
    """

    model = genai.GenerativeModel('gemini-2.5-flash') 

    try:
        response = model.generate_content(prompt) #aqui pede pra ia gerar
        return response.text # e retorna pra essa variavel a resposta
    
    except Exception as e: #caso de erro, é capturado e retorna uma mensagem
        st.error(f"Erro ao gerar o treino: {e}")
        return "❌ Não foi possível gerar o treino no momento."


def gerar_pdf(nome, treino_texto): #argumentos pra dizer o nome e colocar o treino no pdf
    pdf = FPDF() 
    pdf.add_page() #adiciona a pagina
    pdf.set_font("Arial", "B", 16) #fonte, negrito, tamanho
    pdf.cell(
        0, 10, f"Plano de Treino Personalizado para {nome}", ln=True, align='C') 
    #ocupa toda a largura, define a altura, proximo comando vai pra outra linha, centralizado

    pdf.set_font("Arial", "", 12) #nao negrito
    for linha in treino_texto.split('\n'): #divide a resposta da ia em linhas, e roda em loop
        pdf.multi_cell(0, 10, linha)

    return pdf.output(dest='S').encode('latin-1')  #salva o pdf na memoria (bytes)


# funcao pra nao quebrar se vier emoji ou outro unicode
def limpar_texto_pdf(treino_texto):
    return treino_texto.encode('latin-1', errors='ignore').decode('latin-1')


titulo = st.title("🏃 Treino Personalizado")

# ia de previsao numerica
previsao_numerica = st.session_state.get("previsao")
nivel_texto = "" #inicializa a string como vazia

if previsao_numerica == 0:
    nivel_texto = "Avançado"
elif previsao_numerica == 1:
    nivel_texto = "Iniciante"
elif previsao_numerica == 2:
    nivel_texto = "Intermediário"
else:
    st.error("Nível não reconhecido. Por favor, refaça o questionário.")

dados_usuario = st.session_state.get("dados_usuario", {}) #puxa os dados do cara


# conferir alguns dados
campos_necessarios = ["objetivo_encoded",
                      "Distância (km)", "Atividades/semana", "Tempo (min)", "lesao_encoded"]

#funcao all gera um true ou false
#so e true se todos os campos estiverem em dados usuario
if all(campo in dados_usuario for campo in campos_necessarios):

    # dados pro prompt
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

        if "Treino ia" not in st.session_state:  # so gera o pdf se for a primeira vez

            with st.spinner("Criação do treino em progresso. Aguarde alguns instantes..."):
                
                treino_texto = gerar_treino_personalizado(entrada_ia) #gera o treino com base na entrada ia
                treino_texto_limpo = limpar_texto_pdf(treino_texto)  # chama a funcao de ajeitar os unicode
                st.session_state["Treino ia"] = treino_texto_limpo #salva na memoria o treino

        # Pra nao gerar infinitamente
        st.session_state["auto_gerar_pdf"] = False 

    if "Treino ia" in st.session_state:

        treino_texto_limpo = st.session_state["Treino ia"] #define de novo pra nao quebrar

        # botao de download do pdf
        pdf_bytes = gerar_pdf(dados_usuario.get(
            "Nome", "Usuário"), treino_texto_limpo) #se nao achar o nome usa usuario e gera o pdf
        st.subheader(
            f"✅ Plano de treino gerado com sucesso! Seu nível ideal para sua atividade é **{nivel_texto}**")
        botao_download = st.download_button(
            label="📥 Baixar Treino em PDF",
            data=pdf_bytes,
            file_name="treino_personalizado.pdf",
            mime="application/pdf" #define o tipo pro navegador entender
        ) 


else:
    st.warning("⚠️ Dados não encontrados. Será que você preencheu o formulário?")


# Verifica se os dados do usuário estão salvos
if "dados_usuario" in st.session_state:
    dados = st.session_state["dados_usuario"]
    TOTAL_DIAS = dados["Dias de treino"]

    st.subheader(f"🏃 Lista de Treino - {TOTAL_DIAS} Dias")

    # Inicializa lista de treinos se ainda não existir
    if "treinos" not in st.session_state or len(st.session_state.treinos) != TOTAL_DIAS:
        st.session_state.treinos = [False] * TOTAL_DIAS

    # Inicializa controle da mensagem de sucesso
    if "ultimo_concluido" not in st.session_state:
        st.session_state.ultimo_concluido = None

    # Determina qual é o próximo treino não concluído
    proximo = None
    for i, feito in enumerate(st.session_state.treinos):
        if not feito:
            proximo = i
            break

    for i in range(TOTAL_DIAS):
        dia = i + 1

        if st.session_state.treinos[i]:
            st.markdown(f"✅ Treino Dia {dia}")
        elif i == proximo:

            if st.session_state.ultimo_concluido == dia:
                st.success(f"✅ Treino do Dia concluído com sucesso!")

            if st.button(f"✅ Concluir Treino Dia {dia}"):
                st.session_state.treinos[i] = True
                # Marca o próximo dia como a próxima meta
                st.session_state.ultimo_concluido = dia + 1
                st.rerun()
        else:
            st.markdown(f"🔒 Treino Dia {dia}")

    progresso = sum(st.session_state.treinos) / TOTAL_DIAS
    st.progress(progresso)

    if progresso == 1.0:
        st.success(
            f"🎉 Parabéns, você concluiu todos os seus treinos para alcançar seu objetivo de {dados["Distância desejada"]}Km!")
        if st.button("Avalie o seu plano! 💬"):
            st.switch_page("pagina_final.py")
