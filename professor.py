from prettytable import PrettyTable
import mysql.connector

def professor():

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
        grid = PrettyTable(['Registro', "Nomes dos Professores", "Telefone dos Professores", "Idade","Salário"])
        try:
            comandosql = conexao.cursor()
            comandosql.execute(f'select * from professores')
            
            tabela = comandosql.fetchall()
        
        
            if comandosql.rowcount > 0:

                for registro in tabela:
                    
                    grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
            
                print(grid)
            else:

                print('Não existem informações sobre professores cadastradas!!!')
        except Exception as erro:
            print(f'ERRO NÃO FOI POSSÍVEL REALIZAR')

    def consultarprofessor(cdprof = 0):
        try:
            comandosql = conexao.cursor()
        
            comandosql.execute(f'select * from professores where registro = {cdprof};')
            
            tabelaatualizar = comandosql.fetchall()
            for registro in tabelaatualizar:
                grid = PrettyTable(['Registro', "Nomes dos Professores", "Telefone dos Professores", "Idade","Salário"])
                grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
                print(grid)
            conexao.commit()


        except Exception as erro :
            print(f'ERRO NÃO FOI POSSÍVEL REALIZAR')
            return 'Não foi possível consultar este professor !!!'



        
    def cadastrarprofessor(cdprofessor=0,nomeprofessor='',telprof = '' , idade = 0, salario = 0):
        try:
            comandosql = conexao.cursor()
            #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd

            comandosql.execute(f'insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values({cdprofessor}, "{nomeprofessor}", "{telprof}", {idade}, {salario});')

            #método commit é responsável por gravar de fato o novo registro de disciplina na tabela

            conexao.commit()
            return 'Cadastro de professor realizado com sucesso !!!! '
        
        

        
        
        except Exception as erro :
            
            
            return 'Não foi possível cadastrar este professor !!!'
        
        
        



    def alterarprofessor(cdprofessor = 0, nomeprofessor = '',telprof = '',idade = 0,salario = 0):
        try:
            comandosql = conexao.cursor()
            # Creating an update command to update the name of the discipline
            comandosql.execute(f'UPDATE professores SET nomeprof="{nomeprofessor}", telefoneprof={telprof}, idadeprof={idade}, salarioprof={salario} WHERE registro={cdprofessor};')

            # The commit method actually saves the updated discipline name in the table
            conexao.commit()
            return 'Professor alterado com sucesso !!!'
        except Exception as erro:
           
            return 'Não foi possível alterar este professor'
    

    

    def excluirprofessor(cdprofessor=0):
        try:
            comandosql = conexao.cursor()
            #criando comando delete e concatenando o código da disciplina para ser escluída
            comandosql.execute(f'delete from professores where registro = {cdprofessor};')
            #método commit é responsável por gravar de fato o novo registro de disciplina na  tabela
        
            conexao.commit()
            return 'Professor excluído com sucesso !!! '
        except Exception as erro :
            
            return 'Não foi possível excluir este Professor' 



        
    #'''
    #========================================= MÓDULO PRINCIPAL DO PROGRAMA
    #===============================================
    #'''

    if abrebanco() == 1:
        resp = input('Deseja entrar no módulo de Professores? (1-Sim, ou qualquer tecla para sair) ==> ')

        while resp =='1':
            print('='*80)
            print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
            print('='*80)


            while True:
                cdprof = input('( 0- Mostra Todas Tabelas ) ou ( Digite qualquer numero para prosseguir ) ')
                while cdprof.isnumeric() == False:
                    cdprof = input("Deve ser digitado obrigatoriamente um numero!! Digite novamente:")
                if cdprof.isnumeric():
                        cdprof = int(cdprof)
                break
            if cdprof == 0:
                mostratodas()
        

                continue



            else:
                op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")
                while op!='I' and op!= 'C' and op!='U' and op!='E' and op!='CO':
                    op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")
                



                if op=='I':
                    cdprof = input ("Informe o novo código de registro do professor: ")
                    while cdprof.isnumeric() == False or int(cdprof) <= 0 :
                        cdprof = input("O código de registro informado deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")

                    nomeprofessor = input('Informe o nome do professor: ')
                    while nomeprofessor.isnumeric() == True:
                           
                        nomeprofessor = input("O nome do professor deve conter apenas caracteres!! Digite novamente:")

                    telprof = input ("Informe o telefone do professor: ")
                    while telprof.isnumeric() == False or int(telprof) <= 0 or len(telprof) != 11:
                        telprof = input("O telefone informado deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")
                    



                    idade = input("Informe a idade do professor: ")
                    while idade.isnumeric() == False or int(idade) <= 0 or int(idade) >= 105:
                        idade = input("Idade Inválida !! Digite novamente:")
                        
                        
                        #is numeric=
                    salario = input ("Informe o salário do professor: ")
                    while float(salario) < 0:
                        salario = input("Salário Inválido !!! Digite novamente:")
                    msg = cadastrarprofessor(cdprof, nomeprofessor,telprof,idade,salario)
                    print(msg)




                
                elif op == 'C':
                        cdprof = input ("Informe o código de registro que deseja consultar: ")
                        while cdprof.isnumeric() == False or int(cdprof) < 0:
                            cdprof = input("O código de registro deve ser um numero!! Digite novamente: ")
                            

            
                        if cdprof.isnumeric():
                            cdprof = int(cdprof)
                        

                        if cdprof == 0:
                            mostratodas()
                        else:
                            msg = consultarprofessor(cdprof)
                            
                            


                








                elif op=='U':
                    print('Atenção: Código de Registro não pode ser alterado: ')
                    cdprof = input(" Qual o código de registro referente ao professor? ")
                    while int(cdprof.isnumeric()) == False or int(cdprof) <= 0:
                        cdprof = input("O código de registro deve ser um numero!! Digite novamente:")


                        
                    comandosql = conexao.cursor()
            #criando comando delete e concatenando o código da disciplina para ser escluída
                    comandosql.execute(f'select * from professores where registro = {cdprof};')
            #método commit é responsável por gravar de fato o novo registro de disciplina na  tabela
                    tabelaatualizar = comandosql.fetchall()
                    for registro in tabelaatualizar:
                        grid = PrettyTable(['Registro', "Nomes dos Professores", "Telefone dos Professores", "Idade","Salário"])
                        grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
                    print(grid)
                    conexao.commit()


                    
                    
                    nomeprofessor = input('Informe novo nome do professor: ')
                    while nomeprofessor.isnumeric() == True:
                        nomeprofessor = input("O nome do professor deve conter apenas caracteres!! Digite novamente:")

                    telprof = input ("Informe o telefone do professor")
                    while telprof.isnumeric() == False or int(telprof) <= 0 or len(telprof) != 11 :
                        telprof = input("Telefone Inválido !! Digite novamente:")


                    idade = input("Informe a idade do professor")
                    while int(idade.isnumeric()) == False or int(idade) <= 0 or int(idade) > 105:
                        idade = input("Idade Inválida!! Digite novamente:")
                        
                        
                        
                    salario = input ("Informe o salário do professor:")
                    while float(salario) <= 0:
                        salario = input("Salário Inválido!! Digite novamente:")
                    

                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA A atualização? S-SIM OU N-NÃO: ')
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')

                    msg = alterarprofessor(cdprof, nomeprofessor,telprof,idade,salario)
                    print(msg)

                




                elif op == 'E':
                    cdprof = input(" Qual o código de registro que pertence ao professor que deseja excluir? ")
                    while int(cdprof.isnumeric()) == False or int(cdprof) <= 0:
                        cdprof = input("Código inválido!! Digite novamente:")
                
                    
                    comandosql = conexao.cursor()
            #criando comando delete e concatenando o código da disciplina para ser escluída
                    comandosql.execute(f'select * from professores where registro = {cdprof};')
            #método commit é responsável por gravar de fato o novo registro de disciplina na  tabela
                    tabelaexluir = comandosql.fetchall()
                    for registro in tabelaexluir:
                        grid = PrettyTable(['Registro', "Nomes dos Professores", "Telefone dos Professores", "Idade","Salário"])
                        grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
                    print(grid)
                    conexao.commit()
                    
                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                    msg = excluirprofessor(cdprof)
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

