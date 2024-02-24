class User:
    """
    classe para representar os usuários do sistema
    """

    def __init__(self, id, name, email, password, is_active, created_at):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active
        self.created_at = created_at
