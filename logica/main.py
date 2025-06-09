import numpy as np
def montar_usuario(dados):
   excluir=["Nome", "Peso (kg)", "Altura (cm)"]
   for i in excluir:
      dados.pop(i,None) 
      return dados
   
    
    
    
    
    
    
    
    
    
    
# Exemplo: excluir as chaves 'senha' e 'email' do dicionário dados, se existirem
chaves_para_excluir = ['senha', 'email']
for chave in chaves_para_excluir:
dados.pop(chave, None)
return dados