from api import ma
from ..models import operacao_model
from marshmallow import fields
from marshmallow_enum import EnumField

class OperacaoSchema(ma.SQLAlchemyAutoSchema):
    tipo = EnumField(operacao_model.TipoEnum)

    class Meta:
        model = operacao_model.Operacao
        load_instance = True
        include_fk = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        custo = fields.Float(required=True)
        conta_id = fields.Integer(required=True)
        data = fields.Date(required=True)


