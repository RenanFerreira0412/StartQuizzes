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
            with self.conn.cursor() as curs:
                curs.execute("SELECT * FROM users WHERE id=%s", (uid,))
                user = curs.fetchone()
                return user
        except psycopg2.Error as e:
            print(f'Erro: {e}')

        self.conn.close()

    # atualizar
    def updateOne(self, uid, name):
        try:
            with self.conn.cursor() as curs:
                curs.execute(
                    "UPDATE users SET name=%s WHERE id=%s", (name, uid))
                # executando as mudanças
                self.conn.commit()
                return True
        except psycopg2.Error as e:
            print(f'Erro: {e}')

        self.conn.close()
