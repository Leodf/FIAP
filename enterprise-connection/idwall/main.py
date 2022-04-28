import random

def gerar_dados_classificados():
    
    inteiro = random.randint(1, len(tipos_de_dados))
    dados_aleatorios = random.sample(tipos_de_dados, k=inteiro)
    dados_aleatorios.sort()

    dados = []
    for i in dados_aleatorios:
        for j in i:
            if type(j) is str:
                dados.append(j)

    return dados


def gerar_data():
    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    ano = random.randint(1990, 2022)

    return f'{dia}/{mes}/{ano}'

tipos_de_dados = [[0, 'senha'], [1, 'ajuda de senha'], [2, 'telefone'], [3, 'nome'], [4,'email'],]
empresas = ['Apple', 'Microsoft', 'Facebook', 'Google', 'Amazon', 'Shoppe', 'Pentagono', 'Tim']

lista = []
for empresa in empresas:
    a = gerar_data()
    b = gerar_dados_classificados()
    variavel = [empresa, a]
    variavel.extend(b)
    lista.append(variavel)


for i in lista:
    print(i)







