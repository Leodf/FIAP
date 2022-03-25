#importação do módulo calc.py
import calc
#solicitando valores ao usuário
while True:
    valor1 = input("Digite um valor: ")
    print('Operadores: + (soma) -(subtração) *(multiplicação) /(divisão)')
    operando = input('digite o operador: ')
    valor2 = input("Digite outro valor: ")
    #armazenando a o valor
    if operando == '+':
        valor3 = calc.somar(valor1, valor2)
        print("A soma é {}".format(valor3))

    elif operando == '-':
        valor3 = calc.subtrair(valor1, valor2)
        print("A subtração é {}".format(valor3))

    elif operando == '*':
        valor3 = calc.multiplicar(valor1, valor2)
        print("A multiplicação é {}".format(valor3))

    elif operando == '/':
        valor3 = calc.dividir(valor1, valor2)
        print("A divisão é {}".format(valor3))

    else:
        print('voçe digitou um operador inválido!')