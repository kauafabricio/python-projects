""" Projeto de conexão com banco de dados SQL pelo framework SQLAlchemy"""


import pprint
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
import sqlalchemy
from sqlalchemy import Column, inspect, select
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy.orm import relationship

Base = declarative_base()


class Clientes(Base):
    """ Classe Clientes representa a tabela 'Clientes' do 
    banco de dados relacional e tem relacionamento com a tabela
    'Contas'.
    """
    __tablename__ = 'Clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(35), nullable=False)
    cpf = Column(Integer, nullable=False, unique=True)
    data_de_nascimento = Column(Integer, nullable=False)
    endereco = Column(String, nullable=False)
    contas = relationship('ContasPessoaFisica', back_populates = 'cliente')

    def __repr__(self):
        return f"Nome completo: {self.nome_completo}, CPF: {self.cpf}, Data de nascimento: {self.data_de_nascimento}, Endereço: {self.endereco}"


class ContasPessoaFisica(Base):
    """ Classe 'Contas' que representa a tabela 'Contas' do
    banco de dados relacional e tem relacionamento com a tabela
    'Clientes'.
    """
    __tablename__ = 'Contas de Pessoa Física'

    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True)
    numero_conta = Column(Integer, nullable=False, unique=True)
    agencia = Column(Integer, nullable=False)
    saldo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey(Clientes.id), nullable=False)
    cliente = relationship('Clientes', back_populates = 'contas')

    def __repr__(self):
        return f"Numero da conta: {self.numero_conta}, Agência: {self.agencia}, Saldo: {self.saldo}, Cliente: {self.cliente_id}"


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
""" Conexão com o banco de dados pelo engine."""


with Session(engine) as session:
    """Abrir sessão para inserir dados no banco de dados pelo engine."""

    will_byers = Clientes(
        nome_completo = 'Will Byers',
        cpf = 12345678910,
        data_de_nascimento = 16011984,
        endereco = 'Rua das Coisas Estranhas, 94',
        contas = [ContasPessoaFisica(
            numero_conta = 1234567,
            agencia = 1001,
            saldo = 500.0
        ), ContasPessoaFisica(
            numero_conta = 7654321,
            agencia = 1001,
            saldo = 0.0
        )]
    )

    jonathan_byers = Clientes(
        nome_completo = 'Jonathan Byers',
        cpf = 21354687910,
        data_de_nascimento = 10101980,
        endereco = 'Rua das Coisas Estranhas, 94',
        contas = [ContasPessoaFisica(
            numero_conta = 1234568,
            agencia = 1001,
            saldo = 1500.0
        )]
    )
    

    session.add_all([will_byers, jonathan_byers])
    session.commit()

#Recuperando dados do cliente Will Byers

print("\nRecuperando contas do Will Byers\n")

contas_do_will = select(ContasPessoaFisica).where(ContasPessoaFisica.cliente_id.in_([1]))
for contas in session.scalars(contas_do_will):
    pprint.pprint(contas)

print("\nRecuperando nomes das tabelas do banco de dados\n")

inspetor = inspect(engine)
print(inspetor.get_table_names())
