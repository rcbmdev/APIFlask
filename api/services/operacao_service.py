from api import db
from ..models import operacao_model, conta_model
from ..services import conta_service

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def listar_operacao_id(id):
    operacao = operacao_model.Operacao.query.filter_by(id=id).first()
    return operacao

def cadastrar_operacao(operacao):
    operacao_bd = operacao_model.Operacao(
        nome=operacao.nome,
        resumo=operacao.resumo,
        custo=operacao.custo,
        tipo=operacao.tipo,
        data=operacao.data,
        conta_id=operacao.conta
    )
    db.session.add(operacao_bd)
    db.session.commit()
    conta_service.altera_saldo_conta(operacao.conta, operacao, 1)

    return operacao_bd

def atualizar_operacao(operacao, operacao_nova):
    valor_antigo = operacao.custo
    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    operacao.tipo = operacao_nova.tipo
    operacao.data = operacao_nova.data
    operacao.conta_id = operacao_nova.conta
    db.session.commit()
    conta_service.altera_saldo_conta(operacao_nova.conta, operacao_nova, 2, valor_antigo)
    return operacao

def exclui_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()
    conta_service.altera_saldo_conta(operacao.conta_id, operacao, 3)

