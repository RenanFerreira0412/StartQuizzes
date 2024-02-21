class User:
    """
    classe para representar os usuários do sistema
    """

    def __init__(self, name, email, password, created_at):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_active = True
