
# lista = [
#     ['5/9/2020', 'Apple', 'senha', 'ajuda de senha', 'nome'],
#     ['21/7/2011', 'Microsoft', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
#     ['14/7/2014', 'Facebook', 'senha', 'ajuda de senha', 'telefone'],
#     ['27/4/2006', 'Google', 'senha'],
#     ['29/12/2010', 'Amazon', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
#     [ '3/2/2012', 'Shoppe', 'ajuda de senha'],
#     ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
#     ['17/3/2000', 'Tim', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
# ]

lista = [
    ['21/7/2011', 'Microsoft', 'senha'],
    ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['29/12/2010', 'Amazon', 'senha', 'telefone'],
    ['21/7/2011', 'Microsoft', 'senha'],
    ['14/7/2014', 'Facebook', 'senha', 'ajuda de senha', 'telefone'],
    ['17/3/2000', 'Tim', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
    ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['17/3/2000', 'Tim', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
    ['29/10/2006', 'Pentagono', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    ['14/7/2014', 'Facebook', 'senha', 'ajuda de senha', 'telefone'],
    ['21/7/2011', 'Microsoft', 'senha'],
    ['17/3/2000', 'Tim', 'senha', 'ajuda de senha','telefone', 'nome', 'email'],
]

tipos_de_dados = ['senha', 'ajuda de senha','telefone', 'nome', 'email']
contador = len(tipos_de_dados)

i = 0
j = 0
while True:
    if contador == 0:
        break

    if j >= len(lista):
        j = 0

    while j < len(lista):
        if i == len(lista) - 1:
            break 

        if lista[j][2] == 'senha' and len(lista[j]) - 2 == contador:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
        else:
            j += 1
            
    contador -= 1 
            

for j in lista:
    print(j)