import streamlit as st


# st.set_page_config(page_title=" Projeto Corrida", page_icon="🏃‍♂️")

st.sidebar.title("Você")
menu = st.sidebar.selectbox(
    "Escolha uma opção", ["Cadastro", "Treinos", "To-Do List", "Acompanhamento"])


if menu == "Cadastro":
    st.title("🏃‍♂️ Cadastro do Corredor")

    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
    peso = st.number_input("Peso (kg)", min_value=30.0,
                           max_value=200.0, step=0.1)
    altura = st.number_input(
        "Altura (cm)", min_value=130.0, max_value=220.0, step=0.1)

    objetivo = st.selectbox(
        "Objetivo",
        ["Perder peso", "Melhorar pace", "Completar 5km",
            "Completar 10km", "Meia maratona (21km)", "Maratona(42km)"]
    )

    nivel = st.selectbox(
        "Nível de corrida",
        ["Iniciante", "Intermediário", "Avançado"]
    )

    dias = st.slider("Quantos dias por semana quer treinar?",
                     min_value=1, max_value=7)

    if st.button("Salvar Cadastro"):
        if nome == "":
            st.warning("Por favor, preencha seu nome.")
        else:
            st.success(f"Cadastro salvo com sucesso! Bem-vindo, {nome}! 🎉")
            st.session_state["usuario"] = {
                "nome": nome,
                "idade": idade,
                "peso": peso,
                "altura": altura,
                "objetivo": objetivo,
                "nivel": nivel,
                "dias_por_semana": dias
            }

            st.write("### Seus dados:")
            st.json(st.session_state["usuario"])

elif menu == "Treinos":
    st.title("  Agenda de Treinos")

    if "usuario" not in st.session_state:
        st.write("Por favor, preencha seu cadastro.")
    else:
        usuario = st.session_state["usuario"]
        st.subheader(f"Treino para {usuario['nome']}")
        st.write(f"🎯 Objetivo: {usuario['objetivo']}")
        st.write(f"  Nível: {usuario['nivel']}")
        st.write(f"📅 Dias por semana: {usuario['dias_por_semana']}")
