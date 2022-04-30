from gerador_data_e_dados import gerar_data, gerar_dados_classificados, definir_tipo_de_dados


empresas = ['Apple', 'Microsoft', 'Facebook', 'Google', 'Amazon', 'Shoppe', 'Pentagono', 'Tim', 'Tecsul', 'SKA', 'Tesla', 'SpaceX', 'China', 'Orkut', 'Tio da padaria', 'ze da esquina']

lista = []
for empresa in empresas:
    a = list(gerar_data())
    a[0], a[2] = a[2], a[0]
    b = gerar_dados_classificados()
    variavel = [a, empresa]
    variavel.extend(b)
    lista.append(variavel)

#### Algoritmo para ordenar pela criticidade dos dados
lista_prioridade = definir_tipo_de_dados()

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







