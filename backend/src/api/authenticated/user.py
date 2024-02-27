from flask import Blueprint, request, jsonify, json, Response
from ...instances import auth_service
from ...services.database.db import Database

user_bp = Blueprint("user", __name__)


@user_bp.route("/api/v1/app/usuario/<uid>", methods=["GET"])
def find(uid):
    """
    realizando a busca pelo usuário
    """

    # usuário
    response = Database.users.find(uid)

    # convertendo para json
    res = json.dumps(response["data"])
    return Response(res, mimetype="application/json")


@user_bp.route("/api/v1/app/conta/atualizar/<uid>", methods=["PUT"])
def update_account(uid):
    """
    realizando a atualização das informações do usuário
    """

    # recebendo os dados
    data = request.get_json()

    # atualizando as informações
    response = Database.users.updateOne(uid, data['name'])

    return jsonify({"message": response['message']}), response["status"]


@user_bp.route("/api/v1/app/conta/deletar/<uid>", methods=["DELETE"])
def delete_account(uid):
    """
    realizando a exclusão da conta do usuário
    """
    response = auth_service.deleteAccount(uid)

    return jsonify({"message": response["message"]}), response["status"]


@user_bp.route("/api/v1/app/conta/desconectar/<uid>", methods=["PUT"])
def logout(uid):
    """
    realizando a atualização do estado de ativação do usuário
    """

    response = auth_service.signOut(uid)

    return jsonify({"message": response["message"]}), response["status"]
