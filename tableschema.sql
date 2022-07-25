-- Criando a tabela no banco de dados

CREATE TABLE clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50),
  sobrenome VARCHAR(50),
  endereco VARCHAR(100),
  host VARCHAR(50)
);