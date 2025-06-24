import streamlit as st
import pagina_inicial
import pagina_perfil
import pagina_questionario
import pagina_treino
import pagina_final


# Calcula o progresso, se possível
if "treinos" in st.session_state and "dados_usuario" in st.session_state:
    total_dias = st.session_state["dados_usuario"].get("Dias de treino", 1)
    progresso = sum(st.session_state["treinos"]) / \
        total_dias if total_dias > 0 else 0
else:
    progresso = 0

# Define as páginas disponíveis com base no progresso
paginas = {
    "Sobre o Site": [st.Page("pagina_inicial.py", title="Inicio", default=True)],
    "Você": [
        st.Page("pagina_perfil.py", title="Perfil"),
        st.Page("pagina_questionario.py", title="Questionário"),
        st.Page("pagina_treino.py", title="Seu Treino"),
    ]
}

# Só mostra a página final se o progresso estiver completo
if progresso == 1.0:
    paginas["Feedback"] = [st.Page("pagina_final.py", title="Avalie-nos")]

# Roda o navegador de páginas
pg = st.navigation(paginas)
pg.run()
