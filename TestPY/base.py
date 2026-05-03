import pandas as pd
from login import *

df = pd.read_csv('Test.csv')
#Base do programa, programa em python
#Ativar pelo Login.py

Extrato = []

while Inicio:
    Inicio = False
    print('\n', '------------ Caixa ------------')
    print('1 - Ver Saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Extrato')
    print('5 - Sair')
    print('-' * 40) 
    print('--- Escolha uma das opções acima ---')

    Resposta = True
    while Resposta:
        try:
            main = int(input(': '))
            if main in (1, 2, 3, 4, 5):
                Resposta = False
        except ValueError:
            Resposta = True

    if main == 1:
        print(f'\n Seu saldo atual é de R${Saldo:.2f}')

    elif main == 2:
        try:
            Deposito = float(input('Quanto deseja depositar? R$'))
            if Deposito > 0:
                Saldo = Saldo + Deposito
                newSaldo(Saldo, Id)
                print('\n Depósito feito!')
                Extrato.append(f'Depósito: + R${Deposito:.2f}')
            else:
                print('\n Valor não correspondente')
        except ValueError:
            print('\n Valor não correspondente')

    elif main == 3:
        try:
            print(f'Valor diponivel: R${Saldo:.2f}')
            Saque = float(input('Quanto deseja sacar? R$'))
            if Saque > Saldo:
                Precisa = Saque - Saldo
                print(f'\n Saldo insuficiente, falta mais R${Precisa:.2f}')
            else:
                if Saque > 0:
                    Saldo = Saldo - Saque
                    newSaldo(Saldo, Id)
                    Extrato.append(f'Saque: - R${Saque:.2f}')
                print('\n Saque feito!')
        except ValueError:
            print('Valor não correspondente')

    elif main == 4:
        print('--------- Extratos ---------')
        if not Extrato: print('Sem extratos por enquanto')
        for dados in Extrato:
            print(dados)
        print('----------------------------')

    elif main == 5:
        print('Fechando...')
        break
    
    Sn = input('Deseja voltar ao painel pricipal? (S/n): ').capitalize()
    if Sn in ('S', 'Sim'):
        Inicio = True