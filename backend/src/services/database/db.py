from config import Config
from src.services.database.tables.users import UsersTable
from src.services.database.tables.quizzes import QuizzesTable


class Database:
    """
    tabelas do banco de dados
    """

    conn = Config.get_db_connection()

    # referência as tabelas do banco de dados

    users = UsersTable(conn)
    quizzes = QuizzesTable(conn)
