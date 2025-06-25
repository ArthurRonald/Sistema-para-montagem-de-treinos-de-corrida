import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="MZRunning",
    page_icon="🏃‍♂️",
    layout="centered"
)


try:
    logo = Image.open("Movement Zone Running.png")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(logo, width=280)  #centralizando essa mizera
        st.markdown("---")  
    
    st.title("MZRunning", anchor=False)
    st.caption("Seu assistente pessoal para treinos de corrida")  

   
    st.markdown("""
    Este site foi criado para ajudar pessoas que desejam melhorar sua rotina de treinos de corrida. 
    A partir de algumas informações simples, oferecemos sugestões personalizadas para tornar seus 
    treinos mais organizados e eficientes.
    """)

    
    st.subheader("O que você encontra aqui:", anchor=False)
    st.markdown("""
    ✨ **Sistema interativo** - Formulário simples e intuitivo  
    🎯 **Treinos personalizados** - Adaptados ao seu perfil  
    📱 **Acesso direto** - Sem necessidade de downloads  
    🔄 **Ajustes progressivos** - Feedbacks para evolução contínua  
    📅 **Organização semanal** - Lista de treinos dia a dia  
    📄 **Exportação para PDF** - Salve ou imprima seu plano  
    🧠 **IA especializada** - Nossa inteligência artificial exclusiva  
    🤖 **Tecnologia Gemini** - Precisão avançada em recomendações
    """)

    st.markdown("---")
    st.subheader("Pronto para começar? ❔🏃‍♂️", anchor=False)
    if st.button("👉 CRIAR MEU TREINO AGORA", type="primary", use_container_width=True):
        st.switch_page("pagina_questionario.py")

except FileNotFoundError:
    st.error("Arquivo de logo não encontrado. Verifique o caminho: 'Movement Zone Running.png'")
    st.title("MZRunning")  
