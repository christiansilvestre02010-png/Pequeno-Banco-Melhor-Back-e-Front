O programa inicialmente foi feito em python, porem decidi melhora-lo

Para instalar as bibliotecas digite no terminal:

    pip install -r requirements.txt

Para chamar o programa:
    digite no terminal: 

    python app.py

    em cima do link criado use: Crtl + Click,
    vai abrir na seu navegador padrão.

Para fechar:
    vá no terminal e use: Crtl + C.

templates - Os HTML de cada página do programa;
static 
    css - onde fica os CSS das páginas.
    img - onde fica os icones e a imagem de fundo do Login e Registrar.
    js - onde fica o JavaScript do input moeda presente no Depositar e Sacar.

app.py - O programa principal;
base.py - O programa base, Opcional;
login.py - Onde fica as funcões que abastece tanto o programa base, quanto o principal. Onde ativa o programa base;
requirements.txt - Biblitecas que utilizei e suas versões;
Test.csv - O banco de dados do programa, onde fica o Id, Usuário, Senha e o Saldo;