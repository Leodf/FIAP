

lista = [
    [[1997, 3, 5], 'Apple', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2017, 3, 7], 'Microsoft', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[1999, 4, 13], 'Facebook', 'senha', 'telefone'],
    [[2019, 7, 11], 'Google', 'ajuda de senha', 'nome'],
    [[2000, 2, 25], 'Amazon', 'nome'],
    [[1993, 3, 22], 'Shoppe', 'ajuda de senha', 'nome'],
    [[1996, 1, 2], 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[1991, 2, 11], 'Tim', 'telefone'],
    [[2002, 6, 13], 'Tecsul', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2009, 6, 18], 'SKA', 'senha', 'ajuda de senha', 'telefone', 'email'],
    [[2014, 3, 28], 'Tesla', 'senha', 'ajuda de senha', 'nome'],
    [[2017, 1, 11], 'SpaceX', 'telefone', 'nome', 'email'],
    [[2012, 8, 23], 'China', 'ajuda de senha'],
    [[2004, 5, 11], 'Orkut', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2013, 7, 14], 'Tio da padaria', 'senha'],
    [[2004, 8, 16], 'ze da esquina', 'senha', 'ajuda de senha', 'nome', 'email'],
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