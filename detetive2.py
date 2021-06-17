lista = []
for i in range(0,5):
    lista[i] = 'Você telefonou para a vítima? '
    tel = input('Você telefonou para a vítima? ').strip().upper()[0]
    local = input('Você esteve no local do crime? ').strip().upper()[0]
    moraP = input('Você mora perto da vítima? ').strip().upper()[0]
    divida = input('Você devia para a vítima? ').strip().upper()[0]
    trab = input('Você já trabalhou com a vítima? ').strip().upper()[0]

print()
print('=' *  77)
print('\n')

c = 0
if tel == 'S':
  c += 1
if local == 'S':
  c += 1
if moraP == 'S':
  c += 1
if divida == 'S':
  c += 1
if trab == 'S':
  c += 1
 
resposta = ""
if c == 2:
  # print('Classificação:  Suspeito')
  resposta = 'SUPEITO'
elif c >= 3 and c <= 4:
  # print('Classificação:  Cúmplice')
  resposta = 'CÚMPLICE'
elif c == 5:
  # print('Classificação: Assassino')
  resposta = 'ASSASSINO'
else:
  # print('Classificação:  Inocente')
  resposta = 'INOCENTE'

espacoEsq = int((77 - (len(resposta)+len('classificação:  ')))/2)
print(' ' * espacoEsq + ' CLASSIFICAÇÃO: ' + resposta)
print('\n')
print('=' *  77)

