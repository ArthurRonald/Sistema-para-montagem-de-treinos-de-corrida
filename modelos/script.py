import pandas as pd
import numpy as np

# Configurações
np.random.seed(42)
n_usuarios = 5000

# Gerar dados
dados = {
    "Usuário": np.arange(1, n_usuarios + 1),
    "Objetivo do treino": np.random.choice(["Maratona", "Bem-estar", "Emagrecimento"], n_usuarios),
    "Tempo (min)": np.random.randint(20, 181, n_usuarios),
    "Histórico de lesão": np.random.choice(["Sim", "Não"], n_usuarios, p=[0.2, 0.8]),
    "Peso (kg)": np.round(np.random.uniform(50, 100, n_usuarios), 1),
    "Altura (cm)": np.round(np.random.uniform(150, 200, n_usuarios), 0),
    "Atividades/semana": np.random.randint(1, 8, n_usuarios),
}

# Calcular o nível do atleta com base em pesos
def calcular_nivel(row):
    objetivo = row['Objetivo do treino']
    tempo = row['Tempo (min)']
    distancia = row['Distância (km)']
    
    # Pesos
    peso_objetivo = 0.4
    peso_tempo = 0.3
    peso_distancia = 0.3
    
    # Classificação inicial
    score = 0
    
    # Atribuir pontuação com base no objetivo
    if objetivo == "Maratona":
        score += 3 * peso_objetivo
    elif objetivo == "Bem-estar":
        score += 1 * peso_objetivo
    elif objetivo == "Emagrecimento":
        score += 2 * peso_objetivo
    
    # Atribuir pontuação com base no tempo
    if tempo >= 120:
        score += 3 * peso_tempo
    elif tempo >= 60:
        score += 2 * peso_tempo
    else:
        score += 1 * peso_tempo
    
    # Atribuir pontuação com base na distância
    if distancia >= 15:
        score += 3 * peso_distancia
    elif distancia >= 5:
        score += 2 * peso_distancia
    else:
        score += 1 * peso_distancia
    
    # Classificação final
    if score >= 2.5:
        return "Avançado"
    elif score >= 1.5:
        return "Intermediário"
    else:
        return "Iniciante"

# Criar DataFrame
df = pd.DataFrame(dados)

# Calcular Distância e Pace
df["Pace (min/km)"] = np.round(np.random.uniform(4.5, 9.5, n_usuarios), 2)
df["Distância (km)"] = np.round(df["Tempo (min)"] / df["Pace (min/km)"], 1)

# Calcular o nível do atleta
df["Nível"] = df.apply(calcular_nivel, axis=1)

# Reordenar colunas
df = df[["Usuário", "Objetivo do treino", "Tempo (min)", "Distância (km)", 
         "Histórico de lesão", "Pace (min/km)", "Peso (kg)", "Altura (cm)", 
         "Atividades/semana", "Nível"]]

# Salvar CSV
df.to_csv("corredores_ficticios.csv", index=False)

