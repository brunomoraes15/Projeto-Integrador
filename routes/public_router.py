from datetime import date
from utils.cript import *
from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from banco import *  # Certifique-se de que `bd` está acessível

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/indexlog")
def get_root(request: Request):
    return templates.TemplateResponse("indexlog.html", {"request": request})

@router.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@router.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

@router.get("/entrar_recebido")
def post_entrar_recebido(request: Request):
    return templates.TemplateResponse("entrar_recebido.html", {"request": request})

@router.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

from datetime import datetime

@router.post("/post_registrar")
def post_registrar(
    request: Request,
    nome: str = Form(...),
    data_nascimento: date = Form(...),
    email: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    endereco: str = Form(...),
    senha: str = Form(...),
    confirmacao_senha: str = Form(...),
):
    # Validações básicas
    if senha != confirmacao_senha:
        return RedirectResponse("/registrar", status_code=303)

    
    # Criptografar a senha
    senha_hash = cript(senha)
    if isinstance(senha_hash, bytes):
        senha_hash = senha_hash.decode()

    # Criar o objeto Usuario
    novo_usuario = Usuario(
        id=None, 
        nome=nome,
        data_nascimento=data_nascimento,
        email=email,
        cpf=cpf,
        telefone=telefone,
        endereco=endereco,
        senha=senha_hash,
        tipo_usuario="cliente"
    )


    if novo_usuario:
        response = RedirectResponse("/entrar", 303)
        return response
    else:
        response = RedirectResponse("/registrar", 303)
        return response


@router.get("/mapa")
def get_root(request: Request):
    return templates.TemplateResponse("mapa.html", {"request": request})

@router.get("/agenda")
def get_root(request: Request):
    return templates.TemplateResponse("agenda.html", {"request": request})
