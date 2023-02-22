/* Script para criação do banco de dados */
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id integer primary key autoincrement,
    titulo string NOT NULL,
    texto string NOT NULL,
    data_criacao DATETIME DEFAULT NOW
);




