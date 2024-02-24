import psycopg2
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash


class Authentication:
    """
    Classe para representar o serviço de autenticação
    """

    def __init__(self):
        self.conn = Config.get_db_connection()

    # receber usuário atual
    def getCurrentUser(self):
        try:
            with self.conn.cursor() as curs:
                curs.execute("SELECT * FROM users WHERE is_active=%s", (True,))
                user = curs.fetchone()
                return user
        except psycopg2.Error as e:
            print(f'Erro ao buscar usuário: {e}')

        self.conn.close()

    # entrar na conta
    def signInWithEmailAndPassword(self, email, password):
        try:
            with self.conn.cursor() as curs:
                curs.execute("SELECT * FROM users WHERE email=%s", (email,))
                user = curs.fetchone()

                if not user or not check_password_hash(user[3], password):
                    return False

                curs.execute(
                    "UPDATE users SET is_active=%s WHERE id=%s", (True, user[0]))

                self.conn.commit()

                return True
        except psycopg2.Error as e:
            print(f'Erro ao fazer login: {e}')

        self.conn.close()

    # criar conta
    def createUserWithEmailAndPassword(self, name, email, password):
        try:
            with self.conn.cursor() as curs:
                pwd = generate_password_hash(password)
                curs.execute(
                    'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, pwd))
                self.conn.commit()
                return True
        except psycopg2.Error as e:
            print(f'Erro ao criar usuário: {e}')

        self.conn.close()

    # desconectar da conta
    def signOut(self, uid):
        try:
            with self.conn.cursor() as curs:
                curs.execute(
                    "UPDATE users SET is_active=%s WHERE id=%s", (False, uid))
                self.conn.commit()

                return True
        except psycopg2.Error as e:
            print(f'Erro ao sair da conta: {e}')

        self.conn.close()

    # deletar conta
    def deleteAccount(self, uid):
        try:
            with self.conn.cursor() as curs:
                curs.execute("DELETE FROM users WHERE id=%s", (uid,))
                self.conn.commit()

                return True
        except psycopg2.Error as e:
            print(f'Erro ao deletar conta: {e}')

        self.conn.close()

    # mudar senha
    def resetPassword(self, email, password):
        try:
            with self.conn.cursor() as curs:
                curs.execute("SELECT * FROM users WHERE email=%s", (email,))
                user = curs.fetchone()

                if not user:
                    return False

                pwd = generate_password_hash(password)
                curs.execute(
                    "UPDATE users SET password=%s WHERE id=%s", (pwd, user[0]))

                self.conn.commit()

                return True
        except psycopg2.Error as e:
            print(f'Erro ao redefinir senha: {e}')

        self.conn.close()
