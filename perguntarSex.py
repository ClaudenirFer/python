resp = 'S'
pessoa = homem = mulher = 0
while resp == 'S':
    idade = int(input('Idade: '))
    sexo = input('Informe o sexo: ').strip().upper()[0]
    if idade > 18:
        pessoa += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = input('Quer continuar? [S / N]:  ').strip().upper()[0]
    print()
print(f'Quantidade pessoas têm mais de 18 anos:  {pessoa} pessoas')
print(f'Homens cadastrados:  {homem} homens')
print(f'Mulheres cadastradas:  {mulher} mulheres')
