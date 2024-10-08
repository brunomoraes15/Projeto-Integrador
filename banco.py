from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição do modelo de tabela
class User(Base):
    __tablename__ = "users"
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
        )
    
    email = Column(
        String, 
        unique=True, 
        index=True
        )
    
    senha = Column(String)

# Criando a tabela no banco de dados
Base.metadata.create_all(bind=engine)

# Função para criar uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo Pydantic para validação de dados
class UserCreate(BaseModel):
    email: str
    senha: str