from random import randint
import random
pcNum = random.randint(0,10)
print(pcNum)
n = None
while n != pcNum:
    n = int(input('Tente um número: '))
    if n > pcNum:
        print('O número é menor! ')
    else:
        print('O número é maior!')
print()
print(' Acertou! A miserável!!!')