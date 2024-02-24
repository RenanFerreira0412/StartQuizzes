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

    is_authenticated = auth_service.signInWithEmailAndPassword(
        data['email'], data['password'])

    if is_authenticated:
        return jsonify({"message": "Bem vindo de volta."}), 200

    return jsonify({"message": "E-mail ou senha inválidos."}), 404


@auth_bp.route("/api/v1/app/cadastro", methods=["POST"])
def register():
    """
    realizando o cadastro do usuário
    """

    # recebendo os dados
    data = request.get_json()

    is_created = auth_service.createUserWithEmailAndPassword(
        data['name'], data['email'], data['password'])

    if is_created:
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 200

    return jsonify({"message": "Este endereço de email já existe!"}), 404


@auth_bp.route("/api/v1/app/redefinirsenha", methods=["POST"])
def reset_password():
    """
    realizando o processo de mudança de senha do usuário
    """

    data = request.get_json()

    is_reset = auth_service.resetPassword(data['email'], data['password'])

    if is_reset:
        return jsonify({"message": "Sua senha foi atualizada com sucesso! Realize novamente o seu login."}), 200

    return jsonify({"message": "Este endereço de email não foi encontrado."}), 404


@auth_bp.route("/api/v1/usuarioatual", methods=["GET"])
def get_current_user():
    """
    realizando o processo de verificação do usuário atual, ou seja, o usuário que está logado
    """

    # usuário atual
    user_data = auth_service.getCurrentUser()
    currentUser = User(*user_data)

    # convertendo para json
    response = json.dumps(currentUser.__dict__)
    return Response(response, mimetype="application/json")
