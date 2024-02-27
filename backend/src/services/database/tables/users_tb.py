from ....utils.utils import Utils
from ....models.user import User
import psycopg2


class UsersTable:
    """
    classe para gerenciar as operações na tabela users 
    do banco de dados
    """

    def __init__(self, conn):
        self.conn = conn

    # OPERAÇÕES CRUD

    # encontrar
    def find(self, uid):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute("SELECT * FROM users WHERE id=%s", (uid,))
                    data = curs.fetchone()

                    # dados do usuário
                    user = User(*data).toDict()

            return Utils.sendMessage(200, "Dados carregados com sucesso!", user)
        except psycopg2.Error as e:
            print(f'Erro: {e}')
            return Utils.sendMessage(404, str(e), None)

    # atualizar
    def updateOne(self, uid, name):
        try:
            with self.conn as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "UPDATE users SET name=%s WHERE id=%s", (name, uid))
                    # executando as mudanças
                    conn.commit()

            return Utils.sendMessage(200, "Informação atualizada com sucesso.", None)
        except psycopg2.Error as e:
            print(f'Erro: {e}')
            return Utils.sendMessage(404, str(e), None)
