

""" lista = [
    ['5/9/2020', 'Apple', 'senha', 'ajuda de senha', 'nome'],
    ['21/7/2011', 'Microsoft', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    ['14/7/2014', 'Facebook', 'senha', 'ajuda de senha', 'telefone'],
    ['27/4/2006', 'Google', 'senha'],
    ['29/12/2010', 'Amazon', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [ '3/2/2012', 'Shoppe', 'ajuda de senha'],
    ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['17/3/2000', 'Tim', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
] """

""" lista = [
    ['21/7/2011', 'Microsoft', 'senha'],
    ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['29/12/2010', 'Amazon', 'senha', 'telefone'],
    ['21/7/2011', 'Tecsul', 'senha'],
    ['14/7/2014', 'Facebook', 'senha', 'ajuda de senha', 'telefone'],
    ['17/3/2000', 'Tim', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
    ['29/10/2006', 'Vivo', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['17/3/2000', 'Claro', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
    ['29/10/2006', 'Orkut', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['14/7/2014', 'Twiter', 'senha', 'ajuda de senha', 'telefone'],
    ['21/7/2011', 'CNN', 'senha'],
    ['17/3/2000', 'Band', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
] """


lista = [
    [[2022, 7, 10], 'Microsoft', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2021, 6, 11], 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    [[2011, 5, 12], 'Shoppe', 'ajuda de senha', 'telefone'],
    [[2011, 6, 12], 'Claro', 'ajuda de senha', 'email'],
    [[2011, 4, 13], 'Vivo', 'ajuda de senha', 'nome'],
    [[1995, 3, 14], 'Amazon', 'senha', 'telefone'],
    [[2011, 2, 15], 'Tecsul', 'senha'],
]

tipos_de_dados = ['senha', 'ajuda de senha', 'telefone', 'nome', 'email']

i = 0
j = 0

ordem = []
for l, k in enumerate(tipos_de_dados):
    
    contador = len(tipos_de_dados)
    while contador > 0:
        
            if j >= len(lista):
                    j = 0

            ordena_data = []
            while j < len(lista):
                
                if lista[j][2] == k and len(lista[j]) - 2 == contador - l:
                    d = lista[j]
                    ordena_data.append(d)
                    ordena_data.sort(reverse=True)
                    j += 1
                else:
                    j += 1
                    
            contador -= 1
            
            for r in ordena_data:
                if len(ordena_data) == 0 or len(ordena_data) == 1:
                    ordem.append(r)
                else:
                    if r[-1][0][1] > r[0][0][1]:
                        r[-1], r[0] = r[0], r[-1]
                        ordem.append(r)
                    

for j in lista:
    print(j)
print()
for c in ordem:
    print(c)

print(len(lista) == len(ordem))