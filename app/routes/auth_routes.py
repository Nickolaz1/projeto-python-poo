from fastapi import APIRouter, HTTPException

from app.controllers.auth_controller import AuthController

router = APIRouter(prefix='/api/auth', tags=['autenticação'])
controller = AuthController()

@router.post('/login')
def login(nome: str, senha: str):
    usuario = controller.login(nome, senha)
    if usuario is None:
        raise HTTPException(401, 'nome ou senha invalidos')
    return usuario
    
