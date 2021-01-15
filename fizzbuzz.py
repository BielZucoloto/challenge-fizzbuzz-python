print('------------DESAFIO FIZZBUZZ------------\n')
valor = int(input('Informe o numero de vezes para contar: '))
for x in range(1,valor+1):
    if (x % 3 == 0) and (x % 5 == 0):
        print('fizzbuzz')
    elif (x % 3 == 0):
        print('fizz')
    elif (x % 5 == 0):
        print('buzz')
    else: 
        print(x)