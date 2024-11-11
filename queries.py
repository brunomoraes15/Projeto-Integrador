
SQL_INSERIR = """
   INSERT INTO usuario (nome, email) 
   VALUES (?, ?)
"""

SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    cpf TEXT,
    telefone INTEGER,
    endereco TEXT
);
"""

SQL_DROP_TABLE = """
DROP TABLE IF EXISTS usuario
"""

SQL_INSERIR_REGISTRAR = """
INSERT INTO usuario (email, senha) 
VALUES (?, ?);
"""

SQL_VERIFICAR_USUARIO = """
SELECT * FROM usuario
WHERE email = ? AND senha = ?
"""

ALTERAR_NOME = """
UPDATE usuario
SET nome = ?
WHERE email = ?;
"""

DELETAR_USER = """
DELETE FROM usuario
WHERE email = ?;
"""
