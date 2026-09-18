from app.models.usuario import Usuario

class Visitante(Usuario):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha)