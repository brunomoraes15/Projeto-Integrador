from datetime import date
from mensagens import *
from encript import *
from fastapi import APIRouter, Form, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from Banco import * 
from ConsultaQuery import *

# Rotas relacionadas a autenticação do usuário
# e a sessão

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/perfil")
def get_perfil(request: Request): 
    usuario_sessao = request.session.get("usuario")

    if not usuario_sessao or "email" not in usuario_sessao:
        response = RedirectResponse("/login", 303)
        msg_erro(response, "Você precisa estar autenticado para acessar o perfil.")
        return response

    email = usuario_sessao["email"]
    
    bd = BancoDeDados()
    usuario = bd.obter_dados_por_email(email)
    
    if not usuario:
        response = RedirectResponse("/login", 303)
        msg_erro(response, "Usuário não encontrado. Faça login novamente.")
        return response
    
    return templates.TemplateResponse("/user/perfil.html", {
        "request": request,
        "usuario": usuario
    })

@router.get("/perfil_editar", response_class=HTMLResponse)
def carregar_edicao(request: Request, bd: BancoDeDados = Depends(BancoDeDados)):
    sessao = request.session.get("usuario")
    if not sessao:
        raise HTTPException(status_code=401, detail="Usuário não autenticado. Por favor, faça login.")
    
    try:
        usuario_dados = bd.buscar_usuario(sessao["email"])
        if not usuario_dados:
            raise HTTPException(status_code=404, detail="Usuário não encontrado. Verifique suas credenciais.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados do usuário: {str(e)}")
    
    return templates.TemplateResponse("user/perfil_edit.html", {"request": request, "usuario": usuario_dados})

@router.post("/post_editar")
def editar_perfil(
    request: Request,
    email: str = Form(...),
    nome: str = Form(...),
    data_nascimento: date = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    endereco: str = Form(...),
    senha: str = Form(None),
    
):
    try:
        usuario_sessao = request.session.get("usuario")
        
        bd = BancoDeDados()  
    
        usuario_atualizado = Usuario(
            id=usuario_sessao["id"],
            nome=nome,
            data_nascimento=data_nascimento,
            email=email,
            cpf=cpf,
            telefone=telefone,
            endereco=endereco,
            senha=cript(senha),
            tipo_usuario=usuario_sessao["tipo_usuario"]
        )
        
        sucesso = bd.atualizar_usuario(usuario_atualizado)

        if sucesso:
            request.session["usuario"] = {
                "id": usuario_atualizado.id,
                "nome": usuario_atualizado.nome,
                "data_nascimento": usuario_atualizado.data_nascimento.strftime('%Y-%m-%d'),  
                "email": usuario_atualizado.email,
                "cpf": usuario_atualizado.cpf,
                "telefone": usuario_atualizado.telefone,
                "endereco": usuario_atualizado.endereco,
                "tipo_usuario": usuario_atualizado.tipo_usuario
            }
            
            response = RedirectResponse("/perfil", status_code=303)
            msg_sucesso(response, "Perfil atualizado com sucesso!")
            return response
        else:
            raise Exception("Erro ao atualizar o usuário no banco de dados.")
    
    except Exception as e:
        print(f"Erro ao atualizar perfil: {e}")
        response = RedirectResponse("/perfil_editar", status_code=303)
        msg_erro(response, "Ocorreu um erro ao atualizar o perfil. Tente novamente.")
        return response


@router.post("/excluir")
def excluir_perfil(request: Request):
    usuario_sessao = request.session.get("usuario")
    
    if not usuario_sessao or "id" not in usuario_sessao:
        raise HTTPException(status_code=401, detail="Usuário não autenticado ou sessão inválida.")

    id_usuario = usuario_sessao["id"]
    
    try:
        bd = BancoDeDados() 

        sucesso = bd.deletar_usuario(id_usuario)
        
        if sucesso:
            request.session.clear()
            response = RedirectResponse("/", status_code=303)
            msg_sucesso(response, "Perfil excluído com sucesso.")
            return response
        else:
            raise Exception("Erro ao excluir o perfil no banco de dados.")
    
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
        response = RedirectResponse("/perfil", status_code=303)
        msg_erro(response, "Ocorreu um erro ao excluir o perfil. Tente novamente.")
        return response


@router.post("/post_checkup")
def post_checkup(
    request: Request,
    febre: str = Form(...),
    dorCabeca: str = Form(...),
    fadiga: str = Form(...),
    faltaAr: str = Form(...),
    palpitacoes: str = Form(...),
    tontura: str = Form(...),
    perdaApetite: str = Form(...),
    nausea: str = Form(...),
    vomito: str = Form(...),
    perdaPeso: str = Form(...),
    dorAbdomen: str = Form(...),
    tosse: str = Form(...),
    descricaoSintomas: str = Form(None),
):
    try:
        usuario_sessao = request.session.get("usuario")
        
        if not usuario_sessao:
            raise HTTPException(status_code=403, detail="Usuário não autenticado.")
        
        bd = BancoDeDados() 

        checkup_novo = Checkup(
            id_usuario=usuario_sessao.get("id"), 
            nome_usuario=usuario_sessao.get("nome"),
            febre=febre,
            dorCabeca=dorCabeca,
            fadiga=fadiga,
            faltaAr=faltaAr,
            palpitacoes=palpitacoes,
            tontura=tontura,
            perdaApetite=perdaApetite,
            nausea=nausea,
            vomito=vomito,
            perdaPeso=perdaPeso,
            dorAbdomen=dorAbdomen,
            tosse=tosse,
            descricaoSintomas=descricaoSintomas
        )

        sucesso = bd.registrar_checkup(checkup_novo)

        if sucesso:
            response = RedirectResponse("/", status_code=303)
            msg_sucesso(response, "Check-up registrado com sucesso! Aguarde seu diagnóstico")
            return response
        else:
            raise Exception("Erro ao registrar o check-up no banco de dados.")
    
    except Exception as e:
        print(f"Erro ao registrar check-up: {e}")
        response = RedirectResponse("/form_checkup", status_code=303)
        msg_erro(response, "Ocorreu um erro ao registrar o check-up. Tente novamente.")
        return response
    
@router.get("/diagnostico")
def get_diagnostico(request: Request):

    usuario_sessao = request.session.get("usuario")
    bd = BancoDeDados()

    if not usuario_sessao:
        response = RedirectResponse("/login")
        msg_erro(response, "Faça login para acessar seus diagnósticos")
        return response

    try:
        
        diagnostico_id = bd.buscar_consultas_por_ids(usuario_sessao.get("id"))
        
        if not diagnostico_id:
        
            response = RedirectResponse("/")
            msg_erro(response, "Nenhum diagnóstico encontrado para sua conta.")
            return response
        
        
        return templates.TemplateResponse("user/diagnostico.html", {
            "request": request,
            "diagnostico_id": diagnostico_id,
        })
    except Exception as e:
        
        response = RedirectResponse("/erro")
       
@router.get("/diagnostico/{id_check}")
def get_checkup(request: Request, id_check: int):
    bd = BancoDeDados()
    usuario_sessao = request.session.get("usuario")

    if not usuario_sessao:
        response = RedirectResponse("/login")
        msg_erro(response, "Usuário não encontrado. Faça login novamente.")
        return response


    checkup_obj = bd.buscar_checkup(id_check)

    if not checkup_obj:
        raise HTTPException(status_code=404, detail="Check-up não encontrado")

    return templates.TemplateResponse("user/diagnostico_detalhes.html", {"request": request, "checkup": checkup_obj,})