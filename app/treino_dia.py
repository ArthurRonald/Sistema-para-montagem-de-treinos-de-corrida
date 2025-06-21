import streamlit as st


if "dia_atual" not in st.session_state or "origem" not in st.session_state:
    st.error("Treino não selecionado.")
    st.stop()

dia = st.session_state.dia_atual
origem = st.session_state.origem
treino_key = "treinos_" + origem.split("_")[-1].replace(".py", "")

st.title(f"Treino do Dia {dia}")
st.write("Faça seu treino com dedicação!")

if st.button("✅ Concluir Treino"):
    st.session_state[treino_key][dia - 1] = True
    st.success("Treino concluído!")
    st.switch_page("pagina_toDoList.py")
