
def calculadora(a,b):
    '''
    função onde se realizam as operações matemáticas entre os dois números
    '''
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
        try:
            divisao = a/b
        except ZeroDivisionError:
            print('Impossível dividir por 0!')
        else:
            print(f'O resultado de {a} / {b} = {divisao}')
    elif(operacao == '^'):
        potencia = a**b
        print(f'O resultado de {a} ^ {b} = {potencia}')


if __name__ == '__main__':

    nome = input('Digite seu nome: ')
    print(f'Olá {nome} seja bem vindo calculadora! \n')
    
    #verificar se os valores são numéricos
    while True:
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            break
        except ValueError:
            print(f'Erro: Valor digitado não é um número.')

    #loop para verificar se a operação digitada é valida
    while True:
        operacao = (input('Digite a operação desejada (\'+\', \'-\', \'*\', \'/\', \'^\'): '))
        if operacao in ['+','-','*','/','**']:
            break

        print('Operação inválida!\n')


    calculadora(n1,n2)


   


