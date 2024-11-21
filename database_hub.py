
import mysql.connector
import prettytable
from disiciplina import disiciplina 
from professor import professor
from disciplinaxprofessores import disciplinaxprofessores




try:


    
    resp = input(" Deseja manipular qual tabela?? [D] - Disicplina    [P] - Professor    [DP] -   Disiciplina x Professor: ")
    while resp != 'D' and resp != 'P' and resp != 'DP':
        
            resp =input("RESPOSTA INVÁLIDA !!! Deseja manipular qual tabela?? [D] - Disicplina    [P] - Professor    [DP] -   Disiciplina x Professor: ")
        
    if resp == 'D':
        disiciplina()
        
    elif resp == 'P':
            professor()
        
    elif resp == 'DP':
            disciplinaxprofessores()

except Exception as erro:
    print(f'Erro: {erro}')
        
    
        
        
