from app.models.usuario import Usuario

class Contribuidor(Usuario):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha)

    def pode_publicar():
        True