"""
3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant'ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
"""
from time import sleep

soma_notas_impares = 0
soma_notas_pares = 0

for i in range(1, 50, 2):
    print('\nVocê está digitando a nota dos alunos ÍMPARES')
    soma_notas_impares += int(input(f'Digite a nota pro {i}º aluno da chamada: '))
else:
    print('\nAgora você vai digitar a nota dos alunos pares')
    
for j in range(2, 51, 2):
    print('\nVocê está digitando a nota dos alunos PARES')
    soma_notas_pares += int(input(f'Digite a nota pro {j}º aluno da chamada: '))
else:
    print('\nCalculando a média dos alunos pares e impares...')
    sleep(2)
    
media_impares = soma_notas_impares / 25
media_pares = soma_notas_pares / 25

if media_pares > media_impares:
    print(f'\nA média {media_pares} dos alunos pares foi a maior em comparação com a média {media_impares} dos alunos impares\n')

elif media_pares < media_impares:
    print(f'\nA média {media_impares} dos alunos impares foi a maior em comparação com a média {media_pares} dos alunos pares\n')

else:
    print(f'\nA média {media_pares} dos alunos pares e impares são iguais\n')
