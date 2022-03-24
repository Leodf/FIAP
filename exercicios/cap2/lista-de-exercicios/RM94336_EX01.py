"""
1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
Basic -- 30%
Silver -- 20%
Gold -- 10%
Platinum -- 5%
"""
print('#'*50)
print('Programa de calculo de bonus pelo tipo de cliente')
print('#'*50)
assinatura = input('Digite o tipo de assinatura do cliente: ')
assinatura.capitalize()
print('Opçoes: Basic - Silver - Gold - Platinum')
