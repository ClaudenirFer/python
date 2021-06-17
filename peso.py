
maior = menor = 0
for c in range (0,5):      
    n = int(input(f'Informe o peso da pessoa:  '))
    if c == 1:
        maior = menor = n        
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n    
print(f'Maior: {maior}')
print(f'Menor: {menor}')




