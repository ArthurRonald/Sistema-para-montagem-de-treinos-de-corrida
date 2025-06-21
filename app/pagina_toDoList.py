import streamlit as st
from app.ia_recomendacao import gerar_treino_personalizado
from app.gerar_pdf_treino import gerar_pdf


if "dados_usuario" in st.session_state:

    dados = st.session_state["dados_usuario"]

    if dados["Dias de treino"] == "10":
        TOTAL_DIAS = 10
        st.set_page_config(page_title="Treino 10 Dias")
        st.title(f"🏃 Plano de Treino - {TOTAL_DIAS} Dias")

        if "treinos_10" not in st.session_state or len(st.session_state.treinos_10) != TOTAL_DIAS:
            st.session_state.treinos_10 = [False] * TOTAL_DIAS

        proximo = None
        for i, feito in enumerate(st.session_state.treinos_10):
            if not feito:
                proximo = i + 1
                break

        st.subheader("📋 Lista de Treinos")

        for i in range(TOTAL_DIAS):
            dia = i + 1
            if st.session_state.treinos_10[i]:
                st.markdown(f"✅ Treino Dia {dia}")
            elif dia == proximo:
                if st.button(f"🚀 Iniciar Treino Dia {dia}"):
                    st.session_state.dia_atual = dia
                    st.session_state.origem = "todo_treino_10.py"
                    st.switch_page("pages/treino_dia.py")
            else:
                st.markdown(f"🔒 Treino Dia {dia}")

        st.progress(sum(st.session_state.treinos_10) / TOTAL_DIAS)

    elif dados["Dias de treino"] == "15":

        TOTAL_DIAS = 15
        st.set_page_config(page_title="Treino 15 Dias")
        st.title(f"🏃 Plano de Treino - {TOTAL_DIAS} Dias")

        if "treinos_15" not in st.session_state or len(st.session_state.treinos_15) != TOTAL_DIAS:
            st.session_state.treinos_15 = [False] * TOTAL_DIAS

        proximo = None
        for i, feito in enumerate(st.session_state.treinos_15):
            if not feito:
                proximo = i + 1
                break

        st.subheader("📋 Lista de Treinos")
        for i in range(TOTAL_DIAS):
            dia = i + 1
            if st.session_state.treinos_15[i]:
                st.markdown(f"✅ Treino Dia {dia}")
            elif dia == proximo:
                if st.button(f"🚀 Iniciar Treino Dia {dia}"):
                    st.session_state.dia_atual = dia
                    st.session_state.origem = "todo_treino_15.py"
                    st.switch_page("pages/treino_dia.py")
            else:
                st.markdown(f"🔒 Treino Dia {dia}")

        st.progress(sum(st.session_state.treinos_15) / TOTAL_DIAS)

    elif dados["Dias de Treino"] == "20":
        TOTAL_DIAS = 20
        st.set_page_config(page_title="Treino 20 Dias")
        st.title(f"🏃 Plano de Treino - {TOTAL_DIAS} Dias")

        if "treinos_20" not in st.session_state or len(st.session_state.treinos_20) != TOTAL_DIAS:
            st.session_state.treinos_20 = [False] * TOTAL_DIAS

        proximo = None
        for i, feito in enumerate(st.session_state.treinos_20):
            if not feito:
                proximo = i + 1
                break

        st.subheader("📋 Lista de Treinos")
        for i in range(TOTAL_DIAS):
            dia = i + 1
            if st.session_state.treinos_20[i]:
                st.markdown(f"✅ Treino Dia {dia}")
            elif dia == proximo:
                if st.button(f"🚀 Iniciar Treino Dia {dia}"):
                    st.session_state.dia_atual = dia
                    st.session_state.origem = "todo_treino_20.py"
                    st.switch_page("pages/treino_dia.py")
            else:
                st.markdown(f"🔒 Treino Dia {dia}")

        st.progress(sum(st.session_state.treinos_20) / TOTAL_DIAS)

    elif dados["Dias de Treino"] == "25":
        TOTAL_DIAS = 25
        st.set_page_config(page_title="Treino 25 Dias")
        st.title(f"🏃 Plano de Treino - {TOTAL_DIAS} Dias")

        if "treinos_25" not in st.session_state or len(st.session_state.treinos_25) != TOTAL_DIAS:
            st.session_state.treinos_25 = [False] * TOTAL_DIAS

        proximo = None
        for i, feito in enumerate(st.session_state.treinos_25):
            if not feito:
                proximo = i + 1
                break

        st.subheader("📋 Lista de Treinos")
        for i in range(TOTAL_DIAS):
            dia = i + 1
            if st.session_state.treinos_25[i]:
                st.markdown(f"✅ Treino Dia {dia}")
            elif dia == proximo:
                if st.button(f"🚀 Iniciar Treino Dia {dia}"):
                    st.session_state.dia_atual = dia
                    st.session_state.origem = "todo_treino_25.py"
                    st.switch_page("pages/treino_dia.py")
            else:
                st.markdown(f"🔒 Treino Dia {dia}")

        st.progress(sum(st.session_state.treinos_25) / TOTAL_DIAS)

    elif dados["Dias de treino"] == "30":
        TOTAL_DIAS = 30
        st.set_page_config(page_title="Treino 30 Dias")
        st.title(f"🏃 Plano de Treino - {TOTAL_DIAS} Dias")

        if "treinos_30" not in st.session_state or len(st.session_state.treinos_30) != TOTAL_DIAS:
            st.session_state.treinos_30 = [False] * TOTAL_DIAS

        proximo = None
        for i, feito in enumerate(st.session_state.treinos_30):
            if not feito:
                proximo = i + 1
                break

        st.subheader("📋 Lista de Treinos")
        for i in range(TOTAL_DIAS):
            dia = i + 1
            if st.session_state.treinos_30[i]:
                st.markdown(f"✅ Treino Dia {dia}")
            elif dia == proximo:
                if st.button(f"🚀 Iniciar Treino Dia {dia}"):
                    st.session_state.dia_atual = dia
                    st.session_state.origem = "todo_treino_30.py"
                    st.switch_page("pages/treino_dia.py")
            else:
                st.markdown(f"🔒 Treino Dia {dia}")

        st.progress(sum(st.session_state.treinos_30) / TOTAL_DIAS)


if st.button("Recomendação Inteligente"):
    st.info("Gerando plano personalizado com IA...")
    plano = gerar_treino_personalizado(dados)
    caminho_pdf = gerar_pdf(plano)
    st.success("Plano gerado com sucesso!")

    with open(caminho_pdf, "rb") as file:
        st.download_button("📥 Baixar Plano de Treino", file,
                           file_name="treino_personalizado.pdf")
