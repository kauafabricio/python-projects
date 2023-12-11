# SISTEMA BANCÁRIO ORIENTADO À OBJETOS: CRIAR CLIENTE, CRIAR CONTA, LISTAR CONTAS DO CLIENTE, DEPOSITAR NA CONTA, SACAR DA CONTA, EXTRATO DA CONTA.
# COM ACRESCENTO DA FUNCIONALIDADE DE ESCOLHER A CONTA DO CLIENTE QUE IRÁ REALIZAR A OPERAÇÃO.
# LINKEDIN: https://www.linkedin.com/in/kaua-fabricio-ds

from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
import textwrap
from datetime import datetime

class Cliente:
    def __init__(self, cpf, nome):
        self.contas = []
        self.cpf = cpf
        self.nome = nome

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def registrar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, endereco, nascimento, cpf):
        super().__init__(cpf, nome)
        self.nascimento = nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero_conta, cliente):
        return cls(numero_conta, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            input("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            input("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            input("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            input("\n=== Depósito realizado com sucesso! ===")
        else:
            input("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):

        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):

        numero_saques = len( 
            [transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__]
            )
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            input("\n@@@@@ O valor limite do saque na conta corrente é de R$500.00 por vez. @@@@@")
        
        elif excedeu_saques:
            input("@@@@@ Seu limite de saques diários já foi atingido! @@@@")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"Conta: {self._numero}, Saldo: R${self._saldo}, Cliente: {self._cliente.nome}"
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append( 
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\tBem-vindo(a) ao Banco Python!\n\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    \n=> """
    return input(textwrap.dedent(menu))

def main():
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            input("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


def criar_cliente(clientes):
    while True:

        cpf = input("Bem-vindo(a), obrigado por escolher o Banco Python! Por favor, digite seu CPF (sem pontos): ")

        if cpf.isdigit():
            cpf = int(cpf)
            cliente = filtrar_cliente(clientes, cpf)

            if not cliente:
                nome = input("Digite seu nome: ")

                nascimento = input("Digite sua data de nascimento(%D-%M-%A): ")

                endereco = input("Digite seu endereço(logradouro - bairro - cidade - sigla estado/país)")

                cliente = PessoaFisica(nome= nome, endereco= endereco, nascimento= nascimento, cpf= cpf)

                clientes.append(cliente)

                input("\n === Cliente/Usuário criado com sucesso! ===")
                return clientes
        else:
            input("@@@ Digite apenas seu CPF (Apenas números). @@@")

def filtrar_cliente(clientes, cpf):
    cliente_filtrado = [cliente for cliente in clientes if cliente.cpf == cpf]

    return cliente_filtrado[0] if cliente_filtrado else None

def criar_conta(numero_conta, clientes, contas):
    while True:
        cpf = input("Por favor, digite seu CPF (sem pontos): ")

        if cpf.isdigit():
            cpf = int(cpf)
            cliente = filtrar_cliente(clientes, cpf)
            
            if not cliente:
                erro = input("@@@ CLIENTE NÃO ENCONTRADO! CASO QUEIRA CRIAR UMA CONTA, PRIMEIRO SE CADASTRE COMO CLIENTE DO BANCO! @@@")
                break
            
            conta = ContaCorrente(numero_conta=numero_conta, cliente=cliente)
            
            cliente.contas.append(conta)

            contas.append(conta)

            conta_criada = input("\n === Conta corrente criada com sucesso! ===")
            
            return contas
        
        else:
            input("Digite apenas seu CPF (Apenas números): ")

def escolher_conta(cliente):
    if not cliente.contas:
        input("@@@ Você não possui conta ainda, crie uma! @@@")
        return
    
    conta = input(f"Essas são as suas contas: {[str(c) for c in cliente.contas]}\n Escolha uma conta para realizar a operação: ")

    if conta.isdigit():
        indice = int(conta) - 1
        if 0 <= indice < len(cliente.contas):
            return cliente.contas[indice]
        else:
            input("Essa conta não existe na lista!")
            return
    else: 
        input("@@@ Digite apenas o número da conta. @@@")
        return

def depositar(clientes):
    cpf = input("Digite seu CPF(apenas números): ")

    if cpf.isdigit():
        cpf= int(cpf)
        cliente = filtrar_cliente(clientes, cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return
        
        valor = input("Digite o valor do depósito: ")

        if valor.isdigit():
            valor = float(valor)

            transacao = Deposito(valor)

            conta = escolher_conta(cliente)

            if not conta:
                return
            
            cliente.realizar_transacao(conta, transacao)
        else:
            input("@@@ Digite apenas números para representar o valor do depósito! @@@")
            return
    else:
        input("Digite apenas o número do seu CPF!")
        return

def listar_contas(contas):
    for conta in contas:
        print("=" * 25+ "\n")
        print(textwrap.dedent(str(conta)))
        input("\n" + "=" * 25)

def sacar(clientes):
    cpf = input("Digite seu CPF(apenas números): ")

    if cpf.isdigit():
        cpf= int(cpf)
        cliente = filtrar_cliente(clientes, cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return
        
        valor = input("Digite o valor do seu saque: ")
        if valor.isdigit():
            valor = float(valor)
            transacao = Saque(valor)

            conta = escolher_conta(cliente)
            if not conta:
                return
            
            cliente.realizar_transacao(conta, transacao)
        else:
            input("@@@ Digite apenas números para representar o valor do seu saque! @@@")
            return
    else:
        input("Digite apenas seu CPF(apenas números).")
        return

def exibir_extrato(clientes):
    cpf = input("Digite seu CPF(apenas números): ")

    if cpf.isdigit():
        cpf= int(cpf)
        cliente = filtrar_cliente(clientes, cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return
        
        conta = escolher_conta(cliente)

        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes

        if not transacoes:
            extrato = input("Não foram realizadas movimentações.")
            return
        else:
            for transacao in transacoes:
                extrato = print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']}")
                
            input("\n\n" + "=" * 42)

main()