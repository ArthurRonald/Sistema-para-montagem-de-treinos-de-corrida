import openai

openai.api_key = "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"

def gerar_treino_personalizado(dados_usuario):
    prompt = f"""
    Gere um plano de corrida para o seguinte perfil:

    - Nível: {dados_usuario['nivel']}
    - Objetivo: {dados_usuario['objetivo']}
    - Distância desejada: {dados_usuario['distancia']} km
    - Dias por semana: {dados_usuario['dias_por_semana']}
    - Minutos por dia: {dados_usuario['minutos_por_dia']}
    - Histórico de lesão: {dados_usuario['lesao']}
    - Prazo total: {dados_usuario['dias_total']} dias

    Divida o plano por dia, com sugestões práticas e realistas. Evite exercícios que exigem academia.
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um treinador especialista em corrida."},
            {"role": "user", "content": prompt}
        ]
    )

    plano = resposta["choices"][0]["message"]["content"]
    return plano
