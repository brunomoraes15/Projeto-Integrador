from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Banco import * 
from starlette.middleware.sessions import SessionMiddleware
from routes.public_router import router as public_router
from routes.user_router import router as user_router
from routes.medic_router import router as medic_router

bd = BancoDeDados()
#
bd.criar_checkup()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, 
secret_key="a4cc060da26e3251a72b73e241147adb7e050ac6b979911370744fb6ebbd16d46f420e480b83480f7242347f02688eda8712a7121c4611dc8743d17c607c7589")
app.include_router(public_router)
app.include_router(user_router)
app.include_router(medic_router)

for route in user_router.routes:
        print(f'Rota do Usuario> {route.path}, {route.name}')

for route in public_router.routes:
        print(f'Rota Pública> {route.path}, {route.name}')