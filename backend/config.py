from dotenv import dotenv_values
import psycopg2


class Config(object):
    """
    Confihuração com o banco de dados
    """

    @classmethod
    def get_db_connection(cls):
        # dados do arquivo .env
        config = dotenv_values(".env")

        # conexão com o banco de dados
        conn = psycopg2.connect(
            host=config['HOST'],
            database=config['DATABASE'],
            user=config['USER'],
            password=config['PASSWORD']
        )
        return conn
