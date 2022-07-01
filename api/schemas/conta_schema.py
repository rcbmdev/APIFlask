from api import ma
from ..models import conta_model
from marshmallow import fields
from ..schemas import operacao_schema

class ContaSchema(ma.SQLAlchemyAutoSchema):
    operacoes = ma.Nested(operacao_schema.OperacaoSchema, many=True, only=('nome', 'resumo', 'tipo', 'custo', 'data'))
    class Meta:
        model = conta_model.Conta
        load_instance = True

        nome = fields.String(required=True)
        valor = fields.Float(required=True)


