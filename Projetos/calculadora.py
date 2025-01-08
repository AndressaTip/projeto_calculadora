import math

def calculadora():

    while True:

        print('MINHA PRIMEIRA CALCULADORA!')
        print('----------------------------')
        print('Escolha sua opção: ')
        print('----------------------------')
        print('1 - ADIÇÃO')
        print('2 - SUBTRAÇÃO')
        print('3 - MULTIPLICAÇÃO')
        print('4 - DIVISÃO')
        print('5 - POTÊNCIA')
        print('6 - RAIZ QUADRADA')
        print('----------------------------')
        print('0 - Encerrar.')
        print('----------------------------')

        opcao = input('Digite a opção desejada ou zero para encerrar a calculadora: ')

        if opcao == '0':
            print('Encerrando... até mais!')
            break
        elif opcao not in ['1', '2', '3', '4', '5', '6']:
            print('OPÇÃO INVÁLIDA. Tente novamente.')

        def PedirNumeros():
            if opcao in ['1', '2', '3', '4','5']:
                try:
                    a = float(input('Digite o primeiro número: '))
                    b = float(input('Digite o segundo número: '))
                    return a, b
                except ValueError:
                    print('Valor inválido. Favor digitar apenas números válidos.')
                    print('----------------------------')
            elif opcao == '6':
                a = float(input('Digite um número: '))
                b = a
                return a,b   
            
        a, b = PedirNumeros()

        if opcao == '1':
            res = a + b
            print('ADIÇÃO')
            print('----------------------------')
            print(f'{a} + {b} = {res}')
        elif opcao == '2':
            res = a - b
            print('SUBTRAÇÃO')
            print('----------------------------')
            print(f'{a} - {b} = {res}')
        elif opcao == '3':
            res = a * b
            print('MULTIPLICAÇÃO')
            print('----------------------------')
            print(f'{a} x {b} = {res}')
        elif opcao == '4':
            res = a / b
            print('DIVISÃO')
            print('----------------------------')
            print(f'{a} / {b} = {res}')
        elif opcao == '5':
            res = math.pow(a, b)
            print('Opção selecionada: POTÊNCIA')
            print('----------------------------')
            print(f'{a} ^ {b} = {res}')
        elif opcao == '6':
            res = math.sqrt(a)
            print('Opção selecionada: RAIZ QUADRADA')
            print('----------------------------')
            print(f'√{a} = {res}')

        break

calculadora()