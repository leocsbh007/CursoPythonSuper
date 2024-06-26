-- Criar um banco chamado escola

CREATE DATABASE escola;

-- Criar as tabelas

CREATE TABLE alunos(
    id_aluno INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    idade INT NOT NULL  
);

CREATE TABLE cursos(
    id_curso INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome_curso VARCHAR(200) NOT NULL,
    carga_horaria INT NOT NULL
);

CREATE TABLE matriculas(
    id_matricula INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_curso INT NOT NULL,
    data_matricula DATE NOT NULL
);


ALTER TABLE alunos CHANGE COLUMN id_aluno matricula INT NOT NULL;

ALTER TABLE alunos DROP COLUMN idade;

ALTER TABLE alunos
ADD especialidade VARCHAR(200),
ADD endereco VARCHAR(200);


CREATE TABLE professores(
    matricula_professor INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    especialidade_professor VARCHAR(200),
    endereco_professor VARCHAR(200)
);


ALTER TABLE professores 
MODIFY especialidade_professor VARCHAR(200) NOT NULL;

ALTER TABLE professores 
MODIFY endereco_professor VARCHAR(200) NOT NULL;

ALTER TABLE professores CHANGE COLUMN nome nome_professor VARCHAR(200) NOT NULL;


CREATE TABLE turma(
    identificador INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    horario_inicio TIME NOT NULL,
    dia_semana DAY NOT NULL
);





