import os
lista = []

def soma(a,b):
    return (a+b)

def subtracao(a,b):
    return (a-b)

def divisao(a,b):
    return (a/b)

def multiplicacao(a,b):
    return (a*b)

def sairdacalculadora ():
    print("Programa finalizado") 
    for c in lista:
        print(c)

escolha = 0
while escolha != 5:
    print('Digite 1 para soma')
    print('Digite 2 para subtração')
    print('Digite 3 para divisão')
    print('Digite 4 para multiplicação')
    print('Digite 5 para sair da calculadora\n')

    escolha = int(input('Escolha uma operação: '))
    if escolha == 1:
        num = int(input("Digite o primeiro número"))
        num2 = int(input("Digite o segundo número"))
        res = soma(num, num2)
        os.system("cls")
        print(f"O resultado é {res}")
    
    elif escolha == 2:
        num = int(input("Digite o primeiro número"))
        num2 = int(input("Digite o segundo número"))
        res = subtracao(num, num2)
        os.system("cls")
        print(f"O resultado é {res}")
    
    elif escolha == 3:
        num = int(input("Digite o primeiro número"))
        num2 = int(input("Digite o segundo número"))
        res = divisao(num, num2)
        os.system("cls")
        print(f"O resultado é {res}")
    
    elif escolha == 4:
        num = int(input("Digite o primeiro número"))
        num2 = int(input("Digite o segundo número"))
        res = multiplicacao(num, num2)
        os.system("cls")
        print(f"O resultado é {res}")
    
    elif escolha == 5:
        sairdacalculadora()
    else:
        print("Opção invalida")
