import streamlit as st

st.title("👤 Perfil do Usuário")

if "dados_usuario" in st.session_state:
    dados = st.session_state["dados_usuario"]

    if "foto_usuario" not in st.session_state:
        st.session_state["foto_usuario"] = None

# Só mostra a câmera se ainda não tiver tirado a foto
    if st.session_state["foto_usuario"] is None:
        foto = st.camera_input("Tire uma foto")

    # Se o usuário tirar a foto, salva em session_state
    if foto:
        st.session_state["foto_usuario"] = foto
        st.success("📷 Foto capturada com sucesso!")

    # Se já tirou a foto, mostra a imagem salva
    if st.session_state["foto_usuario"] is not None:
        st.image(st.session_state["foto_usuario"],
                 caption="Foto do Usuário", use_container_width=True)

    st.subheader(f"Nome: {dados['Nome']}")
    st.write(f"Objetivo: {dados['Objetivo do treino']}")
    st.write(f"Tempo disponível: {dados['Tempo (min)']} minutos")
    st.write(f"Histórico de lesão: {dados['Histórico de lesão']}")
    st.write(f"Peso: {dados['Peso (kg)']} kg")
    st.write(f"Altura: {dados['Altura (cm)']} cm")
    st.write(f"Atividades na semana: {dados['Atividades/semana']} dias")

else:
    st.warning("Nenhum dado disponível. Faça o cadastro no questionário primeiro.")
