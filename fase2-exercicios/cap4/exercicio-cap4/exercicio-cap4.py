"""
# Exercicio 1

while True:
    nota = int(input('Digite a nota: '))

    if nota >= 20 or nota <= 25:
        print('intervalo verdadeiro')
    else:
        print('Intervalo Falso!')
"""
"""
# Exercicio 2
contador = 0
while contador <= 5:
    print(contador)
    contador = contador + 1
"""
"""
# Exercicio 3
for numero in range(1, 21):
    print(numero, end=' ')
"""
"""
# Exercicio 6

numero = 0
resultado = 0
while numero <= 10:
    resultado = 2 * numero
    print(f'2 x {numero} = {resultado}')
    numero = numero + 1
"""
"""
# Exercicio 7
#variável que servirá para receber a opção do usuário
op = -1
#enquanto o usuário não digitar a opção de saída
while op!=5:
    #exibição das opções do menu
    print("SUPER PROGRAMA MARAVILHOSO")
    print("1 - Rodar código 1")
    print("2 - Rodar código 2")
    print("3 - Rodar código 3")
    print("4 - Rodar código 4")
    print("5 - Sair do programa")
    op = int(input("Informe sua opção: "))
    
    #verificação das opções disponíveis
    if op == 1:
        #O que ocorrerá se a opção 1 for selecionada
        print("CÓDIGO 1 RODANDO!")
    elif op == 2:
        #O que ocorrerá se a opção 2 for selecionada
        print("CÓDIGO 2 RODANDO!")
    elif op == 3:
        #O que ocorrerá se a opção 3 for selecionada
        print("CÓDIGO 3 RODANDO!")
    elif op == 4:
        #O que ocorrerá se a opção 3 for selecionada
        print("CÓDIGO 4 RODANDO!")
    elif op == 5:
        #O que ocorrerá se a opção 3 for selecionada
        break
    else:
        print('Digite uma opção válida')
#Quando o looping terminar de rodar, exibir essa mensagem
print("OK! O programa está encerrado...")
"""
# exercicio 9
"""
resultado = 2 + 5 / 2
final = resultado - (resultado * (10/100))
print(resultado)
print(final)
"""
lista = [0,5,10,15,5,10,20]  

print(lista.count(5))

lista = [0,2,4,8,16,32,64,128]  

print(len(lista))