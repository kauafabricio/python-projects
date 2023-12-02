# SISTEMA BANCÁRIO COM OPERAÇÕES DE EXTRATO, DEPÓSITO, E SAQUE APENAS.
# UMA VERSÃO MAIS ATUALIZADA COM OPERAÇÕES CRIAR CONTA E ENTRAR NA CONTA, ./bank-system-v2.py.
# MEU LINKEDIN: https://www.linkedin.com/in/kaua-fabricio-ds

inicio = '''Olá, bem-vindo ao Banco Python, você iniciará com o saldo de R$5000.00 na sua conta, digite seu nome:
'''
nome = input(str(inicio))
nome = nome.title()
saldo = 5000.00
numero_saques = 0
LIMITE_SAQUES = 3
saques_realizados = []
numero_depositos = 0
depositos_realizados = []
def menu():
     menu = f'''Seja bem-vindo(a), {nome}.
        Digite a letra da operação que você quer realizar:

        [e] Extrato
        [d] Depositar
        [s] Saque
        [q] Sair
    '''
     print(menu)
def extrato(saldo, saques_realizados, numero_depositos, numero_saques, depositos_realizados):
     if (numero_saques == 0) and (numero_depositos == 0):
          first_output = input(f"=============== EXTRATO ===============\nO seu saldo atual é: {saldo}\n=======================================\n Para voltar para o Menu, digite [b]")
          if (first_output == 'b'):
               menu()
     elif (numero_saques > 0) or (numero_depositos > 0):
          output = input(f"=============== EXTRATO ===============\nO seu saldo atual é: {saldo}\n\n Saques:\n{saques_realizados}\n\n Depósitos:\n{depositos_realizados}\n=======================================\nPara voltar para o Menu, digite [b]")
          if (output == 'b'):
               menu()
def deposito(saldo, numero_depositos, depositos_realizados):
         try:
              deposito = float(input("Digite o valor do depósito:"))  
              if deposito > 0:
                   saldo += deposito
                   numero_depositos += 1
                   depositos_realizados.append(f"[{numero_depositos}] Depósito realizado no valor de R${deposito}.")
                   resultado = input(f"Depósito no valor de R${deposito} foi realizado com sucesso! Digite [b] para voltar ao menu:")
                   if resultado == 'b':
                      menu()
                   return saldo, numero_depositos, depositos_realizados
              else:
                   print("Digite apenas valores positivos.")
                   return saldo, numero_depositos, depositos_realizados
         except ValueError:
              print("Digite apenas o valor para realizar o depósito.")
              return saldo, numero_depositos, depositos_realizados
def saque(saldo, numero_saques, saques_realizados, LIMITE_SAQUES):
     if (numero_saques < LIMITE_SAQUES):
          valor_saque = float(input("Digite o valor do saque:"))
          if (valor_saque <= saldo) and (valor_saque <= 500.00):
               saldo -= valor_saque
               numero_saques += 1
               saques_realizados.append(f"[{numero_saques}] Saque realizado no valor de R${valor_saque}.")
               saque_final = input(f"Saque no valor de R${valor_saque} realizado com sucesso!\n Digite [b] para voltar ao menu:")
               if (saque_final == 'b'):
                    menu()
               return saldo, numero_saques, saques_realizados
          else:
               valor_erro = input("Erro! Ou você está com saldo insuficiente, ou o valor do saque ultrapassou o limite que é R$500.00 por vez.\n\nCaso deseja tentar novamente digite [s], ou voltar para o menu [b]:")
               if(valor_erro == 's'):
                    saque(saldo, numero_saques, saques_realizados, LIMITE_SAQUES)
               else:
                    menu()
               return saldo, numero_saques, saques_realizados
     else:
          erro_saque = input("Erro! Você só pode efetuar 3 saques por dia, tente novamente amanhã. Digite [b] para voltar ao menu:")
          if(erro_saque == 'b'):
               menu()
          return saldo, numero_saques, saques_realizados
menu()
while True:
    opcao = input("Escolha uma opção do menu: ")

    if opcao == 'e':
        extrato(saldo, saques_realizados, numero_depositos, numero_saques, depositos_realizados)
    elif opcao == 'd':
        saldo, numero_depositos, depositos_realizados = deposito(saldo, numero_depositos, depositos_realizados)
    elif opcao == 's':
         saldo, numero_saques, saques_realizados = saque(saldo, numero_saques, saques_realizados, LIMITE_SAQUES)
    elif opcao == 'q':
        print("Obrigado por usar o Banco Python. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida do menu.")