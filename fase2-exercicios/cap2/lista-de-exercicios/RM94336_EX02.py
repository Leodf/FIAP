"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
"""

dias_da_semana = ['segunda-feira','terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
voto = []

for i in dias_da_semana:
    informe = input(f'\ninforme quantos votos {i} ganhou: ')
    voto.append(int(informe))

for j, valor in enumerate(voto):
    if valor == max(voto):
        print(f'\n{dias_da_semana[j]} é o melhor dia para fazer Live de acordo com a turma\n')
        break


