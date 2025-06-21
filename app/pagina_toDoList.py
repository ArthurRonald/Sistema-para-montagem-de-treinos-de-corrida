# import streamlit as st
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# st.title("Confira o treino ideal para o nível da atividade desejada")

# previsao = st.session_state.get("previsao")
# historico_lesao = st.session_state.get(
#     "dados_usuario", {}).get("lesao_encoded")

# if previsao == 0:
#     previsao = "Avançado"
# elif previsao == 1:
#     previsao = "Iniciante"
# else:
#     previsao = "Intermediário"

# if previsao is None or historico_lesao is None:
#     st.error(
#         "❌ Dados do usuário não encontrados. Por favor, preencha o questionário primeiro.")
# else:
#     st.subheader(
#         f"O nível adequado para sua atividade é {str(previsao).upper()}")

#     if previsao == "Avançado" and historico_lesao == "Não":
#         treino = pd.read_csv("AVANÇADO SEM LESÃO.csv")
#         st.write(treino)
#     elif previsao == "Avançado" and historico_lesao == "Sim":
#         treino = pd.read_csv("AVANÇADO COM LESÃO.csv")
#         st.write(treino)

#     elif previsao == "Intermediario" and historico_lesao == "Não":
#         treino = pd.read_csv("INTERMEDIÁRIO SEM LESÃO.csv")
#         st.write(treino)

#     elif previsao == "Intermediario" and historico_lesao == "Sim":
#         treino = pd.read_csv("INTERMEDIÁRIO COM LESÃO.csv")
#         st.write(treino)

#     elif previsao == "Iniciante" and historico_lesao == "Não":
#         treino = pd.read_csv("INICIANTE SEM LESÃO.csv")
#         st.write(treino)

#     elif previsao == "Iniciante" and historico_lesao == "Sim":
#         treino = pd.read_csv("INICIANTE COM LESÃO.csv")
#         st.write(treino)

# st.button("Recomendação Inteligente")

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.title("Confira o treino ideal para o nível da atividade desejada")

# Obter dados da sessão
previsao = st.session_state.get("previsao")
historico_lesao = st.session_state.get(
    "dados_usuario", {}).get("lesao_encoded")

# Mapear previsão para texto
if previsao == 0:
    previsao = "Avançado"
elif previsao == 1:
    previsao = "Iniciante"
else:
    previsao = "Intermediário"

if previsao is None or historico_lesao is None:
    st.error(
        "❌ Dados do usuário não encontrados. Por favor, preencha o questionário primeiro.")
else:
    st.subheader(
        f"O nível adequado para sua atividade é {str(previsao).upper()}")

    # Definir o nome do arquivo baseado nas condições
    arquivo = None

    if previsao == "Avançado" and historico_lesao == "Não":
        arquivo = "AVANÇADO SEM LESÃO.csv"
    elif previsao == "Avançado" and historico_lesao == "Sim":
        arquivo = "AVANÇADO COM LESÃO.csv"
    elif previsao == "Intermediário" and historico_lesao == "Não":
        arquivo = "INTERMEDIÁRIO SEM LESÃO.csv"
    elif previsao == "Intermediário" and historico_lesao == "Sim":
        arquivo = "INTERMEDIÁRIO COM LESÃO.csv"
    elif previsao == "Iniciante" and historico_lesao == "Não":
        arquivo = "INICIANTE SEM LESÃO.csv"
    elif previsao == "Iniciante" and historico_lesao == "Sim":
        arquivo = "INICIANTE COM LESÃO.csv"

    if arquivo:
        try:
            # Carregar o DataFrame
            treino = pd.read_csv(arquivo)

            # Exibir o DataFrame de forma mais bonita
            st.write("### Plano de Treino Recomendado")
            # Ou use st.table(treino) para uma tabela estática
            st.dataframe(treino, hide_index=True)

            # Opcional: Mostrar como expandir para ver todos os dados
            st.info("🔍 Role para ver todos os exercícios recomendados.")

        except FileNotFoundError:
            st.error(
                f"Arquivo {arquivo} não encontrado. Verifique o caminho do arquivo.")
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
    else:
        st.warning("Combinação de nível e histórico de lesão não reconhecida.")

    st.button("Recomendação Inteligente")
