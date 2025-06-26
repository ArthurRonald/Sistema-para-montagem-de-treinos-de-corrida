
import streamlit as st
import google.generativeai as genai

CHAVE_API= "AIzaSyBUb0tOQMD1mrcAu5DCtaAMEU_zer7nxwE"
genai.configure(api_key= CHAVE_API)

modelo_da_ia= genai.GenerativeModel('gemini-2.5-flash')


titulo_pagina= st.title("Parabéns por ter completado o seu desafio! 🥳")
mensagem_agradecimento = st.markdown(""" Estamos agradecidos por ter usado a nossa plataforma! Esperamos que tenha gostado do seu plano de corrida personalizado. """)

#logica para tudo aparecer na sua ordem sem sumir
#inicializa variaveis de controle
if 'quer_avaliar' not in st.session_state:
    st.session_state.quer_avaliar = False #comeca sem ter clicado no botao
if 'avaliacao_estrelas' not in st.session_state:
    st.session_state.avaliacao_estrelas = 0 #comeca sem avaliacao
if 'mostrar_feedback' not in st.session_state:
    st.session_state.mostrar_feedback = False #comeca sem mostrar feedback
if 'feedback_digitado' not in st.session_state:
    st.session_state.feedback_digitado = "" #comeca sem nada no feedback
if 'resposta_ia' not in st.session_state:
    st.session_state.resposta_ia = None #comeca sem nada na resposta da ia



st.markdown(""" Gostaria de avaliar seu plano, nossa plataforma ou dar alguma sugestão? """)

if st.button( "Sim!"):
    st.session_state.quer_avaliar = True #diz que quer avaliar
    st.session_state.mostrar_feedback = False #as outras continua sem...
    st.session_state.feedback_digitado = ""
    st.session_state.resposta_ia = None 

if st.session_state.quer_avaliar: #se quer avaliar
    st.session_state.avaliacao_estrelas = st.slider(" Avalie nosso serviço de 1 a 5 estrelas! ⭐ ", min_value= 1, max_value= 5, step= 1, value = st.session_state.avaliacao_estrelas, 
                  help= "Arrastar para selecionar o número de estrelas! ⭐ " ) #salva na memoria as estrelas
    if st.session_state.avaliacao_estrelas:
        st.write(f"Você avaliou o nosso serviço com {st.session_state.avaliacao_estrelas} estrelas ⭐. Obrigado!") #diz quantas estrelas
            
            
        st.markdown("Agradecemos por ter avaliado nosso serviço. Gostaria de escrever um feedback ou sugestão?")
        if st.button("Quero!"):
            st.session_state.mostrar_feedback = True # Ativa a exibição do campo de feedback
            st.session_state.resposta_ia = "" #ia ainda nao respondeu
            
        if st.session_state.mostrar_feedback: #se tiver apertado o botao aparece a caixa de texto
            st.session_state.feedback_digitado = st.text_area("Feedback: ",value=st.session_state.feedback_digitado,
            placeholder="Digite seu texto aqui:", height = 100)
            
            if st.button("Enviar feedback", key= "submit_feedback"): 
                texto = st.session_state.feedback_digitado.strip #salva o feedback como texto e tira os espacos
                if texto:
                    if not st.session_state.resposta_ia: #se nao tiver ainda a ia respondido
                        prompt = (f""" Por favor, analise o sentimento desse usuário. Seja um encarregado de responder feedbacks de usuários de uma plataforma de treinos de corrida personalizados, com base nessa avaliação {st.session_state.feedback_digitado}, e agradeça a opinião. Não
                      use emojis nem asteriscos, nem dê negrito em nenhuma palavra. NAO DIGA APENAS OBRIGADO. RECAPITULE O QUE A PESSOA FALOU E DE SUA OPINIAO SOBRE.""")
                    
                    try:
                    
                        response = modelo_da_ia.generate_content(prompt) #pede pra ia gerar o conteudo
                        st.session_state.resposta_ia = response.text #salva a resposta da ia
                        
                        
                    except Exception as e:
                        
                        st.session_state.resposta_ia = f"Ocorreu um erro ao processar seu feedback. Por favor, tente novamente. Erro: {e}"
                else:
                    st.session_state.resposta_ia = "Por favor, digite seu feedback antes de enviar."
        if st.session_state.resposta_ia:
            st.markdown("---")
            st.markdown(st.session_state.resposta_ia)

            if "erro" not in st.session_state.resposta_ia.lower(): #se tudo da certo, aparece isso tbm
                st.success("Obrigado pelo feedback!")
        
        

    



