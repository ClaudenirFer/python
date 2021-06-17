tot = 0
cont = 0
for c in range(0,6):
    n = int(input('Informe o número: '))
    cont += 1
    if n % 2 == 0:
        tot += n
print(f'O total dos pares foi: {tot}')
print(f'Quantidade de valores: {cont}')