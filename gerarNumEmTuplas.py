from random import randint
import random
maior = menor = 0;
n1 = random.randint(0,10)
n2 = random.randint(0,50)
n3 = random.randint(0,50)
tupla = (n1,n2,n3)
print()
print(tupla)

if tupla[0] > tupla[1] and tupla[0] > tupla[2]:
    maior = tupla[0]    
elif tupla[1] > tupla[0] and tupla[1] > tupla[2]:
    maior = tupla[1]
elif tupla[2] > tupla[1] and tupla[2] > tupla[0]:
    maior = tupla[2]
else:
    maior = 'Os número sõo iguais. '

if tupla[0] < tupla[1] and tupla[0] < tupla[2]:
    menor = tupla[0]    
elif tupla[1] < tupla[0] and tupla[1] < tupla[2]:
    menor = tupla[1]
elif tupla[2] < tupla[1] and tupla[2] < tupla[0]:
    menor = tupla[2]
else:
    maior = 'Os número sõ iguais. '

print()
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')



