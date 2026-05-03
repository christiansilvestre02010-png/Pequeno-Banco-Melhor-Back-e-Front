from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = '@key_'
import pandas as pd
from login import *

#Verify(user): {Se existe o user}, {a senha para analisar}
#newSaldo(Saldo, Id): (Muda o saldo no csv)
#criar(newName, newKey): (Cria o usuário no csv)
#Emit(user): {Saldo}, {Id}
#limpar(Valor): (Para o Flask ler os digitos feitos em moeda.js ultilizado no input) {Saldo}

df = pd.read_csv('Test.csv') 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = request.form.get('usuario')
        status, senha = Verify(user)
        if status:
            key = request.form.get('senha')
            if str(senha) == str(key):
                print(f'User {user} logado')
                Saldo, Id = Emit(user)
                session['Usuario'] = user
                session['Id'] = Id
                session['SaldoTotal'] = Saldo
                session['Extratos'] = []

                return redirect(url_for('banco'))
            else: print(f'User: {senha}')
        else: print(f'{user} não existe no banco')
    return render_template('login.html')

@app.route('/Registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        newName = request.form.get('usuario')
        newKey = request.form.get('senha')
        status, senha = Verify(newName)
        if status: return f'Erro, ja tem um usuário com esse nome'
        if not status: 
            criar(newName, newKey)
            print(f'Usuário de nome: {newName}, Criado!')
        
        return redirect(url_for('home'))
    return render_template('registrar.html')

@app.route('/Banco')
def banco():
    Saldo = session.get('SaldoTotal')
    user = session.get('Usuario')
    if user is None: return redirect(url_for('home'))

    return render_template('banco.html', name=user.split()[0], saldo=Saldo)

@app.route('/Depositar', methods=['GET', 'POST'])
def Depositar():
    user = session.get('Usuario')
    if user is None: return redirect(url_for('home'))
    if request.method == 'POST':
        Saldo = session.get('SaldoTotal')
        Id = session.get('Id')
        Valor = request.form.get('Deposito')
        Deposito = limpar(Valor)
        if Deposito > 0:
            resultDepositar = Saldo + Deposito
            session['SaldoTotal'] = Saldo = resultDepositar
            newSaldo(Saldo, Id)
            session['Extratos'].append(f'Depósito: + R${Deposito:.2f}')
            session.modified = True
        else:
            return f'Erro, valor incorreto'
        
        return redirect(url_for('banco'))
    return render_template('depositar.html')

@app.route('/Sacar', methods=['GET', 'POST'])
def Sacar():
    user = session.get('Usuario')
    if user is None: return redirect(url_for('home'))
    if request.method == 'POST':
        Saldo = session.get('SaldoTotal', 0)
        Id = session.get('Id')
        Valor = request.form.get('saque')
        print(Valor)
        Saque = limpar(Valor)
        if Saque > Saldo:
            Precisa = Saque - Saldo
            return f'Erro, Saque maior que o Saldo, faltou R${Precisa}'
        else:
            resultSacar = Saldo - Saque
            session['SaldoTotal'] = Saldo = resultSacar
            newSaldo(Saldo, Id)
            session['Extratos'].append(f'Saque: - R${Saque:.2f}')
            session.modified = True

            return redirect(url_for('banco'))
    return render_template('sacar.html', saldo=session.get('SaldoTotal'))

@app.route('/Extrato')
def Extrato():
    user = session.get('Usuario')
    if user is None: return redirect(url_for('home'))
    Extratos = session.get('Extratos')
    return render_template('extrato.html', extrato_html=Extratos, name=user.split()[0])

if __name__ == '__main__':
    app.run(debug=True)
