import psycopg2
from config import Config
from ...models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from ...utils.utils import Utils


class Authentication:
    """
    Classe para representar o serviço de autenticação
    """

    def __init__(self):
        self.conn = Config.get_db_connection()

    # receber usuário atual
    def getActiveUsers(self):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "SELECT * FROM users WHERE is_active=%s", (True,))
                    users = curs.fetchall()
            return Utils.sendMessage(200, "Dados carregados com sucesso!", users)
        except psycopg2.Error as e:
            print(f'Erro ao buscar usuário: {e}')
            return Utils.sendMessage(404, str(e), None)

    # entrar na conta
    def signInWithEmailAndPassword(self, email, password):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "SELECT * FROM users WHERE email=%s", (email,))
                    data = curs.fetchone()

                    if not data or not check_password_hash(data[3], password):
                        return Utils.sendMessage(404, "E-mail ou senha inválidos.", None)

                    curs.execute(
                        "UPDATE users SET is_active=%s WHERE id=%s", (True, data[0]))

                    conn.commit()

                    # dados do usuário
                    user = User(*data).toDict()

            return Utils.sendMessage(201, "Bem vindo de volta.", user)
        except psycopg2.Error as e:
            print(f'Erro ao fazer login: {e}')
            return Utils.sendMessage(404, str(e), None)

    # criar conta
    def createUserWithEmailAndPassword(self, name, email, password):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    pwd = generate_password_hash(password)
                    curs.execute(
                        'INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email, password, is_active, created_at', (name, email, pwd))
                    conn.commit()

                    # Recuperar o último usuário inserido
                    data = curs.fetchone()

                    print(data)

                    # dados do usuário
                    user = User(*data).toDict()

            return Utils.sendMessage(201, "Usuário cadastrado com sucesso!", user)
        except psycopg2.Error as e:
            print(f'Erro ao criar usuário: {e}')
            if e.pgcode == "23505":
                # Se o código de erro for 23505, isso significa que o email já existe na tabela
                return Utils.sendMessage(404, "Este endereço de email já existe!", None)
            else:
                # Se for outro tipo de erro, retorne uma mensagem genérica de erro
                return Utils.sendMessage(404, str(e), None)

    # desconectar da conta
    def signOut(self, uid):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "UPDATE users SET is_active=%s WHERE id=%s", (False, uid))
                    conn.commit()

            return Utils.sendMessage(201, "Desconectado(a) com sucesso!", None)
        except psycopg2.Error as e:
            print(f'Erro ao sair da conta: {e}')
            return Utils.sendMessage(404, str(e), None)

    # deletar conta
    def deleteAccount(self, uid):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute("DELETE FROM users WHERE id=%s", (uid,))
                    conn.commit()

            return Utils.sendMessage(200, "Sua conta foi deletada com sucesso!", None)
        except psycopg2.Error as e:
            print(f'Erro ao deletar conta: {e}')
            return Utils.sendMessage(404, str(e), None)

    # mudar senha
    def resetPassword(self, email, password):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "SELECT * FROM users WHERE email=%s", (email,))
                    user = curs.fetchone()

                    if not user:
                        return Utils.sendMessage(404, "Este endereço de email não foi encontrado.", None)

                    pwd = generate_password_hash(password)
                    curs.execute(
                        "UPDATE users SET password=%s WHERE id=%s", (pwd, user[0]))

                    conn.commit()

            return Utils.sendMessage(404, "Sua senha foi atualizada com sucesso! Realize novamente o seu login.", None)
        except psycopg2.Error as e:
            print(f'Erro ao redefinir senha: {e}')
            return Utils.sendMessage(404, str(e), None)
