from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory="templates")


@app.get("/")
def get_root(request: Request):
    return template.TemplateResponse("registrar.html", {"request": request})

@app.get("/entrar")
def get_entrar(request: Request):
    return template.TemplateResponse("entrar.html", {"request": request})

""
@app.post("/post_cadastro")
def post_cadastro(
    nome:       str = Form(...), 
    user:      str = Form(...), 
    email:  str = Form(...), 
    senha:    str = Form(...), 
    categoria:  str = Form(...)):
    return RedirectResponse(url="/", status_code=303)
""
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)