'''
Crie uma classe Pessoa com atributos como nome e idade. Em seguida, crie subclasses
como Estudante e Professor que herdem de Pessoa e adicionem atributos específicos,
como curso para estudantes e disciplina para professores.
'''
from escola import *

aluno = Estudante('Leonardo',29, 'Python Super')
professor = Professor('Jose', 59, "Matematica")

print(aluno.curso)
print(professor.disciplina)
professor.altera_disciplina('Ingles')
print(professor.disciplina)