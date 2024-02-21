from datetime import datetime
import psycopg2
from config import Config

from werkzeug.security import generate_password_hash, check_password_hash


class Authentication:
    """
    classe para representar o serviço de autenticação
    """

    conn = Config.get_db_connection()
    cur = conn.cursor()

    # buscar usuário atual
    @classmethod
    def getCurrentUser(cls):
        try:
            cls.cur.execute("SELECT * FROM users WHERE is_active=%s", (True,))
            user = cls.cur.fetchone()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
            return user
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # entrar na conta
    @classmethod
    def signInWithEmailAndPassword(cls, email, password):
        try:
            # verificar se o usuário existe no banco de dados
            cls.cur.execute(
                "SELECT * FROM users WHERE email=%s", (email,))
            user = cls.cur.fetchone()

            # verificando se o usuário não foi encontrado ou
            # se a senha está errada
            if not user or check_password_hash(user[2], password):
                return False

            # atualizando o status de ativação do usuário
            cls.cur(
                "UPDATE FROM users SET is_active=%s WHERE id=%s", (
                    True, user[0])
            )

            # executando as mudanças
            cls.conn.commit()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # criar uma conta
    @classmethod
    def createUserWithEmailAndPassword(cls, name, email, password):
        try:
            # procurando usuário
            cls.cur.execute("SELECT * FORM users WHERE email=%s", (email,))
            user = cls.cur.fetchone()

            # verificando se o email já foi cadastrado
            if user:
                return False

            # data atual
            date = datetime.now()

            # 'escondendo' a senha informada pelo usuário
            pwd = generate_password_hash(password)

            cls.cur.execute(
                "INSERT INTO users (name, email, password, created_at, is_active)"
                "VALUES (%s, %s, %s, %s, %s)",
                (name, email, pwd, date, True))

            # executando as mudanças
            cls.conn.commit()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # sair da conta
    @classmethod
    def signOut(cls, uid):
        try:
            cls.cur.execute(
                "UPDATE FROM users SET created_at=%s WHERE id=%s", (False, uid))

            # executando as mudanças
            cls.conn.commit()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # deletar conta
    @classmethod
    def deleteAccount(cls, uid):
        try:
            cls.cur.execute(
                "DELETE FROM users WHERE id=%s", (uid,))

            # executando as mudanças
            cls.conn.commit()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # mudar senha
    @classmethod
    def resetPassword(cls, email, password):
        try:
            cls.cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cls.cur.fetchone()

            # verificando se não foi encontrado o usuário
            if not user:
                return False

            # 'escondendo' a nova senha
            pwd = generate_password_hash(password)

            cls.cur.execute(
                "UPDATE FROM users SET password=%s WHERE id=%s", (pwd, user[0]))

            # executando as mudanças
            cls.conn.commit()

            # encerrando a operação
            cls.cur.close()
            cls.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')
