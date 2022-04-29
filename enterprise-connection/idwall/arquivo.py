from gerador_data_e_dados import gerar_data, gerar_dados_classificados, definir_tipo_de_dados

empresas = ['Apple', 'Microsoft', 'Facebook', 'Google', 'Amazon', 'Shoppe', 'Pentagono', 'Tim']
tipos_de_dados = definir_tipo_de_dados()

lista = []
for empresa in empresas:
    a = list(gerar_data())
    a[0], a[2] = a[2], a[0]
    b = gerar_dados_classificados()
    variavel = [a, empresa]
    variavel.extend(b)
    lista.append(variavel)

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
                    
                    j += 1

                else:
                    j += 1
                    
            contador -= 1
            ordena_data.sort(reverse=True)
            for r in ordena_data:
                ordem.append(r)


for j in lista:
    print(j)
print()
for c in ordem:
    print(c)

print(len(lista) == len(ordem))