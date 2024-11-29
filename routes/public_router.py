from datetime import date, datetime
from mensagens import *
from utils.cript import *
from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from banco import * 

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    contexto = {"request": request, "index_ativo": "active"}
    return templates.TemplateResponse("index.html", contexto)

@router.get("/sair")
def get_sair(request: Request):
    request.session.clear()
    response = RedirectResponse("/", 303)
    adicionar_mensagem_info(response, "Você não está mais autenticado.")
    return response

@router.get("/entrar_recebido")
def post_entrar_recebido(request: Request):
    return templates.TemplateResponse("entrar_recebido.html", {"request": request})

@router.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@router.post("/post_entrar")
def post_entrar(
    request: Request, 
    email: str = Form(),
    senha: str = Form()):
    
    banco_de_dados = BancoDeDados()  # Criação da instância
    
    senha_crpt = banco_de_dados.obter_senha_por_email(email)  # Usando a instância para chamar o método
    
    if not senha_crpt:
        response = RedirectResponse("/entrar", 303)
        return response
    
    if not bcrypt.checkpw(senha.encode(), senha_crpt.encode()):
        response = RedirectResponse("/entrar", 303)
        adicionar_mensagem_erro(response, "Credenciais inválidas!")
        return response
    
    usuario = banco_de_dados.obter_dados_por_email(email)
    
    if not usuario:  # Verifica se o usuário existe
        response = RedirectResponse("/entrar", 303)
        adicionar_mensagem_erro(response, "Usuário não encontrado!")
        return response
    
    request.session["usuario"] = {
        "nome": usuario.nome,
        "email": usuario.email, 
        "tipo_usuario": usuario.tipo_usuario
    }
    
    response = RedirectResponse("/", 303)
    adicionar_mensagem_sucesso(response, f"Olá, <b>{usuario.nome}</b>. Você está autenticado!")
    return response



@router.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@router.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

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
    if senha != confirmacao_senha:
        response = RedirectResponse("/registrar", 303)
        adicionar_mensagem_erro(response, "Senha e confirmação de senha não conferem.")
        return response

    senha_crpt = cript(senha)
    if isinstance(senha_crpt, bytes):
        senha_crpt = senha_crpt.decode()
        
    novo_usuario = Usuario(
        id=None, 
        nome=nome,
        data_nascimento=data_nascimento,
        email=email,
        cpf=cpf,
        telefone=telefone,
        endereco=endereco,
        senha=senha_crpt,
        tipo_usuario="cliente"
    )
    if novo_usuario:
        response = RedirectResponse("/entrar", 303)
        adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso! Use suas credenciais para entrar.")
        return response
    else:
        response = RedirectResponse("/registrar", 303)
        adicionar_mensagem_erro(response, "Ocorreu algum problema ao tentar realizar seu cadastro. Tente novamente.")
        return response


@router.get("/mapa")
def get_root(request: Request):
    return templates.TemplateResponse("mapa.html", {"request": request})

@router.get("/agenda")
def get_root(request: Request):
    return templates.TemplateResponse("agenda.html", {"request": request})
