import streamlit as st
import pagina_inicial
import pagina_questionario


paginas = {"Sobre o Site": [
    st.Page("pagina_inicial.py", title="Página Inicial", default=True)],
    "Você": [
        st.Page("pagina_questionario.py", title="Questionário")
]

}

pg = st.navigation(paginas)
pg.run()
