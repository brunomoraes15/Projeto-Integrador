from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/entrar")
def get_entrar(request: Request):
    return template.TemplateResponse("entrar.html", {"request": request})

@app.get("/registrar")
def get_entrar(request: Request):
    return template.TemplateResponse("registrar.html", {"request": request})

@app.post("/post_registrar")
async def registrar_usuario(
    email: str = Form(...), 
    senha: str = Form(...)):
    return RedirectResponse(url="/post_registrar", status_code=303)

"""
@app.post("/post_registro")
def post_cadastro(
    nome:       str = Form(...), 
    user:      str = Form(...), 
    email:  str = Form(...), 
    senha:    str = Form(...), 
    categoria:  str = Form(...)):
    return RedirectResponse(url="/", status_code=303)
"""
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)