lista = []

for cont in range (0,10):
    lista.append(float(input('Digite um número real: ')))
    
lista.sort(reverse = True)

print('A lita na ordem inversa é {}!'.format(lista))