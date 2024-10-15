from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from banco import *  # Certifique-se de importar corretamente a classe BancoDeDados

# Inicializando o FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Montagem da pasta estática de arquivos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency para o banco de dados
@app.on_event("startup")
def inicializar():
    global bd
    bd = BancoDeDados(
        host=host,
        dbname=dbname,
        user=db_user,
        password=password,
        port=port
    )
    bd.criar_banco()

# Rota para a página principal
@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para a página de login
@app.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

# Rota para a página de registro (corrigido)
@app.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

# Rota para registrar um novo usuário
@app.post("/post_registrar")
def post_registrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    user = Usuario(
        email=email,
        senha=senha
    )
    
    validador = bd.inserir_usuario_registro(user)
    if validador:
        return RedirectResponse(url="/registrar_recebido", status_code=303)
    else:
        return RedirectResponse(url="/registrar", status_code=303)

# Rota para a página de confirmação de registro
@app.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

# Inicializando o servidor
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)




"""# Main para o menu do Eduardo

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from banco import *
from config import *

# Inicializando as bibliotecas
app = FastAPI()
templates = Jinja2Templates(directory="templates") 

# Montagem da pasta estatica de arquivos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
# settem as configurações de inicialização que preferirem
def inicializar():
    global bd
    bd = Banco_de_Dados(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    bd.criar_banco()

# Rodando as páginas
@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@app.get("/registrar")
def get_registrar(request: Request): 
    return templates.TemplateResponse("/registrar.html", {"request": request})

@app.post("/post_registrar")
def registrar_usuario(
    request: Request,
    email: str = Form(...), 
    senha: str = Form(...)
):
    user = Usuario(
        email=email,
        nome=senha  
    )
    
    validador = bd.inserir_usuario(user)
    if validador:
        return RedirectResponse(url="/registrar_recebido", status_code=303) 
    else:
        return RedirectResponse(url="/registrar", status_code=303)
       
@app.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
"""