from flask import Blueprint, request, jsonify, json, Response
from ...instances import auth_service
from ...services.database.db import Database

from ...models.user import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/api/v1/app/usuario/<uid>", methods=["GET"])
def find(uid):
    """
    realizando a busca pelo usuário
    """

    # usuário
    data = Database.users.find(uid)
    user = User(*data)

    # convertendo para json
    response = json.dumps(user.__dict__)
    return Response(response, mimetype="application/json")


@user_bp.route("/api/v1/app/conta/atualizar/<uid>", methods=["PUT"])
def update_account(uid):
    """
    realizando a atualização das informações do usuário
    """

    print('id', uid)

    # recebendo os dados
    data = request.get_json()

    # atualizando as informações
    Database.users.updateOne(uid, data['name'])

    return jsonify({"message": "Informação atualizada com sucesso."}), 200


@user_bp.route("/api/v1/app/conta/deletar/<uid>", methods=["DELETE"])
def delete_account(uid):
    """
    realizando a exclusão da conta do usuário
    """
    auth_service.deleteAccount(uid)

    return jsonify({"message": "Sua conta foi deletada com sucesso!"}), 200


@user_bp.route("/api/v1/app/conta/desconectar/<uid>", methods=["PUT"])
def logout(uid):
    """
    realizando a atualização do estado de ativação do usuário
    """

    print('id: ', uid)

    auth_service.signOut(uid)

    return jsonify({"message": "Desconectado(a) com sucesso!"}), 200
