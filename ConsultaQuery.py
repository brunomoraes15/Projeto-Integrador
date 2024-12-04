from dataclasses import dataclass
from typing import Optional

@dataclass
class Checkup:
    id: Optional[int] = None
    id_usuario: Optional[int] = None
    nome_usuario:Optional[int] = None
    febre: Optional[str] = None
    dorCabeca: Optional[str] = None
    fadiga: Optional[str] = None
    faltaAr: Optional[str] = None
    palpitacoes: Optional[str] = None
    tontura: Optional[str] = None
    perdaApetite: Optional[str] = None
    nausea: Optional[str] = None
    vomito: Optional[str] = None
    perdaPeso: Optional[str] = None
    dorAbdomen: Optional[str] = None
    tosse: Optional[str] = None
    descricaoSintomas: Optional[str] = None
    diagnostico: Optional[str] =  None

SQL_CRIAR_CONSULTA = """
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        nome_usuario TEXT,
        febre TEXT,
        dorCabeca TEXT,
        fadiga TEXT,
        faltaAr TEXT,
        palpitacoes TEXT,
        tontura TEXT,
        perdaApetite TEXT,
        nausea TEXT,
        vomito TEXT,
        perdaPeso TEXT,
        dorAbdomen TEXT,
        tosse TEXT,
        descricaoSintomas TEXT,
        diagnostico TEXT,
        FOREIGN KEY(id_usuario) REFERENCES usuario(id)
    );
    """
SQL_REGISTRAR_CONSULTA = """
        INSERT INTO consultas (
            id_usuario, nome_usuario, febre, dorCabeca, fadiga, faltaAr, palpitacoes, tontura, perdaApetite,
            nausea, vomito, perdaPeso, dorAbdomen, tosse, descricaoSintomas
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

SQL_DELETAR_CONSULTA = """
    DELETE FROM consultas WHERE id = ?;
"""

SQL_CONSULTAR_CHECKUP = """
    SELECT * FROM consultas WHERE id = ?;
"""

SQL_BUSCAR_CONSULTA = """
                SELECT consultas.id, consultas.id_usuario, usuario.nome, consultas.febre, consultas.dorCabeca, consultas.fadiga,
                       consultas.faltaAr, consultas.palpitacoes, consultas.tontura, consultas.perdaApetite,
                       consultas.nausea, consultas.vomito, consultas.perdaPeso, consultas.dorAbdomen, consultas.tosse,
                       consultas.descricaoSintomas, consultas.diagnostico
                FROM consultas
                JOIN usuario ON consultas.id_usuario = usuario.id
                WHERE consultas.id = ?
            """
            
SQL_BUSCAR_TODOS_IDS = """
SELECT id, nome_usuario 
FROM consultas 
WHERE diagnostico IS NULL"""

SQL_BUSCAR_CONSULTA_POR_ID = """SELECT id, nome_usuario FROM consultas WHERE id_usuario = ?"""


SQL_INSERIR_DIAGNOSTICO = """
UPDATE consultas
SET diagnostico = ?
WHERE id = ?
"""