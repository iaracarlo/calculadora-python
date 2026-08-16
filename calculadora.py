# CALCULADORA:
print('CÁLCULOS:')
print('1- Adição (+)')
print('2 - Subtração (-)')
print('3 - Multiplicação (*)')
print('4 - Divisão (/)')
print('5 - Tabuada')
op = input('Escolha uma opção: ')

if op == '1':
    x = int(input('Digite o 1o numero: '))
    y = int(input('Digite o 2o numero: '))
    print(f'A soma de {x} + {y} = {x+y}!')
elif op == '2':
    x = int(input('Digite o 1o numero: '))
    y = int(input('Digite o 2o numero: '))
    print(f'A subtração de {x} - {y} = {x-y}!')
elif op == '3':
    x = int(input('Digite o 1o numero: '))
    y = int(input('Digite o 2o numero: '))
    print(f'A multiplicação de {x} * {y} = {x*y}!')
elif op == '4':
    x = int(input('Digite o 1o numero: '))
    y = int(input('Digite o 2o numero: '))
    print(f'A divisão de {x} / {y} = {x/y}!')
elif op == '5':
    numero = int(input('Qual número deseja saber a tabuada? '))
    print(f'TABUADA DO {numero}:')
    for i in range(1,11):
        print(f'{numero} x {i} = {numero*i}')
else:
    print('Opção inválida!')