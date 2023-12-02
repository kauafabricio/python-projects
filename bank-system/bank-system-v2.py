# SISTEMA BANCÁRIO COM OPERAÇÕES DE CRIAR CONTA, ENTRAR NA CONTA, MENU, EXTRATO, DEPÓSITO, E SAQUE.
# MEU LINKEDIN: https://www.linkedin.com/in/kaua-fabricio-ds

numero_da_conta = 100100100
contas = {}
movimentacao_contas = {}

def output_inicial():
     inicio = f'''Olá, seja bem-vindo(a) ao Banco Python!\n\n[cc] Criar Conta\n[lg] Entrar\n[q] Sair\n\n'''
     print(inicio)
def criar_conta(contas, output_inicial, numero_da_conta, movimentacao_contas, AGENCIA = 1001):
     while True:
          cpf = input("Informe seu CPF (sem pontos): ")
          if cpf.isdigit():
               cpf = int(cpf)
               if cpf in contas:
                    print("@@@@@@@@@@Esse CPF já está cadastrado no Banco Python!@@@@@@@@@@\n\nVocê será redirecionado(a) para o início.")
                    output_inicial()
                    return contas, numero_da_conta, movimentacao_contas
               else:
                    contas[cpf] = {} 
                    movimentacao_contas[cpf] = {}
                    movimentacao_contas[cpf]['saldo'] = 0
                    movimentacao_contas[cpf]['numero_depositos'] = 0
                    movimentacao_contas[cpf]['numero_saques']= 0
                    movimentacao_contas[cpf]['depositos_realizados']= []
                    movimentacao_contas[cpf]['saques_realizados'] = []
                    contas[cpf]['nome'] = str(input("Digite seu nome: "))
                    contas[cpf]['nascimento'] = input("Digite sua data de nascimento (dd-mm-aaaa): ")
                    contas[cpf]['endereco'] = input("Informe seu endereço, nesse formato (logradouro, bairro, cidade, estado): ")
                    senha = input("Digite sua senha: ")
                    contas[cpf]['senha'] = senha
                    contas[cpf]['agencia'] = AGENCIA
                    contas[cpf]['numero_da_conta'] = numero_da_conta
                    resultado= input(f"====Sua conta foi criada com sucesso!====\nResumo:\n\nCPF:\t{cpf}\nNome:\t{contas[cpf]['nome']}\nData de Nascimento:\t{contas[cpf]['nascimento']}\nEndereço:\t{contas[cpf]['endereco']}\nAgência:\t{contas[cpf]['agencia']}\nNúmero da conta:\t{contas[cpf]['numero_da_conta']}\n\nAperte qualquer tecla para ser redirecionado(a) para o início, entre na sua conta!")
                    output_inicial()
                    return contas, numero_da_conta + 1, movimentacao_contas,  numero_da_conta + 1
          else:
               print("Digite apenas números inteiros, sem pontuação!")
def entrar_conta(contas, menu):
     while True:

          cpf = input("Digite seu CPF: ")
          if cpf.isdigit():
               cpf = int(cpf)
               if cpf in contas:
                    senha = input("Digite sua senha: ")
                    if senha == contas[cpf]['senha']:
                         print("Bem-vindo(a) ao Banco Python!")
                         menu(contas, cpf)
                         return contas
                    else:
                         print("A senha está incorreta! Digite novamente.")
               else:
                    print("CPF digitado não foi encontrado!")
          else:
               print("Digite apenas números!")
def menu(contas, cpf):
          
         menu = f'''Seja bem-vindo(a), {contas[cpf]['nome']}.
            Digite a letra da operação que você quer realizar:

            [e] Extrato
            [d] Depositar
            [s] Saque
            [q] Sair
         '''
         print(menu)
def extrato(movimentacao_contas):
     while True:
          cpf = input("Digite seu CPF para acessar o seu extrato: ")
          if cpf.isdigit():
               cpf = int(cpf)
               if cpf in movimentacao_contas:
                    
                    if movimentacao_contas[cpf]['numero_depositos'] == 0 and movimentacao_contas[cpf]['numero_saques'] == 0:
                         first_output = input(f"=============== EXTRATO ===============\nO seu saldo atual é: {movimentacao_contas[cpf]['saldo']}\n=======================================\n Para voltar para o Menu, aperte qualquer tecla.")
                         menu(contas, cpf)
                         return movimentacao_contas
                    elif movimentacao_contas[cpf]['numero_depositos']>0 or movimentacao_contas[cpf]['numero_saques'] > 0:
                         output = input(f"=============== EXTRATO ===============\nO seu saldo atual é: {movimentacao_contas[cpf]['saldo']}\n\n Saques:\n{movimentacao_contas[cpf]['saques_realizados']}\n\n Depósitos:\n{movimentacao_contas[cpf]['depositos_realizados']}\n=======================================\nPara voltar para o Menu, aperte qualquer tecla.")
                         menu(contas, cpf)
                         return movimentacao_contas
               else:
                    print("CPF não encontrado! Digite novamente.")
          else:
               print("Digite apenas os números do seu CPF!")
def deposito(movimentacao_contas, contas):
          while True:
              cpf = input("Digite o CPF da sua conta para depositar: ")
              if cpf.isdigit(): 
                    cpf = int(cpf)
                    if cpf in contas:
                         senha = input("Digite sua senha por segurança: ")
                         if senha == contas[cpf]['senha']:
                              deposito = input("Digite o valor do depósito: ")
                              if deposito.isdigit():
                                   deposito = float(deposito)
                                   if deposito > 0:
                                        movimentacao_contas[cpf]['saldo'] += deposito
                                        movimentacao_contas[cpf]['numero_depositos'] += 1
                                        movimentacao_contas[cpf]['depositos_realizados'].append(f"[{movimentacao_contas[cpf]['numero_depositos']}] Depósito realizado no valor de R${deposito}.")
                                        resultado = input(f"Depósito no valor de R${deposito} foi realizado com sucesso! Aperte qualquer tecla para voltar ao Menu.")
                                        menu(contas, cpf)
                                        return movimentacao_contas
                                   else:
                                         print("Digite apenas valores positivos.")
                              else:
                                   print("Digite apenas números!")
                         else:
                              print("@@@@@ Senha Inválida! Digite novamente. @@@@@")
                    else:
                         print("@@@@@ CPF não encontrado, digite novamente! @@@@@")
              else:
                   print("Digite apenas números!")
def saque(movimentacao_contas, contas, LIMITE_SAQUES = 3):
     while True:
          cpf = input("[CPF] Por sua segurança, digite seu CPF para realizar o saque: ")
          if cpf.isdigit():
               cpf = int(cpf)
               if cpf in contas:
                    if (movimentacao_contas[cpf]['numero_saques'] < LIMITE_SAQUES):
                         senha = input("[SENHA] Por sua segurança, digite sua senha: ")
                         if senha == contas[cpf]['senha']:
                              valor_saque = input("[SAQUE] Digite o valor do saque: ")
                              if valor_saque.isdigit() and valor_saque > '0':
                                   valor_saque = float(valor_saque)
                                   if (valor_saque <= movimentacao_contas[cpf]['saldo']) and (valor_saque <= 500.00):
                                        movimentacao_contas[cpf]['saldo'] -= valor_saque
                                        movimentacao_contas[cpf]['numero_saques'] += 1
                                        movimentacao_contas[cpf]['saques_realizados'].append(f"[{movimentacao_contas[cpf]['numero_saques']}] Saque realizado no valor de R${valor_saque}.")
                                        saque_final = input(f"Saque no valor de R${valor_saque} realizado com sucesso!\n Aperte qualquer tecla para voltar ao menu.")
                                        menu(contas, cpf)
                                        return movimentacao_contas
                                   else:
                                        print("ATENÇÃO: o limite do valor do saque é R$500.00 por vez.\nSe você digitou um valor igual ou menor que R$500.00, você está com saldo insuficiente!")
                                        menu(contas, cpf)
                                        return movimentacao_contas
                              else:
                                   print("Digite apenas números positivos!")
                         else:
                              print("Senha incorreta! Digite novamente a senha.")
                    else:
                         print("Número de saques realizados já atingiu o seu limite diário. Tente novamente amanhã!")
                         menu(contas, cpf)
                         return movimentacao_contas
               else:
                    print("CPF não encontrado! Digite novamente.")
          else:
               print("Digite apenas números para o CPF!")
output_inicial()
while True:
    opcao = input("Escolha uma opção: ")
    if opcao == 'cc':
        contas, numero_da_conta, movimentacao_contas, numero_da_conta = criar_conta(contas, output_inicial, numero_da_conta, movimentacao_contas)
    elif opcao == 'lg':
         contas = entrar_conta(contas, menu)
    elif opcao == 'q':
        print("Obrigado por usar o Banco Python. Até logo!")
        break
    elif opcao == 'e':
        movimentacao_contas = extrato(movimentacao_contas)
    elif opcao == 'd':
        movimentacao_contas = deposito(movimentacao_contas, contas)
    elif opcao == 's':
         movimentacao_contas = saque(movimentacao_contas, contas)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida do menu.")