from prettytable import PrettyTable
import mysql.connector

def disiciplina():

   
    
    def abrebanco():
        try:
        
            global conexao
            conexao = mysql.connector.Connect(host='localhost',database='univap',
            user='root', password='')
                # testando se estamos conectado ao banco de dados
            if conexao.is_connected():
                informacaobanco = conexao.get_server_info()
                print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
                print('Conexão ok')
                # criando objeto cursor, responsável para trabalharmos com registros retornados pela tabela fisica
                
                global comandosql
                comandosql = conexao.cursor()
                # Criando uma QUERY para mostrar as informações do banco de dados ao qual nos conectamos
                
                comandosql.execute('select database();')
                # usando método fetchone para buscar um dado do banco de dados e armazenálo na variável nomebanco
                
                nomebanco = comandosql.fetchone()
                print(f'Banco de dados acessado = {nomebanco}')
                print('='*80)
                return 1
            else:
                print('Conexão não realizada com banco')
            return 0
        except Exception as erro:
            
            print(f'ERRO NÃO FOI POSSÍVEL REALIZAR')
            return 0 


    def mostratodas():
        # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
        grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
        try:
            comandosql = conexao.cursor()
            comandosql.execute(f'select * from disciplinas;')
            # O MÉTODO fetchall() retornará todos os registros filtrados (um ou mais registros) pelo comando select)
    
            tabela = comandosql.fetchall()
        
            if comandosql.rowcount > 0:

                for registro in tabela:
            
                    grid.add_row([registro[0], registro[1]])
                print(grid)
            else:
                print('Não existem disciplinas cadastradas!!!')
        except Exception as erro:
            
            print(f'ERRO NÃO FOI POSSÍVEL REALIZAR')


    def consultardisciplina(codigodisc=0):
        
            comandosql = conexao.cursor()
            comandosql.execute(f'select * from disciplinas where codigodisc = {codigodisc};')
                
            tabelaeconsulta = comandosql.fetchall()
            for registro in tabelaeconsulta:
                grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
                grid.add_row([registro[0], registro[1]])
            print(grid)
            conexao.commit()
        
        



    def cadastrardisciplina(cd=0,nd=''):
        try:
            comandosql = conexao.cursor()
            #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd

            comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc)values({cd},"{nd}") ;')
            #método commit é responsável por gravar de fato o novo registro de disciplina na tabela

            conexao.commit()
            return 'Cadastro da disciplina realizado com sucesso !!!! '
        except Exception as erro :
            
            
            return 'Não foi possível cadastrar esta disciplina !!!'







    def alterardisciplina(cd=0, nomedisciplina=''):
        try:
            comandosql = conexao.cursor()
            # Creating an update command to update the name of the discipline
            comandosql.execute(f'UPDATE disciplinas SET nomedisc="{nomedisciplina}" WHERE codigodisc = {cd};')
            # The commit method actually saves the updated discipline name in the table
            conexao.commit()
            return 'Disciplina alterada com sucesso !!!'
        except Exception as erro:
            
            return 'Não foi possível alterar esta disciplina'
        

    

    
    def excluirdisciplina(cd=0):
        try:
            comandosql = conexao.cursor()
            #criando comando delete e concatenando o código da disciplina para ser escluída
            comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')
            #método commit é responsável por gravar de fato o novo registro de disciplina na  tabela
        
            conexao.commit()
            return 'Disciplina excluída com sucesso !!! '
        except Exception as erro :
            
            
            return 'Não foi possível excluir esta disciplina' 

    #'''
    #========================================= MÓDULO PRINCIPAL DO PROGRAMA
    #===============================================
    #'''

    if abrebanco() == 1:
        resp = input('Deseja entrar no módulo de Disciplinas? (1-Sim, ou qualquer tecla para sair) ==> ')

        while resp =='1':
            print('='*80)
            print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
            print('='*80)
            

            while True:
                codigodisc = input('( 0- Mostra Todas Tabelas ) ou ( Digite qualquer numero para prosseguir ) ')
                while codigodisc.isnumeric() == False:
                    codigodisc = input("Deve ser digitado obrigatoriamente um numero!! Digite novamente:")
                if codigodisc.isnumeric():
                        codigodisc = int(codigodisc)
                break
            if codigodisc == 0:
                mostratodas()
    #o comando continue volta a executar o laço de repetição do início do laço de repetição
                continue
    #chamando função para consultardisciplina, se retornar 'nc' não está cadastrada
            
            else:

                op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")
                while op!='I' and op!= 'C' and op!='U' and op!='E' and op!='CO':
                    op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")




                    
                if op=='I':
                    
                    codigodisc = input ("Informe o código da nova disciplina: ")
                    while int(codigodisc.isnumeric()) == False  or int(codigodisc) <= 0:
                        codigodisc = input("O código deve ser um numero!! Digite novamente:")
                

                    nomedisciplina = input('Informe o nome da nova disciplina: ')
                    while nomedisciplina.isnumeric() == True: 
                        nomedisciplina = input("O nome da disciplina deve conter apenas caracteres!! Digite novamente:")  
                    codigodisc = int(codigodisc)
                    msg = cadastrardisciplina(codigodisc, nomedisciplina)
                    print(msg)





                elif op == 'C':
                    
                        codigodisc = input ("Informe o código que deseja consultar (0 - mostra todas) : ")
                        while codigodisc.isnumeric() == False or int(codigodisc) < 0:
                            codigodisc = input("O código deve ser um numero!! Digite novamente:")
                        if codigodisc.isnumeric():
                            codigodisc = int(codigodisc)

                        if codigodisc == 0:
                            mostratodas()

                        else:
                            
                            msg = consultardisciplina(codigodisc)
                            
                        

                






                elif op=='U':

                    print('Atenção: Código da disciplina não pode ser alterado: ')
                    codigodisc = input(" Qual o código referente a disiciplina? ")
                    while codigodisc.isnumeric() == False or int(codigodisc) <= 0 :
                        codigodisc = input("O código deve ser um numero!! Digite novamente:")

                    comandosql = conexao.cursor()
                    comandosql.execute(f'select * from disciplinas where codigodisc = {codigodisc};')
                    tabelaatualizar = comandosql.fetchall()

                    for registro in tabelaatualizar:
                        grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
                        grid.add_row([registro[0], registro[1]])
                    print(grid)

                    conexao.commit()
                    
                    nomedisciplina = input(f"Informe o novo nome para disciplina do código {codigodisc}: ")
                    while nomedisciplina.isnumeric() == True: 
                        nomedisciplina = input("O nome da disciplina deve conter apenas caracteres!! Digite novamente:")
                    
                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA A atualização? S-SIM OU N-NÃO: ')
                
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                    
                    msg = alterardisciplina(codigodisc, nomedisciplina)
                    

                

                elif op == 'E':
                    codigodisc = input(" Qual o código da displina que deseja excluir? ")
                    while codigodisc.isnumeric() == False or int(codigodisc )<= 0:
                        codigodisc = input("O código deve ser um numero!! Digite novamente:")
                    comandosql = conexao.cursor()
            #criando comando delete e concatenando o código da disciplina para ser escluída
                    comandosql.execute(f'select * from disciplinas where codigodisc = {codigodisc};')
            #método commit é responsável por gravar de fato o novo registro de disciplina na  tabela
                    tabelaexluir = comandosql.fetchall()
                    for registro in tabelaexluir:
                        grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
                        grid.add_row([registro[0], registro[1]])
                    print(grid)
                    conexao.commit()
                    
                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                        msg = excluirdisciplina(codigodisc)
                        print (msg)



                print('\n\n')
                print('='*80)
                if input('Deseja continuar usando o programa? 1- Sim OU qualquer tecla para sair:') == '1':

                    continue
                else:

                    break
                    comandosql.close()
                    conexao.close()
        else:
            print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.') 



