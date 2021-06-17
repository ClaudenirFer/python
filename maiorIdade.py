contMaiorIdade = 0
contMenorIdade = 0
for c in range(7):
    anoNascimento = int(input('Ano de Nascimento: ')) 
    if 2021 - anoNascimento >= 18:
        contMaiorIdade += 1
    if 2021 - anoNascimento < 18:
        contMenorIdade += 1

print(f'Menor de Idade: {contMenorIdade}')
print(f'Maior de Idade: {contMaiorIdade}')