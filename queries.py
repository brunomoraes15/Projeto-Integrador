SQL_INSERIR = """
   INSERT INTO usuario (nome, email) 
   VALUES (?, ?)
            """
            #  cpf, telefone 
            
SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    cpf VARCHAR(11),
    telefone INT,
    endereco VARCHAR(255)
);

"""
SQL_DROP_TABLE = """
DROP TABLE usuario
"""

SQL_INSERIR_REGISTRAR = """
INSERT INTO usuario (email, senha) 
            VALUES (%s, %s)"""

SQL_VERIFICAR_USUARIO = """
"SELECT * FROM usuario
WHERE email = %s AND senha = %s
"""
ALTERAR_NOME = """
UPDATE usuario
SET nome = %s
WHERE email = %s;
"""

DELETAR_USER = """
DELETE FROM usuario
WHERE email = (email);
"""