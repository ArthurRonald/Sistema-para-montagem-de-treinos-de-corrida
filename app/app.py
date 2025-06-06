import streamlit as st
import pagina_inicial
import pagina_perfil
import pagina_questionario
import pagina_toDoList
import pagina_questionario2


paginas = {"Sobre o Site": [
    st.Page("pagina_inicial.py", title="Inicio", default=True)],
    "Você": [
        st.Page("pagina_perfil.py", title="Perfil"),
        st.Page("pagina_questionario.py", title="Questionário"),
        st.Page("pagina_toDoList.py", title="Check-List"),
        st.Page("pagina_questionario2.py", title="Avaliação do Treino")
],
    "  ": [st.Page("pagina_final.py", title="FIM")]
}

pg = st.navigation(paginas)
pg.run()
