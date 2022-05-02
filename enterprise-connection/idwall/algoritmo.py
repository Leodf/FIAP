

lista = [
    [[2011, 3, 5], 'Apple', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2011, 3, 7], 'Microsoft', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2011, 4, 13], 'Facebook', 'senha', 'telefone'],
    [[2011, 7, 11], 'Google', 'ajuda de senha', 'nome'],
    [[2011, 2, 25], 'Amazon', 'nome'],
    [[2011, 3, 22], 'Shoppe', 'ajuda de senha', 'nome'],
    [[2011, 1, 2], 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2011, 2, 11], 'Tim', 'telefone'],
    [[2011, 6, 13], 'Tecsul', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2011, 6, 18], 'SKA', 'senha', 'ajuda de senha', 'telefone', 'email'],
    [[2011, 3, 28], 'Tesla', 'senha', 'ajuda de senha', 'nome'],
    [[2011, 1, 11], 'SpaceX', 'telefone', 'nome', 'email'],
    [[2011, 8, 23], 'China', 'ajuda de senha'],
    [[2011, 5, 11], 'Orkut', 'senha', 'ajuda de senha'],
    [[2011, 7, 14], 'Tio da padaria', 'senha', 'ajuda de senha'],
    [[2011, 8, 16], 'ze da esquina', 'senha', 'ajuda de senha'],
]

lista_prioridade = ['senha', 'ajuda de senha', 'telefone', 'nome', 'email']

#### Algoritmo para ordenar pela criticidade dos dados

linha = 0
valores_ordenados = []
for indice, valor_prioridade in enumerate(lista_prioridade):

    contador = len(lista_prioridade)

    while contador > 0:
        
            if linha >= len(lista):
                linha = 0

            ordena_data = []
            while linha < len(lista):
                
                if lista[linha][2] == valor_prioridade and len(lista[linha]) - 2 == contador - indice:

                    ordena_data.append(lista[linha])
                    ordena_data.sort(reverse=True)
                    linha += 1
                else:
                    linha += 1
                    
            contador -= 1
            
            for i, valor_linha in enumerate(ordena_data):
                if ordena_data[0][0][1] < ordena_data[i][0][1]:
                    ordena_data[0], ordena_data[i] = ordena_data[i], ordena_data[0]
                    valores_ordenados.append(valor_linha)
                else:
                    valores_ordenados.append(valor_linha)
                    
print()
for k, j in enumerate(valores_ordenados):
    a, b, *resto = j
    print(f'A empresa {b} ficou em {k+1}º lugar, os dados vazados foram {resto} vazou os dados em {a[2]}/{a[1]}/{a[0]}')