from app.models.contribuidor import Contribuidor

class Moderador(Contribuidor):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha)

    def pode_moderar(self):
        return True