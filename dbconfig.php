<?php

$db = new SQLite3('banco.db');

$sql = 'CREATE TABLE clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50),
  sobrenome VARCHAR(50),
  endereco VARCHAR(100),
  host VARCHAR(50)
)';
$db->exec($sql);