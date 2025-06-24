
import streamlit as st
import google.generativeai as genai

CHAVE_API= "AIzaSyBUb0tOQMD1mrcAu5DCtaAMEU_zer7nxwE"
genai.configure(api_key= CHAVE_API)

modelo_da_ia= genai.GenerativeModel('gemini-2.5-flash')


titulo_pagina= st.title("Parabéns por ter completado o seu desafio! 🥳")
mensagem_agradecimento = st.markdown(""" Estamos agradecidos por ter usado a nossa plataforma! Esperamos que tenha gostado do seu plano de corrida personalizado. """)

if 'quer_avaliar' not in st.session_state:
    st.session_state.quer_avaliar = False
if 'mostrar_feedback' not in st.session_state:
    st.session_state.mostrar_feedback = False
if 'feedback_digitado' not in st.session_state:
    st.session_state.feedback_digitado = ""
if 'resposta_ia' not in st.session_state:
    st.session_state.resposta_ia = ""



st.markdown(""" Gostaria de avaliar seu plano, nossa plataforma ou dar alguma sugestão? """)

if st.button( "Sim!"):
    st.session_state.quer_avaliar = True
    st.session_state.mostrar_feedback = False
    st.session_state.feedback_digitado_valor = ""
    st.session_state.resposta_ia = "" 

if st.session_state.quer_avaliar:
    avaliacao = st.slider(" Avalie nosso serviço de 1 a 5 estrelas! ⭐ ", min_value= 1, max_value= 5, step= 1, 
                  help= "Arrastar para selecionar o número de estrelas! ⭐ " )
    if avaliacao:
        st.write(f"Você avaliou o nosso serviço com {avaliacao} estrelas ⭐. Obrigado!")
            
            
        st.markdown("Agradecemos por ter avaliado nosso serviço. Gostaria de escrever um feedback ou sugestão?")
        if st.button("Quero!"):
            st.session_state.mostrar_feedback = True # Ativa a exibição do campo de feedback
            st.session_state.resposta_ia = ""
            
        if st.session_state.mostrar_feedback:
            st.session_state.feedback_digitado = st.text_area("Feedback: ",
            placeholder="Digite seu texto aqui:", height = 100)
            
            if st.button("Enviar feedback", key= "submit_feedback"):
                if st.session_state.feedback_digitado:
                    prompt = (f""" Por favor, analise o sentimento desse usuário como se fosse uma ia de responder feedbacks de usuários, com base nessa avaliação {st.session_state.feedback_digitado}, e agradeça a opinião. Não
                      use emojis nem asteriscos, nem dê negrito em nenhuma palavra. NAO DIGA APENAS OBRIGADO. RECAPITULE O QUE A PESSOA FALOU E DE SUA OPINIAO SOBRE.""")
                    
                    try:
                    
                        response = modelo_da_ia.generate_content(prompt)
                        st.session_state.resposta_ia = response.text
                        
                        
                    except Exception as e:
                        
                        st.session_state.resposta_ia = f"Ocorreu um erro ao processar seu feedback. Por favor, tente novamente. Erro: {e}"
                else:
                    st.session_state.resposta_ia = "Por favor, digite seu feedback antes de enviar."
                if st.session_state.resposta_ia:
                
                    st.markdown(st.session_state.resposta_ia)
                
                    if "erro" not in st.session_state.resposta_ia.lower():
                        st.success("Obrigado pelo feedback!")
        
        

    



