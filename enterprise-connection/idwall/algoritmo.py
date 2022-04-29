

lista = [
    [[2022, 7, 10], 'Microsoft', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2021, 6, 11], 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    [[2011, 5, 12], 'Shoppe', 'ajuda de senha', 'telefone'],
    [[2011, 6, 12], 'Claro', 'ajuda de senha', 'email'],
    [[2011, 4, 13], 'Vivo', 'ajuda de senha', 'nome'],
    [[1995, 3, 14], 'Amazon', 'senha', 'telefone'],
    [[2011, 2, 15], 'Tecsul', 'senha'],
]

lista_prioridade = ['senha', 'ajuda de senha', 'telefone', 'nome', 'email']

linha = 0
ordem = []
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
            
            for valor_linha in ordena_data:
                ordem.append(valor_linha)
                    

for i in lista:
    print(i)

print()

for j in ordem:
    print(j)

print(len(lista) == len(ordem))