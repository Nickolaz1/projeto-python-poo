from fastapi import APIRouter, HTTPException

from app.controllers.auth_controller import AuthController

router = APIRouter(prefix='/api/auth', tags=['produtos'])
controller = AuthController()


@router.get('/login')
def login():
    
