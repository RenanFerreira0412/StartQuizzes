import psycopg2


class UsersTable:
    """
    classe para gerenciar as operações na tabela users 
    do banco de dados
    """

    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    # OPERAÇÕES CRUD

    # encontrar
    def find(self, uid):
        try:
            self.cur.execute("SELECT * FROM users WHERE id=%s", (uid,))
            user = self.cur.fetchone()
            # encerrando a operação
            self.cur.close()
            self.conn.close()
            return user
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # atualizar
    def updateOne(self, uid, name):
        try:
            self.cur.execute(
                "UPDATE users SET name=%s WHERE id=%s", (name, uid))

            # executando as mudanças
            self.conn.commit()

            # encerrando a operação
            self.cur.close()
            self.conn.close()
        except psycopg2.Error as e:
            print(f'Erro: {e}')
