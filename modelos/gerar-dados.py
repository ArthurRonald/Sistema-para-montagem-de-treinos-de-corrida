import pandas as pd
import numpy as np

np.random.seed(69)
qtd_usuarios=5000

dados= {
    "Usuário": np.range(1,qtd_usuarios+1),
    "Objetivo de treino": np.random.choice(["Emagrecimento", "Resistência","Maratona","Bem-estar"],qtd_usuarios),
    "Tempo (min)": np.random.randit(20,181, qtd_usuarios),
    "Histórico de lesão": np.random.choice(["Sim","Não"], qtd_usuarios, p=[0.2,0.8]),.
    "Peso (kg)": np.round(np.random.uniform(50,100,qtd_usuarios),1),
    "Altura (m)": np.round(np.random.uniform(1.50,2.0, qtd_usuarios),2),
    "Atividades/semana": np.random.randit(1,8,qtd_usuarios),







}