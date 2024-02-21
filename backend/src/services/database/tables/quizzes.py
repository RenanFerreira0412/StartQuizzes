import psycopg2


class QuizzesTable:
    """
    classe para gerenciar as operações na tabela quizzes 
    do banco de dados
    """

    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

     # OPERAÇÕES CRUD

    # inserir

    def insertOne(self):
        try:
            pass
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # encontrar
    def find(self):
        try:
            pass
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # atualizar
    def updateOne(self, id):
        try:
            pass
        except psycopg2.Error as e:
            print(f'Erro: {e}')

    # deletar
    def deleteOne(self, id):
        try:
            pass
        except psycopg2.Error as e:
            print(f'Erro: {e}')
