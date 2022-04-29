from gerador_data_e_dados import gerar_data, gerar_dados_classificados, definir_tipo_de_dados



empresas = ['Apple', 'Microsoft', 'Facebook', 'Google', 'Amazon', 'Shoppe', 'Pentagono', 'Tim']
tipos_de_dados = definir_tipo_de_dados()


lista = []
for empresa in empresas:
    a = gerar_data()
    b = gerar_dados_classificados()
    variavel = [empresa, a]
    variavel.extend(b)
    lista.append(variavel)

#### Algoritmo para ordenar pela criticidade dos dados
i = 0
j = 0

for l, k in enumerate(tipos_de_dados):
    
    contador = len(tipos_de_dados)
    while contador > 0:
        
        if j >= len(lista):
            j = 0

        while j < len(lista):

            if i == len(lista) - 1:
                break 

            if lista[j][2] == k and len(lista[j]) - 2 == contador - l:
                lista[j], lista[i] = lista[i], lista[j]
                i += 1
                j += 1
            else:
                j += 1
                 
        contador -= 1 
    
for j in lista:
    print(j)







