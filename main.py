from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from banco import *  

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@app.get("/registrar")
def get_registrar(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@app.post("/post_registrar")
def post_registrar(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario = Usuario(
        email=email,
        senha=senha
    )
    
    bd.inserir_usuario_registro(usuario)
    return RedirectResponse(url="/registrar_recebido", status_code=302) 


@app.get("/registrar_recebido")
def post_registrar_recebido(request: Request):
    return templates.TemplateResponse("registrar_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)