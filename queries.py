SQL_INSERIR = """
   INSERT INTO usuario (nome, email) 
   VALUES (?, ?)
            """
            #  cpf, telefone 
            
SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255),
    cpf VARCHAR(11),
    telefone INT,
    endereco VARCHAR(255)
);

"""
SQL_DROP_TABLE = """
DROP TABLE usuario
"""

SQL_INSERIR = """
INSERT INTO produto (nome, descricao, estoque, preco, categoria)
VALUES (?, ?, ?, ?, ?)
"""

SQL_INSERIR_REGISTRAR = """
INSERT INTO usuario (email, nome) 
            VALUES (%s, %s)"""

SQL_EXCLUIR = """
DELETE FROM produto
WHERE id = ?;
"""

SQL_OBTER_TODOS = """
SELECT * FROM produto
"""