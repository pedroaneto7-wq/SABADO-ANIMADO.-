import os
os.system
lista_nome = []
lista_sobrenome = []
lista_pacientes = []
codigo_do_paciente = []


while True:
    print('''
          ==== Medico do Senai ====
          1- cadastro do paciente
          2- lista  de pacientes
          3- atualizar pacientes
          4- escluir pacientes
          ''')
    
    opicao = int(input('qual sua opição'))
    
    match opicao:
        
        case 1:
            print('=== Cadastro de pacientes ===')
            nome = input('Me fale seu nome:').strip().upper()
            sobrenome = input('Me fale seu nome:').strip().upper()
            if nome == sobrenome == '':
                print('cadastrando o senhor(A)')
            elif nome in sobrenome:
                print('paciente já cadastrado')
            else:
                nome.append(sobrenome)
                
        case 2:
            print('=== Pacientres ja cdastrados ===')
            for nome in sobrenome:
                print(f'- {nome}')
                print(f'total: {len(lista_pacientes)}')
                
        case 3:
            print('=== Atualizando lista de cadastros ===')
            codigo_do_paciente = input('digite seu codigo')
            if codigo_do_paciente in lista_pacientes:
                novo = input(' novo codigo')
                lista_pacientes [codigo_do_paciente] = novo
                print('cadastros modificados com sucesso')
            else:
                print('produto não encontrado')
                
        case 4:
            print('=== Removendo cadastros ===')
            if codigo_do_paciente in lista_pacientes:
                print('produto encontrado')
                lista_pacientes.remove(codigo_do_paciente)
            else:
                print('cadastro removido')
                
        case 0:
            print('saindo do programa')
            break
        case _:
            print('opição invalida')
            
            
    input('precione a tecla para continuar...')