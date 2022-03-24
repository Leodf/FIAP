"""
1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
Basic -- 30%
Silver -- 20%
Gold -- 10%
Platinum -- 5%
"""

print()
cabecalho = ' Programa de calculo de bonus pelo tipo de cliente '
print('#'*100, f'\n{cabecalho:#^100}')
print('#'*100,'\n')
opcoes = 'Opçoes de assinatura: Basic (30%) - Silver (20%) - Gold (10%) - Platinum (5%)\n'
print(opcoes.center(100))

assinatura = input('Digite o tipo de assinatura do cliente: \n')
a = assinatura.capitalize()
faturamento = input('Digite o faturamento anual do cliente: \n')
f = float(faturamento)

if a == 'Platinum':
    bonus = f * 0.05
    print(f'O cliente tem a assinatura {a}, faturou no ano R$ {f:.2f} e seu bonus é de R$ {bonus:.2f}')

elif a == 'Gold':
    bonus = f * 0.1
    print(f'O cliente tem a assinatura {a}, faturou no ano R$ {f:.2f} e seu bonus é de R$ {bonus:.2f}')

elif a == 'Silver':
    bonus = f * 0.2
    print(f'O cliente tem a assinatura {a}, faturou no ano R$ {f:.2f} e seu bonus é de R$ {bonus:.2f}')

elif a == 'Basic':
    bonus = f * 0.3
    print(f'O cliente tem a assinatura {a}, faturou no ano R$ {f:.2f} e seu bonus é de R$ {bonus:.2f}')

else:
    print('Você digitou uma assinatura não existente')

print()    