resp = 'S'
total = qtdProdAcMil = maisBarato = cont = 0
while resp == 'S':
    preco = float(input('Preço:  '))
    nome = input('Nome:  ')
    total += preco
    cont += 1
    if preco > 1000:        
        qtdProdAcMil += 1
    if cont == 1:
        maisBarato = nome
        precoMaisBarato = preco
    elif precoMaisBarato > preco:
        maisBarato = nome
        precoMaisBarato = preco
    resp = input('Quer continuar? [S / N]:  ').strip().upper()[0]
print()
print(f'Total gasto: R$  {total}')
print(f'Produtos acima de R$ 1000,00:  {qtdProdAcMil}')
print(f'Produto mais barato:  {maisBarato}')


