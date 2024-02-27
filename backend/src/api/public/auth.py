from flask import Blueprint, request, jsonify, Response, json
from ...instances import auth_service
from ...models.user import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/api/v1/app/entrar", methods=["POST"])
def login():
    """
    realizando o login do usuário
    """

    # recebendo os dados
    data = request.get_json()

    response = auth_service.signInWithEmailAndPassword(
        data['email'], data['password'])

    return jsonify({"message": response['message'], "data": response['data']}), response['status']


@auth_bp.route("/api/v1/app/cadastro", methods=["POST"])
def register():
    """
    realizando o cadastro do usuário
    """

    # recebendo os dados
    data = request.get_json()

    response = auth_service.createUserWithEmailAndPassword(
        data['name'], data['email'], data['password'])

    return jsonify({"message": response["message"], "data": response["data"]}), response["status"]


@auth_bp.route("/api/v1/app/redefinirsenha", methods=["POST"])
def reset_password():
    """
    realizando o processo de mudança de senha do usuário
    """

    data = request.get_json()

    response = auth_service.resetPassword(data['email'], data['password'])

    return jsonify({"message": response["message"], "data": response["data"]}), response["status"]


@auth_bp.route("/api/v1/usuarioatual", methods=["GET"])
def get_active_users():
    """
    realizando o processo de verificação dos usuário ativos no app
    """

    # usuário atual
    response = auth_service.getActiveUsers()
    active_users = [User(*data).toDict() for data in response["data"]]

    # convertendo para json
    res = json.dumps(active_users)

    return Response(res, mimetype="application/json")
