from prettytable import PrettyTable
import mysql.connector

def disciplinaxprofessores ():


    def abrebanco():
        try:
        
            global conexao
            conexao = mysql.connector.Connect(host='localhost',database='univap',
            user='root', password='')
            
            if conexao.is_connected():
                informacaobanco = conexao.get_server_info()
                print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
                print('Conexão ok')
            
                
                global comandosql
                comandosql = conexao.cursor()
                
                
                comandosql.execute('select database();')
            
                
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
    
        grid = PrettyTable(['Codigo da Disciplina no Curso', "Curso", "Carga Horaria", "Ano letivo","Código da Disciplina","Código do Professor" ])
        try:
            comandosql = conexao.cursor()
            comandosql.execute(f'select * from disciplinasxprofessores;')
            
            tabela = comandosql.fetchall()
        
        
            if comandosql.rowcount > 0:

                for registro in tabela:
        
                    grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4], registro[5]])
            
                print(grid)
            else:
                print('Não existem informações cadastradas nessa tabela !!!')
        except Exception as erro:
            print(f'ERRO NÃO FOI POSSÍVEL REALIZAR')
            

    def consultardiscxprof(cddisciplinaprof = 0):
        try:
            comandosql = conexao.cursor()
        
            comandosql.execute(f'select * from  disciplinasxprofessores  where codigodisciplinanocurso = {cddisciplinaprof};')
            
            tabelaatualizar = comandosql.fetchall()
            for registro in tabelaatualizar:
                grid = PrettyTable(['Codigo da Disciplina no Curso', "Curso", "Carga Horaria", "Ano letivo","Código da Disciplina","Código do Professor" ])
                grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4], registro[5]])
                print(grid)
            conexao.commit()


        except Exception as erro :
            
            return 'Não foi possível consultar  !!!'



        
    def cadastrardiscxprof(cddisciplinaprof = 0, curso = ' ', cargahoraria = 0 , anoletivo = 0, codigodisciplina = 0, cdprof = 0):
        try:
            comandosql = conexao.cursor()
        

            comandosql.execute(f'insert into disciplinasxprofessores (codigodisciplinanocurso, curso , cargahoraria, anoletivo, coddisciplina,codprofessor) values({cddisciplinaprof}, "{curso}", "{cargahoraria}", {anoletivo}, {codigodisciplina}, {cdprof});')


            conexao.commit()
            return 'Cadastro realizado com sucesso !!!! '
        except Exception as erro :
            
            return 'Não foi possível realizar o cadastro !!!'
        



    def alterardiscxprof(cddisciplinaprof = 0, curso ='', cargahoraria = 0 , anoletivo = 0, codigodisciplina = 0, cdprof = 0):
        try:
            comandosql = conexao.cursor()
        
            comandosql.execute(f'UPDATE disciplinasxprofessores SET curso="{curso}", cargahoraria={cargahoraria}, anoletivo={anoletivo}, coddisciplina={codigodisciplina} , codprofessor = {cdprof} WHERE codigodisciplinanocurso = {cddisciplinaprof};')

            
            conexao.commit()

            return ' Alterado com sucesso !!!'
        
        except Exception as erro:
            
            return 'Não foi possível alterar '


    

    def excluirdiscxprof(cddisciplinaprof=0):
        try:
            comandosql = conexao.cursor()
            
            comandosql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso = {cddisciplinaprof};')
        
            conexao.commit()
            return  'Excluído com sucesso !!! '
        except Exception as erro :
            
            return 'Não foi possível excluir !!' 



    #'''
    #========================================= MÓDULO PRINCIPAL DO PROGRAMA
    #===============================================
    #'''



    if abrebanco() == 1:
        resp = input('Deseja entrar no módulo de Disciplinas x Professores? (1-Sim, ou qualquer tecla para sair) ==> ')

        while resp =='1':
            print('='*80)
            print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS E PROFESSORES'))
            print('='*80)


            while True:
                cd = input('( 0- Mostra Todas Tabelas ) ou ( Digite qualquer numero para prosseguir ) ')
                while cd.isnumeric() == False:
                    cd = input("Deve ser digitado obrigatoriamente um numero!! Digite novamente:")
                if cd.isnumeric():
                        cd = int(cd)
                break
            if cd == 0:
                mostratodas()
        

                continue



            else:
                op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")
                while op!='I' and op!= 'C' and op!='U' and op!='E' and op!='CO':
                    op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [CO]- Cancelar Operações ==> ")
                



                if op=='I':
                    cddisciprof = input ("Informe o novo código da disciplina no curso: ")
                    while cddisciprof.isnumeric() == False or int(cddisciprof) <= 0 :
                        cddisciprof = input("O código da discplina no curso informado deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")

                    curso = input("Informe o curso: ")
                    while curso.isnumeric() == True:
                        curso = input("O nome do curso deve conter apenas caracteres!! Digite novamente:")

                    cargahoraria = input ("Informe a carga horaria: ")
                    while cargahoraria.isnumeric() == False or int(cargahoraria) < 0 :
                        cargahoraria = input("A carga horaria deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")


                    anoletivo = input("Informe o ano letivo : ")
                    while anoletivo.isnumeric() == False or int(anoletivo) <= 0:
                        anoletivo = input("O ano letivo informado deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")
                        
                        
                        #is numeric
                    codigodiscplina = input ("Informe o código da disciplina: ")
                    while codigodiscplina.isnumeric() == False or int(codigodiscplina) <= 0:
                        codigodiscplina = input(" Código Inválido !! Digite novamente:")
                    

                    cdprof = input ("Informe o código do professor: ")
                    while cdprof.isnumeric() == False or int(cdprof) <= 0:
                        cdprof = input("Código Inválido!! Digite novamente:")
                    



                    msg = cadastrardiscxprof(cddisciprof, curso, cargahoraria,anoletivo,codigodiscplina, cdprof)
                    print(msg)




                
                elif op == 'C':
                        cddisciprof = input ("Informe o código da disciplina no curso que deseja consultar: ")
                        while cddisciprof.isnumeric() == False or int(cddisciprof) < 0:
                            cddisciprof = input("Código Inválido!! Digite novamente: ")

                        if cddisciprof.isnumeric():
                            cddisciprof = int(cddisciprof)
                        

                        if cddisciprof == 0:
                            mostratodas()
                        else:
                            msg = consultardiscxprof(cddisciprof)
                            
                            


                





                elif op=='U':
                    print('Atenção: Código da Disiciplina no Curso não pode ser alterado: ')
                    cddisciprof = input(" Qual o código da disciplina no curso? ")
                    while cddisciprof.isnumeric() == False or int(cddisciprof) <=0:
                        cddisciprof = input("Código Inválido !! Digite novamente:")

                    comandosql = conexao.cursor()
                    comandosql.execute(f'select * from  disciplinasxprofessores  where codigodisciplinanocurso = {cddisciprof};')
            
                    tabelaatualizar = comandosql.fetchall()
                    for registro in tabelaatualizar:
                            grid = PrettyTable(['Codigo da Disciplina no Curso', "Curso", "Carga Horaria", "Ano letivo","Código da Disciplina","Código do Professor" ])
                            grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4], registro[5]])
                    print(grid)
                    conexao.commit()



                    
                    
                    curso = input("Informe o novo curso: ")
                    while curso.isnumeric() == True:
                        curso = input("O nome do curso deve conter apenas caracteres!! Digite novamente:")

                    cargahoraria = input ("Informe a nova carga horaria: ")
                    while cargahoraria.isnumeric() == False or int(cargahoraria) < 0 :
                        cargahoraria = input("A carga horaria deve conter apenas numeros e deve ser maior que 0!! Digite novamente:")


                    anoletivo = input("Informe o novo ano letivo : ")
                    while anoletivo.isnumeric() == False or int(anoletivo) <= 0:
                        anoletivo = input( "Ano letivo inválido !! Digite novamente:")
                        
                        
                        
                    codigodiscplina = input ("Informe o novo código da disciplina: ")
                    while codigodiscplina.isnumeric() == False or int(codigodiscplina) <= 0 :
                        codigodiscplina = input("Código da Disciplina inválido!! Digite novamente:")
                    

                    cdprof = input ("Informe o novo código do professor: ")
                    while cdprof.isnumeric() == False or int(cdprof) <= 0:
                        cdprof = input("Código do Professor inválido !! Digite novamente:")

                    msg = alterardiscxprof(cddisciprof,curso, cargahoraria,anoletivo,codigodiscplina, cdprof)
                    

                




                elif op == 'E':
                    
                    cddisciprof = input(" Qual o código de registro que pertence ao professor que deseja excluir? ")
                    while cddisciprof.isnumeric() == False or int(cddisciprof) <=0 :
                        cddisciprof = input(" Código inválido!! Digite novamente:")
                    comandosql = conexao.cursor()
                    comandosql.execute(f'select * from  disciplinasxprofessores  where codigodisciplinanocurso = {cddisciprof};')
            
                    tabelaexluir = comandosql.fetchall()
                    for registro in tabelaexluir:
                            grid = PrettyTable(['Codigo da Disciplina no Curso', "Curso", "Carga Horaria", "Ano letivo","Código da Disciplina","Código do Professor" ])
                            grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4], registro[5]])
                    print(grid)
                    conexao.commit()
                    
                    
                    
                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                    msg = excluirdiscxprof(cddisciprof)
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

