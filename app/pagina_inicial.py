import streamlit as st

col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
with col3:
    st.title("MZRun")

st.markdown(""" Este site foi criado para ajudar pessoas que desejam melhorar sua rotina de treinos de corrida. A partir de algumas informações simples, ele oferece sugestões personalizadas para tornar seus treinos mais organizados e eficientes. A proposta é tornar o processo de planejar, acompanhar e ajustar seus treinos algo prático, acessível e pensado para o seu ritmo. """)

st.subheader("O que você encontra aqui: ")
st.markdown("""
            
**-Um sistema simples e interativo:** Você só precisa preencher um formulário com algumas informações básicas.

**-Sugestões de treinos personalizadas:** Com base no que você responder, o sistema oferece um plano de corrida adaptado ao seu perfil.

**-Sem necessidade de baixar nada:** Tudo acontece na própria página, de forma prática e leve.

**-Sugestão com o feedback de seu treino:** Depois de seguir os treinos, você pode contar como foi e receber um novo plano ajustado conforme o seu progresso ou suas dificuldades.

**-Organização em lista de seu treino:** O sistema também exibe os treinos da semana de forma simples, como uma lista que você pode acompanhar dia a dia.

**-PDF com seu plano:** Se quiser, você pode salvar ou imprimir seu plano para acompanhar quando estiver offline. """)

st.subheader("Vamos Começar❔🏃‍♂️")

if st.button("Criar seu Treino"):
    st.switch_page("pagina_questionario.py")
