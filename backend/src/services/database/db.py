from config import Config
from src.services.database.tables.users_tb import UsersTable
from src.services.database.tables.quizzes_tb import QuizzesTable


class Database:
    """
    tabelas do banco de dados
    """

    conn = Config.get_db_connection()

    # referência as tabelas do banco de dados
    users = UsersTable(conn)
    quizzes = QuizzesTable(conn)
