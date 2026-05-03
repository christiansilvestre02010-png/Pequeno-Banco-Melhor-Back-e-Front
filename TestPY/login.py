import pandas as pd

df = pd.read_csv('Test.csv')

def limpar(Valor):
    a = Valor.replace('R$ ', '').replace('.', '').replace(',', '.')
    b = float(a)
    return b

def Verify(user):
    if user in df['Usuário'].values:
        senha = df.loc[df['Usuário'] == user, 'Senha'].item()
        verUser = True
    else:
        verUser = False
        senha = None
    return verUser, senha

def Emit(user):
    global df
    Id = df.loc[df['Usuário'] == user, 'Id'].item()
    Saldo = int(df.loc[(df['Usuário'] == user) & (df['Id'] == Id), 'Saldo'].item())
    return Saldo, Id

def newSaldo(Saldo, Id):
    global df
    df.loc[df['Id'] == Id, 'Saldo'] = int(Saldo)
    df.to_csv('Test.csv', index=False)

def criar(newName, newKey):
    global df
    newId = df['Id'].max() + 1
    newUser = {'Id': newId, 'Usuário': newName, 'Senha': newKey, 'Saldo': 1000}
    df = pd.concat([df, pd.DataFrame([newUser])], ignore_index=True)
    df.to_csv('Test.csv', index=False)

Login = Inicio = False 
#Deixar em true para ativar o programa base
#Deixar em false para ativar o programa site
Registrar = add = False

while Login:
    print('\n', '------------- Login ------------')
    print('Digite X para sair')
    print('Digite R se não tiver login')
    print('Qual o nome de usuário?')
    user = input(': ')
    
    if user in ('r', 'R'): Registrar = True
    elif user in ('x', 'X'): break
    else:
        status, senha = Verify(user)
        if status == True:
            print('Qual a senha?')
            key = input(': ')
            if str(senha) == str(key):
                print('Acesso permitido!')
                Saldo, Id = Emit(user)
            else:
                print('Senha errada')
            Login = False
            Inicio = True
        else:
            print('Nome de Usuário não encontrado')

    while Registrar:
        print('\n', '---------- Registro ----------')
        print('Digite X para sair')
        print('Qual vai ser o nome de usuário?')
        newName = input(': ')

        newSenha = True
        while newSenha:
            try:
                print('Qual vai ser a senha? (6 digitos numéricos)')
                newKey = input(': ')

                if not (len(newKey) == 6):
                    print('Senha só pode conter 6 números')
                else:
                    newSenha = False
                    print('Usuario criado!')
                    criar(newName, newKey)
                    Registrar = False
            except ValueError:
                print('Senha só pode conter números')
