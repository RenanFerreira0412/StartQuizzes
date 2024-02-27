
class Utils:
    """
    métodos de ajuda
    """

    # enviar mensagens
    @classmethod
    def sendMessage(self, status, message, data):
        response = {"status": status, "message": message, "data": data}
        return response
