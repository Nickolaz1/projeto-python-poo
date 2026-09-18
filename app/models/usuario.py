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
    
    def pode_favoritar(): 
        True

    def pode_publicar():
        False

    def pode_moderar():
        False

def carregar_usuarios():
    return [Produto(u['id'], u['nome'], u['senha']) for u in USUARIOS]
