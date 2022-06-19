from flask_restful import Resource
from ..schemas import conta_schema
from flask import request, make_response, jsonify
from ..entidades import conta
from ..services import conta_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators.autorizacao import user_conta
from ..decorators.api_key import require_apikey


class ContaList(Resource):
    def get(self):
        contas = conta_service.listar_contas()
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 201)

    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, valor=valor)
            resultado = conta_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(resultado), 201)

class ContaDetail(Resource):
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)

    def put(self, id):
        conta_bd = conta_service.listar_conta_id(id)
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, valor=valor)
            resultado = conta_service.atualizar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(resultado), 201)

    def delete(self, id):
        conta = conta_service.listar_conta_id(id)
        conta_service.exclui_conta(conta)
        return make_response(jsonify(""), 204)

api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')