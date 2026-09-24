from app.data.usuarios_mock import USUARIOS

class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_perfil(self):
        return type(self).__name__

    def conferir_senha(self, senha):
        return self._senha == senha
    
    def pode_favoritar(self): 
        return True

    def pode_publicar(self):
        return False

    def pode_moderar(self):
        return False


from app.models.visitante import Visitante
from app.models.contribuidor import Contribuidor
from app.models.moderador import Moderador

PERFIS = {
    'visitante': Visitante, 
    'contribuidor': Contribuidor, 
    'moderador': Moderador
}

def carregar_usuarios():
    return [PERFIS[usuario['perfil']](usuario['id'], usuario['nome'], usuario['senha']) for usuario in USUARIOS]
