
ordem = []

ordena_data = [
    [[2011, 4, 13], 'Vivo', 'ajuda de senha', 'nome'],
    [[2011, 6, 12], 'Claro', 'ajuda de senha', 'email'],
    [[2011, 5, 12], 'Shoppe', 'ajuda de senha', 'telefone'],
]

for i, valor in enumerate(ordena_data):
    if ordena_data[i][0][1] > ordena_data[0][0][1]:
        ordena_data[i], ordena_data[0] = ordena_data[0], ordena_data[i]

print(ordena_data)

# for r in ordena_data:
#     if len(ordena_data) == 0 or len(ordena_data) == 1:
#         ordem.append(r)
#     else:
#         if r[-1][0][1] > r[0][0][1]:
#             r[-1], r[0] = r[0], r[-1]
#             ordem.append(r)