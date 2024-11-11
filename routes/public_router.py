from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from banco import *  # Certifique-se de que `bd` está acessível

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@router.post("/post_registrar")
def post_registrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario = Usuario(
        email=email,
        senha=senha
    )
    
    bd.inserir_usuario_registro(usuario)  # Usa `bd` em vez de `BancoDeDados`
    return RedirectResponse(url="/registrar_recebido", status_code=302)

@router.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

@router.get("/entrar_recebido")
def post_entrar_recebido(request: Request):
    return templates.TemplateResponse("entrar_recebido.html", {"request": request})

@router.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@router.post("/post_entrar")
def post_entrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario_verificado = bd.verificar_usuario(email, senha)
    
    if usuario_verificado:
        return RedirectResponse(url="/entrar_recebido", status_code=302)
    else:
        return RedirectResponse(url="/entrar", status_code=302)


"""from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from banco import *  # certifique-se de que `bd` está acessível

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@router.post("/post_registrar")
def post_registrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario = Usuario(
        email=email,
        senha=senha
    )
    
    #BancoDeDados.inserir_usuario_registro(usuario)  # Usa `bd` em vez de `BancoDeDados`
    return RedirectResponse(url="/registrar_recebido", status_code=302)

@router.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

@router.get("/entrar_recebido")
def post_entrar_recebido(request: Request):
    return templates.TemplateResponse("entrar_recebido.html", {"request": request})

@router.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@router.post("/post_entrar")
def post_entrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario = Usuario(
        email=email,
        senha=senha
    )
    
    usuario_verificado = BancoDeDados.verificar_usuario(usuario.email, usuario.senha)
    
    if usuario_verificado:
        return RedirectResponse(url="/entrar_recebido", status_code=302)
    else:
        return RedirectResponse(url="/entrar", status_code=302)
"""