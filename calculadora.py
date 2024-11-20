def calculadora(a,b):
    if(operacao == '+'):
        soma = a+b
        print(f'O resultado de {a} + {b} = {soma}')
    elif(operacao == '-'):
        subtracao = a-b
        print(f'O resultado de {a} - {b} = {subtracao}')
    elif(operacao == '*'):
        multiplicacao = a*b
        print(f'O resultado de {a} x {b} = {multiplicacao}')
    elif(operacao == '/'):
        if b == 0:
            print('Impossível dividir por 0!')
        else:
            divisao = a/b
            print(f'O resultado de {a} / {b} = {divisao}')
    elif(operacao == '^'):
        potencia = a**b
        print(f'O resultado de {a} ^ {b} = {potencia}')



if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    print(f'Olá {nome} seja bem vindo calculadora! \n')

    operacao = None

    n1 = float(input('Digite o primeiro número: '))

    while True:
        operacao = (input('Digite a operação desejada (\'+\', \'-\', \'*\', \'/\', \'^\'): '))
        if operacao == '+'or operacao == '-' or operacao == '*' or  operacao == '/' or operacao == '**':
            break

        print('Operação inválida!\n')

    n2 = float(input('Digite o segundo número: '))

    calculadora(n1,n2)


   


