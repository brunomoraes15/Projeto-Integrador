from mensagens import *
from encript import *
from fastapi import APIRouter, Form, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from Banco import * 
from ConsultaQuery import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/pacientes")
def get_pacientes(request: Request): 
    usuario_sessao = request.session.get("usuario")
    bd = BancoDeDados()
    if not usuario_sessao:
        response = RedirectResponse("/login")
        msg_erro(response, "Usuário não encontrado. Faça login novamente.")
        return response

    if usuario_sessao.get("tipo_usuario") != "medico":
        response = RedirectResponse("/login")
        msg_erro(response, "Você não possui os privilégios necessários para acessar esta página.")
        return response

    checkups_id = bd.buscar_todos_ids()
    return templates.TemplateResponse("medic/paciente.html", {
        "request": request,
        "checkups_id": checkups_id,
    })

@router.get("/paciente/{id_check}")
def get_checkup(request: Request, id_check: int):
    bd = BancoDeDados()
    usuario_sessao = request.session.get("usuario")

    if not usuario_sessao:
        response = RedirectResponse("/login")
        msg_erro(response, "Usuário não encontrado. Faça login novamente.")
        return response

    if usuario_sessao.get("tipo_usuario") != "medico":
        response = RedirectResponse("/login")
        msg_erro(response, "Você não possui os privilégios necessários para acessar esta página.")
        return response

    checkup_obj = bd.buscar_checkup(id_check)

    if not checkup_obj:
        raise HTTPException(status_code=404, detail="Check-up não encontrado")

    return templates.TemplateResponse("medic/detalhes.html", {"request": request, "checkup": checkup_obj,})

@router.post("/post_check_medico")
def post_checkup_medico(
    request: Request, 
    diagnostico: str = Form(),
    checkup_id: int = Form()):
    
    bd = BancoDeDados() 
    insercao = bd.inserir_diagnostico(checkup_id, diagnostico)
    if insercao:
        response = RedirectResponse("/pacientes", 303)
        msg_sucesso(response, "Diagnóstico enviado com êxito!")
        return response
    else:
        response = RedirectResponse("/paciente/{checkup_id}", 303)
        msg_erro(response, "Erro ao enviar diagnóstico ao sistema")
        return response
