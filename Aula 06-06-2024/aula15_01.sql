CREATE DATABASE aula_01;

USE aula_01;

CREATE TABLE pessoas(
    id_pessoa INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE
);


INSERT INTO pessoas (nome, data_nascimento, cpf) VALUES
	('Leonardo Souza', '1978-09-15', '12345678902'),
    ('Joazinho da Couve', '2004-12-30', '23456789125'),
    ('Fulano de Souza Silva', '2004-12-30', '45678912389');

START TRANSACTION;

TRUNCATE TABLE pessoas;

ROLLBACK;

-- Este é o comando
ALTER TABLE pessoas RENAME COLUMN id_pessoa TO matricula;
-- Se a versão for antiga tem que usar o comando abaixo.
ALTER TABLE pessoas CHANGE COLUMN id_pessoa matricula INT NOT NULL;



SELECT 
    nome,
    cpf,
    data_nascimento
FROM 
    pessoas;

DROP TABLE pessoas;


CREATE DATABASE teste;