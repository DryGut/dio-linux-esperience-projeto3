#criando um programa para armazenamento em banco de dados

import sqlite3
import os
import io
import socket

class Connect():
  """
  Criando a conexao com o 
  Banco de Dados
    
    Args:
        db_name = nome do banco de dados
  """
  def __init__(self, db_name):

    try:
      #conectando
      self.conn = sqlite3.connect(db_name)
      self.cursor = self.conn.cursor()
      print('Banco: ', db_name)
      self.cursor.execute('SELECT SQLITE_VERSION()')
      self.data = self.cursor.fetchone()
      print("Sqlite version: %s " % self.data)
    
    except sqlite3.Error:
      print('Erro ao abrir o Banco de Dados')
      return False

  def commit_db(self):
    if self.conn:
      self.conn.commit()

  def close_db(self):
    if self.conn:
      self.conn.close()
      print('Conexao Encerrada')

class ClienteDB():
  """ Criando o BD e 
  a respectiva Tabela 
  """
  tb_name = 'banco1'

  def __init__(self):
    """ faz a conexao com o banco de dados"""
    self.db = Connect('banco1.db')
    self.tb_name

  def fecha_conexao(self):
    self.db.close_db()

  def criar_tabela(self, schema_name='/python/tableschema1.sql'):

    print("Criando a Tabela %s... " % self.tb_name)

    try:
      with open(schema_name, 'rt') as f:
        schema = f.read()
        self.db.cursor.executescript(schema)
    except sqlite3.Error:
      print('Aviso: A Tabela ja existe %s' % self.tb_name)
      return False
    print('Tabela criada com Sucesso')

  def inserir_dados(self):
        """inserindo dados dos alunos"""

        self.nome = input('Nome: ').title()
        self.sobrenome = input('Sobrenome: ').title()
        self.endereco = input('Endereco: ').title()
        self.host = socket.gethostname()
        

        try:
            self.db.cursor.execute(
                """
                      INSERT INTO clientes (
                      nome, 
                      sobrenome,
                      endereco,
                      host) 
                      VALUES  (?, ?, ?, ?)
                      """, (self.nome, self.sobrenome, self.endereco, self.host))
            self.db.commit_db()
            print("dados inseridos com sucesso")

        except sqlite3.IntegrityError:
            print("Aviso: Email Invalido.")
            return False

    