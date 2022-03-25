

while True:
    nota = int(input('Digite a nota: '))

    if nota > 10 or nota < 0:
        print('Intervalo Falso!')
        continue
    else:
        print('Intervalo verdadeiro!')
        break

"""
for i in range(0, 11, 2):
    print(i, end=" ")
"""