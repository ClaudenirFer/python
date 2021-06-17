resp = 'S'

total = nulo = branco = tot1 = tot2 = tot3 = tot4 = totBranco = totNulo= 0

print(''' 
[ 1 ] Chapolin
[ 2 ] Sr Madruga
[ 3 ] kiko
[ 4 ] Brucha do 71
[ 5 ] Nulo
[ 6 ] Branco
''')

while resp == 'S':    
    n = int(input('Digite o número do seu candidato:  '))
    total = total + 1    
    if n == 1:
        tot1 += 1
    elif n == 2:
        tot2 += 1
    elif n == 3:
        tot3 += 1
    elif n == 4:
        tot4 += 1
    elif n == 5:
        totNulo += 1
    elif n == 6:
        totBranco += 1

    resp = input('Deseja votar: [S / N]  ').strip().upper()[0]


porcentNulo = float(totNulo / total * 100)
porcentBranco = float(totBranco / total * 100)
print()

print()
print()
print(f'O total de votos para o Chapolin:  {tot1}')
print(f'O total de votos para o Sr Madruga:  {tot2}')
print(f'O total de votos para o Kiko:  {tot3}')
print(f'O total de votos para a Brucha do 71:  {tot4}')
print(f'Total de votos apurados:  {total}')
print(f'Percentual de votos nulo:  {porcentNulo}%')
print(f'Percentual de votos nulo:  {porcentBranco}%')
